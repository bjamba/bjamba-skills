# Per-Candidate Research Checklist

Each of the N candidates gets one research pass before it goes into the simulated pitch meeting. Use WebSearch and WebFetch against real sources. Spawn an Explore subagent if available — research benefits from parallelism.

The output of this phase is a structured research note (`./pitches/<slug>/research.md`) that the panel reads alongside the one-pager during the meeting.

In v2 of the skill, **every candidate gets full research and a full meeting regardless of how the research lands**. If research surfaces a fatal flaw, *that flaw becomes part of the pitch's deliverables* — the panel will critique it accordingly and the user will read it as a documented learning artifact. Do not soften research findings to make a candidate look more passable.

## Source quality bar

**Acceptable sources**:
- Industry reports from named firms (Statista, Gartner, IBISWorld, McKinsey) — but only with the publication date, not stale 2018 numbers.
- Public company filings, S-1s, 10-Ks for adjacent comps.
- Crunchbase / PitchBook funding data with dates.
- Real customer quotes from Reddit, Hacker News, Indie Hackers, niche forums, G2/Capterra/TrustPilot reviews. Prefer threads where you can show the buyer is paying for *something* in the space.
- Pricing pages of named competitors, captured with the URL.
- Founder transparency posts (e.g., MicroConf-style revenue dashboards, IndieHackers profiles).
- Government / regulatory primary sources for compliance questions.

**Not acceptable**:
- Made-up percentages without a citation.
- AI-generated content farms (Medium SEO listicles, generic "Top 10 X" articles).
- "Industry experts say…" with no named expert or source.
- Marketing material from the company being researched, taken at face value.

If a number can't be sourced, **say so explicitly** in the research note ("TAM not directly published; triangulated from {two cited inputs} as ~{number}, math shown below"). Confident-sounding fake numbers are the failure mode the personas hammer hardest.

## Research note structure

Produce this exact structure for each candidate, saved to `./pitches/<slug>/research.md`:

### 1. Market sizing
- TAM: total addressable, with the unit of analysis and the source.
- SAM: realistic served-able portion given the founder's reach.
- SOM: what 1% / 5% / 10% capture would look like in revenue.
- If sizing isn't published, show the triangulation math with both inputs cited.

### 2. Buyer profile
- Specific job title or persona with company-size band (B2B) or demographic + behavior (B2C).
- 3–5 quotes from real buyers describing this pain. Link each.
- What they're doing today as a workaround. What they're paying (in time or money) for that workaround.

### 3. Competitive landscape
- 3–5 direct competitors. For each: URL, pricing, positioning, what users complain about (cite reviews), team size if findable.
- 3+ indirect competitors / substitutes (including "do nothing" and "use spreadsheets").
- The wedge: where this pitch slides in that incumbents can't or won't follow.

### 4. Pricing benchmark
- What comparable tools charge.
- Anchor pricing claim for this pitch with a justification ("priced at $X because comp Y charges $Z and we deliver Q% of that value at half the surface area").
- Sensitivity: how the unit economics change at $X / $X*1.5 / $X*0.5.

### 5. Distribution channel evidence
- Named channel(s) with the *exact* sub-channel (specific subreddit, specific marketplace, specific newsletter, specific search keyword).
- Concrete examples of similar tools that won via this channel — name and any public numbers.
- Estimated cost (time + money) to acquire customers #1, #10, and #100 via this channel.
- If applicable, what the founder must do *first* to be welcome in this channel (build credibility, ship a free tool, write a specific post).

### 6. Regulatory / platform / model risk
- Any compliance risk (GDPR, HIPAA, FCRA, FTC ad rules, COPPA, state-level licensing) — even if low.
- Platform risk if the product depends on another platform (App Store, OpenAI, Shopify, Stripe, Foundry, Etsy, Webflow).
- Model risk: what happens if AI provider pricing 5x's, capabilities improve, or the provider ships a competing native feature.
- **Founder licensing**: does the pitch require credentials the founder doesn't have? Tools FOR licensed pros are fine; BEING the licensed pro is not.

### 7. Unit economics sketch
- AI / inference cost per active customer per month. Show the math (tokens, calls, model tier).
- Other variable costs (third-party APIs, data sources, payment fees).
- Gross margin at the proposed price.
- Breakeven customer count to cover fixed monthly costs.
- What happens if a power user uses 10x the average — does the margin survive?

### 8. Why now
- What changed in the last 18 months (AI capability, cost curve, regulatory shift, behavior change post-pandemic, platform availability) that makes this newly tractable.
- If the only "why now" is "AI got better generically," that's weak — push for something specific.

### 9. Commitment-mode fit (NEW)
- Does the realistic effort profile (build hours, ongoing ops, sales motion, support load) match the chosen commitment mode?
- Specifically:
  - For passive-income mode: is the v1 truly buildable in ≤80 hours and operable in ≤2 hr/wk at scale, or is that wishful thinking?
  - For higher modes: does the founder profile match what the mode demands (full-time time, hiring willingness, fundraising plan)?
- If the realistic effort exceeds the chosen mode, **say so explicitly**. The panel will then evaluate "best-fit commitment mode" alongside the chosen mode.

### 10. Open questions
- Things the research couldn't resolve. The panel will see these and weight them.
- Don't hide unknowns. Surface them — it earns trust and lets the panel evaluate honestly.

## Research subagent prompt template

When spawning an Explore subagent for research, give it this prompt (adapt the candidate paragraph):

> Research this startup candidate and produce a structured note covering market sizing, buyer profile, competitors, pricing, distribution, regulatory/platform/model risk, unit economics, why-now, commitment-mode fit, and open questions.
>
> Candidate: {one-paragraph thesis from Phase 2}
> Commitment mode under evaluation: {mode}
> Pitch style: {bold | niche | laser | solid}
>
> Source quality bar: cite real sources by URL. If a number isn't directly published, triangulate and show the math with cited inputs. Prefer real customer quotes from Reddit/HN/IndieHackers/G2 over marketing copy. Capture pricing pages with URLs. Flag stale (>2 year old) data as stale.
>
> Output the note in the structure described in `references/research-checklist.md` sections 1–10. Save to `./pitches/{slug}/research.md`. Be concise but specific — this note feeds the 7-investor panel pitch meeting that will hammer any unsupported claim.
>
> If you discover the candidate is unworkable (TAM is fake, dominant incumbents already own the wedge, distribution is unreachable, unit economics break, mode-mismatched), say so explicitly in the note's "Why this might not work" section at the end. **Do not soften the finding to keep the candidate viable** — the pitch meeting will use the honest research and the resulting failure becomes part of the user's learning artifacts.

## Honest research, not protective research

In v1 of this skill, weak research killed candidates and they got dropped from the pool. In v2, weak research **goes into the meeting unchanged** and the panel critiques it honestly. This means:

- TAM that doesn't support the revenue floor: the panel will say so.
- The "wedge" disappearing once the competitive landscape is mapped: the panel will say so.
- Distribution channel evidence missing: the panel will say so.
- Unit economics breaking at realistic prices: the panel will say so.
- Regulatory or platform risk severe enough to veto: the panel will say so.

**Your job in research is to surface the truth, not to protect the pitch from rejection.** The user wants to read both wins and losses. A pitch that fails for a clear, well-researched reason is more useful to the user than a pitch that scrapes by because the research was charitable.
