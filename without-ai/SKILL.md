---
name: without-ai
description: Takes a prompt the user would normally throw at an LLM and produces a comprehensive plan for an AI-free (or AI-trending-to-zero) infrastructure that answers it durably — runnable on local hardware, build­able with AI as a one-time bootstrap, maintainable by a solo person. Outputs a high-level overview with architecture diagrams, a roadmap, an "AI fork vs without-ai fork" comparison, an analysis of why this prompt category is brittle to put in front of an LLM, and copy-pasteable handoff packets for /teach-me, /productionize-me, and /hacky-hours. Optionally scaffolds the actual infrastructure in a new repo and uses it to answer the original prompt, with human-readable docs so a solo person can take over. Use this skill whenever the user asks "what would the non-AI version of this look like", "how do I build this without depending on an LLM", "how do I make this self-hostable", "design infrastructure for this", "what's the long-term version of this prompt", or whenever you see them about to repeatedly throw the same kind of question at an LLM and you should suggest standardizing it as infrastructure instead. Triggers on /without-ai, "minimize AI dependency", "trend AI to zero", "build me an editor / engine / DSL for X", "what tools would replace this AI workflow", or whenever a prompt implicates generating assets (art, copy, designs, rules, layouts) that an LLM would one-shot but a real product needs a tool to produce consistently. Default behavior is autonomous after one short intake — produces the planning artifact, then asks before scaffolding the actual repo.
---

# without-ai

A skill for taking a prompt — the kind a person would normally hand to an LLM — and producing a plan, and optionally a working repository, for a **non-AI (or AI-trending-to-zero) infrastructure** that answers it durably.

The core move is to refuse the instant answer. Instead of solving the prompt as stated, you ask: *what is the user actually going to want a year from now, and what infrastructure would make this prompt — and the next ten like it — answerable without ever going back to a model?*

## The premise

A prompt to an LLM is a transient artifact. The answer evaporates the moment the context window closes; the next user with the same need pays the same tokens and gets a slightly different answer. For some questions ("what's a good name for my band") that's fine. For many ("build me a clone of Magic: The Gathering"; "design a curriculum for teaching my kid algebra"; "generate the art for my game") the prompt is **a brittle stand-in for infrastructure the user actually needs**.

This skill identifies those cases, designs the infrastructure, and (optionally) builds it. The deliverable is something the user owns, hosts locally, can keep using when the AI bill stops being affordable, and can hand to another person without an API key.

The user's example to keep in mind: *"build me a clone of Magic: The Gathering"* — the AI answer is to start generating cards and rules text. The without-ai answer is to design **a card-game engine** with a card-definition schema, a rules-evaluation DSL, an art-asset pipeline with a custom editor, and a tournament/balance-test harness. The user ends up able to build *any* card battler, not just one shaky MTG impersonation.

## What the skill produces

Every run produces these artifacts under `./without-ai/<run-id>/`:

| Artifact | What it is |
|---|---|
| `_overview.md` | The full plan, in markdown, with embedded Mermaid diagrams. Authoritative document. |
| `_overview.html` | Standalone rendered version of the overview — opens in any browser, shows diagrams, suitable to send to someone else. |
| `architecture/` | Per-component design docs (`engine.md`, `editor.md`, `data-model.md`, etc.) referenced from `_overview.md`. |
| `roadmap.md` | Phased plan, calibrated to a solo builder, with explicit "AI dependency at end of each phase" tracking. |
| `ai-vs-without-ai.md` | Side-by-side: what the LLM solution would have been, why it's brittle long-term, what categories of prompts this brittleness applies to. |
| `benefits.md` | Honest list of what the user gains from the infra approach (and what they give up — speed-to-first-answer is real). |
| `handoff/teach-me.md` | Copy-pasteable prompt for `/teach-me` to build a curriculum that teaches the user every piece of the infra. |
| `handoff/productionize-me.md` | Vibe-coding prompt that builds the infra, designed to be analyzed by `/productionize-me` after. |
| `handoff/hacky-hours.md` | Copy-pasteable prompt for `/hacky-hours` if the user wants to scope this as a structured weekend-build. |

