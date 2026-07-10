# Belief — Full Specification

*Institutional memory is portable: what is normal, what is template, what is evolving, and what would break — loaded into agents at the moment they draft, validate, or flag — instead of re-teaching the model from raw decks every time.*

*Gogul Kumar Mathi · 2026*

---

## 01 — What Is Belief

### The Source

Every organization produces recurring documents as part of how it operates: quarterly business reviews, earnings calls, investor presentations, board decks, operating reports. These are not incidental outputs — they are the formal record of how management interprets performance, explains outcomes, and communicates direction.

What those documents contain, beyond the numbers:

- How this team explains performance — what causes they name, in what order, framed how
- Which metrics they treat as primary versus secondary
- How emphasis shifts when results disappoint
- What language recurs, and what language disappears
- How commitments are explained when they are not met

These behavioral patterns are not visible in any single document. They only emerge after reading many comparable documents from the same entity over time.

### The Analyst Analogy

A senior analyst who has been reading the same business's quarterly reviews for ten months holds a mental model that no one has written down. They know what a normal deck looks like for this business — so they immediately see what is unusual about this one. They know how this management team typically explains a shortfall. They know which commitment is always ambitious and which is typically conservative.

They know that when the deck leads with a small beat, the real story is always in the second half of the bridge. They know that when the word "investment" appears in the cost commentary, it means discretionary spend the team chose — not external pressure. They know that the Q2 sequential pattern in this business always looks like a softening that recovers in Q3, and that certain numbers are structurally low because of how the business closes its quarter.

None of that knowledge lives in any single document. It accumulated across dozens of documents, hundreds of reviews, and years of pattern recognition. That analyst is the most valuable person in the room during a business review. And any AI deployed against the same documents starts each session knowing nothing that she knows.

They don't remember every slide. They hold the pattern. That pattern is the belief.

That accumulated understanding isn't in a file. It isn't queryable. When the analyst leaves, it leaves with them.

### What Belief Is

Belief reads business process deliverables — the recurring decks, transcripts, reports, and documents that organizations already produce — and builds a living model of how the business works and behaves.

Not what any single document says. The pattern of behavior visible only across many comparable documents over time.

It doesn't store facts. It accumulates beliefs. And beliefs are different.

### The System Learns the Business From the Documents

A critical design principle: **the system discovers the business model by reading — it doesn't require the user to describe it upfront.**

The documents already contain the business model. Every quarterly review, earnings transcript, or board deck includes management's explanation of what drove the results: "Q1 marketing investment drove Q2 new customer volume," "when transaction volume crosses this threshold, supplier economics improve," "the cost structure is largely fixed, so volume softness flows directly to margin." These are explicit relationship claims — statements connecting one metric to another with direction, lag, and mechanism.

The belief system treats these relationship claims as its most valuable signal type. When a document says A drives B, that is not a framing observation — it is a structural claim about how the business works. It should become a belief from the moment it first appears, marked Candidate, and confirmed or contradicted as more documents arrive.

This means:
- The user doesn't need to explain how the business works before any documents are read
- The foundation doesn't need to pre-encode the operating chain or causal model
- The first 1–3 documents build the preliminary business model from what management explicitly states
- Later documents deepen, refine, or challenge that model
- The accumulated Stream 02 beliefs become the discovered business model — earned from reading, not specified from assumption

The analyst analogy holds here too. A new analyst joining a business doesn't start with a business model document. They read the company's own communications. Those communications contain the model — management explains it every period. The belief system does the same thing, systematically, at scale.

**Facts vs Beliefs**

- A fact: Revenue was $2.3B in Q3.
- A belief: Revenue growth is increasingly dependent on pricing rather than volume, suggesting the business is extracting from its existing base rather than expanding it.

Facts are static. Beliefs carry direction, confidence, and trajectory. Beliefs tell you what to expect in the next document — and what would constitute a surprise worth investigating.

### What a Belief Is Not

| Not this | Why a belief is different |
|---|---|
| A **fact** to look up | A fact is retrieved and static. A belief is applied as working truth and can change. |
| A **document summary** | A summary describes what a document said. A belief describes what the pattern of documents means. |
| A **metric reading** | A metric is a value at a point in time. A belief is the durable interpretation of how a metric behaves over time. |
| A **management attribution** | Management saying "efficiency improved because of better process" is reported attribution. The belief is whether that attribution is consistent, how it is framed, and whether the numbers support it. |

### The Failure Modes Beliefs Prevent

These are the failure modes that appear when AI works with recurring business documents without institutional memory.

**The summary trap.** AI tools produce accurate summaries of individual documents. But a summary of what this document says is not the same as knowing what this document means in the context of everything that came before it. The belief system doesn't summarise. It maintains standing interpretations that exist independently of any single document.

**The attribution fabrication trap.** AI models are fluent with causal language. They connect observations to explanations with confidence. "Revenue declined because of FX headwinds" — but was it? Or did the team attribute it to FX because FX is an uncontrollable external factor that absolves accountability for a controllable miss? The belief system separates management's stated attribution (what they said caused it) from verified causality (what actually caused it). These are different beliefs, tracked separately, evolved separately.

**The recency trap.** An AI reading this month's deck in isolation treats everything in it as equally newsworthy. A senior analyst who has read 18 months of decks knows that three of the five items in this month's bridge are structural recurring patterns — not news — and the one genuinely new signal is buried in a footnote on slide 12. The belief system creates that distinction mechanically: what is expected (held as a belief) versus what is new (not yet matched to any belief, or contradicting a held belief).

**The vocabulary drift trap.** Business teams change the language they use to describe things over time — sometimes deliberately, sometimes not. When a word disappears from commentary, it might mean the thing stopped happening, or it might mean the team stopped wanting to highlight it. When a new phrase appears, it might reflect a genuine strategic shift or a narrative management choice. A system that tracks beliefs about language patterns surfaces vocabulary drift as a signal. A system that just reads the current document doesn't notice.

### What a Belief Contains

The belief memory carries four kinds of institutional understanding:

| What it captures | Where it lives in the system | What it gives you |
|---|---|---|
| **What is normal** | Normal baseline (belief entry field) | Expected ranges and behaviors — deviations are immediately visible without re-reading the archive |
| **What is template** | Entity foundation — signals-vs-noise | What this entity always says, what language is formulaic, what to discount so the real signal stands out |
| **What is evolving** | Evolution trail (belief entry field) | Per-document history of how the pattern developed — deepened, tensioned, narrowed, or shifted perspective |
| **What would break** | Falsification test (belief entry field) | The specific signal in a future document that would contradict, narrow, or retire the belief |

These four things — loaded into an agent at the start of a drafting, validation, or flagging task — replace the need to re-teach the model from raw decks every time. The belief memory is the institutional knowledge; the raw documents are the evidence it was built from. Once the belief exists, the document doesn't need to be re-read.

Each belief entry has five narrative fields — **Statement**, **Why it matters**, **Evolution trail**, **Normal baseline**, **Falsification test** — plus a structured **Provenance** record that makes the verification behind the narrative machine-checkable.

### Skills and Beliefs

A skill does the task — pulls the numbers, builds the report. It runs on whatever it can infer about the business at the time.

