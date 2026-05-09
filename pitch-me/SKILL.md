---
name: pitch-me
description: Generates research-backed startup pitches for solo, AI-assisted, near-zero-cost ventures, then stress-tests each one against a panel of skeptical VC/operator personas and produces a scorecard plus an HTML deck and one-pager. Use whenever the user asks for startup ideas, side-hustle ideas, indie-hacker ideas, "things I could build with AI", passive income concepts, AI SaaS pitches, micro-SaaS opportunities, niche revenue plays, or wants ideas vetted/scored/critiqued by simulated investors. Triggers on phrases like "/pitch-me", "pitch me N startups", "give me startup ideas", "what could I build solo with AI", "evaluate this startup idea", "make me a pitch deck", "score this idea like a VC". Default behavior assumes solo founder with full-time job, $0 budget, no hires, no physical product, AI tools only — unless the user specifies otherwise.
---

# pitch-me

A skill for generating, researching, and stress-testing startup pitches for the **solo, AI-leveraged, near-zero-cost, near-passive** founder profile.

The output of one run is N **fully-researched, investor-vetted pitches**, each with:

- An HTML pitch deck
- A one-pager (Markdown)
- A scorecard (Markdown) with per-persona ratings and rationale
- A feedback / red-team doc (Markdown) with the strongest objections and how the pitch answers them

Every claim that touches market size, competitor landscape, pricing benchmark, or regulatory constraint must be **link-cited** to a real source the skill found via web research.

## Default parameters

If the user doesn't specify, assume:

| Parameter | Default |
|---|---|
| `N` (number of pitches) | 10 |
| Industry / domain | Open — search broadly across software, content, services, marketplaces, info products |
| Revenue floor | ≥ $1K/mo net ARR within 12 months **OR** plausible path to ≥ $100K ARR within 24 months |
| Founder profile | One person, has a full-time job, ≤ 10 hr/week available, no co-founders, no hires, no physical product, no inventory, no in-person ops |
| Capital | $0–$500 to start. No outside funding. Tooling fits within standard AI-tool budgets ($20–$200/mo). |
| Tech stack | Off-the-shelf AI APIs + standard web tooling. No bespoke ML training, no GPU infra. |
| Pass threshold | Average ≥ 8.0 / 10 across the 5 personas, **and** no single persona scores below 6/10 (a single hard veto kills it). |
| Time budget | 5 hours wall-clock. If the budget is hit before N pitches pass, return what passed plus the strongest near-misses, clearly labeled. |

The user can override any of these in their prompt ("give me 5 ideas in the legal-tech space, $5K floor, willing to spend 20 hr/week"). Honor what they say; only fall back to the defaults for anything they didn't specify.

## The pipeline

The skill runs in five phases. Use TaskCreate to track them so you don't lose your place.

### Phase 1 — Frame the brief

Read the user's prompt and produce a short **brief** that fixes:

- Domain / industry scope (or "open")
- Revenue target and timeframe
- Founder constraints (time, money, skills, willingness to do sales/content/ops)
- Hard exclusions (e.g. "no crypto", "must be B2B")
- Number of pitches `N`
- Pass threshold (default 8.0 with no <6 veto)

Write this brief to `./pitches/_brief.md` for the run. Show it to the user in one short paragraph and proceed unless they push back.

### Phase 2 — Generate a candidate pool

Brainstorm `2 × N` candidate ideas (so you have a buffer for ones that get killed in scoring). Each candidate is a one-paragraph thesis: who the customer is, what the painful job-to-be-done is, why now (what AI capability or shift makes it newly tractable), and the rough monetization mechanism.

Bias the pool toward ideas that:

- Sell to **businesses or professionals**, not consumers (better willingness-to-pay per unit of distribution effort).
- Use AI as the **delivery mechanism**, not the marketing hook ("AI-powered X" with no real AI leverage is weak).
- Have a **boring, identifiable buyer** with a budget line item already.
- Can ship a v1 that creates real value within ~2 weeks of part-time work.
- Have **distribution paths a solo founder can actually walk** (cold email to a known niche, a single subreddit/forum/Discord, ProductHunt + indie-hacker channels, partnership with one larger creator/tool).
- Are **content-free or content-light** to operate (not "you must publish daily on TikTok").

Avoid ideas that secretly require:

- A team or hires
- Physical fulfillment, inventory, or in-person ops
- Regulated activity the founder isn't already licensed for
- A two-sided marketplace with chicken-and-egg dynamics (unless one side is solved)
- Paid ads as the primary distribution (burns capital, conflicts with $0-budget premise)

Read `references/founder-fit.md` for the full filter and `references/idea-patterns.md` for proven solo-AI patterns to draw from.