If the user opts into Phase 2 (build-and-prove), the run *also* produces a sibling repo at `./without-ai/<run-id>/repo/` containing the actual scaffolded infrastructure plus human-readable docs (see Phase 2 below).

## Default parameters

| Parameter | Default |
|---|---|
| Run mode | Autonomous after one short intake. After Phase 0, run Phase 1 to completion without interruption. Pause once before Phase 2 (build) since that's the expensive/sticky step. |
| Output directory | `./without-ai/<run-id>/`. Default `<run-id>` = today's ISO date. If that exists, append `-2`, `-3`, etc. User can override at intake. |
| Builder profile | Solo person, full-time job, evenings and weekends, $0–$500 to start, off-the-shelf tooling, local hosting (laptop, single VPS, or NAS — no cloud-native assumptions). |
| AI dependency target | Trends to **zero or near-zero** in steady state. AI is acceptable as a one-time bootstrap (writing scaffolding code, generating placeholder assets) but the running system must function without it. |
| Build-and-prove | Off by default. Always offered after Phase 1 lands. |
| Multi-prompt input | If the user supplies more than one prompt, generate one plan per prompt *plus* `_meta-overview.md` identifying shared infrastructure across them. |

The user can override any of these at intake. Honor what they say; only fall back to defaults for what they didn't specify.

## The pipeline

Use TaskCreate to track phases — runs can be long.

### Phase 0 — Intake (the only blocking step)

If the user's invocation already gives you a clean prompt, restate it and skip to confirmation. Otherwise ask, in one round (use AskUserQuestion if available):

1. **The prompt** — what would they have asked the LLM? Get the full thing in their words. Ask for multiple if they have a series.
2. **Domain hints** — anything about who it's for, what platform, what scale (just me / a few friends / public)? Drives architecture choices.
3. **Hard constraints** — any "must run on a Raspberry Pi" / "must work offline" / "no JavaScript" type rules.
4. **Build-and-prove preference** — "After I deliver the plan, do you want me to also scaffold the actual repo and use it to answer your prompt? (default: I'll ask after the plan is done.)"
5. **Run-id** — accept override; otherwise today's date.

Write `./without-ai/<run-id>/_brief.md` with what you captured, confirm it back in one paragraph, then announce: *"Going autonomous through the planning phase. I'll surface when the overview and handoff packets are written."*

### Phase 1 — Plan the infrastructure

This is the heart of the skill. For each prompt:

#### 1. Restate the prompt verbatim and sketch the AI answer

Open the per-prompt working file with the user's exact words. Then in a section called *"What the LLM would have done"*, write a candid sketch of how a model would actually answer this prompt today — what it would generate, where it would hand-wave, what would feel impressive in the first 30 seconds and break down on the 30th use. This is not a strawman; be honest about what LLMs do well here.

#### 2. Categorize the brittleness

Read `references/brittle-prompt-taxonomy.md` and identify which categories this prompt falls into. Common ones:
- **Asset-generation-disguised-as-question** ("design my game's cards")
- **Repeated-instance-of-the-same-pattern** ("answer this kind of customer question") — the user will run it a thousand times
- **Stateful-thing-pretending-to-be-stateless** ("track my workouts")
- **Deterministic-rules-disguised-as-prose** ("adjudicate this MTG turn")
- **Personal-context-that-should-be-durable** ("plan my week given everything you know about me")
- **Creative-tool-the-user-actually-wants** ("write me a song" → music sequencer)

Be honest if the prompt *isn't* a good without-ai candidate. Some prompts ("rephrase this email") are genuinely well-served by an LLM and trying to build infrastructure for them is overkill. Say so plainly. The valuable signal here is when the user is about to repeatedly hit a model for something a tool would do better — flag that, don't manufacture work.

#### 3. Abstract upward

The MTG example is the rule, not the exception: the right move is almost always to abstract one level above the prompt. The user said "MTG clone" but wants "card battler engine"; the user said "tutor my kid in algebra" but wants "personal-curriculum authoring tool"; the user said "recipe app that knows what's in my fridge" but wants "ingredient-graph + meal-database with a barcode scanner".

Write the abstracted target as a one-paragraph framing in `_overview.md` under *"What you're actually building"*.

