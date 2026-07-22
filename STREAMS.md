# Beliefs — Stream Definitions, Purpose, and Examples

*The authoritative reference for what each belief stream covers,
what it must never do, and what a real belief looks like per stream.*

*Role in the repo: this file is the single home for full worked
examples. `BELIEF.md` Section 03 carries the compact spec-level
definitions and points here — one authority per concern, so the
spec and the reference cannot drift apart.*

---

> **The single rule underlying all streams:**
> A belief must say something the document does not say.
> If you can find the belief by reading the document, it is a fact not a belief.
> A belief lives in the interpretation that accumulates across many documents —
> in the understanding a six-month reader has that a first-time reader
> completely misses.

---

## How to Read This Document

Each stream has five sections:

- **Purpose** — what the stream exists to accumulate
- **What it covers** — the full scope, stated precisely
- **What it must never do** — the hard boundary
- **The test** — the single question that determines whether a belief qualifies
- **Example** — one real belief written the way it should actually read

The example in each stream says something the document never explicitly states.
That is the standard every belief must meet.

---

## The Belief Entry Format

Every belief across every stream uses this structure:

```
## Belief #N — [the claim as a complete sentence]
               [Status: Candidate | Provisional | Confirmed | Established]

Statement        The claim restated precisely and falsifiably.
                 Present tense. Business judgment.
                 Not a document description.

Why it matters   How this connects to the business foundation.
                 Why it matters for how the business actually operates.
                 What makes it reusable judgment rather than a document fact.

Evolution trail  The per-document journey in first person.
                 When first seen and in which document.
                 What each subsequent comparable document added,
                 confirmed, narrowed, or challenged.
                 Current maturity and document count.

Normal baseline  What the next comparable document should show
                 if the belief is holding.

Falsification    What a future comparable document must show to
test             prove this wrong, narrow it, or retire it.
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 00 — FACTUAL UNDERSTANDING
═══════════════════════════════════════════════════════════════════════

### Purpose

The verified, stable factual record of how this business is measured.
Not what the numbers mean — what they definitively are and whether
they are consistent across documents over time.

### What It Covers

```
Metric definitions       How each key metric is defined and whether
                         the definition holds stable across every
                         comparable document reviewed.

Benchmark sequences      Which comparison bases are used — Plan, FC,
                         prior year, prior FC — and in what order.
                         Whether the sequence ever shifts and what
                         that signals.

Calculation bases        Net vs gross, adjusted vs reported, what is
                         included and excluded. Whether the calculation
                         basis changes across periods or document types.

Data source consistency  Whether numbers come from the same source
                         system consistently across documents.

Scope stability          Whether the same segments, geographies,
                         channels, and lines of business are included
                         in a metric definition over time, or whether
                         scope quietly changes.
```

### What It Must Never Do

State interpretation. Never say what a number means for the business.
Never say whether performance is good or bad. Never draw conclusions
about business health from metric readings. Only state what is
verifiably true about how the business is measured and whether
that measurement is consistent.

### The Test

Any analyst with the source document can verify this belief
independently. It is fully re-checkable. If it requires accumulated
understanding to verify, it belongs in a different stream.

---

### Example Belief

```
## Belief #1 — [Entity] defines its primary efficiency ratio on a net
basis excluding partner co-funding, making it structurally lower
than how competitors report the same ratio.
[Status: Established]

Statement: The spend figure in the primary efficiency ratio excludes
partner co-funding contributions, so the ratio is not directly
comparable to any external benchmark that uses gross spend in
the numerator.

Why it matters: Every time someone compares this entity's
efficiency ratio to an industry figure or a competitor ratio,
they are comparing different things. The number looks more
efficient than it actually is on a gross basis. Understanding
this prevents misreading efficiency improvements as real when
they may reflect partner mix changes rather than genuine spend
discipline. Any analyst using this ratio as a sector comparison
benchmark is working from a definition mismatch.

Evolution trail: Confirmed in the first document reviewed against
the stated methodology footnote. Verified against three subsequent
documents — definition unchanged across all four. The footnote
language is identical in every document reviewed. Four documents.
Established.

Normal baseline: Every document reports the ratio on this net
basis. The footnote appears consistently on the efficiency slide.
A shift to gross reporting or a change in the co-funding exclusion
would change the ratio materially and would require restatement of
all prior periods to compare accurately.

