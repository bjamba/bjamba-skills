# Execute Paths

After the plan is approved, the user picks one of three execution paths. This file is the playbook for each.

**Always confirm before any shared-state action**: creating remote branches, force-pushing, opening PRs, modifying `main`, deleting branches, deploying. Local-only changes (creating branches, committing, modifying files in the working tree) are fine without per-action confirmation once the path is chosen.

---

## Path A — Plan-Only

The user takes the plan and executes themselves. Skill exits gracefully.

"Plan-only" means the user is not asking the skill to execute the items in `PLAN.md` (refactors, infra changes, etc.). It does NOT mean the skill produces no files. The four required outputs — diagnostics, design docs, scaffolding, enforceable CLAUDE.md — still happen.

**What to do:**
1. Confirm the diagnostic artifacts (`SUMMARY.md`, `AUDIT.md`, `PLAN.md`) are in `.productionize-me/`.
2. Generate the **retrospective design docs** in `docs/` (per `references/retrospective-artifacts.md`) — tier-appropriate selection, written in team-grade voice with metadata and cross-links.
3. Lay down **production scaffolding** files (per `references/scaffolding.md`) — `.gitignore` updates, `.env.example`, `README.md` skeleton, and tier-2+ if applicable: CI config, pre-commit, dependabot, PR template. List what would be created/modified before doing it; never overwrite without confirmation.
4. Generate **enforceable `CLAUDE.md`** + the guardrail mechanisms it references — `scripts/check.sh`, pre-commit wiring, CI workflow extensions, PR template (per `references/guardrails-claudemd.md`). Every CLAUDE.md rule must point to its enforcement mechanism.
5. Update `.productionize-me/STATE.md` to: `phase: complete (plan-only)`.
6. Run `git status` to show the user the actual file changes; offer a brief "what to read first" — usually `PLAN.md` § M0 and `docs/README.md`.
7. Optionally: offer to schedule a follow-up agent (via `/schedule`) to check progress in a few weeks.

**Don't:**
- Push the user to pick Path B or C if they're not ready.
- Open PRs or modify code.

---

## Path B — In-Place Modernization

Work on a new branch off the user's default branch. Tackle plan items in priority order, milestone by milestone, with a PR per milestone.

### Setup (do once)

1. **Confirm the default branch.** Read it from `git symbolic-ref refs/remotes/origin/HEAD` if available, otherwise ask.
2. **Confirm the working tree is clean.** If not, ask the user whether to stash, commit, or stop.
3. **Create the M0 branch:** `productionize/m0` off the default branch.
4. **Confirm with the user:** "I'm going to start on M0 — first item is [X]. Sound good?"

### For each milestone

1. **Read the milestone items in `PLAN.md`.** Confirm priorities haven't changed.
2. **Work item by item, smallest first.** Every item should result in a discrete, reviewable commit. Commit messages should reference the plan item.
3. **Run tests after each item.** If tests are missing, that's likely an M0 item — set them up first.
4. **At the end of the milestone:**
   - Update `CHANGELOG.md` (create one if missing — Keep a Changelog format).
   - **Update `CLAUDE.md`.** At the end of M0, *generate* it from the template in `references/guardrails-claudemd.md` (or merge with any existing `CLAUDE.md`). At the end of every subsequent milestone, revisit it: have new architectural invariants emerged? new "how to add X" recipes? new "things we deliberately don't do"? CLAUDE.md is what prevents future regression — keeping it current is part of the milestone definition of done.
   - Update `.productionize-me/STATE.md`: phase, milestone complete, next milestone.
   - Push the branch only after explicit confirmation.
   - Open a PR only after explicit confirmation. Use `gh pr create` with a body summarizing the milestone.
5. **Stop and ask the user to review** before moving to the next milestone. Their review may surface follow-ups that change the plan — update `PLAN.md` if so.

### Branch naming

`productionize/m0`, `productionize/m1`, etc. If a milestone is large, sub-branches are fine: `productionize/m0-secrets`, `productionize/m0-tests`. Each merges into the milestone branch, which merges into the user's default branch when the milestone is done.

### When to stop

Stop and reconsider if:
- The user pushes back on a recommendation — discuss, possibly update the plan, then resume.
- A change is bigger than estimated by 2x or more — surface it explicitly.
- You find something during execution that should have been flagged in the audit — update the audit and ask the user how to proceed.
- Tests are failing on `main` (not just your branch) — flag it; not your fight to fix unless asked.

---

## Path C — Greenfield Rebuild

Start a clean codebase in a sibling directory that takes lessons from the original but rebuilds with production patterns from day one.

This is the **right choice** when:
- The existing code is structurally beyond saving (e.g., everything in one file, nondeterministic state, no clear boundaries)
- The user is open to a stack change
- Migration cost is dominated by data migration, not code migration

This is the **wrong choice** when:
- The user has live customers who need continuity
- The existing code is fine, just under-documented
- The team can't afford to maintain two codebases during transition

If the user picks Path C, **explicitly confirm** they understand the transition cost. "Greenfield means running both versions side-by-side until you cut over. Are you sure that's what you want, or would in-place modernization on a branch be safer?" Then proceed.

### Setup

1. **Decide the new repo location.** Default: sibling directory `<original-name>-v2/`. Confirm with user.
2. **Initialize:** `git init`, set up the chosen tooling (build system, test runner, linter, CI scaffold, README skeleton, LICENSE).
3. **Write `<new-repo>/CLAUDE.md` *before* any production code** (per `references/guardrails-claudemd.md`). The new repo's CLAUDE.md is the constitutional document — it sets the tier, invariants, testing expectations, and structural rules from day one. Every subsequent decision in the rebuild references back to it.
4. **Write `<new-repo>/MIGRATION.md` next.** This is the map from old to new:
   - Concept-by-concept mapping (old name → new name → why)
   - Data migration plan if there's persistent data
   - Cutover plan (when does old version turn off?)
   - What is *deliberately not* being carried over and why

### Building the new repo

Build it according to Tier requirements from day one. Don't import the old patterns — recreate the functionality with production patterns.

Module-by-module:
1. Pick the simplest, leafmost module to start (utility functions, pure transforms).
2. Implement with tests.
3. Move outward toward the entry point.
4. The last module to come over is the integration / entry point.

After each module, update `MIGRATION.md` with what's done and what's pending.

### Don't

- Don't `cp -r old/* new/` and call it migration.
- Don't keep two writable copies of the same data.
- Don't delete the original. Until the user confirms cutover, the original is the source of truth.

---

## State Management Across Paths

After each significant action, update `.productionize-me/STATE.md`. This is what lets the user (or you in a future session) pick up where things left off.

```markdown
# State

**Phase:** Execute / Path B
**Current milestone:** M1
**Last action:** Merged PR #42 (M0 complete)
**Next:** Start M1 item: "Add Sentry to API service"
**Blocked on:** Nothing
**Updated:** 2026-05-02
```

Keep it short — under 20 lines. Detailed history goes in `CHANGELOG.md` and `git log`, not here.