#### 4. Design the architecture

Read `references/infra-patterns.md` for the standard patterns. Produce, in `_overview.md`:

- A **component diagram** (Mermaid `graph` or `flowchart`) showing the major pieces — data model, engine/runtime, editor(s), import/export, UI.
- A **data-flow diagram** showing how a single end-user request flows through the system without an LLM in the loop.
- A **deployment diagram** for the local hosting story (laptop / VPS / NAS / browser-only — pick what fits).
- A short prose description of each component, with deeper detail spilled into `architecture/<component>.md` when it gets long.

The architecture must be **runnable on commodity hardware** and **maintainable by one person**. If you can't honestly say that, narrow the scope until you can.

#### 5. The AI-trending-to-zero curve

In `_overview.md`, include a *"AI dependency over time"* section with a Mermaid timeline (or a simple table) showing what role AI plays in Phase 1 / Phase 2 / Phase 3 / steady-state. Acceptable AI roles in steady state are typically zero or near-zero — examples of legitimate residual roles: optional natural-language search over a hand-built corpus; a fallback for never-seen-before inputs that gets logged for the user to bake into the system. Anything load-bearing in steady state is a flag and you should call it out.

#### 6. Asset-creation tools

If the prompt implicates generating assets — art, copy, music, level layouts, card definitions, character sheets, recipes, lesson plans — the without-ai answer is almost always **an editor or engine the user can use to make those assets themselves**, not "we'll generate them with AI". Design the editor explicitly:

- What does the editing surface look like (sketch the UI in markdown or ASCII)?
- What's the file format the editor reads/writes (and is it human-readable so the user can hand-edit)?
- What primitives does the editor provide (brushes, templates, snippets, copy-paste from another instance)?
- What's the smallest version that's actually useful?

Reference patterns in `references/infra-patterns.md` under "asset-tool patterns".

#### 7. Roadmap

In `roadmap.md`, lay out 3–5 phases for a solo builder. For each phase: scope, time estimate (in evenings/weekends), what's runnable at the end, AI dependency at end of phase (a number or short description), and what's deferred. Be honest — most of these projects are 3–12 months of solo evenings, not weekends.

#### 8. Benefits, costs, and brittle-prompt analysis

- `benefits.md` — what the user gains: ownership, lower running cost, no rate limits, durability, the ability to share with someone who has no API key, the ability to keep working offline, the option to commercialize without an OpenAI bill in their COGS.
- `ai-vs-without-ai.md` — a side-by-side comparison plus a section *"why this category of prompt is brittle to put in front of an LLM"* that generalizes from the user's specific prompt to the class of prompts it represents. This is the most reusable piece of writing in the run.
- Be candid about what they give up: speed-to-first-version, generative variety, sometimes quality on day one. The honest comparison is what makes the rest credible.

#### 9. Handoff packets

Read `references/handoff-templates.md` and produce three files in `handoff/`:

- `teach-me.md` — a prompt the user can paste into `/teach-me` to get a curriculum that covers every skill they need to build the proposed infra (DSL design, sprite-editor UX, SQLite, etc.).
- `productionize-me.md` — a self-contained prompt that an AI agent can execute to vibe-code the proposed infra into a fresh repo. The output of *that* run is exactly what `/productionize-me` is designed to audit and harden.
- `hacky-hours.md` — a structured prompt for `/hacky-hours` framing the build as a recurring evening project.

Each handoff file is copy-pasteable and pre-filled with all the context from this run. The user shouldn't need to re-explain anything.

#### 10. Render `_overview.html`

Take `assets/overview-template.html`, substitute in the run's content, and write `./without-ai/<run-id>/_overview.html`. This is the artifact the user will most likely show to someone else, so it should look respectable. Mermaid diagrams render via CDN.

#### 11. Surface the result

Tell the user the plan is done, point at `_overview.html` as the entry point, and ask: *"Want me to scaffold the actual infrastructure in a new repo and use it to answer your original prompt? This is Phase 2 — heavier, slower, but you end up with a runnable starting point and human-readable docs."* Wait for the answer before proceeding.

### Phase 2 — Build-and-prove (opt-in)

