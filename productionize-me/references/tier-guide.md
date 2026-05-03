# Production Tier Guide

Not every codebase needs the same level of rigor. Picking the right tier *first* is the single most important calibration decision in this skill — it prevents over-engineering personal tools and under-engineering systems that will hold real user data.

When in doubt, ask the user. When still in doubt after asking, lean **conservative** for anything touching user data, money, or health information; lean **lighter** for anything internal-only or single-user.

---

## The Tiers

### Tier 1 — Personal / Internal-only / Single-user

**Examples:** A weekend script you run from your laptop. A cron job that posts to your own Slack. A static dashboard only you see. A CLI tool used by one person. A localhost-only side project.

**Stakes if it breaks:** You are mildly annoyed for an hour.

**What's required:**
- Code runs and does the thing
- README explains how to run it (so future-you doesn't forget)
- Secrets aren't hardcoded (use `.env` + `.gitignore`)
- A `requirements.txt` / `package.json` / `go.mod` so it can be installed cleanly
- Recovery story for "I lost my laptop" — code is in version control somewhere

**What's NOT required:**
- Tests (nice to have, not required)
- CI/CD
- Observability beyond `print()` / basic logs
- Backups (unless it stores something irreplaceable)
- Multiple environments
- Runbooks

**Common over-engineering at Tier 1:** Suggesting Sentry, Terraform, Docker, structured logging, CI matrices, branch protection rules. Don't.

---

### Tier 2 — Small team / Internal business / Trusted users

**Examples:** Internal tool used by a 10-person team. A side business with a handful of paying customers. An app you're sharing with your friends and family. A SaaS pre-launch / closed beta. A service that integrates with one customer.

**Stakes if it breaks:** A handful of people are blocked. Some money may be on the line. The user gets pinged in Slack.

**What's required (everything from Tier 1, plus):**
- Tests on critical paths (auth, payment, data writes — wherever a silent failure costs the most)
- Automated deployment (push to `main` → deploys, or PR → preview → deploy)
- Error tracking (Sentry, Rollbar, or equivalent — free tiers are fine)
- Basic auth where appropriate
- Backups for any user data
- A way to roll back a bad deploy (revert + redeploy is sufficient)
- README is good enough for a teammate to set up locally without help
- Dependencies are pinned (lockfile committed)
- `.env.example` documents every required variable

**What's NOT required:**
- Full test coverage (cover what hurts most)
- Multi-region anything
- 24/7 on-call
- Formal incident process
- WCAG 2.1 AA (unless customer-facing)
- SOC 2 / ISO 27001

**Common over-engineering at Tier 2:** Microservices, Kubernetes, multi-cluster, distributed tracing, service mesh, GitOps. None of this is needed.

---

### Tier 3 — Customer-facing / Public SaaS / Real revenue

**Examples:** A SaaS product with paying customers. A consumer mobile app. A B2B platform with multiple customer accounts. Anything where downtime costs money or reputation.

**Stakes if it breaks:** Customers churn. Revenue lost. Public bug reports. Possibly press.

**What's required (everything from Tier 2, plus):**
- Real auth + authz (sessions, tokens, roles — not toy auth)
- Input validation at every trust boundary (use a schema validator)
- Rate limiting on public endpoints
- Audit logging for sensitive actions (admin actions, data exports, permission changes)
- Real observability: structured logs + metrics + error tracking. Tracing if request paths cross >2 services.
- Alerting on real signals: error rate, latency, availability — not "CPU > 80%"
- Runbooks for the top 5 things that can go wrong
- Staging environment that mirrors prod
- Database migrations are reversible and tested in staging
- Backups are verified (test the restore — backups you haven't restored are not backups)
- Privacy policy that matches what the code actually does
- WCAG 2.1 AA for any UI
- Dependency vulnerability scanning in CI
- A documented on-call story (even if "on-call" is one person)

**What's NOT (necessarily) required:**
- SOC 2 (unless your customers ask for it)
- Multi-region active-active
- Formal SRE practices
- Chaos engineering

---

### Tier 4 — Regulated / Safety-critical / High-stakes

**Examples:** Healthcare (HIPAA), payments (PCI-DSS), financial services, anything with HIPAA/PCI/GDPR/SOC 2 requirements, anything safety-critical (medical devices, automotive, industrial control).

**Stakes if it breaks:** Regulatory fines. Lawsuits. Real-world harm.

**Recommendation if the user lands here:** Be honest that this skill can audit and plan, but going to Tier 4 is rarely a thing one engineer does over a quarter — it usually requires legal, security, and compliance partnership. Recommend they engage a compliance advisor and treat the audit output as a starting point for a much larger conversation.

**What's required (everything from Tier 3, plus):**
- Formal threat model
- Encryption at rest AND in transit, with documented key management
- Strict access controls + audit logs that can survive a regulatory review
- Data retention and deletion policies that match the regulatory requirement
- Incident response plan with documented timelines
- Background checks / access reviews for engineers with prod access
- Penetration testing (regular, by a third party)
- Disaster recovery plan with tested RTO/RPO
- Vendor management for any third-party that touches regulated data
- Documented SDLC with code review, security review, change management

This skill is **not a substitute for compliance expertise** at Tier 4. Be explicit about that.

---

## How to Pick the Tier

Ask in this order — stop at the first "yes":

1. **Does this handle health information, payments, or fall under specific regulation (HIPAA, PCI, SOC 2 in scope)?** → Tier 4
2. **Will paying customers or the general public use this?** → Tier 3
3. **Will more than ~5 people who aren't you use this, or will it hold data those people would care if lost?** → Tier 2
4. **Otherwise** → Tier 1

If the user says "Tier 3, but we're pre-launch," still pick Tier 3 — the launch criteria is what we're auditing toward. If they say "Tier 1, but it might grow," pick Tier 1 *now* and note the upgrade path in the plan.

## Tier override: aspiring higher than the recommendation

After you (the skill) recommend a tier, **always offer the user the option to apply a higher tier's standards.** Some users want to overinvest in production rigor — for the practice, to graduate the codebase faster, to win an enterprise customer that demands it, or because they expect rapid growth.

How to offer it (in Phase 0):

> "Based on what you described, I'd recommend **Tier N** for this project (because [reason]). That sets the bar for the audit and plan. You can override it if you want to:
>
> - **Stay at Tier N** — recommended; everything is calibrated to your actual needs
> - **Aspire to Tier N+1** — apply a higher bar; we'll audit and plan against that, even though it's overkill for current usage. Useful for: graduating to a more mature posture, demonstrating rigor for a future customer, or just learning what one tier up looks like
> - **Aspire to Tier N+2 or higher** — possible but usually not advisable until the lower tier is solid"

If the user picks an aspirational tier:
- The audit scores against the *aspirational* tier (so more dimensions will be 🔴 or 🟡)
- The plan reflects more work, more milestones, more scaffolding
- Be explicit in `STATE.md`, `AUDIT.md`, and `CLAUDE.md`: "Recommended tier: N. Aspirational target: N+1. All gates calibrated to N+1."
- Don't silently downgrade in subsequent sessions — the chosen tier sticks until the user explicitly changes it

If the user picks a *lower* tier than recommended (e.g., "this app handles user data but I just want Tier 1 rigor for now"):
- Honor it, but **flag the divergence prominently** in `AUDIT.md` and `STATE.md`
- Note the specific risks they're accepting (data loss without backups, no encryption at rest, no breach response, etc.)
- Add a "Risks accepted" section to the audit so the choice is documented for future-them

The user owns the call. Your job is to make sure they're making it knowingly.

## Recalibrating Mid-Skill

If during the audit you discover something that suggests a different tier (e.g., "I assumed Tier 1 personal tool, but the code is uploading user emails to a third-party API"), **stop the audit** and recalibrate with the user. Don't silently upgrade — say what you found and ask whether the tier changes.
