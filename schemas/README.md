# Schemas

JSON Schema (draft 2020-12) for every entry type in SPEC §4. Field definitions follow SPEC §4; where they disagree, SPEC wins and the schema is the bug.

| Schema | Used for |
|---|---|
| `base-header`, `governed-header` | Headers composed into every entry (SPEC §4.1) |
| `lens-deliverable` | `lens/` (deliverable with nested procedure) |
| `record-artifact`, `tool-contract`, `source-authority` | `record/` |
| `concept`, `metric-definition`, `normality`, `dependency-link` | `business-understanding/` |
| `belief`, `story-thread` | `beliefs/` |
| `evidence-ledger` | `beliefs/ledger/<belief id>.yaml` |
| `inquiry-chain`, `judgment-rule` | `reasoning-patterns/` |
| `editorial-rule` | `editorial/` |
| `proposal` | `proposals/`, `proposals/pending/`, `proposals/rejected/` |
| `match-ledger-row` | each row of `match_ledger.yaml` |

An entry's type is found from its id prefix and folder; it must match exactly one schema for that prefix.

## Validate a brain

```bash
pip install jsonschema pyyaml
python schemas/validate.py path/to/brain
```

The validator checks:
- every entry against its schema
- that referenced ids exist
- ledger and proposal file names
- that each entry's `sensitivity` is a configured level and never lower than its sources

If everything passes, it regenerates `index.yaml`, with relevance computed from `last_confirmed`, `review_window` and `valid_to`. Use `--check` to validate without writing, and `--today YYYY-MM-DD` to compute relevance as of a given date. It ignores `archive/`, `passes/` and `.applier.lock`.
