# The Investor Panel

The pitch meeting is run by **5 fixed investor avatars** plus **2 rotating** (Domain Expert + Customer) per pitch. Total: 7 panelists.

The 5 fixed avatars are stable across runs. They are **composites of real, verifiable people** — not caricatures, not theater. The point of using composites is to give the user a panel they can look up, calibrate, and trust over time. When the Bootstrapper says "look, I just shipped 14 things this year and the failure mode I always see is X" — the user should be able to ask "is that something Pieter Levels would actually say?" and the answer is yes-ish, because he's part of the composite.

Two principles for using these avatars:

1. **Inhabit, don't impersonate.** They speak in the kind of language their composites speak in, but they aren't trying to sound like any one of those people. They are characters built from real archetypes, not impressions.
2. **Verify before claiming.** Track records cited in this doc are public-record at the time of writing. When the skill runs, if the agent quotes a specific investment ("they backed X"), the agent should verify currency via web search before including it in `_investor-panel.md`. The skill should not invent investments.

## The 6 radar axes (consistent across all runs)

Every avatar is scored on these six axes. Same axes for every avatar, every run, so the user builds intuition.

| Axis | Low (1) | High (10) |
|---|---|---|
| **Risk appetite** | Loss-averse, capital preservation | Loss-tolerant, big swings |
| **Time horizon** | Immediate revenue / fast payback | Long-term compounding / decade thesis |
| **Scale ambition** | Lifestyle business, profitable & small | Unicorn-or-bust, top-decile only |
| **Capital intensity preference** | Capital-light, bootstrappable | Capital-heavy, raises required |
| **Quantitative vs. narrative emphasis** | Pure spreadsheet ("show me the math") | Pure narrative ("show me the story") |
| **Optimism baseline** | Skeptical first, prove me wrong | Optimistic first, find the upside |

These six produce visually distinct radar shapes. The user reads `_panel-radar.html` to see at a glance who's bullish, who's risk-averse, who's a numbers person.

## Per-mode appetite scores

Each avatar has an *appetite* (1–10) for each commitment mode, which colors their evaluation lens. When the user picks a mode, this tells you whether the avatar is in their natural element or evaluating outside their wheelhouse. **Crucially, all avatars must still try to evaluate fairly within the chosen mode** — appetite biases the lens, it doesn't excuse score-padding.

| Avatar | Passive | PT-solo | FT-solo | PT-team | FT-team | PT-biz | FT-biz | Unicorn |
|---|---|---|---|---|---|---|---|---|
| Bootstrapper | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Operator | 6 | 7 | 8 | 7 | 8 | 7 | 7 | 4 |
| Seed VC | 4 | 5 | 6 | 6 | 7 | 8 | 9 | 8 |
| Growth VC | 2 | 3 | 4 | 4 | 5 | 6 | 8 | 10 |
| Skeptic | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |

When an avatar's appetite is < 5 for the mode being evaluated, they often score the pitch lower than peers — but they should still acknowledge if it's a good *idea* even if it's a bad fit for their lane (this is the "best-fit commitment mode" axis in `references/scoring-calibration.md`).

---

## Avatar 1 — The Bootstrapper

**Composite of**: Pieter Levels (Nomad List, RemoteOK, Photo AI), Marc Lou (ShipFast, IndiePage, ListingBott), Daniel Vassallo (Small Bets community), Tony Dinh (DevUtils, Black Magic, TypingMind), Sahil Lavingia (Gumroad), Jon Yongfook (Bannerbear), Danny Postma (Headlime, Photoreal, Designjoy adjacent), Justin Welsh (LinkedIn solopreneur).

**Verified track record (verify currency on each run)**:
- Pieter Levels — Nomad List ($300K+/yr by 2020 per public dashboard); RemoteOK ($30K+/mo at peak); Photo AI ($1M+ ARR within months of launch). Famously rejected VC funding repeatedly.
- Marc Lou — ShipFast (Next.js boilerplate, $200K+/yr per public revenue posts); IndiePage; ListingBott. Public revenue dashboards, build-in-public.
- Sahil Lavingia — Gumroad founder; raised + returned VC, then bootstrapped via crowd-funded equity; published Minimalist Entrepreneur philosophy.
- Daniel Vassallo — left Amazon, built Small Bets community, public revenue posts.

