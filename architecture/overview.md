# Architecture Overview — Belief in the Stack

## The Architecture: A Cascade With Three Return Loops

Belief is built in four layers plus an activation surface. Quality flows **forward** through the cascade — foundation grounds configuration, configuration compiles into runtime prompts, runtime prompts govern execution. What makes the system robust rather than fragile is that evidence also flows **backward** through three return loops: execution is continuously allowed to correct the layers above it. A pipeline with no return arrows can only ever be as good as its setup guesses; this one recalibrates itself against the documents as they actually arrive.

```
┌──────────────────────────────────────────────────────────────┐
│  LAYER 0 — ENTITY FOUNDATION                                  │
│  foundation.md — atomic claims with stable claim IDs          │
│  Every claim labeled: source: interview | corpus | both       │
│  Pass 1 (setup): interview → hypotheses                       │
│  Pass 2 (after first N fact logs): corpus grounding →         │◄──┐
│    what recurred identically becomes source: corpus           │   │
│  Revised ONLY via Foundation Review — never silent edit       │◄──┼─┐
└──────────────────────────┬───────────────────────────────────┘   │ │
                           │  (read by every stream for this entity)│ │
                           ▼                                        │ │
┌──────────────────────────────────────────────────────────────┐   │ │
│  LAYER 1 — CONFIGURATION (once per stream)                    │   │ │
│  Document Profile: interview (user knows the business)        │   │ │
│    + mandatory STRUCTURAL READ of sample docs (documents      │   │ │
│    know themselves) → Structural Map: a stream-blind x-ray    │   │ │
│    (identical no matter which stream asks; shared across      │   │ │
│    streams) + stream-aware scouting, verbatim + traceable     │◄──┼─┼─┐
│  Strategic Blueprint: signal matrix CITES the Structural      │   │ │ │
│    Map — type-level inference banned · seed set (8–15)        │   │ │ │
└──────────────────────────┬───────────────────────────────────┘   │ │ │
                           ▼                                        │ │ │
┌──────────────────────────────────────────────────────────────┐   │ │ │
│  LAYER 2 — COMPILATION (once per stream / doc type)           │   │ │ │
│  belief_reasoning_prompt — doctrine, promotion gating,        │   │ │ │
│    Provenance format, evolution actions                       │   │ │ │
│  fact_extractor_prompt — Expected Structure embedded,         │◄──┼─┼─┤
│    two extraction modes (belief-aware / blind)                │   │ │ │
└──────────────────────────┬───────────────────────────────────┘   │ │ │
                           ▼                                        │ │ │
┌──────────────────────────────────────────────────────────────┐   │ │ │
│  LAYER 3 — EXECUTION (every new document)                     │   │ │ │
│  5   intake → L3 raw units (immutable, once)                  │   │ │ │
│  6   extract → L2 fact log:                                   │   │ │ │
│        opens with STRUCTURE OBSERVED (skeleton walked),       │   │ │ │
│        then REDEFINITION SIGNALS (ranked above relationship   │   │ │ │
│        claims — routes straight to 7.5, never to the engine)  │   │ │ │
│        + BLIND PASS in parallel when a belief is up           │   │ │ │
│          for promotion (belief withheld from extractor)       │   │ │ │
│  6.5 STRUCTURAL DRIFT CHECK — observed vs Structural Map:     │───┼─┼─┘
│        match / Recalibrate (map revised + logged,             │   │ │
│        extractor recompiled) / Signal (change is              │   │ │
│        communication behavior → feeds beliefs) / Defer        │   │ │
│  7   classify (master test → belief | observation, never     │   │ │
│        discard) · route (match_ledger) · evolve belief.md —   │   │ │
│        promotion GATED: recurrence → Provisional (hedged) ·   │   │ │
│        blind pass → Confirmed (first un-hedged tier) ·        │   │ │
│        contradiction search → Established · silence walks     │   │ │
│        DOWN the ladder → [DECAY] → STALE at Provisional floor │   │ │
│  7.5 FOUNDATION REVIEW — Confirmed/Established belief vs      │───┼─┘
│        its named claim ID, OR a REDEFINITION SIGNAL (fires    │   │
│        immediately, no belief maturity required): Adopt       │   │
│        (revise + flag dependents [FOUNDATION_CHANGED]) /      │   │
│        Hold / Defer — user decides                            │   │
│  8   changelog — append-only, one action per belief           │   │
│      (fact logs accumulate → corpus grounding, Pass 2)        │───┘
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────┐
│  ACTIVATION (on demand — Prompt 07)                           │
│  Pre-read briefing · Analytical Q&A · Meeting prep            │
│  Every citation carries Status + Provenance — a belief        │
│  whose status outruns its verification is flagged, not cited  │
└──────────────────────────────────────────────────────────────┘

THREE TIERS (the master test classifies, it never discards):
  foundation.md (facts) · belief.md (tested interpretation) ·
  observations.md (recurring regularities that fail the master
  test — cited as unverified patterns, never as beliefs)

PERMANENT MEMORY (nothing a belief cites is ever discarded):
  L3 raw archive · L2 fact logs (addressable by doc_id — the
  pointer target of every Provenance record) · L1 belief.md
  + belief_versions/ snapshots (the memory's state after every
  document, forever) · match_ledger.md (every evidence-routing
  decision, so routing is auditable) · changelog ·
  Foundation Revision Log · Structural Map Revision Log
```