A belief is the understanding the task is performed *from* — the working model behind the doing. Skills take the doing; beliefs take the thinking.

---

## 02 — The Belief

### A Belief Defined

A belief is a durable, falsifiable, actionable interpretation of how a business behaves — supported or challenged by evidence across many documents. It is not a fact. It is not a metric. It is not a slide summary. It is the compressed judgment that a trained analyst would carry in their head after months of reading.

### What Makes a Belief a Belief

- **Durable** — independently re-derived across documents, not just confirmed by a pass that already knew what it was checking for
- **Falsifiable** — a future document can confirm or contradict it, and that contradiction has actually been searched for, not just theoretically possible
- **Grounded** — depends on a named foundation claim (by claim ID, e.g. `foundation.business_model`), and is flagged `[FOUNDATION_CHANGED]` if a Foundation Review revises that claim
- **Actionable** — it tells you what to expect next, and what would constitute a surprise worth investigating — provable with a concrete before/after answer to a stated query
- **Direction** — Improving, Stable, Deteriorating, or Unclear
- **Confidence** — a number from 0.05 to 0.95 reflecting how strongly it is held

Each of the first four is a procedural test, not a descriptive claim — see "The Two-Test Gate" below for what process must have actually happened before each can be claimed.

### Also Not a Belief

Beyond the core distinctions (not a fact, not a rule, not agent memory), a belief is also not:

- A **metric reading** — a specific value at a specific point in time
- A **one-period observation** — something a single document mentioned that hasn't recurred
- A **document summary** — what a document said, not what it means
- An **opinion** about whether performance is good or bad
- A **projection or forecast** — a belief describes what is, not what is predicted

### The Dual Nature: Durable AND Provisional

A belief must be durable enough to act from — it should not be abandoned after one contradicting document. But it must also be provisional — open to revision when accumulated evidence warrants it.

These two properties aren't in tension. They define the difference between a belief and either a reflex (no durability) or a bias (no provisionality).

Nir Eyal in *Beyond Belief* frames this precisely: the best beliefs are both practical and provisional — they offer just enough certainty to act, yet enough flexibility to adapt. A belief is a firmly held interpretation, open to revision when new evidence arrives. A belief that requires ignoring evidence to sustain itself is not a belief. It is a bias.

### Two Kinds of Belief Revision

Not all revision is the same.

**Incremental update** — The statement is refined as confidence rises or falls. The interpretive frame stays intact. A belief about "external attribution patterns" becomes more confident as three more comparable documents confirm it, or weakens as two consecutive documents show a different framing. The frame itself is stable.

**Perspective shift** — Enough evidence accumulates to suggest a fundamentally different interpretation of what has been observed. The frame itself changes. What looked like "cost efficiency behavior" was actually a response to a structural market constraint. What looked like "consistent external attribution" was a temporary framing choice that has now reversed. The prior evidence trail doesn't become invalid — it's now understood differently.

A perspective shift is not a failure of the previous belief. The previous belief was the best available interpretation at the time, held provisionally. A perspective shift is what a working belief model is designed to produce: accumulated evidence eventually changing not just confidence, but understanding.

### The Durability Ladder

A belief passes through maturity stages as more comparable documents are processed. Do not skip stages — and do not promote a stage without the verification that stage requires. **Rigor follows citation weight:** the gates sit one rung lower than plain confirmation-by-count, so that forming a hypothesis is cheap and the expensive verification is spent only where trust is actually consumed (the un-hedged tiers).

| Stage | Documents | What It Means | Verification required to enter | Citable as |
|-------|-----------|---------------|--------------------------------|------------|
| **Candidate** | 1 | A signal with the shape of a durable pattern. Every first-document entry is Candidate. | None — nothing to check against yet. | Not citable |
| **Provisional** | 2 | Two comparable documents support the pattern. An honest hypothesis. | Plain recurrence across a second comparable document. Forming a hypothesis is cheap by design. | Only as "unverified recurrence" — hedged |
| **Confirmed** | 3 | Three documents, and the pattern was independently re-derived blind. The first tier of real trust. | A blind pass independently found the same pattern. A belief-aware-only confirmation does not promote — flag for review. | Without hedging |
| **Established** | 4+ | The pattern is structural; it survived an active contradiction search. Breaking it is meaningful signal. | Contradiction search reported clean ("searched, none found"). Holds across document types if applicable. Foundation claim still current. | Without hedging |

**Decay walks a belief down the ladder.** A belief untouched by any relevant signal descends one rung per silence window (default 4 consecutive silent comparable documents): Established → Confirmed → Provisional. At the Provisional floor it is marked **STALE** rather than dropping to Candidate — its evidence still exists; it is untested, not unfounded. This changes Status, not just Confidence, and is tagged `[DECAY]`. The point is that "Established six months ago, untested since" and "Established and still being challenged" can never be cited with the same confidence — and a STALE belief whose pattern resurfaces re-enters verification rather than coasting on a status it earned long ago.

### The Four Update States

| State | What Happened | Confidence Change |
|-------|---------------|-------------------|
| **New Prior** | No existing belief covers this signal | Seed at 0.20 |
| **Confirm** | New document supports this belief | +0.08 |
| **Contradict** | New document challenges this belief | −0.15 |
| **Decay** | Not seen in 90+ days | −0.05 per cycle |

Cap: 0.95 (0.90 for causal beliefs). Floor: 0.05. Archive below 0.10.

These arithmetic updates handle incremental revision. They don't handle perspective shifts. When contradictions accumulate to the point where the interpretive frame itself is wrong — not just weakened — the belief engine must assess whether a reframe is warranted rather than continued decay. See Section 07 (Scope Boundaries) for when to retire vs reframe.

This day-based Decay row adjusts Confidence only. It is a separate mechanism from the document-count-based `[DECAY]` tag under the Durability Ladder above, which downgrades Status from Established to Confirmed after N silent comparable documents. A belief can lose Confidence without losing Status, and can lose Status without its Confidence score having crossed any threshold — they track different things.

**Status outranks Confidence.** The two signals answer different questions and are not interchangeable. Status is earned through verification — a blind pass to reach Confirmed, a reported contradiction search to reach Established — and is the signal that governs how a belief may be cited. Confidence is arithmetic bookkeeping: it tracks incremental strengthening and staleness *within* a status and drives archival of neglected beliefs. Confidence can never promote a belief past the verification its status requires. A belief at Confidence 0.90 whose Provenance shows no blind pass is still Provisional at most, must be cited as unverified recurrence, and its high score means only that it has been repeatedly echoed — which is precisely the condition the Process Test exists to catch.

### The Fact-to-Belief Gate

Not everything in a document becomes a belief. Most things should produce silence. The gate is the filter.

| Gate State | Action |
|------------|--------|
| Fact only — a metric, a date, a result with no durable interpretation | Stay silent |
| Supports or challenges an existing belief but cannot create a new one | Update existing belief |
| Strengthens an existing belief without rewriting it | Confirm +0.08 |
| Challenges an existing belief | Contradict −0.15 |
| Implies something durable that no existing belief covers | New prior at 0.20 |

**The Two-Test Gate — both required before a belief is written or promoted:**