Falsification test: A document that reports the ratio including
co-funding contributions in the numerator, or an explicit footnote
stating that the calculation basis has changed. Either would
retire this belief and require recalibration of every efficiency
comparison made to date.

Provenance:
- Foundation dependency: the efficiency ratio is a thesis-defining
  metric whose calculation basis is expected to be stable (foundation,
  thesis metrics section)
- Confirming documents: document 1–4
- Blind passes: document 3 (independently re-derived the same
  footnote language with no visibility into the prior belief,
  before promotion to Confirmed)
- Contradiction searches: document 4 (searched, none found, before
  promotion to Established)
- Related beliefs: none identified yet
- Last checked: document 4
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 01 — BUSINESS MODEL UNDERSTANDING
═══════════════════════════════════════════════════════════════════════

### Purpose

The durable understanding of how this specific business makes money —
not what it reported, but what the underlying economic engine is and
whether it is working. The profitability thesis and whether the
evidence supports it.

### What It Covers

```
The profitability thesis  The core bet the business is making.
                          What has to be true for this business
                          to create value. What breaks the model
                          if it fails.

Thesis-defining metrics   Which specific metrics reveal whether
                          the thesis is holding or breaking —
                          not the metrics Finance reports most
                          prominently, but the ones that actually
                          tell you whether the model is working.

Revenue model             What drives top line at a structural level.
                          Price vs volume. New customers vs existing.
                          Whether the growth mechanism is sustainable
                          or relying on a finite lever.

Margin structure          Where margin is generated and where it leaks.
                          Which cost lines are structurally fixed vs
                          variable. How the cost base responds to
                          volume changes.

Unit economics            Whether the business is getting more or
                          less efficient per unit of output over time.
                          The trajectory, not the current level.

Structural constraints    What constrains or enables the model.
                          What the business is structurally dependent
                          on. What would change the model itself
                          if it shifted.
```

### What It Must Never Do

Report what happened in a specific period. Never state a metric
reading from a single document. Never describe a document's content.
This stream describes the economic model — how the business makes
money as a system — not the economic results of any given period.

### The Test

This belief is true regardless of which specific quarter is being
reviewed. You could read it in any period and it would describe
the same underlying reality. If it only holds for one period,
it is not a business model belief — it is a result.

---

### Example Belief

```
## Belief #1 — [Entity] is extracting more from existing demand
rather than expanding demand — and the gap between those two
things is getting harder to see in the headline numbers.
[Status: Established]

Statement: Revenue growth is being driven by price realization
while core volume remains flat or grows minimally. The business is
monetizing its existing customer base more intensively rather
than bringing more new customers in. This is a fundamentally
different economic engine from what the headline metric suggests —
and the headline does not flag the distinction.

Why it matters: Price-driven growth has a ceiling. When pricing
power is exhausted — either because the market pushes back or
because the addressable premium has been fully captured — there
is no volume engine behind it. The business is currently growing
on borrowed headroom. Any document that shows flat core volume
alongside strong revenue is showing this pattern. It is not a
sign of pricing sophistication. It is a sign of volume stagnation
dressed as efficiency. The difference matters enormously for
what happens many periods out.

Evolution trail: First identified in the first comparable document
when revenue grew faster than core volume. Treated as possible
noise — seasonality could explain it. The second comparable
document repeated the split. The third confirmed it. By the
fourth, this stopped being treated as seasonal and started being
treated as structural. The volume engine is not working. The
pricing engine is carrying the growth story. The document never
frames it this way — it reports both numbers but never draws
the implication. Four documents. Established.

Normal baseline: Any period where core volume grows materially
slower than revenue is confirming this belief. That is the
current normal. A genuine departure would be core volume growing
faster than revenue for two consecutive comparable periods —
meaning volume is genuinely expanding faster than price.

Falsification test: Two consecutive comparable periods where
core volume growth exceeds revenue growth. That would mean the
demand engine restarted and this belief was wrong about the
structural nature of the volume stagnation. One period of strong
volume is not enough — the pattern needs to hold for two periods
before the belief is retired.

Provenance:
- Foundation dependency: the growth engine's price vs. volume
  composition is a thesis-defining question (foundation, profitability
  thesis section)
- Confirming documents: document 1–4
- Blind passes: document 3 (independently re-derived the same
  price/volume split with no visibility into the prior belief,
  before promotion to Confirmed)
- Contradiction searches: document 4 (searched, none found, before
  promotion to Established)
- Related beliefs: none identified yet
- Last checked: document 4
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 02 — BUSINESS DYNAMICS
═══════════════════════════════════════════════════════════════════════

### Purpose

How the parts of the business move relative to each other over time.
Not what the model is — how it behaves mechanically. The lead-lag
relationships, seasonal cycles, conversion chains, and feedback loops
that hold across periods independent of who is managing them.

### What It Covers

```
Lead-lag relationships   Which metrics move first and which follow,
                         with what lag. The early warning signals
                         embedded in the business's own data that
                         the document does not feature in the
                         narrative.

