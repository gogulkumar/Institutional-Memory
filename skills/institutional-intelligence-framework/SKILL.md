---
name: institutional-intelligence-framework
description: Guides the conversion of corporate artifacts (business review decks,
  forecast files, Excel models, earnings transcripts, analyst reports, KPI
  dictionaries, emails, meeting notes, strategy memos) into reusable
  institutional memory whenever the user wants to build a "company brain," a
  business context layer, belief tracking, or an intelligence system on top of
  internal documents — even if they don't use those exact words. Also trigger
  when the user asks how to structure business knowledge for an AI agent, how
  to make document search feel less like "dumb RAG" and more like a
  variance-explanation or CFO-narrative skill backed by curated context, or how
  to set up a feedback loop that updates beliefs as new documents arrive. Push
  toward this skill any time the user is trying to turn a pile of documents
  into something an agent can reason with reliably, rather than just search
  over.
---

# Institutional Intelligence Framework

## Why this exists

A generic LLM already reasons well and knows general facts. It does not know how *this* company works: which source is authoritative for actuals, whether a margin improvement is durable or a one-time artifact, how leadership prefers to explain it, or how it fits into the rest of the business.

The fix is not a smarter model. It's a company-specific intelligence layer wrapped around the model: source authority, extracted facts, curated business meaning, durable beliefs that evolve, repeatable workflow skills, and an agent that decides what to use.

**Core pipeline:** Corporate documents → Extracted facts → Business context → Belief streams → Workflow skills → Agent reasoning → Feedback and learning

When a user brings you documents, a domain, or a "build me an intelligence system" request, use this pipeline as the default shape to sequence the actual work.

## Step 0: Write the purpose document first — before building any layer

This is not optional, and it's the step most likely to get skipped in favor of jumping straight to extracting facts. Before creating a single artifact record, fact, or belief, produce a short `00_PURPOSE.md` that states:

- **The actual goal, in the user's words, confirmed with them rather than assumed.** "Understand narrative patterns" and "generate investor-facing talking points" are different goals that need different layer depth — don't silently assume one when the user said the other. If you discover a mismatch between what's been built and what the user actually needs, say so explicitly rather than quietly deferring the correction.
- **What each of the 7 layers needs to accomplish here, specifically for this goal, and why.** Not every goal needs all 7 layers built with equal depth on day one — but if the goal explicitly involves agents *reusing* the knowledge (as opposed to a human occasionally reading a summary), Layers 5 and 6 (Workflow Skills, Agent Reasoning) are the layers that make the word "reuse" true. If a layer is being deliberately left shallow or skipped for this goal, say so explicitly as an out-of-scope call — don't just quietly omit it.
- **Which layers matter most for this goal, and why.**

Write this purpose document *before* touching Layer 1 metadata or Layer 2 extraction — it's what every later layer corrects against. If the user later corrects the goal, rewrite the purpose document first, then reassess which existing layer content still fits — don't just patch definitions in place while the underlying goal statement is stale. See `references/00_PURPOSE_template.md`.

## Step 0.5: Context-needs analysis before extracting anything

Root cause of a common failure: the skill produces output for a task without ever having asked whether the underlying context that task depends on actually exists. Fix it structurally, not by remembering to check once.

Before writing a single Layer 3 record, build and show the user a table that maps each task the system is meant to support against the angles of context it needs, and the real status of each:

| Angle | Status |
|---|---|
| (e.g.) Rhetorical/language devices | Have |
| (e.g.) Structural template | Archived, unreviewed |
| (e.g.) Factual/business grounding | Archived, unreviewed |
| (e.g.) Speaker attribution | Unverified — partial coverage |
| (e.g.) Materiality/emphasis | Missing entirely |
| (e.g.) Competitor data | Missing entirely — hard input gap |

`Unverified` is its own category, distinct from `Have` — it means evidence exists somewhere but hasn't been checked/confirmed against the current task, and it should not be silently treated as `Have`. Do this task-by-task, angle-by-angle. State plainly which downstream tasks are blocked and on how many of the needed angles, rather than proceeding to build on angles that are missing or unverified. See `references/00b_CONTEXT_NEEDS_ANALYSIS_template.md`.