**Content Test** — is it insightful? Three sub-checks:
1. **Interpretation** — does this say something the document does not say? A belief is what the documents collectively reveal that none of them state directly. If you can find it by reading one document, it is an extraction, not a belief.
2. **Falsifiability** — can a future document contradict this?
3. **Distinctiveness** — is this specific to this business, not any business in this sector?

**Process Test** — is it trustworthy? Was this belief actually checked for being wrong, not just checked for being right?
1. **Independent re-derivation** — has at least one blind pass (extraction with no visibility into the existing belief) found the same pattern, or has every confirmation come from a pass that already knew what it was supposed to find?
2. **Active contradiction search** — has a pass actually searched for evidence against this belief and reported the result — "searched, none found" — rather than simply not encountering contradiction?

The two tests do different jobs. **The Content Test decides the tier; the Process Test decides the rung.** A recurring regularity that fails the Content Test is not discarded — it is reclassified as an **Observation** (see below). A belief that passes the Content Test but fails the Process Test is not discarded either — it is held at the highest rung its evidence supports (recurrence alone → Provisional, cited as unverified). Passing one test does not excuse the other, but failing one is never a reason to throw useful memory away.

### Three Tiers of Memory — the Master Test Classifies, It Does Not Discard

The earlier design treated the master test as an admission gate: pass it and become a belief, fail it and be thrown away. That optimized for the purity of the apex and discarded the useful middle of the pyramid — and with only a handful of documents almost nothing can *legitimately* be a verified belief, so the system yielded nearly nothing. A convention held stable across every document ("they always report three benchmarks in this fixed order") fails the master test, yet it is exactly the institutional memory a new analyst wants on day one.

So the master test is a **classification rule, not an admission gate.** Everything entity-specific and recurring is stored, at the tier its evidence and interpretation earn:

| Tier | Where | What it holds | Cited as |
|------|-------|---------------|----------|
| **Foundation fact** | `foundation.md` | Definitional constants — metric definitions, benchmark structure, the reporting scaffold. Recurs *identically* and is definitional. | As fact |
| **Observation** | `observations.md` | Entity-specific recurring regularities that carry little or no interpretation — reporting conventions, vocabulary habits, structural patterns. **Fails the master test** (findable in one document). | As "unverified pattern," never as a belief |
| **Belief** | `belief.md` | Durable, falsifiable *interpretation* — something the documents collectively reveal that none states directly. **Passes the master test.** | By Status, hedged below Confirmed |

When the engine finds a recurring regularity it asks the master test: does this say something no single document says? Yes → belief candidate, subject to the Two-Test Gate. No → an **Observation**, stored in a lightweight two-field form, citable honestly as an unverified pattern. Nothing useful is thrown away; nothing weak impersonates a belief. An Observation that later acquires genuine interpretation is *promoted* to a new belief — the only bridge between the tiers.

### Facts, Memory, and Beliefs Are Different Things

Beyond the three storage tiers, the system distinguishes what a fact log *is* from what a belief *is*:

- **Facts** — what a document literally states. Captured per document in the fact log.
- **Memory** — the full, permanent, addressable record of every fact log ever produced for this stream. Not compressed. Not discarded once a belief has been drawn from it.
- **Beliefs** — the compressed, tested conclusions drawn from memory. Not memory itself — a claim about what memory, examined and checked for contradiction, implies.

A fact log is not disposable intermediate output consumed once by the belief engine and thrown away. It is the memory a belief's Provenance record points back into. The Evolution trail is a readable narrative generated from that memory — it doesn't compete with the Provenance record for truth, and it isn't itself the record of what happened.

This distinction is what makes a Retired or Contradicted belief diagnosable rather than a dead end. Marking a belief Retired tells you it failed. It doesn't tell you *why* — whether the verification process broke down, whether the foundation claim it depended on was wrong, whether the match ledger routed evidence into the wrong belief, or whether the sample was simply unlucky. That diagnosis is only possible if the memory the belief was built from — the fact logs, the match ledger, the version snapshots — is still there, addressable, to trace back to.

### What a Mature Belief Looks Like

After five or more comparable documents, a belief entry looks like this. The heading is a complete, specific, falsifiable sentence — not a category label. The same structure — five narrative fields plus the Provenance record — applies to every stream, but what it contains differs by stream.

---

**Stream 05 example — document-level patterns**

**## Belief #7 — Every Variance Headline Opens With the Best-Performing Driver; the Negative Is Always the Second Clause**
**Status:** Established | **Confidence:** 0.60 | **Direction:** Stable

**Statement:** Established across five documents. Every variance headline in every deck is structured positive-first without exception. Whether the overall result is a beat or a miss, the opening attribution clause names a positive driver. In beats, the leading positive is the dominant contributor. In misses or mixed results, the team still locates a positive to lead with before acknowledging the headwind. The negative driver is structurally relegated to the second clause in every instance across all five documents. This is a systematic narrative convention, not a neutral factual ordering.

**Why it matters:** A reader who knows this pattern knows to find the actual commercial story in the offset clause, not the headline. A reader who doesn't know this pattern will systematically overweight the opening attribution because it leads.

**Evolution trail:** First seen in Document 1 — the headline led with channel efficiency ahead of a modest miss; I noted it but held it as a single observation. Document 2 repeated the same structure: a positive driver led even though the result was flat. At that point I held it as Provisional. Documents 3, 4, and 5 each confirmed the same structure without exception, including one document where the business posted its weakest result of the period — and still led with the best available positive. Established.

**Normal baseline:** In the next comparable document, the first clause of every variance headline will name the most favourable driver available, regardless of whether the overall result is positive or negative.

**Falsification test:** A headline that opens with a miss, headwind, or structural deterioration before stating any positive contributor would indicate a break in the team's narrative sequencing convention and should be investigated immediately.

**Provenance:** Foundation dependency: `foundation.narration_design` — narration design consistently frames results positive-first | Confirming documents: Doc 1–5 | Blind passes: Document 3 (independently re-derived the same positive-first ordering with no visibility into the prior belief, before promotion to Confirmed) | Contradiction searches: Document 4 (searched, none found, before promotion to Established), Document 5 (searched, none found — this was the weakest-result document and still confirmed) | Related beliefs: none identified yet | Last checked: Document 5

---

**Stream 02 example — performance track record**

**## Belief #3 — Revenue Guidance Has Been Met or Exceeded in 7 of 8 Comparable Quarters; the One Miss Was Preceded by a Specific Language Shift**
**Status:** Established | **Confidence:** 0.72 | **Direction:** Stable

**Statement:** This business delivers against its stated revenue guidance in 7 of 8 comparable quarters, median beat 1.4%. The single significant miss (−3.1%, Q3) was preceded in the prior-period document by a shift in forward commitment language from "we expect" to "we are targeting" — the only instance of that language shift in the record. Revenue guidance reliability is high; the language shift is a leading indicator that has now been confirmed once.

**Why it matters:** High guidance reliability means a miss is signal, not noise. The language shift pattern, if it recurs before another miss, becomes an early warning indicator one period ahead of the result.

**Evolution trail:** First three documents established the beat pattern. Q3 miss prompted investigation — reviewing prior document found the language shift. Subsequent five documents have all been beats with "we expect" language. One data point on the language shift; tracking for recurrence.