Seasonal mechanics       Recurring patterns tied to the calendar.
                         What is expected at each point in the year.
                         What looks alarming but is actually seasonal
                         and what looks seasonal but is actually real.

Conversion chain         The chain from spend to demand to volume
                         to revenue to margin. Where the chain is
                         efficient, where it leaks, what changes
                         conversion at each step.

Metric interdependencies How metrics move together or against each
                         other. What one thesis metric growing while
                         another is flat implies. What the combination
                         of two signals reveals that neither reveals
                         alone.

Cross-period dynamics    How performance in one period sets up or
                         constrains the next. Carry effects, pull-
                         forward and slippage patterns, the mechanics
                         of how one period's decisions become the
                         next period's results.
```

### What It Must Never Do

Describe the business model itself — that is Stream 01.
Describe organizational decisions about resource allocation — that is
Stream 04. Only the mechanical relationships between metrics —
how the numbers move, not why management decided to move them.

### The Test

This belief would hold even if the management team changed completely.
It describes how the numbers behave, not how the people decide.
A new leader would inherit this mechanic on day one.

---

### Example Belief

```
## Belief #2 — The conversion break between demand and completed
volume is the earliest signal that something in the demand chain
is wrong — and it appears 4-6 weeks before it shows up in the
primary volume metric.
[Status: Confirmed]

Statement: When paid-channel demand grows faster than completed
volume — meaning the demand-to-completion conversion ratio falls
below 0.88 — the primary volume metric misses its forecast target
4–6 weeks later, and the document never features this ratio in
the main narrative.

Why it matters: By the time a volume miss appears in the variance
bridge, the conversion problem already happened four to six weeks
earlier. Watching the conversion ratio in real time gives an early
warning on volume performance that the document does not provide.
This is the signal that gets buried — not because it is unimportant
but because it implicates operational decisions rather than
external factors. When you see a volume miss with an external
factor in the lead attribution, the conversion ratio in the prior
period is usually the better explanation.

Evolution trail: First noticed the lead-lag when conversion dropped
and volume missed forecast the following period. Tested against
three subsequent periods — pattern held in every instance. When
conversion is above 0.92, volume consistently meets or beats
forecast. When it drops below 0.88, it misses. Five observations.
Confirmed.

Normal baseline: Conversion ratio between 0.90 and 0.96 is the
healthy operating range. Below 0.88 is an early warning signal.
Above 0.96 suggests demand is strong enough that even lower-
quality channel volume is converting — a sign of underlying
demand health.

Falsification test: A period where conversion drops below 0.88
and the primary volume metric meets or beats forecast anyway.
That would break the lead-lag relationship and mean the two
metrics have decoupled — which would itself be a significant
signal worth understanding because it would mean the chain
between demand quality and volume realization has changed
structurally.

Provenance:
- Foundation dependency: the conversion chain connecting demand to
  the primary volume metric is a thesis-relevant mechanic (foundation,
  operating chain section)
- Confirming documents: periods 1–5
- Blind passes: period 3 (independently re-derived the same lead-lag
  pattern with no visibility into the prior belief, before promotion
  to Confirmed)
- Contradiction searches: period 4 (searched, none found, before
  promotion to Established)
- Related beliefs: none identified yet
- Last checked: period 5
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 03 — CAUSAL UNDERSTANDING
═══════════════════════════════════════════════════════════════════════

### Purpose

What this business attributes as the causes of performance movement —
and whether those attributions are honest, selective, or strategically
framed. The gap between what the team says caused something and what
the evidence across other streams shows actually moved.

