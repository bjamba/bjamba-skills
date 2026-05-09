# Storytelling lessons

Generated pitches without storytelling all sound the same — they read like search-result summaries. The cure is to bake real-pitch storytelling patterns into how the founder narrative is constructed, and to study what canonical successes and canonical failures had in common.

This file is a working library of patterns. Read it before writing the founder's narrative for any pitch meeting.

## Patterns from successful pitches

### Pattern 1 — Open with a customer moment, not market size

**Example: Airbnb (2008 seed deck "AirBed & Breakfast")**

The pitch did not open with "the hospitality industry is a $X trillion market." It opened with a problem: "Conferences come to town. Hotels sell out. People can't find rooms. Hosts have empty space." A specific human friction, told in 12 seconds.

**The pattern**: First slide / first 30 seconds = a real customer in a real moment of pain. Market size comes later (or never — Stripe's pitch reportedly didn't have a TAM slide).

**Why this works**: investors hear 100 pitches a week. Numbers blur. Stories don't.

**For the skill**: every founder narrative must open with a 2–4 sentence customer moment. "Imagine you're a [specific buyer persona] and it's [specific time / situation] and you need to [specific painful action]..." Keep the buyer specific, the moment concrete, the pain visceral.

### Pattern 2 — Demo over description

**Example: Stripe (2010, Patrick Collison's pitch)**

The Collison brothers' pitch reportedly led with "7 lines of code to take a payment." Not a deck slide explaining the product — actual code. Anyone seeing this and the alternative (PayPal's API at the time, which required pages of integration work) understood the product instantly.

**The pattern**: if you can demo the product in 30 seconds, do that *before* you explain it.

**Why this works**: investors evaluate clarity-of-thought. A founder who can demo their own product in 30 seconds has thought hard about what the product *is*.

**For the skill**: in the founder narrative, after the customer moment, show what the *moment of value delivery* looks like. "Here's what they see: [specific UI / experience]. Here's what just happened: [the AI plumbing under the hood]." Don't describe features in a list; show the experience.

### Pattern 3 — Redefine the category

