"""Validate a brain/ directory against the framework schemas and regenerate brain/index.yaml.

Usage: python schemas/validate.py <brain_dir> [--today YYYY-MM-DD] [--check]
  --check   validate only; do not rewrite index.yaml
Not read: archive/, passes/ (Learn working files) and .applier.lock.
Requires: jsonschema, pyyaml.
"""
import argparse
import calendar
import datetime as dt
import json
import pathlib
import re
import sys

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

SCHEMA_DIR = pathlib.Path(__file__).resolve().parent
COMPONENT_DIRS = {
    "lens": "LENS",
    "record": "REC",
    "business-understanding": "BU",
    "beliefs": "BEL",
    "reasoning-patterns": "RP",
    "editorial": "ED",
}
CANDIDATES = {
    "LENS": ["lens-deliverable"],
    "REC": ["record-artifact", "tool-contract", "source-authority"],
    "BU": ["concept", "metric-definition", "normality", "dependency-link"],
    "BEL": ["belief", "story-thread"],
    "RP": ["inquiry-chain", "judgment-rule"],
    "ED": ["editorial-rule"],
}
GOVERNED = {"BU", "BEL", "RP", "ED"}
DAYS = {"d": 1, "w": 7, "m": 30, "q": 91, "y": 365}
ULID_RE = re.compile(r"^[0-9A-HJKMNP-TV-Z]{26}$")


def load_validators():
    schemas = {p.name.removesuffix(".schema.json"): json.loads(p.read_text()) for p in SCHEMA_DIR.glob("*.schema.json")}
    registry = Registry().with_resources((f"{n}.schema.json", Resource.from_contents(s)) for n, s in schemas.items())
    return {n: Draft202012Validator(s, registry=registry) for n, s in schemas.items()}


def load_yaml(path):
    with path.open() as f:
        return yaml.safe_load(f)


def period_end(value):
    if value is None:
        return None
    value = str(value)
    if m := re.fullmatch(r"(\d{4})-Q([1-4])", value):
        year, month = int(m[1]), int(m[2]) * 3
    elif m := re.fullmatch(r"(\d{4})-(\d{2})", value):
        year, month = int(m[1]), int(m[2])
    elif re.fullmatch(r"\d{4}", value):
        year, month = int(value), 12
    else:
        return dt.date.fromisoformat(value)
    return dt.date(year, month, calendar.monthrange(year, month)[1])


def window_days(window):
    return int(window[:-1]) * DAYS[window[-1]]