### The Three Return Loops

The forward cascade sets quality; the return loops keep it honest. Each loop has the same shape: execution observes something the setup layer assumed wrong or incompletely, the conflict is surfaced visibly (never silently absorbed), and the resolution is logged.

| Loop | From → To | Trigger | Resolution |
|------|-----------|---------|------------|
| **Corpus grounding** | Fact logs → Foundation | First N fact logs exist (default 3) | What recurred identically becomes `source: corpus`; contradicted interview claims go to Foundation Review |
| **Foundation Review** (Step 7.5) | Belief memory → Foundation, OR Document → Foundation directly | A belief reaches Confirmed/Established bearing on its named claim ID, OR a document's Redefinition Signal fires regardless of belief maturity | Adopt (claim revised, logged, dependents flagged) / Hold / Defer — user decides |
| **Structural Drift Check** (Step 6.5) | Fact log → Profile + Compiled prompts | STRUCTURE OBSERVED deviates from the Structural Map | Recalibrate (map revised, extractor recompiled) / Signal (feeds beliefs) / Defer |

### The Cascade Principle

The foundation (Layer 0) grounds the blueprint (Layer 1), which is compiled into the runtime prompts (Layer 2). Every downstream step inherits its quality from this cascade. If the foundation is precise and entity-specific, everything below it is precise. If the blueprint is correct, the execution prompts are correct without additional configuration.

Quality is injected at Layers 0 and 1 and propagates forward. Debugging a bad belief output should start by examining the foundation and blueprint, not the execution prompt — and if the blueprint was wrong about the documents, the drift check is the mechanism that catches it in production rather than never.

### What Changes Cascade

A change to the blueprint automatically propagates to:
- The belief reasoning prompt (Layer 2A)
- The fact extraction prompt (Layer 2B)
- The belief memory (Layer 3)

A refinement to the foundation propagates to every belief stream for that entity — and because every belief names the foundation claim ID it depends on, an Adopted revision automatically flags every dependent belief `[FOUNDATION_CHANGED]` for re-grounding rather than leaving them standing on a claim that changed under them.

No code changes required. The compilers are generic. Only the foundation and blueprint are entity-specific.

---

## Where Belief Sits

Business process deliverables sit at the bottom of the stack. Belief reads those deliverables and builds the pattern model that sits above retrieval and below any agent or analyst that needs to reason about the business.

