# Scaffolding

Productionize-me does not just diagnose — it leaves the codebase materially closer to production. Every execution path (A, B, or C) lays down concrete scaffolding files, calibrated to the tier.

This is what makes the skill *productionize*, not just *audit*. After the skill runs, the codebase should *feel* more production-grade: real configs, real CI, real hooks, real structured READMEs — not just markdown describing what's missing.

---

## Core principle

**Scaffold what's universally true at this tier.** Don't scaffold things that depend on user-specific choices (e.g., don't generate a Stripe webhook handler if the user might use Paddle).

Always:
1. **Read existing files first.** Never overwrite without confirmation.
2. **Use language/framework-appropriate templates.** A Python repo gets `pre-commit-config.yaml` + `pyproject.toml` setup; a Node repo gets `husky` + `package.json` scripts.
3. **Match the project's existing tooling choices.** If they're using Yarn, scaffold for Yarn. If they're on Bun, use Bun.
4. **Make scaffolding minimal and explicit.** Better to scaffold 5 high-leverage files well than 30 generic ones poorly.

---

## Required at every tier (the always-do list)

These files are non-negotiable. Every productionize-me run produces them, regardless of tier. If they exist already, *update or merge*; if they don't, create them.

| File | Required because |
|------|-----------------|
| `README.md` | If a stranger can't get this running locally in 30 minutes, the codebase is by definition not production-grade. The README is the front door. |
| `.gitignore` | Must exclude `.env` and any other secret-bearing files. A missing `.gitignore` is a P0 finding masquerading as a missing config file. |
| `.env.example` | The contract for required environment variables. Without it, "configuration" is tribal knowledge. |
| Dependency manifest (`requirements.txt` / `package.json` / `go.mod` / `Cargo.toml`) | Reproducible installs. Ad-hoc `pip install` is not a deployment story. |
| `LICENSE` (or explicit "all rights reserved" note in README) | Without one, the legal default is ambiguous. |

If any of these is missing or insufficient, **scaffold it as part of M0 — even at Tier 1**.

## What to scaffold by tier

### Tier 1 (Personal / Internal-only)

Just the always-do list above. Nothing more.

Tier 1 doesn't need CI, hooks, or PR templates — but it absolutely still needs a README that future-you can follow, a `.env.example` so future-you doesn't lose API keys, and a manifest so future-you can reinstall.

### Tier 2 (Small team / Internal business)

Everything from Tier 1, plus:

| File | Purpose | Skip if |
|------|---------|---------|
| Lockfile (`package-lock.json`, `poetry.lock`, etc.) | Reproducible installs | Already committed |
| `.github/workflows/ci.yml` | Run tests + linter on every PR | Already exists |
| `.github/dependabot.yml` | Automated dep updates | Already exists |
| `.pre-commit-config.yaml` (or husky equivalent) | Run linter + type-check + secrets scan locally | Already exists |
| `CHANGELOG.md` | Keep a Changelog format | Already exists |
| `.github/PULL_REQUEST_TEMPLATE.md` | Forces a description + test plan | Already exists |
| `CONTRIBUTING.md` (short) | How to set up locally and submit a PR | Already exists |

### Tier 3 (Customer-facing / Real revenue)

Everything from Tier 2, plus:

| File | Purpose | Skip if |
|------|---------|---------|
| `.github/CODEOWNERS` | Required reviews per area | Already exists |
| `SECURITY.md` | Vulnerability disclosure path | Already exists |
| `.github/ISSUE_TEMPLATE/bug_report.md` & `feature_request.md` | Structured intake | Already exists |
| `.github/workflows/security.yml` | Dependency vuln scanning, secret scanning | Already exists |
| Structured logging boilerplate at the framework level | Log everything as JSON, no PII | Already structured |
| Error tracking init in entry point | Sentry/Rollbar/equivalent loaded at startup | Already initialized |
| `docs/postmortem-template.md` | Format for incident write-ups | Already exists |
| `docs/runbooks/<top-5-scenarios>.md` | Specific to the system's failure modes | (Tier-3 minimum is generated regardless) |

### Tier 4 (Regulated)

Tier 3 scaffolding is the floor. Beyond that, this skill's posture is: *recommend* compliance scaffolding (sample DPA, sample BAA placeholders, audit-log boilerplate, encryption-at-rest configs) but **defer to the user's compliance partner** for the real artifacts. Generate placeholders + a checklist; do not pretend to produce regulator-ready docs.

---

## Templates

### `.gitignore` (always — language-aware)

For Python:
```
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.env
.env.*
!.env.example
.pytest_cache/
.mypy_cache/
.ruff_cache/
dist/
build/
.coverage
htmlcov/
.DS_Store
```

For Node/TS:
```
node_modules/
dist/
build/
.next/
.env
.env.*
!.env.example
*.log
.DS_Store
coverage/
.turbo/
```

Adapt for the actual stack. Always include `.env` exclusion + `!.env.example` allow.

### `.env.example` (always)

Read the codebase for all `process.env.X` / `os.environ['X']` / `os.getenv('X')` references. Produce a complete list with placeholder values and a one-line comment per variable.

```bash
# OpenAI API key — get one at platform.openai.com
OPENAI_API_KEY=sk-...

# Postgres connection string
DATABASE_URL=postgres://user:pass@localhost:5432/dbname

# Sentry DSN (optional in dev)
SENTRY_DSN=
```

### `README.md` skeleton (Tier 1+)

```markdown
# [Project name]

[One sentence: what it does and who it's for.]

## Requirements
- [Language/runtime version]
- [System dependencies if any]

## Setup
\`\`\`bash
git clone <repo>
cd <repo>
[install command]
cp .env.example .env  # then fill in real values
\`\`\`

## Run
\`\`\`bash
[run command]
\`\`\`

## Test
\`\`\`bash
[test command]
\`\`\`

## Project layout
[Brief tree or list of top-level dirs and what's in them]

## Documentation
- `docs/02-design/ARCHITECTURE.md` — system design
- `docs/02-design/DATA_MODEL.md` — data model
- `docs/runbooks/` — what to do when things break
- `CLAUDE.md` — guardrails for working in this repo

## License
[License or "all rights reserved"]
```

### `.github/workflows/ci.yml` (Tier 2+)

Match the language. Generic Python skeleton:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: mypy .
      - run: pytest -v
```

Generic Node/TS skeleton:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck
      - run: npm test
```

### `.pre-commit-config.yaml` (Tier 2+)

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: detect-private-key
      - id: detect-aws-credentials
        args: [--allow-missing-credentials]

  # Language-specific hooks below — pick the ones that fit
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.4
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.21.2
    hooks:
      - id: gitleaks
```

For Node, swap the language hooks for Prettier + ESLint via `lint-staged` + `husky`.

### `.github/dependabot.yml` (Tier 2+)

```yaml
version: 2
updates:
  - package-ecosystem: "[npm|pip|gomod|cargo]"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### `SECURITY.md` (Tier 3+)

```markdown
# Security policy

## Reporting a vulnerability

If you've found a security issue, please **do not open a public issue**. Email [security@example.com] with:
- Description of the issue
- Steps to reproduce
- Impact assessment if known

We'll acknowledge within 2 business days and coordinate a fix and disclosure timeline.

## Supported versions

| Version | Supported |
|---------|-----------|
| latest  | ✅ |

## Known constraints

[Any caveats — e.g., "we currently encrypt at rest at the volume level, not field level"]
```

### `.github/PULL_REQUEST_TEMPLATE.md` (Tier 2+)

```markdown
## What
[One sentence on what this changes.]

## Why
[The problem or motivation.]

## Test plan
- [ ] [How you verified this works]
- [ ] [Tests added/updated]

## Risk
[Anything reviewers should think hard about — DB migrations, breaking changes, etc.]
```

### `CHANGELOG.md` (Tier 2+)

Use [Keep a Changelog](https://keepachangelog.com) format:

```markdown
# Changelog

All notable changes are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Productionization scaffolding (CI, pre-commit, dependabot)

### Changed
-

### Fixed
-

## [0.1.0] - YYYY-MM-DD
- Initial release
```

---

## How to scaffold without breaking things

1. **List what would be created/modified before doing anything.** Show the user the list and confirm.
2. **Use git to stage scaffolding atomically.** One commit per scaffolding category (`scaffold: CI workflow`, `scaffold: pre-commit config`).
3. **Do NOT modify substantive application code as part of scaffolding.** Scaffolding only touches config / docs / tooling.
4. **For Path A (plan-only):** scaffolding still happens — it's pure additive plumbing the user benefits from regardless of whether they execute the rest of the plan.
5. **For Path B/C:** scaffolding is M0 work — the very first commit on the productionize branch.
6. **Verify after writing.** Run `git status` to confirm files actually landed; run the tools (e.g., `pre-commit run --all-files`) at least once to make sure the scaffolding works.