def relevance(entry, today, default_window):
    end = period_end(entry.get("valid_to"))
    if end and end < today:
        return "historical"
    confirmed = dt.date.fromisoformat(str(entry["last_confirmed"]))
    window = entry.get("review_window") or default_window
    return "current" if (today - confirmed).days <= window_days(window) else "stale"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("brain_dir", type=pathlib.Path)
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    brain = args.brain_dir
    validators = load_validators()
    errors = []

    config = load_yaml(brain / "config.yaml") or {}
    levels = config.get("sensitivity_levels") or []
    default_window = config.get("review_window", "1q")

    entries = {}
    known_ids = set()
    for folder, prefix in COMPONENT_DIRS.items():
        for path in sorted((brain / folder).glob("*.yaml")):
            data = load_yaml(path)
            rel = path.relative_to(brain)
            if not isinstance(data, dict) or not str(data.get("id", "")).startswith(prefix + "-"):
                errors.append(f"{rel}: id must start with {prefix}-")
                continue
            failures = {}
            kind = None
            for name in CANDIDATES[prefix]:
                errs = sorted(validators[name].iter_errors(data), key=lambda e: list(e.path))
                if not errs:
                    kind = name
                    break
                failures[name] = errs
            if kind is None:
                best = min(failures, key=lambda n: len(failures[n]))
                errs = failures[best]
                # A failed $ref drops its annotations, so unevaluatedProperties then flags valid header fields too.
                errs = [e for e in errs if e.validator != "unevaluatedProperties"] or errs
                errors += [f"{rel} (as {best}): {e.json_path} {e.message}" for e in errs[:5]]
                known_ids.add(data["id"])
                continue
            if data["id"] in entries:
                errors.append(f"{rel}: duplicate id {data['id']}")
            entries[data["id"]] = (kind, data, rel)
    known_ids |= set(entries)

    for ledger in sorted((brain / "beliefs" / "ledger").glob("*.yaml")):
        data = load_yaml(ledger)
        rel = ledger.relative_to(brain)
        errors += [f"{rel}: {e.json_path} {e.message}" for e in validators["evidence-ledger"].iter_errors(data)]
        if isinstance(data, dict):
            if ledger.stem != data.get("belief"):
                errors.append(f"{rel}: file name must equal its belief id")
            if data.get("belief") not in known_ids:
                errors.append(f"{rel}: belief {data.get('belief')} not found")

    proposal_dirs = [brain / "proposals", brain / "proposals" / "pending", brain / "proposals" / "rejected"]
    for prop in sorted(p for d in proposal_dirs for p in d.glob("*.yaml")):
        rel = prop.relative_to(brain)
        if not ULID_RE.match(prop.stem):
            errors.append(f"{rel}: file name must be a ULID")
        errors += [f"{rel}: {e.json_path} {e.message}" for e in validators["proposal"].iter_errors(load_yaml(prop))]

    rows = load_yaml(brain / "match_ledger.yaml") or []
    if not isinstance(rows, list):
        errors.append("match_ledger.yaml: must be a list of rows")
        rows = []
    for i, row in enumerate(rows):
        errors += [f"match_ledger.yaml[{i}]: {e.json_path} {e.message}" for e in validators["match-ledger-row"].iter_errors(row)]

    for eid, (kind, data, rel) in entries.items():
        level = data["sensitivity"]
        if levels and level not in levels:
            errors.append(f"{rel}: sensitivity '{level}' not in config sensitivity_levels")
            continue
        for src in data["provenance"]:
            if src.startswith("expert:"):
                continue
            if src not in known_ids:
                errors.append(f"{rel}: provenance {src} not found")
            elif src in entries and levels and entries[src][1]["sensitivity"] in levels and levels.index(level) < levels.index(entries[src][1]["sensitivity"]):
                errors.append(f"{rel}: sensitivity '{level}' is lower than source {src}")
        refs = list(data.get("related", [])) + list(data.get("serves_task", [])) + list(data.get("source_concepts", []))
        refs += [data[k] for k in ("normal_baseline", "from", "to") if k in data]
        refs += (data.get("procedure") or {}).get("question_sources", [])
        errors += [f"{rel}: reference {r} not found" for r in refs if r not in known_ids]

    if errors:
        print(f"FAIL {brain}: {len(errors)} problem(s)")
        for e in errors:
            print("  " + e)
        return 1

    index = []
    for eid, (kind, data, rel) in sorted(entries.items(), key=lambda kv: str(kv[1][2])):
        row = {"id": eid, "kind": kind, "file": str(rel), "sensitivity": data["sensitivity"]}
        if "agent_reuse" in data:
            row["agent_reuse"] = data["agent_reuse"]
        if eid.split("-")[0] in GOVERNED:
            row["serves_task"] = data["serves_task"]
            row["trust"] = data["trust"]
            row["relevance"] = relevance(data, args.today, default_window)
        index.append(row)
    if not args.check:
        header = "# Generated by schemas/validate.py. Do not edit by hand.\n"
        (brain / "index.yaml").write_text(header + yaml.safe_dump({"entries": index}, sort_keys=False, allow_unicode=True))
    print(f"OK {brain}: {len(entries)} entries, {len(rows)} ledger rows" + ("" if args.check else ", index.yaml regenerated"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
