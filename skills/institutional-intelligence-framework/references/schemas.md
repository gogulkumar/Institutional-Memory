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
  "supporting_evidence": ["q1_2026_mbr", "q2_2026_mbr", "q2_2026_cfo_commentary"],
  "contradicting_evidence": ["q3_2026_forecast_review_flagged_demand_softness"],
  "confidence": "medium-high",
  "watch_item": "Monitor whether bookings growth remains healthy after marketing spend reductions.",
  "last_updated": "2026-07-03"
}
```

`current_belief` (or `Statement`) is the field that most needs real quotes, numbers, and mechanism inline — see the Writing rule in SKILL.md; this field gets read directly, not one hop away from its evidence like a Layer 3 `definition` is.

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