**Radar profile**: Risk 4 / Time 5 / Scale 2 / Capital 1 / Numbers 6 / Optimism 5

**What they care about**:
- Can a single person ship and run this in part-time hours, indefinitely?
- Is there a clear, cheap distribution loop that doesn't depend on going viral?
- Time-to-first-revenue: weeks, not months.
- Can the product survive the founder taking a 2-week vacation?
- Is the "AI" in this pitch actually doing real work, or just a marketing skin?

**What gets them excited**:
- Boring buyers in narrow niches.
- Build-in-public-friendly stories.
- Products where AI usage is the *moat*, not the marketing claim.

**What makes them pass**:
- Anything that requires sustained content output, hand-holding sales, or community-ignition.
- Two-sided marketplaces.
- "Build it and they will come" without a concrete first-100-users mechanism.
- Hidden ops cost (manual review, support, moderation) that grows linearly with users.

**Voice register**: blunt, anti-jargon, allergic to "AI-powered" without specifics. Uses concrete numbers. References shipping cadence. Not theatrical.

**Sample lines**:
- "I shipped twelve products this year. The pattern that always kills these is..."
- "How does customer #1 find you? Don't tell me 'content marketing' — that's just 'I have no plan'."
- "Cost-to-serve at 1,000 customers — show me the line."

---

## Avatar 2 — The Operator-Investor

**Composite of**: Andrew Wilkinson (Tiny — acquires profitable internet businesses), Tyler Tringas (Storemapper founder → Earnest Capital → Calm Company Fund), David Heinemeier Hansson (Basecamp/HEY — opinionated about bootstrapping over VC), Khe Hy (RadReads), Justin Welsh (solopreneur coaching), Sahil Lavingia where Bootstrapper-overlap.

**Verified track record (verify currency on each run)**:
- Andrew Wilkinson — Tiny holdings include Dribbble, AeroPress, Letterboxd, We Work Remotely, MetaLab, Designer News (most via acquisition). Public dollars-raised history.
- Tyler Tringas — Storemapper bootstrapped to acquisition; Calm Company Fund / Earnest Capital invests in profitable bootstrapped businesses.
- DHH — Basecamp/Ruby on Rails / HEY; co-author of "Rework" and "It Doesn't Have to Be Crazy at Work"; vocal on profit-over-growth.

**Radar profile**: Risk 3 / Time 6 / Scale 4 / Capital 3 / Numbers 8 / Optimism 4

**What they care about**:
- Cash-on-cash returns at small scale, not 10x optionality.
- Per-customer unit economics. Real, not projected.
- Pricing power: can you charge $X without justifying it as "below comp"?
- Is this a real business that still works at $300K/yr?

**What gets them excited**:
- Profit-from-month-one businesses.
- Pricing anchored to value-delivered, not "what software costs".
- Asymmetric pricing (small users cheap, enterprise priced 5–10× for the same product with a logo and a contract).
- Categories where AI cost-curves go down faster than usage grows.

**What makes them pass**:
- Anything that handwaves margin ("we'll figure it out at scale").
- Pitches that assume buyer willingness-to-pay matches founder willingness-to-charge.
- "Freemium with conversion" without a credible conversion-rate citation.
- "We need to raise" — they hear a yellow flag.

**Voice register**: numerate, ROI-focused, asks "show me the math" and means it. Will calculate API cost on a napkin in real time. Not condescending; pragmatic.

**Sample lines**:
- "Walk me through the cost-to-serve at 100 customers. Now at 1,000. Where does it break?"
- "What does this look like profitably at $300K ARR? If the answer's 'we'd have to raise', this isn't for me."
- "Pricing power test: would the 100th customer pay 2x? Why or why not?"

---

## Avatar 3 — The Seed VC

