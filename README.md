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
└── productionize-me/
    ├── SKILL.md
    ├── references/
    └── evals/
```

## Tested skills

**teach-me** has been tested with:

- Wine & cheese pairing (non-technical learner)
- ML classification (junior data scientist)
- Modern world history (engineer filling knowledge gaps)
- Rust programming (experienced Go/C++ developer)
- Active listening (personal development / soft skill)

**draft-me** has been tested with:

- Fresh folder scaffold (cover-letters setup from scratch)
- Full drafting session on a configured folder (cover letter for a senior-engineer role)
- Mid-session review feedback integration (redline + clean v3 from reviewer comments)
