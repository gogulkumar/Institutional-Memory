# Layer Schemas

Field templates for each layer, with a worked example. Keep these compact — the point of the layered design is that agents retrieve small, curated records, not long summaries.

## Layer 1: Raw Artifact

```json
{
  "artifact_id": "q2_2026_business_review_deck",
  "artifact_type": "Business Review Deck",
  "business_area": "Finance",
  "period": "Q2 2026",
  "owner": "FP&A Team",
  "version": "Final",
  "source_location": "SharePoint",
  "created_date": "2026-07-01"
}
```

| Field | Purpose |
|---|---|
| `artifact_id` | Stable identifier used by every downstream layer to cite this document. |
| `artifact_type` | e.g. MBR deck, QBR deck, forecast model, earnings transcript, analyst report, KPI dictionary. |
| `business_area` | Function or business unit the artifact belongs to. |
| `period` | Reporting period covered. |
| `owner` | Team or person accountable for the artifact. |
| `version` | Draft vs. Final — governs whether it's safe to cite as authoritative. |
| `source_location` | Where the original lives, for traceability. |

## Layer 2: Extracted Facts

```json
{
  "artifact_id": "q2_2026_business_review_deck",
  "facts": [
    {"type": "metric", "metric": "Revenue", "value": "+6%", "comparison": "YoY", "period": "Q2 2026"},
    {"type": "driver", "statement": "B2B acceleration supported revenue growth"},
    {"type": "profitability", "statement": "EBITDA margin expanded 180 basis points"},
    {"type": "risk", "statement": "Domestic demand softness remains a risk"}
  ]
}
```

Extract whatever a later Layer 3 claim will need to cite exactly — an exact phrase, whether a figure was quantitative or qualitative, a specific caveat. A general `topics` tag is not sufficient evidence for a specific downstream claim; give the specific thing its own field.

## Layer 3: Business Context

```json
{
  "concept_id": "marketing_efficiency",
  "concept_name": "Marketing Efficiency",
  "concept_type": "Business Driver",
  "definition": "The ability to generate bookings or revenue with lower relative marketing spend.",
  "business_interpretation": "Marketing efficiency is positive when bookings, revenue, and demand remain healthy while marketing spend intensity declines. It should be interpreted cautiously if margin improves mainly because spend was reduced, because that may create future demand risk.",
  "positive_signal": "Bookings or revenue grow while marketing spend as a percentage of revenue declines.",
  "negative_signal": "Margin improves while bookings, conversion, or demand weaken.",
  "related_metrics": ["Marketing spend", "Bookings", "Revenue", "Conversion", "EBITDA margin"],
  "related_concepts": ["Operating leverage", "Demand health", "Margin quality"],
  "supporting_evidence": ["q1_2026_mbr", "q2_2026_forecast_review", "q2_2026_cfo_commentary"],
  "contradicting_evidence": ["q3_2026_forecast_review_flagged_demand_softness"],
  "confidence": "medium-high",
  "scope": "Finance performance analysis",
  "owner": "FP&A Team",
  "last_reviewed": "2026-07-03",
  "review_trigger": "Review after each MBR, QBR, forecast miss, or major marketing strategy change",
  "agent_reuse": "Load when generating a variance explanation or CFO narrative that touches marketing spend or margin.",
  "example": "In the Q2 2026 MBR, marketing spend fell from 14% to 11% of revenue quarter-over-quarter while bookings grew 9% and conversion held flat — the CFO commentary explicitly credited 'channel mix optimization,' not a demand pullback, which is the specific instance this concept generalizes from."
}
```

| Field | Purpose |
|---|---|
| `concept_id` | Stable identifier used by agents and systems. |
| `concept_name` | Human-readable standard name. |
| `concept_type` | Business driver, risk, structural/narrative pattern, rhetorical/language device, content-pairing pattern, or relationship between concepts. Not every concept is a "driver" — tag honestly. |
| `definition` | What the concept *is*, in one plain sentence — no evidence packed in. See the Writing rule in SKILL.md. |
| `business_interpretation` | How the company should interpret it. |
| `positive_signal` / `negative_signal` | When the signal is good vs. risky/misleading. |
| `related_metrics` / `related_concepts` | What to check alongside this concept. |
| `supporting_evidence` / `contradicting_evidence` | Artifact IDs — the detail lives in the evidence ledger, not here. |
| `confidence` | How strongly the system should rely on this. |
| `scope` | Business unit, function, region, or audience where it applies. |
| `owner` | Human or team accountable for the meaning. |
| `last_reviewed` / `review_trigger` | When last checked, and what should force a re-check. |
| `agent_reuse` | Concretely, when/how an agent should pull this record. A record with no clear `agent_reuse` isn't pulling its weight. |
| `example` | One fully worked-out instance from the actual source material, detailed enough to understand the concept from this field alone — not a citation like `supporting_evidence`, a short self-contained story (what quarter, what was said or done, why it illustrates this concept specifically). If it could apply equally to a different concept, it's too generic. |

