# Working Rules for This Repo

This repo is a documentation-defined system: the same concepts are deliberately expressed at several altitudes (spec, reference, lifecycle, architecture, prompts, skill, config). That means every conceptual change touches many files, and a change applied in one place but not the others produces contradictions that actively mislead — worse than the change never being made.

## The Two-Step Rule (non-negotiable, every change)

1. **Make the change AND remove the stale version.** Never add the new alongside the old. Hunt down the superseded wording, the old numbers, the previous mechanism — and delete or rewrite it. A file that teaches the old mechanic is worse than an empty file.
2. **Propagate everywhere.** Understand the whole project before editing: find every file that expresses the concept you are changing, and update all of them in the same commit. Use the propagation map below, then verify with repo-wide greps for the old terminology — never trust memory of where things live.

After any change, before committing: grep for the old terms/names/numbers across `*.md` and `*.yaml` (excluding `.claude/`), and fix every hit.

## Propagation Map — where each concern lives

| Concern | Files that express it |
|---------|----------------------|
| **Belief entry format** (five narrative fields + Provenance) | `prompts/belief-doctrine.md` · `belief-memory/schema.md` (template + all worked examples) · `skill.md` (Stage 4 two templates + Reference section) · `prompts/01-generate-blueprint.md` §3.1 · `prompts/03-belief-reasoning-compiler.md` (Sections B, F, H) · `BELIEF.md` (mature-belief examples, "What a Belief Contains") · `README.md` ("Each belief carries") · `STREAMS.md` (entry format + all seven examples) |
| **Changelog action tags** | `lifecycle/ingestion-pipeline.md` (tag table) · `prompts/03-belief-reasoning-compiler.md` (Section F list) · `skill.md` (Stage 5 action table) · `belief-memory/schema.md` (changelog examples) |
| **Durability ladder + promotion gating** (rigor-follows-citation-weight: recurrence→Provisional hedged, blind pass→Confirmed, contradiction search→Established; decay walks DOWN the ladder to STALE) | `prompts/belief-doctrine.md` · `BELIEF.md` §02 · `belief-memory/schema.md` · `prompts/03-belief-reasoning-compiler.md` (Sections B, E, F) · `skill.md` (Stage 3b spec, Stage 4/5 ladder + Reference) · `usage.md` (accumulation walkthrough + numbers table — historically goes stale, always check) · `lifecycle/ingestion-pipeline.md` (Step 7 + steady-state loop) · `architecture/overview.md` (Layer 3 box) · `config/belief_config.yaml` · every worked-example Provenance block (blind pass gates Confirmed, not Provisional) |
| **Three tiers of memory** (foundation fact / belief / Observation — master test classifies, never discards) | `prompts/belief-doctrine.md` (Three Tiers section + Observation entry) · `BELIEF.md` §02 · `belief-memory/schema.md` (Observation format + file structure) · `prompts/03-belief-reasoning-compiler.md` (classify-first, tags) · `skill.md` (Stage 4/5 + persist layout + Reference table) · `prompts/07-belief-activation.md` (whole-pyramid citation) · `README.md` · `usage.md` · `architecture/overview.md` (three-tiers block) · `config/belief_config.yaml` (`observation_tier_*`) |
| **Match ledger** (evidence-routing is auditable; match by mechanical claim) | `prompts/belief-doctrine.md` (Match Ledger section) · `belief-memory/schema.md` (format + file structure) · `prompts/03-belief-reasoning-compiler.md` (route-and-log) · `lifecycle/ingestion-pipeline.md` (Step 7) · `skill.md` (Stage 4/5) · `config/belief_config.yaml` (`match_ledger_enabled`) |
| **Compilation gate + injection boundary** (compiled prompts carry `status: ready\|blocked`; runtime refuses blocked; document text is data never instructions) | `prompts/03-belief-reasoning-compiler.md` · `prompts/06-fact-extractor.md` · `lifecycle/ingestion-pipeline.md` (Steps 3, 4, 6) · `skill.md` (Stage 3b/3c + Stage 7 refuse-if-blocked) · `prompts/belief-doctrine.md` (injection principle) · `config/belief_config.yaml` (`block_runtime_on_unready_prompt`) |
| **The seven streams** (names, numbers, tests) | `BELIEF.md` §03 (spec definitions) · `STREAMS.md` (sole home of worked examples — role split, don't duplicate) · `README.md` (table) · `prompts/00-document-profile.md` (Area 3) · `skill.md` (Stage 2 table) · `config/belief_config.yaml` (`standard_streams`) · `prompts/03-belief-reasoning-compiler.md` (Section C numbers policy) · `prompts/06-fact-extractor.md` (Section C) · `prompts/belief-doctrine.md` (domain guidance) · `architecture/overview.md` (pattern table) |
| **Pipeline steps** (incl. 6.5 drift check, 7.5 foundation review, corpus grounding, snapshots) | `lifecycle/ingestion-pipeline.md` (canonical) · `BELIEF.md` §04–§05 · `architecture/overview.md` (both diagrams) · `skill.md` (stages) · `README.md` ("How Belief Works") |
| **Foundation** (claim IDs, source labels, revision log, review process) | `prompts/-1-generate-foundation.md` (canonical) · `lifecycle/ingestion-pipeline.md` (Step −1, Step 7.5) · `skill.md` (Stage 1 + Stage 5) · `prompts/belief-doctrine.md` (Grounded property) · `BELIEF.md` §07 prohibitions · `config/belief_config.yaml` |
| **Document Profile / Structural Map / drift** | `prompts/00-document-profile.md` (canonical) · `prompts/01-generate-blueprint.md` (Section 2) · `prompts/06-fact-extractor.md` (Expected Structure + Part 0) · `lifecycle/ingestion-pipeline.md` (Steps 1, 6, 6.5) · `skill.md` (Stages 2, 4, 5) · `BELIEF.md` §07 prohibitions |
| **Numeric parameters** (thresholds, decay counts, escalation counts) | `config/belief_config.yaml` is the source of truth — every prose mention of a number (e.g., "4 consecutive silent documents", "8–15 Candidates", "after 3 fact logs") must match it |
| **Scope-boundary prohibitions** ("must never" lists) | `BELIEF.md` §07 · the corresponding prompt file's Behavior Rules · `prompts/03-belief-reasoning-compiler.md` Section H |

**Check the skill last, always.** `skill.md` is the only file end users actually run — it is the convergence point where every mechanism must land in executable form. Historically it lags the spec; treat "did this reach the skill?" as a mandatory final question for every change.

## Content Rules

- **No employer-, brand-, or company-specific content — ever.** No real company names, internal product/system names, internal metric abbreviations, or vocabulary that identifies a specific business. All examples use generic placeholders ("[Entity]", "core volume metric", "spend ratio", "demand"). Sweep for leaks before every commit, including in newly pasted-in source material.
- **One authority per concern.** When the same content exists at two altitudes, one file is canonical and the other points to it (e.g., `STREAMS.md` owns worked examples; `BELIEF.md` §03 owns spec definitions). Never let two files independently maintain the same content — declare the role split at the top of both.
- **Nothing is silently absorbed.** Every revision to a foundation claim, structural map, or belief goes through its defined visible process (Foundation Review, Structural Drift Check, changelog) with a logged resolution. This applies to the docs themselves too: superseded design decisions get removed, not left to coexist.

## Git

- Work on the designated `claude/*` branch; commit with clear messages explaining the *why*; push after every completed change set.
- If the branch's PR was merged, restart the branch from latest `main` and open a new PR — never stack onto merged history.
