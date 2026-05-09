# Pitch-style mix

The user wants the N pitches to span a **range of styles**, not all conform to one shape. This file defines four styles and the default mix; the user can override the proportions in Phase 0.

The point of mixing styles is to inoculate the user against monoculture. If the skill only generated "solid documented problem" pitches, every run would feel the same — a list of slightly-different niche-CRM ideas. By forcing some bold/novel candidates into every run, the skill produces pitches that *might* fail spectacularly but that occasionally surface a genuinely interesting non-consensus idea.

## The four styles

### Bold / novel ("out-there")

Creative swings. Ideas that haven't been validated in market and might not work, but if they do, the upside is real. Often combines two unrelated capabilities, leans on a recent AI unlock, or proposes a category that doesn't fully exist yet.

**Examples of bold/novel framing**:
- "AI agent that listens to a podcast feed nightly and generates a personalized morning audio digest tied to your project context — paid via your podcast app's API."
- "Tool that converts any small business's Stripe history into a Loom-style 'state of the business' video for the founder, weekly."
- "Marketplace for retired CPAs to be on-call AI escalations for accounting AI tools."

**Why include them**: even when they fail in the meeting, they *teach the user something about the frontier*. The Skeptic and Domain Expert tear them apart with specific reasoning; that reasoning compounds over a season.

**Failure rate**: high. Expect bold pitches to score 3–6 on average. Occasionally one breaks 7+ and surprises everyone. That's the point.

### Niche

Deep verticals AI hype skipped — boring industries with documented incumbent dissatisfaction. Per the user's `project_2026_survival_patterns` memory: restaurants, contractors, fitness studios, dentists, photographers, real-estate investors, etc.

**Examples of niche framing**:
- "Tool that auto-tags inbound estate-sale leads for funeral directors based on death-notice scrapes."
- "Recurring automation for solo immigration lawyers that watches USCIS visa-bulletin changes and emails affected clients."
- "Vetted-supplier sourcing dashboard for solo Etsy POD sellers shifting away from Printful."

**Why include them**: niche is the highest-conviction source of solo-AI revenue. AI-vendor SaaS ignores them; bigger funded teams ignore them; the user can credibly own a small market.

**Failure rate**: moderate. Niche pitches are often dragged down by distribution (no obvious cold-email targeting) but have above-average unit economics.

### Laser-focused

A single specific painful problem solved end-to-end. Not "an X for Y" but "the way this one painful task gets done, replaced." Usually targets a workflow that takes 30 minutes today and could take 30 seconds with the right tool.

**Examples of laser framing**:
- "One-shot CSV-to-state-of-the-business audit for boutique fitness studio owners considering switching off Mindbody."
- "Inbox-zero rule generator for solo ops people who manage Stripe customer-support email."
- "Browser extension that watches LinkedIn and surfaces 'this person mentioned hiring' alerts for solo recruiters."

**Why include them**: laser pitches have the cleanest cold-email pitch-to-customer math. Easy to explain, easy to demo, easy to validate.

**Failure rate**: low. The risk isn't that they fail — it's that they cap out at small ARR.

### Solid / well-documented

Established categories with proven pain, clear incumbents, and empty solo-priced wedges. The "boring + identifiable buyer + budget line item already exists" pattern.

**Examples of solid framing**:
- "Standalone IOLTA reconciliation desktop tool for solo lawyers."
- "Insurance commission reconciler for independent agencies."
- "State-court docket monitor for solo plaintiff litigators."

**Why include them**: highest base rate of actually generating $1K MRR. Lowest learning value (the user already knows these categories exist) but the highest "I could build this next month" signal.

**Failure rate**: low when scoped right; high when the wedge is too narrow or distribution depends on a partnership the founder can't credibly pursue.

## Default mix

| Style | % | At N=10 | At N=20 |
|---|---|---|---|
| Bold / novel | 30% | 3 | 6 |
| Niche | 30% | 3 | 6 |
| Laser-focused | 20% | 2 | 4 |
| Solid / well-documented | 20% | 2 | 4 |

Round to whole pitches. Lean toward more variety (bold or niche) over less variety if rounding is ambiguous.

## How to use the mix in Phase 0

In intake, ask:

> Pitch-style mix — out of N pitches, what proportion should be:
> - Bold / novel ("out-there", high-risk-high-learn)?
> - Niche (deep boring verticals AI hype skipped)?
> - Laser-focused (one specific painful problem)?
> - Solid / well-documented (proven pain, clear incumbents, empty wedges)?
>
> Default 30/30/20/20. Common alternates: "all bold" (high-creativity run), "all solid" (ready-to-build run), "all niche" (vertical exploration), "no bold" (conservative)).

If the user has a clear preference, honor it. If not, take the default.

## How to apply the mix in Phase 2

When generating the candidate pool, **tag each candidate with its style** in the one-line thesis. Example:

```
1. [BOLD] AI agent that listens to your podcasts overnight and...
2. [NICHE] Inbound-lead auto-tagger for funeral directors...
3. [LASER] One-shot CSV audit for boutique fitness owners...
4. [SOLID] Standalone IOLTA reconciler for solo lawyers...
```

In Phase 5, surface the style tag in:
- `meta.json` (`"style": "bold"`)
- `_index.md` (column for style)
- `season-recap.html` (badge per episode card)

The user should be able to filter the season by style and see, e.g., "all the bold pitches" or "show me only solid ones."

## Mixing styles within a single pitch

Some pitches naturally span styles (a bold + niche fusion). Tag them with the dominant style, and note the secondary style in the candidate's one-line thesis.

## What NOT to do

- Don't generate four indistinguishable pitches and tag them "bold / niche / laser / solid" to satisfy the mix. Each style should *meaningfully differ* in shape.
- Don't over-rotate to bold pitches because they sound exciting. The default 30% is a ceiling for most users.
- Don't let bold pitches escape rigor. They still need full research and full meeting; the bar isn't "be defensible," it's "be honestly evaluated."
