# Belief Memory Schema

The belief memory (L1) is the living belief memory for one belief stream. It is the file an agent loads at session start. It is surgically updated — never rewritten from scratch.

## File Structure

One belief memory file per active belief stream. Each stream lives under its own directory alongside its raw archive and fact logs. Every stream for an entity reads the entity's `foundation.md` as its prior.

```
entities/{entity_id}/
└── foundation.md                ← entity-level business understanding (built once, before any stream)

compiled/{stream_id}/
├── document_profile.md
├── strategic_blueprint.md
├── belief_reasoning_prompt.md
└── fact_extractor_prompt.md

streams/{stream_id}/
├── belief.md                    ← the belief memory (L1) — current state, the interpretation tier
├── observations.md              ← the Observation tier — recurring entity-specific regularities that failed the master test
├── belief_versions/
│   └── {doc_id}_belief.md      ← snapshot of belief.md after each document (version history)
├── match_ledger.md              ← append-only log of every evidence-routing decision (which signal → which belief, or why not)
├── belief_changelog.md          ← append-only audit trail
├── L2_factlogs/
│   └── {doc_id}_fact_log.md    ← per-document extracted signals
└── L3_raw/
    └── {doc_id}.json            ← immutable transcription archive
```

Three tiers of memory live here, and the master test decides which tier a recurring regularity lands in — it classifies, it never discards (see `prompts/belief-doctrine.md`, "Three Tiers of Memory"). Foundation facts live in `foundation.md`; interpretations that pass the master test live in `belief.md`; recurring regularities that fail it (reporting conventions, vocabulary habits, structural patterns) live in `observations.md`. Everything entity-specific and recurring is stored somewhere — the tier is set by how much interpretation it carries and how far its evidence has climbed.

---

## Version History

Every time the belief engine finishes a document pass, the resulting `belief.md` is snapshotted to `belief_versions/{doc_id}_belief.md` before the next document is processed. The changelog records the *diffs*; the snapshots preserve the *states* — so anyone can see exactly what the belief memory looked like after document 3 versus after document 7, and trace how a belief evolved rather than only ever seeing the current, final state.

This is the memory principle applied to the beliefs themselves: nothing the system once held is discarded. A belief that was later revised, narrowed, or retired is still readable exactly as it stood at every point along the way — which is what makes a wrong belief diagnosable (where did the reasoning turn?) rather than just gone.

---

## Belief Entry Format

Each belief is one numbered block inside `belief.md`. The heading is the claim itself — a complete, specific sentence. Beliefs are numbered once and never renumbered. Retired beliefs keep their number marked RETIRED.

```markdown
## Belief #N — [The claim stated as a complete, falsifiable sentence.]   [ACTION_TAG]   Status: Candidate | Provisional | Confirmed | Established | Retired

**Statement**: The claim restated precisely and falsifiably, as business judgment grounded in how the business works (per the foundation). One sentence. Present tense. No hedging.

**Why it matters**: How this belief connects to the foundation — why it matters for how the business operates, which thesis metric it touches, what it reveals about business behavior that is not obvious from any single document.

**Evolution trail**: First-person, per-document journey. When it was first seen and in which document. What each subsequent comparable document added, confirmed, narrowed, or challenged. What the current maturity is and how many documents it rests on. Written as accumulating judgment, not a list of facts.

**Normal baseline**: What the next comparable document should show if this belief is holding, expressed in terms of the foundation's normalization model. On the first document: "not yet established — awaiting second comparable document."

**Falsification test**: What a future document must show to prove this wrong, narrow its scope, or retire it. For Candidate stage: "fails to recur in the next comparable document." For mature beliefs: name a specific reversal — a concrete signal that would force revision.

**Provenance**:
- Foundation dependency: [the specific foundation claim ID this belief relies on, e.g. `foundation.business_model` — not a paraphrase]
- Confirming documents: [doc_ids]
- Blind passes: [doc_ids where this pattern was independently re-derived with no visibility into the prior belief — empty until one has run]
- Contradiction searches: [doc_ids checked, and what was found — "searched, none found" counts as a result; an absent line does not]
- Related beliefs: [belief IDs, in this stream or another, sharing the same underlying phenomenon — empty if none identified yet]
- Last checked: [doc_id of the most recent document that produced any action on this belief, including SILENCE]
```

