# Institutional Intelligence Blueprint

## Starting from the beginning

You are trying to create an AI system inside a company, but you are not trying to create a new LLM. The LLM already exists. What you are trying to create is the company-specific intelligence layer around the LLM, so that the model can understand how the business works, how people explain numbers, which documents matter, what source to trust, what patterns repeat, and how to produce useful business outputs.

A normal LLM knows general language and reasoning. But it does not automatically know your company's internal definitions, planning cycles, leadership preferences, reporting logic, metric caveats, source hierarchy, or historical business interpretation. That knowledge lives inside corporate artifacts such as decks, Excel files, transcripts, emails, business reviews, forecasts, strategy memos, analyst reports, and leadership notes.

The big question is:

How do we turn corporate documents into reusable business intelligence?

The answer is not simply "upload documents into RAG." That only gives you search. The stronger framework is a layered system where every layer converts the previous layer into something more useful.

## The full framework

| Layer | Purpose | Simple Example |
| --- | --- | --- |
| Raw Artifacts | Store the original documents. | Decks, transcripts, Excel files, emails, notes. |
| Extracted Facts | Pull out numbers, claims, dates, owners, definitions, and commentary. | Revenue grew 6%, B2B accelerated, margin expanded. |
| Business Concepts / Business Context | Connect facts to internal business meaning. | B2B growth means partner demand strength. |
| Belief Streams | Maintain durable interpretations that evolve over time. | Marketing leverage is good only if growth remains healthy. |
| Workflow Skills | Execute repeatable tasks using facts, context, and beliefs. | Generate variance summary or deck section. |
| Agent Reasoning | Decide which skill, source, belief, and explanation to use. | Prepare CFO-ready narrative from multiple sources. |
| Feedback Loop | Update facts, concepts, beliefs, and source rules when new documents or corrections arrive. | New quarter confirms, weakens, or changes prior belief. |

This framework starts with documents but does not end with documents. The goal is to move from evidence to facts, then from facts to meaning, then from meaning to judgment, and finally from judgment to business action.

The simple mental model:

Documents -> Facts -> Meaning -> Judgment -> Work -> Learning

Think of the system like a very experienced finance or business person. An experienced person does not just remember files. They know which file is official, which number is final, which explanation is weak, what leadership usually means, what a variance usually signals, and when a metric movement is actually important.

This AI framework is trying to recreate that kind of institutional intelligence.

## 1. Raw Artifacts Layer

The raw artifacts layer stores the original corporate documents exactly as they exist.

These artifacts can include business review decks, QBR decks, MBR decks, Excel forecast files, Hyperion exports, earnings transcripts, analyst reports, meeting notes, leadership emails, Slack messages, KPI dictionaries, strategy memos, and planning documents.

At this layer, the system is not trying to deeply interpret the business yet. It is preserving the source material so anything the AI says later can be traced back to the original evidence.

For example, if the company has a Q2 business review deck, the raw artifact layer stores the deck itself, along with metadata such as the document name, owner, period, business function, version, and source location.

| Input | Output |
| --- | --- |
| Original deck, transcript, Excel file, email, or note | Stored artifact with metadata |

Example raw artifact record:

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

This layer answers: what documents do we have, where did they come from, who created them, and what period do they belong to?

This layer is important because corporate AI must be traceable. If the AI says, "Margin improved because marketing efficiency increased," someone should be able to ask, "Which document said that?"

One document gives the title, type, owner, date, period, version, audience, and location.

Multiple documents build a document inventory across time. For example, every month the finance team produces an MBR deck, every quarter leadership produces an earnings script, and every forecast cycle creates a new forecast file.

The unified output is a clean artifact catalog. Instead of random files sitting across folders, the system has a structured inventory of business artifacts.

## 2. Extracted Facts Layer

The extracted facts layer pulls specific information out of the raw documents.

This is where the system reads a document and extracts numbers, metrics, claims, drivers, dates, owners, risks, assumptions, definitions, and commentary.

For example, a business review deck may contain these statements:

- Revenue grew 6% year over year.
- B2B accelerated due to partner demand.
- EBITDA margin expanded 180 basis points.
- Marketing spend came in below forecast.
- Domestic demand softness remains a risk.

The extracted facts layer turns that into structured records.

| Input | Output |
| --- | --- |
| One raw artifact | Extracted facts, metrics, claims, drivers, risks, and commentary |

Example extracted fact record:

