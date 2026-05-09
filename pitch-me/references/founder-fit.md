# Solo-AI Founder Fit Filter

Use this to triage candidates *before* spending research budget on them. If a candidate fails any of the hard gates, kill it and pull the next one. Soft gates are scoring inputs, not vetoes.

## Hard gates (any failure → kill the candidate)

1. **Solo-buildable**: A reasonably skilled person using off-the-shelf AI tooling can build v1 in ≤ 80 hours of part-time work. If the v1 requires a team, custom ML training, native mobile fluency, or specialist domain certification the founder doesn't have, fail.

2. **Solo-operable at 1,000 customers**: At 1,000 paying customers, the operational load (support, ops, fulfillment, content) is still manageable in ≤ 10 hr/week. If serving each customer requires manual touch that doesn't go away, fail.

3. **No physical fulfillment**: No inventory, shipping, manufacturing, or in-person service delivery. Digital products and services only.

4. **No ongoing money pit**: Total monthly fixed cost to keep the business alive at 0 customers is ≤ $200/mo (hosting, AI APIs minimum tier, domain, basic SaaS subscriptions). If the business requires sustained paid ads or expensive infra to stay alive, fail.

5. **Legal & licensable**: The founder doesn't need a license they don't have (medical, legal advice, financial advisory, real-estate brokerage, etc.). Tools *for* licensed professionals are fine; *being* the licensed professional is not.

6. **Not platform-dependent in a fatal way**: If the entire business is "an app on the OpenAI store" or "a Shopify plugin" or "a ChatGPT custom GPT", flag the platform risk. Not always a kill, but the candidate must have a credible answer to "what if the platform deprecates this surface or builds it natively."

7. **Identifiable buyer**: The pitch can name the *exact job title and company size* (or persona, for B2C) of the first 10 paying customers. "Small businesses" is not identifiable. "Owner-operator HVAC companies in the US with 5–15 trucks who use ServiceTitan" is identifiable.

## Soft gates (penalize, don't kill)

- **Distribution-feasible for solo**: There's a concrete, named channel a solo founder without an existing audience can credibly walk. Penalize ideas whose only described channel is "content marketing" or "go viral on TikTok" without a structural reason that would actually work.

- **AI-leveraged, not AI-flavored**: AI does real work in the product, ideally work that wasn't possible at this cost 18 months ago. Penalize "ChatGPT wrapper around a thing that already worked fine without AI."

- **Defensibility is at least narrated**: There's some thesis on why this isn't trivially copyable in a weekend. Doesn't have to be a moat — could be data accumulated, integration depth, niche trust, or just speed of execution into a small market that's not worth a bigger team's time.

- **Founder won't burn out in 6 months**: The work pattern (sales calls? content production? customer support? night-shift monitoring?) is something a person with a full-time day job can sustain.

- **Pricing power exists**: There's a credible reason the buyer will pay at least $20–$50/mo (B2C) or $50–$500/mo (B2B). Sub-$20 B2C SaaS rarely supports a solo founder past hobby revenue without a million users — penalize unless there's a clear path.

- **Cost-to-serve is bounded**: AI inference + tooling cost per customer per month is < 30% of the revenue per customer per month, with a clear plan if usage spikes.

## Patterns that almost always fail these gates

- "Marketplace for X" — two-sided liquidity is brutal for a solo founder.
- "Social network for X" — needs people, network effects, moderation.
- "AI tutor for K-12" — regulatory + parent-side trust + content review.
- "AI therapist / mental health coach" — liability, regulatory, ethical landmines.
- "AI that writes legal/medical/financial advice for end users" — licensing.
- "Platform to help creators monetize" — chicken-and-egg, low willingness to pay, churn.
- "Better X for consumers" where X is anything Big Tech ships free.
- "AI-generated content site monetized by ads" — Google's algorithmic posture toward AI-generated content makes this fragile and time-intensive to maintain.

## Patterns that often pass

(See `idea-patterns.md` for detail.)

- AI-leveraged tools sold to specific professional niches.
- Workflow automations that replace a recurring expensive contractor task.
- "Productized service" delivered mostly by AI with thin human review.
- Integrations between two existing tools, where the integration itself is the product.
- Vertical-specific data products built by AI-curating public data.