The narrative fields are for humans and for agent-generated explanation. The Provenance record is structured and machine-checkable — it is what lets an agent citing a belief, or a person auditing one, determine trustworthiness without parsing prose. A well-written Evolution trail and an actually-verified belief must not be allowed to look identical.

---

## Observation Entry Format

Observations (`observations.md`) are the lightweight tier — recurring entity-specific regularities that failed the master test but are worth remembering. Two fields, own number sequence, never cited as beliefs.

```markdown
## Observation #N — [The recurring regularity, stated plainly as a convention or habit.]   Status: seen ×[count]

**Pattern**: What recurs, described concretely — a reporting convention, a vocabulary habit, a structural regularity. No interpretation. The moment it starts explaining what the pattern *means*, run the master test and promote it to a belief.

**Seen in**: [doc_ids]. Last seen: [doc_id].
```

An Observation that acquires genuine interpretation is promoted: open a new belief with its own number, mark the Observation `→ promoted to Belief #M`, keep it for history. Promotion is the only path from Observation to belief — nothing becomes a belief by accumulating a count alone.

---

## Durability Ladder

The **Status** field tracks how far a belief has climbed. Don't skip stages — and don't promote a stage without the verification it requires (see the Provenance record above). Verification follows citation weight: recurrence forms a hypothesis, the blind pass earns the first un-hedged tier, the contradiction search earns the top.

| Stage | Documents | Meaning | Verification required to enter | Citable as |
|-------|-----------|---------|--------------------------------|------------|
| **Candidate** | 1 | A signal with the shape of a durable pattern. Every first-document entry is Candidate. | None — nothing to check against yet. | Not citable |
| **Provisional** | 2 | Two comparable documents support the pattern. An honest hypothesis. | Plain recurrence across a second comparable document. | Only as "unverified recurrence" — hedged |
| **Confirmed** | 3 | Three documents, pattern independently re-derived blind. First tier of real trust. | A blind pass independently found the same pattern. Belief-aware-only confirmation does not promote — flag for review. | Without hedging |
| **Established** | 4+ | Four or more; survived an active contradiction search. | Contradiction search reported clean ("searched, none found"). Holds across document types if applicable. Foundation claim still current. | Without hedging |

**Decay walks down the ladder.** A belief untouched by relevant signal keeps descending one rung per silence window (default 4 consecutive silent comparable documents): Established → Confirmed → Provisional. At the Provisional floor it is marked **STALE** rather than dropping to Candidate — its evidence still exists, it is untested, not unfounded. Tag each downgrade `[DECAY]` — distinct from `[SILENCE]`, which notes one document's silence without changing Status. If a STALE belief's pattern resurfaces, it re-enters verification rather than coasting on a status it earned long ago.

A Candidate entry is subject to confirmation by the next comparable document. An Established belief requires sustained contradiction — never one anomalous document — before revision or retirement (default: 3 consecutive contradicting comparable documents to retire).

---

## Match Ledger

`match_ledger.md` is append-only. Every time the engine routes a signal — to an existing belief, a new belief, a new observation, or deliberately *not* to a belief it superficially resembles — it logs one line. This is what makes evidence-routing auditable; without it, the decision that a signal "belongs" to Belief #5 is the one unfalsifiable step in a falsifiability-first system.

```markdown
## [doc_id] — match decisions

[doc_id] SIGNAL "spend ratio elevated in Q1, new-customer volume rose in Q2"
  → MATCHED Belief #5
  Basis: same underlying mechanic (Q1 spend → Q2 volume with a lag), not just shared vocabulary.

[doc_id] SIGNAL "management used the word 'disciplined' about cost three times"
  → NEW_OBSERVATION #12
  Basis: recurring vocabulary habit, no interpretation yet — fails the master test.

[doc_id] SIGNAL "margin rose while volume fell"
  → NO_MATCH — considered Belief #5, rejected
  Basis: superficially about the same metrics, but asserts a different (opposite-direction) mechanic. Opened Belief #14 instead.
```

Match by the **underlying mechanical claim, not the heading text.** The ledger answers two questions no silent routing can: "which beliefs have not had a clean match in N documents?" (staleness) and "did an anomalous or injected document warp a routing decision?" (integrity).

---

## Volume Check

