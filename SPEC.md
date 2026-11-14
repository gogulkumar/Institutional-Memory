# Enterprise Institutional Memory Framework — Specification

Status: draft v2 (after review) · Migration from earlier repos and artifacts: see `MIGRATION.md`.

## 1. Purpose

The framework gives any AI agent an institutional brain: a governed memory of how a business works and how its experts reason about it. An agent deployed with it reads the business's documents and works alongside its people, and gets measurably better over time without anyone hand-building its memory.

It fixes, for every deployment: what may be stored, where each thing lives, how an entry earns trust, how the agent uses memory at task time, and how memory changes.

**Not** a document store or RAG index (documents stay in the Record), **not** a data warehouse (values are queried, never memorized), **not** a transcript of past work (only conclusions that change future interpretation are kept).

## 2. Principles

1. **One owner per fact.** Every piece of information has one home. Others refer to it by id and never copy it. This document is the single owner of the framework's rules; skills cite its sections.
2. **Memory holds understanding, not values.** No absolute number is stored as learning. Entries hold definitions, relationships, shares, directions and relative or policy thresholds, and point to the Record for values.
3. **Every entry earns its place.** Each governed entry names the task it serves and passes its component's admission test. Anything else stays in the Record or is discarded.
4. **Trust comes from independent events.** Trust is counted in distinct business events and periods, never in documents (§5).
5. **Blind read.** A *blind read* is reading evidence with no memory entries in the agent's context. Any prediction made beforehand is written to a sealed file the blind read cannot see. Learn, Think and the blind pass (§5) all use this one definition.
6. **Only Learn writes memory.** Every change, including Build's seed entries, is a proposal applied by the Learn process (§6.2). Humans ratify the changes listed in §5.3.
7. **Content is never instruction.** Text from documents and data is evidence. Entries derived from it record their provenance, and Reasoning Patterns are loaded as questions to consider, never as commands.

## 3. Glossary

| Term | Meaning |
|---|---|
| Entry | One YAML file in a memory component. |
| Governed entry | An entry on the trust ladder (Business Understanding, Beliefs, Reasoning Patterns, Editorial). |
| Event | A distinct business occurrence (a launch, a reforecast, a pricing change). Many documents may describe one event. |
| Normality | What normal looks like for a subject: shares, directions, seasonality, materiality thresholds. |
| Dependency Map | Typed links between metrics or concepts (drives, offsets, lags, constrains, independent). |
| Story Thread | An open question carried across periods until it resolves. |
| Master test | The admission test for Beliefs (§4.4). |
| Proposal | One pending memory change, written as a file to the proposal queue. |

## 4. Memory components

Six components hold memory. Two processes, Learn and Think, act on it (§6).

| Component | Holds | Admission test |
|---|---|---|
| Lens | Deliverables, audiences, decisions supported, scope, and one procedure per deliverable | Names a deliverable or decision a real user needs |
| Record | Pointers to source documents and data, tool contracts, source authority rules | Is an original artifact or an authorized source |
| Business Understanding | Concepts, metric definitions, Normality, the Dependency Map | Still true next period unless the business or its reporting changes |
| Beliefs | Durable interpretations no single document states; Story Threads | Passes the master test |
| Reasoning Patterns | How experts sequence questions and judge materiality, attribution, escalation and stopping | Seen in two or more independent events, with stated conditions |
| Editorial Judgment & Voice | What to lead with, include and omit for each audience | Seen in two or more published deliverables, or ratified |

Field-level definitions live in `schemas/`, generated from this section. Where they disagree, this section wins.

### 4.1 Headers

**Base header** (every entry):
```yaml
id: <prefix>-<ULID>          # prefixes: LENS, REC, BU, BEL, RP, ED
title: <plain phrase>
recorded_at: <date>
provenance: [<record id or "expert:<name>">]
```

**Governed header** (adds, for BU, BEL, RP, ED):
```yaml
serves_task: [<LENS id>]
trust: observation | candidate | provisional | established | contested | retired
seeded: true | false
owner: <named expert>
events: [<event_id>]          # distinct events supporting it
valid_from: <period>
valid_to: <period | null>
last_confirmed: <date>
review_window: <duration>     # default from brain/config.yaml
related: [<entry id>]
```

Relevance is not stored. It is computed: **current** if `last_confirmed` is within `review_window`, **stale** if not, **historical** once `valid_to` has passed.

