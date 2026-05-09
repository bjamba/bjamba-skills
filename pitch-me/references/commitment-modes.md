# Commitment Modes

The single most important variable in this skill. Every other lever — candidate generation, research depth, scoring distribution, investor calibration, pass thresholds, deliverable emphasis — flexes to the chosen mode.

A pitch that scores 9/10 in passive-income mode might score 3/10 in unicorn mode. That isn't a bug; it's the whole point. **The right idea for the wrong mode is the wrong idea.**

## The 8 modes

In order from least-effort to most-effort. The user picks **one** during Phase 0 intake.

| # | Mode | Founder time | Founder ambition | Capital risk | What "success" means |
|---|---|---|---|---|---|
| 1 | **Passive-income** | ≤ 2 hr/wk steady; ≤ 80 hr v1 build | Keep day job. Software runs itself. | < $500 | $1K–$5K MRR with near-zero ongoing ops |
| 2 | **Part-time solo** | 5–15 hr/wk indefinite | Day job preserved. Hands-on but bounded. | < $2K | $3K–$10K MRR with light weekly upkeep |
| 3 | **Full-time solo** | 30–50 hr/wk | No day job. Solo founder commits full-time. No team. | < $20K | $5K–$30K MRR; a real living |
| 4 | **Part-time team** | Founder PT + 1–2 PT collaborators | Day job optional. Has trusted collaborators. | < $20K | $5K–$30K MRR with ops sustainable across 2–3 people |
| 5 | **Full-time team** | Founder FT + 2–4 FT teammates | Real small business. Hires. Maybe office. | $20K–$200K | $30K–$200K MRR; ramen-profitable team |
| 6 | **Part-time business / startup** | Founder PT but planning growth | Building toward real company; preserving optionality | < $50K | Path to $1M ARR within 24 months without giving up day job yet |
| 7 | **Full-time business / startup** | Founder FT, building real company | Hires, possibly raises seed. Real fiduciary stakes. | Often raised | $1M–$10M ARR within 24–36 months |
| 8 | **Unicorn** | Founder FT + funded team | Venture-backed, top-decile ambitions | $1M+ raised | $100M+ ARR, IPO/M&A path |

## How to choose / how to ask

In Phase 0, present the 8 modes briefly (with one-line descriptors) and ask the user to pick one. The default is **Passive-income**, because that's the user's baseline mental model when they say "AI side hustle" or "thing I could build solo with AI." If their phrasing implies something more ambitious ("startup", "VC", "co-founder", "raise"), surface that and confirm.

If the user gives mixed signals (e.g., "I want passive income but I'm willing to work full-time on it"), pick the more demanding mode and note the ambiguity in `_brief.md`. Mismatched-mode classification is the #1 source of bad pitches in this skill.

## Mode-specific filters and gates

These layer on top of `references/founder-fit.md`. Each mode has its own hard-kill conditions; a candidate that fails any of these in its target mode dies in research.

### Passive-income mode (THE DEFAULT)

The hardest mode to satisfy. Most "decent-sounding" startup ideas fail here because they require sustained founder attention.

**Hard gates (any failure → kill the candidate):**
- v1 buildable in ≤ 80 hr of part-time work
- Steady-state ops ≤ 2 hr/wk at 1,000 customers (no manual review, no support hand-holding, no daily content production)
- No sustained sales calls, no daily content output, no community moderation
- Cost-to-serve < 30% of revenue per customer per month
- No regulatory licensing or ongoing compliance work the founder has to personally do
- Distribution must work without paid ads as the primary channel
- API/inference costs must be flat or sub-linear with customer count
- Customer-success and onboarding can be 100% self-serve (or one-pager docs)