```json
{
  "artifact_id": "q2_2026_business_review_deck",
  "facts": [
    {
      "type": "metric",
      "metric": "Revenue",
      "value": "+6%",
      "comparison": "YoY",
      "period": "Q2 2026"
    },
    {
      "type": "driver",
      "statement": "B2B acceleration supported revenue growth"
    },
    {
      "type": "profitability",
      "statement": "EBITDA margin expanded 180 basis points"
    },
    {
      "type": "risk",
      "statement": "Domestic demand softness remains a risk"
    }
  ]
}
```

This layer answers: what did the document actually say?

This is still not business intelligence by itself. It is cleaner information extracted from messy artifacts. A fact says what happened. It does not yet explain what it means.

For example, "Revenue grew 6%" is a fact. It does not yet answer whether that growth was high quality, temporary, broad-based, margin-accretive, or risky.

One document can safely give facts local to that document: revenue grew 6%, B2B accelerated, margin expanded, or leadership flagged a risk.

Multiple documents allow facts to be compared across time. For example, B2B accelerated in Q1, Q2, and Q3, or marketing efficiency improved for two quarters but started hurting demand in the third quarter.

This layer unifies raw text into structured facts. Different documents may say things in different words, but the extraction layer converts them into consistent records such as metric, value, period, comparison, driver, risk, and owner.

## 3. Business Concepts / Business Context Layer

The business context layer explains what facts mean inside the company.

It connects raw facts to internal business meaning.

For example, the extracted fact layer may say:

> B2B revenue grew 18%.

The business context layer says:

> B2B growth is generally interpreted as partner demand strength, scalable distribution growth, and strategic momentum, especially when growth is broad-based across partners and regions.

Another extracted fact may say:

> Marketing spend declined as a percentage of revenue.

The business context layer says:

> Marketing efficiency is positive only when bookings, conversion, and demand remain healthy. If margin improves because marketing spend was reduced too aggressively, the business should treat that margin improvement cautiously.

This layer is where the AI stops merely repeating documents and starts understanding business meaning.

### Inputs

| Input | Description |
| --- | --- |
| Extracted facts | Numbers, claims, drivers, risks, and commentary from documents. |
| Raw artifact metadata | Document type, owner, period, version, and audience. |
| KPI definitions | Official metric definitions and calculation logic. |
| Source hierarchy | Which document or system should be trusted for which type of answer. |
| Human review | Corrections and approvals from business experts. |

### Output

The output is a reusable business concept record.

```json
{
  "concept_name": "Marketing Efficiency",
  "concept_type": "Business Driver",
  "definition": "The ability to generate bookings or revenue with lower relative marketing spend.",
  "business_interpretation": "Marketing efficiency is positive when bookings, revenue, and demand remain healthy while marketing spend intensity declines. It should be interpreted cautiously if margin improves mainly because spend was reduced, because that may create future demand risk.",
  "positive_signal": "Bookings or revenue grow while marketing spend as a percentage of revenue declines.",
  "negative_signal": "Margin improves while bookings, conversion, or demand weaken.",
  "related_metrics": [
    "Marketing spend",
    "Bookings",
    "Revenue",
    "Conversion",
    "EBITDA margin"
  ],
  "related_concepts": [
    "Operating leverage",
    "Demand health",
    "Margin quality"
  ],
  "evidence": [
    "q1_2026_mbr",
    "q2_2026_forecast_review",
    "q2_2026_cfo_commentary"
  ],
  "confidence": "medium-high",
  "scope": "Finance performance analysis",
  "review_trigger": "Review after each MBR, QBR, forecast miss, or major marketing strategy change"
}
```

This is not a document summary. This is reusable business meaning.

### One Document vs. Multiple Documents

One document can create document-level context.

For example, one Q2 business review deck may say:

> Marketing efficiency supported margin expansion.

From this one document, the system can create a local interpretation:

> In this Q2 business review deck, marketing efficiency is framed as a positive margin driver.

That is useful, but it is not yet durable company context.

One document can create local meaning, candidate concepts, document-specific caveats, and metric usage.

Multiple documents create durable business context. For example:

- Q1 MBR: B2B growth was driven by partner demand.
- Q2 MBR: B2B acceleration supported revenue growth.
- Q2 earnings transcript: Leadership described B2B as a strategic growth area.
- Q3 forecast review: B2B outperformance drove the forecast raise.
- Q3 analyst report: Analysts viewed B2B as a durable growth driver.

Now the system can create a stronger business context:

> B2B growth is generally interpreted as strategic and higher-quality growth when it reflects broad-based partner demand, scalable distribution, and repeatable transaction volume.