**Normal baseline:** Next comparable document delivers at or above stated revenue guidance. Forward commitment language reads "we expect" or equivalent directional certainty.

**Falsification test:** Two consecutive misses without a prior-period language shift would break the guidance reliability belief. A language shift that does not precede a miss would narrow the leading indicator belief.

**Provenance:** Foundation dependency: `foundation.metrics.revenue_delivery` — revenue delivery is the primary commitment metric | Confirming documents: Q1–Q8 (8 comparable quarters) | Blind passes: Q3 (independently re-derived the same beat pattern with no visibility into the prior belief, before promotion to Confirmed) | Contradiction searches: Q4 (searched, none found, before promotion to Established), Q6 (searched — found the miss and the preceding language shift, recorded as the leading-indicator sub-claim rather than a break) | Related beliefs: none identified yet | Last checked: Q8

---

**Stream 02 example — relationship claim initialized from document one, then deepened**

**## Belief #5 — Spend Concentration Against the Core Volume Metric in Q1 Drives New Customer Volume in Q2 With a 6–8 Week Lag; the Chain Has Held in 6 Consecutive Cycles**
**Status:** Established | **Confidence:** 0.78 | **Direction:** Stable

**Statement:** This business runs a deliberate spend-to-acquisition mechanic. Marketing spend rises against the core volume metric in Q1 (typically 28–34% range) as the business runs a concentrated acquisition push. New customer volume follows in Q2 with a 6–8 week lag from peak Q1 spend. This mechanic was first stated explicitly by management in the first document reviewed and has been confirmed across 6 consecutive Q1→Q2 cycles. Q1 spend concentration is not a problem — it is the thesis executing.

**Why it matters:** An agent reading the Q1 spend ratio in isolation will flag it as elevated. An agent that holds this belief will correctly interpret it as the acquisition-investment phase of a mechanic that management has stated explicitly and that the delivery record has confirmed across 6 cycles. The calibration changes the entire downstream interpretation.

**Evolution trail:** First seen in the first document reviewed — management stated: "our Q1 marketing investment is designed to drive new customer signups; we typically see conversion into new customer volume over the following 6–8 weeks." I initialized this as a Candidate relationship belief on the first document where it appeared — the explicit causal claim was sufficient to warrant tracking. The first Q1→Q2 cycle confirmed the timing. The second cycle the same. By the third cycle I had observed the mechanic in three cycles and advanced to Confirmed. Cycles 4–6 narrowed the spend range to 28–34% and confirmed the 6–8 week lag. The chain is now Established — deviation in either direction is the signal worth investigating, not the concentration itself.

**Normal baseline:** Q1 spend ratio in 28–34% range. Q2 core volume metric at or above FC by mid-quarter. Lag between peak Q1 spend and new customer volume: 6–8 weeks.

**Falsification test:** A Q1 with the spend ratio in range that does not produce Q2 new customer volume by week 10 would indicate the mechanic has broken. Management no longer describing the Q1 spend as an intentional acquisition investment — a language shift in how they explain Q1 — would be an early warning signal worth tracking before the next cycle confirms or denies the break.

**Provenance:** Foundation dependency: `foundation.metrics.spend_and_core_volume` — spend and the core volume metric are the two primary thesis metrics | Confirming documents: cycles 1–6 | Blind passes: cycle 3 (independently re-derived the same Q1→Q2 lag with no visibility into the prior belief, before promotion to Confirmed) | Contradiction searches: cycle 4 (searched, none found, before promotion to Established), cycle 5 (searched, none found) | Related beliefs: none identified yet | Last checked: cycle 6

---

A mature belief stream holds 12–20 entries at this level of specificity across all streams. Together they cover what is structurally established, what is under tension, and what is being watched as a Candidate. Any analyst — or any AI model — loading the full stream before opening the next document is informed in ways that are impossible to replicate by reading that document alone.

---

### The Difference Between Extraction and Belief

The clearest way to understand the master test is to see it applied. Each pair below starts with a statement that fails, then shows what it should become.

---

**Pair 1 — Document observation vs. business insight**

*Extraction (fails the master test):*
> The entity consistently reports its core volume metric against three benchmarks in this order: Plan, FC, then prior year — without varying the sequence.

This describes how the deck is structured. A new analyst reads it and learns nothing about the business. They learn something about a formatting convention. They could discover this in five minutes by opening any document. It is not something accumulated across months of reading — it is something visible on the first page of the first document.

*Belief (passes the master test):*
> This entity's growth is a ceiling problem disguised as an efficiency story. Revenue has grown while core volume has stagnated. Management frames this as pricing sophistication — and the efficiency improvements are real. But what they reveal is that the business cannot expand demand; it can only extract more from demand that already exists. The S&M efficiency story is covering a structural ceiling the documents never name directly.
>
> Why it matters: Every efficiency improvement buys time. It doesn't solve the underlying problem. When you read any document from this entity, the question isn't whether efficiency improved. It's whether volume moved. If it didn't, the business is closer to the ceiling than the narrative suggests.

The second version makes a claim someone could argue with. It names something the documents don't say. It changes what you look for in every future document.

---

**Pair 2 — Sector knowledge vs. entity-specific understanding**

*Extraction (fails the master test):*
> Q1 marketing spend concentration is the structural lead signal for Q2 volume growth — a deliberate acquisition mechanic, not a cost problem.

This applies equally to any business in this sector. Any subscription or consumer business invests ahead of an acquisition push. An analyst who has never read a single document from this entity could write this from general knowledge. It reveals nothing specific about how this business actually works.

*Belief (passes the master test):*
> Under pressure, this entity manages the narrative before it manages the problem. Every miss period in the record follows the same attribution sequence: external factors first, channel mix second, volume third. Controllable decisions come last or not at all. But the dynamics stream shows the actual primary driver in miss periods is consistently conversion efficiency — how efficiently demand becomes completed transactions. That metric rarely leads the bridge. The team has learned that external attribution is accepted more readily than operational attribution, so the story is structured to lead with what cannot be controlled before reaching what can.
>
> Why it matters: When you hear external factors leading the attribution in a miss, don't spend time on those factors. Ask about conversion. That's where the real explanation lives. The narrative isn't wrong — the external factor did have an effect. But it is not the lead driver. It is the lead story.

The second version reveals something that requires months of reading the same documents to see. It is specific to this entity's communication pattern. It names what isn't in the document.

---

**Pair 3 — Behavioral description vs. interpretive judgment**

*Extraction (fails the master test):*
> This entity consistently protects its core demand investment when EBITDA is under pressure, cutting overhead and headcount before touching demand spend.

This describes a behavior without saying what it means. A fact is "they protect demand investment." A belief is what that protection reveals about this organization's actual priorities — and what it means when it breaks.

*Belief (passes the master test):*
> The deck's opening slide is a confidence indicator, not a content decision. Documents that open on the efficiency metric are documents where the team believes efficiency is the strongest story they have. Documents that open on cost discipline or EBITDA are documents where they don't. The document template doesn't mandate the opening sequence — the team chooses it. And they consistently choose the metric they most want leadership to anchor on.
>
> Why it matters: Look at the opening slide before reading anything else. If it's not the primary efficiency metric, you already know the volume number is difficult. The team told you by choosing not to lead with it. This is faster and more reliable than scanning to find the volume number.

