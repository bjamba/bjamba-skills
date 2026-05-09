# Scoring calibration

The default LLM tendency is to score 7–8 on every reasonable-sounding pitch. The previous version of this skill produced runs where almost every pitch landed 7.6–8.4 — flat, uncalibrated, and unhelpful. This file's job is to fight that.

## The principle

Scores are useful only if they discriminate. A run where 9 of 10 pitches score "around 8" is information-free. A run where the spread is 4.2 / 5.5 / 6.8 / 7.0 / 7.4 / 7.8 / 8.0 / 8.5 / 8.9 / 9.4 *teaches* the user. They can read the bottom and the top and feel the difference.

The way to force discrimination is **anchored distributions** — explicit "what a 5 looks like, what a 7 looks like, what a 9 looks like" benchmarks per commitment mode. Without anchors, every score collapses to the mean.

## Distribution targets per commitment mode

These are the *expected* shapes of the score distribution across the N pitches in a run. If a run produces a distribution dramatically tighter than these, you're not discriminating; recalibrate.

| Mode | Expected mean | Expected spread | % of pitches scoring 7+ | % scoring 4 or below |
|---|---|---|---|---|
| Passive-income | 5.0 | 4.0–6.5 typical range | ~15% | ~25% |
| Part-time solo | 5.5 | 4.5–7.0 | ~20% | ~20% |
| Full-time solo | 6.0 | 5.0–7.5 | ~30% | ~15% |
| Part-time team | 5.8 | 4.8–7.0 | ~25% | ~15% |
| Full-time team | 6.0 | 5.0–7.5 | ~30% | ~10% |
| Part-time biz/startup | 5.5 | 4.0–7.0 | ~20% | ~20% |
| Full-time biz/startup | 5.5 | 4.0–7.0 | ~25% | ~25% |
| Unicorn | 4.0 | 2.5–6.0 | ~10% | ~40% |

Notice: even in the modes the user picked, **most pitches should score 4–6**. Scoring 7+ should mean "this is a genuinely strong pitch *for this specific commitment mode*", not "this is a fine, defensible idea."

## What each score-band means (canonical anchors)

Use these as the calibration reference. When you assign a score, ask: does the pitch behave more like a 5-anchor or a 7-anchor?

### Score 1–3 — Don't do this

The pitch has at least one fatal flaw that the panel agrees on. Examples:
- The unit economics are negative at any plausible price.
- The wedge is illusory — the real competitor space is fully owned and the panel's evidence shows it.
- The regulatory / legal risk is serious enough to be a personal liability.
- The ICP is unreachable (no specific channel works for solo founder).
- The "AI" in the pitch is a 200-token prompt anyone can replicate.

These pitches still get full deliverables. Their value to the user is teaching what *not* to build.

### Score 4 — Borderline don't, with one redeeming feature

The pitch has one strength (real pain, identifiable buyer, decent unit economics) but a clear structural problem. Examples:
- Right buyer + right pain, but the founder needs a license/credential they don't have.
- Right idea + right wedge, but cost-to-serve is 50%+ of revenue and there's no scaling path.
- Solid documented problem, but a funded incumbent shipped a free version 3 months ago.

These are valuable for the user to see — they teach the difference between "good idea" and "good idea *that I could actually do*."

### Score 5 — Plausible but not exciting

The default case. The pitch has no fatal flaws, no breakaway strengths. Most ideas live here. Examples:
- A standard SaaS niche where the wedge exists but is small.
- A productized service with okay unit economics and no obvious channel.
- A solo Shopify app in a non-saturated category but without a real distribution insight.

The panel typically votes SOFT-PASS on these — "I see why someone might do this, but I wouldn't, and I wouldn't fund it."

### Score 6 — Worth thinking about

The pitch has at least one *real* strength that the panel agrees on. Maybe the buyer is unusually accessible (forced-compliance audience, named distribution channel). Maybe the unit economics are exceptionally clean. Maybe there's a non-obvious "why now" that opens the window for the next 6 months.

The panel often votes INTERESTED on these — "I'd take a meeting, hear more."

### Score 7 — Genuinely strong

The pitch has multiple compounding strengths and the panel can't easily articulate the kill condition. The unit economics are honest, the wedge is real, the distribution is solo-walkable, the "why now" is specific. The Skeptic can find risks but they're manageable.