Multiple documents help the system decide whether something is a one-time statement or a repeated business pattern.

The business context layer unifies different wording, different facts, and different documents into one reusable concept.

For example, many documents may use different language:

- Marketing leverage improved.
- Marketing efficiency supported EBITDA.
- Lower spend helped margin.
- Marketing spend intensity declined.
- Marketing pullback may affect future demand.

The unified concept becomes:

> Marketing efficiency means generating revenue or bookings with lower relative marketing spend, but it should be judged together with demand health because lower spend can improve margin while weakening future growth.

## 4. Evidence Ledger

The evidence ledger is not always shown as a separate layer in the simple framework, but practically it is very important.

The evidence ledger stores the proof behind every business concept.

The business context layer should be compact and reusable. The evidence ledger can be long and detailed.

For example, the business context layer may store this:

> B2B growth is generally interpreted as strategic when it reflects partner demand and scalable distribution.

The evidence ledger stores all the documents and statements that support or challenge that concept.

| Input | Output |
| --- | --- |
| Extracted facts, document-level context, and candidate concepts | Supporting evidence, contradicting evidence, confidence trail |

Example evidence ledger record:

```json
{
  "concept_id": "b2b_growth_quality",
  "evidence": [
    {
      "artifact_id": "q1_2026_mbr",
      "statement": "B2B growth was driven by partner demand",
      "evidence_type": "supporting"
    },
    {
      "artifact_id": "q2_2026_earnings_transcript",
      "statement": "Leadership described B2B as a strategic growth area",
      "evidence_type": "supporting"
    },
    {
      "artifact_id": "q4_2025_forecast_review",
      "statement": "B2B growth benefited from one-time partner onboarding",
      "evidence_type": "caution"
    }
  ]
}
```

This is important because the system should not store business context as unsupported AI opinion. Every reusable concept should be connected to evidence.

One document contributes one piece of evidence. Multiple documents create a body of evidence, showing whether a concept is repeatedly supported, contradicted, or changing over time.

This layer unifies the evidence around one concept. Instead of scattered proof across many decks and transcripts, the evidence ledger attaches all support and contradiction to the same business concept.

## 5. Belief Streams Layer

The belief stream layer maintains durable interpretations that evolve over time.

This is different from business context.

Business context explains what a concept means. A belief stream tracks what the company currently believes about that concept based on evidence over time.

For example, business context may say:

> Marketing efficiency is positive when growth remains healthy.

A belief stream may say:

> Recent quarters suggest that marketing leverage has supported margin expansion, but the belief should be treated cautiously because there are early signs that lower spend may pressure demand in some regions.

The belief stream is more dynamic. It changes when new documents arrive.

| Input | Output |
| --- | --- |
| Approved business context, new evidence, prior beliefs, contradictions, human feedback | Updated belief statement, confidence, caveats, watch items |

Example belief stream record:

```json
{
  "belief_stream": "Marketing Efficiency Belief Stream",
  "current_belief": "Marketing leverage is valuable only when bookings, conversion, and demand remain healthy.",
  "supporting_evidence": [
    "q1_2026_mbr",
    "q2_2026_mbr",
    "q2_2026_cfo_commentary"
  ],
  "contradicting_evidence": [
    "q3_2026_forecast_review_flagged_demand_softness"
  ],
  "confidence": "medium-high",
  "watch_item": "Monitor whether bookings growth remains healthy after marketing spend reductions.",
  "last_updated": "2026-07-03"
}
```

One new document can update or challenge a belief. For example, a new forecast review may say demand weakened after marketing spend was reduced. That one document may not destroy the old belief, but it can lower confidence or add a caveat.

Multiple documents create the actual belief trend. If many quarters show the same pattern, confidence increases. If new documents repeatedly contradict the old belief, the system updates the belief.

The belief stream unifies the company's evolving interpretation over time. It does not keep every quarter as a separate memory in the active context. Instead, it compresses history into a current belief with evidence, caveats, and confidence.

## 6. Workflow Skills Layer

The workflow skills layer turns the knowledge into repeatable work.

A skill is a procedure that knows how to perform a specific business task. It does not just answer a question. It follows a known workflow.

For example, a finance variance explanation skill may follow this process:

1. Identify the metric.
2. Pull actuals.
3. Pull forecast or plan.
4. Calculate the variance.
5. Identify drivers.
6. Check source authority.
7. Apply business context.
8. Apply relevant belief streams.
9. Generate a business-ready explanation.

Examples of workflow skills:

