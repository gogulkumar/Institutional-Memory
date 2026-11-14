# Discovery angles

The angles below are prompts for **finding** candidate Beliefs during Learn step 4–5. They are not storage partitions and not a required field (SPEC §4.5). A Belief may carry one as an optional `tag`.

Facts about what a metric means or how it is calculated are not Beliefs. They go to Business Understanding as concepts or metric definitions (SPEC §4.4).

Every candidate found through an angle must still pass the master test (SPEC §4.5): it says something no single document says, draws on two or more Business Understanding entries, and implies an action for a named deliverable.

---

## 1. Business model
**Ask:** How does this business actually make and keep money, and which of its engines is doing the work right now?
**Look for:** shifts in where growth comes from (volume vs price vs mix), which lines carry profitability, which investments are structural vs discretionary.
**Test:** the statement describes the same underlying reality whichever period you read it in. If it only holds for one period it is a result, not a belief.

## 2. Business dynamics
**Ask:** How do the numbers move together: what leads, what lags, where does a chain break?
**Look for:** lead-lag relations, conversion chains, offsets, feedback loops, seasonality that recurs across periods. Confirmed relations also become Dependency Map links (SPEC §4.4).
**Test:** the statement would still hold if the management team changed completely. It describes how the numbers behave, not how people decide.

## 3. Causal attribution
**Ask:** What does the team say caused its results, and how reliable is that attribution?
**Look for:** recurring explanations for misses and beats, which causes are named first, which are never named, where attribution is later revised.
**Test:** a reader could predict what the team will say in the next miss period, and whether to accept or probe the attribution.

## 4. Organizational behavior
**Ask:** What does this organization actually do under pressure, as opposed to what it says it will do?
**Look for:** what gets protected and what gets cut, how fast it reacts, which commitments survive a bad period.
**Test:** a reader could predict the organization's next move in a comparable situation, and would recognize a deviation as a signal.

## 5. Narrative versus numbers
**Ask:** How is the story told, and where does the telling diverge from what the numbers show?
**Look for:** recurring structure of documents, what leads and what is buried, language that shifts before results shift.
**Test:** a reader could predict the structure of the next document, and notice immediately when it deviates and what that signals.

## 6. Forecast and plan behavior
**Ask:** How are forecasts and plans set and revised over time?
**Look for:** systematic direction of revisions, timing of resets, which assumptions are habitually optimistic or conservative. Express patterns as directions and relative sizes, never absolute values (SPEC Principle 2).
**Test:** a reader could predict the direction and rough relative size of the next revision from the pattern alone.

---

## Using the angles
- Run the angles **after** the blind read and comparison, against the signals the pass produced, never before (SPEC Principle 5).
- An angle that yields nothing in a pass is normal. Do not force a candidate.
- If two angles produce the same insight, propose one entry and list both tags.
- Wording rules for every statement: SPEC §4.5 statement rules.