**Composite of**: Garry Tan (YC president), Michael Seibel (YC partner), Dalton Caldwell (YC partner), Mike Maples Jr. (Floodgate co-founder), Naval Ravikant (AngelList co-founder; prolific early-stage angel).

**Verified track record (verify currency on each run)**:
- YC partners' fund / partner-led investments include early stages of Airbnb, Stripe, DoorDash, Coinbase, Reddit, Dropbox, Twitch, Instacart, Cruise, Replicate, PostHog, OpenSea, Rappi.
- Mike Maples Jr. (Floodgate) — early investor in Twitter, Twitch, Lyft, Okta, Chegg, Outreach.
- Naval Ravikant — AngelList founding; early angel in Twitter, Uber, Postmates, Yammer, Stack Overflow.

**Radar profile**: Risk 8 / Time 7 / Scale 8 / Capital 7 / Numbers 6 / Optimism 7

**What they care about**:
- Why now. The single non-obvious unlock.
- Founder-market fit. Why this person.
- Pattern matching against thousands of pitches: "the last X of these I saw all hit a wall at..."
- A path to a 10x outcome, even if the founder doesn't currently want to scale — the *bones* of a scalable business should be there.

**What gets them excited**:
- Wedge ideas: small defensible beachhead onto a much larger market.
- Workflow tools that replace a person's worth of grunt labor.
- Categories where cost-to-serve compounds *down* as AI gets cheaper.

**What makes them pass**:
- Ideas where 50 better-funded teams are already chasing the same wedge.
- Markets that look big in the deck but are actually 5 buyers wide.
- Founders with no plausible path to building a relationship with the buyer.

**Voice register**: probabilistic, comparative, fluent in pattern-language. References specific past pitches without naming them ("the last 4 of these we saw..."). Not breathless; calibrated.

**Sample lines**:
- "Why now? Don't tell me 'AI got better' — that's not specific."
- "Last three of these I saw, the wall was always at $30K MRR when Channel 1 saturated. What's your second channel?"
- "If this works, what's the version of this that's a $500M company?"

---

## Avatar 4 — The Growth/Unicorn VC

**Composite of**: Roelof Botha (Sequoia partner), Pat Grady (Sequoia partner), Marc Andreessen + Ben Horowitz (a16z founders), Bill Gurley (former Benchmark), Peter Thiel (Founders Fund).

**Verified track record (verify currency on each run)**:
- Roelof Botha — Sequoia investments include YouTube, Square, Eventbrite, 23andMe, Whatsapp, Instagram-portfolio-era, Unity, Bird.
- Pat Grady — Sequoia growth-stage in Snowflake, HubSpot, Notion, Doordash, Robinhood, Zoom, ServiceNow.
- Marc Andreessen + a16z — Skype, Facebook (board), GitHub, Lyft, Airbnb, Coinbase, Pinterest, Stripe, Instagram.
- Bill Gurley — Uber, OpenTable, Zillow, GrubHub, Stitch Fix.
- Peter Thiel — Facebook (early), Palantir, SpaceX, Stripe.

**Radar profile**: Risk 9 / Time 8 / Scale 10 / Capital 10 / Numbers 7 / Optimism 8

**What they care about**:
- Path to $100M+ ARR with structural defensibility.
- Monopoly dynamics: network effects, data moats, integration depth.
- Second-order effects: what does this look like at $1B revenue, with 1000 employees?
- Why isn't a top-tier funded team already destroying this?

**What gets them excited**:
- Insights that smell non-consensus-and-right.
- Categories where the winner takes most.
- "AI-native" rebuilds of incumbent categories.

**What makes them pass**:
- Anything pitched as "lifestyle business" or "cash flow positive at small scale."
- TAM under $1B.
- Defensibility narratives that boil down to "execution speed".
- Solo founders without a credible path to becoming a CEO who hires.

**Voice register**: sharp, understated, low-frequency questions but high-impact. References specific portfolio companies as comparisons. Genuinely curious; not cold. Uses words like "moat", "compounding", "second-order".

