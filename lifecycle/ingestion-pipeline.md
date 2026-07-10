# Ingestion Pipeline

How a belief stream is set up and how documents flow through it to produce belief updates.

---

## The Core Principle

Durable judgment is never created directly from a raw document. It is built only after profiling, blueprinting, extraction, and recurrence.

A single document can never manufacture a belief. Beliefs are earned across comparable documents over time.

---

## Two Phases

**Phase 1 — Stream Setup** runs once per belief stream, before any documents are processed.
**Phase 2 — Document Ingestion** runs every time a new document arrives.

---

## Phase 1 — Stream Setup (Steps −1 through 4)

### Step −1 — Entity Foundation (Prompt −1)

**Who:** LLM, in two passes — a structured interview with the user at setup, and a corpus grounding pass once the first fact logs exist
**Input:** Pass 1: user interview across five areas (business model, thesis-defining metrics, normalization model, narration design, what matters vs. noise). Pass 2: all fact logs produced so far, read together (default trigger: 3 fact logs — `foundation_grounding_min_documents` in config)
**Output:** `entities/{entity_id}/foundation.md`

Produces the institutional business understanding that every belief stream for this entity reads as its prior. Not a document summary. Not a belief. The mental model a strong analyst carries before opening any document — what kind of business this is, what its profitability thesis rests on, which metrics are thesis-defining, what normal looks like, and how this entity narrates its own performance.

**Every claim is labeled with its source.** Interview claims are hypotheses (`source: interview`) — the user's stated understanding, useful but unverified. The corpus grounding pass reads the first N fact logs together and extracts what recurred *identically* across all of them — the definitional scaffold: metric definitions, benchmark sequences, decomposition structure. Those claims are `source: corpus`. Interview claims the corpus corroborates become `interview+corpus`; claims the corpus contradicts trigger an immediate Foundation Review; claims the corpus is silent on remain labeled hypotheses. The test separating a foundation claim from a belief is not recurrence — it's what could ever change it: could new evidence of different performance argue against it → belief; could only a stated redefinition change it → foundation (see `-1-generate-foundation.md`).

Without the foundation, a belief stream produces document-level facts. With it, it produces grounded business judgment.

The foundation is built once per entity. All streams for that entity inherit it. The foundation is a living document — but it is only ever refined through the corpus grounding pass and the Foundation Review process (Step 7.5 below), never by silent edit. Every atomic claim in the output carries a stable claim ID (e.g. `foundation.business_model`) that belief Provenance records reference directly.

---

### Step 0 — Stream Setup (user-driven)

**Who:** The user, through a short questioning session
**Scope:** Capture three things: the entity, the requested belief stream (angle), and the document set that will feed it.
**Output:** A stream setup record: entity, belief stream name, document set

The belief stream may be one of the seven standard streams (00 — Factual Understanding, 01 — Business Model Understanding, 02 — Business Dynamics, 03 — Causal Understanding, 04 — Business Memory, 05 — Narrative Understanding, 06 — Forecast and Plan Behavior) or a custom stream (Marketing Efficiency Memory, Forecast Reliability, Operational Risk Memory, Investor Messaging, Margin Quality, Forecast Bias, or any user-defined stream). The user chooses. The documents determine what can be grounded.

This step only captures intent. The system grounds it in Steps 1 and 2. Two rules govern it: the stated scope is a **fence** — it permanently bounds what the system is allowed to learn, and an out-of-scope aside in a future document stays outside the fence by design, not by failure. And scope is *business* scope, never document scope — conflating "what parts of the business I care about" with "what files I'll upload" produces streams that are secretly about file formats. Setup never validates intent against document content (that would tempt it into promises the profile then has to walk back); if the requested angle and the actual documents disagree, Step 1 records the mismatch honestly and the user decides.

---

### Step 1 — Document Profile (Prompt 00)

**Who:** LLM, once at setup — a short interview for what only the user knows, plus a **mandatory structural read** of one sample per document type
**Input:** requested belief stream, the user's answers (scope, document types, cadence, success criteria), one sample document per type, optional user purpose
**Output:** `compiled/{stream_id}/document_profile.md`, containing a **Structural Map** per document type