A populated belief stream must hold at minimum 8 active beliefs. Fewer than 8 indicates over-collapse — beliefs that are umbrella statements covering multiple distinct patterns. The belief engine must self-audit when the count falls below 8 and split any umbrella beliefs into their constituent claims.

On the first document, the belief engine must initialize between 8 and 15 specific Candidate beliefs. Not 3–4 shallow umbrellas. Specific, falsifiable claims at the level of observable business behavior.

---

## Examples

### Stream 05 example — Narrative Understanding, document-level patterns

```markdown
## Belief #1 — The business leads every quarterly review with volume growth before any cost discussion.   [DEEPEN]   Status: Confirmed

**Statement**: Every quarterly review opens with volume performance against prior year before addressing any cost or margin line — establishing volume as the primary narrative frame through which all other performance is interpreted.

**Why it matters**: The foundation identifies volume growth as the primary thesis metric. Leading with volume signals that management reads its own performance through this lens first — cost and margin are downstream of the volume story, not parallel to it. This shapes how to interpret any period where volume leads strong but margins miss.

**Evolution trail**: First seen in Q4 2025 review — volume metrics occupied slides 2–3, with the first cost discussion not appearing until slide 7. I treated this as a possible structure, not yet a pattern. Q1 2026 repeated the same ordering: two volume slides, then pipeline, then cost efficiency. The structure held even though volume growth had slowed. By Q2 2026, with three consecutive reviews following this sequence, I treat this as how this business reads itself. The volume-first ordering is not driven by which metric performed better — it held in Q1 when volume was weak.

**Normal baseline**: Next comparable document should open with volume performance on slides 2–4, with cost/margin content not appearing until at least slide 6. If the ordering inverts, note it as a signal worth watching.

**Falsification test**: Two consecutive quarterly reviews that lead with margin or cost performance before volume would break this belief. A single inversion is worth noting as TENSION but not yet sufficient to revise.

**Provenance**:
- Foundation dependency: `foundation.metrics.volume_growth` — volume growth is the primary thesis metric
- Confirming documents: Q4 2025, Q1 2026, Q2 2026
- Blind passes: Q2 2026 (independently re-derived the same slide-ordering pattern with no visibility into the prior belief, before promotion to Confirmed)
- Contradiction searches: Q2 2026 (searched, none found — checked specifically whether the ordering inverted in the one period where volume growth had slowed; it held)
- Related beliefs: none identified yet
- Last checked: Q2 2026
```

---

### Stream 02 example — Business Dynamics, performance track record component

```markdown
## Belief #3 — Revenue guidance has been met or exceeded in 7 of 8 comparable quarters; the one miss was preceded by a distinct language shift in the prior period.   [DEEPEN]   Status: Established

**Statement**: This business delivers against its stated revenue guidance in 7 of 8 comparable quarters, with a median beat of 1.4%. The single miss (Q3 2024) was preceded by the prior quarter's document shifting from "on track" language to hedged phrasing ("remain focused on achieving our targets") — a language change not seen in any quarter that produced a beat.

**Why it matters**: The foundation identifies revenue delivery as the primary commitment metric. A 7-of-8 track record with a consistent median beat of ~1.4% is the baseline expectation going into every document. The language-shift preceding the only miss creates a leading indicator: hedged commitment language is now a falsifiable warning signal, not a stylistic variation.

**Evolution trail**: First seen in Q4 2023 review — revenue beat guidance by 1.2%. I initialized this as a Candidate. Q1 2024 added a second comparable beat (1.8%). Q2 2024 added a third (1.1%), advancing to Confirmed. Q3 2024 produced the first miss (−0.6%); I noted the prior-quarter language shift as a potential signal and held the belief at Confirmed with TENSION on the language indicator. Q4 2024 through Q2 2025 produced three more beats (1.3%, 1.6%, 0.9%), with no hedged language in prior periods. The pattern is now Established: the track record is durable, and the language indicator has been seen once. Seven of eight periods at consistent magnitude.

**Normal baseline**: Next comparable document should show revenue within 0–2.5% above guidance. A beat of more than 3% or a miss of any size is worth flagging against this baseline. If the prior-period document contained hedged commitment language, weight a miss more heavily.

**Falsification test**: Two consecutive guidance misses would break the delivery reliability belief. A pattern where hedged language precedes beats — not misses — would retire the language-as-leading-indicator sub-claim, narrowing the belief to the delivery rate alone.

**Provenance**:
- Foundation dependency: `foundation.metrics.revenue_delivery` — revenue delivery is the primary commitment metric
- Confirming documents: Q4 2023, Q1 2024, Q2 2024, Q3 2024, Q4 2024, Q1 2025, Q2 2025
- Blind passes: Q2 2024 (independently re-derived the same beat pattern with no visibility into the prior belief, before promotion to Confirmed)
- Contradiction searches: Q2 2024 (searched, none found, before promotion to Confirmed); Q3 2024 (searched — found the miss and the preceding language shift, recorded as TENSION rather than a break); Q1 2025 (searched, none found)
- Related beliefs: none identified yet
- Last checked: Q2 2025
```