| Workflow Skill | Output |
| --- | --- |
| Variance explanation skill | Explains actual vs forecast or actual vs plan. |
| CFO narrative skill | Produces executive-ready commentary. |
| Deck section generation skill | Creates a business review slide section. |
| Metric definition skill | Explains what a metric means and where it comes from. |
| Forecast change skill | Explains what changed between forecast versions. |
| Analyst comparison skill | Compares external analyst views with internal narrative. |
| Risk summary skill | Summarizes persistent, emerging, and declining risks. |

| Input | Output |
| --- | --- |
| User task, extracted facts, business context, belief streams, source rules | Business-ready artifact or answer |

For example, if the user asks:

> Generate a variance explanation for margin improvement.

A weak system may answer:

> Margin improved because EBITDA increased and costs were controlled.

A better system using this framework may answer:

> Margin improvement was supported by operating leverage, marketing efficiency, and disciplined spend. However, because marketing-driven margin improvement is higher quality only when demand remains healthy, the explanation should confirm whether bookings and conversion remained strong before calling the improvement structural.

That better answer comes from using business context and belief streams, not just facts.

One document may provide the immediate facts needed for the skill, such as the current quarter's revenue, margin, forecast, and drivers.

Multiple documents provide the prior context, trend, and interpretation rules that make the output smarter.

The workflow skill unifies facts, context, beliefs, and source rules into a usable business output.

## 7. Agent Reasoning Layer

The agent reasoning layer decides what to do, which sources to use, which skill to run, which belief stream matters, and what kind of output the user needs.

A skill executes a known task. An agent decides how to solve a messy business request.

For example, suppose the user asks:

> Prepare a CFO-ready explanation for why margin improved this quarter.

A simple chatbot may search for "margin improved" and summarize the nearest paragraph.

An agent should reason more carefully:

First, I need the official actuals because margin is a financial metric. Then I need the forecast or plan to understand whether margin beat expectations. Then I need the business review commentary to understand the internal explanation. Then I need marketing, cost, revenue, and mix drivers because margin can improve for many reasons. Then I need the business context for margin quality and marketing efficiency. Then I need the leadership narrative belief stream so the wording is CFO-ready. Then I need to produce a concise explanation with caveats.

| Input | Output |
| --- | --- |
| User request, available tools, source hierarchy, business context, belief streams, workflow skills | Decision plan and final business output |

The agent makes decisions such as:

| Agent Decision | Example |
| --- | --- |
| Which source should be trusted? | Use official finance system for actuals, not a draft deck. |
| Which skill should be used? | Use variance explanation skill, not generic summarization. |
| Which business context matters? | Margin quality, marketing efficiency, operating leverage. |
| Which belief stream matters? | Leadership narrative and forecast reliability. |
| What output format is needed? | CFO talking points, not a long memo. |
| What caveat is needed? | Do not call margin improvement structural unless demand remains healthy. |

One document can trigger the agent's task or provide immediate evidence. Multiple documents help the agent reason across periods, sources, and patterns.

The agent unifies the entire system at runtime. It decides which facts, concepts, beliefs, and skills should be used for the specific user request.

## 8. Feedback Loop

The feedback loop keeps the system alive.

A company changes every month and every quarter. New documents arrive. Forecasts change. Leadership changes wording. A metric definition gets updated. A source of truth changes. A belief that was true last year may no longer be true.

So the system needs a feedback loop.

The feedback loop asks:

- What is new?
- What changed?
- What confirmed an existing concept?
- What contradicted an existing concept?
- What changed a belief?
- What source rule needs correction?
- What output did the user edit?
- What should be promoted into memory?
- What should be retired?

| Input | Output |
| --- | --- |
| New documents, user corrections, leadership edits, forecast misses, updated definitions | Updated facts, concepts, beliefs, source rules, and skills |

For example, suppose the existing belief says:

> Marketing leverage is good when growth remains healthy.

Then a new document says:

> Marketing spend declined, margin improved, but bookings slowed and leadership flagged demand softness.

The feedback loop may update the belief:

> The belief remains valid, but current confidence in marketing leverage quality should be reduced because the latest evidence shows possible demand pressure.

One new document can trigger a review. It can add evidence, introduce a caveat, or challenge an existing belief.

Multiple new documents over time determine whether the system should actually change the approved context or belief confidence.

The feedback loop unifies new evidence with old memory. It prevents the system from becoming stale or bloated.

## Complete Input-Output Chain

