# Deliverable Structure (v2)

For each of the N pitches (pass or fail), produce the full deliverable set. The slug is a 2–4-word kebab-case name derived from the pitch (e.g., `permit-prep-copilot`, `niche-rfp-autodrafter`).

```
./pitches/<run-id>/<slug>/
├── one-pager.md              # executive summary
├── deck.html                 # visual deck (filled from assets/deck-template.html)
├── research.md               # market research note (Phase 3 output)
├── scorecard.md              # per-investor + composite scoring (Phase 4 output)
├── red-team.md               # strongest objections + answers
├── pitch-meeting/
│   ├── transcript.md         # voice-render-ready full back-and-forth
│   ├── transcript.json       # structured turns (for visual novel + audio export)
│   ├── visual-novel.html     # Shark-Tank-style episode replay (with Web Speech API)
│   ├── pre-pitch-survey.md   # founder + investor perceptions BEFORE pitch
│   ├── post-pitch-survey.md  # same perceptions AFTER pitch
│   └── perception-gap.md     # analysis of how perceptions shifted
├── meeting-summary.md        # exec summary of the meeting (for skim-readers)
├── investor-feedback.md      # per-investor written feedback to founder
├── founder-reflection.md     # solo founder's response/reflection
├── handoff/
│   ├── hacky-hours.md        # ready-to-paste prompt for /hacky-hours
│   ├── teach-me.md           # ready-to-paste prompt for /teach-me
│   └── productionize-me.md   # ready-to-paste prompt for /productionize-me
└── meta.json                 # structured pitch metadata for cross-skill use
```

Run-level files at `./pitches/<run-id>/`:

```
./pitches/<run-id>/
├── _brief.md                 # the intake brief (Phase 0 output)
├── _investor-panel.md        # the panel for this run with profiles + radar
├── _panel-radar.html         # SVG radar visualization of panel biases
├── _index.md                 # all N pitches ranked, with one-line theses + decision
├── season-recap.html         # Shark-Tank-/Dragons'-Den-style season landing page
├── _post-mortem.md           # cross-cutting observations: what landed, what bombed, why
└── audio-rendering.md        # how to export transcripts to audio
```

