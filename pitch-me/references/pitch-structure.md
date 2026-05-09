# Deliverable Structure

For each pitch that passes, produce four files in `./pitches/<slug>/`. The slug is a 2–4-word kebab-case name derived from the pitch (e.g., `permit-prep-copilot`, `niche-rfp-autodrafter`).

```
./pitches/<slug>/
├── deck.html         # the visual pitch
├── one-pager.md      # the executive summary
├── scorecard.md      # 5-persona scoring + iteration history
└── red-team.md       # objections + answers
```

Plus the run-level files at `./pitches/`:

```
./pitches/
├── _brief.md         # the run brief from Phase 1
└── _index.md         # all pitches sorted by score, with one-line theses
```

(Note: research.md from Phase 3 also lives in each pitch folder, per `research-checklist.md`.)

---

## one-pager.md

The executive doc. Read by the personas, by the user, and (later) potentially by an actual investor or partner. Should stand alone — someone reading only this should understand the entire pitch.

Use this structure:

```markdown
# {Pitch name}

**One-line**: {12-word thesis. The buyer + the wedge + the mechanism.}

**Score**: {avg}/10  (panel: {p1}/{p2}/{p3}/{p4}/{p5})  •  Pattern: {A/B/C/D/E/F/G}  •  Slug: {slug}

## The buyer
- **Who**: {specific job title or persona}
- **Where**: {company size band, industry, geography if relevant}
- **What they're doing today**: {workaround, current spend, current pain}
- **Why they'll pay**: {the value-anchor — hourly rate, alternative cost, opportunity cost}

## The product
- **v1 scope** (shippable in ≤ 80 hours): {bullet the v1 surface}
- **What AI does**: {the specific work AI performs that wasn't tractable before}
- **What the founder does**: {ongoing weekly time, kind of work}

## The wedge
{1 paragraph: why this beachhead, what's specifically narrow, why incumbents won't follow}

## Market
- **TAM**: {number} ({citation})
- **SAM**: {number} ({reasoning})
- **SOM**: {revenue at 1% / 5% / 10% capture}
- **Why now**: {the specific unlock}

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

## Why this fits a solo + AI founder
{1 paragraph: how the constraints (10 hr/week, $0 budget, full-time job) actually map to this specific business.}
```

Keep it under 800 words. Specificity beats completeness.

---

## deck.html

A self-contained HTML deck (no external assets, no JS frameworks needed beyond what's in `assets/deck-template.html`). The deck is the pretty version of the one-pager — designed for skimming and screensharing, not for being the source of truth.

Use the slide structure below. Each `<section class="slide">` in the template is one slide. Aim for **10–12 slides total**.

1. **Title** — pitch name, one-line thesis, your name/handle.
2. **The buyer & the pain** — who, what they're doing today, the cost in time/money/lost-revenue.
3. **Why now** — the specific unlock (AI capability, cost curve, regulatory, behavior shift).
4. **The product** — v1 surface, what AI does, what the founder does.
5. **The wedge** — why this narrow beachhead, with the competitive map (incumbents, indie comps, the gap).
6. **Market** — TAM / SAM / SOM with the numbers and citations as small footnotes.
7. **Pricing & unit economics** — price, cost-to-serve, gross margin, breakeven.
8. **Distribution** — channel #1, channel #2, first-10 plan, first-100 plan.
9. **Roadmap** — week-by-month milestones, with the kill criteria.
10. **Risks & answers** — top 3 risks with one-line mitigations.
11. **The ask / the close** — for solo founders this is "what would make me build this", for investor framing it's "what we'd need to raise / partner on". Either is fine.
12. **Appendix (optional)** — citations, math, alternative scenarios.

Keep slide text terse — bullets, not paragraphs. The one-pager has the prose. The deck is for skim.

The HTML template at `assets/deck-template.html` is a single-file scaffold with inlined CSS and keyboard nav (arrow keys, space). Fill in the slides; don't reinvent the styling.

---

## scorecard.md

The 5-persona scoring history. This is where the panel's verdicts live, with enough context for the user (or future-you) to understand *why* each score landed where it did.

```markdown
# Scorecard — {Pitch name}

**Final**: avg {X}/10  •  min {Y}/10  •  result: PASS / FAIL  •  iterations: {N}

## Iteration {N} (final)

| Persona | Score | Strongest pass reason | Strongest invest reason | +1 change |
|---|---|---|---|---|
| Indie-Hacker Operator | X | … | … | … |
| Pattern-Matching Seed VC | X | … | … | … |
| Unit-Economics Hawk | X | … | … | … |
| Distribution Skeptic | X | … | … | … |
| Contrarian Devil's Advocate | X | … | … | … |

**Aggregate**: avg {X}/10, min {Y}/10. {Pass/Fail reasoning.}

## Iteration history

### Iteration 1
- Avg: X/10, min Y/10
- Killed by: {persona, reason} OR Approved with changes:
- Changes applied for next iteration: {bullet list}

### Iteration 2 (if applicable)
- …
```

Show the iteration arc honestly. If a pitch got better because of a specific persona's `+1 change`, that's the most useful signal in the whole document.

---

## red-team.md

The objections-and-answers doc. This is where the strongest critiques the panel raised — and any obvious ones the panel missed — get explicitly answered. This is the doc that, if shown to a real investor, pre-empts the conversation that would otherwise happen.

```markdown
# Red Team — {Pitch name}

## Top 5 objections, answered

### Objection 1 — {one-line summary}
**Raised by**: {persona}
**Why it's serious**: {1-2 sentences}
**Answer**: {the response — what's true, what's a calculated risk, what's a plan to address}

### Objection 2 — {…}

(repeat for top 5)

## Objections we don't have a great answer for

{Be honest. The pitch is stronger if it acknowledges its weakest assumptions, not weaker. List 1–3 things that are still genuinely uncertain.}

## What would make this idea wrong?

{1 paragraph stress-test: what specific thing, if true, would kill this business? How would we find out before spending real time/money on it?}
```

The red-team doc isn't optional — it's the difference between a pitch that survives a real conversation and one that crumbles under the first hard question.

---

## _index.md (run-level)

```markdown
# Pitch Run — {date}, {brief one-line of the run scope}

| Rank | Pitch | Score | Pattern | One-line |
|---|---|---|---|---|
| 1 | [{name}](./{slug}/one-pager.md) | X/10 | A | {12 words} |
| 2 | … |

## Brief
{paste of _brief.md}

## Pitches that didn't make it
- {slug}: killed at {phase} because {one-line reason}
- {slug}: killed at {phase} because {one-line reason}

## Notes
{Any cross-cutting observations from the run — patterns that came up, niches that look unexpectedly strong, etc.}
```

The "didn't make it" list matters. It tells the user what was tried and why it failed, which both builds trust and saves them from rediscovering the same dead ends.
