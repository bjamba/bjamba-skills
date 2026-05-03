# Guardrails: Enforceable CLAUDE.md

A descriptive CLAUDE.md is wishful thinking. A new contributor (human or LLM) who doesn't read it will silently violate every rule, and a CI pipeline that doesn't enforce it will allow the regression to merge. To prevent that, **every rule in CLAUDE.md must be paired with an enforcement mechanism**.

This file specifies the protocol: rules in CLAUDE.md, enforcement in `.github/workflows/`, `.pre-commit-config.yaml`, `scripts/check.sh`, and other files that *actually run*.

---

## The Three Layers of Guardrails

Every guardrail lives at three layers:

1. **The rule** — stated in `CLAUDE.md` in plain language. The *what* and *why*.
2. **The local enforcement** — pre-commit hook, lint rule, type check, or `scripts/check.sh` step that catches the violation before it's even committed.
3. **The CI enforcement** — `.github/workflows/guardrails.yml` (or extension to existing CI) that catches anything the local layer missed and blocks the merge.

When you can only enforce at one layer, document the gap explicitly in CLAUDE.md.

---

## When to generate

- **Path A (plan-only):** Generate CLAUDE.md + the enforcement scaffolding even if no other code is being changed. This is high-leverage on its own — every future PR (human or LLM) gets caught.
- **Path B (in-place):** Generate at the end of M0; update at the end of every milestone.
- **Path C (greenfield):** Generate before any production code. CLAUDE.md + enforcement is the constitution for the rebuild.

If a `CLAUDE.md` already exists, **never silently overwrite**. Read it, propose a merge, surface conflicts.

---

## CLAUDE.md structure (revised)

The file should be opinionated, specific, and lean — under ~300 lines. Generic advice is worse than nothing.

### Required sections

1. **About this repo** — one paragraph: what it is, what tier, who uses it.
2. **Production tier & rationale** — explicit. Tier N because [reason]. This anchors all other decisions.
3. **Architectural invariants** — structural rules. Each item is `**Rule.** Why. Enforced by: <mechanism>`.
4. **Security & secrets rules** — same pattern.
5. **Testing expectations** — same pattern.
6. **Where things live** — pointers to `docs/02-design/`, `docs/adr/`, `docs/runbooks/`, `BACKLOG.md`.
7. **Things we deliberately don't do** — and why. Each item also paired with enforcement where possible.
8. **How to add [common change types]** — playbooks specific to this codebase.
9. **The enforcement layer** — explicit list of where the rules are enforced and how to run the checks locally.

### Pattern: every rule paired with enforcement

Bad (descriptive only):
> Never log request bodies. They might contain PII.

Good (descriptive + enforced):
> **Never log request bodies.** They might contain PII.
> **Why:** journal entries are sensitive personal data; logs are retained for 30 days in CloudWatch.
> **Enforced by:** `scripts/check-no-pii-logs.sh` (pre-commit + CI). Greps for `logger.info(request.body)` and similar patterns.

If a rule cannot be enforced automatically, mark it explicitly:
> **No new dependencies without an ADR.** Why: dependency licenses are checked manually quarterly.
> **Enforced by:** *Manual review only — flagged in PR template.*

This honesty is important. A rule that says "enforced by: X" when X doesn't exist is worse than a rule that says "enforced by: nothing yet."

---

## Standard enforcement mechanisms (and what they catch)

### Pre-commit hooks (`.pre-commit-config.yaml`)

Runs locally on `git commit`. Best for fast checks that fail loud.

| Check | Tool | Catches |
|-------|------|---------|
| Secrets in diffs | `gitleaks`, `detect-secrets` | API keys, tokens accidentally committed |
| Large files | `check-added-large-files` | Binary blobs, accidental DB dumps |
| Lint | `ruff` / `eslint` | Style and basic correctness |
| Type check | `mypy` / `tsc --noEmit` | Type errors |
| Format | `ruff-format` / `prettier` | Inconsistent formatting |

### CI workflow (`.github/workflows/ci.yml` + `guardrails.yml`)

Runs on every PR. Best for slower checks and the "you can't bypass" enforcement layer.

| Check | Tool | Catches |
|-------|------|---------|
| Tests | `pytest` / `vitest` / `jest` | Regressions |
| Coverage threshold | `pytest --cov-fail-under` | Untested new code |
| Dep vulns | `pip-audit`, `npm audit`, Dependabot | Known CVEs |
| License scan | `pip-licenses`, `license-checker` | GPL in proprietary code |
| Custom rules | `scripts/check.sh` | Repo-specific invariants |

