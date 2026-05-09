# Cross-skill handoff prompts

Every pitch (pass or fail) ships with a `handoff/` directory containing copy-pasteable prompts for `/hacky-hours`, `/teach-me`, and `/productionize-me`. The user reviews the season, picks a pitch they want to act on, and pastes the relevant handoff into the next skill — no synthesis required.

Failed pitches still get handoff packets, but the prompts are flagged so the user knows what they're walking into. The user might still choose to build a "failed" pitch — perhaps they disagree with the panel, perhaps they're using a different commitment mode for themselves, perhaps the pitch has personal meaning. The handoff respects that.

## handoff/hacky-hours.md

For users who want to ship the MVP. The prompt should give `/hacky-hours` enough context that it doesn't need to re-do the research.

```markdown
# Hacky-Hours handoff for {Pitch Name}

**Status from pitch meeting**: {decision spread, e.g., "2 INVEST, 3 INTERESTED, 2 SOFT-PASS"}
**Composite score**: {X.X}/10 in {commitment mode} mode
**Founder reflection**: {KEEP-PUSHING / RECONSIDER / PIVOT / KILL}
{If failed: "**Note**: This pitch did not pass the investor panel for {commitment-mode}. Read pitch-meeting/perception-gap.md before committing time."}

## Paste this into /hacky-hours

> I want to build {pitch name in plain language — one line}.
>
> The MVP scope is: {3–5 bullets from one-pager.md "v1 scope" section}.
>
> The buyer is: {ICP from one-pager.md, in concrete terms — name a job title, company size, industry}.
>
> The first 10 customers come from: {channel #1 from one-pager.md}.
>
> Tech stack assumptions: {languages / frameworks / APIs / hosting from research.md, if specified; otherwise let /hacky-hours decide}.
>
> Validation criteria before paid launch: {2–3 specific gates — e.g., "30 cold emails to {audience} yield ≥2 paid signups"}.
>
> My time commitment: {hours/week per the chosen commitment mode}.
>
> Hard constraints: {anything from _brief.md hard exclusions, e.g., "no PII handling", "must run on a Mac mini"}.
>
> Risks I want to keep front-of-mind: {top 3 from red-team.md}.

## Files in this pitch directory that /hacky-hours might want to consult
- `../one-pager.md` — full executive summary
- `../research.md` — market + competitor + unit-economics research
- `../red-team.md` — strongest objections and answers
- `../pitch-meeting/perception-gap.md` — where investors and the founder disagreed
```

## handoff/teach-me.md

For users who want to learn the skills before building. Especially useful for pitches where the founder profile is "learn this then build" rather than "already a domain expert."

```markdown
# Teach-Me handoff for {Pitch Name}

## Paste this into /teach-me

> I want to learn the skills needed to build {pitch name in plain language — one line}.
>
> Specifically I need to learn: {extracted skills list from product scope, e.g., "the Shopify App Store API, basic OAuth flow, Polaris React components, and Shopify-app billing model"}.
>
> My current background: {founder profile from _brief.md and any user-supplied delta}.
>
> Goal: ship MVP in {timeframe consistent with commitment mode}.
>
> I learn best by: {let user override if they have preferences; otherwise default to "building small projects that compound toward the MVP"}.
>
> Constraints: {time per week per commitment mode}.

## Files in this pitch directory that /teach-me might want to consult
- `../one-pager.md` — what we're building
- `../research.md` — domain context and competitor study material (real apps to read source / docs for)
```

## handoff/productionize-me.md

For users who already shipped a v1 (perhaps via /hacky-hours) and want to harden it. The prompt highlights mode-appropriate production concerns — passive-income mode doesn't need enterprise SOC 2; full-time-business mode does.