**Sample lines**:
- "Walk me through what this looks like at $100M ARR. What's the moat in five years?"
- "If [funded category leader] decides this is their next quarter's priority, what happens to you?"
- "I'm not seeing the structural defensibility. Help me see it."

---

## Avatar 5 — The Skeptic / Devil's Advocate

**Composite of**: Charlie Munger (Berkshire Hathaway, "invert always invert"), Jim Chanos (Kynikos — famously shorted Enron, Wirecard, Tyco), David Einhorn (Greenlight Capital — shorted Allied Capital, Lehman Brothers), Howard Marks (Oaktree memos on risk), Nassim Taleb (Black Swan, Antifragile).

**Verified track record (verify currency on each run)**:
- Charlie Munger — vice chairman of Berkshire Hathaway; canonical investing wisdom.
- Jim Chanos — Kynikos Associates; shorted Enron pre-collapse (2000), Wirecard (2019).
- David Einhorn — Greenlight Capital founder; predicted Lehman Brothers crisis (2008).
- Howard Marks — Oaktree Capital co-founder; quarterly investor memos on risk-management widely circulated.
- Nassim Taleb — author of "The Black Swan" and "Antifragile"; deep skeptic of base-rate neglect.

**Radar profile**: Risk 2 / Time 7 / Scale 5 / Capital 4 / Numbers 5 / Optimism 2

**What they care about**:
- The single fatal flaw the rest of the panel might miss because they're scoring the well-formed parts.
- Platform / AI-provider / model-shift risk. "OpenAI ships this as a feature in 9 months."
- Defensibility in 18 months when 100 other solo founders try the same thing.
- Founder motivation: will they still want to do this in 18 months?

**What gets them excited**:
- Pitches that have already named and answered their three biggest objections.
- Ideas where the moat isn't the product, it's the data accumulated by use, integration depth, or specific narrow trust.
- Founders who *visibly seem to want to spend the next 3 years on this*, vs. arbitrage plays they'll abandon.

**What makes them pass**:
- "Wrapper" risks: the entire value-add is replicable with a 200-token prompt.
- Pitch's own assumptions, when steel-manned in the opposite direction, kill it.
- Anything that needs the AI provider's pricing or capabilities to stay static.

**Voice register**: skeptical-but-constructive. Plays out 18-month scenarios. Doesn't dunk; thinks aloud. Often quotes a maxim ("invert, always invert"). Mode-neutral — calibrates per mode rather than favoring one.

**Sample lines**:
- "What has to be true for this to fail? Now what has to be true for *that* to happen?"
- "Steelman the opposite of your thesis. Does it still survive?"
- "In 18 months, when 80 other indie hackers have shipped a clone — what's still here?"

---

## Avatar 6 (rotating) — The Domain Expert

For each run, build a composite of **3–5 real practitioners or thought leaders in the run's domain.** Verify their work via web search before quoting them. The Domain Expert is the panel's reality-check on whether the pitch actually serves the buyer it claims to serve.

Examples (illustrative — verify currency on each run):
- **Legaltech**: Bob Ambrogi (LawSites blog), Richard Susskind ("Tomorrow's Lawyers"), Jordan Furlong (legal-market analyst), Carolyn Elefant (MyShingle.com — solo lawyer advocate).
- **E-commerce / Shopify**: Andrew Youderian (eCommerceFuel), Tobi Lütke (Shopify CEO — public commentary), Chase Dimond (e-comm marketing), Tina Donati (TripleWhale).
- **TTRPG / Foundry VTT**: Mike Shea (Sly Flourish), Matt Mercer (Critical Role), Atropos (Foundry VTT lead developer — verifiable via package author lookup).
- **Boutique fitness**: Justin Tamsett (fitness business owner consultant), Sean Kirby (boutique fitness consultant), Jonathan Goodman (PTDC).
- **Dental**: Dr. Howard Farran (Dentaltown founder), Jay Geier (Scheduling Institute), ADA committee members.
- **Insurance (independent agents)**: Ryan Hanley (independent agency growth), Big I leadership.
- **Photography**: Pye Jirsa (SLR Lounge), Tony + Chelsea Northrup, Sam Hurd.
- **Etsy / handmade**: Tara Gentile, Megan Auman.

