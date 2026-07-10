# Belief — Business Belief Intelligence

> Institutional memory is portable: what is normal, what is template, what is evolving, and what would break — loaded into agents at the moment they draft, validate, or flag — instead of re-teaching the model from raw decks every time.

*Gogul Kumar Mathi · 2026*

---

## The Problem

Every organization produces recurring documents as part of how it operates: quarterly business reviews, earnings calls, investor presentations, board decks, operating reports. These are not incidental outputs — they are the formal record of how management interprets performance, explains outcomes, and communicates direction.

What those documents contain, beyond the numbers:

- How this team explains performance — what causes they name, in what order, framed how
- Which metrics they treat as primary versus secondary
- How emphasis shifts when results disappoint
- What language recurs, and what language disappears
- How commitments are explained when they are not met

These behavioral patterns are not visible in any single document. They only emerge after reading many comparable documents from the same entity over time.

A senior analyst who has read ten months of the same business's review decks holds a mental model that no one has written down. They know what a normal deck looks like — so they immediately see what is unusual about this one. They know how this management team typically explains a shortfall. They know which commitment is always ambitious and which is typically conservative.

That accumulated understanding isn't in a file. It isn't queryable. When the analyst leaves, it leaves with them.

---

## What Belief Is

Belief reads business process deliverables — the recurring decks, transcripts, reports, and documents that organizations already produce — and builds a living model of how the business works and behaves.

Not what any single document says. The pattern of behavior visible only across many comparable documents over time.

**The system discovers the business model by reading. The user doesn't need to explain it upfront.** The documents contain the model — management explains how the business works every period. When a transcript says "Q1 marketing investment drives new customer volume in Q2 with a 6–8 week lag," that is a relationship claim. The belief system extracts it, initializes a Candidate belief on the first document it appears in, and confirms or contradicts it as more documents arrive. By document 3–4, the belief memory contains a preliminary working model of the business — discovered from reading, not specified from assumption.

It doesn't store facts. It accumulates **beliefs**.

| A Fact | A Belief |
|--------|----------|
| Revenue was $2.3B in Q3. | Revenue growth is increasingly dependent on pricing rather than volume, suggesting the business is extracting from its existing base rather than expanding it. |
| Static. Answers lookup queries. | Carries direction, confidence, and trajectory. Tells you what to expect in the next document — and what would be a surprise. |

A belief is both **durable** and **provisional**. Durable: it holds across time, not abandoned after one contradicting document. Provisional: it's a working interpretation open to revision when accumulated evidence warrants it. When enough evidence accumulates to demand a different interpretive frame — not just refined confidence, but a different understanding of what the pattern means — the belief shifts perspective, not just statement.

The belief memory carries four kinds of institutional understanding:

| What it captures | Where it lives in the system | What it gives you |
|---|---|---|
| **What is normal** | Normal baseline (belief entry field) | Expected ranges and behaviors — deviations are immediately visible |
| **What is template** | Entity foundation — signals-vs-noise | What this entity always says, what language is formulaic, what to discount so the real signal stands out |
| **What is evolving** | Evolution trail (belief entry field) | Per-document history of how the pattern developed — deepened, tensioned, narrowed |
| **What would break** | Falsification test (belief entry field) | The specific signal in a future document that would contradict, narrow, or retire the belief |

These four things — loaded into an agent at the start of a drafting, validation, or flagging task — replace the need to re-teach the model from raw decks every time.

**Memory has three tiers, and nothing entity-specific is thrown away.** The master test — *does this say something no single document says?* — doesn't admit or reject, it **classifies**. Definitional constants (metric definitions, benchmark structure) are **foundation facts**. Interpretations that pass the master test are **beliefs**. Recurring regularities that fail it (reporting conventions, vocabulary habits) are **Observations** — cited as unverified patterns, never as beliefs, but kept, because they are exactly what a new analyst wants on day one. This is what lets the system yield something useful early instead of discarding everything that isn't yet a verified belief.

Each belief entry has five narrative fields — **Statement**, **Why it matters**, **Evolution trail**, **Normal baseline**, **Falsification test** — plus a structured **Provenance** record: which documents confirmed it, which pass independently re-derived it blind, which contradiction searches came back empty, and which foundation claim it depends on.

A **skill** does the task — pulls the numbers, builds the report. A **belief** is the understanding the task is performed from. Skills take the doing; beliefs take the thinking.

---

## The Seven Belief Streams

Every document is read through seven belief streams. Each asks a different question about the same entity. All seven write into one belief memory — one living model of one entity. The governing rule across every stream: a belief must say something the document does not say.

| # | Stream | What It Asks |
|---|--------|-------------|
| 00 | Factual Understanding | What is verifiably true about how the business is measured — metric definitions, calculation bases, the stable factual record? |
| 01 | Business Model Understanding | What is the underlying economic engine — the profitability thesis, and whether it is holding? |
| 02 | Business Dynamics | How do the parts of the business move relative to each other — lead-lag relationships, conversion chains, stress and feedback behavior? |
| 03 | Causal Understanding | What does the team attribute as the causes of performance — and is that attribution honest, selective, or strategically chosen? |
| 04 | Business Memory | How does this organization behave as a decision-making system under pressure — what does it actually do, not say? |
| 05 | Narrative Understanding | How does this business tell its story — what does the framing reveal versus what the numbers actually show? |
| 06 | Forecast and Plan Behavior | How does this business plan, forecast, and revise — what systematic biases show up in how it sets and updates expectations? |

