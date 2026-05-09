# Build-and-prove playbook

Phase 2 of the skill. The user has reviewed the plan in `_overview.md` and asked you to scaffold the actual repo. The goal is a *proof* — a working repo that uses the proposed infrastructure to answer the original prompt — plus human-readable docs so the user can take over.

This is **not** "build the v1 product." It's "build the smallest thing that exercises every component of the architecture, so the plan is demonstrably real."

---

## What you're building

A repo at `./without-ai/<run-id>/repo/` containing:

```
repo/
├── README.md                # what this is, why, 3-command quickstart
├── ARCHITECTURE.md          # diagrams + file pointers
├── GETTING_STARTED.md       # tutorial: clone → run → edit → run again
├── LIMITATIONS.md           # honest stub list
├── PROOF.md                 # the system answering the original prompt
├── <component-1>/
│   ├── README.md
│   └── ...
├── <component-2>/
│   ├── README.md
│   └── ...
└── ... (per-component dirs from the architecture)
```

If the proposed infra has a natural existing layout convention (Python package, Node monorepo, Go project, etc.), use it. Don't impose `<component>/` directory style if it conflicts with a real convention.

---

## The vertical-slice rule

**Every component in the architecture must be exercised by the proof.** That's the rule that makes this a *proof* instead of a vague start.

For the MTG-clone example with these components:
- card schema + DB
- rules DSL + interpreter
- card editor
- art-asset pipeline
- balance-test harness

A valid Phase 2 build is:
- Card schema with **3 hand-written cards** in YAML.
- Rules DSL that handles **just the abilities those 3 cards use** (e.g., "deal damage", "draw a card", "destroy a creature").
- Card editor that's just a YAML form + live preview, with **no styling polish**.
- Art-asset pipeline that takes a placeholder PNG and composites it under the card frame.
- Balance-test harness that simulates **one matchup, one time**, between two pre-built decks.

That's the proof. The roadmap is the rest.

If a component genuinely cannot be exercised in a small vertical slice (rare; usually means the architecture is wrong), narrow Phase 2 to the components that *can* be exercised and explain in `LIMITATIONS.md` what was deferred.

---

## Sequence

### Step 1 — Scaffold

1. Create `./without-ai/<run-id>/repo/`.
2. `git init`.
3. Create the directory layout.
4. Write a stub `README.md`, `ARCHITECTURE.md`, `GETTING_STARTED.md` (placeholders — fill in at end).
5. Add a `.gitignore` and a license file (default MIT unless user said otherwise at intake).
6. Add config for the language stack (`pyproject.toml`, `package.json`, `go.mod`, etc.).
7. Commit: "scaffold".

### Step 2 — Build component-by-component

Build in dependency order — bottom-up. Foundations first (data model, schema, file format), interpreters and engines next, editors and UIs last.

For each component:
1. Write the smallest thing that works.
2. Write a per-component `README.md`: what this is, the public interface (functions/CLIs/HTTP endpoints), the file formats it produces or consumes, an example.
3. Add a few tests if the component has obvious assertions (parsers, evaluators, generators with seeds).
4. Commit per component or per logical unit. Small commits.

Lean toward boring tools. SQLite over Postgres. Single binary over microservices. `make` over a custom task runner. The user will read this code; readability beats cleverness.

### Step 3 — Wire it into a proof

Pick the **smallest invocation** that answers the original prompt using every component. This usually looks like:

- A CLI command, a `make demo` target, or a script in `scripts/proof.sh`.
- It exercises the data layer (read a few rows), the engine/runtime (one evaluation pass), and produces output the user can see.

Run it. Capture the actual output. Do *not* fake it.

### Step 4 — Write `PROOF.md`

```markdown
# Proof

The original prompt this infrastructure answers:

> <verbatim user prompt>

## How the infrastructure answers it

<one paragraph: which components are involved, in what order>

## The actual run

```
$ <exact command>
<actual stdout>
```

<screenshot reference if there's a UI: e.g., "See screenshots/proof-1.png">

## What this demonstrates

- <each component>: <what role it played in the run>

## What this does *not* yet demonstrate

- <each component>: <what's still stubbed/hardcoded/unbuilt; pointer to roadmap.md phase>
```

The "does not yet demonstrate" section is critical. It's how the user knows what they're getting and what's still ahead.

### Step 5 — Write the human-readable docs

These four documents determine whether the user can take over from here. Spend real effort.

#### `README.md`