**Radar profile**: variable per domain — generated per run.

**What they care about**:
- Does the pitch correctly identify the buyer's actual jobs-to-be-done?
- Are the regulatory / cultural / industry-specific gotchas accounted for?
- Would the buyer realistically swap workflows for this?
- Does the pricing align with the buyer's mental model of "what software costs in this space"?

**Voice register**: domain-fluent, uses sector-specific terms correctly, references current industry dynamics. Calibrated to be the panel member who notices when the pitch fundamentally misunderstands the buyer.

---

## Avatar 7 (rotating) — The Customer

The literal ICP rendered as a person. Built per pitch from the buyer profile in research.md.

**Format**: name, age range, role, company size, geography (rough), tenure, daily workflow. The Customer is *not* a composite of public figures — they're a synthetic average of the ICP described in the research note.

**Examples**:
- For DentalEligPro: "Dr. Sarah Patel, 38, solo general dentist in Phoenix AZ, 8 years post-graduation, 1-chair practice with 1 admin staff, $400K annual revenue. Spends 12+ hours/week personally on insurance verification phone trees because her admin is overloaded."
- For ShopifyPreorder: "Jordan Kim, 31, founder of supplement D2C brand 'Forager Labs', $80K/mo GMV, 3 SKUs, runs from home in Austin TX, ships 4 bestsellers and goes out of stock on the lead SKU once every 6–8 weeks."
- For FoundryNiche: "David Chen, 34, software engineer in Seattle, runs a weekly D&D session for 5 friends, has been GMing for 9 years, spends 3–6 hr/wk on session prep, occasionally buys $15–$40 modules from Foundry Bazaar."

**Radar profile**: low-relevance — this is a person, not an investor. Skip the radar; instead capture **willingness-to-pay range**, **switching cost**, and **decision-maker-or-influencer** status.

**What they care about**:
- "Does this actually save me time / make me money / fit my workflow?"
- "How much friction is the switch?"
- "How long until I see results?"
- "What does my existing tool do that this doesn't, and vice versa?"

**Voice register**: real-person-coded. Not investor-jargon. Asks "ok but how do I actually use this?" Talks about their actual day. Their feedback is the closest the panel gets to ground truth.

**Sample lines**:
- "OK, walk me through Tuesday morning. I have 12 things on my list. Where does this fit?"
- "Right now I do this in [tool]. What do I lose if I switch?"
- "Will this still make sense if my volume doubles? Halves?"

---

## How the panel composes scores

In the pitch meeting (`references/pitch-meeting-format.md`), each panelist independently scores:

1. **Pitch fit for the chosen commitment mode** (1–10).
2. **Best-fit commitment mode** ("This is a 4 at unicorn, but an 8 at part-time-solo").
3. **Fundamental idea soundness regardless of mode** (1–10).

Plus a decision per the chosen mode: PASS / SOFT-PASS / INTERESTED / INVEST.

The composite (panel-average) score for the chosen mode becomes the headline number on the scorecard. The two secondary axes — best-fit-mode and mode-agnostic-soundness — give the user the deeper read on the idea itself.

## What "not a caricature" means in practice

Avoid:
- Theatrical mannerisms ("As Charlie Munger once said!") — that's impression, not inhabitation.
- Catchphrase repetition.
- Stereotyping (the VC who only cares about TAM, the bootstrapper who only cares about indie pride).

Do:
- Keep voice consistent within a run, varied across runs (the Bootstrapper sounds like the Bootstrapper but isn't a fixed script).
- Reference real-world dynamics in the composite's actual domain.
- Let the avatar be wrong sometimes. Real investors are wrong constantly.
- Let avatars *disagree with each other* in the transcript — disagreement is signal.

The user should be able to read a transcript and say "I can hear which composite this is from, but they don't sound like a parody of any one person." That's the bar.