| Step | Input | What One Document Gives | What Multiple Documents Give | Output |
| --- | --- | --- | --- | --- |
| 1. Raw Artifacts | Decks, Excel files, transcripts, emails, notes | Original source and metadata | Artifact inventory across time | Stored artifact catalog |
| 2. Extracted Facts | One classified document | Metrics, claims, dates, drivers, risks, commentary | Comparable facts across periods | Structured fact records |
| 3. Document-Level Context | Extracted facts from one document | Local meaning inside that document | Not durable yet | Candidate interpretation |
| 4. Cross-Document Patterning | Many document-level contexts | One evidence point | Repeated meanings, contradictions, trends | Pattern clusters |
| 5. Business Context Layer | Pattern clusters, KPI docs, source rules, expert review | Candidate concept | Durable interpretation and caveats | Approved business concept |
| 6. Evidence Ledger | Extracted facts and concept evidence | Supporting or contradicting statement | Full proof history | Evidence trail |
| 7. Belief Streams | Approved context plus new evidence | Belief update trigger | Evolving interpretation over time | Current belief with confidence |
| 8. Workflow Skills | User task plus facts, context, and beliefs | Current task facts | Historical judgment and rules | Business output |
| 9. Agent Reasoning | User request and available system knowledge | Immediate evidence | Cross-source reasoning | Decision path and final response |
| 10. Feedback Loop | User edits, new docs, corrections, new definitions | Specific correction or new evidence | Pattern-level updates | Refreshed context and beliefs |

## Example: B2B Growth From Document to Intelligence

### Step 1: Raw artifact

The system receives a Q2 business review deck and stores it with metadata.

```json
{
  "artifact_type": "Business Review Deck",
  "period": "Q2 2026",
  "owner": "Finance",
  "version": "Final"
}
```

### Step 2: Extracted fact

The system reads the deck and extracts:

- B2B revenue grew 18%.
- B2B acceleration supported revenue growth.
- Partner demand improved.

This is only what the document says.

### Step 3: Document-level context

From this one document, the system says:

> In this Q2 deck, B2B growth is presented as a positive revenue driver connected to partner demand.

This is local context, not yet a durable business concept.

### Step 4: Cross-document patterning

Now the system compares many documents:

- Q1 MBR: B2B growth was driven by partner demand.
- Q2 MBR: B2B acceleration supported revenue growth.
- Q2 earnings transcript: Leadership called B2B strategic.
- Q3 forecast review: B2B outperformance supported forecast raise.
- Q3 analyst report: Analysts viewed B2B as durable growth.

Now the system sees a repeated pattern.

### Step 5: Business context

The system proposes this concept:

> B2B growth is generally interpreted as strategic and higher-quality growth when it reflects broad-based partner demand, scalable distribution, and repeatable transaction volume.

A finance expert may approve it, but add a caveat:

> This should be caveated when growth is concentrated in one partner, driven by one-time onboarding, or helped by easy prior-year comparisons.

The approved business context becomes:

```json
{
  "concept_name": "B2B Growth Quality",
  "business_interpretation": "B2B growth is generally interpreted as strategic and higher-quality growth when it reflects broad-based partner demand, scalable distribution, and repeatable transaction volume.",
  "positive_signal": "Growth is broad-based across partners, regions, and recurring transactions.",
  "negative_signal": "Growth is concentrated in one partner, driven by one-time onboarding, or helped by easy comparisons.",
  "confidence": "high"
}
```

### Step 6: Evidence ledger

The evidence ledger stores all supporting and cautionary evidence.

```json
{
  "concept_id": "b2b_growth_quality",
  "supporting_evidence": [
    "q1_mbr_partner_demand",
    "q2_mbr_b2b_acceleration",
    "q2_earnings_transcript_strategic_b2b"
  ],
  "cautionary_evidence": [
    "q4_forecast_review_one_time_partner_onboarding"
  ]
}
```

### Step 7: Belief stream

The belief stream says:

> The company currently treats B2B as a durable strategic growth engine, but the quality of that growth should be checked against partner concentration, regional breadth, and repeatable transaction volume.

### Step 8: Workflow skill

Now if a user asks for a revenue variance explanation, the skill uses this context.

Instead of saying:

> Revenue grew because B2B increased.

It says:

> Revenue growth was supported by B2B acceleration, which should be framed as a higher-quality driver if the growth reflects broad-based partner demand and repeatable volume. The explanation should verify whether the acceleration was broad-based rather than driven by one-time partner onboarding.

### Step 9: Agent reasoning