---

### Stream 02 example — Business Dynamics, relationship belief, initialized from document one, deepened across 6 cycles

```markdown
## Belief #5 — Spend in Q1 drives new customer volume in Q2 with a 6–8 week lag — stated explicitly by management, confirmed in 6 consecutive cycles.   [DEEPEN]   Status: Established

**Statement**: This business runs a deliberate spend-to-acquisition mechanic. The spend ratio against the core volume metric rises in Q1 (typically 28–34%), which drives new customer volume in Q2 within 6–8 weeks. The chain has held in all 6 comparable cycles observed. When the spend ratio falls below 26% in Q1, Q2 new customer volume has underperformed by a median of 4.2 percentage points.

**Why it matters**: The foundation identifies spend and the core volume metric as the two primary thesis metrics. The 6–8 week lag between Q1 spend and Q2 acquisition conversion is the single most predictive mechanic in the business. Understanding where the spend ratio sits in Q1 — relative to the 28–34% normal range — is the earliest leading signal for whether Q2 volume will land on cycle or disappoint.

**Evolution trail**: This relationship belief was initialized on the first document — the first document reviewed included an explicit management statement: "our Q1 marketing investment is designed to drive new customer signups; we typically see conversion into new volume over the following 6–8 weeks." I captured this as a RELATIONSHIP CLAIM and initialized a Candidate belief on that statement alone. The statement was the evidence; I did not wait for the relationship to play out. The first Q1–Q2 cycle confirmed the lag: spend ratio at 31% in Q1, new volume up 8.4% in Q2 within 7 weeks — Provisional. Three confirmed cycles by the third Q1 — Confirmed. The sub-claim about the 26% threshold emerged when the spend ratio fell to 24.8% in a Q1 and Q2 volume grew only 3.1%. A later Q1–Q2 cycle added a sixth cycle. The threshold sub-claim rests on two datapoints — Provisional sub-claim inside an Established primary claim.

**Normal baseline**: Q1 spend ratio in the 28–34% range should produce Q2 new customer volume growth of 6–10% within 6–8 weeks of Q1 close. Any Q1 reading below 26% should lower the Q2 volume expectation by approximately 4 percentage points. Any Q1 reading above 36% (which has not yet occurred) is outside the observed range and requires a new baseline.

**Falsification test**: A cycle where the spend ratio sits within the 28–34% normal range in Q1 but Q2 demand fails to recover within 6–10% would break this belief. A cycle where the spend ratio falls below 26% but Q2 demand still recovers on the normal range would retire the threshold sub-claim. Either outcome would force a fundamental re-examination of the operating chain.

**Provenance**:
- Foundation dependency: `foundation.metrics.spend_and_core_volume` — spend and the core volume metric are the two primary thesis metrics
- Confirming documents: doc_1, doc_2, doc_3, doc_4, doc_5, doc_6
- Blind passes: doc_3 (independently re-derived the same Q1/Q2 lag with no visibility into the Provisional belief before promotion to Confirmed)
- Contradiction searches: doc_4 (searched, none found), doc_6 (searched, none found)
- Related beliefs: none identified yet
- Last checked: doc_6
```

---

## Changelog Structure

After every document, `belief_changelog.md` records what changed — one entry per affected belief, appended.