## Writing rule: plain sentences, separated from their evidence

This applies to every `definition` in Layer 3 and every `Statement`/heading in Layer 4 — the two places a human actually reads first. Five failure modes to avoid, each with a before/after:

**1. Cramming the evidence into the definition.** A definition like "A recurring phrase family that reframes flat or declining segment margin as a deliberate strategic choice rather than a shortfall" tries to state the fact *and* argue for why it's a pattern in the same sentence — dense and hard to parse. Fix: state only what the thing *is*, in one plain sentence. Push "how many quarters," "which exact quotes," "how confident to be" into the separate fields (`evidence`, `confidence`, `pattern_observed`/`Evolution Trail`) that already exist. Use the read-it-out-loud test: if you wouldn't say the sentence that way to a colleague across a table, rewrite it.
- Before: *"A recurring phrase family that reframes flat or declining segment margin as a deliberate strategic choice rather than a shortfall."*
- After: *"Whenever B2B's profit margin doesn't improve, management says it's because they chose to invest in growth — not because something went wrong."*

**2. Judgmental or accusatory word choice.** Words like *excuse, spin, bragged, deflect, defensive, evasion* smuggle in an interpretation (dishonesty, intent to mislead) that the evidence usually doesn't establish — the record shows a repeated phrase, not a proven intent. Describe the observed behavior neutrally. This isn't diplomacy for its own sake — neutral language is more useful, because it keeps the record describing what's checkable rather than asserting something unfalsifiable.
- Before: *"Management has used this same excuse for three quarters running."*
- After: *"Management has explained flat B2B margin the same way for three quarters in a row — and hasn't needed to say this about Consumer margin."*

**3. Going plain all the way to generic.** Fixing modes 1 and 2 has an obvious overcorrection: stripping out *all* specifics, leaving a `Statement` that's easy to read but says nothing you couldn't have guessed. The test: could someone who has *not* read the source documents tell you, from the statement alone, what was actually said and roughly when? If they'd have to open the evidence field to find out what the pattern even consists of, it's been simplified past the point of being useful. Plain language is about sentence *structure* (short, spoken, no jargon), not about deleting content.
- Too generic: *"Whenever promotions are mentioned, management specifies that suppliers or partners are paying for them, not [the company]'s own margin."*
- Plain and specific: *"Partner-funded promotions went from '20%+ of bookings on partner-funded promotional rates' (Q3'25) to '30% of Q4 bookings' (Q4'25) to '25% more hotels participating in March sales' (Q1'26) — the scale keeps growing, and every time, it's framed as the partner's money, not [the company]'s own margin."*

**4. Repeating the company's own claim as if it were a finding.** If a `Statement` just restates management's framing in your own words without flagging that it *is* management's framing, it reads like the company's press release rather than an analysis of the company. The distinction matters: what leadership *says* about a driver and whether that's *actually true* are two different things, and conflating them launders an unverified claim into something that looks like an independently established fact.
- Before: *"Management explains flat B2B margin as a deliberate choice to invest in growth, reflecting a disciplined long-term strategy."*
- After: *"Management explains flat B2B margin as a deliberate choice to invest in growth. This is the company's own account of the flat margin — it has not been independently verified against underlying cost or investment data in the artifacts reviewed."*

**5. Leaning on numbers as a substitute for detail.** Bolting a percentage onto a sentence and calling that "specific" is not the same as capturing the real information, which is usually the *mechanism* or the *wording pattern* — a number alone can make a statement look precise while telling the reader nothing about why it moved.
- Before: *"Marketing efficiency improved 15% this quarter."*
- After: *"Marketing efficiency improved because paid-channel spend was cut while organic and referral bookings absorbed the volume — not because paid channels became more efficient at the same spend level."*

