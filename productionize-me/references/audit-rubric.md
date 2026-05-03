# Audit Rubric

The fourteen dimensions this skill audits, what "good" looks like at each tier, and how to write up findings.

## How to use this file

For each dimension below:
1. Find the row matching the user's chosen tier
2. Compare the codebase to the "Production at this tier" column
3. Score: 🔴 Missing · 🟡 Partial · 🟢 Production-ready (at this tier)
4. Capture specific findings with `file:line` references
5. Skip dimensions marked "N/A at Tier X" if applicable

A 🔴 doesn't mean the codebase is bad — it means the dimension hasn't been addressed *yet at the chosen tier*. State it without judgment.

---

## The Dimensions

### 1. Code Quality & Structure
- **Tier 1:** Code runs. Names are roughly consistent. No giant duplicated blocks.
- **Tier 2:** Reasonable file/folder organization. A new dev could find things. Dead code mostly removed. No 500-line functions.
- **Tier 3:** Consistent style enforced (linter/formatter in CI). Module boundaries make sense. Complexity hot spots have been refactored or noted.
- **Tier 4:** Above plus: documented architecture decisions for non-obvious choices.

**What to look for:** Run a quick complexity scan (count files, longest function, deepest folder nesting). Note duplicated patterns. Note any file that's clearly "the dumping ground."

### 2. Testing & Verification
- **Tier 1:** Optional. If tests exist, they should pass.
- **Tier 2:** Tests exist for critical paths (auth, payment, data writes). Tests run automatically before merge.
- **Tier 3:** Above plus: integration tests for cross-module flows. CI gates merges on test pass. A small e2e or smoke suite for the happy path.
- **Tier 4:** Above plus: coverage threshold gates, mutation testing for critical code, regression tests for every prior production bug.

**What to look for:** Is there a test directory? Do the tests run? Do they pass? What's covered vs. what's risky-and-uncovered?

### 3. Security & Secrets
- **Tier 1:** No hardcoded secrets. `.env` in `.gitignore`. No credentials in git history.
- **Tier 2:** Above plus: secrets via env vars or a secret manager (not committed). Basic auth where data isn't public. Input validation on anything from a user.
- **Tier 3:** Above plus: real auth (sessions/tokens/OAuth, not toy auth). Authorization checks at every protected endpoint. Input validation via schema (Zod, Pydantic, etc.). Rate limiting on public endpoints. Dependency vulnerability scanning.
- **Tier 4:** Above plus: formal threat model. Penetration testing. Encryption at rest. Documented key management.

**What to look for:** `git log -p | grep -i "api_key\|password\|secret"` for leaked secrets. Check every route handler for auth/authz. Search for `eval`, `exec`, raw SQL string concatenation, raw shell concatenation.

### 4. Dependencies & Supply Chain
- **Tier 1:** Dependencies declared (`requirements.txt`, `package.json`, etc.). Optional pinning.
- **Tier 2:** Lockfile committed (`package-lock.json`, `poetry.lock`, `Cargo.lock`). No abandoned packages with known vulnerabilities.
- **Tier 3:** Above plus: automated vulnerability scanning (Dependabot, Renovate, or equivalent) in CI. License scanning (no GPL in proprietary code, etc.).
- **Tier 4:** Above plus: SBOM generated on build. Vendor management process for transitive deps that touch regulated data.

**What to look for:** Lockfile present? Run `npm audit` / `pip-audit` / `cargo audit` if applicable. Check for packages that haven't been updated in 3+ years.

### 5. Observability
- **Tier 1:** `print()` or basic logs. N/A formal observability.
- **Tier 2:** Error tracking integrated (Sentry, Rollbar, or equivalent). Logs go somewhere persistent.
- **Tier 3:** Above plus: structured logs (JSON or key=value). Metrics for traffic, latency, errors. Tracing if request paths cross >2 services.
- **Tier 4:** Above plus: audit logs for all sensitive actions, retained per regulatory requirement.

**What to look for:** Is there error tracking init code? Are logs structured or just `console.log`? Can you tell if a deploy went bad without SSHing in?

### 6. CI/CD & Deployment
- **Tier 1:** Deploys are documented even if manual ("ssh in, git pull, restart"). No deploys from random branches.
- **Tier 2:** Push to `main` → deploys automatically. Tests run before deploy. Rollback story exists (revert + redeploy is fine).
- **Tier 3:** Above plus: PR previews or staging environment. Deploys are atomic and observable. Rollback is one command and tested.
- **Tier 4:** Above plus: change management process. Deploys gated by approval for prod. Documented SDLC.

**What to look for:** Is there a `.github/workflows/`, `.gitlab-ci.yml`, `Dockerfile`, deploy script? Does the README say how to deploy? When did the last deploy happen?

### 7. Documentation
- **Tier 1:** README explains: what is this, how to run it locally, where to find help.
- **Tier 2:** Above plus: how to deploy, how to add a feature, where the data lives. `.env.example` listing every required variable.
- **Tier 3:** Above plus: runbooks for top 5 ops scenarios. ADRs for non-obvious architectural decisions.
- **Tier 4:** Above plus: SDLC, change management, incident response, data handling docs that survive regulatory review.

**What to look for:** Does the README let a new dev get to "running locally" in under 30 minutes? Does `.env.example` exist and match `.env`?

### 8. Configuration & Environments
- **Tier 1:** Config via env vars. Default values fail loud, not silent.
- **Tier 2:** Separate config for dev/prod. No prod credentials on dev laptops.
- **Tier 3:** Above plus: dev/staging/prod with parity. Feature flags for risky launches.
- **Tier 4:** Above plus: documented environment isolation (network, IAM, data).