### What It Covers

```
Attribution vocabulary   The specific language this business uses
                         to explain movement. Which words, phrases,
                         and framing constructions recur and what
                         they signal about intent.

Driver sequencing        Which causes are named first, which are
                         secondary, which appear only in appendices.
                         The ordering of the bridge reveals what
                         the team wants attention to land on.

Controllable vs          How the business categorizes its own
external framing         drivers. Whether controllable problems
                         are consistently framed as external.
                         Whether this framing shifts with
                         performance direction.

Attribution verification Where stated causes are supported by
                         observable metric movement vs where they
                         are asserted without corroboration from
                         the data in the same document.

Selectivity patterns     Whether certain causes appear only in
                         miss periods, only in beat periods, or
                         shift with the direction of performance.
                         Selectivity is itself a signal about
                         communication strategy.
```

### What It Must Never Do

State what actually caused performance — that is Stream 02 which
holds the real mechanical drivers. This stream only holds what
the team attributes and whether the attribution pattern is
consistent, selective, or drifting. Never treat stated attribution
as verified causality.

### The Test

A new analyst reading this belief would know what the team will say
in the next miss period before opening the document — and would know
whether to look deeper or accept the attribution at face value.

---

### Example Belief

```
## Belief #2 — The team leads every miss explanation with an
external factor first, always — and the real operational driver
appears third or not at all.
[Status: Established]

Statement: In a miss period, the variance bridge leads with an
external or macro factor, names channel mix second, and buries
or omits operational drivers third — management frames the
shortfall as external, not something it caused.

Why it matters: The sequencing tells you where the team wants
attention to land. External factors cannot be questioned — they
are external. Channel mix is semi-controllable — the team can
acknowledge it without fully owning it. Conversion rates,
product decisions, and pricing execution — the genuinely
controllable drivers — almost never appear in the top two
positions in a miss bridge. When you read the variance bridge,
mentally reorder it. The third item is usually the real story.
The first item is the preferred story.

Evolution trail: Tested across four miss periods. An external
factor led in three of four. Channel mix led in one but an
external factor appeared second. Controllable drivers led in
zero of four. Cross-referenced against the Dynamics stream: in
three of the four miss periods, the conversion ratio had dropped
below threshold in the prior period — a controllable signal —
and conversion appeared below the fold in the bridge or not at
all. The pattern is structurally consistent across every miss
period in the observation window. Four documents. Established.

Normal baseline: In any miss period, the first two bridge items
will be external or semi-external attributions. An external
factor will appear in the top two regardless of its actual
contribution. That is the expected pattern. An anomaly is a miss
period where a controllable driver leads the bridge — that
signals the operational problem is too large or too visible to
frame externally any longer.

Falsification test: A miss period where a controllable driver
— conversion rate, pricing decision, channel investment level —
leads the variance bridge. That would mean either the scale of
the operational miss is undeniable, the team's communication
strategy has fundamentally changed, or new leadership is
running a different framing approach. Any of those would be
a significant signal worth understanding beyond the miss itself.

Provenance:
- Foundation dependency: narration design consistently frames
  controllable misses as external where possible (foundation,
  narration design section)
- Confirming documents: miss periods 1–4
- Blind passes: miss period 3 (independently re-derived the same
  external-first sequencing with no visibility into the prior belief, before promotion
  to Confirmed)
- Contradiction searches: miss period 4 (searched, none found, before
  promotion to Established —
  cross-referenced against the Dynamics stream's conversion-ratio
  belief in the same periods)
- Related beliefs: business_dynamics.2 (conversion-ratio lead-lag
  belief — same underlying phenomenon, viewed from attribution vs.
  mechanics)
- Last checked: miss period 4
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 04 — BUSINESS MEMORY
═══════════════════════════════════════════════════════════════════════

### Purpose

How this organization behaves as a decision-making system under
different conditions. Not what it reports — what it actually does
when performance is under pressure, when facing tradeoffs, when
deciding what to protect and what to sacrifice. The organizational
character revealed through repeated behavior.

### What It Covers

```
Decision patterns        How leadership makes decisions under
under pressure           different performance conditions. What gets
                         protected first. What gets cut first. The
                         decision logic that recurs consistently
                         across comparable pressure periods.