**Example: Slack (pre-launch 2013, Stewart Butterfield's narrative)**

Slack's original pitch wasn't "team chat." Butterfield's framing: "we're not selling chat, we're selling organizational transformation." This sounds grandiose, but the practical effect was that it took the product out of the saturated "chat tool" comparison and into a category where it had no direct comp.

**The pattern**: name what you're selling in a way that escapes the closest crowded comparison.

**Why this works**: investors auto-pattern-match new pitches against existing categories. If you let them place you in "X for Y" they'll discount you to the median of that category.

**For the skill**: where appropriate, the founder narrative can include a "we're not X, we're actually Y" reframe. Use it sparingly (once per pitch, not as a tic). Wrong-feeling reframes ("we're not a CRM, we're a relationship operating system") are red flags — make sure the reframe is *true*, not marketing.

### Pattern 4 — One sentence thesis, one sharp insight

**Example: Notion (early-stage, Ivan Zhao)**

Notion's thesis came down to "tools for thought, but composable like Lego." The contrast was Evernote's locked-in mental model. The single sentence carried both the product description and the contrast.

**The pattern**: the one-line thesis should *encode* the contrast against the closest incumbent. "[Product] is [thing], but [contrast that explains why it's different]."

**For the skill**: the one-line thesis in `one-pager.md` and the deck title slide must follow this pattern. "X is Y, but [specific contrast]." Not "X is Y. We're better." That's not a thesis, that's a brag.

### Pattern 5 — Why now, in one specific unlock

**Example: DocuSign (mid-2000s)**

The "why now" wasn't "people sign documents." It was "the ESIGN Act of 2000 made electronic signatures legally binding for the first time, and adoption has cleared the network-effect threshold." Specific regulatory unlock + specific adoption threshold. Anyone hearing this knew exactly *why* DocuSign could exist now and not in 1998.

**The pattern**: the "why now" must be one specific shift — a regulatory change, a technology unlock at a specific cost threshold, a behavior change tied to a specific event. Not "AI got better" — that's vapor.

**For the skill**: the one-pager and the deck must articulate the "why now" in **one sentence with one citable trigger**. If the trigger is "Anthropic shipped Claude for Word in April 2026," cite the date. If it's "Mindbody complaints crystallized post-2024 into a competitive set," cite the alternatives. Vague "AI is changing things" is not a why-now.

### Pattern 6 — Ground the unit economics

**Example: Square (early-stage, Jack Dorsey + Jim McKelvey)**

Square's pitch had specific numbers: small businesses pay X% to existing card processors, Square offers X% (lower) with simpler hardware. The unit economics were front-loaded; the story closed the deal.

**The pattern**: numbers + story, not numbers OR story. Story without numbers feels like spin; numbers without story feels like a spreadsheet.

**For the skill**: every founder narrative should anchor at least one unit-economic claim with a specific number ("API cost per customer per month is fifty cents at our usage") and at least one storytelling moment. Pure-numbers founder narratives sound robotic; pure-story narratives sound like marketing.

## Patterns from failed pitches

### Anti-pattern 1 — Narrative without math

**Example: WeWork (2019 IPO failure)**

The S-1 famously contained 169 instances of "community" and a vague claim about "elevating the world's consciousness." The unit economics behind the community story showed roughly $-13 per dollar of revenue. The story wasn't wrong, it was just unsupported by the math.

**The lesson**: a story that's contradicted by the math is worse than no story. Investors learn to discount sweeping language and demand the unit-economic anchor.

**For the skill**: any founder narrative that uses words like "transform", "revolutionize", "platform", "ecosystem", or "future of [X]" must back them with a specific unit-economic claim. If the claim doesn't exist, cut the word.

### Anti-pattern 2 — Demo without customers

**Example: Theranos**

The pitch had a demo (the pinprick blood test reading) but no customer evidence — no working customer, no published clinical trial, no third-party validation. The demo carried the story alone. When the demo turned out to be selectively curated, the story collapsed.

**The lesson**: a demo isolated from real customers is just a demo. Real pitches have at least one named customer, or one credible path to one.

**For the skill**: every pitch must include real customer evidence in research.md. The founder narrative should reference at least one named customer or named near-customer ("I emailed five solo dentists last week; here's what they said"). Hypothetical customers are fine for early-stage pitches but must be labeled hypothetical.

### Anti-pattern 3 — TAM without ICP

**Example**: countless rejected YC applications with "this is a $50B market" framing.

The lesson: nobody invests in TAM. They invest in your ability to credibly capture a tiny first slice of TAM. A $50B TAM with no clear ICP is a worse pitch than a $50M TAM with a named customer who's about to sign.

**For the skill**: TAM is fine in research.md as ceiling math. But the *founder narrative* should focus on the ICP — the specific buyer, the specific channel, the specific first ten customers — not the headline market size.

### Anti-pattern 4 — Reading the deck

The most common failure mode in real pitches isn't about strategy — it's that the founder *reads the slides verbatim* instead of using them as visual support. Investors can read; they want to hear what's not on the slide.

**For the skill**: in the transcript, the founder narrative should *reference* the deck ("on slide 3 you'll see…") but never recite slide bullets. The slides are visual scaffolding; the narrative is the spoken texture.

### Anti-pattern 5 — "AI-powered X" as the wedge

In 2026, "AI-powered" is wallpaper. Saying it isn't a differentiator. Investors auto-discount it.

**For the skill**: the founder narrative must *show what the AI specifically does* (per Pattern 2 above) and never use "AI-powered" as a stand-alone claim. If the only thing the founder can say about the AI is that it's there, the AI isn't actually doing anything.

## How to apply these in the founder narrative

When writing the founder's opening turn in the pitch meeting, check:

1. **Customer moment in the first 4 sentences?** (Pattern 1)
2. **Demo / "here's what they see" within the first 8 sentences?** (Pattern 2)
3. **One-sentence thesis includes the contrast against the closest incumbent?** (Pattern 4)
4. **Why-now references one specific unlock with one citable trigger?** (Pattern 5)
5. **At least one unit-economic claim with a specific number?** (Pattern 6)
6. **Avoids hype-words ("transform", "revolutionize") unless backed by math?** (Anti-pattern 1)
7. **Names a real or near-real customer?** (Anti-pattern 2)
8. **Talks about the ICP, not the TAM, in the spoken narrative?** (Anti-pattern 3)
9. **Doesn't read the deck verbatim?** (Anti-pattern 4)
10. **Doesn't use "AI-powered" as a stand-alone claim?** (Anti-pattern 5)

If a draft narrative misses 3+ of these, rewrite it. If it misses 5+, the underlying pitch is probably weaker than you thought — surface that to the meeting honestly.

## A note on the "playable" texture

The founder narrative is not just text in research.md — it's spoken in the simulated meeting. That means the writing should sound natural when read aloud. Test it: would an actual founder say this sentence? If it reads like a press release, rewrite it. Real founders say "look," "honestly," "here's the thing," and trail off mid-sentence sometimes.

That's not a license for filler — it's permission to make the dialogue *real*. The user is going to listen to this. Don't make them listen to a robot.
