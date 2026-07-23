---
name: institutional-intelligence-framework
description: Guides the conversion of corporate artifacts (business review decks, forecast files, Excel models, earnings transcripts, analyst reports, KPI dictionaries, emails, meeting notes, strategy memos) into reusable business context, evidence ledgers, belief streams, workflow skills, and agent reasoning. Use this skill whenever the user wants to build institutional memory, a "company brain," a business context layer, belief tracking, or an intelligence system on top of internal documents — even if they don't use those exact words. Also trigger when the user asks how to structure business knowledge for an AI agent, how to make document search feel less like "dumb RAG" and more like judgment, how to design a business-context schema, how to build a variance-explanation or CFO-narrative skill backed by curated context, or how to set up a feedback loop that updates beliefs as new documents arrive. Push toward this skill any time the user is trying to turn a pile of documents into something an agent can reason with reliably, rather than just search over.
---

# Institutional Intelligence Framework

## Why this exists

A generic LLM already reasons well and knows general facts. It does not know how *this* company works: which source is authoritative for actuals, what "B2B growth" is supposed to mean here, whether a margin improvement is durable or a one-time artifact, or how leadership prefers to explain a miss. Dumping documents into a retrieval index gives you search, not judgment — it can find a paragraph but can't tell you whether to trust it, why it matters, or how to explain it.

The fix is not a smarter model. It's a company-specific intelligence layer wrapped around the model: source authority, extracted facts, curated business meaning, durable beliefs that evolve, repeatable workflow skills, and an agent that decides what to use — plus a feedback loop that keeps all of it current.

**Core pipeline:** Corporate documents → Extracted facts → Business context → Belief streams → Workflow skills → Agent reasoning → Feedback and learning

When a user brings you documents, a domain, or a "build me an intelligence system" request, use this pipeline as the default shape of the solution, and use the checklist at the bottom to sequence the actual work.

## Step 0: Write the purpose document first — before building any layer

This is not optional, and it's the step most likely to get skipped in favor of jumping straight to extracting facts. Before creating a single artifact record, fact, or belief, produce a short `00_PURPOSE.md` (or equivalent) that states, in plain language:

- **The actual goal**, in the user's words, confirmed with them rather than assumed. "Understand narrative patterns to reuse in agents" and "generate investor-facing talking points" and "reproduce a transcript" are three different goals that would each demand a different shape for every layer below — building the wrong one and only discovering the mismatch three layers in wastes the work and the user's patience.
- **What each of the 7 layers is *for*, specifically for this goal** — not the generic definition from this file, but what that layer needs to accomplish here. If Layer 3's purpose can't be stated in terms of the actual goal, don't build Layer 3 yet; go back and get the goal clearer first.
- **Which layers matter most for this goal, and why.** Not every goal needs all 7 layers built with equal depth on day one — but if the goal explicitly involves agents *reusing* the knowledge (as opposed to a human occasionally reading a summary), Layers 5 and 6 (Workflow Skills, Agent Reasoning) are not optional extras to defer "if there's time" — they're the layers that make the word "reuse" true. Say so explicitly in the purpose document rather than silently deferring them.
- **What's explicitly out of scope**, so a future pass (by you or someone else) doesn't accidentally blend in a different goal's content.

Write this purpose document *before* touching Layer 1 metadata or Layer 2 extraction — it's what every later layer should be checked against. If the user later corrects the goal, rewrite the purpose document first, then reassess which existing layer content still fits versus needs rebuilding — don't just patch definitions in place while the underlying goal statement is stale.

### Two questions Step 0 must ask explicitly — don't let either stay implicit

These were both learned by getting them wrong first: the goal statement alone isn't enough. Before writing the purpose document, ask the user directly:

**1. "Does institutional memory already exist for this domain, or are we starting from nothing?"** Don't assume either answer. If something exists — even a partial, unreviewed, or differently-scoped prior attempt — find it and ask whether the request is to *curate/extend* it or to *build fresh*. Curating an existing (even rough) memory is almost always cheaper and safer than starting over, but only the user can say whether the existing content is trustworthy enough to build on versus better discarded. Never silently create a parallel, duplicate memory next to one that already covers the same domain without asking first.