Resource allocation      How the business actually deploys resources
behavior                 versus how it says it will. Where investment
                         goes when there is pressure to redirect it.
                         Whether stated priorities survive contact
                         with a bad period.

Response patterns        How the organization responds to misses and
                         beats — what changes, what does not, and
                         what the pattern of response reveals about
                         what the organization actually values.

Organizational           What the business treats as structurally
protection instincts     protected — the lines, people, or investments
                         it will not touch regardless of pressure.
                         What it consistently sacrifices first when
                         forced to choose.

Initiative delivery      Whether stated strategic initiatives complete,
                         slip, or quietly disappear. The delivery
                         character of the organization — not what it
                         commits to but what it actually follows through on.
```

### What It Must Never Do

Describe what the document says about decisions. Describe the actual
decision pattern evidenced across multiple documents. Never describe
a single period — a one-time behavior is not an organizational
pattern. Business Memory beliefs require at least two comparable
situations showing the same response before they are written.

### The Test

A new analyst reading this belief would know what the organization
will do in the next comparable situation before it does it —
because the behavior has been consistent enough to be predictive.
And they would know what a deviation from that behavior means.

---

### Example Belief

```
## Belief #3 — Demand investment is the last thing that gets cut
under pressure — and when it finally gets cut, something
fundamental has changed in how leadership views the business.
[Status: Established]

Statement: Under pressure, this business cuts overhead and defers
hiring before it ever touches demand spend — so the first time
demand spend gets cut, it will mean leadership no longer believes
that spend is buying profitable growth, not that they are simply
managing costs.

Why it matters: When you see overhead cut and hiring frozen, it
means performance is under pressure but the thesis is intact —
leadership still believes in the demand engine and is protecting
it by cutting everything around it. When you see demand spend
cut, the thesis itself is being questioned. The two signals look
similar in a cost bridge — both are cost reductions — but they
mean completely different things for the business. The first is
a normal pressure response. The second is a statement about the
model. Watching which line moves first tells you more about
leadership's actual confidence than any metric in the document.

Evolution trail: First pressure period — overhead cut, hiring
frozen, demand spend held. Second pressure period — same pattern.
Third — overhead cut again, hiring frozen again, demand spend
held and actually grew slightly. Fourth — same pattern repeated.
Four pressure periods. Zero demand-spend cuts. The pattern is
consistent and deliberate — this is not coincidence, it is a
repeating organizational response to a comparable condition.
Four documents. Established.

Normal baseline: Under pressure, expect overhead reduction and
hiring deferral. Expect demand spend to hold or increase. That
is the organizational reflex. Any other response requires an
explanation — not because it is wrong, but because it represents
a departure from a very consistent pattern.

Falsification test: A pressure period where demand spend is
reduced before overhead is fully exhausted. That single event
breaks this belief entirely and signals that the organizational
thesis about demand-spend return has changed — which changes
everything downstream about how to read the business. When this
happens, do not read it as a cost efficiency move. Read it as
leadership questioning the model.

Provenance:
- Foundation dependency: demand investment is treated as the primary
  thesis-defining spend line (foundation, thesis metrics section)
- Confirming documents: pressure periods 1–4
- Blind passes: pressure period 3 (independently re-derived the same
  overhead-first cutting order with no visibility into the prior belief, before promotion
  to Confirmed)
- Contradiction searches: pressure period 4 (searched, none found,
  before promotion to Established)
- Related beliefs: none identified yet
- Last checked: pressure period 4
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 05 — NARRATIVE UNDERSTANDING
═══════════════════════════════════════════════════════════════════════

### Purpose

How this business tells its story — the deliberate communication
choices the team makes across documents that reveal what leadership
wants you to think versus what the numbers actually show. The gap
between framing and reality, accumulated across many documents.

### What It Covers