```
┌─────────────────────────────────────────────────────────┐
│              AGENTS / ANALYSTS                           │
│         Query agents · Report builders · Evaluators     │
└──────────────────────┬──────────────────────────────────┘
                       │  belief context loaded at session start
                       ▼
┌─────────────────────────────────────────────────────────┐
│                   BELIEF LAYER                          │
│         Belief Memory (L1) — living belief memory         │
│         Fact-to-belief gate · Update arithmetic         │
└──────────────────────┬──────────────────────────────────┘
                       │  evidence retrieval
                       ▼
┌─────────────────────────────────────────────────────────┐
│                 FACT LOGS / ARCHIVE                     │
│         L2 Fact Logs (per document) · L3 Raw Archive    │
└──────────────────────┬──────────────────────────────────┘
                       │  reads from
                       ▼
┌─────────────────────────────────────────────────────────┐
│           BUSINESS PROCESS DELIVERABLES                 │
│    Quarterly reviews · Earnings calls · Board decks     │
│    Investor presentations · Operating reports · Audios  │
└─────────────────────────────────────────────────────────┘
```

Belief is not a retrieval system, a chat interface, or a database. It is the **pattern layer** — the accumulated interpretation of how this entity behaves, built from the documents the entity already produces.

## How Agents Use Belief

Agents don't query Belief at runtime. The belief memory is **loaded into context at session start** — the same way a senior analyst reads their notes before a meeting. Every inference is then implicitly grounded by accumulated business understanding.

### Query Agent
Without Belief: queries data blind — syntactically correct answers, contextually naive.
With Belief: knows Q3 always has a one-time cost distortion. Knows a cost center runs 15% above plan historically. Answers become calibrated, not just correct.

### Narrative / Comms Agent
Without Belief: writes from static voice profiles frozen at setup.
With Belief: knows how management framing has evolved. Knows when the team shifted from growth to efficiency language. Content reflects the actual evolving communication pattern.

### Evaluation
Without Belief: checks output format and data accuracy.
With Belief: checks whether an answer reflects what is actually true about how this business operates. A new category of evaluation that cannot exist without a pattern layer.

---

## The Setup and Execution Flow

### Foundation — runs once per entity

```
Prompt -1 ← (user interview: business model, thesis metrics, normalization, narration, signals/noise)
          → entities/{entity_id}/foundation.md
```

### Setup — runs once per belief stream

```
Prompt 00 ← (entity, document types, angle, prior knowledge,
             + one SAMPLE DOCUMENT per type — read in full for the
             Structural Map: how the document tells its story)
          → document_profile.md (with Structural Map per doc type)

Prompt 01 ← (foundation.md, document_profile.md, stated purpose)
          → strategic_blueprint.md

Prompt 03 ← (strategic_blueprint.md)
          → belief_reasoning_prompt.md

Prompt 06 ← (strategic_blueprint.md, belief_reasoning_prompt.md, doc type)
          → fact_extractor_prompt.md
```

### Execution — runs for every document

```
intake.py          ← uploaded document (any format)
                   → L3_raw/{doc_id}.json (immutable)

fact_extractor.py  ← fact_extractor_prompt.md (system)
                   + L3 units + topics_touched
                   → L2_factlogs/{doc_id}_fact_log.md
                   (opens with STRUCTURE OBSERVED — the skeleton
                    walked through, deviations from the Structural
                    Map reported, never silently absorbed;
                    belief-aware pass by default; a BLIND pass —
                    existing belief withheld — runs additionally
                    whenever a belief is up for promotion)

structural drift   ← STRUCTURE OBSERVED vs the profile's Structural Map
check (Step 6.5)   → match: no action
                   → drift: Recalibrate (map revised + logged,
                     extractor recompiled) / Signal (the change is
                     communication behavior — feeds the belief
                     engine) / Defer (watch next document)

belief_engine.py   ← belief_reasoning_prompt.md (system)
                   + existing belief.md + observations.md (or NULL)
                   + fact log (+ blind-pass fact log when run)
                   → belief.md (evolved, Provenance updated)
                   → observations.md (regularities that fail master test)
                   → match_ledger.md (every routing decision + basis)
                   → belief_changelog.md (appended)
                   (classify: master test → belief | observation;
                    a REDEFINITION SIGNAL skips classification, routes
                    straight to foundation review below;
                    promotion gated: recurrence → Provisional (hedged),
                    blind pass → Confirmed, contradiction search →
                    Established; silence decays DOWN the ladder → STALE)

foundation review  ← any belief reaching Confirmed/Established that
(Step 7.5)           bears on its named foundation claim, OR a
                     document's REDEFINITION SIGNAL (fires immediately,
                     independent of any belief's maturity)
                   → user resolves Adopt / Hold / Defer
                   → foundation.md revised + revision logged (if Adopt)
                   → dependent beliefs flagged [FOUNDATION_CHANGED]
```