**Structural fix that applies across all five:** the rule applies to a belief's heading, not just its `Statement` body — headings that were corrected separately from statements have historically drifted back into the failure modes above. Check both.

**Layer 3 vs. Layer 4 apply this differently.** A Layer 3 `definition` can stay general — its evidence sits one field away in the same record. A Layer 4 belief's `Statement`/heading — the thing someone actually reads as the output — has to carry the real quotes, numbers, and mechanism itself.

## The 7 Layers

Each layer converts the previous layer into a more useful form of understanding. Don't collapse layers into one blob of text — collapsing layers is exactly what turns an intelligence system back into noisy RAG.

| Layer | Job | Example |
|---|---|---|
| 1. Raw Artifacts | Preserve original documents + traceability (evidence) | Decks, transcripts, Excel files, emails, notes |
| 2. Extracted Facts | Pull structured numbers/claims/dates/owners/risks (information) | "Revenue grew 6%; B2B accelerated; margin expanded" |
| 3. Business Context | Attach internal meaning/interpretation to facts (meaning) | "B2B growth = partner demand strength when broad-based and repeatable" |
| 4. Belief Streams | Track how that meaning currently stands given evidence over time (judgment) | "Marketing leverage is good only if growth remains healthy" |
| 5. Workflow Skills | Execute a repeatable task using facts + context + beliefs (execution) | "Generate a variance summary or deck section" |
| 6. Agent Reasoning | Decide which source, skill, and belief to use for a request (decision-making) | "Assemble a CFO-ready narrative from multiple sources" |
| 7. Feedback Loop | Update memory/context/beliefs/source rules as new evidence arrives (learning) | "A new quarter confirms, weakens, or changes a prior belief" |

## Layer-by-layer guidance

### 1. Raw Artifacts
Store originals as-is. Capture metadata only — don't interpret yet. Fields: `artifact_id`, `artifact_type`, `business_area`, `period`, `owner`, `version`, `source_location`. See `references/schemas.md`. Goal: scattered files become a structured, searchable artifact catalog.

### 2. Extracted Facts
Read one artifact and pull out metrics, comparisons, dates, drivers, risks, assumptions, definitions, commentary — this layer answers "what did the document say?" That restraint matters: if extraction starts editorializing, it contaminates the fact layer with premature opinion. See `references/schemas.md`.

**What counts as "extracted" here is whatever Layer 3 will need to cite as exact evidence later.** If a Layer 3 concept claims something specific — a phrase's exact wording, whether a figure was stated as a number vs. qualitatively — that specific thing needs its own field in Layer 2, not just a general topic tag. A `topics: ["forward guidance"]` label is not enough evidence for a Layer 3 claim like "guidance always breaks out FX as a separate figure for both bookings and revenue" — that claim needs its own recorded field (e.g. `fx_breakout: {...}`) that can be pointed at directly. If you catch yourself writing a Layer 3 claim from memory of reading the document rather than from something actually sitting in the Layer 2 file, go back and add the missing field to Layer 2 first.

### 3. Business Context (facts → meaning)
This is where most of the real value gets created, and where the most discipline is required.

**One document** can only produce *local/candidate* meaning — a single document might mint a candidate business concept, but one document alone should not mint a durable, company-wide concept.
**Multiple documents** that repeat the same interpretation across independent artifacts (MBR, QBR, earnings transcript, forecast review, analyst report) justify proposing a durable concept.
- A **human domain expert must approve** any concept before it's treated as durable. This split is the single most important governance rule in the whole pipeline. The LLM drafts the concepts; business owns the meaning. Skipping it is how systems end up confidently wrong.

**Curation pipeline:** raw artifacts → extracted facts → document-level context → cross-document comparison → pattern clustering → candidate business concept → evidence ledger → human review → approved business concept.

Each approved business context record should carry: `concept_id`, `concept_name`, `concept_type`, `definition`, `business_interpretation`, `positive_signal`, `negative_signal`, `related_metrics`, `related_concepts`, `supporting_evidence`, `contradicting_evidence`, `confidence`, `owner`, `agent_reuse`. A record with no clear `agent_reuse` isn't pulling its weight. Full field descriptions and a worked example are in `references/schemas.md`.