## Evidence Ledger

```json
{
  "concept_id": "b2b_growth_quality",
  "evidence": [
    {"artifact_id": "q1_2026_mbr", "statement": "B2B growth was driven by partner demand", "evidence_type": "supporting"},
    {"artifact_id": "q2_2026_earnings_transcript", "statement": "Leadership described B2B as a strategic growth area", "evidence_type": "supporting"},
    {"artifact_id": "q4_2025_forecast_review", "statement": "B2B growth benefited from one-time partner onboarding", "evidence_type": "caution"}
  ]
}
```

Long and append-friendly, deliberately kept separate from the compact Layer 3 record so agent retrieval at runtime doesn't bloat. A belief (Layer 4) doesn't carry its own supporting/contradicting evidence fields — it reaches evidence indirectly, through the evidence ledger entries of each concept named in its `source_concepts`. Don't duplicate that evidence onto the belief record.

## Layer 4: Belief

```json
{
  "belief_id": "marketing_leverage_conditional_on_demand",
  "claim": "Marketing spend fell as a share of revenue in the same quarter operating leverage improved and bookings held — treat this margin gain as durable, but re-open the belief the moment bookings growth decelerates.",
  "explanation": "Declining spend intensity alone would only say the company is spending less; it says nothing about whether that's healthy or just a margin trade against future demand. Operating leverage improving on the same base means the gain isn't purely a spend cut showing up as margin — some of it reflects fixed-cost absorption, which doesn't reverse the way a spend cut would if bookings later disappoint. The two together are what let this be called a durable gain instead of a one-quarter trade-off.",
  "source_concepts": ["marketing_efficiency", "operating_leverage"],
  "confidence": "medium-high",
  "serves_task": "cfo_variance_narrative",
  "owner": "FP&A Team",
  "status": "active"
}
```

| Field | Purpose |
|---|---|
| `belief_id` | Stable identifier for the belief record. |
| `claim` | One direct sentence naming the pattern *and* the action a downstream task must take from it — no separate "what this means" appendix. This is the field the Writing rule is about; see SKILL.md. |
| `explanation` | The reasoning the claim rests on, in the writer's own analysis. Must **not** narrate the extraction process ("concept A says X, concept B says Y") — that's process narration, not explanation. Explain why the combination matters, not which concepts were consulted. |
| `source_concepts` | ≥2 `concept_id`s actually combined to produce this claim — a one-line traceability pointer, never woven into `explanation`'s prose. Fewer than 2 entries means the record is a candidate, not an active belief. |
| `confidence` | How strongly the system should rely on this claim. |
| `serves_task` | The downstream task (from Step 0.5) this belief exists to support. A belief with no named task isn't earning its keep. |
| `owner` | Human or team accountable for the belief. |
| `status` | e.g. active, weakening, retired. |

**Hard rule:** a belief must combine at least 2 concepts and produce a conclusion that none of them makes alone. In the example above, `marketing_efficiency` alone would only give "spend intensity is declining" (a restatement, not a belief); it's checked against `operating_leverage` (is the margin gain structural or just spend timing?) before the belief is allowed to state a view. A concept that doesn't combine with anything stays a concept — it does not get promoted into a belief just because it's true and evidenced.

Derive belief categories from the downstream tasks a memory actually serves (Step 0.5), not from a fixed checklist. Typical categories seen in practice — Business Performance, Forecast Reliability, Leadership Narrative, Metric Definition, Source Trust, Variance Explanation, Investor Relations, Risk — are illustration, not a template to fill in. If a task has no belief serving it and the corpus genuinely can't produce one, name that as an explicit gap rather than leaving the category silently empty.