The `<run-id>` is chosen during Phase 0 intake (default: today's ISO date `YYYY-MM-DD`; override for parallel sessions). All cross-links inside the run directory are relative — moving or renaming the run-id root is safe.

There is no `_killed.md` in v2. Failed pitches are first-class artifacts in their own slug directories.

---

## one-pager.md

The executive doc. Read by panelists, by the user, and (later) potentially by an actual investor or partner. Should stand alone — someone reading only this should understand the entire pitch.

Structure:

```markdown
# {Pitch name}

**One-line**: {12-word thesis. The buyer + the wedge + the mechanism.}

**Score**: {avg}/10 in {commitment mode} mode  •  Decisions: {N INVEST / N INTERESTED / N SOFT-PASS / N PASS}  •  Pattern: {idea-pattern letter}  •  Style: {bold | niche | laser | solid}  •  Slug: {slug}

## The buyer
- **Who**: {specific job title or persona}
- **Where**: {company size band, industry, geography if relevant}
- **What they're doing today**: {workaround, current spend, current pain}
- **Why they'll pay**: {value-anchor — hourly rate, alternative cost, opportunity cost}

## The product
- **v1 scope** (shippable in {hours} consistent with commitment mode): {bullet the v1 surface}
- **What AI does**: {the specific work AI performs that wasn't tractable before}
- **What the founder does**: {ongoing weekly time, kind of work}

## The wedge
{1 paragraph: why this beachhead, what's specifically narrow, why incumbents won't follow}

## Market
- **TAM**: {number} ({citation})
- **SAM**: {number} ({reasoning})
- **SOM**: {revenue at 1% / 5% / 10% capture}
- **Why now**: {the specific unlock with citable trigger}

## Pricing & unit economics
- **Price**: ${X}/{unit} (anchored to {comp} which charges ${Y})
- **Cost-to-serve**: ${Z}/customer/mo (math in research.md)
- **Gross margin**: {%}
- **Breakeven**: {N customers}

## Distribution
- **Channel #1**: {specific channel + sub-channel + first move}
- **Channel #2**: {same}
- **First 10 customers**: {concrete plan, named source}
- **First 100**: {concrete plan, time/cost estimate}

## Roadmap
- **Week 1–2**: ship v1 ({2–3 bullets})
- **Week 3–4**: first paying customer; iterate on the {wedge}
- **Month 2–3**: scale channel #1; add the lowest-effort retention mechanic
- **Month 4–6**: revenue target {$X MRR}; decide kill / scale / sell
- **Kill criteria**: {if not at $X MRR by month Y, walk away}

## Risks & mitigations
{3–5 bullets, each with a mitigation. The big ones the panel surfaced.}

## Why this fits {commitment mode}
{1 paragraph: how the constraints (per the chosen mode) actually map to this specific business.}

## If you'd swap modes
{1 short paragraph: at what other commitment mode does this idea work better, and why? Reference the panel's "best-fit mode" votes.}
```

Keep it under 800 words. Specificity beats completeness.

---

## deck.html

Self-contained HTML deck. The deck is the visual version of the one-pager — designed for skimming and screen-sharing, not for being the source of truth. **The deck is not the pitch — the meeting transcript is the pitch.** The deck is just visual support.

Slide structure (10–12 slides):

1. **Title** — pitch name, one-line thesis.
2. **The customer moment** (per `references/storytelling-lessons.md`) — open with a real human in real friction.
3. **The buyer & the pain** — concrete: who, what they're doing today, cost of pain.
4. **Why now** — the specific unlock with citable trigger.
5. **The product** — v1 surface, what AI does, what the founder does.
6. **The wedge** — competitive map.
7. **Market** — TAM / SAM / SOM with citations.
8. **Pricing & unit economics**.
9. **Distribution** — channel #1, channel #2, first-10 plan.
10. **Roadmap** — milestones with kill criteria.
11. **Risks & answers** — top 3.
12. **Close** — what would make me build this / what's needed.

Keep slide text terse — bullets, not paragraphs. The one-pager has the prose. The deck is for skim.

The HTML template at `assets/deck-template.html` is a single-file scaffold with inlined CSS and keyboard nav (arrow keys, space). Fill in the slides; don't reinvent the styling.

---

## scorecard.md

The 7-investor scoring history with commitment-mode awareness.

```markdown
# Scorecard — {Pitch name}

**Mode under evaluation**: {commitment mode}
**Composite score (chosen mode)**: {X.X}/10
**Idea soundness (mode-agnostic, Skeptic)**: {X.X}/10
**Decision spread**: {N INVEST / N INTERESTED / N SOFT-PASS / N PASS}
**Best-fit mode (panel consensus)**: {mode if different from chosen}

## Per-investor scores

| Investor | Chosen-mode score | Best-fit mode | Soundness | Decision |
|---|---|---|---|---|
| Bootstrapper | X | {mode} | X | {DECISION} |
| Operator | X | {mode} | X | {DECISION} |
| Seed VC | X | {mode} | X | {DECISION} |
| Growth VC | X | {mode} | X | {DECISION} |
| Skeptic | X | {mode} | X | {DECISION} |
| Domain Expert ({named composite}) | X | {mode} | X | {DECISION} |
| Customer ({named persona}) | X | {mode} | X | {DECISION} |

## Per-investor rationale (one line each)

- **Bootstrapper**: {one sentence explaining the score}
- ... (repeat for each)

## Strongest pro arguments
{Bullet list of the panel's top 3 reasons this could work, with attribution.}

## Strongest con arguments
{Bullet list of the panel's top 3 reasons this could fail, with attribution.}

## "+1 change" suggestions
{Each investor's single concrete change that would move their score up. Useful even for failed pitches as future-pivot fodder.}

## Calibration check
{Confirm that the score distribution matches `references/scoring-calibration.md` for the mode. If too tight or too uniform, recalibrate.}
```

---

## red-team.md

```markdown
# Red Team — {Pitch name}

## Top 5 objections, answered

### Objection 1 — {one-line summary}
**Raised by**: {investor}
**Why it's serious**: {1-2 sentences}
**Answer**: {the response — what's true, what's a calculated risk, what's a plan to address}

### Objection 2 — {…}

(repeat for top 5)

## Objections we don't have a great answer for

{Be honest. The pitch is stronger if it acknowledges its weakest assumptions, not weaker. List 1–3 things that are still genuinely uncertain.}

## What would make this idea wrong?

{1 paragraph stress-test: what specific thing, if true, would kill this business? How would we find out before spending real time/money on it?}
```

---

## meeting-summary.md

A 200–400 word skim-friendly summary of the meeting. Useful for users who don't want to read the full transcript.

```markdown
# Meeting Summary — {Pitch name}

**Format**: 60-min simulated pitch meeting, {commitment mode} evaluation.
**Panel**: 5 fixed investors + Domain Expert ({composite}) + Customer ({persona}).
**Outcome**: {decision spread}; composite {X.X}/10.

## Top 3 things that landed
1. {…}
2. {…}
3. {…}

## Top 3 things that fell flat
1. {…}
2. {…}
3. {…}

## Key disagreement on the panel
{1 paragraph: which investors disagreed and why. The disagreements are the most informative parts of the meeting.}

## What the founder learned (from founder-reflection.md)
{1 sentence summary.}
```

---

## investor-feedback.md

Per-investor written feedback to the founder, in the voice of each investor. Each investor writes a short paragraph (3–6 sentences) addressed to the founder. This is what the founder takes home from the meeting and re-reads.

---

## founder-reflection.md

The founder's honest reflection after the meeting:

```markdown
# Founder Reflection — {Pitch name}

## What I thought going in
{Pre-pitch confidence level. Quote pre-pitch survey scores.}

## What surprised me
{One or two things investors raised that hadn't been on the founder's mind.}

## What I'd change if I pitched again
{Two or three concrete tweaks.}

## Decision
{KEEP-PUSHING / RECONSIDER / PIVOT / KILL}

## Reasoning
{1 paragraph explaining the decision.}
```

---

## meta.json

Structured metadata for cross-skill use:

```json
{
  "slug": "trust-ledger-desktop",
  "name": "TrustLedger Desktop",
  "one_line": "Desktop IOLTA 3-way reconciliation that runs on the firm's own network",
  "commitment_mode": "passive-income",
  "pitch_style": "solid",
  "panel_composite_score": 7.4,
  "skeptic_soundness_score": 7.0,
  "decisions": {"INVEST": 1, "INTERESTED": 3, "SOFT_PASS": 2, "PASS": 1},
  "best_fit_mode_consensus": "passive-income",
  "founder_decision": "KEEP-PUSHING",
  "tam_estimate_usd": 100000000,
  "som_at_5pct_usd": 1800000,
  "v1_hours_estimate": 80,
  "ongoing_hours_per_week": 5,
  "monthly_fixed_cost_usd": 200,
  "channel_primary": "State bar IOLTA boards",
  "regulatory_flags": ["state-bar compliance"],
  "platform_dependencies": [],
  "tags": ["legaltech", "anti-subscription", "boring-b2b"]
}
```

---

## _index.md

```markdown
# Pitch Run — {date}, {one-line scope from _brief.md}

**Mode**: {commitment mode}  •  **Style mix**: {bold % / niche % / laser % / solid %}  •  **Panel**: 5 fixed + {Domain Expert composite} + {Customer persona}

## All N pitches (ranked by composite score)

| Rank | Pitch | Score | Decision spread | Style | One-line |
|---|---|---|---|---|---|
| 1 | [{name}](./{slug}/one-pager.md) ([📺 episode](./{slug}/pitch-meeting/visual-novel.html)) | X.X | 2I/3?/2-/0× | solid | {12 words} |
| 2 | … |

(Sort all N strongest-first. Failures stay in the table.)

## Quick takeaways from `_post-mortem.md`
{2–3 bullets surfacing the season's most interesting findings.}

## How to consume this run

- **Browse the season**: [season-recap.html](./season-recap.html)
- **Listen to a pitch**: open any episode's `pitch-meeting/visual-novel.html`, click ▶ (uses Web Speech API)
- **Render to studio audio**: see [audio-rendering.md](./audio-rendering.md)
- **Act on a pitch**: each pitch's `handoff/` directory has copy-paste prompts for `/hacky-hours`, `/teach-me`, `/productionize-me`.
```

---

## _post-mortem.md

The most important run-level document. The user reads this after consuming the season; it's where the lessons live.

```markdown
# Post-Mortem — {date}

## What this run produced
{1 paragraph: counts, modes, scoring distribution.}

## Highest-conviction pitches (3)
{1 paragraph each on the top 3, with the panel's strongest-pro and strongest-con arguments.}

## Most informative failures (2-3)
{1 paragraph each on the most-instructive failed pitches, what we learned from why they failed.}

## Cross-cutting findings
- **Pattern A** (e.g., "every passive-income pitch with a forced-compliance audience scored well"): {evidence}
- **Pattern B** (e.g., "every bold pitch with a 2-yr horizon got Skeptic vetoes"): {evidence}
- {3–5 patterns total}

## What surprised the panel
{Things the panel didn't expect — moments where the cold opinion shifted dramatically post-pitch, in either direction.}

## What didn't work
{Honest accounting: which research was thin, which buyer cohorts couldn't be validated, which channels couldn't be confirmed.}

## Recommended next step
{If the user is going to act on one pitch, which one and why. Specifically reference `handoff/<skill>.md`.}
```

The post-mortem is what the user reads with their morning coffee. Make it readable.