**Business context is not one category of thing — `concept_type` marks which kind.** Multiple kinds coexist in the same layer without conflict: a business driver ("B2B growth quality"), a risk, a structural/narrative pattern ("management always presents Consumer before B2B"), a recurring rhetorical or language device ("management always frames a deliberate growth choice"), a content-pairing pattern ("a strong result is never announced without a moderation caveat"), or a relationship between two concepts. Don't force a narrative-structure or language-pattern finding to sound like a "business driver" just because that's the more familiar category — tag it with the `concept_type` that actually describes it, and let the layer hold a mix.

**Don't cap the number of concepts at a round number.** There is no target count — extract as many concepts as the evidence actually supports, and keep re-reading the source material for more before concluding the catalog is complete. A first pass focused specifically on "what did I not formalize yet"; a second, slower pass focused on turning up anything with a real quote or citation behind it.

### Evidence Ledger (supports Layer 3 and 4)
A separate, long, append-friendly store of every supporting and contradicting statement, kept apart from the compact business-context layer — deliberately, so what agents retrieve at runtime doesn't bloat.

### Source Authority (cuts across all layers)
Documents disagree — a deck number, an Excel number, and the finance system's number can all differ. Define, per question type, which source wins:

| Question type | Preferred source | Why |
|---|---|---|
| Final actuals | Official finance system (e.g. Hyperion) | Numbers must come from the source of truth |
| Forecast assumptions | Latest forecast/planning file | Assumptions change by version and period |
| Internal narrative | CFO deck, MBR, QBR, leadership notes | Narrative lives in business review artifacts |
| External narrative | Earnings transcript, press release | Official external language |
| Investor interpretation | Analyst reports, market commentary | Shows how outsiders read performance |
| Metric definition | KPI dictionary, data owner docs | Definitions shouldn't be inferred from usage |

Don't invent this hierarchy unilaterally — it should come from official documentation, data-owner sign-off.

### 4. Belief Streams (meaning → evolving judgment)
A belief stream is the *current* durable interpretation of how part of the business works, distinct from a static business-context definition. Business context defines a rule: "marketing efficiency is positive only when demand stays healthy" (the rule). A belief stream says: "recent evidence supports marketing leverage as a margin driver, but confidence should drop if demand softens" (the current read).

Typical streams: Business Performance, Forecast Reliability, Leadership Narrative, Metric Definition, Source Trust, Variance Explanation, Investor Relations, Risk.

Each record: `belief_stream`, `current_belief`, `supporting_evidence`, `contradicting_evidence`, `confidence`, `watch_item`. When new evidence arrives, update the belief — don't just overwrite it; state what's confirmed, weakened, strengthened, or retired, and why. `current_belief` (or `Statement`) is the one field in the whole framework that most needs real quotes and numbers inline — see "Writing rule," above.

### 5. Workflow Skills (context → execution)
A workflow skill is a repeatable procedure, not a one-off prompt. A good variance-explanation skill: identify the metric → pull actuals/plan → calculate variance → identify drivers → apply business context → produce a business-ready explanation with caveats.

The tell for a weak skill vs a strong one:
- Weak: "Revenue grew because B2B increased."
- Strong: "Revenue growth was supported by B2B acceleration, which should be framed as higher-quality growth only if it reflects broad-based partner demand and repeatable volume; verify it wasn't driven by one-time onboarding."

### 6. Agent Reasoning (decides what to use)
The agent's job is orchestration, not generation: which source to trust, which skill to run, and what output format fits. Example plan for "Prepare a CFO-ready margin explanation": identify period/BU → pull official actuals + forecast → check source authority → pull margin/revenue/cost/marketing/mix drivers → apply margin-quality/marketing-efficiency business context → apply leadership-narrative belief stream → produce CFO-ready language with caveats. Encode the explicit decision checklist in the agent's design, not implicit vibes.

