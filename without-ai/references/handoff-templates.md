# Handoff packet templates

The skill produces three handoff files in `./without-ai/<run-id>/handoff/`. Each is a self-contained, copy-pasteable prompt the user can drop into the named skill without re-explaining anything. Pre-fill them with the run's specifics — don't leave placeholders.

---

## `handoff/teach-me.md`

Goal: turn the architecture into a curriculum that teaches the user every skill they need to actually build it.

```markdown
/teach-me

I want to learn the skills I need to build the following infrastructure as a solo person, starting from where I am today. Here's the architecture I'm planning to build:

**Project:** <one-line description, e.g. "a card-battle game engine">

**Original prompt I was going to ask an LLM:** <user's verbatim prompt>

**What I'm building instead (the without-ai version):** <one-paragraph framing from `_overview.md`>

**Architecture components I need to learn how to build:**

<for each component in architecture/, list:>
- <component name>: <one sentence on what it does> — I need to learn <list the underlying skills, e.g. "DSL design, parser combinators, basic interpreter implementation">

**My current background:** <fill in from intake — be honest about what the user already knows. If the skill didn't capture this, leave a single line "[user: please describe your current background]" and tell the user in chat to fill it in before pasting]>

**Constraints:**
- Solo builder, evenings and weekends
- ~<N> hours per week available for learning + building
- Local-only / on-prem deployment target — no cloud-native skills needed
- AI dependency in the final system: <target from `_overview.md`>

**Output I want from /teach-me:**
- A learning path ordered so each module unblocks something I can actually build
- Each module pinned to a concrete artifact in my project (not just abstract "learn DSLs" — "learn enough DSL design to build the card-rules engine in this project")
- Practice projects that *are* the project (build the real thing, not toy versions)
- Honest time estimates

The full architecture and roadmap are in `./without-ai/<run-id>/_overview.md`. Read that first if you can; it has the diagrams.
```

Pre-fill aggressively. The user shouldn't need to do anything except paste it.

---

## `handoff/productionize-me.md`

Goal: a vibe-coding prompt that *builds* the proposed infra in a fresh repo. The output of running this prompt is what `/productionize-me` is then designed to audit and harden.

There are two flavors. Generate both in the file, with a header explaining when to use which.

```markdown
# productionize-me handoff

Two prompts below. Use **A** if you haven't built the infra yet — paste it into a fresh Claude Code session in an empty repo. Use **B** *after* you've built (or generated) the infra and want it audited.

---

## A. Build prompt (paste into a fresh repo)

I want you to build the following infrastructure end-to-end in this repo. Treat this as an MVP that exercises every component of the architecture, *not* a finished product. The roadmap is for filling in the rest.

**Project:** <one-line description>

**Original user prompt this infrastructure replaces:** <verbatim>

**Why this is being built as infrastructure rather than answered with an LLM:** <one paragraph from `ai-vs-without-ai.md`>

**Architecture (full overview at `<path>/_overview.md` if you have access; otherwise summarized below):**

<for each component:>
- **<component>**: <responsibility, key file/folder, public interface, dependencies>

**Hard constraints for the build:**
- AI must not be load-bearing in the running system. AI is allowed at build time and as an explicit, optional bootstrap; the running system must function with no API keys.
- Local-hostable (laptop / single VPS / Raspberry Pi). No cloud-native dependencies.
- Solo-maintainable. One person should be able to read all the source in a weekend.
- Human-readable file formats wherever the user is editing data.
- Deterministic where possible (rules, generators with seeds, etc.).

**Required deliverables:**
1. Working code for each component, wired together.
2. A `PROOF.md` that shows the system being used to answer the original prompt — exact command, exact output, short reflection.
3. `README.md` (what + why + 3-command quickstart).
4. `ARCHITECTURE.md` (diagrams + file pointers).
5. `GETTING_STARTED.md` (tutorial: clone → run → edit one piece of content → re-run).
6. `LIMITATIONS.md` (honest list of what's stubbed, hardcoded, or skipped).
7. Per-component `README.md` in each major directory.

Roadmap for what's *next* (out of scope for this build) is in `<path>/roadmap.md`.

Start by reading the overview, then propose the file/folder layout before writing code. Confirm with me before generating large amounts of code.

---

## B. Audit prompt (after the infra exists)

/productionize-me

This repo was generated from a /without-ai plan. The plan and roadmap are at `<path>/_overview.md` and `<path>/roadmap.md`. The proof-of-concept run is in `PROOF.md`. Limitations the build acknowledged are in `LIMITATIONS.md`.

Audit at the appropriate production tier for: <fill in: solo-tool / friends-and-family / public-side-project / commercial-SaaS — pick from the user's intake>.

Areas I most want a pass on:
- AI dependency: confirm nothing snuck back in as load-bearing.
- The asset editors / content tools — is the file format honest, the editing flow ergonomic?
- The DSL / rules engine — is the grammar minimal, the interpreter testable?
- Solo-maintainability — could one person keep this running?

Use your standard rubric otherwise. Don't over-engineer past the tier.
```

---

## `handoff/hacky-hours.md`

Goal: scope the build as a recurring evening project, with a structured first session.

```markdown
/hacky-hours

I'm going to build the following project on evenings + weekends. Help me scope this as a recurring hacky-hours commitment.

**Project:** <one-line description>

**Original LLM prompt this replaces:** <verbatim>

**The without-ai approach (one paragraph):** <from `_overview.md`>

**Phases (from `roadmap.md`):**
<for each phase, one line: scope + estimated evenings/weekends>

**My realistic available time:** <from intake, or "[user: please fill in]">

**What I'd like out of /hacky-hours:**
- A first-session plan that gets to *something running* by the end of the evening — even if it's the smallest possible vertical slice.
- A check-in cadence (weekly? bi-weekly?) and what artifacts to bring to each.
- Triggers for when to swap a phase order (e.g., "if the editor is more painful than expected, go straight to the DSL first").
- A cut list — if I'm running out of evenings, what gets dropped from each phase without breaking the architecture.

The full architecture is at `<path>/_overview.md`. The asset-tool / editor designs are in `<path>/architecture/`.

I want this to feel like a project, not a marathon. Help me find the rhythm.
```

---

## What to substitute in

For every handoff file you produce, replace these placeholders with concrete content from this run:

| Placeholder | Source |
|---|---|
| `<one-line description>` | First line of `_overview.md` |
| `<user's verbatim prompt>` | `_brief.md` |
| `<one-paragraph framing>` | "What you're actually building" section in `_overview.md` |
| `<architecture components>` | The component list from `_overview.md` (Step 4) |
| `<roadmap phases>` | Each phase from `roadmap.md` |
| `<AI dependency target>` | The steady-state row in the AI-trending-to-zero table |
| `<production tier>` | From intake, default "solo-tool" if not specified |
| `<path>` | `./without-ai/<run-id>` |

Don't leave any `<...>` placeholder unfilled in the handoff files. If something genuinely wasn't captured at intake, leave a single bracketed line `[user: please fill in <thing>]` and call it out in your wrap-up message — the user should never paste a packet and immediately have to add their own context.

---

## Style of the handoff prose

- Voice the prompt as if the user were typing it. First person. Direct.
- Don't be cute. The receiving skill doesn't need flavor; it needs context.
- Cite file paths when relevant — the receiving skill might be running in the same workspace and can read the artifacts.
- If a constraint is non-obvious or hard-won (e.g., "no JavaScript build step", "must run offline"), put it in bold. The constraint *is* the value.