Realistic outcomes:
- 1–2 INVEST decisions, 2–3 INTERESTED, 1–2 SOFT-PASS.
- Founder reflection: KEEP-PUSHING.
- Best-fit-mode often matches the chosen mode.

These are the pitches the user should consider actually building.

### Score 8 — Strong with a clear edge

7-anchor plus one of:
- A documented unfair advantage the founder has (existing audience, network, past credibility).
- A timing window that closes within 12 months (e.g., regulatory enforcement window).
- A wedge so narrow that funded teams literally won't pursue it.

The panel votes 3+ INTERESTED or INVEST. These are uncommon — perhaps 10–15% of pitches in their target mode.

### Score 9 — Exceptional within the mode

8-anchor plus the panel finding it genuinely difficult to identify the kill condition. The Skeptic concedes ("I can't find the fatal flaw and I tried"). The Domain Expert validates the buyer pain unprompted. The Customer says "I would buy this today."

These are rare. Perhaps 2–5% of pitches.

### Score 10 — Reserved

The score 10 should be reserved for pitches where the panel genuinely cannot find a flaw. Almost no pitch should score 10. If the panel feels like 10, ask: is there a flaw you're not seeing because the panel agrees?

## Avatar-specific calibration nudges

Each investor avatar has a per-mode bias profile (`references/investor-panel.md`). Use these to color the score, but don't let them override the anchored distribution:

- **Bootstrapper** evaluating passive-income mode: their natural appetite is 9. They should score *closer to the panel mean* for the mode, not way higher. Use their voice (anti-hype, pro-shipping) but stick to the calibration.
- **Growth VC** evaluating passive-income mode: their natural appetite is 2. They should still score honestly within their lens — "this isn't my world but here's what I'd notice." Don't trash a perfectly fine passive-income pitch with a 1/10 just because the mode is wrong for the avatar.
- **Skeptic** evaluating any mode: their bias is mode-neutral but their *baseline* is pessimistic. Their scores should *trend slightly below* the panel mean by ~0.5–1.0 points. That's their job.

## Forbidden score patterns

If you find a draft scorecard with any of these, recalibrate:

1. **All scores within 1.0 point of each other**. Real panels disagree more than that. Force at least one outlier per pitch.
2. **All N pitches scoring within 1.5 points of each other**. The skill's whole point is to discriminate; if everyone scores 7, the skill failed.
3. **No pitches scoring below 4**. Some ideas are bad. Surface them.
4. **No pitches scoring above 7**. If genuinely none of the N are strong, that's a real signal — but write it explicitly in `_post-mortem.md` ("the well was thin in this domain"), don't pad.
5. **Skeptic and Bootstrapper agreeing on every pitch**. They should disagree on most pitches; if they don't, you're not separating them in voice or in scoring.

## How to use this when running the skill

1. After running a meeting and drafting the scorecard, lay out the panel's scores.
2. Compute the panel mean.
3. Compare against the mode's expected distribution above.
4. If the score is too tight, ask: which avatar is over-scoring? Which is under-scoring?
5. Re-anchor against the canonical 5/7/9 descriptions above.
6. Re-write the scorecard with the recalibrated scores and updated rationales.

If after recalibration the panel mean is honestly 8 and the user is in unicorn mode, that's a real 8 — celebrate it. Don't artificially compress strong pitches. The point is *honest* discrimination, not forced negativity.

## A note on rounding

Scores are 1–10 integers in the simple case. If the panel is split (3 score 7, 2 score 5), the panel mean might be 6.2. Round to one decimal in the headline; don't try to be more precise than the underlying judgments.

## Cross-mode soundness score

Independently of the chosen-mode score, every pitch gets a "fundamental idea soundness regardless of mode" score from the Skeptic. This is calibrated separately:

- 1–3: bad idea in any mode
- 4–5: idea works in some specific mode but not most
- 6–7: idea is sound in the right hands at the right mode
- 8–9: idea is sound in multiple modes, mostly limited by founder's ambition
- 10: idea is sound at any mode (rare)

This score helps the user understand: is this pitch failing because of the *idea* or because of the *mode mismatch*? An idea soundness 9 with a chosen-mode score 4 means "great idea, wrong mode for this user." An idea soundness 4 with a chosen-mode score 4 means "just a so-so idea."