---

These pairs demonstrate the standard the belief engine must reach. Extractions describe what is in the documents. Beliefs say what the documents — collectively, over time — reveal that none of them state directly. If a belief passes the master test, someone reading it for the first time understands something specific and important about this business that they could not have inferred from general knowledge.

---

## 03 — The Seven Belief Streams

Seven streams. Each owns exactly one discriminating axis — one type of understanding that no other stream claims. Every signal from every document belongs to exactly one stream. If two streams could plausibly hold a belief about the same signal, the stream design has failed.

Each stream also has a test — a single question that separates beliefs that belong here from beliefs that don't.

This section carries the spec-level definition of each stream. The full worked examples — one complete belief entry per stream, with Provenance — live in `STREAMS.md` and only there.

---

### Stream 00 — Factual Understanding

**Purpose:** The verified, stable factual record of how this business is measured. Not what the numbers mean — what they definitively are and whether they are consistent.

**What it covers:**
- Metric definitions and whether they hold stable across documents
- Benchmark sequence and whether it ever shifts
- Calculation bases — net vs gross, adjusted vs reported
- Data source and system consistency
- Scope stability — same segments, geographies, channels included each period

**What it must never do:** State interpretation. Never say what a number means for the business. Never say whether performance is good or bad. Only what is verifiably true and whether it is consistent.

**The test:** Any analyst with the source document can verify this belief independently. It is re-checkable.

**Worked example:** see `STREAMS.md` — Stream 00 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 01 — Business Model Understanding

**Purpose:** The durable understanding of how this specific business makes money — not what it reported, but what the underlying economic engine is and whether it is working.

**What it covers:**
- The profitability thesis — the core bet this business is making
- Which metrics reveal whether the thesis is holding vs breaking
- The revenue model — what drives the top line at a structural level
- The margin structure — where margin is made and where it leaks
- The growth engine — price vs volume, new vs existing, sustainable vs finite
- Unit economics — is the business getting more or less efficient per unit of output

**What it must never do:** Report what happened this period. Never state a metric reading. Never describe a document. Describe the economic model, not the economic results.

**The test:** This belief is true regardless of which specific period is being reviewed. It describes how the business works, not what it did.

**Worked example:** see `STREAMS.md` — Stream 01 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 02 — Business Dynamics

**Purpose:** How the parts of the business move relative to each other over time. Not what the model is — how it behaves mechanically. Lead-lag relationships, seasonal cycles, conversion chains, feedback loops.

**What it covers:**
- Which metrics move first and which follow, with what lag
- Seasonal mechanics — what is expected at each point in the year
- The conversion chain — from first spend to final output
- Where the chain is efficient, where it leaks, what changes conversion at each step
- How one period's performance sets up or constrains the next

**What it must never do:** Describe the business model — that is Stream 01. Describe organizational decision patterns — that is Stream 04. Only the mechanical relationships between metrics.

**The test:** This belief would hold even if the management team changed. It describes how the numbers move, not how the people decide.

**Initialization rules:**

| Belief type | Can initialize from doc 1? | Condition |
|-------------|---------------------------|-----------|
| Relationship claim (explicit) | Yes — Candidate | Document explicitly states the relationship in causal language |
| Lead-lag mechanic (explicit) | Yes — Candidate | Document states the timing |
| Lead-lag mechanic (inferred) | Doc 2 minimum | Two periods required to observe the pattern |
| Conversion chain | Yes — Candidate (partial) | Mark as incomplete until more links confirmed |
| Stress behavior | After first pressure episode | Requires observing at least one pressure period |
| Feedback dynamics | After two comparable episodes | Requires two stress or recovery periods |

**Worked example:** see `STREAMS.md` — Stream 02 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 03 — Causal Understanding

**Purpose:** What this business attributes as the causes of performance movement — and whether those attributions are honest, selective, or strategically chosen. The gap between what the team says caused something and what the evidence shows.

**What it covers:**
- Which causes are named, in what order, with what language
- Whether the attribution is consistent across comparable periods
- Whether external factors are used selectively to explain controllable misses
- Whether controllable problems are framed as external
- The gap between stated attribution and what the dynamics stream shows actually moved

**What it must never do:** State what actually caused performance — that belongs in Stream 02. Only what the team attributes and whether that attribution pattern is consistent or selective.

**The test:** A new analyst reading this belief would know what the team will say before opening the document — and would know whether to believe it.

**Worked example:** see `STREAMS.md` — Stream 03 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 04 — Business Memory

**Purpose:** How this organization behaves as a decision-making system under different conditions. Not what it reports — what it actually does when performance is under pressure, when facing tradeoffs, when deciding what to protect and what to sacrifice.

**What it covers:**
- Decision patterns under pressure — what gets protected, what gets cut
- What the organization treats as structurally protected regardless of conditions
- How leadership responds to misses vs beats
- Whether stated priorities survive contact with a difficult period
- The organizational character — what it values when forced to choose

**What it must never do:** Describe what the document says about decisions. Describe the actual decision pattern evidenced across documents. Never describe a single period — always the recurring behavior.

**The test:** A new analyst reading this belief would know what the organization will do before it does it — because the behavior has been consistent enough to predict.

**Worked example:** see `STREAMS.md` — Stream 04 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 05 — Narrative Understanding

**Purpose:** How this business tells its story — the deliberate communication choices that reveal what leadership wants you to think versus what the numbers actually show. The gap between framing and reality.

**What it covers:**
- What the document leads with and what that choice signals
- Which metric becomes the narrative anchor and when it shifts
- How confidence language changes under different performance conditions
- What topics disappear from the main document as they deteriorate
- Specific words that recur with specific meanings
- How the framing has drifted over time and what triggered the drift

**What it must never do:** State what actually happened — that belongs in Stream 02. Only the communication choices and what they reveal about what the team wants the reader to conclude.

**The test:** A reader who had never opened the document could predict the narrative structure before reading it. And when the structure deviates, they notice immediately.

**Worked example:** see `STREAMS.md` — Stream 05 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

### Stream 06 — Forecast and Plan Behavior

**Purpose:** How this business plans, forecasts, and revises — the systematic patterns in how it sets expectations and updates them. Not whether forecasts are accurate this period — whether the forecasting behavior is predictable and what that predicts.

**What it covers:**
- Whether Plan is set aggressively, conservatively, or realistically
- How forecast moves through the year — timing, direction, magnitude of revisions
- Systematic bias by period or condition
- How the business explains forecast changes — the attribution pattern for revisions
- Whether risk and upside language materializes or is consistently wrong

**What it must never do:** State actual forecast vs actual values as beliefs — those belong in Stream 00. Only the behavioral pattern of how forecasting is done and what that pattern reveals.

**The test:** A reader of this belief can predict, before the new forecast is released, approximately what it will say and in which direction it will be revised.

**Worked example:** see `STREAMS.md` — Stream 06 carries the full worked example — five narrative fields plus the Provenance record. Worked examples live there and only there, so the spec and the reference cannot drift apart.

---

## 04 — The Lifecycle

### Step −1 — Entity Foundation (Before Any Stream)

Before any belief stream is created, the entity foundation must exist. The foundation is built once per entity through a short setup interview (Prompt −1) and stored at `entities/{entity_id}/foundation.md`.