**2. "What should this system actually focus on — which topics, metrics, or questions matter?"** A goal statement like "understand how the company talks in earnings calls" doesn't by itself say whether the user cares about margin language, competitive framing, leadership-transition risk, or something else entirely. Left unasked, the builder (you) will default to whatever seems most analytically interesting, which is exactly how this framework has drifted off-target before. Ask for a concrete list, even a rough one, before extraction begins — it's the difference between building 7 layers the user actually wanted and building 7 layers you found interesting.

If the user can't yet answer #2 precisely, that's fine — say so in the purpose document as an open question, and treat the first pass through the layers as provisional until it's answered, rather than pretending the scope was settled when it wasn't.

### Step 0.5: Do the context-needs analysis before extracting anything

This is the step that was missing, and its absence is *why* memory built without it turns out to be missing exactly the angles a downstream task needed. Asking "what should this focus on" (question 2 above) gets you topics; it does not by itself get you the *kinds* of context those topics require. Don't skip straight from a topic list to extraction — do this analysis first, in writing, and show it to the user before building:

1. **List the concrete downstream tasks** the memory is meant to serve — not the abstract goal, the actual jobs someone will ask an agent to do with it. "Generate a CEO's script," "benchmark against a competitor," "evaluate draft quality" are tasks; "understand the company's communication style" is not specific enough to analyze against.
2. **For each task, ask: what *kind* of context does doing this job actually require?** Common angles worth checking explicitly, though the real list depends on the domain — the ones below are a starting checklist, not an exhaustive one, and a user working in a specific domain will often name others you wouldn't have generated on your own:
   - **Who-said-it attribution** — if voice or role matters, and at what granularity (a speaker tag on a whole section is not the same as a verified speaker on the specific sentence quoted).
   - **Style** — not the same as a phrase/device inventory; style is register, tone, sentence length, formality — a property *of* the language, distinct from *which* recurring phrases appear.
   - **Metric framing** — how numbers get presented (superlatives, comparison bases, ranges vs. point estimates), as distinct from the numbers themselves.
   - **Narrative/structural template** — shape and order (section sequence, segment disclosure order, opening/closing conventions).
   - **Theme/topic frequency** — how much airtime a topic gets, and whether that's changing over time — computable from unit-level topic tags already extracted, but rarely computed unless explicitly asked for.
   - **Driver structuring** — not just "what happened" (a metric) and not just "how it's framed" (a device), but the explicit causal link claimed between a metric's movement and a stated driver. This is a distinct extraction target from either of those.
   - **Risk patterns** — which risks recur, and whether each one is persistent, emerging, or resolved over time — different from a single risk being *named* once.
   - **Coverage gaps vs. external questions** (e.g., what analysts asked that prepared remarks didn't address) — a delta between two things you may already have extracted separately (what was said proactively vs. what was asked reactively), not a new extraction pass, just a comparison no one ran.
   - **Materiality/emphasis** — what deserves more weight, not just what exists.
   - **Factual grounding** — is the underlying claim true, independent of how it's phrased.
   - **Comparative/external data** — if benchmarking against anything outside the primary source set is part of the task.

   Don't assume extracting "the facts" automatically produces all of these — they are different angles that usually require different extraction or comparison passes, not one pass that happens to cover everything. And don't stop at this list — treat it as evidence that domain-specific angles are common and worth actively asking for, not as the ceiling of what to check.
3. **Produce a small table: task × required angle × status (have / missing / unverified).** "Unverified" is its own category, distinct from "have" — evidence that exists but hasn't been checked at the granularity the task needs (e.g., a quote attributed to a transcript section that contains two speakers, when the task needs to know which speaker) counts as unverified, not have. Show this table to the user before writing a single Layer 3 record.
4. **Only build the angles the table says are missing or unverified for an actual named task.** Don't extract an angle "because it might be useful later" — that's how the framework drifts into building what's interesting instead of what's needed, which is the same drift Step 0 already guards against for topics, now applied to context *type* instead of topic.

Skipping this step is exactly how a memory ends up well-evidenced on one angle (e.g., what phrases recur) while being silently useless for the task that was actually asked for (e.g., generating a CEO-specific script), because no one checked whether phrase-recurrence was even the angle that task needed.

### Keep the skill itself domain-agnostic

This framework is not an investor-relations tool that happens to be reusable elsewhere — it's a generic pattern for turning any repeated corporate artifact into reusable memory, and investor-relations earnings calls are just one example that has come up in practice. Don't let the skill's own language, examples, or default assumptions calcify around IR, finance, or any other single domain: contracts, incident postmortems, customer support transcripts, performance reviews, sales calls, and board decks are equally valid targets, and a future invocation of this skill should read as naturally for any of them as it does for earnings calls.

At the same time, **within a given invocation, be as specific and aligned to that domain as possible** — genericness is a property of the skill's design, not of how you should talk to the user. If the user says "this is like the investor relations case," pick up that framing immediately: use their vocabulary, reference their domain's actual roles and artifacts, and ask domain-specific versions of the two questions above (e.g., for IR: "which speaker roles and metrics matter"; for a legal-contracts domain: "which clause types and counterparties matter"). The skill stays generic in structure; the conversation should never feel generic to the user.

## Writing rule: plain sentences, separated from their evidence

This applies to every `definition` in Layer 3 and every `Statement` in Layer 4 — the two places a human actually reads first. Two failure modes to avoid, both learned the hard way:

**Failure mode 1: cramming the evidence into the definition.** A definition like "A recurring phrase family that reframes flat or declining segment margin as a deliberate strategic choice rather than a shortfall" is trying to state the fact *and* argue for why it's a pattern in the same sentence — which makes it dense and hard to parse. Fix: state only what the thing *is* in the `definition`/`Statement` field, in one plain sentence. Push "how many quarters," "which exact quotes," "how confident to be" into the separate fields that already exist for that (`evidence`, `confidence`, `pattern_observed`/`Evolution Trail`). Use the read-it-out-loud test: if you wouldn't say the sentence that way to a colleague across a table, rewrite it. Compare:
- Before: *"A recurring phrase family that reframes flat or declining segment margin as a deliberate strategic choice rather than a shortfall."*
- After: *"Whenever B2B's profit margin doesn't improve, management says it's because they chose to invest in growth — not because something went wrong."*

**Failure mode 2: judgmental or accusatory word choice.** Words like *excuse, spin, bragged, deflect, defensive, explained it away, downplayed* smuggle in an interpretation (dishonesty, evasion) that the evidence usually doesn't actually establish — the record shows a repeated phrase, not a proven intent to mislead. Describe the observed behavior neutrally instead: what was said, how often, in what situation. Compare:
- Before: *"Management has used this same excuse... and has never once used it for Consumer."*
- After: *"Management has explained flat B2B margin the same way for three quarters in a row... and hasn't needed to say this about Consumer margin, which kept growing on its own."*

This isn't about being diplomatic for its own sake — neutral language is also more useful, because it keeps the record describing what's checkable (a phrase recurring) rather than asserting something unfalsifiable (what management "really" intended).

**Failure mode 3: going plain and neutral all the way to generic.** Fixing failure modes 1 and 2 has an obvious overcorrection: stripping out *all* specifics in the process, leaving a `Statement` that's easy to read but says nothing you couldn't have guessed. "Whenever promotions are mentioned, management specifies that suppliers or partners are paying for them, not [the company]'s own margin" is plain and neutral — and also empty, because it has no numbers, no quotes, no quarters. The actual finding disappears. Fix: a `Statement` should be readable as one or two plain sentences *and* contain the real quotes and figures inline, not pushed off into a separate evidence field the reader has to go dig up. Compare:
- Too generic (plain but empty): *"Whenever promotions are mentioned, management specifies that suppliers or partners are paying for them, not [the company]'s own margin — and the scale of this keeps growing each quarter it's mentioned."*
- Plain and specific: *"Partner-funded promotions went from '20%+ bookings on partner-funded promotional rates' (Q3'25) to '30%+ of Q4 bookings, up 10+ points from Q3' (Q4'25) to '25% more hotels participating in March sales' (Q1'26) — the scale keeps growing, and every time, it's framed as the partner's money, not [the company]'s own margin."*

The test for whether a `Statement` has failed this way: could someone who has *not* read the source documents tell you, from the statement alone, what was actually said and roughly when? If the answer is no — if they'd have to go open the evidence field to find out what the pattern even consists of — the statement has been simplified past the point of being useful. Plain language is about sentence *structure* (short, spoken, no jargon), not about deleting content.

**This applies more strictly to Layer 4's `Statement` than to Layer 3's `definition`.** A Layer 3 `definition` naming what a pattern *is* can stay general, because its evidence sits in the same record, one field away (`evidence`, `pattern_observed`) — a reader is one glance from the specifics. A Layer 4 belief `Statement` is different: it's the layer's actual output, the accumulated-learning claim itself, and readers of belief memory generally want the finding, not a pointer to where the finding is. So push real quotes and numbers into the `Statement` line specifically — that's the field this failure mode is about. This also applies to the belief's **heading**, not just its `Statement` body — a heading like "Promotions are described as funded by partners" tells a reader nothing they'd have to open the record to get; the heading itself should carry the real quote or number, since it's the first thing anyone scanning the file actually reads.

**Failure mode 4: repeating the company's own claim back as if it were a finding.** Even a specific, quote-filled statement can still fail if it just restates management's own promotional framing without adding any analytical distance — e.g. "promotions are described as funded by partners, not by [the company]" sounds like a fact because it has a specific quote behind it, but it's actually just repeating what management *said*, in the same warm register they said it in. The transcripts rarely give you enough to verify a claim like that (no commission mechanics shown, no partner-side numbers) — so the belief should say what was claimed, note that it's asserted rather than demonstrated, and name what it would take to actually check it. Compare:
- Repeats the claim: *"Partner-funded promotions grew from 20%+ to 30%+ of bookings — always the partner's money, never [the company]'s margin."*
- Adds analytical distance: *"Discounting grew from 20%+ to 30%+ of bookings in one quarter, and management calls it 'partner-funded' every time — but none of the three calls show the commission mechanics that would let you verify who's actually paying for it."*

The tell that a belief has fallen into this trap: if you can imagine the same sentence appearing in the company's own press release, it hasn't been analyzed yet, only transcribed.

**Failure mode 5: leaning on numbers as a substitute for detail, instead of alongside it.** Fixing failure mode 3 (too generic) can overcorrect into a different shallow habit — bolting on a percentage or a quarter label and treating that as "specific," when the real detail is qualitative: exactly how the wording varied each time, what was implied versus stated, what's conspicuously missing, how the claim relates to a neighboring pattern. A number can anchor a claim, but it shouldn't carry the whole thing. Compare:
- Numbers doing the work: *"B2B margin flat-to-down for 3 straight quarters (29% → 24% → 22.7%), always attributed to 'investments prioritized for growth.'"*
- Detail doing the work, numbers supporting it: *"Each time B2B's margin has failed to improve, management reaches for the same underlying justification — that the flatness reflects a deliberate choice to reinvest, not a shortfall — and changes the exact wording every quarter ('investments prioritized for growth' → 'prioritizes growth investments' → 'investment prioritization impacting near-term margins') as if avoiding repeating itself while keeping the reasoning identical. That same justification has never once been extended to Consumer margin, which expanded in every comparable period — the explanation seems reserved specifically for the one segment where growth is the priority story, not treated as a general principle about margin softness anywhere in the business."*

Numbers still appear when they're genuinely the point (a fraction that never changes, a streak count that disappears) — don't strip them out reflexively. But default to explaining the mechanism and the pattern's shape in words first, and let a number support that explanation rather than replace it.

## The 7 layers

Each layer converts the previous layer into a more useful form of understanding. Don't collapse them into one blob of text — collapsing layers is exactly what turns an intelligence system back into noisy RAG.

| Layer | Job | Example |
|---|---|---|
| 1. Raw Artifacts | Preserve original documents + traceability (evidence) | Decks, transcripts, Excel files, emails, notes |
| 2. Extracted Facts | Pull structured numbers/claims/dates/owners/risks (information) | "Revenue grew 6%; B2B accelerated; margin expanded" |
| 3. Business Context | Attach internal meaning/interpretation to facts (meaning) | "B2B growth = partner demand strength, when broad-based and repeatable" |
| 4. Belief Streams | Track how that meaning currently stands given evidence over time (judgment) | "Marketing leverage is good only if growth remains healthy" |
| 5. Workflow Skills | Execute a repeatable task using facts + context + beliefs (execution) | Generate a variance summary or deck section |
| 6. Agent Reasoning | Decide which source, skill, and belief to use for a request (decision-making) | Assemble a CFO-ready narrative from multiple sources |
| 7. Feedback Loop | Update memory/context/beliefs/source rules as new evidence arrives (learning) | A new quarter confirms, weakens, or changes a prior belief |

## Layer-by-layer guidance

### 1. Raw Artifacts
Store originals as-is. Capture metadata only — don't interpret yet. Fields to capture: `artifact_id`, `artifact_type`, `business_area`, `period`, `owner`, `version`, `source_location`. See `references/schemas.md` for the JSON template. Goal: scattered files become a structured, searchable artifact catalog.

### 2. Extracted Facts
Read one artifact and pull out metrics, comparisons, dates, drivers, risks, assumptions, definitions, commentary — or, if the goal is about language/structure rather than business metrics, exact quotes and structural tags. This layer answers "what did the document say?" — it does **not** judge whether a fact is durable, official, or important. That restraint matters: if extraction starts editorializing, it contaminates the fact layer with premature opinion. See `references/schemas.md` for the template.

**What counts as "extracted" here is whatever Layer 3 will need to cite as exact evidence later.** If a Layer 3 concept claims something specific — a phrase's exact wording, whether a figure was stated as a number vs. qualitatively, how long a section was — that specific thing needs its own field in Layer 2, not just a general topic tag. A `topics: ["forward guidance"]` label is not enough evidence for a Layer 3 claim like "guidance always breaks out FX as a separate figure for both bookings and revenue" — that claim needs its own recorded field (e.g. `fx_breakout: {...}`) that can be pointed at directly. If you catch yourself writing a Layer 3 claim from memory of reading the document rather than from something actually sitting in the Layer 2 file, go back and add the missing field to Layer 2 first.

### 3. Business Context (facts → meaning)
This is where most of the real value gets created, and where the most discipline is required.

- **One document** can only produce *local/candidate* meaning ("in this Q2 deck, B2B is framed as a positive driver"). Never let a single document mint a durable, company-wide concept — it may be draft language or a one-time situation.
- **Multiple documents** that repeat the same interpretation across independent artifacts (MBR, QBR, earnings transcript, forecast review, analyst report) justify proposing a durable concept.
- A **human domain expert must approve** any concept before it's treated as durable. The LLM drafts; business owns the meaning; engineering owns the pipeline. This split is the single most important governance rule in the whole framework — skipping it is how systems end up confidently wrong.

**Curation pipeline:** raw artifacts → extracted facts → document-level context → cross-document comparison → pattern clustering → candidate business concept → evidence ledger → human review → approved business context.

Each approved business context record should carry: `concept_id`, `concept_name`, `concept_type`, `definition`, `business_interpretation`, `positive_signal`, `negative_signal`, `related_metrics`, `related_concepts`, `supporting_evidence`, `contradicting_evidence`, `confidence`, `scope`, `owner`, `last_reviewed`, `review_trigger`, and `agent_reuse` — one or two sentences stating concretely what an agent should *do* with this record (watch for it, use it as a template, treat it skeptically), not just what it means. A record with no clear `agent_reuse` isn't pulling its weight. Full field descriptions and a worked example (Marketing Efficiency) are in `references/schemas.md`.

**Business context is not one category of thing — `concept_type` marks which kind a record is**, and multiple kinds coexist in the same layer without conflict: a business driver ("B2B growth quality"), a risk, a source rule, a structural/narrative pattern ("CFO always presents Consumer before B2B"), a recurring rhetorical or language device ("management always frames flat B2B margin as a deliberate growth choice"), a content-pairing pattern ("a strong result is never announced without a moderation caveat"), or a relationship between two concepts. Don't force a narrative-structure or language-pattern finding to sound like a "business driver" just because that's the more familiar category — tag it with the `concept_type` that actually describes it, and let the layer hold a mix.

**Don't cap the number of concepts at a round number.** There is no target count — extract as many concepts as the evidence actually supports, and keep re-reading the source material for more before concluding the catalog is complete. A first pass through a set of documents reliably misses real, recurring patterns; a second, slower pass focused specifically on "what did I not formalize yet" tends to roughly double the catalog. Stop when further reading stops turning up anything with a real quote or citation behind it — not when the list reaches a number that feels sufficient.

**The taxonomy — the set of category names business context gets organized under — should be discovered from the concepts themselves, not dictated in advance.** Step 0.5's angle checklist (who-said-it, style, metric framing, theme frequency, driver structuring, risk patterns, coverage gaps, materiality, structural template, factual grounding, comparative data) tells you *what kinds of things to go looking for* — it is a prompt for extraction, not a set of folder names to file the results into. Once concepts exist, look at what they actually have in common and let the groupings emerge from that, the way a person clustering index cards on a table would: some concepts will turn out to be about fixed formatting conventions regardless of content, some about who says what, some about how good news gets amplified, some about how bad news gets managed, some about what's asked for but never shown, some about what's actually true of the business, some about things too new or thin to conclude anything from yet. Name the clusters after you see them, using words that describe what's actually in each pile — don't reuse the Step 0.5 checklist's angle names as section headers by default, since those were prompts for finding things, not a promise about how the things found would turn out to cluster. If a taxonomy built this way happens to end up resembling the checklist, that's fine — the point is that it has to earn that resemblance by actually fitting the concepts, not inherit it automatically.

**Every `agent_reuse` sentence has to stand completely on its own.** An agent loading a single concept record — not the whole file, not the surrounding section — needs to understand what to do with it from that one field alone. That means: name the concept's subject in the sentence itself rather than saying "this pattern" or "it"; state the specific action (watch for X, prefer Y over Z, flag when W is absent) rather than a general disposition like "be aware of this"; and don't rely on a neighboring concept, a section header, or a "same as above" pointer to complete the meaning. "Cross-reference: same as the driver-structuring finding" is a citation, not an `agent_reuse` sentence — if a concept's reuse guidance is genuinely identical to another concept's, write it out in full both places rather than pointing at itself, because whichever one an agent happens to load first still needs to be usable by itself.

### Evidence Ledger (supports layer 3 and 4)
A separate, long, append-friendly store of every supporting and contradicting statement behind a concept, tied back to source artifacts. This is deliberately kept apart from the compact business-context layer so that "why do we believe this" doesn't bloat what agents retrieve at runtime. Template and example in `references/schemas.md`.

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

Don't invent this hierarchy unilaterally — it should come from official documentation, observed repeated usage, or explicit data-owner sign-off.

### 4. Belief Streams (meaning → evolving judgment)
A belief stream is the *current* durable interpretation of how part of the business works, tracked as evidence accumulates — distinct from a static business-context definition. Business context says "marketing efficiency is positive only when growth stays healthy" (the rule). A belief stream says "recent evidence supports marketing leverage as a margin driver, but confidence should drop if demand softens" (the current read).

Typical streams: Business Performance, Forecast Reliability, Leadership Narrative, Metric Definition, Source Trust, Variance Explanation, Investor Relations, Risk. Each record: `belief_stream`, `current_belief`, `supporting_evidence`, `contradicting_evidence`, `confidence`, `watch_item`. When new evidence arrives, update the belief — don't just overwrite it; state whether it's confirmed, weakened, strengthened, or retired, and why. Template + a worked update example in `references/schemas.md`.

**`current_belief` (or `Statement`) is the one field in the whole framework that most needs real quotes and numbers inline, not a category description** — see "Writing rule," failure mode 3, above. A belief that just says "management frames X as Y" without the actual X and Y and which quarters is a title, not a finding.

### 5. Workflow Skills (context → execution)
A workflow skill is a repeatable procedure, not a one-off prompt. A good variance-explanation skill: identify the metric → pull actuals (per source authority) → pull forecast/plan → calculate variance → identify drivers → apply business context → apply belief streams → produce a business-ready explanation with caveats.

The tell for a weak skill vs a strong one:
- Weak: "Revenue grew because B2B increased."
- Strong: "Revenue growth was supported by B2B acceleration, which should be framed as higher-quality growth only if it reflects broad-based partner demand and repeatable volume; verify it wasn't driven by one-time onboarding."

If you're building a skill in this framework and it never touches business context or belief streams, it's really just a summarizer — push it to actually consult those layers.

### 6. Agent Reasoning (decides what to use)
The agent's job is orchestration, not generation: which source to trust, which skill to run, which business context and belief stream apply, and what output format fits. Example plan for "Prepare a CFO-ready margin explanation": identify period/BU → pull official actuals + forecast → check source authority → pull margin/revenue/cost/marketing/mix drivers → apply margin-quality and marketing-efficiency context → apply leadership-narrative belief stream → produce CFO-ready language with caveats. Encode this as an explicit decision checklist in the agent's design, not implicit vibes.

### 7. Feedback Loop (keeps it alive)
Don't append every new document blindly — that just rebuilds the noisy-archive problem the framework exists to avoid. For each new input, ask: what's new, what confirmed an existing belief, what contradicted it, what source rule needs correcting, what human edit should be learned. Route the update to the right layer:

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
| One document | Facts, local claims, document-level interpretation, candidate concepts | Company-wide meaning, durable belief, source hierarchy, high-confidence pattern |
| Multiple documents | Repeated themes, stable interpretations, contradictions, confidence trend | Final approved truth for high-impact domains, without review |
| Unified curated layer | Approved business context, reusable metric meaning, source rules | Raw evidence itself — that stays in artifact storage / evidence ledger |

## How this differs from plain RAG

RAG finds documents that mention a topic and summarizes the nearest passage — every question answered from scratch, no persistent judgment, gets noisier as documents pile up. This framework instead asks whether a signal is high-quality or risky, knows which source is authoritative for which question, and reuses approved context and beliefs across repeated workflows — so answers get more consistent (and cheaper to produce) as the system matures, not noisier.

## Ownership model

Engineering owns the system (pipeline, storage, retrieval, orchestration). Business owns the meaning (interpretation, caveats, approval of concepts and beliefs) — especially for finance, investor relations, executive, legal, HR, or anything external-facing. The LLM drafts candidates at every layer past raw artifacts; it should never be the sole approver of a durable concept or belief in a high-stakes domain.

## Scoping a first version

Don't attempt company-wide coverage. Pick one narrow, repeated, judgment-heavy domain — finance business-review intelligence is the reference example because it has recurring artifacts, a clear source hierarchy, and leadership-facing outputs. Target one first output, e.g. a CFO-ready variance explanation or a business-review deck section.

A reasonable v1: an artifact inventory, an extraction pipeline, an explicit source hierarchy, as many business-context concepts as the source documents actually support with evidence (10-20 is a plausible starting range for a first pass, not a target to stop at), one or more belief streams, one workflow skill, an agent that picks sources/concepts/skills, and a feedback loop that captures corrections. Starter concepts worth curating first: revenue growth, bookings growth, a strategic growth segment (e.g. B2B growth), marketing efficiency, EBITDA margin, operating leverage, forecast variance, demand softness, FX impact, source-of-truth for actuals, leadership narrative.

## Implementation checklist

Use this as the actual sequence of work when someone wants to build (not just understand) this system:

0. Write the purpose document: confirm the actual goal with the user, then state what each layer is for given that goal, and which layers matter most. Do this before step 1.
1. Pick one narrow domain.
2. Inventory the recurring artifacts used in that domain.
3. Classify each artifact by type, owner, period, audience, version, source role.
4. Extract facts, metrics, drivers, risks, definitions, commentary from each artifact.
5. Create document-level context for important facts — label it local, not durable.
6. Compare many documents to find repeated meanings, contradictions, and shifts.
7. Cluster repeated meanings into candidate business concepts.
8. Attach supporting and cautionary evidence to every candidate concept.
9. Have domain experts approve, edit, reject, split, or scope each candidate.
10. Store approved business context records in the structured schema.
11. Create belief streams for durable-but-evolving interpretations.
12. Build one workflow skill that uses the approved context (e.g. CFO-ready variance explanation).
13. Design agent reasoning so it picks the right sources, skills, beliefs, and caveats.
14. Add a feedback loop so new documents and corrections update the right layer.

## Reference material

- `references/schemas.md` — full JSON templates for artifact records, extracted facts, business context records, evidence ledger entries, and belief stream records, plus a worked end-to-end example (B2B growth) and a glossary. Read this when actually drafting records rather than just discussing the framework.