### Custom validator (`scripts/check.sh` or similar)

For rules no off-the-shelf tool catches. Generated as part of the scaffolding.

Example structure:
```bash
#!/usr/bin/env bash
# scripts/check.sh — repo-specific guardrails. Run locally, called from CI.
# Each check is a function that returns 0 (pass) or non-zero (fail).
# Add new checks below; keep them fast and fail-loud.

set -uo pipefail
exit_code=0

check_no_pii_in_logs() {
    if git grep -nE 'log(ger)?\.(info|debug)\([^)]*request\.body' -- '*.py' '*.ts'; then
        echo "❌ Logging request.body — see CLAUDE.md § Security."
        return 1
    fi
}

check_no_db_in_handlers() {
    # Routes must not import the DB client directly; they must go through repo/.
    if git grep -nE "from db|from \\./db" -- 'app/api/**/*.ts'; then
        echo "❌ API handler importing DB directly — use repo/ — see CLAUDE.md § Architecture."
        return 1
    fi
}

check_no_pii_in_logs || exit_code=1
check_no_db_in_handlers || exit_code=1

exit $exit_code
```

Wired into pre-commit:
```yaml
- repo: local
  hooks:
    - id: repo-checks
      name: Repo-specific guardrails (scripts/check.sh)
      entry: scripts/check.sh
      language: system
      pass_filenames: false
```

And into CI:
```yaml
- name: Repo-specific guardrails
  run: scripts/check.sh
```

### PR template (`.github/PULL_REQUEST_TEMPLATE.md`)

For rules that need a human to certify (no automated check possible). Forces the author to actively confirm.

```markdown
## Guardrail check
- [ ] No new dependencies introduced (or ADR linked)
- [ ] No PII in logs
- [ ] If this changes a public API, the OpenAPI spec is updated
```

---

## Template (revised — every rule paired)

Use this as the starting structure. Customize heavily.