**Writing constraints on `claim`:** no first person; no unresolved absolutist language ("always," "never," "zero") unless the evidence genuinely supports zero exceptions; the sentence must name the action a downstream task should take, not stop at the observation.

**Falsifiability and honest confidence:** a belief must state what would prove it wrong (the example's `claim` does this with "re-open the belief the moment bookings growth decelerates"). Don't round a single-instance or low-track-record concept up into a confident-sounding belief on its own — bundle genuinely thin findings together and label the result low-confidence, rather than dressing up any one of them alone.

## Source Authority Rule

```json
{
  "question_type": "Final actuals",
  "preferred_source": "Official finance system (e.g. Hyperion)",
  "reason": "Numbers must come from the source of truth."
}
```

One record per question type. Don't invent these unilaterally — they should trace back to official documentation or data-owner sign-off.

## Worked end-to-end example: B2B Growth

Traces one concept through every layer, showing what each layer adds that the previous one didn't have.

**1. Raw artifact** — Q2 2026 business review deck, stored with metadata (`artifact_id: q2_2026_business_review_deck`, `version: Final`).

**2. Extracted facts**
```json
{
  "artifact_id": "q2_2026_business_review_deck",
  "facts": [
    {"type": "metric", "metric": "B2B Revenue", "value": "+18%", "comparison": "YoY", "period": "Q2 2026"},
    {"type": "driver", "statement": "B2B acceleration supported revenue growth"},
    {"type": "driver", "statement": "Partner demand improved"}
  ]
}
```
This is only what the document says — no interpretation yet.

**3. Document-level context (candidate, not durable)** — "In this Q2 deck, B2B growth is presented as a positive revenue driver connected to partner demand." One document; local meaning only.

**4. Cross-document pattern** — Q1 MBR, Q2 MBR, Q2 earnings transcript, Q3 forecast review, and a Q3 analyst report independently repeat the same interpretation: B2B growth reflects partner demand and is framed as strategic. Independent recurrence across artifact types is what justifies moving past document-level context.

**5. Approved business context**
```json
{
  "concept_id": "b2b_growth_quality",
  "concept_name": "B2B Growth Quality",
  "concept_type": "Business Driver",
  "definition": "Whether B2B revenue growth reflects broad-based, repeatable demand rather than a one-time or concentrated event.",
  "business_interpretation": "B2B growth is treated as strategic and higher-quality when it reflects broad-based partner demand, scalable distribution, and repeatable transaction volume.",
  "positive_signal": "Growth is broad-based across partners, regions, and recurring transactions.",
  "negative_signal": "Growth is concentrated in one partner, driven by one-time onboarding, or helped by easy prior-year comparisons.",
  "related_metrics": ["B2B Revenue", "Partner count", "Transaction volume"],
  "related_concepts": ["Revenue growth", "Forecast variance"],
  "supporting_evidence": ["q1_2026_mbr", "q2_2026_mbr", "q2_2026_earnings_transcript", "q3_2026_forecast_review", "q3_2026_analyst_report"],
  "contradicting_evidence": ["q4_2025_forecast_review_one_time_partner_onboarding"],
  "confidence": "high",
  "scope": "Finance performance analysis",
  "owner": "FP&A Team",
  "last_reviewed": "2026-07-03",
  "review_trigger": "Review after each MBR, QBR, or forecast review that discusses B2B",
  "agent_reuse": "When explaining B2B revenue variance, check partner concentration and onboarding timing before calling growth structural; cite this concept and its negative_signal explicitly if either is unclear.",
  "example": "In the Q2 2026 earnings transcript, leadership attributed the 18% YoY B2B growth to 'broad-based demand across our top-20 partners,' and the Q2 MBR shows no single partner above 15% of B2B revenue — the specific instance behind this concept's positive_signal."
}
```
A human domain expert approved this and added the caveat reflected in `negative_signal`.

**6. Evidence ledger** — stores the full supporting and cautionary statement list (see the Evidence Ledger template above), so the compact record in step 5 doesn't have to carry it.

**7. Belief — synthesized, not translated.** `b2b_growth_quality` alone would only give "B2B growth looks broad-based this quarter" — a reworded concept, not a belief. Before writing the belief, it's checked against a second, already-approved concept in the store, `forecast_reliability_b2b` ("B2B has beaten its own forecast in 3 of the last 4 quarters"). The two concepts reinforce each other here — breadth of demand *and* a track record of hitting forecast — so the belief can state a confident view; if the forecast-reliability concept had instead shown B2B routinely missing its own guide, the two concepts would cut against each other and confidence would have to drop even with broad-based demand.
```json
{
  "belief_id": "b2b_growth_durability_and_reliability",
  "claim": "B2B growth this window is broad-based and has a forecast-beat track record (3 of the last 4 quarters) — treat B2B upside as a higher-confidence driver in the next forecast raise than a segment without that track record, and re-check the moment growth concentrates in fewer than 3 partners.",
  "explanation": "Breadth alone would only support calling this quarter's growth non-one-time; it says nothing about how much weight to put on B2B in a forward-looking forecast. A forecast-beat track record alone would only say B2B's own guidance has been dependable; it says nothing about whether the underlying demand is broad or fragile. A segment that is both broad-based and has consistently hit its own forecast is the specific combination that justifies leaning on it for a raise — either signal alone would leave real uncertainty a forecast owner would have to guess past.",
  "source_concepts": ["b2b_growth_quality", "forecast_reliability_b2b"],
  "confidence": "high",
  "serves_task": "revenue_variance_and_forecast_narrative",
  "owner": "FP&A Team",
  "status": "active"
}
```
Note what `explanation` does *not* do: it never writes "`b2b_growth_quality` says X, `forecast_reliability_b2b` says Y" — that would be process narration. It argues the reasoning directly; `source_concepts` alone carries the traceability.

**8. Workflow skill usage** — a revenue-variance-explanation skill loads this concept and belief when B2B appears as a driver, and writes: "Revenue growth was supported by B2B acceleration, which should be framed as a higher-quality driver only if it reflects broad-based partner demand and repeatable volume — verify it wasn't driven by one-time onboarding," instead of the weak "Revenue grew because B2B increased."

**9. Feedback update** — if a new Q4 forecast review shows B2B concentrated in two partners, the belief's `claim` and `explanation` are updated (not overwritten) to note the narrowing, and `confidence` drops from high to medium — the belief itself isn't discarded on one data point, and `status` only moves to `weakening` if the pattern repeats.

## Glossary

| Term | Meaning |
|---|---|
| Raw artifact | The original corporate document or message, stored with metadata. |
| Extracted fact | A structured number, claim, driver, risk, definition, or exact quote pulled from one artifact — no interpretation. |
| Document-level context | Local meaning inside one document only; not durable on its own. |
| Business context | Approved, reusable interpretation of what a business concept means, backed by evidence from multiple independent artifacts. |
| Evidence ledger | The long, append-friendly proof trail behind a business context record or belief. |
| Belief | A durable interpretation of how part of the business works, built by combining ≥2 business-context concepts into a conclusion none of them makes alone — never one concept reworded. |
| Workflow skill | A repeatable procedure that consults facts, context, and beliefs to produce a business output. |
| Agent reasoning | The orchestration layer that decides which source, skill, and belief to use for a given request. |
| Feedback loop | The mechanism that routes new documents, corrections, and edits to the layer they should update. |
| Source authority | The rule defining which source is trusted for a given question type (actuals, forecast, narrative, definition). |
| `agent_reuse` | The field on a business context record stating concretely what an agent should do with it — not just what it means. |
| `example` | The field on a business context record holding one fully worked-out, source-specific instance — distinct from `supporting_evidence`, which only cites where evidence lives. |
| `source_concepts` | The field on a belief record listing every `concept_id` actually weighed together to reach that belief. Fewer than 2 entries means the record is a candidate, not yet an earned belief. |
| `claim` | The one-sentence field on a belief record naming the pattern and the action a downstream task must take from it — the field the Writing rule is strictest about. |
| `explanation` | The reasoning field on a belief record. Must argue the case directly; must never narrate which concepts were consulted ("concept A says X, concept B says Y") — that belongs in `source_concepts`, not prose. |
| `serves_task` | The field on a belief record naming which downstream task (from Step 0.5) the belief exists to support. |
| Concept-type taxonomy | The set of category names business context gets grouped under; discovered from the concepts actually extracted, not assigned in advance. |