Custom belief streams are also supported: Marketing Efficiency Memory, Forecast Reliability, Operational Risk Memory, Investor Messaging, Margin Quality, Forecast Bias, or any user-defined angle.

---

## How Belief Works

0. **Entity foundation built** — a 5-minute setup captures entity identity and document types only. The business model isn't pre-specified — it's discovered from documents. Once the first few fact logs exist, a corpus grounding pass extracts the definitional constants (metric definitions, benchmark structure) into foundation claims, each with a stable claim ID that beliefs reference.
1. **Stream setup** — defines the entity, the angle, and the document set
2. **Blueprint compiled** — defines what a belief looks like for this entity in this stream; seeds 8–15 candidate hypotheses including relationship hypotheses for Stream 02 (Business Dynamics)
3. **Prompts compiled** — one belief reasoning prompt and one fact extraction prompt
4. **Document arrives** — any format: deck, transcript, report, audio
5. **Signals extracted** — first pass: relationship claims (explicit statements connecting metrics); second pass: candidate signals. Relationship claims from the first document initialize Stream 02 (Business Dynamics) Candidate beliefs immediately.
6. **Belief evolves — and is verified where trust is spent** — the belief engine makes surgical updates, routing every signal through an auditable match ledger. Promotion is gated, but rigor follows citation weight: recurrence forms a Provisional hypothesis (cited only as unverified); a blind pass (extraction with the belief withheld) earns Confirmed, the first tier cited without hedging; a contradiction search earns Established. A belief only ever echoed never climbs past Provisional; a belief gone silently stale decays back down the ladder.
7. **Belief activated** — at any point, the belief memory can be queried: pre-read briefing before the next document, a calibrated answer to a specific question, or a meeting brief with what to push on and what to accept.
8. **Silence by default** — most inputs produce no update. The gate is the mechanism.

Each belief carries:
- **Claim as heading** — `## Belief #N — [specific, falsifiable sentence]`
- **Statement** — the claim restated precisely as business judgment grounded in the foundation
- **Why it matters** — how it connects to the entity's profitability thesis
- **Evolution trail** — first-person, per-document journey of how the pattern developed
- **Normal baseline** — what the next comparable document should show if holding
- **Falsification test** — what a future document must show to break, narrow, or retire it
- **Provenance** — the machine-checkable audit record: confirming documents, blind passes, contradiction searches, the foundation claim ID it depends on, related beliefs, last checked

---

## Repo Structure

```
belief/
├── README.md                               ← you are here
├── BELIEF.md                               ← full specification
├── STREAMS.md                              ← the seven streams in depth — one full worked example per stream
├── usage.md                                ← how beliefs accumulate and how to use them
│
├── architecture/
│   └── overview.md                         ← system architecture & how it fits in the stack
│
├── lifecycle/
│   └── ingestion-pipeline.md               ← how documents flow through Belief (foundation + two phases)
│
├── belief-memory/
│   └── schema.md                           ← belief file structure, update arithmetic, changelog tags
│
├── prompts/
│   ├── belief-doctrine.md                  ← shared doctrine: what a belief is across all prompts
│   ├── -1-generate-foundation.md           ← Prompt -1: build the entity foundation (once per entity)
│   ├── 00-document-profile.md             ← Prompt 00: interview agent to build document profile
│   ├── 01-generate-blueprint.md           ← Prompt 01: produce the Strategic Blueprint
│   ├── 03-belief-reasoning-compiler.md    ← Prompt 03: compile the belief reasoning prompt
│   ├── 06-fact-extractor.md              ← Prompt 06: compile the fact extraction prompt
│   └── 07-belief-activation.md           ← Prompt 07: activate the belief memory (pre-read, Q&A, meeting prep)
│
├── config/
│   └── belief_config.yaml                  ← reference configuration file
│
├── entities/                               ← one subdirectory per entity; built before any stream
│   └── {entity_id}/
│       └── foundation.md                   ← business model, thesis metrics, normalization, narration
│
├── compiled/                               ← generated at setup; one subdirectory per stream
│   └── {stream_id}/
│       ├── document_profile.md
│       ├── strategic_blueprint.md
│       ├── belief_reasoning_prompt.md
│       └── fact_extractor_prompt.md
│
└── streams/                                ← living data; one subdirectory per stream
    └── {stream_id}/
        ├── belief.md                       ← L1 belief memory (surgically updated, numbered beliefs)
        ├── belief_changelog.md             ← append-only audit trail
        ├── L2_factlogs/                    ← per-document extracted signals
        └── L3_raw/                         ← immutable transcription archive
```

---

## The Acceptance Criterion

Give Belief ten months of business review decks. Read the resulting belief memory. If a senior analyst reads it and identifies two or three beliefs they agree with that they would not have articulated explicitly — beliefs that feel true, that reflect how the business actually behaves — **the system is working**.

Not accuracy on a benchmark. Not a perplexity score. An analyst saying: *yes, that is what I know about this business.*

---

## Quick Links

- [Run Belief End-to-End (Skill Prompt) →](skill.md)
- [Full Specification →](BELIEF.md)
- [How Belief Accumulates and How You Use It →](usage.md)
- [Shared Belief Doctrine →](prompts/belief-doctrine.md)
- [Architecture & Stack Integration →](architecture/overview.md)
- [Ingestion Pipeline →](lifecycle/ingestion-pipeline.md)
- [Belief Memory Schema →](belief-memory/schema.md)
- [Config Reference →](config/belief_config.yaml)