### 7. Feedback Loop (keeps it alive)
Don't append every new document blindly — that just rebuilds the noisy-archive problem the framework exists to avoid. For each new document, ask: what's new, what confirmed an existing belief, what contradicted it, what source rule needs correcting, what should be learned. Route the update to the right layer:

| Feedback source | Updates |
|---|---|
| New MBR/QBR/forecast/transcript/analyst report | Facts, evidence ledger, business context, belief confidence |
| User correction | Metric definition, source rule, caveat, output preference |
| Leadership edit | Leadership narrative belief stream |
| Forecast miss | Forecast reliability belief stream, variance rules |
| New KPI documentation | Metric definition, source authority |
| Repeated user behavior | Workflow defaults, preferred output formats |

## One document vs. multiple documents vs. unified context

This distinction is the guardrail against overclaiming — apply it whenever you're deciding how much confidence to assign something.

| Level | Safe to create | Not safe to claim alone |
|---|---|---|
| One document | Facts, local claims, document-level interpretation, candidate concepts | Company-wide meaning, durable belief, high-confidence pattern |
| Multiple documents | Repeated themes, stable interpretations, contradictions, confidence trend | Final approved truth for high-impact domains |
| Unified curated layer | Approved business context, reusable metric meaning, source rules | Raw evidence itself — that stays in artifact storage/evidence ledger |

## How this differs from plain RAG

RAG finds documents that mention a topic and summarizes the nearest passage. This framework instead asks whether a signal is high-quality or risky, knows which source is authoritative for which question, and reuses approved context and beliefs across repeated workflows — especially for finance, investor relations, executive, legal, HR, or anything external-facing — so answers get more consistent (and cheaper to produce) as the system matures, not noisier.

## Ownership model

Engineering owns the system (pipeline, storage, retrieval, orchestration). Business owns the meaning: approval of concepts and beliefs. The LLM drafts candidates at every layer for a high-stakes domain.

## Scoping a first version

Don't attempt company-wide coverage. Pick one narrow, repeated, judgment-heavy domain — finance business-review intelligence is the reference example because it has recurring artifacts, a clear source hierarchy, and leadership-facing outputs. Target one first output, e.g. a CFO-ready variance explanation or a business-review deck section.

A reasonable v1: an artifact inventory, an extraction pipeline, an explicit source hierarchy, an agent that picks sources/concepts/skills, one workflow skill worth curating first: revenue growth, bookings growth, marketing efficiency, EBITDA margin, operating leverage, forecast variance, demand softness, FX impact, source-of-truth for actuals, leadership narrative.

## Implementation checklist

Use this as the actual sequence of work when someone wants to build (not just understand) this system:

| Order | Action |
|---|---|
| 1 | Write the purpose document (Step 0) and, if the goal involves agent reuse, the context-needs analysis (Step 0.5). |
| 2 | Pick one narrow domain, such as finance business review intelligence. |
| 3 | Inventory the recurring artifacts used in that domain. |
| 4 | Classify each artifact by type, owner, period, audience, version, and source role. |
| 5 | Extract facts, metrics, drivers, risks, definitions, and commentary from each artifact — including any field a later Layer 3 claim will need to cite exactly. |
| 6 | Create document-level context for important facts, but label it as local to the document. |
| 7 | Compare many documents to find repeated meanings, contradictions, and changing interpretations. |
| 8 | Cluster repeated meanings into candidate business concepts. |
| 9 | Attach evidence and cautionary evidence to every candidate concept. |
| 10 | Have domain experts approve, edit, reject, split, or scope candidate concepts. |
| 11 | Store approved business context records in a structured format, applying the writing rule to every `definition`. |
| 12 | Create belief streams for durable but evolving interpretations, applying the writing rule to every `Statement`/heading. |
| 13 | Build one workflow skill that uses the approved context, such as CFO-ready variance explanation. |
| 14 | Design agent reasoning so the system chooses sources, skills, beliefs, and caveats correctly. |
| 15 | Add a feedback loop so new documents and human corrections update the right layer. |