```markdown
# CLAUDE.md

Guidance for Claude Code (and any developer) working in this repo.

*Last reviewed: YYYY-MM-DD. Owner: [team or person]. Generated by productionize-me.*

## About this repo

[1 paragraph: what it is, who uses it, tier.]

## Production tier: Tier N

We're a Tier N product because [reason]. See `.productionize-me/AUDIT.md` for the most recent audit and `docs/02-design/` for the design docs that follow from this.

## Architectural invariants

These rules are non-negotiable. Violations are bugs.

**All persistence goes through `internal/repo/`.**
- *Why:* keeps query logic centralized, lets us swap data stores, lets us audit data access.
- *Enforced by:* `scripts/check.sh` (greps for direct DB imports in handlers); CI workflow `guardrails.yml`.

**External HTTP calls have a 5-second timeout and use `pkg/httpc`.**
- *Why:* prevents one slow upstream from cascading into request-handler thread exhaustion.
- *Enforced by:* `scripts/check.sh` (greps for raw `requests.get`/`fetch` outside `pkg/httpc`).

**Background jobs are idempotent.**
- *Why:* the worker queue can deliver any job up to twice. A non-idempotent job double-charges, double-emails, double-writes.
- *Enforced by:* *Manual review — flagged in PR template.* Future: a property test runner is in `BACKLOG.md`.

## Security & secrets

**Never commit secrets.**
- *Enforced by:* `gitleaks` (pre-commit + CI), `.gitignore` excludes `.env`.
- `.env.example` is the source of truth for required variables.

**Never log request bodies, response bodies, or anything with PII.**
- *Why:* journal entries are sensitive personal data; logs retain 30 days.
- *Enforced by:* `scripts/check-no-pii-logs.sh` (pre-commit + CI).

**Auth check on every protected endpoint.**
- *Enforced by:* `scripts/check-auth-coverage.sh` runs after route changes (CI). The script lists every route and verifies an auth guard is present.

**Input validated via Pydantic schemas at every external boundary.**
- *Enforced by:* `mypy --strict` flags untyped request handlers. Routes that accept `dict` instead of a schema fail type-check.

## Testing

**Every new route requires at least one integration test.**
- *Enforced by:* `scripts/check.sh` checks that PRs touching `app/api/**` also touch `tests/integration/**`.

**Unit tests for the happy path and at least one error case.**
- *Enforced by:* coverage threshold (currently 70%); CI fails below.

**Run `make check` before pushing. CI runs the same.**

## Where things live

- `docs/02-design/` — architecture, data model, security/privacy
- `docs/adr/` — decision records
- `docs/runbooks/` — what to do when things break
- `.productionize-me/AUDIT.md` — current state vs. tier
- `scripts/check.sh` — the guardrail validator
- `.pre-commit-config.yaml` / `.github/workflows/` — where guardrails are wired in

## How to add an API route

1. Define request/response schema in `app/api/schemas/`
2. Add the handler in `app/api/<area>/<route>.py`
3. Add the auth guard at top of the handler
4. Add an integration test in `tests/integration/api/`
5. If it touches the DB, add a migration in `migrations/`
6. Update `docs/02-design/ARCHITECTURE.md` if the route is structurally novel

## How to add a database table

1. Write the migration in `migrations/`
2. Update the ERD in `docs/02-design/DATA_MODEL.md`
3. Add the repo methods in `internal/repo/<entity>.py`
4. Add an ADR in `docs/adr/` if the table introduces a non-obvious design choice

## Things we deliberately don't do

**No ORM auto-eager-loading.**
- *Why:* it caused production N+1 issues in v0.3 — see `docs/adr/0007-no-eager-loading.md`.
- *Enforced by:* code review; flagged in PR template.

**No generated code committed.**
- *Why:* hard to review, hides intent.
- *Enforced by:* `.gitignore` excludes generation outputs; `scripts/check.sh` warns on common patterns.

**No new top-level dependencies without an ADR.**
- *Why:* keeps surface area small and licensing auditable.
- *Enforced by:* PR template checkbox; quarterly manual review.

## Running the guardrails locally

```bash
# Run all checks at once
make check

# Or individually
pre-commit run --all-files
scripts/check.sh
pytest
```

CI runs the same set on every PR.

## When in doubt

Read `docs/02-design/ARCHITECTURE.md`, then `docs/adr/`. Ask before making structural changes.
```

---

## Audit findings must thread to CLAUDE.md

Every P0/M0 finding in `AUDIT.md` must produce a corresponding **rule + enforcement** in `CLAUDE.md`. This is non-negotiable. A rule without an audit-finding origin is generic; a finding without a CLAUDE.md rule is a regression waiting to happen.

The pattern:

1. **Audit identifies a problem.** "Secrets are shared via Slack — live Stripe key was pasted in #ops-tools on 2026-04-12." (`AUDIT.md` § Security & Secrets)
2. **Plan addresses it now.** M0.0 — rotate keys, migrate to Vercel env vars + 1Password. (`PLAN.md`)
3. **CLAUDE.md prevents recurrence.** "**Never share secrets via Slack, email, DM, screen share, or any chat surface.** Why: chat platforms retain message history; Slack search exposes pasted keys to anyone who joins. Why this rule exists: a live Stripe key was leaked via #ops-tools on 2026-04-12 — see `AUDIT.md`. Enforced by: `gitleaks` (catches commit-path); PR template checkbox (catches review path); manual review only for chat surfaces — flagged in `docs/runbooks/secret-rotation.md`."
4. **Cross-link.** CLAUDE.md rules cite the audit finding by section. Audit findings cite the CLAUDE.md rule. They reinforce each other.

Before declaring CLAUDE.md done: walk through every P0/M0 in `AUDIT.md` and confirm there's a corresponding rule. If a finding can be fully fixed by execution (e.g., "missing CHANGELOG.md") and won't recur, no CLAUDE.md rule needed. If it could recur (any pattern, practice, or human-behavior issue), it gets a rule.

This is the load-bearing connection between *audit* (current state), *plan* (work to do), and *guardrails* (preventing regression). Skipping it means the same incident can happen again next quarter.

## What to scaffold alongside CLAUDE.md

When generating CLAUDE.md, also generate (or update) the enforcement files referenced in it:

1. `scripts/check.sh` — the custom validator with tier-appropriate checks
2. `.pre-commit-config.yaml` — wired to call `scripts/check.sh` and standard hooks
3. `.github/workflows/ci.yml` — runs the same checks
4. `.github/PULL_REQUEST_TEMPLATE.md` — surfaces manual checks
5. `Makefile` (or `npm script`/`task` equivalent) — `make check` should be one command that runs everything

If any of these already exist, *merge* rather than overwrite. Surface conflicts to the user.

CLAUDE.md without these files is just a wish list. With them, it's a system.

---

## Maintaining over time

- Every milestone ends with: "is CLAUDE.md current? are the enforcement mechanisms still working?"
- Run `scripts/check.sh` against the codebase as part of the audit (Phase 2). Findings often suggest new guardrails.
- Treat removing a guardrail as seriously as introducing a regression — it requires an ADR.
