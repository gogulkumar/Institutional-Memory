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
  "agent_reuse": "Load when generating a variance explanation or CFO narrative that touches marketing spend or margin."
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

Long and append-friendly, deliberately kept separate from the compact Layer 3 record so agent retrieval at runtime doesn't bloat.

## Layer 4: Belief Stream

```json
{
  "belief_stream": "Marketing Efficiency Belief Stream",
  "current_belief": "Marketing leverage is valuable only when bookings, conversion, and demand remain healthy.",
  "source_concepts": ["marketing_efficiency", "demand_health", "operating_leverage"],
  "supporting_evidence": ["q1_2026_mbr", "q2_2026_mbr", "q2_2026_cfo_commentary"],
  "contradicting_evidence": ["q3_2026_forecast_review_flagged_demand_softness"],
  "confidence": "medium-high",
  "watch_item": "Monitor whether bookings growth remains healthy after marketing spend reductions.",
  "last_updated": "2026-07-03"
}
```

`current_belief` (or `Statement`) is the field that most needs real quotes, numbers, and mechanism inline — see the Writing rule in SKILL.md; this field gets read directly, not one hop away from its evidence like a Layer 3 `definition` is.

`source_concepts` is the list of `concept_id`s actually weighed against each other to reach this belief — never just the one concept the belief sounds like it's restating. Here, `marketing_efficiency` alone would only give you "spend intensity is declining" (a restatement, not a belief); it's checked against `demand_health` (does bookings growth still hold?) and `operating_leverage` (is the margin gain structural or just spend timing?) before the belief is allowed to state a view. If `source_concepts` has one entry, treat the record as a candidate, not an active belief — see the synthesis rule in SKILL.md, Layer 4.

Typical streams: Business Performance, Forecast Reliability, Leadership Narrative, Metric Definition, Source Trust, Variance Explanation, Investor Relations, Risk.

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
  "agent_reuse": "When explaining B2B revenue variance, check partner concentration and onboarding timing before calling growth structural; cite this concept and its negative_signal explicitly if either is unclear."
}
```
A human domain expert approved this and added the caveat reflected in `negative_signal`.

**6. Evidence ledger** — stores the full supporting and cautionary statement list (see the Evidence Ledger template above), so the compact record in step 5 doesn't have to carry it.

**7. Belief stream — synthesized, not translated.** `b2b_growth_quality` alone would only give "B2B growth looks broad-based this quarter" — a reworded concept, not a belief. Before writing the belief, it's checked against a second, already-approved concept in the store, `forecast_reliability_b2b` ("B2B has beaten its own forecast in 3 of the last 4 quarters, so a raise driven by B2B carries less miss-risk than one driven by a segment with a choppier forecast record"). The two concepts reinforce each other here — breadth of demand *and* a track record of hitting forecast — so the belief can state a confident view; if the forecast-reliability concept had instead shown B2B routinely missing its own guide, the two concepts would cut against each other and confidence would have to drop even with broad-based demand.
```json
{
  "belief_stream": "Business Performance Belief Stream",
  "current_belief": "B2B is currently treated as a durable strategic growth engine — Q1 MBR, Q2 MBR, and the Q2 earnings transcript all tie 18% YoY B2B growth to partner demand, not a one-time event, and B2B has beaten its own forecast in 3 of the last 4 quarters, so this isn't just breadth without a track record.",
  "source_concepts": ["b2b_growth_quality", "forecast_reliability_b2b"],
  "supporting_evidence": ["q1_2026_mbr", "q2_2026_mbr", "q2_2026_earnings_transcript"],
  "contradicting_evidence": ["q4_2025_forecast_review_one_time_partner_onboarding"],
  "confidence": "high",
  "watch_item": "If the next forecast review shows B2B growth concentrated in two partners rather than broad-based, or a forecast miss breaks the reliability track record, drop confidence and flag for re-review.",
  "last_updated": "2026-07-03"
}
```

**8. Workflow skill usage** — a revenue-variance-explanation skill loads this concept and belief when B2B appears as a driver, and writes: "Revenue growth was supported by B2B acceleration, which should be framed as a higher-quality driver only if it reflects broad-based partner demand and repeatable volume — verify it wasn't driven by one-time onboarding," instead of the weak "Revenue grew because B2B increased."

**9. Feedback update** — if a new Q4 forecast review shows B2B concentrated in two partners, the belief stream's `current_belief` is updated (not overwritten) to note the narrowing, and `confidence` drops from high to medium — the belief itself isn't discarded on one data point.

## Glossary

| Term | Meaning |
|---|---|
| Raw artifact | The original corporate document or message, stored with metadata. |
| Extracted fact | A structured number, claim, driver, risk, definition, or exact quote pulled from one artifact — no interpretation. |
| Document-level context | Local meaning inside one document only; not durable on its own. |
| Business context | Approved, reusable interpretation of what a business concept means, backed by evidence from multiple independent artifacts. |
| Evidence ledger | The long, append-friendly proof trail behind a business context record or belief. |
| Belief stream | The current, evolving durable interpretation of how part of the business works, synthesized from multiple business-context concepts weighed against each other — not one concept reworded. |
| Workflow skill | A repeatable procedure that consults facts, context, and beliefs to produce a business output. |
| Agent reasoning | The orchestration layer that decides which source, skill, and belief to use for a given request. |
| Feedback loop | The mechanism that routes new documents, corrections, and edits to the layer they should update. |
| Source authority | The rule defining which source is trusted for a given question type (actuals, forecast, narrative, definition). |
| `agent_reuse` | The field on a business context record stating concretely what an agent should do with it — not just what it means. |
| `source_concepts` | The field on a belief record listing every `concept_id` actually weighed together to reach that belief. One entry means the record is a candidate, not yet an earned belief. |
| Concept-type taxonomy | The set of category names business context gets grouped under; discovered from the concepts actually extracted, not assigned in advance. |
