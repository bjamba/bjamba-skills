# Retrospective Artifacts

A mature software team maintains a set of documents that explain *why* the codebase looks the way it does — architecture diagrams, ERDs, design docs, ADRs, roadmaps, runbooks. When a codebase has been built fast (hackathon, prototype, "I just wanted to see if the idea worked"), these usually don't exist.

This skill can generate them retrospectively, by reading the code and inferring what *should have been* documented if the team had been working at production rigor from day one.

The structure deliberately echoes the [Hacky Hours](https://github.com/empathetech/hacky-hours-docs) framework, so a project graduating from prototype to production lands in a familiar shape.

---

## When to generate

Offer retrospective artifacts:
- Whenever the user has reached Phase 1 (Discover) and the codebase clearly lacks structured docs
- When the user explicitly asks for "design docs", "architecture diagram", "ERD", "roadmap", "runbook"
- As an optional add-on after the audit, before or alongside execution
- During Path C (greenfield) — these become the *forward-looking* design docs for the new build

Don't auto-generate everything. Pick artifacts that are useful for *this* codebase at *this* tier:
- A CLI tool doesn't need user journeys
- A static site doesn't need an ERD
- A solo personal tool may only need ARCHITECTURE.md and README

Always present a menu and let the user pick. **Default selections** are listed per artifact below.

### Doc-set floors (the minimum, not the menu)

Each tier has a *floor* — the doc set below which the codebase cannot honestly be called productionized at that tier. The "menu" approach above means picking *which* docs from a wider list, not whether to produce *any*. At Tier 2+ a sparse "ARCHITECTURE.md only" output is incomplete.

**Tier 1 floor:** `README.md` (always — see scaffolding) is sufficient. Retrospective design docs are optional. Generate `ARCHITECTURE.md` only if the system is non-obvious from the README.

**Tier 2 floor (must be present):**
- `docs/README.md` — index + navigation hub
- `docs/02-design/ARCHITECTURE.md` with Mermaid diagram
- `docs/02-design/DATA_MODEL.md` with Mermaid ERD (or note + reasoning if no persistent data)
- `docs/02-design/SECURITY_PRIVACY.md` — even short. The "known gaps" section is the load-bearing part.
- At least one ADR in `docs/adr/` — if the codebase has *no* non-obvious decisions, write the ADR explaining that and the design defaults

**Tier 3 floor (everything from Tier 2, plus):**
- `docs/02-design/USER_JOURNEYS.md` if there's a UI — top 3 paths
- `docs/runbooks/` — at least 2 runbooks for the highest-probability failure modes you can identify from the audit
- `docs/03-roadmap/ROADMAP.md` — Now/Next/Later/Won't synced with `PLAN.md`
- `SECURITY.md` at repo root (vulnerability disclosure path)

**Tier 4 floor:** Tier 3 + compliance scaffolding *placeholders* (DPA template, data flow diagram with regulatory boundary, retention/deletion docs). Defer to compliance partner for the real artifacts; produce the structure.

**The point of the floor:** a reviewer walking into a Tier 2 codebase that has *only* `ARCHITECTURE.md` should reasonably conclude "this is partially documented." A reviewer walking into one with the full Tier 2 floor should conclude "this team takes documentation seriously." The skill's success is measured against the second standard.

---

## Where artifacts live

By default, write to `docs/` in the repo root, organized by step (mirroring Hacky Hours):

```
docs/
├── 01-ideate/
│   ├── PRODUCT_OVERVIEW.md
│   └── IDEATION.md          (only if generated — usually skipped retrospectively)
├── 02-design/
│   ├── ARCHITECTURE.md
│   ├── DATA_MODEL.md
│   ├── USER_JOURNEYS.md
│   ├── SECURITY_PRIVACY.md
│   ├── STYLE_GUIDE.md
│   └── diagrams/
│       └── *.mmd            (Mermaid source for any diagrams)
├── 03-roadmap/
│   └── ROADMAP.md
├── 04-build/
│   ├── BACKLOG.md
│   └── CHANGELOG.md         (or move to repo root if preferred)
├── adr/
│   ├── 0001-<title>.md
│   └── ...
└── runbooks/
    └── <scenario>.md
```

If the repo already has a `docs/` folder with a different structure, ask before overwriting. Don't shoehorn — adapt.

---

## The Artifacts

### PRODUCT_OVERVIEW.md (Step 1)

**Default for:** any project with users (humans or other systems) — not strictly needed for libraries.

A one-page summary of who, what, where, when, why. Reverse-engineer this by reading the README, the entry points, and any user-facing strings. Confirm with the user — they often have unstated context that's not in the code.

```markdown
# [Product Name] — Overview

## Who
- **Primary users:** [inferred from code: e.g., "engineers running this CLI from a terminal"]
- **Secondary users:** [admin? end users of those engineers' work?]

## What
[2–4 sentences: the form factor (CLI / web app / mobile / library / service) and the core function.]

## Where
[Where it runs: localhost, hosted at X, distributed via Y.]

## When
[Rough lifecycle: prototype, beta, production. What's the next milestone?]

## Why
[What problem this solves. The "why" is rarely in the code — ask the user.]
```

### ARCHITECTURE.md (Step 2)

**Default for:** anything beyond a script.

The single most useful retrospective artifact. Map: what runs where, how data flows, what's external, what's the entry point.

Generate from:
- Entry-point file(s)
- Top-level folder structure
- External-call sites (HTTP clients, DB clients, third-party SDKs)
- Deployment files (Dockerfile, k8s manifests, terraform, serverless config)

Always include a **Mermaid diagram**. Even a rough one is more useful than prose.

```markdown
# Architecture

## Overview
[2–4 sentences. What kind of system is this — monolith, client+server, services, lambda, library, CLI?]

## Diagram

\`\`\`mermaid
flowchart LR
    User[User] --> Frontend[Web App<br/>React, Vite]
    Frontend --> API[API Server<br/>Node, Express]
    API --> DB[(Postgres)]
    API --> Stripe[Stripe API]
\`\`\`

## Components
| Component | Path | Purpose | Tech |
|-----------|------|---------|------|
| Frontend | `web/` | UI for end users | React + Vite |
| API | `api/` | Business logic, persistence | Node + Express |
| Worker | `worker/` | Async jobs | Node |
| Database | (managed) | Persistent data | Postgres on Supabase |

## Data flow
[Trace the most important request end-to-end. e.g., "User clicks Submit → POST /api/orders → API validates → writes to DB → enqueues job → returns 201."]

## External dependencies
| Service | Purpose | Failure mode |
|---------|---------|--------------|
| Stripe | Payments | Order creation fails |
| Postmark | Email | Email queued, retried |

## Notable design decisions
- [Decision] because [reason]. See `docs/adr/0001-...`.
```

### DATA_MODEL.md (Step 2)

**Default for:** anything that persists data (DB, files, blob storage, durable queues).

Reverse-engineer from migrations, ORM models, schema files, or `CREATE TABLE` statements. Include an **ERD via Mermaid**.

```markdown
# Data Model

## Diagram

\`\`\`mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered as"

    USER {
        uuid id PK
        text email
        timestamp created_at
    }
    ORDER {
        uuid id PK
        uuid user_id FK
        text status
        numeric total
    }
    ORDER_ITEM {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
    }
    PRODUCT {
        uuid id PK
        text name
        numeric price
    }
\`\`\`

## Entities
[For each entity: purpose, key fields, lifecycle, retention.]

## Sensitive data
[What's PII? What's encrypted at rest? What has retention requirements?]

## Migrations
[Where they live, how they run, are they reversible.]
```

### USER_JOURNEYS.md (Step 2)

**Default for:** anything with a UI or human-driven workflow.

The 3–5 most important paths a user takes. Reverse-engineer from routes, page components, or CLI subcommands.

```markdown
# User Journeys

## Journey 1: First-time signup
\`\`\`mermaid
flowchart TD
    A[Land on /] --> B[Click Sign Up]
    B --> C[/auth/signup form]
    C --> D[Verify email]
    D --> E[Onboarding flow]
    E --> F[Dashboard]
\`\`\`

**Touchpoints:**
- `web/pages/index.tsx` — landing
- `web/pages/auth/signup.tsx` — form
- `api/routes/auth.ts:signup` — backend
- Email sent via Postmark

[Repeat for journeys 2–N.]
```

### SECURITY_PRIVACY.md (Step 2)

**Default for:** Tier 2+. Anything that handles user data.

Document the security and privacy posture *as it actually is*, not aspirationally. The audit (Phase 2) will already have flagged gaps — this doc is a snapshot of current reality, with explicit "known gaps" section.

```markdown
# Security & Privacy

## Auth
[How users authenticate. Sessions, tokens, OAuth providers.]

## Authorization
[Role model. What can users do vs admins.]

## Data classification
[What's stored, what's PII, what's secret.]

## Encryption
- In transit: [HTTPS everywhere? Certificate management?]
- At rest: [DB-level? Field-level? Backups?]

## Secrets management
[Where secrets live. How they rotate.]

## Third-party data sharing
[Every service that receives user data. What they get. Why.]

## Known gaps (from audit)
[Honest. These will be fixed per the plan.]
```

### STYLE_GUIDE.md (Step 2)

**Default for:** anything with a UI.

Document the design system as observed: colors, typography, spacing scale, component patterns. Useful for designers joining and for keeping consistency as the codebase grows.

### ROADMAP.md (Step 3)

**Default for:** any project that's planning more work (i.e., almost all of them).

Convert the productionize plan plus the user's product wishlist into a tiered roadmap.

```markdown
# Roadmap

## Now (this milestone)
- [Plan items from M0/M1]

## Next (next 1–3 months)
- [M2 items + product priorities]

## Later (>3 months)
- [M3+ + aspirational]

## Won't (consciously deciding not to)
- [Things considered and dropped, with reasoning]
```

### BACKLOG.md (Step 4)

**Default for:** active development.

Per-task list. Each item: title, branch name, version target, definition of done, link back to the design doc that motivates it.

### ADRs (Architecture Decision Records)

**Default for:** Tier 2+ where there are non-obvious choices in the code.

One ADR per non-obvious decision. Format (Michael Nygard style):

```markdown
# 0001 — Use Postgres rather than Mongo

**Status:** Accepted (retrospective)
**Date:** 2026-05-02

## Context
[The situation that forced a choice.]

## Decision
[What was chosen.]

## Consequences
[Tradeoffs — both good and bad.]

## Alternatives considered
[What was explicitly rejected.]
```

Generate ADRs for choices that future-you would want explained: framework picks, custom auth instead of off-the-shelf, unusual data store, polyglot decisions, build tool choices.

### Runbooks

**Default for:** Tier 3+.

One runbook per failure mode that an operator could realistically face. Format:

```markdown
# Runbook: Database is down

## Symptoms
- API returns 500 with "ECONNREFUSED" on every request
- Sentry alert: DatabaseConnectionError spike

## Quick check
1. Is the DB host reachable? `pg_isready -h ...`
2. Is the DB process up? Check the managed dashboard at [url].
3. Is it a credential issue? Recent secret rotation?

## Mitigation
[Step by step.]

## Escalation
[Who to page if the above doesn't resolve in N minutes.]

## Post-incident
[Open an incident doc, run the postmortem template at docs/templates/postmortem.md.]
```

---

## How to generate these well

1. **Read before writing.** Don't draft `ARCHITECTURE.md` from a file tree alone — read the entry points, the routing layer, the deploy config. Real diagrams require real understanding.

2. **Use Mermaid liberally.** A diagram beats three paragraphs of prose. Every architecture and data-model artifact gets one.

3. **Be honest about gaps.** A retrospective `SECURITY_PRIVACY.md` that paints a rosy picture is worse than no doc. If the answer to "How does authorization work?" is "it doesn't, every authenticated user can hit every endpoint," write that. Then it goes in the audit/plan as a P0.

4. **Confirm with the user.** Especially for `PRODUCT_OVERVIEW.md`, `WHY` sections, and roadmap intent — these aren't fully derivable from code. Generate a draft from what you can see, present it, and ask the user to fill in the gaps.

5. **Don't over-produce.** Five honest, used artifacts are better than fifteen artifacts that nobody reads. Pick what's actually useful and skip the rest. A solo prototype probably doesn't need `STYLE_GUIDE.md` even if there's a UI.

6. **Wire them together.** Every artifact links to the others it references (`See ARCHITECTURE.md § Data Flow` etc.). Coherent doc set > pile of disconnected docs.

7. **Mark them as retrospective.** Every artifact gets a top note: `*Drafted retrospectively from existing code. Confirmed by [user]. Last updated YYYY-MM-DD.*` This makes it clear these aren't original design docs.

---

## Voice and polish: write like a team, not like an LLM

This is the difference between docs that feel like *team-grade artifacts* and docs that feel like *Claude's notes pasted into a markdown file*. The skill should produce the former — a person walking into the repo should feel "this was built by a team that takes documentation seriously," not "an LLM analyzed this codebase."

### Voice rules (apply to every retrospective doc)

**Use first-person plural / institutional voice — "we", "our system", "this service" — not second-person ("you have", "your codebase") or first-person singular ("I noticed", "I think").**
- ❌ "I noticed that you don't have backups configured."
- ✅ "We do not currently take database backups. See `docs/runbooks/restore-from-backup.md` once backups are wired in."

**Be declarative, not exploratory. Drop hedges, "may", "might", "could", "I'd recommend".**
- ❌ "It looks like you might want to consider adding rate limiting."
- ✅ "Public API endpoints have no rate limiting. Add per-IP limits in M0 (see `PLAN.md`)."

**Drop LLM tells.** No "Let me explain", "Great question", "Here's a summary of...", "I've drafted...", "It's worth noting", "In conclusion". A senior engineer writing a design doc would not write any of these.

**Reference specific files and lines.** Generic claims read as filler. `auth.py:42` reads as work product.

**Names, not pronouns.** "The `RefundService`" not "it". "The `users` table" not "the users". This is how reference documentation reads.

### Required metadata block (every retrospective artifact)

Every doc generated retrospectively starts with this front-matter block:

```markdown
---
title: [Doc title]
owner: [TBD or named team]
status: Living
last-reviewed: YYYY-MM-DD
generated: Retrospectively from codebase commit <sha-prefix> by productionize-me
---
```

This sets expectations: it's owned, it's a living doc, it has a date.

### Cross-linking and navigation

Every doc in the design set links to related docs at the **top** and **bottom**:

```markdown
**Related:** [`DATA_MODEL.md`](./DATA_MODEL.md) · [`SECURITY_PRIVACY.md`](./SECURITY_PRIVACY.md) · [`runbooks/`](../runbooks/)
```

The `docs/` folder gets a `README.md` index that lists every doc with a one-line description. A reader should be able to land in `docs/` and orient themselves in under 30 seconds.

### Diagram standards

Every Mermaid diagram has:
- A caption above (1 sentence: what this diagram shows)
- Real component names from the codebase, not generic placeholders
- Color or shape coding for trust boundaries (external services, persistent storage, user-facing surfaces)
- A "Source: [file:line]" line below if the diagram traces a specific code path

### Section structure

Each major artifact follows a consistent structure so readers know what to expect:
1. **Purpose** — one sentence, what this doc is for
2. **TL;DR** — 3-5 bullets, the load-bearing facts
3. **Body** — the substance, with consistent heading levels
4. **Open questions / known gaps** — explicit and dated. This is the part that distinguishes a real team's doc from a marketing doc.
5. **Related** — cross-links

### What a reader should *not* be able to tell

After reading the docs, a reader should not be able to tell:
- That they were generated retrospectively (until they read the metadata block, which is honest about it)
- That they were generated by an LLM (no rhetorical tics, no scaffolding language)
- That this codebase was vibe-coded (the docs accurately reflect current state, including the gaps, but read like a team that takes its documentation seriously)

The skill's success criterion: a reviewer who has never seen the codebase should be able to read the docs and feel oriented in 15 minutes. If they can't, the docs failed.