```
Structural emphasis      What is placed first, last, in the appendix.
                         The architecture of attention the document
                         creates — what you are meant to see before
                         you see anything else.

Metric anchoring         Which metric becomes the narrative frame —
                         the number established first, through which
                         all subsequent numbers are read. Whether and
                         how the anchor metric changes under different
                         performance conditions.

Performance framing      How good and bad performance are described.
                         The specific language for beats and misses.
                         The softening and escalating constructions.
                         How the same underlying result is packaged
                         differently in different performance contexts.

Confidence language      How assertive or hedged the communication is
                         over time. The shift from confident commitment
                         language to qualified language to monitoring
                         language — and what that trajectory signals
                         before performance data confirms it.

Omission patterns        What is consistently absent where it would
                         be expected. What topics disappear from the
                         main document as they deteriorate. What metrics
                         stop being featured as they weaken.
                         Absence is as informative as presence.

Linguistic fingerprints  Specific words, phrases, and constructions
                         that recur with consistent meaning.
                         What the team always says when an external
                         factor is the lead driver. What language
                         appears when management is defending a
                         miss it owns.
```

### What It Must Never Do

State what actually happened operationally — that is Factual or
Dynamics. Only the communication choices and what they reveal about
what the team wants the reader to conclude. No numbers as beliefs —
numbers are context for a narrative observation, never the
observation itself.

### The Test

A reader of this belief could predict the narrative structure of
the next document before opening it. And when the structure
deviates from the prediction, they notice immediately and
understand what that deviation signals.

---

### Example Belief

```
## Belief #1 — The opening section is a confidence signal not a
content decision — and the team has been consistent enough that
you can read the performance result from the section choice before
you find the number.
[Status: Established]

Statement: When the team opens the document on the efficiency
ratio, the primary volume metric is within 2% of plan; when they
open on cost discipline or margin instead, volume has missed plan
by more than 4% — the opening section is where the team's real
read on the quarter shows up first.

Why it matters: You do not need to find the volume section to
know whether the period was good or bad. Open the document. Look
at the opening section title. The opening choice tells you the
performance direction before you read a number. This sounds
trivial but in practice it is deeply useful — it means you can
walk into a review already knowing whether the team is in a
defensive or confident posture from the moment you see the first
section. It also means you can read the team's confidence level
independently of what the document claims. When the narrative
opening does not match what you know from the Dynamics stream,
that mismatch is information.

Evolution trail: Tracked across six consecutive comparable
documents. Three opened on the efficiency ratio — volume was
within 1.5% of plan in all three. Two opened on cost discipline
or margin — volume missed by more than 4% in both. The sixth
opened on operational efficiency improvement; cross-referencing
with Dynamics, conversion was in the healthy range. Six for six.
This pattern has held without exception across every document
reviewed. Established.

Normal baseline: Opening section is the efficiency ratio versus
forecast. That is the expected document architecture when
performance is on track. Any other opening — cost, margin,
operational metrics — is a tell before you read anything else.

Falsification test: A period where the primary volume metric
misses plan by more than 4% but the document opens on the
efficiency ratio anyway. That would mean the team changed how
they want misses framed — possibly because the miss is so large
that leading with cost is not viable, or because a new
communication approach is being tested. Either way it would break
this belief and would itself be a signal worth investigating.

Provenance:
- Foundation dependency: narration design uses the efficiency ratio
  as the preferred confidence signal (foundation, narration design
  section)
- Confirming documents: document 1–6
- Blind passes: document 3 (independently re-derived the same
  opening-section-predicts-result pattern with no visibility into the
  document-1 Candidate belief, before promotion to Confirmed)
- Contradiction searches: document 4 (searched, none found), document 6
  (searched, none found — cross-referenced against the Dynamics
  stream's conversion reading, which was healthy)
- Related beliefs: none identified yet
- Last checked: document 6
```

---

═══════════════════════════════════════════════════════════════════════
STREAM 06 — FORECAST AND PLAN BEHAVIOR
═══════════════════════════════════════════════════════════════════════

### Purpose

How this business plans, forecasts, and revises over time — the
systematic patterns in how it sets expectations, updates them, and
explains the changes. Not whether forecasts are accurate this period
— whether the forecasting behavior itself is predictable, and what
that predictability reveals about how the business manages expectations.

### What It Covers