### Phase 3 — Research each candidate

For every candidate that survives an initial sniff test, spawn an **Explore subagent** (or run inline if no subagents available) to do real web research using WebSearch and WebFetch. The research must produce:

- **Market**: TAM / SAM / SOM with cited sources. If precise numbers don't exist, triangulate (e.g. "X businesses × Y avg spend"). Show the math.
- **Competitors**: Top 3–5 incumbents and 3+ indie/solo competitors. Note their pricing, positioning, weaknesses, and where the proposed pitch wedges in.
- **Customer evidence**: Real quotes/posts from prospective buyers complaining about the problem (Reddit, HN, niche forums, G2/Capterra reviews of competitors). Link them.
- **Pricing benchmark**: What do comparable tools charge? What's the realistic ACV?
- **Distribution channel evidence**: Concrete examples of similar tools that won via the proposed channel. Who, what, what numbers if public.
- **Regulatory / platform risk**: Any compliance, ToS, or platform-policy gotchas.
- **Unit economics sketch**: Cost-to-serve per customer (API costs, tool subs), gross margin, breakeven customer count.

See `references/research-checklist.md` for the exact prompt template to give the research subagent and the source-quality bar.

If a candidate fails research (TAM is fake, competitors already dominate, distribution is unreachable, unit economics break), kill it and pull the next one from the pool. Don't try to rescue weak ideas with optimistic spin — that wastes the persona panel's time later.

### Phase 4 — Score with the 5-persona panel

For every candidate that survived research, run it past the 5 evaluator personas defined in `references/personas.md`. Each persona reads the one-pager and the research, then returns:

- A score 1–10
- The single strongest reason they'd pass
- The single strongest reason they'd invest / build it themselves
- One concrete change that would move their score up by ≥1 point

Aggregate into a scorecard. Apply the pass rule (default: avg ≥ 8.0 AND min ≥ 6). For ideas that fail by a small margin, **apply each persona's "+1 change" suggestion** and re-score once. If still failing, kill it.

Keep going — pulling from the candidate pool, researching, scoring — until either:
- N pitches have passed, or
- The 5-hour wall-clock budget is hit, or
- The candidate pool is exhausted and you can't responsibly generate more good ones (don't pad with garbage).

### Phase 5 — Produce the deliverables

For each passing pitch, produce in `./pitches/<slug>/`:

```
./pitches/<slug>/
├── deck.html         # self-contained HTML deck (see assets/deck-template.html)
├── one-pager.md      # the executive summary doc
├── scorecard.md      # 5-persona scores + aggregate + the iteration history
└── red-team.md       # strongest objections + how the pitch answers each
```

Plus a top-level `./pitches/_index.md` that lists all pitches with their scores and one-line theses, sorted strongest-first.

See `references/pitch-structure.md` for the section-by-section content of the deck and one-pager. See `assets/deck-template.html` for the HTML scaffold to fill in.

## Communicating with the user during the run

This is a long-running skill (potentially hours). Don't go silent.

- After Phase 1: show the brief, confirm in one line.
- After Phase 2: report the candidate count and 2–3 representative theses. No long lists.
- During Phase 3 & 4: brief progress pings as candidates pass/fail ("Idea 4/20 passed research, scoring now"). Don't dump the full research into chat.
- After Phase 5: give a one-paragraph summary, the path to `./pitches/_index.md`, and the top 3 by score with their one-line theses.

If the time budget is getting tight, surface that to the user before silently truncating: "I've got 4 pitches passed at the 4hr mark, ~1hr left. Want me to keep pushing for 10 or stop here and write up what passed?"

## Why these constraints matter

The whole skill is calibrated to a specific kind of founder — someone with a day job who wants leverage, not another job. Almost every default in this skill exists because relaxing it tends to produce ideas that look good on a deck and die in execution:

- **Solo + AI delivery** keeps the operating cost flat as customers grow, which is the only way "passive-ish" math works without a team.
- **Boring, identifiable buyer** matters more than a clever idea — distribution kills more solo startups than product does, and you can't out-distribute YC-backed teams unless your buyer is too unsexy for them to bother with.
- **Pass-with-no-veto** matters because solo founders can't power through a single fatal flaw the way a team can. If one credible persona says "this dies because of X," X probably kills it.
- **Real citations** matter because confident-sounding fake numbers are the failure mode of LLM-generated pitches. The personas in Phase 4 will (correctly) hammer any unsupported claim.

When in doubt, prefer fewer, stronger pitches over hitting N. Returning 6 bulletproof ideas is more useful than 10 with two embarrassments mixed in.
