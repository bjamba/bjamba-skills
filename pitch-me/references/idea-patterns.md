# Solo-AI Idea Patterns

This is a catalog of patterns that have actually produced revenue for solo founders using AI as the core leverage. Use them as scaffolding when generating candidates — not as a list to copy from. The point is to recognize the *shape* of an idea that fits the constraints, then specialize it to a real niche, buyer, and wedge.

When you generate a candidate, try to articulate which pattern (or hybrid of patterns) it instantiates. If you can't, the idea may be too vague.

## Mapping patterns to commitment modes

Each pattern has a "natural mode" where it shines, and modes where it tends to break:

| Pattern | Best modes | Worst modes |
|---|---|---|
| A — Vertical AI workflow tool | Part-time solo, Full-time solo | Passive-income (often needs sales motion); Unicorn (TAM cap) |
| B — Productized service with AI as labor | Part-time solo, Full-time solo, Part-time team | Passive-income (review touch); Unicorn (doesn't scale infinite) |
| C — Integration glue | Passive-income, Part-time solo | Unicorn (platform-dependent ceiling) |
| D — Curated AI-generated data product | Passive-income, Part-time solo | Unicorn (TAM cap) |
| E — Niche-trained content site / freemium tool | Passive-income (slow burn), Part-time solo | Higher modes need faster ramp |
| F — AI-augmented expert / agent-on-call | Full-time solo, Part-time team | Passive-income (escalations break it) |
| G — Internal-tool-as-a-product | Most modes; depends on the tool | Unicorn unless the tool addresses a $1B+ category |

Use these as a sanity-check during candidate generation. If a candidate is Pattern F (escalations) being pitched in passive-income mode, that's mode-mismatched — call it out and let the meeting evaluate accordingly. Don't reject it; just be clear-eyed.

## Pattern × Pitch-style mix

For the pitch-style mix in `references/pitch-style-mix.md`:

- **Bold** candidates often combine 2 patterns (e.g., F + D = "AI-on-call layered on a curated data product"). Useful for exploring what's possible at the frontier.
- **Niche** candidates usually instantiate a single pattern in a deep vertical (e.g., A in legaltech, A in dental ops, A in funeral home).
- **Laser** candidates almost always instantiate a single pattern with the smallest possible v1 (e.g., E or D narrowed to one specific use).
- **Solid** candidates instantiate Patterns A, B, or C with a documented buyer and an empty wedge — these are where most of the user's actually-buildable hits will come from.

---

## Pattern A — Vertical AI workflow tool

**Shape**: Take a recurring, expensive task done by a specific job title. Build a tool that does 80% of it with AI. Sell to that job title at a price anchored to their hourly rate, not to "what software costs."

**Why it works for solo + AI**: The buyer already has the budget (they're already paying for the labor). AI now does work that previously required judgment. A solo founder can ship a thin, opinionated v1.

**Examples that have worked**:
- AI tools for paralegal-style document review, scoped to one document type.
- "Brief generators" for specific consulting verticals (RFP responses, grant applications).
- Vertical-specific transcription + structured-extraction tools (medical scribes, court reporting prep, real-estate inspection notes).

**Pitfalls**: Generic horizontal tools (AI writing assistant, AI meeting notes) are saturated and dominated by funded teams. The pattern only works when the *vertical* is narrow enough that funded teams won't bother.

---

## Pattern B — Productized service with AI as the labor

**Shape**: Offer a fixed-scope, fixed-price deliverable. AI does the production work; the founder packages, reviews, and delivers. Buyer pays for the outcome and the trust, not the underlying tech.

**Why it works**: Buyers who don't want to learn a tool will happily pay 3–5x more for a delivered result. Bypasses the SaaS pricing-pressure trap entirely.

**Examples that have worked**:
- "We build your website / marketing site for a flat fee in 5 days."
- "We write your weekly newsletter, you approve, we ship."
- "Custom-trained chatbot for your business, set up and handed over in a week."
- Audit-style deliverables (SEO audits, ADA-compliance audits, brand-voice audits) sold flat-rate.

**Pitfalls**: Operations cost compounds with customers if review/QA isn't tight. Price floor must be high enough that founder time per delivery is worth it (think $500+ per delivery).

---

## Pattern C — Integration glue

**Shape**: Two popular tools that don't talk to each other well. The product is the integration — usually a sync, an enrichment, or a workflow trigger. Often distributed via the marketplaces of the parent tools.

**Why it works**: Distribution is solved-ish (parent marketplaces). Buyer is already paying for both tools. AI can do the data normalization or transformation that previously made integrations brittle.

**Examples that have worked**:
- Slack/Notion/Linear/Salesforce integrations that AI-enrich or transform data in flight.
- Email-to-CRM with AI categorization.
- Data sync between specific niche-tool pairs.

**Pitfalls**: Platform risk is real (parent tool may build it natively). Counter by going *narrower* than the parent would bother with.

---

## Pattern D — Curated AI-generated data product

**Shape**: AI scrapes, cleans, and structures public data into a high-value-per-row dataset. Sold as a subscription, an API, or a downloadable report. Often refreshed weekly/monthly.

**Why it works**: Data buyers (sales, recruiting, research) have budget. AI replaces manual analysts who used to do this. Cost-to-serve is low and bounded.

**Examples that have worked**:
- Job-board scrapers + AI-enrichment for specific industries.
- "Companies that just raised X" with AI-extracted decision-maker info.
- Monitoring-as-a-service for niche regulatory filings, court dockets, patent grants.

**Pitfalls**: ToS risk on the underlying sources. Data quality is the entire moat — if AI hallucinates rows, trust collapses.

---

## Pattern E — Niche-trained content site or tool that's *also* an audience

**Shape**: A free or freemium tool that solves a small problem for a specific audience. The tool acquires the audience; monetization is via paid tier, sponsorships, or a related higher-priced product.

**Why it works**: Distribution is the product. AI lets a solo founder ship the free tool fast.

**Examples that have worked**:
- Free calculators / generators that rank organically and feed a paid product.
- Job-board-style aggregators in narrow verticals.
- "Inverse" SEO plays — tools that consume long-tail search demand competitors abandoned.

**Pitfalls**: Slow burn before revenue. Risk of Google algorithmic shifts on AI-generated content. Best when the *tool itself* is the value, not the SEO content around it.

---

## Pattern F — AI-augmented expert network / agent-on-call

**Shape**: An AI agent acts as the always-on first line for a specific expert task. Founder is escalation path for the small fraction of cases AI can't handle.

**Why it works**: Buyers pay 24/7-availability premium. AI handles 80–95%. Founder time scales sub-linearly with users.

**Examples that have worked**:
- "Always-on assistant for X profession" where the assistant handles routine queries.
- Customer-service AI for a single niche where the founder also serves as the human escalation.
- AI-first triage layered on top of a specialist's existing practice.

**Pitfalls**: The 5% the AI gets wrong determines the brand. Liability needs to be carefully scoped. Founder availability for escalations becomes the bottleneck.

---

## Pattern G — Internal-tool-as-a-product

**Shape**: Founder built something for themselves or a former employer, realizes others have the same need, packages it as a product.

**Why it works**: The founder *is* the customer, so problem validation and product-market fit are partially solved. Distribution can leverage the founder's professional network.

**Examples that have worked**:
- Anything where the founder's day job exposed a real, paid pain — and the AI version is meaningfully cheaper or better.

**Pitfalls**: Founder may overestimate how generalizable their context is. Always validate with at least 5 customers outside the founder's immediate network.

---

## Anti-patterns (the seductive failure modes)

- **"AI for X" where X is huge and obvious** (AI for sales, AI for marketing, AI for HR). Funded teams own the broad spaces. Go narrow or go home.
- **AI agent platforms / agent marketplaces** — solving a problem no buyer has yet articulated, with brutal funded competition.
- **"ChatGPT but for [niche]"** — if the only differentiation is a system prompt, anyone can replicate the product in an afternoon.
- **B2C subscription apps without a viral mechanism** — solo founders can rarely afford the CAC.
- **Tools for other founders / creators** — low willingness to pay, oversaturated, founders are the worst customers.
- **AI-generated SEO content sites** — Google's posture, the brittleness of programmatic content, and the slow ramp make this fragile and time-intensive.

---

## How to use this when generating candidates

For each candidate idea you generate, you should be able to say:

> "This is a {Pattern letter} play in the {specific niche}. The buyer is {specific job title or persona}. The wedge is {what's specifically narrow about this version}. The AI leverage is {what AI now does that wasn't tractable before}."

If you can't fill in those four blanks crisply, the idea isn't ready. Either sharpen it or drop it.