The division of knowledge: the user knows the business — that's the foundation. The documents are the only reliable witness to their own structure — users cannot recite their deck's anatomy, and asking them produces guesses. So Prompt 00 reads the samples in two parts with a hard boundary between them. **Part 1, the x-ray, is stream-blind**: it maps the document's internal logic as if the profiler had never heard which stream was requested — section inventory in order (verbatim titles), narrative assembly, how the pieces are stitched, how the current period's story connects to the recurring structure, numbers vs. commentary, benchmarks as labeled, composed metrics as name-relationships (with reconciliation tested at every cut and breaks reported precisely — counts allowed, values banned), behavioral patterns in non-metric sections, recurring apparatus, and actively-hunted absences (including cross-granularity ones). The x-ray must be reproducible identically no matter which stream asks, and is shared across streams of the same document family — if it isn't reproducible, stream bias has leaked into what was considered worth noticing. **Part 2, the scouting read, is stream-aware**: given this skeleton, what could this particular lens learn from it?

The boundary: **map the telling, not the tale.** How the story is communicated, stitched, and connected — yes. What the story means — never. No performance judgment, no causal reading, no candidate beliefs, no cross-document pattern claims from a single sample. Does NOT extract signals — signal extraction is Step 6's job, against the compiled extractor prompt.

The CAN/CANNOT capability assessment is derived from the Structural Map, each line citing observed structure — never from type-level intuition. If no sample is available, the Structural Map is marked `UNGROUNDED — pending first document`, the CAN/CANNOT sections are explicitly provisional, and the first document processed at Step 6 must trigger completing the map and revisiting the profile before the compiled prompts are trusted.

The profile answers: what kind of durable beliefs could these documents eventually support if similar signals recur across comparable documents?

---

### Step 2 — Strategic Blueprint (Prompt 01)

**Who:** LLM, once at setup, reading the foundation and profile
**Input:** `entities/{entity_id}/foundation.md`, `document_profile.md`, requested belief stream, optional purpose and history
**Output:** `compiled/{stream_id}/strategic_blueprint.md`

Converts the profile into an answered configuration document, grounded in the foundation. Defines what a belief MEANS for this entity, this stream, these documents, this cadence.

The blueprint has five sections:
- **Section 0** — Foundation reference (how the entity foundation grounds this specific stream — which thesis metrics are relevant, which normalization model applies, what narration patterns are background knowledge)
- **Section 1** — Belief stream identity (entity, scope, exclusions)
- **Section 2** — Document types and signal matrix (what each document CAN and CANNOT carry, numbers policy, template artifact risk, trigger question)
- **Section 3** — Belief definition for this stream (what a belief is here, claim-as-heading rule, entry structure (five narrative fields plus Provenance), durability test for this cadence, strong worked example, weak example, volume check rule — all in entity vocabulary)
- **Section 4** — Candidate belief seed set (8–15 specific candidate claims grounded in foundation knowledge; each is a complete falsifiable sentence about how this entity behaves)

Every section is answered with entity-specific content. No placeholders.

The angle is a hypothesis, not a constraint. If the documents cannot carry the requested stream, the blueprint says so and explains what CAN be extracted instead.

---

### Step 3 — Compile Belief Reasoning Prompt (Prompt 03)

**Who:** LLM compiler, once at setup, reading the blueprint
**Input:** `strategic_blueprint.md`
**Output:** `compiled/{stream_id}/belief_reasoning_prompt.md`

Compiles the blueprint into a self-contained runtime system prompt for the belief engine. At runtime the belief engine sees ONLY this prompt, the existing `belief.md` (or NULL), and the new fact log. So everything it needs must be inside: the belief doctrine, the entity-specific definition, the candidate belief seed set, the claim-heading rule, the entry format (five narrative fields plus Provenance), the numbers policy, the durability ladder with its promotion gating, the volume check, the first-document rule, the subsequent-document rule, the no-renumber rule, contradiction and silence handling, and all evolution actions.

Does NOT re-derive the belief definition from generic rules — reads Blueprint Section 3 directly. **If Blueprint Section 3 is thin or missing for this stream, the compiler names the gap AND sets the prompt's header to `status: blocked` with the reason.** Naming a gap is not a substitute for stopping: a blocked prompt must not silently ship and produce beliefs from an undocumented definition. The compilation gate (Step 6) refuses to run against it. Only a fully-grounded definition compiles to `status: ready`.

---

### Step 4 — Compile Fact Extractor Prompt (Prompt 06)

