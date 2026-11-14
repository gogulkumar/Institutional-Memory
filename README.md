# Enterprise Institutional Memory Framework

A framework that gives any AI agent an institutional brain: a governed memory of how a business works and how its experts reason about it, that gets better every time the business produces a document.

- **[SPEC.md](./SPEC.md)** is the framework: components, entry schemas, trust ladder, processes. It is the single source of truth.
- **[skills/](./skills/)** are the three skills an agent runs: `build`, `learn`, `think`.
- **[templates/brain/](./templates/brain/)** is an empty brain to copy.
- **[examples/expedia/](./examples/expedia/)** is one worked brain.

## Why this exists

The model is the reasoning engine, and everyone has the same one. What makes an agent useful inside one company is the layer around the model: what its metrics mean, which source wins when two disagree, what normal looks like, how the business has behaved before, and how its experts decide what matters. Today that layer lives in people's heads and in decks nobody rereads.

Retrieval does not recover it. A search over documents finds what is textually near, not what is authoritative, current, or judgment-relevant. It cannot tell a draft from an actual, an expired fact from a standing rule, or a one-off comment from a pattern that has held for two years.

The framework turns that layer into a structured, auditable memory an agent reads at the right moment and maintains as a side effect of real work. Every team that deploys it gets the same discipline instead of an ad hoc pile of prompts and notes.

## How it works

Six components hold memory. Each piece of information has exactly one home.

| Component | Holds |
|---|---|
| **Lens** | What the work is for: deliverables, audiences, decisions, and one procedure per deliverable |
| **Record** | Pointers to source documents and data, tool contracts, source authority |
| **Business Understanding** | Concepts, metric definitions, what normal looks like, which metrics drive which |
| **Beliefs** | Durable interpretations no single document states, plus open questions carried across periods |
| **Reasoning Patterns** | How experts sequence questions and decide materiality, attribution and when to stop |
| **Editorial Judgment & Voice** | What to lead with, include and omit for each audience |

Three processes act on it:

- **Build** sets up a brain for a new domain: the Lens, the Record, seed definitions, a backfill over past periods, and an expert interview.
- **Learn** runs on every new document. The agent predicts what it will say, reads it without memory, and treats each gap as a signal about which entry is wrong. Changes go through a proposal queue.
- **Think** runs on every task. The agent reads the new evidence first, ranks the questions worth asking, investigates only what matters, stops at what the evidence supports, and writes back conclusions only.

Trust is earned on one ladder (observation → candidate → provisional → established), counted in independent business events, not documents. The agent's wording follows trust: "suggests", "accounts for", "because". People approve what matters: promotion to established, contradictions, retirements, changes in meaning.

Memory never stores numbers. Values stay in source systems and are queried when needed.

## Quickstart

1. Copy `templates/brain/` into your agent's workspace as `brain/`.
2. Fill `brain/config.yaml`: owner, backup reviewer, review windows.
3. Give your agent the three skills in `skills/` and file, tool and sub-agent access (SPEC §7).
4. Run `build` on one deliverable with a few past periods of documents.
5. Wire `learn` to run when a new document arrives and `think` to run when a task arrives.
6. Validate the brain at any time:
   ```bash
   python schemas/validate.py brain/
   ```

## What it is not

- Not a document store or RAG index. Documents stay in the Record.
- Not a data warehouse. Numbers are queried, never memorized.
- Not fine-tuning. Every belief can be shown, traced to its evidence, and corrected.
- Not a transcript of past work. Only conclusions that change future interpretation are kept.

## Where to start

Start with one domain where documents recur and judgment is dense, such as quarterly business reviews or forecast reviews. Build from the decisions the brain must support, not from the documents you happen to have. Measure it on held-out periods: does the agent ask the questions your experts asked, and produce what they produced (SPEC §8)?