The belief engine at runtime receives only its compiled prompt, the existing belief memory, and the fact log(s). It never receives the raw document, the foundation, or the blueprint. This is the contract that makes the system reproducible and auditable.

---

## The Storage Layers

| Layer | Purpose | Mutability |
|-------|---------|------------|
| **Entity Foundation** | Business understanding for the entity — thesis, metrics, normalization, narration. Every atomic claim carries a stable claim ID that belief Provenance records point to. One `foundation.md` per entity. | Revised only through Foundation Review (Adopt/Hold/Defer, logged in the Foundation Revision Log) — never by silent edit |
| **L1 — Belief Memory** | Living belief memory. One `belief.md` per stream. Loaded into agent context. | Surgically updated per document |
| **L2 — Fact Logs** | Per-document extracted signals — the permanent, addressable memory layer that belief Provenance records cite by doc_id. | Written once per document; retained indefinitely once a belief cites it |
| **L3 — Raw Archive** | Original document content verbatim. | Immutable. Written once. |

---

## Pattern Recognition Is the Method, Not an Eighth Stream

Pattern recognition is not a separate belief stream. It is the method that all seven streams apply. Every stream is about patterns — the difference is what form patterns take:

| Stream | Pattern Form |
|--------|-------------|
| 00 — Factual Understanding | Metric definition stability; benchmark comparison consistency |
| 01 — Business Model Understanding | Structural margin and unit-economics trajectory across periods |
| 02 — Business Dynamics | Lead-lag pair recurrence; conversion chain stability; stress and feedback sequencing |
| 03 — Causal Understanding | Attribution sequencing; gap between stated cause and what actually moved |
| 04 — Business Memory | Decision pattern recurrence across pressure episodes |
| 05 — Narrative Understanding | Linguistic fingerprints; sequencing habits; what appears vs what is absent |
| 06 — Forecast and Plan Behavior | Revision direction and magnitude recurrence; planning bias stability |

The fact extraction prompt is the injection point for pattern direction. When the blueprint specifies what form patterns take, the fact extractor captures not just values but recurrence signals — the actual language used, the structural positions occupied, what appeared vs what was absent. Without pattern direction, the extractor captures point-in-time readings. With it, it captures evidence that accumulates into fingerprints.

---

## The Silence Default Is Not a Weakness — It Is the Design

Every belief prompt instructs the engine to stay silent unless a durable interpretation is visible. Most documents produce no belief updates across most beliefs. This is correct behavior. The rarity of a genuine belief update is what keeps confidence meaningful.

A belief system that updates on everything is a summarizer.

---

## The Compounding Effect

After 3 documents: Candidates and first Provisionals — patterns spotted, the first blind passes run.
After 10 documents: Confirmed baselines — patterns that survived independent re-derivation and contradiction searches.
After 30+ documents: Established structural understanding — beliefs with multiple blind passes and empty contradiction searches on record.

What compounds is not just document count — it is survived verification. A belief's trustworthiness is read from its Status and its Provenance record, not from a confidence number alone. The belief memory becomes more valuable the longer it runs. This is the behavior of understanding, not retrieval.