The foundation captures three things: entity identity (name, organizational scope, what kind of entity it is), document types that will be read (format, cadence, who produces them), and the angles or streams to be tracked.

**What the foundation does NOT pre-specify:** The business model, operating chain, causal relationships between metrics, normal ranges, narration patterns, and what matters vs. noise. These are discovered by reading documents — they are outputs of the belief streams, not inputs to them.

On the first 1–3 documents, Stream 02 (Business Dynamics) operates in model-discovery mode: its primary job is to extract explicit relationship claims from documents and initialize them as Candidate beliefs. Those accumulated beliefs become the discovered business model. Stream 00 (Factual Understanding) builds the metric definition baseline. Stream 05 (Narrative Understanding) begins mapping communication patterns. Stream 01 (Business Model Understanding) starts forming interpretations of the economic engine. By document 3–4, the belief memory holds a preliminary model of the business — built from what the documents said, not from what the user specified.

The foundation is updated — not rewritten — as the streams accumulate understanding, and only through a defined **Foundation Review** (see `lifecycle/ingestion-pipeline.md`, Step 7.5), never by silent edit. Each atomic foundation claim carries a stable claim ID that belief Provenance records reference directly. The review triggers on either of two independent paths: a belief reaches Confirmed or Established while adding precision to, narrowing, or contradicting the claim it depends on; or a document explicitly states that a claim's definition, calculation, or scope changed — a **Redefinition Signal** (extracted at `06-fact-extractor.md`), which fires immediately regardless of any belief's maturity, because a stated redefinition needs no accumulated evidence to be taken seriously. Either way, the user resolves it as Adopt (the foundation claim is revised, logged in the Foundation Revision Log, and every other belief citing that claim ID is flagged `[FOUNDATION_CHANGED]` for re-grounding), Hold (the original claim stands), or Defer (not enough evidence yet). The understanding flows from reading to foundation, not the other way around — but that flow is now an auditable, triggered process rather than an implied one.

The discriminating test for whether something belongs in the foundation or in a stream is not whether it recurs — a real belief recurs too. It is what kind of thing could ever change it: if new evidence of the entity performing differently could argue against it, it belongs to a stream as a belief; if only a stated redefinition could change it, it belongs in the foundation as a claim. "Gross margin has stayed above 40% all year" is a belief — a future document showing 35% would mean the business performed differently, not that the definition moved. "Gross margin is calculated after fulfillment cost but before marketing spend" is a foundation claim — it can only change if the entity redefines the calculation.

Every belief stream for the entity inherits the foundation as its prior context. The foundation keeps the streams aligned to the same entity definition, even as each stream builds its own understanding independently.

---

### Three Layers of Storage

| Layer | What It Is | Characteristics |
|-------|-----------|-----------------|
| **Entity Foundation** | Business understanding for the entity | One `foundation.md` per entity. Built before any stream. Referenced by every blueprint for that entity. |
| **L1 — Belief Memory** | The living belief file for one stream | One `belief.md` per stream. Numbered beliefs, surgically updated. Loaded into context at session start. Snapshotted to `belief_versions/{doc_id}_belief.md` after every document — the changelog records diffs, the snapshots preserve states. |
| **L2 — Fact Logs** | Per-document extracted signals — the permanent, addressable memory layer | One fact log per document per stream. Written once, never discarded. Referenced by doc_id from every belief's Provenance record — the pointer target for Confirming documents, Blind passes, and Contradiction searches. |
| **L3 — Raw Archive** | Original document content | Immutable. Written once. Never reprocessed. Source of truth for evidence retrieval. |
| **Changelog** | Append-only audit trail | Every document: which beliefs changed, what action, why, what to test next. |

### Ingestion Pipeline — When a Document Arrives

```
DOCUMENT ARRIVES (any format)
          │
          ▼
┌─────────────────────────┐
│  intake.py              │  route by format → transcribe → chunk
│  writes L3 (immutable)  │  pptx / pdf / docx / audio / md
└─────────────────────────┘
          │
          ▼  RAW UNITS → L3 (once only, never rerun)
          │
          ▼
┌──────────────────────────────────────────┐
│  fact_extractor.py                        │
│  system: compiled fact_extractor_prompt   │
│  input:  L3 units + topics_touched        │
│  output: L2 fact log (per-stream)         │
│  opens with STRUCTURE OBSERVED block      │
│  captures signals at belief-claim level   │
│  surfaces distinct patterns separately    │
└──────────────────────────────────────────┘
          │
          ▼  STRUCTURE OBSERVED vs Structural Map
          │  (Step 6.5 — drift resolves:
          │   Recalibrate / Signal / Defer)
          │
          ▼  FACT LOG → belief engine
          │
          ▼
┌──────────────────────────────────────────┐
│  belief_engine.py                         │
│  system: compiled belief_reasoning_prompt │
│  input:  existing belief.md (or NULL)     │
│          + fact log                       │
│  output: belief.md (evolved)              │
│          + belief_changelog.md (appended) │
│  volume check: ≥ 8 active beliefs         │
└──────────────────────────────────────────┘
```

---

## 05 — The Prompt Architecture

Three phases. Entity foundation runs once per entity. Stream setup runs once per stream. Document ingestion runs for every document. Belief activation runs on demand — whenever the belief memory is used to answer a question or prepare an analysis.

### Phase 0 — Entity Foundation (runs once per entity)

| Prompt | What It Does |
|--------|-------------|
| **Prompt −1 — Entity Foundation** | Short setup interview: entity name and identity, document types and cadence, who produces the documents, and which streams to track. Produces `entities/{entity_id}/foundation.md`. Does NOT ask about the business model, operating chain, or causal relationships — those are discovered from documents. |

### Phase 1 — Stream Setup (runs once per belief stream)

| Prompt | What It Does |
|--------|-------------|
| **Prompt 00 — Document Profile** | Interview agent. Discovers document types, cadence, chosen angle, and what each document type can and cannot carry. Produces a structured Document Profile. |
| **Prompt 01 — Strategic Blueprint** | Reads the entity foundation and the Document Profile together. Produces the master configuration document: stream identity, signal matrix, belief definition, and candidate belief seed set (8–15 hypotheses). For Stream 02, the seed set includes relationship hypotheses — not pre-specified relationships, but prompts for what to look for in the first document. |
| **Prompt 03 — Belief Reasoning Compiler** | Reads the blueprint and compiles a self-contained runtime system prompt for the belief engine. Encodes the candidate seed set, claim-heading rule, entry format (five narrative fields plus Provenance), promotion gating (blind pass, contradiction search), volume check, no-renumber rule, relationship belief initialization rules, and all evolution actions. |
| **Prompt 06 — Fact Extraction Compiler** | Reads the blueprint and compiles the runtime system prompt for the fact extractor. Places RELATIONSHIP CLAIM extraction as the top priority signal type. Mandates granularity to support 8–15 Candidate beliefs on the first document. One compiled extractor per document type. |

### Phase 2 — Document Ingestion (runs for every document)