**What to look for:** Are there magic strings or URLs hardcoded? Are dev and prod truly separate? Can you accidentally point dev at prod DB?

### 9. Data Handling & Privacy
- **Tier 1:** N/A unless storing data about real people. If yes, ask: is this OK?
- **Tier 2:** PII identified. Encryption in transit (HTTPS). Backups exist. Data deletion possible if a user asks.
- **Tier 3:** Above plus: privacy policy matches code reality. GDPR/CCPA basics: data export, deletion, retention. Encryption at rest for sensitive fields.
- **Tier 4:** Above plus: regulator-facing docs (HIPAA BAA, PCI scope docs, SOC 2 controls).

**What to look for:** What user data is stored? For how long? Is there a deletion path? Are backups encrypted? Is the privacy policy a copy-paste lie?

### 10. Performance & Scalability
- **Tier 1:** N/A unless something is slow enough to be annoying.
- **Tier 2:** Known slow paths are noted. No N+1 queries on the critical path.
- **Tier 3:** Above plus: caching where it pays. Load expectations documented. Indexes match query patterns.
- **Tier 4:** Above plus: capacity planning. Tested load scenarios for tier-appropriate volumes.

**What to look for:** Database queries inside loops. Synchronous calls that should be async. Missing indexes on frequently-filtered columns.

### 11. Reliability & Error Handling
- **Tier 1:** Failures don't corrupt data. App can be restarted.
- **Tier 2:** External calls have timeouts. Retries on idempotent operations. Errors don't silently disappear.
- **Tier 3:** Above plus: circuit breakers or backoff for unreliable external services. Idempotency keys on critical writes. Graceful degradation when dependencies are down.
- **Tier 4:** Above plus: tested DR scenarios. Documented RTO/RPO.

**What to look for:** Bare `try: ... except: pass`. External calls without timeouts. Money-affecting writes that aren't idempotent.

### 12. Operational Readiness
- **Tier 1:** N/A.
- **Tier 2:** N/A. The user IS the operator.
- **Tier 3:** Runbooks for: deploy bad, DB down, third-party API down, data corrupted, secret leaked. Alerting on user-visible signals.
- **Tier 4:** Above plus: 24/7 on-call rotation, paging, incident response with documented timelines.

**What to look for:** If 3am on a Saturday and it's down, what happens? Is anyone alerted? Is there a runbook?

### 13. Accessibility
- **Tier 1:** N/A unless there's a public UI.
- **Tier 2:** N/A unless there's a public UI. If yes, semantic HTML and reasonable keyboard nav.
- **Tier 3:** WCAG 2.1 AA. Alt text. Keyboard nav. Color contrast. Tested with a screen reader at least once.
- **Tier 4:** WCAG 2.1 AA + tier-specific accessibility regulation (e.g., Section 508 for US gov-adjacent).

**What to look for:** `aria-*` attributes used correctly. Form labels. Color used as the only indicator. Click handlers on non-button elements.

### 14. Licensing & Compliance
- **Tier 1:** Repo has a LICENSE file (or explicitly notes "not licensed — all rights reserved").
- **Tier 2:** Above plus: dependency licenses don't conflict with intended use (no GPL in closed-source product without SaaS exception).
- **Tier 3:** Above plus: privacy policy and terms of service match code reality.
- **Tier 4:** Above plus: regulatory compliance documentation (whichever regs apply).

**What to look for:** LICENSE file present? Any GPL deps? Privacy policy promising things the code doesn't do (e.g., "we don't share your data" while sending events to 3 analytics SDKs)?

---

## Audit Template

Use this in `.productionize-me/AUDIT.md`:

```markdown
# [Project] — Production Readiness Audit

**Tier:** [Tier N — short description]
**Date:** YYYY-MM-DD

## Headline
[One paragraph. The most important findings — both strengths and gaps — in plain language. Not a spreadsheet, a summary a human would actually read.]

## Score Card

| # | Dimension | Current | Target (Tier N) | Notes |
|---|-----------|---------|-----------------|-------|
| 1 | Code Quality & Structure | 🟡 | 🟢 | ... |
| 2 | Testing & Verification | 🔴 | 🟢 | ... |
| ... | ... | ... | ... | ... |

## Findings by Dimension

### 1. Code Quality & Structure — 🟡 Partial
**What's there:**
- [Specific observation with file:line]

**What's missing for Tier N:**
- [Specific gap]

**Recommended actions:**
- [Concrete change, sized S/M/L]

[Repeat for each non-N/A dimension.]

## Out of Scope / N/A
- Dimension X — N/A at Tier N because [reason]

## What I'm Less Sure About
[Anything the audit couldn't determine without more info from the user. Be honest.]
```

---

## Priority Heuristics

When converting findings into the plan (Phase 3), use this rough priority logic:

- **P0 (blocks production):** anything 🔴 in Security, Data Handling, or Reliability at the chosen tier. Anything that could leak user data, lose user data, or charge a user the wrong amount.
- **P1 (should ship before launch):** anything 🔴 in Testing, CI/CD, Configuration, or Documentation at the chosen tier. The "rough edges that bite once you have users" tier.
- **P2 (improve over time):** 🟡 in any dimension. Things that work but could be better.

Don't blindly apply this. A 🔴 in Performance might be P0 if the use case actually depends on it (e.g., an LLM streaming app where latency matters). Use judgment and explain it.