If the user says yes, follow `references/build-and-prove.md`. The shape of this phase:

1. **Scaffold the repo** at `./without-ai/<run-id>/repo/` — directory structure, package config, README placeholder, license, gitignore. Initialize as a git repo.
2. **Build the minimum viable infrastructure** to answer the original prompt. *Minimum* is load-bearing here — the goal is to *prove the plan can answer the prompt*, not to build a v1 product. If the prompt is "build a card battler", the proof is one card-definition file, one rule-evaluation pass, and a CLI that plays one turn. The roadmap is for the rest.
3. **Use the infrastructure to answer the original prompt.** Run the system. Show the output. Capture the run in `PROOF.md` — the actual command used, the actual output, a short reflection on what's still missing vs. what the plan promised.
4. **Write human-readable docs.** Bare minimum:
   - `README.md` — what this is, why it exists (link back to `_overview.md`), how to run it in three commands, where to look next.
   - `ARCHITECTURE.md` — same diagrams as the overview but specific to what got built, with file/folder pointers.
   - `GETTING_STARTED.md` — a tutorial that takes a fresh user from clone → running the proof → editing one piece of content → running it again. This is the document that determines whether the user can take over from here.
   - Per-component `README.md` files inside each major directory.
5. **Honesty pass.** Add a `LIMITATIONS.md` listing what's stubbed, what's hardcoded, what would break under load. The user is going to find this out anyway; better to put it in writing.
6. **Exit cleanly.** Surface the path to `repo/`, summarize what's runnable today, and point to `roadmap.md` for next steps. Do not claim it's production-ready — it isn't. Phase 2 is a *proof*, the roadmap is the path to real.

The build-and-prove step is intentionally constrained to what one solo person could keep maintaining. If the proposed infra is too big to scaffold meaningfully in one Phase 2 pass, narrow Phase 2 to the smallest *vertical slice* that exercises every component of the architecture, and say so.

## When *not* to use this skill

Be honest with the user. The skill is overkill — and you should say so plainly — when:
- The prompt is genuinely one-shot and the user will never repeat it.
- The "asset" the LLM would produce is the deliverable itself (e.g., one cover letter for one job — `/draft-me` is a better fit).
- The infrastructure cost wildly exceeds the value of the answer (don't build a CMS to write three blog posts).
- The user wants to *learn* something, not build infrastructure (`/teach-me` directly is better).

If you find yourself stretching to justify the without-ai treatment, stop and tell the user it isn't a fit. That call is more valuable than another pile of artifacts.

## Multi-prompt runs

If the user supplies multiple prompts in one invocation, run Phase 1 for each (sequentially is fine; don't try to parallelize the writing). Then write `_meta-overview.md`:

- For each prompt, a one-paragraph summary linking to its full plan.
- A *"shared infrastructure"* section identifying components multiple prompts want — these are the highest-leverage things to build first. Use Mermaid to show prompt-to-component overlap.
- A consolidated roadmap if it makes sense (often the right answer is "build the shared stuff once, then layer the prompt-specific bits on top").

The meta-overview is the reason multi-prompt mode exists. If there's no meaningful overlap, say so and treat the run as N independent plans.

## Style notes

- Write the deliverables as if to a smart solo builder who's tired of paying API bills. They are technical but not omniscient — explain why each architectural choice is the way it is.
- Diagrams are first-class. If a section would benefit from a diagram, draw the diagram (Mermaid). Don't just describe it.
- Don't oversell. The honest version of "this will take you 6 months of evenings" is more valuable than the fictional version where it's done in a weekend. The user will trust the artifact more if it doesn't lie about effort.
- Keep the `_overview.html` polished. It's the document the user shows to someone else.

## Reference files

- `references/brittle-prompt-taxonomy.md` — categories of prompts that benefit from infrastructure replacement, with examples.
- `references/infra-patterns.md` — standard patterns for replacing AI with infrastructure, including asset-tool patterns.
- `references/handoff-templates.md` — exact structures for the three handoff packets.
- `references/build-and-prove.md` — playbook for Phase 2.
- `assets/overview-template.html` — the HTML template for the rendered overview.