```markdown
# <project name>

<one-paragraph plain-English description of what this is and who it's for>

This was generated as the build-and-prove output of a `/without-ai` plan. The full plan, including the architecture diagrams, the AI-vs-without-ai analysis, and the roadmap, lives at `../_overview.md`.

## Why this exists (instead of an LLM call)

<one paragraph from `ai-vs-without-ai.md`>

## Quickstart (3 commands)

```bash
<command 1>
<command 2>
<command 3>
```

You should see <expected output>. If you don't, see `GETTING_STARTED.md`.

## What's here

| Directory | What it is |
|---|---|
| <list each top-level directory with one line> |

## What's not here yet

See `LIMITATIONS.md` and `../roadmap.md`.
```

#### `ARCHITECTURE.md`

Same diagrams as `_overview.md`, but every component now has a concrete file/folder pointer.

```markdown
# Architecture

<the component diagram, Mermaid>

## Components

### <component name> — `<directory>/`

<one paragraph: what it does>

**Public interface:** <function signatures / CLI / endpoints>

**File format:** <if it produces or consumes data>

**Read these files to understand it:** <2-4 file pointers>

**Tests:** `<test file or directory>`

(...repeat for each component)

## Data flow

<flow diagram, Mermaid>

For a worked example, see `PROOF.md`.
```

#### `GETTING_STARTED.md`

A tutorial. It takes a fresh user from `git clone` to running the proof to **editing one piece of content** to re-running. This document is what determines whether someone other than you can keep building on this. Spend time on it.

```markdown
# Getting started

This tutorial takes about <N> minutes. By the end, you'll have:
- The system running locally.
- A copy of the proof output.
- One piece of content you edited yourself, with the system reflecting your edit.

## 1. Set up

<exact steps; show actual commands and expected output>

## 2. Run the proof

<exact command, exact expected output>

## 3. Edit a piece of content

<pick the smallest user-editable piece — one card, one sprite, one lesson — and walk the user through editing it>

Open `<file>` in your editor. Change `<this field>` to `<that value>`. Save.

## 4. Re-run

<exact command, expected new output>

You just changed the system without writing code or talking to an LLM. That's the whole point.

## What to do next

- Read `ARCHITECTURE.md` to understand what's where.
- Read `../roadmap.md` to see what's planned next.
- Pick a Phase 2 item from the roadmap and implement it. The handoffs at `../handoff/` are pre-loaded with context.
```

#### `LIMITATIONS.md`

Be honest. The user will find these out anyway; better in writing.

```markdown
# Limitations

This is a Phase 2 proof, not a finished product. Here's what's stubbed, hardcoded, or skipped — and where to look in the roadmap to fill it in.

## Stubbed
- <thing>: <where, why, and which roadmap phase fills it>

## Hardcoded
- <thing>: <where, why, and what would make it dynamic>

## Skipped entirely
- <thing>: <why it's deferred and how to add it later>

## Things that will break under load
- <thing>: <under what conditions, and what to swap in>
```

### Step 6 — Per-component READMEs

Inside each component directory, a focused `README.md`:

- What this component is in one sentence.
- Public interface (functions, CLI, endpoints).
- File formats it produces or consumes.
- An example.
- Tests location.
- Where it sits in the larger architecture (link to root `ARCHITECTURE.md`).

These short documents are what the user re-reads when they sit down on a Saturday morning and try to remember what this folder was for.

### Step 7 — Final pass

1. Run the quickstart yourself, fresh, exactly as written. Fix anything that doesn't work.
2. Make sure every diagram is current.
3. Commit: "phase 2 complete: <one-line summary>".

### Step 8 — Surface the result

In chat, tell the user:

- The path to the repo.
- The exact command for the proof (so they can run it).
- A one-paragraph summary of what got built.
- The honest list of what's still ahead (point at `LIMITATIONS.md` and `roadmap.md`).
- The handoffs they can paste into `/teach-me`, `/productionize-me`, `/hacky-hours` next.

Do **not** call it production-ready. Call it a proof. The roadmap and the handoffs are the path to real.

---

## Things to avoid in Phase 2

- Don't add features that aren't in the architecture. The plan is the contract.
- Don't add observability, CI, advanced testing. Those are `/productionize-me`'s job. Phase 2 is about *the plan being real*, not about being production-grade.
- Don't sneak the LLM back in. If you find yourself wanting to add an LLM call to make something work, that's a signal the architecture isn't right — escalate to the user before adding it.
- Don't gold-plate the docs. They should be accurate and short, not exhaustive.
- Don't fake the proof. If the system doesn't actually answer the prompt, say so plainly in `PROOF.md` under "what this does not yet demonstrate" — that's still a useful artifact.

The standard for Phase 2: **a real human, alone, with this repo and these docs, can keep building.** That's the bar.
