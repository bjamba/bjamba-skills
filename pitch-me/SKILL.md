---
name: pitch-me
description: Generates research-backed startup pitches calibrated to a chosen commitment mode (passive-income → unicorn), simulates full pitch meetings between an AI-avatar founder and a panel of investor avatars composited from real, verified investors (with track records and a radar profile), produces voice-render-ready transcripts plus a visual-novel rendering of each meeting, scorecards that quantify the perception gap between founder and investors before vs. after the pitch, and handoff packets that plug into /hacky-hours, /teach-me, and /productionize-me. Use whenever the user asks for startup ideas, side-hustle ideas, indie-hacker ideas, "things I could build with AI", passive income concepts, AI SaaS pitches, micro-SaaS opportunities, niche revenue plays, or wants ideas vetted/scored/critiqued by simulated investors. Triggers on phrases like "/pitch-me", "pitch me N startups", "give me startup ideas", "what could I build solo with AI", "evaluate this startup idea", "make me a pitch deck", "score this idea like a VC", or whenever the user wants extensive, ready-to-act-on output they can review on their own time. Default behavior assumes solo founder + full-time job + passive-income commitment mode unless the user overrides — and in autonomous mode it runs end-to-end after one intake interview without further interruption.
---

# pitch-me

A skill for generating, researching, and stress-testing startup pitches calibrated to a chosen **commitment mode**, simulated as full pitch meetings between an AI-avatar **founder** and a panel of AI-avatar **investors** composited from real, verified people. The output is **extensive** — designed to be something the user can wake up to, spend an hour or two reading, and feed into other skills (`/hacky-hours`, `/teach-me`, `/productionize-me`) before writing a line of code.

The single most important variable is the **commitment mode** the user picks. Everything else — candidate generation, research depth, investor calibration, scoring distribution, pass thresholds — flexes to that mode. A pitch that scores 9/10 in passive-income mode would score 3/10 in unicorn mode, and vice versa. See `references/commitment-modes.md` for the eight modes and their rules.

## What changes vs. v1 (read this if you ran the older skill)

This is a deeper, more deliberate skill than the v1. The biggest changes:

