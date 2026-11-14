# Example: Expedia earnings-call narrative brain

This is an illustrative brain, built from five quarters of Expedia Group earnings-call material (Q1 2025 to Q1 2026). It shows what a populated brain looks like. It is not a maintained analysis, and its entries are not investment views.

It has one deliverable, a quarterly narrative brief, and 21 entries across all six components:
- **Lens:** the narrative brief and its procedure
- **Record:** three call artifacts, a transcript-search tool contract and a source authority rule
- **Business Understanding:** concepts such as call architecture and minimizing qualifiers, the total versus domestic US bookings definition, a Normality entry, and one dependency link
- **Beliefs:** one belief at each of candidate, provisional and established, plus two Story Threads
- **Reasoning Patterns:** an inquiry chain for metric substitution, and an attribution rule
- **Editorial:** the brief's structure

The governance files show a Learn pass in progress:
- the match ledger for the Q1 2026 call
- two queued proposals in `proposals/pending/`, one automatic and one that needs ratification
- changelog lines

As the framework requires, memory holds no figures, only patterns and pointers to the Record. The source files listed under `location` are not included.

`index.yaml` is generated as of 2026-06-01:

```bash
python schemas/validate.py examples/expedia/brain --today 2026-06-01
```