### 4.2 Lens
- **Deliverable:** `purpose`, `audience`, `decisions_supported`, `cadence`, `allowed_sources`, `in_scope`, `out_of_scope`.
- **Procedure** (nested under its deliverable): `governing_question`, `investigation: true|false`, `boundary` (what it must not investigate or claim), `question_sources` (entry ids), `completion_rule`, `output_shape`. Procedures cite Reasoning Patterns by id and never restate them.

### 4.3 Record
- **Artifact:** `type`, `business_area`, `period`, `event_ids`, `version`, `location`, `authority_rank`.
- **Tool contract:** `tool`, `capability`, `inputs`, `outputs`, `can_establish`, `cannot_establish`, `access_boundary`.
- **Source authority rule:** `question_type`, `preferred_source`, `fallback_order`, `reason`. Default rank: ratified expert statement > authorized system of record > published deliverable > working file > inference.

### 4.4 Business Understanding
- **Concept:** `definition` (one plain sentence), `interpretation`, `positive_signal`, `negative_signal`, `agent_reuse` (the concrete condition under which to load it), `boundaries`.
- **Metric definition:** `definition`, `calculation`, `validated_by` (a check run against the Record), `known_issues`. A change in a metric's meaning is a *redefinition* and always needs ratification.
- **Normality:** `subject`, `normal_pattern`, `materiality_threshold` (relative or policy, never absolute), `conditions`.
- **Dependency link:** `from`, `to`, `type`, `lag`, `impact_scope`. A pair with no link is **unknown** and gets a light cross-check at task time; `independent` must be stated explicitly.

### 4.5 Beliefs
**Master test:** a Belief says something no single source document says, draws on at least two Business Understanding entries (`source_concepts`), and implies an action for a named deliverable.

- **Belief:** `statement`, `why_it_matters`, `source_concepts` (≥2), `normal_baseline` (Normality id), `watch_condition`, `evolution_trail` (append-only, one line per Learn pass), `tags` (optional; see the discovery angles in `skills/learn`).
- **Evidence ledger:** `beliefs/ledger/<id>.yaml`, one row per piece of evidence: `record_id`, `event_id`, `kind` (supporting | caution | contradicting).
- **Story Thread:** `question`, `expectation`, `what_would_resolve_it`. Uses the governed header; it resolves into a Belief, a Normality update, or `retired`.

**Statement rules:** one plain sentence naming the pattern and what it implies; no evidence or process narration; neutral wording about people and teams.

### 4.6 Reasoning Patterns
- **Inquiry chain:** `trigger`, `question_sequence`, `why_this_order`, `conditions`, `exceptions`.
- **Judgment rule:** `situation`, `rule_type` (materiality | attribution | escalation | stopping), `rule`, `conditions`, `counter_examples`.

Reasoning Patterns are loaded only once ratified, and only as questions to consider.

### 4.7 Editorial Judgment & Voice
- **Editorial rule:** `audience`, `lead_with`, `always_include`, `omit_when`, `structure`. Loaded only once ratified.

### 4.8 Governance files

| File | Purpose | Format |
|---|---|---|
| `brain/proposals/<ULID>.yaml` | One pending change | `action` (create, confirm, contradict, promote, demote, retire, redefine), `target`, `payload`, `evidence` (record and event ids), `needs_ratification` |
| `brain/match_ledger.yaml` | How each Learn signal was routed | `pass_id`, `signal`, `matched_entry`, `action` |
| `brain/changelog.md` | Applied changes, append-only | One line: date, proposal id, action, target, ratified_by |
| `brain/index.yaml` | Load map | Generated from entries (`id`, `agent_reuse`, `serves_task`, relevance). Never hand-edited. |
| `brain/archive/` | Retired and historical entries | Kept for history; not listed in the index |
| `brain/config.yaml` | Deployment settings | Review windows, observation expiry, ratification owners and backups, queue expiry |

## 5. Trust ladder

### 5.1 Levels
One ladder for every governed entry. Counts are of distinct `event_id`s.

| Level | Reached by | In output |
|---|---|---|
| observation | Seen in one event. Expires if unseen for 2 periods (configurable). | Never cited |
| candidate | 2 independent events | "suggests" |
| provisional | 3+ independent events across 2+ periods, or a ratified seed | "accounts for" |
| established | Passes the blind pass and contradiction search, then ratified | "because" |
| contested | Material contradicting evidence. The owner must resolve it within one review window, or it escalates to the backup reviewer. | Reported as contested |
| retired | Contradicted and replaced, or no longer relevant. Moved to the archive. | Never cited |