**Who:** LLM compiler, once at setup, reading the blueprint and compiled belief prompt
**Input:** `strategic_blueprint.md`, `belief_reasoning_prompt.md`, document type context
**Output:** `compiled/{stream_id}/fact_extractor_prompt.md`

Compiles a belief-stream-scoped extraction prompt derived by working backward from what the belief engine needs. The extractor is grounded in the entity foundation — it knows which signals connect to thesis metrics and which are background noise per the foundation's what-matters-vs-noise section.

The extractor captures:
1. Signals that feed belief statements (specific, verbatim, falsifiable)
2. Evolution trail evidence (what was said, where, in what language — not paraphrased)
3. Normalization readings (reference the foundation's normal ranges)
4. Leading indicators for falsification tests

The extractor must surface distinct signals separately to support 8–15 Candidate beliefs on the first document. No collapsing distinct patterns into umbrella summaries.

Different document types in the same stream get different compiled extractor prompts. Each inherits from the same blueprint but has document-type-specific extraction guidance.

Like Step 3, this compile carries a header `status: ready | blocked`. It is `blocked` if the profile's Structural Map for this document type is `UNGROUNDED — pending first document`, or the signal matrix it derives from is provisional — the extractor would be calibrated against a document it has never seen. A blocked extractor prompt does not silently run; Step 6 refuses it (or runs under explicit override, tagging output provisional-pending-recompile).

---

## Phase 2 — Document Ingestion (Steps 5 – 8, including 6.5 and 7.5)

Runs every time a new document arrives.

---

### Step 5 — Document Intake → L3 Units

**Who:** Code (intake.py)
**Input:** Uploaded document (pdf / pptx / docx / txt / audio)
**Output:** `streams/{stream_id}/L3_raw/{doc_id}.json`

Routes by format, transcribes, and splits into meaningful units. Each unit carries:
- `transcription` — full text content of this unit
- `topics_touched` — labels for what this unit covers
- `timestamp` — when processed
- `source_filename` — preserved from upload metadata

**Routing:**

| Document Type | Extraction Method |
|---------------|------------------|
| PPTX / image-heavy PDF | Vision model transcription (slide-by-slide) |
| Scanned PDF | OCR |
| Text PDF / DOCX / MD / TXT | Direct text extraction |
| Audio / video | Audio transcription → text |

The vision/OCR pass runs ONCE per document. The raw extract is stored permanently in L3 (Raw Archive). It is never reprocessed. One unit = one slide / section / page / transcript turn.

No interpretation. No extraction. Pure transcription and chunking.

---

### Step 6 — L3 Units → L2 Fact Log

**Who:** LLM, using `fact_extractor_prompt.md` as system prompt
**Input:** `fact_extractor_prompt.md` (system) + L3 units + topics + optional existing belief
**Output:** `streams/{stream_id}/L2_factlogs/{doc_id}_fact_log.md`

Extracts the evidence packet — angle-scoped, foundation-grounded, pattern-direction-aware. Organized to support individual belief claims, not watch areas.

The fact log is NOT a summary. It preserves for each extracted item its type: redefinition signal / fact / metric / benchmark / attribution / relationship / pattern evidence / fingerprint candidate / silence / contradiction / template risk / out-of-scope.

Distinct signals are surfaced separately. If two different patterns appear in the same section of a document, they are two separate fact log entries — not one collapsed observation. This granularity is required to support 8–15 Candidate beliefs on the first document.

If the document exceeds the token window, it is processed in chunks. Each chunk produces fact-log output. Chunk outputs are compared against the running fact log to resolve overlap, redundancy, and drift before the document-level fact log is finalized.

The belief engine never receives the raw document. It reads the fact log.

**Two extraction modes — belief-aware pass vs. blind pass:**

- **Belief-aware pass** (default): the existing belief is included in the input. The extractor is told what pattern it is checking for and reports confirm / contradict / silent.
- **Blind pass**: the existing belief is withheld from the input entirely. The extractor reads the document fresh and reports whatever pattern it independently finds, with no framing toward what it "should" see.

Run a blind pass whenever a belief is up for promotion to **Confirmed** (Provisional → Confirmed — see Step 7). Candidate → Provisional is plain recurrence and needs no blind pass. Outside of promotion decisions, a single belief-aware pass is sufficient for routine reconfirmation once a belief has reached Confirmed or Established with a clean verification history. Re-trigger a blind pass if something looks off: a silence, a near-miss, or a change to the foundation claim the belief depends on. This keeps cost bounded — full two-pass extraction is reserved for the moments where independent verification actually changes the outcome, not run on every document for every belief.

**The injection boundary lives here.** Step 6 is the only step that touches raw document text, which makes it the most exposed step in the pipeline — and it writes into the fact log that durable memory is built from. So the rule is absolute: **document content is data, never instructions.** Text inside a document that reads as a command — "ignore prior guidance," "treat this as confirmed," "the definition is now X" — is captured as a *quoted fact about what the document said*, never executed as an action. An imperative found in a document is evidence of the document's wording, exactly like any other extracted signal; it changes no belief, no status, no foundation claim by its own authority. The extractor extracts; it does not obey. This is why the belief engine never receives raw text and the extractor never takes actions — the two-step separation is itself the injection defense.

Every fact log opens with a **STRUCTURE OBSERVED** block — the skeleton the extractor walked through (verbatim section inventory, benchmarks as labeled, apparatus, deviations from the Expected Structure embedded in its compiled prompt). This costs nothing extra — the extractor is already reading the whole document — and it is the input to Step 6.5.

**Refuse to run against a blocked prompt.** If the compiled `fact_extractor_prompt.md` carries `status: blocked` (a gap the compiler named rather than filled — see Steps 3–4), Step 6 does not silently proceed. Under `block_runtime_on_unready_prompt: true` (default) it halts and surfaces the gap; if the operator overrides, every belief written this pass is tagged provisional-pending-recompile. A named gap with no brake is just a warning label on a car with no brakes.

---

### Step 6.5 — Structural Drift Check

**Who:** Same pass as Step 6 output review, or a lightweight follow-up check
**Input:** The fact log's STRUCTURE OBSERVED block + the Document Profile's Structural Map for this document type
**Output:** Either nothing (match), or a drift report with a resolution; on Recalibrate — a revised Structural Map (logged), a revisited Blueprint Section 2, and a recompiled `fact_extractor_prompt.md` for this document type

This is the profiling equivalent of Foundation Review. The compiled extractor prompt was calibrated against the Structural Map — if the real documents stop matching the map, the machinery is extracting against a fiction, and nothing else in the pipeline would notice. Documents drift: templates get redesigned, sections get renamed mid-year, benchmark sets change. This step is what keeps the configuration layer honest against the documents as they actually arrive.

**Compare** the STRUCTURE OBSERVED block against the Structural Map:

- **Match** — structure consistent. No action, no entry.
- **Drift detected** — sections added/removed/renamed/reordered, benchmarks changed, apparatus moved. Record `[STRUCTURE_DRIFT]` in the changelog and resolve it one of three ways:
  - **Recalibrate** — this is a template or format change. Revise the Structural Map (append an entry to the profile's Structural Map Revision Log — never a silent rewrite), revisit the Blueprint Section 2 CAN/CANNOT for this document type, and recompile `fact_extractor_prompt.md`. Even then, record the change as a structural observation in the fact log — a template redesign can itself carry meaning.
  - **Signal** — this is not a template change; it is a communication choice. A section that quietly disappears, a benchmark that stops being shown, commentary that moves to the appendix — that is exactly the behavior Stream 05 (Narrative Understanding) exists to track. Keep the Structural Map as-is, and let the deviation flow to the belief engine as a signal (an absence or emphasis observation) rather than being laundered into template noise.
  - **Defer** — seen once, could be a one-off (a special quarter with an extra deep-dive section). No change; watch the next comparable document. Drift that recurs across 2 consecutive documents of the same type (configurable) can no longer be Deferred — it must resolve to Recalibrate or Signal.
- **UNGROUNDED completion** — if the profile's Structural Map was marked `UNGROUNDED — pending first document`, this document's STRUCTURE OBSERVED block becomes the Structural Map (grounding it, logged as such), and the Blueprint Section 2 assessment plus the compiled extractor prompt must be revisited against it before their output is trusted.

**The one rule that governs this step:** drift is never silently absorbed. The extractor reports it, this step resolves it visibly, and the resolution is on the record. "The document changed shape" is information — sometimes about the template, sometimes about the story — and deciding which is a resolution, not a default.

Like Foundation Review, the Recalibrate-vs-Signal decision is surfaced to the user by default (`structural_drift_resolution` in config), because the two readings lead in opposite directions: one updates the machinery, the other feeds the beliefs.

---

### Step 7 — Fact Log + Existing Belief → Evolved belief.md

**Who:** LLM, using `belief_reasoning_prompt.md` as system prompt
**Input:** `belief_reasoning_prompt.md` (system) + `{{EXISTING_DURABLE_BELIEF}}` (belief.md or NULL) + `{{NEW_CHRONOLOGICAL_FACT_LOG}}` (+ blind-pass fact log, when one was run)
**Output:** `streams/{stream_id}/belief.md` (evolved) + a snapshot copy at `streams/{stream_id}/belief_versions/{doc_id}_belief.md` — the version history. The changelog records the diffs; the snapshots preserve the states, so the belief memory as it stood after any document remains readable forever.

**Classify before you route — the master test decides the tier, not admission.** For every recurring entity-specific regularity in the fact log, ask the master test: does this say something no single document says? If yes → it is a belief candidate (below). If no → it is an **Observation** — a reporting convention, vocabulary habit, or structural regularity — written to `observations.md` in the two-field form, cited only as an unverified pattern, never discarded. Nothing useful is thrown away; nothing weak is allowed to impersonate a belief.

**A REDEFINITION SIGNAL never enters this classification at all.** If the fact log carries one (Part 1 of the fact log, ahead of relationship claims — see `06-fact-extractor.md`), it is not weighed as belief evidence or Observation evidence — it routes straight to Step 7.5's Redefinition Signal path, at full priority, regardless of any belief's current maturity.

**Log every routing decision to the match ledger.** Before writing any belief update, decide which existing belief (if any) this signal is evidence for — matching by the **underlying mechanical claim, not the heading text** — and append one line to `match_ledger.md`: MATCHED Belief #N / NEW_BELIEF / NEW_OBSERVATION / NO_MATCH (considered #N, rejected, with the distinguishing basis). This is what makes evidence-routing auditable; a silent match is the one unfalsifiable step in a falsifiability-first system.

**On first document (belief.md is NULL):**
Initialize between 8 and 15 specific Candidate beliefs drawn from the fact log. Beliefs must use the candidate seed set from Blueprint Section 4 as a starting frame, but are grounded in what the first document actually showed. Every entry marked Status: Candidate. Evolution trail says "First seen in [doc_id] — [brief observation]." Normal baseline: "not yet established." Provenance record initialized with the foundation dependency named and all other fields empty — nothing exists yet to check against. Recurring regularities that fail the master test on this first document open `observations.md`. No umbrella beliefs.

**Volume check:** If the active belief count falls below 8, audit for umbrella beliefs that conflate multiple distinct patterns and split them. Record the split in the changelog as [SPLIT_BELIEF].

**On subsequent documents:**
For each existing belief, decide: deepen / narrow / contradict / tension / silence / retire / no change. Update only when the evolution trail, baseline, or falsification test changes. Check contradiction and silence BEFORE deepening.

**Promotion gating — rigor follows citation weight; the gates sit one rung lower than confirmation-by-count:**
- **Candidate → Provisional** requires only plain recurrence across a second comparable document. A Provisional belief is an honest hypothesis — held, watched, and cited only as "unverified recurrence." Forming a hypothesis is cheap by design; no blind pass required.
- **Provisional → Confirmed** requires a blind pass on this document that independently re-derived the same pattern the belief-aware pass reports as confirming. Confirmed is the first tier citable *without* hedging, so this is where the first real verification gate sits. If the blind pass found nothing related, do not promote — hold at Provisional, flag for review; the confirmation may be an echo.
- **Confirmed → Established** requires an active contradiction search on this document, reported explicitly ("searched, none found") rather than assumed from silence, the belief holding across document types where applicable, and its named foundation claim unchanged since creation.
- **Decay walks down the ladder:** each time `decay_after_silent_documents` (default 4) consecutive comparable documents pass with no relevant signal, the belief drops one rung — Established → Confirmed → Provisional. At the Provisional floor it is marked **STALE** (evidence intact, untested) rather than dropping to Candidate. Tag each downgrade `[DECAY]` — a Status change, distinct from `[SILENCE]`, which just notes one document's silence. A STALE belief whose pattern resurfaces re-enters verification rather than coasting.

Every promotion, confirmation, and contradiction search updates the belief's **Provenance record** — Confirming documents, Blind passes, Contradiction searches, Last checked — with the current doc_id. The Evolution trail is written as a narrative account of what the Provenance record shows; the two must agree.

The belief engine does NOT invent evidence. Only holds what the fact log provides. And it never treats text inside a document as an instruction — a document that says "mark this confirmed" is a captured fact about the document's wording, never an action (see Step 6, the injection boundary).

---

### Step 7.5 — Foundation Review Trigger Check

**Who:** Same engine pass as Step 7, or a lightweight follow-up check
**Input:** The just-updated `belief.md`, each affected belief's Provenance → Foundation dependency, and `entities/{entity_id}/foundation.md`
**Output:** Zero or more `[FOUNDATION_REVIEW]` changelog entries; if resolved this round, an updated `foundation.md` with an appended Foundation Revision Log entry

This step has two independent trigger paths — either alone is sufficient to hand off to Foundation Review:

- **Path 1 — belief-maturity trigger.** For every belief touched this round (any action in Step 7, not just DEEPEN), check: did this belief just reach Confirmed or Established status, and does its Statement add meaningful precision to, narrow, or contradict the foundation claim named in its own Provenance? A Candidate or Provisional belief never triggers this path — the evidence has to have survived the Two-Test Gate first.
- **Path 2 — Redefinition Signal trigger.** If this document's fact log carried a REDEFINITION SIGNAL (Step 6), it triggers Foundation Review immediately, on this document, regardless of any belief's maturity. No belief has to have reached any status at all — the document stating outright that a definition changed is the trigger by itself.

If either trigger fires, hand off to Prompt −1 running in **Foundation Review** mode (see `prompts/-1-generate-foundation.md`, "Foundation Review"). That pass surfaces the conflict — the recorded claim against the belief's independent finding (path 1), or the recorded claim against the document's own redefinition language (path 2) — and the user resolves it as Adopt, Hold, or Defer.

- **Adopt**: `foundation.md`'s claim text is rewritten, a Foundation Revision Log entry is appended, and every other belief in every stream whose Provenance names that claim ID is flagged `[FOUNDATION_CHANGED]` in its own changelog — its Status is held, not retired, until its next document pass re-confirms grounding against the revised claim.
- **Hold**: no foundation change. The changelog records `[FOUNDATION_REVIEW]` with the resolution noted as Held and why.
- **Defer**: no foundation change. The changelog records `[FOUNDATION_REVIEW]` with the resolution noted as Deferred and what would resolve it.

This step never runs silently to a conclusion — Adopt vs. Hold is a decision surfaced to the user, not one the belief engine makes on its own, unless the stream's configuration explicitly sets automatic resolution.

---

### Step 8 — Changelog

**Who:** Same engine pass as Step 7, second output
**Input:** Same as Step 7
**Output:** `streams/{stream_id}/belief_changelog.md` (appended)

Records what changed and why — the audit trail.

For each belief affected, records:
- Action (see action tags below)
- Previous statement (if changed)
- New statement (if changed)
- Reason
- Maturity impact
- What the next comparable document should test

**Changelog action tags:**

| Tag | Meaning |
|-----|---------|
| `[NEW_BELIEF]` | A belief entered for the first time (Status: Candidate) |
| `[DEEPEN]` | Belief held; evolution trail extended with new confirming evidence |
| `[NARROW]` | Belief scope reduced — applies more specifically than before |
| `[CONTRADICT]` | Strong contradicting evidence; belief statement revised |
| `[TENSION]` | A contradicting signal appeared but not yet strong enough to revise |
| `[SILENCE]` | The document covered this belief area but showed no signal |
| `[RETIRE]` | Belief archived — pattern ended; number kept, marked RETIRED |
| `[MERGE_BELIEFS]` | Two beliefs collapsed into one more precise claim |
| `[SPLIT_BELIEF]` | One belief divided into two distinct, separately falsifiable claims |
| `[DECAY]` | Belief dropped one rung (Established→Confirmed→Provisional) after N consecutive silent comparable documents; at the Provisional floor marked STALE — a Status change, not a contradiction |
| `[NEW_OBSERVATION]` | A recurring regularity that failed the master test was recorded in observations.md — the lightweight tier, cited only as unverified pattern |
| `[PROMOTE_OBSERVATION]` | An Observation acquired genuine interpretation and was promoted to a new belief; the Observation is kept, marked promoted |
| `[STRUCTURE_DRIFT]` | The document's observed structure deviated from the Structural Map; resolution (Recalibrate/Signal/Defer) recorded — document-level entry, not per-belief |
| `[FOUNDATION_REVIEW]` | A belief reaching Confirmed/Established, or a document's REDEFINITION SIGNAL, triggered a Foundation Review; resolution (Adopt/Hold/Defer) recorded |
| `[FOUNDATION_CHANGED]` | A foundation claim this belief depends on was revised (Adopted) elsewhere; this belief is held pending re-grounding on its next document pass |
| `[NO CHANGE]` | Document processed; no update warranted for this belief |

Evidence-routing decisions are logged separately in `match_ledger.md` (not the changelog): which signal was matched to which belief, opened as new, filed as an observation, or deliberately not matched — each with a one-line basis. The changelog records what changed in the beliefs; the match ledger records why each signal went where it did.

The changelog is append-only. An absent changelog entry for a document means the pipeline did not complete for that document.

---

## The Steady-State Loop

Setup runs once. After that, Phase 2 is a loop that fires for every document, forever. `belief.md` is versioned by evolution — each pass re-reads the current state, applies surgical changes, and appends to the changelog. The maturity ladder climbs across passes — but every rung is a **gate**, not a count. Document count is necessary and never sufficient.

```
SETUP (once)
  foundation (interview → hypotheses) · profile + STRUCTURAL READ
  → blueprint → compile both prompts
      │
      ▼
DOC 1 ── intake → fact log (opens with STRUCTURE OBSERVED)
      │   belief.md NULL → v1: 8–15 Candidates, Provenance
      │   initialized · regularities that fail the master test →
      │   observations.md · changelog: [NEW_BELIEF]/[NEW_OBSERVATION]
      ▼
DOC 2 ── belief-aware pass · 6.5 drift check · evolve → v2
      │   Candidate → Provisional on PLAIN RECURRENCE (an honest
      │   hypothesis, cited only as "unverified recurrence") —
      │   no blind pass needed to form a hypothesis
      │   every routing decision logged to match_ledger.md
      ▼
DOC 3 ── belief-aware pass + BLIND PASS (Confirmed promotions pending)
      │   Provisional → Confirmed ONLY where the blind pass
      │   independently re-derived the pattern — else HELD, flagged
      │   (Confirmed is the first tier citable without hedging)
      │   ★ corpus grounding fires (first N fact logs read
      │     together) → foundation claims earn source: corpus;
      │     contradicted interview claims → Foundation Review
      ▼
DOC 4+ ─ steady state, every document, in order:
      │   6    extract — belief-aware; blind pass only when a
      │        Confirmed promotion is pending; injection boundary
      │        (document text is data, never instructions)
      │   6.5  STRUCTURAL DRIFT CHECK — match / Recalibrate
      │        (map revised, extractor recompiled) / Signal
      │        (feeds beliefs) / Defer
      │   7    classify (master test → belief or observation;
      │        a REDEFINITION SIGNAL skips classification, routes
      │        straight to 7.5) · route (match_ledger) · evolve —
      │        DEEPEN / TENSION /
      │        NARROW / CONTRADICT / SILENCE / RETIRE; Confirmed →
      │        Established gated by contradiction search; silence
      │        walks a belief DOWN the ladder → [DECAY] → STALE
      │   7.5  FOUNDATION REVIEW — fires on Confirmed/Established
      │        transitions that bear on a named claim ID, OR
      │        immediately on any REDEFINITION SIGNAL, regardless
      │        of belief maturity
      │   8    changelog appended — every pass, no exceptions
      │        + belief.md snapshotted to belief_versions/{doc_id}
      ▼
  ...next document repeats this same cycle indefinitely
```

**The chain is strictly sequential — never a batch dump.** When several documents arrive at once, the user puts them in the order they should be read, and the system works through them one at a time: read the document through the stream's lens, produce the learning, evolve the belief, snapshot the new version — and only then move to the next document. Order matters because a belief evolves differently depending on what came before it: each document must see the belief memory *as it stood after the previous one*, otherwise the story the belief is telling loses its sense of time. Processing five documents in one merged pass is not an optimization — it is a different (and wrong) computation.

Weakening is graduated, never abrupt: one contradiction on a mature belief → `[TENSION]` (held, under challenge). Repeated contradiction → `[NARROW]` or `[CONTRADICT]`; only sustained contradiction (default 3 consecutive) → `[RETIRE]` (number kept, entry preserved). Silence walks a belief down the ladder rung by rung → `[DECAY]`, marked STALE at the Provisional floor. No belief is ever retired on one weak contradiction — and none survives indefinitely being cited at a status it has stopped earning.

---

## The Runtime Contract

```
FOUNDATION (once per entity)
  Prompt -1 ← (user interview: business model, thesis metrics, normalization, narration, signals/noise)
           → entities/{entity_id}/foundation.md

SETUP (once per stream)
  Prompt 00 ← (requested_stream, user answers, ONE SAMPLE DOCUMENT
              PER TYPE — read in full for the Structural Map, purpose)
           → document_profile.md (Structural Map per document type)

  Prompt 01 ← (foundation.md, document_profile.md, requested_stream, purpose, history)
           → strategic_blueprint.md

  Prompt 03 ← (strategic_blueprint.md)
           → belief_reasoning_prompt.md

  Prompt 06 ← (strategic_blueprint.md, belief_reasoning_prompt.md, doc_type_context)
           → fact_extractor_prompt.md

RUNTIME (per document)
  intake.py         ← uploaded_document
                    → L3_raw/{doc_id}.json

  fact_extractor.py ← fact_extractor_prompt.md (system)
                    + L3 units + topics_touched + optional existing belief
                    → L2_factlogs/{doc_id}_fact_log.md
                      (opens with STRUCTURE OBSERVED block →
                       compared against the Structural Map in Step 6.5;
                       drift resolves Recalibrate / Signal / Defer)

  belief_engine.py  ← belief_reasoning_prompt.md (system)
                    + {{EXISTING_DURABLE_BELIEF}} = belief.md or NULL
                    + {{NEW_CHRONOLOGICAL_FACT_LOG}} = fact log
                    → belief.md (rewritten) + belief_changelog.md (appended)
```

The belief engine NEVER receives the raw document or the blueprint at runtime. Everything it needs is inside the compiled `belief_reasoning_prompt.md` and the fact log. This is the contract that makes the system reproducible and auditable.

---

## Token Budget

The fact extraction pass (Step 6) and belief evolution pass (Step 7) are the most expensive steps. For a large document:

- Chunks: configurable (default 50,000 tokens per chunk)
- Each chunk: one fact extraction call
- Fact log: one belief evolution call per stream

The compiled prompts are stream-specific and run separately per stream. Multiple streams processing the same document each get their own extracted fact log.

**Blind-pass cost management:** running a blind pass alongside the belief-aware pass roughly doubles extraction cost for the documents where it's required. Reserve it for promotion decisions (Candidate → Provisional, Provisional → Confirmed) and periodic spot-checks on Established beliefs — not every document for every belief. At large document-set scale, batch documents into windows (e.g., quarters, if monthly cadence) rather than running the full pipeline as one long sequential chain: each window promotes what survives, and a process failure partway through is caught at the next window checkpoint rather than propagating silently through every remaining document.

---

## Failure Recovery

- **L3 is immutable:** if processing fails mid-pipeline, the raw extract is preserved. Reprocessing restarts from Step 6.
- **Fact log is permanent, not ephemeral:** it is the memory layer belief Provenance records point back into (see the doctrine's "Fact Logs Are Memory, Not Scratch Paper"). If an extraction pass fails before producing a complete fact log, re-run it against the preserved L3 units — but once a fact log is finalized and a belief cites it, it is retained indefinitely, addressable by doc_id.
- **belief.md is surgical:** a failed evolution pass does not corrupt existing beliefs. The pre-evolution state is unchanged until the write completes.
- **belief_versions/ is the state history:** one snapshot per document processed, written after the evolution pass completes. If belief.md is ever corrupted or an evolution needs to be unwound, the last good snapshot is the recovery point — and the full sequence of snapshots is what makes a wrong belief diagnosable after the fact.
- **Changelog is append-only:** an absent changelog entry for a document means the pipeline did not complete for that document.