```
Planning calibration     How the business sets its annual Plan —
                         whether it is consistently aggressive,
                         realistic, or conservative. The historical
                         relationship between Plan and eventual actuals
                         across comparable periods and years.

Forecast revision        How FC moves through the year. When it is
behavior                 revised, by how much, in which direction,
                         and what triggers revisions. Whether the
                         revision behavior is proactive or reactive.

Systematic bias          Recurring patterns in forecast accuracy
                         by quarter, season, or performance condition.
                         Whether the business consistently over or
                         under-estimates specific metrics in specific
                         periods regardless of the current year's
                         starting conditions.

Guidance calibration     How externally communicated guidance relates
                         to internal FC — consistently conservative,
                         in line, or aggressive. Whether guidance
                         has historically tracked to eventual results
                         or systematically diverged.

Revision attribution     How the business explains forecast changes.
                         Whether revision explanations are consistent
                         with actual drivers or follow the same
                         selective attribution pattern as miss
                         explanations.
```

### What It Must Never Do

State actual forecast vs actual values as beliefs — those are
Factual Understanding (Stream 00). Only the behavioral pattern of
how forecasting is done and what that pattern reveals about how
the business manages expectations over time.

### The Test

A reader of this belief can predict, before the new FC is released,
approximately what it will say, in which direction it will be
revised, and roughly how large the revision will be — based on
the established behavioral pattern rather than the current
period's data.

---

### Example Belief

```
## Belief #1 — The early-year forecast is always optimistic and the
late-year forecast is always conservative — and the revisions are
not corrections, they are scheduled.
[Status: Established]

Statement: This business sets its early-year forecast above what
actuals eventually land at, and its late-year forecast below —
a consistent bias, not random error, that the planning process
produces regardless of how the year starts.

Why it matters: When early-year actuals miss FC, that is not
underperformance. That is the expected bias materializing on
schedule. When late-year actuals beat FC, that is not
outperformance. That is the conservative cushion being released.
Reading either as genuine signal leads to wrong conclusions. The
FC is not the performance target — it is a communication artifact
with a known directional bias that must be adjusted for before
interpreting results against it. An analyst who does not know
this will consistently over-react to early-year misses and
under-react to late-year beats.

Evolution trail: Early-year FC above actuals in four consecutive
comparable periods across two years. Late-year FC below actuals
in four consecutive comparable periods across two years. Pattern
consistent in direction and magnitude across both years. Not a
coincidence. The planning process is producing these biases
systematically. Four comparable period observations across two
years. Established.

Normal baseline: Early-year actuals will miss FC by a consistent
margin. Late-year actuals will beat FC by a consistent margin.
Both are expected and neither is signal. Signal is an early-year
miss larger than the typical range — that means performance is
worse than even the optimistic baseline. Signal is a late-year
miss of any size — that means the conservative cushion was not
enough and something structural broke in the final period.

Falsification test: An early-year period where actuals meet or
beat FC. That would mean either the planning process has been
recalibrated toward realism, or the business genuinely
outperformed against a structurally optimistic baseline — and
understanding which one it is matters significantly for how to
read forward guidance. A late-year miss of any size is an even
stronger falsification — it means the conservative cushion
failed, which has not happened in any period reviewed.

Provenance:
- Foundation dependency: the planning process's calibration against
  thesis metrics is expected to be consistent year over year
  (foundation, thesis metrics section)
- Confirming documents: early-year and late-year FC across 2
  comparable years (4 comparable periods)
- Blind passes: year 2's early-year FC (independently re-derived the
  same optimistic/conservative split with no visibility into the
  year-1 Candidate belief, before promotion to Confirmed)
- Contradiction searches: year 2's late-year FC (searched, none found,
  before promotion to Established)
- Related beliefs: none identified yet
- Last checked: year 2's late-year FC
```

---

═══════════════════════════════════════════════════════════════════════
HOW BELIEFS FEED THE LEADERSHIP BRIEF
═══════════════════════════════════════════════════════════════════════

The beliefs across all seven streams are the input to the
pre-reading brief that leadership receives before opening any
new document. The brief does not show the beliefs. It uses them.

```
Beliefs are the analyst's memory.
The new document is what is on the table.
The brief is what the analyst tells leadership
before the meeting starts.
```

The brief answers six questions from the accumulated belief
knowledge applied against the new document:

```
1. The one thing to know before anything else.
2. What is normal this period — what to ignore.
3. What actually changed from the established pattern.
4. Where to look in the document and what to look for.
5. The one question that cuts through everything.
6. What the next document should show — and what would break it.
```

Leadership walks in already knowing. The beliefs made that possible.
The brief is how they experience it.

---

*End of stream definitions document.*