**Soft signals (penalize, don't kill):**
- Anything content-heavy, even if "scheduled"
- Anything requiring founder availability for escalations (e.g., "AI-augmented expert on call" patterns are mode-mismatched here unless the escalation frequency is genuinely <1/week)

**Realistic outcomes:** $1K–$5K MRR is the realistic ceiling without scope-creeping into Mode 2. If a pitch promises $20K MRR in passive-income mode, it's almost certainly miscategorized.

### Part-time solo mode

A relaxed version of passive. The founder is willing to do 5–15 hours of *bounded, predictable* weekly work.

**Hard gates:**
- v1 buildable in ≤ 200 hr of part-time work
- Steady-state ops ≤ 15 hr/wk at 1,000 customers
- Day job is preserved; the work pattern must be sustainable around it (evenings/weekends)
- No real-time customer support (next-business-day OK)

**Realistic outcomes:** $3K–$10K MRR. Productized services, marketplaces with light ops, and slow-burn content plays all become viable here. Doc-heavy services (custom contracts, bookkeeping at low volume) can fit if the workflow is bounded.

### Full-time solo mode

The founder commits full-time. No team, no hires. Software is the leverage.

**Hard gates:**
- The founder must be capable of doing all of: build, sell, support, operate
- Total fixed monthly burn (tools + infra) ≤ 5% of target MRR
- The work must be sustainable for 2+ years without burnout

**Realistic outcomes:** $5K–$30K MRR. This is the "indie Shopify-app developer" / "bootstrapped micro-SaaS" zone. Pitches in this mode can absorb more sales/ops effort than passive can.

### Part-time team and Full-time team modes

Founder + 1–4 collaborators. Either part-time (founder keeps day job, collaborators are PT) or full-time small team.

**Hard gates:**
- Hiring/cost structure must be defensible from revenue (no betting on raise)
- Ops can absorb 2–4 people's bandwidth, but founder still does most-important work
- No two-sided marketplaces requiring concurrent supply+demand activation unless one side is genuinely solved at launch

**Realistic outcomes:** $5K–$30K MRR (PT) / $30K–$200K MRR (FT). Cash businesses, productized service shops, vertical SaaS at small scale.

### Part-time business/startup and Full-time business/startup modes

The founder is building a real company with growth ambitions. May raise capital. Plans to hire.

**Hard gates:**
- There must be a credible path to $1M+ ARR within 24 months (PT) or 12–18 months (FT)
- TAM must be ≥ $100M
- Distribution must scale beyond founder-as-only-channel
- Defensibility (data moat, network effects, integration depth, brand) must be narrated, even if early-stage

**Realistic outcomes:** $1M–$10M ARR. Vertical SaaS, AI-native vertical apps, B2B platforms with outbound sales motions.

### Unicorn mode

The most demanding mode. Top-decile ambitions only.

**Hard gates:**
- Path to $100M+ ARR with credible defensibility
- Market is structurally winner-take-most or has strong network effects
- Capital plan supports it (the founder has, or can credibly raise, what's needed)
- The idea must be one a top seed VC would back over the next 100 they see

**Realistic outcomes:** Most candidates die here. Unicorn-mode runs typically pass 1–3 pitches out of 20 generated. That's correct.

## Investor-mode interaction

Each investor avatar (`references/investor-panel.md`) has a per-mode bias profile. The Bootstrapper treats passive-income pitches generously and unicorn pitches harshly. The Growth/Unicorn VC does the opposite. The Skeptic stays mode-neutral but calibrates the kill-criteria per mode.

When scoring a pitch:

1. The panel scores **for the user's chosen commitment mode** (the primary score).
2. The panel additionally rates **best-fit commitment mode** ("I'd score this 4/10 at unicorn but 8/10 at passive-income — it's a fine micro-SaaS, not a venture").
3. The Skeptic separately rates **fundamental soundness regardless of mode** ("This works in any mode" or "This dies regardless of mode").

This three-axis scoring is what makes the skill genuinely useful — it tells the user not only "is this a good pitch *for me*" but also "is the *idea* good, and would a different mode change the answer?"

## Calibration anchors

For each mode, `references/scoring-calibration.md` provides explicit "what a 5 looks like, what a 7 looks like, what a 9 looks like" benchmarks. The default LLM tendency is to cluster scores in 7–8; the calibration anchors fight that and produce more honest distributions. Most pitches should land 4–6 in their target mode; 7+ is genuinely strong and 9+ is exceptional.

## What to write to the brief

In `_brief.md`, capture the chosen mode plus the user's answers to:

- Domain / industry
- Hard exclusions
- Number of pitches `N`
- Founder profile delta (anything different from the mode's default)
- Autonomous-mode confirmation

Reference the chosen mode by number and name in every downstream artifact (one-pager, scorecard, transcript) so a reader picking up a single deliverable knows the mode it was scored against.