```markdown
# Productionize-Me handoff for {Pitch Name}

**Production tier expected for {commitment mode}**: {e.g., "Tier 1 — passive ops, no PII, 99% uptime is fine, no SOC 2"}

## Paste this into /productionize-me

> I have a {tech stack} v1 of {pitch name}. I need to harden it for production at the {commitment mode} level.
>
> Key concerns specific to this pitch:
> {list extracted from research.md regulatory/platform/model risk section}
>
> Production tier I'm targeting:
> - **Uptime**: {e.g., "99% — best-effort. Not a 24/7 ops team."}
> - **PII**: {e.g., "None handled per the pitch's no-PII constraint."}
> - **Compliance**: {e.g., "None. State bar listing requires basic operational disclosure."}
> - **Observability**: {appropriate level for the mode}
> - **Scale ceiling**: {realistic — passive-income tier doesn't need 10,000 RPS}
>
> What I do NOT want: {anything mode-mismatched, e.g., "I do not want a SOC 2 roadmap. I do not want CI for 3+ environments. I do not want a feature flag service for a product with one user-facing toggle."}
>
> Hard constraints from the original pitch: {from _brief.md}.
>
> Existing stack in v1: {from /hacky-hours output if available, else describe}.

## Files in this pitch directory that /productionize-me might want to consult
- `../one-pager.md` — what the product does
- `../research.md` — regulatory/platform/model risk to bake into the production plan
- `../red-team.md` — known failure modes the production hardening should address
```

## How to compose these per-pitch

Use the templates above as base templates. Per-pitch fill-ins come from:

- **one-pager.md** → buyer, MVP scope, distribution, pricing
- **research.md** → tech stack hints, regulatory concerns, unit economics
- **scorecard.md** → headline decision spread + composite score
- **red-team.md** → top risks the next skill should address
- **pitch-meeting/perception-gap.md** → flag for user that the room and founder disagreed
- **_brief.md** → commitment mode, hard exclusions, founder profile

## What to do if a pitch is a clear FAIL

If the panel scored a pitch poorly and the user shouldn't pursue it, the handoff prompts still get written, but with a **"Don't do this" preface**:

```markdown
# Hacky-Hours handoff for {Pitch Name}

⚠️ **The panel rated this pitch poorly** — composite {X.X}/10, {N PASS decisions}. Read `../pitch-meeting/perception-gap.md` and `../red-team.md` before deciding to build it. The most likely failure modes are: {top 2 from red-team.md}.

If you want to build it anyway (sometimes the right call — panels are wrong sometimes), here's the handoff prompt...

> [normal handoff prompt]
```

The user might still build a 3/10 pitch — maybe they have unique context the panel didn't model. The handoff respects that, but doesn't pretend the pitch was great.

## Mode-specific handoff tweaks

The "production tier" and time-commitment language in `productionize-me.md` should match the commitment mode. Examples:

| Mode | Production tier suggested | Time-commitment language |
|---|---|---|
| Passive-income | Tier 1 — best-effort uptime, no on-call, no compliance | "≤ 2 hr/wk steady-state" |
| Part-time solo | Tier 1 — 99% uptime, basic monitoring | "5–15 hr/wk" |
| Full-time solo | Tier 2 — 99.5% uptime, real monitoring, basic incident playbook | "30–50 hr/wk" |
| Part-time team | Tier 2 — 99.5% uptime, shared on-call across 2–3 | "Founder PT + 1–2 collaborators PT" |
| Full-time team | Tier 2/3 — 99.9% uptime, structured on-call | "Founder FT + 2–4 FT" |
| Part-time biz/startup | Tier 3 — 99.9% uptime, formal incident process, light SOC 2 prep | "PT founder building toward FT" |
| Full-time biz/startup | Tier 3/4 — 99.95% uptime, real SOC 2 if customer-facing, on-call rotation | "FT founder + hires" |
| Unicorn | Tier 4 — 99.99% uptime, full SOC 2 / ISO, multi-region, eng-org-grade | "FT funded team" |

Pick the row that matches the pitch's commitment mode and use it in the productionize-me handoff prompt.
