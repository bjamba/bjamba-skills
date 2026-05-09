# Founder Fit Filter (commitment-mode-aware)

Use this to triage candidates **before** spending research budget on them. The hard gates differ per commitment mode — a candidate that fails a hard gate for the chosen mode goes into the candidate pool tagged "expected-fail," but in v2 the skill still produces the full deliverable for it (per the "failures are first-class" principle in `SKILL.md`). The hard gates are signals to the panel, not deletions.

The soft gates are scoring inputs to the meeting.

## Mode-independent hard gates (apply to all modes)

These are the gates that fail any commitment mode:

1. **No physical fulfillment**: No inventory, shipping, manufacturing, or in-person service delivery. Digital products and services only.
2. **Legal & licensable**: The founder doesn't need a license they don't have (medical, legal advice, financial advisory, real-estate brokerage, etc.). Tools *for* licensed professionals are fine; *being* the licensed professional is not.
3. **Identifiable buyer**: The pitch can name the *exact job title and company size* (or persona, for B2C) of the first 10 paying customers. "Small businesses" is not identifiable. "Owner-operator HVAC companies in the US with 5–15 trucks who use ServiceTitan" is identifiable.
4. **Not catastrophically platform-dependent**: If the entire business is "an app on the OpenAI store" or a single-vendor's plugin and the platform's deprecation kills the business overnight, flag it. Not always a kill, but the candidate must have a credible answer to "what if the platform deprecates this surface or builds it natively."

## Mode-specific hard gates

### Passive-income mode

The strictest set:
- **v1 ≤ 80 hr** of part-time founder work
- **Steady-state ops ≤ 2 hr/wk** at 1,000 customers
- **Fixed monthly cost ≤ $200/mo** at 0 customers
- **No sustained sales calls, no daily content production, no community moderation**
- **Cost-to-serve ≤ 30%** of per-customer revenue
- **Distribution channel works without paid ads as primary**
- **API/inference costs flat or sub-linear with customer count**

Candidates that fail any of these in passive-income mode get the "expected-fail-passive" tag. They might still be wonderful pitches in a more demanding mode — note the "best-fit mode" in the meeting.

### Part-time solo mode

Relaxed:
- **v1 ≤ 200 hr** of part-time work
- **Steady-state ops ≤ 15 hr/wk** at 1,000 customers
- **Fixed cost ≤ $500/mo**
- **Day-job-compatible work pattern** (evenings/weekends sustainable)
- **No real-time customer support** (next-business-day OK)

### Full-time solo mode

Relaxed further. The founder does everything but is one person:
- **v1 buildable in ≤ 600 hr full-time**
- **Total burn ≤ 5% of target MRR**
- **Sustainable for 2+ years** without burnout
- **No need for hires** — if the idea requires "a part-time CS rep at 50 customers", it's mode-mismatched

### Part-time team mode

- **Founder PT + 1–2 PT collaborators** sustainable
- **No two-sided marketplace** unless one side is solved at launch
- **Defensible from revenue** without raising

### Full-time team mode

- **Founder FT + 2–4 FT teammates** affordable from revenue (or runway plan)
- **Hiring plan defensible** without raising
- **Real ops can absorb** 2–4 people's bandwidth

### Part-time business / startup mode

- **Path to $1M+ ARR within 24 months** while founder still PT
- **TAM ≥ $100M**
- **Distribution scales beyond founder-as-only-channel** within 12 months
- **Defensibility narrated** (data moat, integration depth, brand, network effects)

### Full-time business / startup mode

- **Path to $1M+ ARR within 12–18 months**
- **TAM ≥ $500M**
- **Founder ready to be CEO who hires** — solo full-time builders who don't want to manage anyone are mode-mismatched here

### Unicorn mode

- **Path to $100M+ ARR** with credible defensibility
- **Market is winner-take-most** or strong network effects
- **A top-5 seed VC would back it** over the next 100 they see
- **TAM ≥ $5B**

---

## Mode-independent soft gates (scoring inputs, all modes)

These don't fail a candidate; they show up in the scoring.

- **Distribution-feasible at the chosen mode**: There's a concrete, named channel the founder can credibly walk **at the chosen mode's time/capital constraints**. Penalize ideas whose only described channel is "content marketing" without a structural reason that would actually work.

- **AI-leveraged, not AI-flavored**: AI does real work in the product, ideally work that wasn't possible at this cost 18 months ago. Penalize "ChatGPT wrapper around a thing that already worked fine without AI."

- **Defensibility narrated**: Some thesis on why this isn't trivially copyable in a weekend. Doesn't have to be a moat — could be data accumulated, integration depth, niche trust, speed of execution into a small market not worth a bigger team's time.

- **Burnout-resistant work pattern**: The pattern of work (sales calls? content production? customer support? night-shift monitoring?) is sustainable for the chosen mode's time commitment.

- **Pricing power exists**: A credible reason the buyer will pay at least $20–$50/mo (B2C) or $50–$500/mo (B2B). Sub-$20 B2C SaaS rarely supports a solo founder past hobby revenue without a million users.

- **Cost-to-serve is bounded**: AI inference + tooling cost per customer per month is < 30% of the revenue per customer per month, with a clear plan if usage spikes.

## Patterns that almost always fail (for any solo mode)

- **"Marketplace for X"** — two-sided liquidity is brutal for solo founders unless one side is solved.
- **"Social network for X"** — needs people, network effects, moderation.
- **"AI tutor for K-12"** — regulatory + parent-side trust + content review.
- **"AI therapist / mental health coach"** — liability, regulatory, ethical landmines.
- **"AI that writes legal/medical/financial advice for end users"** — licensing.
- **"Platform to help creators monetize"** — chicken-and-egg, low willingness to pay, churn.
- **"Better X for consumers" where X is anything Big Tech ships free.**
- **"AI-generated content site monetized by ads"** — Google's posture toward AI-generated content makes this fragile.

## Patterns that often pass (see `idea-patterns.md`)

- AI-leveraged tools sold to specific professional niches.
- Workflow automations that replace a recurring expensive contractor task.
- "Productized service" delivered mostly by AI with thin human review.
- Integrations between two existing tools, where the integration itself is the product.
- Vertical-specific data products built by AI-curating public data.
- Marketplace-distributed niche tools (Shopify, Foundry, Webflow, Word, Etsy).
- Anti-subscription wedges with documented incumbent complaints.
- Human-taste moats (curated against AI-commoditized noise).
- AI-as-plumbing (workflow + UX + curated defaults; AI does non-text-gen work behind the scenes).

## How this interacts with the pitch-style mix

The pitch-style mix (`references/pitch-style-mix.md`) intentionally pushes some candidates outside the safe zone:

- **Bold / novel** candidates often violate one or two soft gates intentionally — that's part of being bold. The meeting will surface that as a real weakness.
- **Niche** candidates almost always pass hard gates; the question is whether the niche has enough volume.
- **Laser** candidates almost always pass hard gates and have clean unit economics; the question is ceiling.
- **Solid** candidates by definition pass all hard and most soft gates; the question is whether the wedge is large enough to be worth the effort.

Don't reject a bold candidate at the gate stage just because it violates a soft gate. The meeting is the right venue for that critique.