If the user asks for a CFO-ready explanation, the agent decides to use:

- Official revenue actuals
- B2B revenue facts
- Business context for B2B growth quality
- Leadership narrative belief stream
- Forecast comparison
- Known caveats

### Step 10: Feedback loop

If a new Q4 forecast review says B2B growth is now concentrated in two partners, the system updates the belief:

> B2B remains a strategic growth driver, but current confidence in growth quality should be reduced until the system confirms broader partner and regional contribution.

That is the full process from document to intelligence.

## Who Creates Each Layer?

The AI system should not rely only on engineers, and it should not make every business judgment by itself.

| Layer | Who Creates It? |
| --- | --- |
| Raw artifacts | Business teams produce the documents; system stores them. |
| Extracted facts | LLM and parsers extract; humans spot-check important data. |
| Business context | LLM proposes; domain experts review and approve. |
| Evidence ledger | System maintains automatically. |
| Belief streams | LLM proposes updates; business owners approve important changes. |
| Workflow skills | AI/product/engineering teams build with business input. |
| Agent reasoning | AI/product/engineering teams design the orchestration logic. |
| Feedback loop | Users, new documents, and domain experts continuously update the system. |

The most important point:

> Engineering owns the system. Business owns the meaning.

The LLM can draft the business context, but the business expert should approve it, especially for finance, investor relations, executive, legal, or customer-facing use cases.

## How to Curate the Business Context Layer

Curation means the system should not blindly keep adding text forever.

Every candidate business concept should be reviewed using these questions:

- Is this interpretation correct?
- Is it supported by enough evidence?
- Is it true across multiple documents or only one document?
- Does it apply to the whole company or only one business unit?
- Is it current or outdated?
- Does it need a caveat?
- Is there contradicting evidence?
- Which source supports it?
- Who approved it?
- When should it be reviewed again?

A good curation workflow:

```text
LLM extracts candidate concept
        |
System attaches supporting evidence
        |
System attaches contradicting evidence
        |
System assigns draft confidence
        |
Business expert reviews
        |
Concept is approved, edited, rejected, split, or merged
        |
Approved concept becomes reusable business context
        |
New documents trigger future review
```

The system should not treat all concepts equally. Some concepts can be low-risk and automatically updated. Others require human approval.

| Concept Type | Review Level |
| --- | --- |
| Simple metric explanation | Light review |
| Internal variance driver | Medium review |
| CFO narrative rule | Strong review |
| Investor-facing interpretation | Strong review |
| Official source of truth rule | Data owner approval |
| Legal, HR, or compliance interpretation | Strict review |

## First Version Scope

Do not start with the whole company. Start with one business domain.

Example:

> Finance Institutional Intelligence System

Start with 10-15 business concepts, not 1,000.

A good first set could be:

| Concept | Why It Matters |
| --- | --- |
| Revenue growth | Core business performance. |
| Bookings growth | Demand indicator. |
| B2B growth | Strategic growth driver. |
| Marketing efficiency | Growth vs margin tradeoff. |
| EBITDA margin | Profitability measure. |
| Operating leverage | Quality of margin expansion. |
| Forecast variance | Explains expectation vs reality. |
| Demand softness | Risk signal. |
| FX impact | Separates reported and underlying performance. |
| Source of truth for actuals | Prevents wrong numbers. |
| Leadership narrative | Helps produce executive-ready language. |

For each concept, store:

- Concept name
- Definition
- Business interpretation
- Positive signal
- Negative signal
- Related metrics
- Related concepts
- Supporting evidence
- Contradicting evidence
- Confidence
- Scope
- Owner
- Last reviewed date
- Review trigger

## Clean Final Explanation

From the beginning, the system works like this:

1. A company produces documents.
2. The system stores the documents as raw artifacts.
3. The system extracts facts from each document.
4. The system creates local document-level context from one document.
5. The system compares many documents to find repeated meanings.
6. The system clusters repeated meanings into candidate business concepts.
7. The system stores evidence behind each concept.
8. A domain expert reviews and approves the concept.
9. The approved concept becomes reusable business context.
10. Belief streams track how that context changes over time.
11. Workflow skills use the context to perform repeatable business tasks.
12. The agent decides which facts, concepts, beliefs, and skills to use.
13. The feedback loop updates everything when new documents or corrections arrive.

The most important distinction:

> One document gives evidence. Multiple documents reveal patterns. Curation turns patterns into approved business context. Belief streams update that context over time. Agents and skills use it to do real business work.

That is the complete framework from the beginning.
