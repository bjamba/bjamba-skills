# bjamba-skills

A collection of custom Claude Code skills by [@bjamba](https://github.com/bjamba).

## Skills

### teach-me

A personalized learning coach that builds a complete curriculum and study environment for any topic. Give it a topic — anything from wine pairing to Rust programming to being a better listener — and it builds you a complete, interactive learning environment tailored to how you learn.

**What it does:**

1. **Interviews you** about what you want to learn, your goals, timeline, and how you like to learn
2. **Designs a curriculum** with modules, lessons, exercises, and milestones
3. **Builds a full repository** of interactive HTML lessons, flashcard apps, quizzes, progress dashboards, and whatever artifacts fit your learning style
4. **Tutors you** when you come back — picks up where you left off, keeps you on track, adapts the pace, and creates new material on the fly

**Usage:**

```
/teach-me how to pair wines with cheeses
```

Or just describe what you want to learn:

```
I want to get better at machine learning classification models
```

The skill also activates automatically when you open a conversation inside an existing teach-me repo (one that has a `curriculum.json` file) — it'll pick up where you left off in tutor mode.

**What it produces:**

- **`dashboard.html`** — Interactive progress dashboard you open in your browser. Tracks your journey visually.
- **HTML lessons** — Styled, navigable lesson pages (not flat markdown). Just double-click to open.
- **Interactive tools** — Flashcard apps, quizzes, matching games, reference cards, scenario practice tools. All single-file HTML, no dependencies.
- **`curriculum.json`** — Machine-readable curriculum state so Claude can pick up where you left off.
- **Exercises** — Hands-on practice tailored to the topic. Could be coding exercises, tasting worksheets, conversation scenarios, creative prompts — whatever fits.

For technical topics, it uses Jupyter notebooks instead of raw code files. For non-technical topics, everything is browser-based — no terminal required.

### continuity-check

A continuity analyst for any body of text. Point it at a story, novel, series, article collection, or any long-form writing and it produces an interactive "canon bible" website that maps every element of the work and flags where things don't add up — character inconsistencies, timeline errors, world-rule violations, tonal drift, plot holes.

**What it does:**

1. **Ingests the text** — fiction, non-fiction, journalism, blog posts, anything
2. **Extracts the canon** — characters, locations, timelines, world rules, relationships, tone signatures
3. **Runs continuity checks** — flags contradictions, timeline errors, character drift, rule violations
4. **Builds an interactive website** — canon bible pages, relationship maps, deviation-scored annotations, searchable index

**Usage:**

```
/continuity-check on the drafts in ./my-novel/
```

Or naturally:

```
Does this draft contradict anything in the earlier chapters?
```

**What it produces:** a single-file HTML site with navigable canon pages, visual relationship maps, a scored list of continuity deviations, and annotation tools so you can accept/reject flags as you edit.

### draft-me

An iterative writing collaborator that learns your voice from a folder of your own writing, then helps you produce a new piece through a structured brainstorm → draft → review → finalize loop. Built for things you want in *your* voice — cover letters, personal essays, blog posts, speeches, application responses — not generic writing.

**What it does:**

1. **Scaffolds a folder** — `format-samples/`, `voice-samples/`, `about-me/` for your existing writing; `_drafts/`, `_finals/`, `_meta/` for the skill's working files
2. **Analyzes your voice** — reads your samples, builds a voice profile, shares what it notices with specific quotes and evaluative opinion, then asks you to confirm or correct before drafting
3. **Moves through fixed phases** — ORIENT (voice summary + direction), BRAINSTORM (your raw thoughts, organized), DRAFT (v1 and beyond), REVIEW (iterative loop), FINALIZE (clean output + voice-profile update)
4. **Commits at every phase boundary** — so `git log` is the evolution of the piece, and you can diff v2 against v5 any time
5. **Redlines every revision** — shows strikethrough-old / bold-new inline so you can see the edit without leaving the chat
6. **Collaborates like a peer** — gives real editorial opinions, names weaknesses, doesn't affirm or glaze, stays in scope

**Usage:**

Set up a folder once:

```
I want to start using draft-me for my cover letters in this folder
```

Then drop your existing writing into `format-samples/` and `voice-samples/`, and start a piece:

```
/draft-me a cover letter for Zillow for a Senior Software Engineer role
```

The skill also activates automatically when you open a conversation inside an existing draft-me folder (one with a `.draft-me.json` file) — it'll resume as your drafting collaborator.

**What it produces:**

- **`_drafts/<session-name>.md`** — one file per session, versioned through git, one commit per draft iteration
- **`_finals/<session-name>.md`** — the clean final piece, no frontmatter, no AI markers, ready to copy
- **`_meta/sessions/<session-name>/`** — session notes, brainstorm summary, snapshotted context (JDs, reference docs), running references list
- **`_meta/voice-profile.md`** — the skill's evolving mental model of your voice, updated after every finalized piece

### productionize-me

Takes an existing immature, prototype, or "vibe-coded" codebase and walks you through bringing it to production-grade quality. Audits the code against a tier-calibrated rubric, produces a prioritized plan, lays down concrete scaffolding (CI configs, hooks, secrets handling), retrospectively generates the team-grade design docs / ERDs / ADRs / runbooks the codebase should already have, and writes an enforceable `CLAUDE.md` paired with hooks that prevent regression.

**What it does:**

1. **Calibrates to the right tier** — Tier 1 (personal) through Tier 4 (regulated/safety-critical), so it doesn't over-engineer a weekend script or under-engineer a customer-facing SaaS. Lets you override the recommended tier if you want to aspire higher.
2. **Audits across 14 dimensions** — testing, security, observability, CI/CD, deps, docs, configuration, data handling, performance, reliability, ops readiness, accessibility, licensing, code structure. Findings are tier-aware (no padding with N/A items dressed up as recommendations).
3. **Produces a prioritized plan** — M0 (pre-flight), M1 (launch-ready), M2 (mature), M3+ (beyond MVP). Each item has effort sizing and tradeoffs.
4. **Lays down real scaffolding** — actual files, not just recommendations: `.gitignore`, `.env.example`, `README.md`, CI workflows, pre-commit, `scripts/check.sh` validators, security workflows. Tier-calibrated.
5. **Writes team-grade retrospective design docs** — `ARCHITECTURE.md` with Mermaid diagrams, `DATA_MODEL.md` with ERDs, `SECURITY_PRIVACY.md`, ADRs, runbooks — all in declarative voice with metadata, written like a senior engineer producing canonical team documentation.
6. **Threads audit findings into an enforceable CLAUDE.md** — every P0/M0 finding produces a corresponding rule paired with an enforcement mechanism (pre-commit hook, CI gate, custom validator). Prevents regressions in future sessions, by humans or LLMs.
7. **Three execution paths** — plan-only (you take it from here), in-place modernization on a branch (PR per milestone), or greenfield rebuild (only when the existing code is structurally beyond saving).

**Usage:**

```
/productionize-me
```

In any repo. Or naturally:

```
is this code production grade? we have ~50 daily users and i'm getting nervous
```

```
draft me an architecture diagram and ERD for this repo so i can paste them into the new-hire onboarding doc
```

```
write the design docs we never wrote
```

The skill also activates automatically when you open a conversation inside a codebase that already has a `.productionize-me/` directory — it'll resume where the previous session left off.

**What it produces:**

- **`.productionize-me/`** — diagnostic artifacts (`SUMMARY.md`, `AUDIT.md`, `PLAN.md`, `STATE.md`)
- **`docs/`** — retrospective design docs, organized like the [Hacky Hours](https://github.com/empathetech/hacky-hours-docs) framework: `02-design/`, `adr/`, `runbooks/`, `03-roadmap/`
- **Repo-root scaffolding** — `README.md`, `.gitignore`, `.env.example`, `LICENSE`, `CHANGELOG.md`, plus tier-appropriate CI/hook/security configs
- **`CLAUDE.md`** — durable, enforceable guardrails. Every rule is paired with a hook, CI check, or `scripts/check.sh` step that catches violations
- **`scripts/check.sh`** — runnable repo-specific validator (Tier 2+) that enforces architectural invariants, security rules, and data-handling constraints

### pitch-me

A research-backed startup-pitch generator tuned to the **solo, AI-leveraged, near-zero-cost, near-passive** founder profile. Give it a prompt — broad ("ten startup ideas") or narrow ("five legal-tech ideas with a $5K/mo floor") — and it generates candidate ideas, does live web research on each, then puts them through a 5-persona devil's-advocate panel. You get back only the pitches that earned a strong score, each with a deck, a one-pager, a scorecard, and a red-team objections doc.

**What it does:**

1. **Frames the brief** — fixes scope, revenue floor, founder constraints, exclusions, and pass threshold (defaults: solo + day-job, $0 budget, ≤10 hr/week, no hires, no physical product, $1K/mo floor, avg ≥8/10 with no persona <6)
2. **Generates a candidate pool** — 2× the requested N, biased toward boring buyers, AI-as-delivery (not AI-as-marketing), distribution paths a solo founder can actually walk
3. **Researches each survivor live** — TAM/SAM/SOM with citations, real customer quotes from Reddit/HN/IndieHackers/G2, competitor pricing, distribution evidence, regulatory/platform/model risk, unit-economics math
4. **Stress-tests with a 5-persona panel** — Indie-Hacker Operator, Pattern-Matching Seed VC, Unit-Economics Hawk, Distribution Skeptic, Contrarian Devil's Advocate. Each scores, names the strongest objection, and proposes one +1 change
5. **Iterates** — applies +1 changes for near-misses; kills ideas that fail outright; keeps generating from the pool until N pitches pass or the 5-hour wall-clock budget is hit
6. **Produces deliverables** — HTML deck, Markdown one-pager, scorecard, red-team doc, plus a top-level index sorted strongest-first

**Usage:**

```
/pitch-me
```

Or naturally:

```
pitch me 5 startups in legal-tech I could build solo on nights and weekends
```

```
give me 10 micro-SaaS ideas where AI does most of the work
```

```
what could a solo founder with $0 and a day job actually ship and monetize?
```

**What it produces:**

- **`./pitches/_index.md`** — all pitches sorted by score with one-line theses, plus the kill list of what didn't make it and why
- **`./pitches/<slug>/deck.html`** — self-contained HTML pitch deck with arrow-key nav, no external assets
- **`./pitches/<slug>/one-pager.md`** — exec doc that stands alone (buyer, product, wedge, market, pricing, distribution, roadmap, risks)
- **`./pitches/<slug>/scorecard.md`** — 5-persona scores with iteration history
- **`./pitches/<slug>/red-team.md`** — top objections with answers, plus the "what would make this idea wrong" stress-test
- **`./pitches/<slug>/research.md`** — full research note with link-cited TAM, competitors, customer evidence, unit economics

### without-ai

Takes a prompt — the kind a person would normally throw at an LLM — and produces a comprehensive plan for an **AI-free (or AI-trending-to-zero) infrastructure** that answers it durably. Runnable on local hardware, build­able with AI as a one-time bootstrap, maintainable by a solo person. Optionally scaffolds the actual repo and uses it to answer the original prompt.

The premise: an LLM answer is a transient artifact. For some prompts ("name my band") that's fine. For many — *"build me a clone of Magic: The Gathering"*, *"plan my week given everything you know about me"*, *"triage this support email"* — the prompt is a brittle stand-in for infrastructure the user actually needs. This skill identifies those cases, abstracts upward (MTG → card-game engine; weekly planner → personal data layer + planner; LLM-on-each-ticket → rules engine + reply-template library), designs the infrastructure, and optionally builds it.

**What it does:**

1. **Restates the prompt and sketches the AI answer** — what an LLM would actually generate, what feels impressive at 30 seconds and breaks down on the 30th use
2. **Categorizes the brittleness** — which classes of prompts (asset-generation, repeated-pattern, stateful, deterministic-rules, personal-context, creative-tool, search-as-Q&A) does this fall into, and is the without-ai treatment even worth it
3. **Abstracts upward** — frames the *actual* target one level above the literal prompt (MTG → card battler engine; "track my workouts" → workout database with heuristics; "answer customer questions" → knowledge base + retrieval)
4. **Designs the architecture** — component diagram, data-flow diagram, deployment diagram, with each component named and described. Local-hostable, solo-maintainable
5. **Plots the AI-trending-to-zero curve** — what role AI plays per phase, with steady-state at zero or near-zero
6. **Designs the asset-creation tools** — when the prompt implicates art / copy / level layouts / lesson plans / cards, the without-ai answer is almost always *an editor or generator the user uses themselves*, not "we'll have AI make it"
7. **Roadmap calibrated to a solo builder** — phased, with honest evening/weekend estimates and per-phase AI dependency tracking
8. **Handoff packets** — copy-pasteable prompts for `/teach-me` (curriculum to learn the skills you need), `/productionize-me` (vibe-code prompt to build the infra, plus an audit prompt for after), `/hacky-hours` (recurring evening project framing)
9. **Optional Phase 2 — build and prove** — scaffolds the actual repo, builds the smallest vertical slice that exercises every component, uses it to answer the original prompt, writes human-readable docs (README / ARCHITECTURE / GETTING_STARTED / LIMITATIONS) so a solo person can take over

**Usage:**

```
/without-ai build me a clone of Magic: The Gathering
```

Or naturally:

```
i keep dumping my whole life into chatgpt every monday morning to get help planning my week. what would the without-ai version of this look like?
```

```
i'm spending $80/mo on Claude API to triage support emails. what would a self-owned version of this look like?
```

```
what's the long-term version of asking an LLM to generate D&D dungeons for me?
```

**What it produces** (per run, under `./without-ai/<run-id>/`):

- **`_overview.md` + `_overview.html`** — the authoritative plan with embedded Mermaid diagrams (component, data-flow, deployment, AI-dependency timeline). HTML is a standalone rendered version suitable to share
- **`architecture/<component>.md`** — per-component design docs (data model, engine, editor, deployment, etc.)
- **`roadmap.md`** — phased plan with explicit AI-dependency-at-end-of-phase tracking
- **`ai-vs-without-ai.md`** — side-by-side AI-fork-vs-without-ai-fork analysis, plus a "why this category of prompt is brittle to put in front of an LLM" generalization that's reusable across the next ten similar prompts
- **`benefits.md`** — honest gains and tradeoffs (the user gives up speed-to-first-answer; they gain ownership, durability, $0 running cost, no rate limits, no vendor lock-in)
- **`handoff/teach-me.md` / `handoff/productionize-me.md` / `handoff/hacky-hours.md`** — pre-filled, copy-pasteable handoff packets for the next skill in the chain
- **(optional Phase 2) `repo/`** — scaffolded repo with the smallest vertical slice that exercises every component, plus `PROOF.md` showing the system answering the original prompt and human-readable docs for a solo person to keep building

## Installation

Claude Code discovers skills one level deep in `~/.claude/skills/`. Since this repo contains multiple skills in subdirectories, you clone it once and then symlink each skill into the right place.

**Personal install (available in all your projects):**

```bash
# 1. Clone the repo
git clone https://github.com/bjamba/bjamba-skills.git ~/.claude/skills/bjamba-skills

# 2. Symlink each skill into the Claude Code skills directory
ln -sf ~/.claude/skills/bjamba-skills/teach-me ~/.claude/skills/teach-me
ln -sf ~/.claude/skills/bjamba-skills/continuity-check ~/.claude/skills/continuity-check
ln -sf ~/.claude/skills/bjamba-skills/draft-me ~/.claude/skills/draft-me
ln -sf ~/.claude/skills/bjamba-skills/productionize-me ~/.claude/skills/productionize-me
ln -sf ~/.claude/skills/bjamba-skills/pitch-me ~/.claude/skills/pitch-me
ln -sf ~/.claude/skills/bjamba-skills/without-ai ~/.claude/skills/without-ai
```

Restart your Claude Code session. Skills will be available by their slash command (e.g. `/teach-me`, `/draft-me`, `/continuity-check`) or will activate automatically based on context.

**Updating:**

```bash
cd ~/.claude/skills/bjamba-skills && git pull
```

No re-linking needed — the symlinks automatically point to the updated files.

**Adding a newly released skill:**

When a new skill is added to this repo, pull and add one new symlink:

```bash
cd ~/.claude/skills/bjamba-skills && git pull
ln -sf ~/.claude/skills/bjamba-skills/new-skill-name ~/.claude/skills/new-skill-name
```

**Per-project install (available only in a specific project):**

```bash
git clone https://github.com/bjamba/bjamba-skills.git .claude/skills/bjamba-skills
ln -sf .claude/skills/bjamba-skills/teach-me .claude/skills/teach-me
ln -sf .claude/skills/bjamba-skills/continuity-check .claude/skills/continuity-check
ln -sf .claude/skills/bjamba-skills/draft-me .claude/skills/draft-me
ln -sf .claude/skills/bjamba-skills/productionize-me .claude/skills/productionize-me
ln -sf .claude/skills/bjamba-skills/pitch-me .claude/skills/pitch-me
ln -sf .claude/skills/bjamba-skills/without-ai .claude/skills/without-ai
```

## Structure

```
bjamba-skills/
├── README.md
├── teach-me/
│   ├── SKILL.md
│   ├── references/
│   └── evals/
├── continuity-check/
│   ├── SKILL.md
│   ├── scripts/
│   ├── references/
│   ├── assets/
│   └── evals/
├── draft-me/
│   ├── SKILL.md
│   ├── scripts/
│   ├── references/
│   └── evals/
├── productionize-me/
│   ├── SKILL.md
│   ├── references/
│   └── evals/
├── pitch-me/
│   ├── SKILL.md
│   ├── references/
│   └── assets/
└── without-ai/
    ├── SKILL.md
    ├── references/
    ├── assets/
    └── evals/
```