| Component | What It Does |
|-----------|-------------|
| **intake.py** | Routes by format, transcribes, and splits into meaningful units. Writes immutable raw transcript to L3. |
| **fact_extractor.py** | Reads L3 units. Opens the fact log with a STRUCTURE OBSERVED block — the skeleton walked through, with every deviation from the profile's Structural Map reported (drift resolves at Step 6.5: Recalibrate / Signal / Defer). First pass: scan for RELATIONSHIP CLAIMS — explicit statements connecting one metric to another. Second pass: extract individual metric signals, attribution statements, structural observations. Writes fact log to L2. Does not interpret — only captures. |
| **belief_engine.py** | Reads the fact log and the existing belief memory. Relationship claims from the fact log initialize Stream 02 Candidate beliefs on first document. Numbered beliefs, claim-as-heading, five narrative fields plus Provenance. Promotion gated by blind pass and contradiction search. Surgical updates to `belief.md`. Volume check (≥8 beliefs). Appends to `belief_changelog.md`. |

### Phase 3 — Belief Activation (runs on demand)

| Prompt | What It Does |
|--------|-------------|
| **Prompt 07 — Belief Activation** | Reads the current belief memory and produces a specific output for a specific use case: pre-read briefing (what to expect from the next document), analytical Q&A (answers a specific question using the belief memory), or meeting prep (what to push on, what to watch for, what can be skipped). This is how the belief memory is used, not just built. |

The cascade principle: quality injected at the blueprint propagates forward without additional configuration. The belief engine at runtime receives only its compiled prompt, the existing `belief.md`, and the fact log. It never receives the foundation, the blueprint, or the raw document — everything it needs is encoded inside the compiled prompt.

The understanding flows from documents upward: documents → relationship claims → Stream 02 beliefs → discovered business model. Not the other way around.

See [`lifecycle/ingestion-pipeline.md`](lifecycle/ingestion-pipeline.md) for the full step-by-step pipeline and runtime contract.

---

## 06 — Why This Matters

### The Four Use Cases

**01 — Pre-reading a document**
Before reading the next document, an analyst loads the belief memory into Prompt 07 and gets a briefing: here is what this document is expected to show, here is what normal looks like for each area it will cover, and here is what would constitute a signal worth investigating — deviation from a held belief. They walk in with priors, not cold.

**02 — Analytical Q&A**
An analyst asks a specific question: "Is the Q1 spend concentration a problem?" Prompt 07 reads the belief memory and answers from it: "Belief #5 says no — this business runs a deliberate spend-to-acquisition mechanic, confirmed in 6 consecutive cycles. Q1 concentration is the thesis executing. The question to watch is whether Q2 new customer volume lands on the 6–8 week timeline, not whether Q1 spend was elevated." The answer is not a summary of the current document. It is calibrated judgment from accumulated evidence.

**03 — Anomaly detection**
The belief sets the normal. When a new document arrives, the question is not "what does this document say?" but "what does this document do differently from what was expected?" Without a precise baseline, anomalies are invisible. With a belief, they surface immediately — not because a rule was triggered, but because the expected state is known and the deviation from it is specific.

**04 — Institutional memory transfer**
A new analyst or a new model reads the belief memory and gets the accumulated business understanding immediately. For this to work, the beliefs must be specific enough to be actionable — not just "the business is seasonal" but specific enough that the reader knows exactly what to look for, what normal is, and what its absence would mean. The belief memory is the knowledge asset. It transfers when models change, when analysts rotate, when teams rebuild.

---

### Three Things Belief Enables That Nothing Else Does

**01 — Contextual reasoning over time**
Every agent today is context-blind at session start. Belief gives agents a belief memory to reason from — not just a document to search through. Queries become calibrated to the business.

**02 — Belief-grounded evaluation**
Current evals check output format and SQL accuracy. Belief enables a new kind of eval — does this answer reflect what is actually true about this business? You can check agent outputs against the belief model.

**03 — Portable business understanding**
When you upgrade a model or rebuild a system the understanding currently lives nowhere. With Belief the belief memory is portable. A new model inherits the business understanding immediately. The investment compounds.

### The Business Case

**Saves repetitive thinking, not just repetitive doing.**
Skills removed the doing once. Beliefs remove the re-thinking — remember, decide, reconcile, frame — every time after. That is what compounds and what actually drives adoption.

**A durable asset, not a rented one.**
The model is rented and commoditized. The accumulated beliefs are owned and specific to this business. Investment in understanding does not depreciate when the model is swapped.

**The first step of interpretation.**
Running tasks inside a business is not the same as interpreting a business. Beliefs are the first step of interpretation — they make the system's outputs reflect how the business actually works, not just what was in the prompt.

### The Acceptance Criterion

Give Belief 10 months of business review decks. Read the resulting belief memory. If a senior analyst reads it and identifies two or three beliefs they agree with that they would not have articulated explicitly — beliefs that feel true, that reflect how the business actually behaves — the system is working.

Not accuracy on a benchmark. Not a perplexity score. An analyst saying: *yes, that is what I know about this business.*

---

## 07 — Scope Boundaries

Every step in the pipeline has explicit prohibitions. These are not edge-case warnings — they are the core integrity rules that prevent the system from manufacturing beliefs it has not earned.

### What the Entity Foundation Agent (Prompt −1) Must Never Do

- Create beliefs. The foundation is the prior that beliefs are grounded in — it is not a belief and carries no confidence or direction.
- Describe documents. The foundation is about how the business works, not about how its documents are written. Document format belongs in the document profile and blueprint.
- Invent content. Only record what the user told you — or, in corpus grounding, what recurred identically across the fact logs. If information is missing, say so explicitly and note what is unknown.
- Produce generic content. Every sentence must be specific enough that any reader immediately understands what this business cares about most — not what any business in its industry cares about.
- Revise a claim silently. Every change to a foundation claim goes through Foundation Review with a Revision Log entry — and the Adopt/Hold/Defer decision belongs to the user, never to the agent alone.
- Reassign a claim ID. Once minted, a claim ID means one thing forever; a claim that needs to split gets new IDs and the old one is retired in the log.
- Promote an interview answer to corpus-grounded. A claim's source label (interview / corpus / interview+corpus) reflects where the evidence actually came from — an interview claim stays labeled a hypothesis until fact logs corroborate it.
- Wait for belief maturity before reviewing a Redefinition Signal. A document stating outright that a definition changed triggers Foundation Review immediately — treating it as ordinary belief evidence that must first accumulate is exactly the silent-drift failure this path exists to close.

### What the Document Profile (Prompt 00) Must Never Do

- Create beliefs. The interview captures intent; the Structural Read captures architecture. Neither produces interpretation.
- Re-interview about the business. The entity foundation already exists and captures business model, metrics, and behavioral patterns. Prompt 00 focuses on documents and angle only.
- Ask the user to describe document structure. Users know the business, not their documents' anatomy — structure comes from reading the sample, never from the interview.
- Skip the Structural Read when a sample exists. A profile whose CAN/CANNOT sections were guessed from a document-type label is confident-sounding fiction, and every compiled prompt downstream inherits the fiction.
- Let the stream's angle shape the x-ray. The structural map is stream-blind — it must come out identical no matter which stream requested it, like an x-ray that doesn't change depending on which doctor ordered it. Stream-awareness enters only in the scouting sections that follow.
- Put metric values in the x-ray, even to prove a composition breaks. Structural counts ("two of five lines don't reconcile") are structure; dollar figures are facts, and facts in the profile invite the one-document-became-a-belief failure.
- Write maturity-gap filler ("cannot confirm from one document") — true of every document ever profiled; it drowns the real, document-specific gaps.
- Smooth an inconsistency into an average. "Described once as firm policy, once as a temporary exception" is the signal; averaging it destroys it.
- Interpret the story. It maps how the story is communicated, stitched together, and connected — never what the story means, whether the period was good, or what caused what.
- Claim recurrence from one sample. One document shows its own architecture; patterns across documents are earned at ingestion.
- Decide what signals matter. That is the blueprint's job.
- Invent document characteristics — neither ones the user didn't state nor ones the sample doesn't show. Every Structural Map line must be traceable to the sample.