```markdown
## Changelog — {doc_id} — {timestamp}

### Belief #1 — The business leads every quarterly review with volume growth before any cost discussion.
<!-- Stream 05 — Narrative Understanding -->
**Action:** [DEEPEN]
**Previous statement:** (unchanged)
**New statement:** (unchanged)
**Reason:** Third consecutive document confirms volume-first ordering. Evolution trail extended with Q2 2026 observation that ordering held even when volume growth decelerated.
**Maturity impact:** Provisional → Confirmed
**What next document should test:** Whether volume-first ordering holds in a period where volume is negative or flat.

### Belief #4 — Management attributes margin misses exclusively to external cost inflation.
<!-- Stream 03 — Causal Understanding -->
**Action:** [TENSION]
**Previous statement:** Management attributes margin misses exclusively to external cost inflation.
**New statement:** (unchanged — held under tension)
**Reason:** Q2 document included one reference to internal procurement inefficiency contributing to cost pressure — first internal attribution observed. Single document; not yet sufficient to revise.
**Maturity impact:** None — held at Confirmed pending next document
**What next document should test:** Whether internal attribution recurs or Q2 reference was isolated.

### Belief #9 — This entity treats headcount as the primary lever under margin pressure, cutting it before any other cost line.
<!-- Stream 04 — Business Memory -->
**Action:** [DECAY]
**Previous statement:** (unchanged)
**New statement:** (unchanged — Status downgraded only)
**Reason:** Fourth consecutive comparable document with no pressure episode to test this belief against — the business has not been under margin pressure since the belief reached Established. Silence across four documents, not contradiction.
**Maturity impact:** Established → Confirmed
**What next document should test:** Whether the pattern reconfirms at the next pressure episode. A confirming episode restores Established; a contradicting one triggers [CONTRADICT] instead.
```

### Changelog Action Tags

| Tag | Meaning |
|-----|---------|
| `[NEW_BELIEF]` | A belief entered for the first time (Status: Candidate) |
| `[DEEPEN]` | Belief held; evolution trail extended with new confirming evidence |
| `[NARROW]` | Belief scope reduced — the claim now applies more specifically than before |
| `[CONTRADICT]` | Strong contradicting evidence; belief statement revised under a new interpretation |
| `[TENSION]` | A contradicting signal appeared but is not yet strong enough to revise the belief. Multiple consecutive TENSION entries signal a revision may be approaching. |
| `[SILENCE]` | The document covered this belief area but showed no signal — noted but no update |
| `[RETIRE]` | Belief archived — the pattern ended. The number is kept; the belief marked RETIRED. |
| `[MERGE_BELIEFS]` | Two beliefs collapsed into one more precise claim |
| `[SPLIT_BELIEF]` | One belief divided into two distinct, separately falsifiable claims |
| `[NO CHANGE]` | Document processed; no update warranted for this belief |

The changelog is append-only. An absent changelog entry for a document means the pipeline did not complete for that document.

---

## Update Arithmetic

| Action | Confidence Change |
|--------|------------------|
| Confirm (DEEPEN) | +0.08 |
| Contradict (TENSION) | −0.15 |
| New Prior (NEW_BELIEF) | initialized at 0.20 |
| Decay (90+ days unseen) | −0.05 per cycle |

**Bounds:** Floor 0.05 · Cap 0.95 (0.90 for causal beliefs)
**Archive threshold:** Below 0.10 → moved to archive; not deleted

---

## What the Belief Engine Reads at Runtime

The belief engine receives exactly three inputs at runtime. It receives nothing else.

1. **The compiled belief reasoning prompt** — `compiled/{stream_id}/belief_reasoning_prompt.md` — the self-contained system prompt encoding the doctrine, angle definition, candidate belief seed set, evolution rules, and worked examples for this stream. Produced once at setup from the Strategic Blueprint. Never changes unless the stream is reconfigured.
2. **The existing belief memory** — `streams/{stream_id}/belief.md` — the current state of all numbered beliefs in this stream. May be NULL for the first document.
3. **The fact log** — `streams/{stream_id}/L2_factlogs/{doc_id}_fact_log.md` — signals extracted from the current document, organized by belief area.

The belief engine never receives the raw document, the blueprint, or any other context. Everything it needs is inside the compiled prompt and the fact log. This is the contract that makes the system reproducible and auditable.

---

## Belief Memory Bounds

- **Min active beliefs per stream:** 8 (enforced by volume check)
- **Max active beliefs per stream:** ~20 (configurable)
- **Decay trigger:** 90 days since last confirming document (configurable)
- **Archive, not delete:** Contradicted and decayed beliefs are archived, not erased. History is preserved.
- **No renumbering:** Once a belief is assigned #N, that number is permanent. Retired beliefs keep their number marked RETIRED.