1. **Commitment mode is now a first-class input.** v1 implicitly assumed "solo + passive-ish" and rated everything against that single bar. Most pitches that emerged were actually startup-trajectory ideas mislabeled as passive. v2 forces an explicit choice from eight modes (passive-income → unicorn) and calibrates investors, candidate generation, research depth, and scoring against the chosen mode.
2. **The 5-persona panel is now a 7-investor panel of verified composites.** The old "Indie-Hacker Operator / Pattern-Matching VC / Unit-Economics Hawk / Distribution Skeptic / Contrarian" archetypes were caricatures. They're now 5 stable composite avatars built from real people with verifiable track records (Pieter Levels + Marc Lou + Daniel Vassallo for the Bootstrapper; Roelof Botha + Marc Andreessen + Bill Gurley for the Growth VC; etc.) plus 1 rotating Domain Expert and 1 rotating Customer per pitch. Each avatar has a radar profile across consistent axes, and the user gets an investor-panel artifact summarizing who's in the room. See `references/investor-panel.md`.
3. **Pitches are now full simulated meetings, not just scorecards.** Every pitch produces a voice-render-ready transcript (clear `**SPEAKER:**` blocks, exportable to ElevenLabs / Play.ht / OpenAI TTS / Web Speech API) and a Shark-Tank-/Dragons'-Den-style visual-novel HTML rendering of the back-and-forth. The pre-pitch and post-pitch perceptions of every participant are captured separately, and a perception-gap analysis quantifies how much the pitch actually moved the room.
4. **N full-effort pitches always — failures are deliverables, not deletions.** v1 generated `2 × N` candidates and killed the weak ones. The user couldn't learn from the failures. v2 generates exactly N candidates with full effort on each one and produces the *complete* deliverable set for *every* pitch — including the ones that fail. The `_index.md` ranks them, but the failed pitches stay as first-class artifacts so the user can study why ideas fail. There is no kill list; the post-mortem is the kill list.
5. **Pitch-style mix is a Phase 0 input.** Default mix: 30% bold/novel ("out-there" creative swings), 30% niche (deep verticals AI hype skipped), 20% laser-focused (one specific painful problem), 20% solid/well-documented (proven pain, established categories). The user can override any of these at intake, including telling the skill to go all-bold or all-solid.
6. **Scoring is calibrated against documented optimism bias.** v1 scores clustered 7.6–8.4. The new `references/scoring-calibration.md` provides anchored distributions per commitment mode and explicit "what a 5 looks like, what a 7 looks like, what a 9 looks like" benchmarks so the panel doesn't just rubber-stamp.
7. **Storytelling is now a first-class output, not an afterthought.** `references/storytelling-lessons.md` distills patterns from real successful pitches (Airbnb's "airbed and breakfast", Stripe's "7 lines of code", Slack's category redefinition) and from canonical failures (WeWork narrative-without-math, Theranos demo-without-customers). Generated pitches must open with a customer moment, not market size.
8. **Cross-skill handoff packets.** Each pitch (pass or fail) ships with `handoff/hacky-hours.md`, `handoff/teach-me.md`, and `handoff/productionize-me.md` — copy-pasteable prompts for the user's other skills, pre-filled with full context. Failed pitches' handoffs surface the failure mode so the user can decide whether to pivot or skip.
9. **Season-recap landing page.** A run-level `season-recap.html` shows all N pitches as a Shark-Tank-/Dragons'-Den-style season, with each pitch as an episode. The user can binge-watch the season visually before deciding which one to actually build.
10. **Autonomous-by-default execution.** After one intake interview (Phase 0), the skill runs end-to-end without further interruption. The user is not asked anything else until everything is delivered.

## Default parameters

If the user doesn't specify, assume:

| Parameter | Default |
|---|---|
| `N` (number of pitches) | 10 |
| Industry / domain | Open — search broadly across software, content, services, marketplaces, info products |
| **Commitment mode** | **Passive-income** (software-version-of-passive-income; full-time job kept; ≤2 hr/wk steady-state ops) |
| Revenue floor (passive mode) | ≥ $1K MRR within 12 months, with credible path to $5K MRR within 24 months that does not require founder full-time switch |
| Founder profile (passive mode) | One person, has a full-time job, ≤ 10 hr/week available for build, ≤ 2 hr/week for ongoing ops, no co-founders, no hires, no physical product, no inventory, no in-person ops |
| Capital | $0–$500 to start. No outside funding. Tooling within standard AI-tool budgets ($20–$200/mo). |
| Tech stack | Off-the-shelf AI APIs + standard web tooling. No bespoke ML training, no GPU infra. |
| Pass threshold | Mode-calibrated. See `references/scoring-calibration.md`. |
| Time / token budget | Run until done. Do not interrupt the user mid-run. |
| Autonomous after Phase 0 | Yes. After intake confirms, run all phases without interruption and report only when all deliverables are written. |

The user can override any of these in their prompt. Honor what they say; only fall back to the defaults for anything they didn't specify.

## The pipeline

The skill runs in six phases. Use TaskCreate to track them so you don't lose your place across long runs.

### Phase 0 — Intake interview (BLOCKING; the only blocking interaction)

Before anything else, capture the user's intent in one structured pass. This is the *only* time the skill blocks for user input — after this, it runs autonomously to completion.

Ask using AskUserQuestion (or a single short message if context already provides answers):

1. **Commitment mode** — which of the 8 modes (see `references/commitment-modes.md`)? Default: passive-income.
2. **Domain / industry** — open, or specific (e.g., legaltech, fitness, e-commerce)?
3. **Hard exclusions** — anything off-limits (e.g., "no crypto", "must be B2B", "no PII")?
4. **Number of pitches** `N` — default 10. Every one of the N gets full effort and full deliverables, regardless of how the panel scores it.
5. **Pitch-style mix** — what proportion of the N should be bold/novel vs niche vs laser-focused vs solid/well-documented? Default 30/30/20/20. See `references/pitch-style-mix.md`.
6. **Founder profile delta** — anything different from the mode's default (skills, time, capital, audience, prior credibility)?
7. **Autonomous mode confirmation** — "I'll run this end-to-end without checking in further. Tell me now if you want me to pause anywhere." Default: full autonomous.

If the conversation already contains enough context (e.g., the user said "/pitch-me 10 dental SMB ideas at part-time-solo mode, all bold"), skip the interview and write the brief directly — but still confirm in one line.

Write the captured intake to `./pitches/_brief.md` and surface a one-paragraph confirmation. Then announce: "Going autonomous now. Will surface only when all deliverables are written."

### Phase 1 — Set up the investor panel

Read `references/investor-panel.md`. Select:

- **5 fixed investor avatars** (Bootstrapper, Operator-Investor, Seed VC, Growth/Unicorn VC, Skeptic) — these are stable across runs.
- **1 rotating Domain Expert** chosen for the run's domain. Build the composite from 3–5 real, verifiable practitioners or thinkers in the domain. (Web research is appropriate here to verify track record.)
- **1 rotating Customer** chosen as the average ICP buyer for the run's domain. Render as a person with name + occupation + situation.

Write `./pitches/_investor-panel.md` summarizing each avatar's composite, verified track record, radar scores across the 6 consistent axes, and bias profile per commitment mode. Generate `./pitches/_panel-radar.html` from `assets/panel-radar-template.html`.

### Phase 2 — Generate the candidate pool (exactly N)

Generate **exactly N** candidate ideas calibrated to the chosen commitment mode AND the chosen pitch-style mix. Each candidate is a one-paragraph thesis: who the customer is, what the painful job-to-be-done is, why now, and the rough monetization mechanism.

Distribute candidates across the user's pitch-style mix (see `references/pitch-style-mix.md`). With the default 30/30/20/20 mix and N=10, that's 3 bold/novel, 3 niche, 2 laser-focused, 2 solid/well-documented. Round to whole pitches, leaning toward more variety not less.

This is full effort, no buffer, no rescue runs. Every candidate gets the full Phase 3 + 4 + 5 treatment. If a candidate fails research or scoring, **it stays in the deliverables** as a documented failure — the user learns from the fails as much as from the wins.

Mode-specific filters apply. See `references/founder-fit.md` for the full filter (organized by commitment mode) and `references/idea-patterns.md` for proven solo-AI patterns.

Bias the pool toward ideas that:

- Sell to **businesses or professionals**, not consumers (better willingness-to-pay per unit of distribution effort).
- Use AI as the **delivery mechanism**, not the marketing hook ("AI-powered X" with no real AI leverage is weak).
- Have a **boring, identifiable buyer** with a budget line item already.
- Have **distribution paths the founder can actually walk at the chosen commitment level** (e.g., for passive-income mode, distribution must work without sustained sales calls or daily content production).

Avoid ideas that secretly require:

- A team or hires (unless the commitment mode permits)
- Physical fulfillment, inventory, or in-person ops
- Regulated activity the founder isn't already licensed for
- A two-sided marketplace with chicken-and-egg dynamics (unless one side is solved)
- Paid ads as the primary distribution
- Sustained personal-brand content production (unless the commitment mode permits)

### Phase 3 — Research each candidate

For each of the N candidates, do thorough web research using WebSearch and WebFetch. The research must produce, for each candidate:

- **Market** — TAM / SAM / SOM with cited sources (or triangulation math with cited inputs)
- **Competitors** — top 3–5 incumbents and 3+ indie/solo competitors with pricing, positioning, weaknesses
- **Customer evidence** — real quotes/posts from prospective buyers (Reddit, HN, niche forums, G2/Capterra)
- **Pricing benchmark** — what comparables charge; realistic ACV
- **Distribution channel evidence** — concrete examples of similar tools that won via the proposed channel, with public numbers if available
- **Regulatory / platform / model risk** — compliance, ToS, platform-policy, AI-provider risk
- **Unit economics** — cost-to-serve per customer at the proposed price; gross margin; breakeven count
- **Commitment-mode fit** — does the realistic effort profile match the mode? Flag if the idea is secretly more demanding than the mode permits.

See `references/research-checklist.md` for the source-quality bar and the per-candidate research note structure (saved as `./pitches/<slug>/research.md`).

**Research is honest, not protective.** If TAM is fake, dominant incumbents already own the wedge, distribution is unreachable, or unit economics break — record that clearly in research.md. Do not abandon the candidate; do not soften the findings to keep it alive. The pitch meeting will then carry that honest assessment forward, and the resulting failure becomes part of the user's learning material.

When parallel subagents are available, fan research out across candidates concurrently.

### Phase 4 — Run the pitch meeting (the core simulation)

For every one of the N candidates, run a full simulated pitch meeting. This is where the skill's value compounds. See `references/pitch-meeting-format.md` for the detailed structure; the high-level flow per pitch is:

1. **Pre-pitch perception survey** — every panelist (including the founder) rates the idea on three axes (good idea / viable / profitable, each 1–10) **without seeing the pitch deck**, based only on a one-line description and the candidate's domain. Captures the "cold opinion."
2. **Founder narrative** — the founder presents a story-led pitch (open with a customer moment, per `references/storytelling-lessons.md`), then walks through the deck.
3. **Q&A** — round-robin questions from each investor, founder answers, occasional inter-investor crosstalk. Aim for 25–45 dialogue turns. Investors stay in their composite voice (anchored by `references/investor-panel.md`); none of them caricature.
4. **Closing remarks** — each investor gives a 2–3 sentence final and a decision for the chosen commitment mode (`PASS` / `SOFT-PASS` / `INTERESTED` / `INVEST`) and a separate "best-fit commitment mode" note ("I'd pass on this at unicorn but it's an INVEST at full-time-solo").
5. **Post-pitch perception survey** — same three axes, now post-deck-and-Q&A. Captures perception shift.
6. **Founder reflection** — the founder writes a brief honest reflection on what landed, what didn't, and whether they'd KEEP-PUSHING / RECONSIDER / PIVOT / KILL.

Apply mode-calibrated scoring distributions per `references/scoring-calibration.md`. Don't cluster scores in 7–9; the calibration anchors are explicit and most pitches should land 4–6 in their target mode.

**Failures are first-class.** If the panel votes 5×PASS, that's a *legitimate documented failure* with full deliverables. The user wants to read those alongside the wins to learn the difference. Do not skip a pitch's deliverables because it scored badly. Do not soften the meeting transcript to make it less embarrassing — the realism is the value.

The "+1 change" round (apply each investor's suggested change and re-score) is **optional** for borderline pitches and is only useful if the user is going to act on the pitch. Run it for pitches scoring ≥ 6 average that fall short of the pass bar; skip it for pitches scoring lower (their failure is the lesson).

Run pitch meetings in parallel via subagents when available, since each is self-contained.

### Phase 5 — Produce the deliverables (full set for ALL N)

Every pitch gets the full deliverable set, pass or fail. The per-pitch directory:

```
./pitches/<slug>/
├── one-pager.md              # executive summary
├── deck.html                 # visual deck (filled from assets/deck-template.html)
├── research.md               # market research note (Phase 3 output)
├── scorecard.md              # per-investor + composite scoring (Phase 4 output)
├── red-team.md               # strongest objections + answers
├── pitch-meeting/
│   ├── transcript.md         # voice-render-ready full back-and-forth
│   ├── transcript.json       # structured turns (for visual novel + audio export)
│   ├── visual-novel.html     # Shark-Tank-style episode replay (with Web Speech API)
│   ├── pre-pitch-survey.md   # founder + investor perceptions BEFORE pitch
│   ├── post-pitch-survey.md  # same perceptions AFTER pitch
│   └── perception-gap.md     # analysis of how perceptions shifted
├── meeting-summary.md        # exec summary of the meeting (for skim-readers)
├── investor-feedback.md      # per-investor written feedback to founder
├── founder-reflection.md     # solo founder's response/reflection
├── handoff/
│   ├── hacky-hours.md        # ready-to-paste prompt for /hacky-hours
│   ├── teach-me.md           # ready-to-paste prompt for /teach-me
│   └── productionize-me.md   # ready-to-paste prompt for /productionize-me
└── meta.json                 # structured pitch metadata for cross-skill use
```

Plus run-level files at `./pitches/`:

```
./pitches/
├── _brief.md                 # the intake brief (Phase 0 output)
├── _investor-panel.md        # the panel for this run with profiles + radar
├── _panel-radar.html         # SVG radar visualization of panel biases
├── _index.md                 # all N pitches ranked, with one-line theses + decision
├── season-recap.html         # Shark-Tank-/Dragons'-Den-style season landing page
├── _post-mortem.md           # cross-cutting observations: what landed, what bombed, why
└── audio-rendering.md        # how to export transcripts to audio (Web Speech / ElevenLabs / etc.)
```

There is no `_killed.md`. Failed pitches are full deliverables in their own slug directory. The `_index.md` ranks all N and surfaces decisions; the `season-recap.html` lets the user binge the episodes; the `_post-mortem.md` synthesizes what the season teaches.

See `references/pitch-structure.md` for section-by-section content of each deliverable. See `references/handoff-prompts.md` for the handoff packet format. See `references/pitch-meeting-format.md` for transcript / audio / visual-novel guidance. See `assets/` for templates.

### Phase 6 — Final report to user

After all deliverables are written, surface to the user:

- One-paragraph summary of the run (N pitches generated, commitment mode, panel used, headline result spread — e.g., "2 INVEST / 4 INTERESTED / 3 SOFT-PASS / 1 PASS")
- Path to `./pitches/_index.md` and `./pitches/season-recap.html`
- Top 3 by composite score with their one-line theses
- Bottom 2 with one-line "why it failed" (so the user can decide whether to study them)
- Notable cross-cutting findings from `_post-mortem.md`
- A note that the per-pitch handoff packets are ready to paste into `/hacky-hours`, `/teach-me`, or `/productionize-me`
- A note about audio rendering options (`pitches/audio-rendering.md`) — the visual-novel HTML auto-plays via Web Speech API; ElevenLabs / OpenAI TTS / etc. instructions are in the doc.

## Communicating with the user during the run

The user has explicitly opted into a long, autonomous run. Do **not** interrupt to ask clarifying questions after Phase 0. If you genuinely cannot proceed without more information, write a checkpoint file (`./pitches/_blocked.md`), surface a single message asking for the missing piece, then resume.

Brief progress pings are OK — short status notes between phases ("Phase 2 done: 18 candidates generated, 6 killed in triage; Phase 3 research starting on the surviving 12") help the user follow along if they're watching, but do not block on a response.

Save intermediate state often so a partial run is recoverable. After every phase boundary, the workspace should be in a state where another agent could pick up where you left off.

If a token-budget concern arises (extremely long runs), surface it as a non-blocking note: "Running long; if you'd rather I tighten scope on remaining pitches, say so — otherwise I'll continue."

## Why these constraints matter

The whole skill is calibrated to produce output the user can act on without further synthesis. Every default and pattern exists because relaxing it tends to produce ideas that look good on a deck and die in execution:

- **Commitment mode is the master variable.** Most "great-sounding" startup ideas are mode-mismatched for the user's actual life. A pitch is only as good as its fit to the commitment mode the user can actually sustain.
- **Verified investor composites > caricatures.** When the panel is anchored to real, named people the user can look up, their feedback becomes calibration the user trusts. Caricatures invite eye-rolling.
- **Simulated meetings expose the perception gap.** What an investor thinks pre-pitch vs. post-pitch is the actual signal. A pitch that fails to move opinion is broken even if the score is fine.
- **Storytelling is the wedge.** Generated pitches without narrative all sound the same. Real pitches have a customer moment, a singular insight, a demo. The skill enforces this.
- **Anti-optimism calibration.** The default LLM tendency is to score 7–8 on every "reasonable-sounding" pitch. The calibration anchors fight that. Most pitches should score 4–6 in their target mode; only genuinely strong ones earn 7+.
- **Extensive output > terse output.** This skill produces a lot per pitch by design. The user wants something to wake up to and read carefully, not a tweet-length take.
- **Handoff packets close the loop.** A pitch that leads nowhere is a thought experiment. A pitch with a copy-pasteable `/hacky-hours` prompt becomes a project the user can actually start.

## Hitting N is non-negotiable; quality is what's variable

Always produce N pitches. Do not pad the candidate pool to manufacture wins, and do not censor failures. The fail outcomes are part of the deliverable — the user wants to read both wins and losses to develop intuition. The `_post-mortem.md` is where the lessons live.

If a domain or commitment mode is genuinely thin (e.g., unicorn mode in a tiny niche), it's fine for most of the N to score poorly — that's a signal worth surfacing, not a problem to hide.

## Reference files at a glance

- `references/commitment-modes.md` — the 8 modes (passive-income → unicorn) with rules per mode
- `references/pitch-style-mix.md` — bold/novel vs. niche vs. laser vs. solid mix; default 30/30/20/20
- `references/founder-fit.md` — hard/soft gates per commitment mode
- `references/idea-patterns.md` — proven solo-AI patterns to draw from
- `references/investor-panel.md` — the 5 fixed + 2 rotating avatars; verified composites; radar axes
- `references/pitch-meeting-format.md` — full simulation structure (pre-/post-survey, transcript, decisions, audio export)
- `references/storytelling-lessons.md` — patterns from real successful and failed pitches
- `references/scoring-calibration.md` — anchored distributions; what a 5/7/9 looks like per mode
- `references/research-checklist.md` — per-candidate research note structure and source-quality bar
- `references/pitch-structure.md` — per-deliverable content guidance
- `references/handoff-prompts.md` — templates for /hacky-hours, /teach-me, /productionize-me handoffs

## Asset files at a glance

- `assets/deck-template.html` — the pitch deck scaffold (existing, kept)
- `assets/transcript-template.md` — voice-render-ready transcript skeleton
- `assets/transcript.schema.json` — JSON shape for transcript turns (consumed by visual-novel and audio renderers)
- `assets/visual-novel-template.html` — Shark-Tank-style episode replay; bundles Web Speech API playback
- `assets/season-recap-template.html` — run-level "season landing" page linking all N episodes
- `assets/panel-radar-template.html` — radar chart for the panel
- `assets/meeting-summary-template.md` — meeting-summary skeleton

The skill's commitment is: every run produces exactly N full-effort pitches with the complete deliverable set, regardless of how the panel scored each one. The user's commitment is to read both the wins and the losses — the post-mortem is where the season's lessons compound.