### What the Strategic Blueprint (Prompt 01) Must Never Do

- Create beliefs. The blueprint is configuration, not extraction.
- State what beliefs will exist. It defines what beliefs CAN exist if signals recur — the difference matters.
- Invent entity vocabulary. If the user did not provide it and the documents did not contain it, it is not in the blueprint.
- Leave any section generic or templated. Every section must be answered for this entity.

### What the Fact Extractor Must Never Do

- Interpret signals. Capturing is not interpreting. The fact extractor surfaces what the document contains; the belief engine decides what it means.
- Summarize. A summary is not a fact log. The belief engine needs raw signals.
- Invent signals the document does not contain. "No signal in this window" is a valid and useful output.
- Extract signals the blueprint's signal matrix says the document type cannot carry.
- Create or update beliefs. It reads documents; it does not reason about them.
- Silently adapt to a changed document structure. Every fact log opens with a STRUCTURE OBSERVED block; deviations from the profile's Structural Map are reported there, and resolved visibly at the Structural Drift Check (Recalibrate / Signal / Defer) — never absorbed. A document changing shape is sometimes the story, and the extractor is not the one who decides which.
- Bury a redefinition inside a number-based signal. A document stating that a metric's definition, calculation, or scope changed is captured as its own REDEFINITION SIGNAL, ranked ahead of relationship claims, and routed to Foundation Review directly — not folded into an ordinary metric reading as a footnote.

### What the Belief Engine Must Never Do

- Receive the raw document at runtime. It reads only the compiled belief reasoning prompt, the existing `belief.md`, and the fact log.
- Receive the blueprint at runtime. Everything it needs from the blueprint is already encoded in the compiled prompt.
- Invent evidence not present in the fact log. If the fact log does not contain it, the belief engine does not hold it.
- Treat a REDEFINITION SIGNAL as belief evidence. It never enters belief classification or the Observation tier — it routes straight to Foundation Review.
- Write a belief at higher than Candidate stage from a single document. A first-document entry is Candidate only — explicitly marked as pending confirmation.
- Lower confidence precipitously on a single contradicting signal. One document showing tension does not revise an Established belief.
- Write beliefs that fail the quality test: non-falsifiable, entity-generic, single-period, template artifacts, unsupported causality, not grounded in the foundation.
- Use category labels as headings. The heading of every belief entry is the claim itself — a complete, specific, falsifiable sentence. Not a topic name.
- Renumber beliefs. Once a belief is assigned #N, that number is permanent. Retired beliefs keep their number marked RETIRED.
- Let active belief count fall below 8 without auditing for umbrella beliefs and splitting them.
- Match incoming learnings to beliefs by title text. Matching is by underlying mechanical claim — real language varies period to period, and exact-wording matching fractures one recurring belief into fragments that never mature.
- Retire on fewer than 3 consecutive contradicting comparable documents (configurable). One anomalous period is common; a single contradiction produces TENSION with the Statement rewritten to hold the tension honestly and name what would resolve it — and a resolved tension often yields a narrower, more precise belief than the original.
- Keep a heading that secretly contains two falsifiable claims. The split test: if removing one sentence from the heading would change what falsifies the claim, it is two beliefs wearing one title — split it.
- Confuse RETIRE with CONTRADICT (perspective shift). RETIRE means the pattern ended — the behavior is no longer occurring. CONTRADICT with a perspective shift means the interpretive lens was wrong — the behavior was occurring but it meant something different than previously understood. When multiple consecutive TENSION signals accumulate, the engine must ask: did the pattern end (RETIRE), or did we misread what the pattern was (CONTRADICT + restatement)?

### The Silence Default

Most documents produce no update. The gate is the mechanism. Rarity of genuine updates is what keeps confidence meaningful. A belief system that updates on everything is a summarizer.

---

## 09 — Concept Grounding

This is not a new architecture. It is a named implementation of an established idea.

- In **agent theory**, this is a *belief* in the BDI (Belief-Desire-Intention) sense — something the agent treats as true while acting.
- In **enterprise AI practice**, the same idea appears under different names: semantic memory, business rules engine, semantic layer, ontology, context layer.

Same underlying concept, different names across fields. Naming it honestly avoids overclaiming and makes it easier to reason about where it fits alongside tools teams already use.

---

## 10 — Open Design Questions

These are unresolved architectural decisions. They are documented here to prevent them from being re-litigated from scratch each time the system is extended.

**01 — Belief entry field structure** *(resolved in v4)*
The belief entry now uses five narrative fields — Statement, Why it matters, Evolution trail, Normal baseline, Falsification test — plus the structured Provenance record. The old concern about a separate "pattern fingerprint" field is resolved — the Evolution trail carries the concrete per-document evidence (specific language, structural positions, behavioral markers) as a first-person narrative of how the pattern developed, the Falsification test carries what would break it, and the Provenance record carries the audit data (confirming documents, blind passes, contradiction searches) so the narrative never has to double as the evidence log.

**02 — Anomaly detection as a first-class output**
Should the pipeline produce an explicit anomaly report when a new document breaks an established pattern? Currently the changelog records that a belief changed but not why it changed or what the anomaly was. A dedicated anomaly output would be more actionable for the pre-reading use case.

**03 — Cross-document pattern synthesis**
The pipeline processes one document at a time. Some patterns only emerge across many documents — seasonal behavior, systematic forecast bias, consistent framing shifts. Should there be a periodic synthesis step that looks across all fact logs simultaneously rather than evolving beliefs one document at a time?

**04 — Explicit durability tiers**
Should the Provisional / Confirmed / Established stages from the durability ladder be stored as explicit fields in the belief entry, or is the document count implicit in the evidence trail sufficient? Explicit tiers make the stage queryable; implicit tiers keep the format simpler.

**05 — Statement diff in changelog**
The changelog currently records that a statement changed, not what it said before vs after. Full statement history would enable drift analysis — understanding how the interpretation of a business evolved over time as more documents were read. Not yet implemented.

**06 — document_mechanics.json wiring**
The system can maintain a knowledge base of document-type structure by sector (`document_mechanics.json`) — what sections typically appear, in what order, what each section reliably carries. This would allow the interview agent (Prompt 00) and the blueprint compiler (Prompt 01) to pre-populate signal matrix defaults for common document types rather than deriving them from scratch each time. Open question: at what point in the setup flow does this knowledge base get consulted, and how does it interact with user-provided document samples that may deviate from sector norms? Not yet wired into the questioning session.