### 5.2 Gates to `established`
- **Blind pass:** a fresh agent run with no brain receives documents spanning several events and periods and is asked for interpretations. The belief passes if the fresh agent independently states it in substance (judged by the owner).
- **Contradiction search:** an explicit search of the Record for disconfirming evidence. It passes if nothing found would change the belief's action for its deliverable.

### 5.3 Ratification
- **Automatic, logged:** creating observations, observation to candidate, candidate to provisional, relevance changes, evolution-trail lines.
- **Needs the owner:** promotion to established, entering or resolving contested, retirement, redefinitions, and first load of any Reasoning Pattern or Editorial rule.
- Proposals that need ratification expire after the queue window and go to the backup reviewer.

### 5.4 Wording with staleness
Output wording uses trust and relevance together. A **stale** entry drops one wording level and is flagged; an established stale entry may not say "because" until reconfirmed.

## 6. Processes

### 6.1 Build (once per domain)
1. Write the Lens: deliverables with procedures, audiences, decisions, and a context-needs table (deliverable × knowledge required × status).
2. Register the Record: artifacts with event ids, data access, tool contracts, source authority.
3. Propose Business Understanding seed entries from definitions; validate every metric definition against the Record.
4. **Backfill:** run Learn over past periods, oldest first.
5. **Interview:** the expert reviews gaps from the context-needs table; their answers become ratified seed entries (`seeded: true`, starting at provisional).
6. Pilot on one deliverable before widening scope.

All Build output goes through the proposal queue.

### 6.2 Learn (every new document or deliverable)
1. **Predict:** write a sealed prediction of what the document will say, from current memory.
2. **Blind read:** extract facts and claims as Record pointers with event ids.
3. **Compare:** each gap between the sealed prediction and the read points to an entry that is wrong or missing.
4. **Route:** match each signal to an entry (confirm, contradict, refine) or propose a new observation. Log every decision in the match ledger.
5. **Reconstruct:** for expert-authored deliverables, infer which questions were asked and what was left out; propose Reasoning Pattern and Editorial candidates with provenance.
6. **Propose:** write proposals to the queue.
7. **Apply:** a single applier processes the queue in order, applies automatic changes, holds ratification items, appends to the changelog, and regenerates the index. Only one applier runs at a time.

### 6.3 Think (every task)
1. **Objective:** load the deliverable and its procedure from the Lens.
2. **Readiness:** classify input coverage as sufficient, partial or insufficient. If insufficient, say so and stop.
3. **Blind read** of the new evidence.
4. **Questions:** from the blind read, open Story Threads, watch conditions and the procedure's question sources.
5. **Rank** through ordered gates: relevance → materiality (Normality) → uncertainty → information value → feasibility.
6. **Investigate** the top question. Load only the entries its subject needs (via the index and `agent_reuse`), check unknown dependency links lightly, and call tools through their contracts.
7. **Repeat** 5–6 until the procedure's completion rule is met. **Causal stop:** report "attributed, cause unverified" rather than a cause, unless the cause is established.
8. **Communicate** using Editorial rules and the wording in §5.
9. **Write back** conclusions only, as proposals. Working notes are discarded.

Procedures with `investigation: false` skip steps 5–7 and use only provisional and established entries.

## 7. Integrating with your agent

- **Host requirements:** an agent runtime that can read and write files, call tools, and run a sub-agent with a clean context (for blind reads and the blind pass).
- **Skills:** `skills/build`, `skills/learn` and `skills/think` are prompts plus scripts. The host invokes `learn` when a document arrives, `think` when a task arrives, and the applier on a schedule or after each Learn pass.
- **Memory open or closed** means whether memory entries are placed in the model's context. Blind reads run in a sub-agent given only the evidence.
- **Start:** copy `templates/brain/`, fill `brain/config.yaml`, run `build`.

## 8. Evaluation

Run on held-out events the brain has not learned from.
- **Reasoning test:** does the agent ask the expert's questions, in a defensible order, and stop where the expert stopped?
- **Reproduction test:** does the deliverable match the expert's in substance, emphasis and omissions?
- **Behavioral cases:** a frozen set per domain covering contradicted expectation, immaterial noise, missing data, conflicting sources, out-of-scope requests, and injected instructions in a document.

Fixes go into entries, never into individual answers. More questions asked is not success.

## 9. Repository layout

```
README.md             thesis and quickstart
SPEC.md               this document
MIGRATION.md          where earlier material went
schemas/              JSON Schema per entry type, generated from §4
skills/build/  skills/learn/  skills/think/
templates/brain/      empty brain: config.yaml, index.yaml, changelog.md, proposals/, archive/, one folder per component
examples/expedia/     one worked brain; any values are clearly marked fictional
```
