# Migration into the Enterprise Institutional Memory Framework

One-time record of where earlier material went. Delete this file once migration is complete.

## Decisions taken
- One repo: Institutional-Memory. The `belief` repo's history is merged here and the repo is then archived.
- Six memory components plus the Build, Learn and Think processes (SPEC §4, §6). The earlier nine-component draft folded Procedures into the Lens and turned Inquiry and Learning & Governance into processes.
- Ratification by one named owner with one backup reviewer.
- Belief streams are discovery angles in `skills/learn`, not storage partitions or a required field.
- YAML is the storage format.

## `belief` repo

| File | Disposition | Destination |
|---|---|---|
| `BELIEF.md` | merge | SPEC §4.5 (master test, statement rules) |
| `STREAMS.md` | merge | `skills/learn` discovery angles |
| `prompts/belief-doctrine.md` | merge | SPEC §2, §4.5, §5 |
| `belief-memory/schema.md` | merge | SPEC §4; drop `L2_factlogs/` and `L3_raw/` value copies |
| `architecture/overview.md` | merge | SPEC §6 |
| `lifecycle/ingestion-pipeline.md` | merge | `skills/learn` |
| `prompts/-1-generate-foundation.md` | merge | `skills/build` step 3 |
| `prompts/00-document-profile.md`, `01-generate-blueprint.md` | merge | `skills/build` step 1 |
| `prompts/03-belief-reasoning-compiler.md` | merge | `skills/learn` steps 3–6 |
| `prompts/06-fact-extractor.md` | merge | `skills/learn` step 2 |
| `prompts/07-belief-activation.md` | merge | `skills/think` |
| `skill.md` | merge | split across the three skills |
| `usage.md` | merge | README quickstart |
| `config/belief_config.yaml` | merge | `templates/brain/config.yaml` |
| `README.md`, `CLAUDE.md` | drop | superseded |

## `Institutional-Memory` repo

| File | Disposition | Destination |
|---|---|---|
| `README.md` | keep, edit | thesis + quickstart; remove the 7-layer framing |
| `BLUEPRINT.md` | merge, then drop | Step 0/0.5 → `skills/build`; schemas → `schemas/` |
| `skills/institutional-intelligence-framework/SKILL.md` | merge, then drop | writing rules → SPEC §4.5; build steps → `skills/build` |
| `.../references/schemas.md` | merge, then drop | `schemas/`; drop numeric `confidence` and separate `status` |

## Artifacts

| Artifact | Disposition | Destination |
|---|---|---|
| AI Analyst Brain | merge | component boundaries, one owner per fact, tool contracts, editorial rules; drop metaphors, numbering, quiz |
| Inquiry Layer | merge | SPEC §6.3, causal stop, Story Threads, evaluation cases |
| Agent Learning Framework | merge | SPEC §6.2 predict-then-compare and reconstruction, event counting, clocks, never store numbers, interview step |
| Rolling Analytical Memory example, P&L Drivers v2 | drop | superseded by `examples/expedia` |
| Finance AI Partner Operating Model, CFO one-pager | out of repo | positioning; link from README if wanted |
| Inside the Transformer, I-130 checklist, Driver Prompt fixes | out of repo | unrelated |
