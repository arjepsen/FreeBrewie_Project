# Contributing

## Before starting work

Read the canonical [current-authority section](PROJECT.md#current-authority),
which is the source of truth for current milestone status and work authority.
Confirm that an approved, active milestone authorises the requested work. Stop
when the request is not authorised or when its status or scope conflicts with
that canonical authority.

## Before inspecting reference material

Record milestone purpose and evidence category; require explicit inspection authority. See the [reference-material policy](docs/governance/reference-material-policy.md) and [milestone template](docs/templates/milestone.md).

## Before making a material decision

Establish fresh requirements, alternatives, and rationale using the [decision template](docs/templates/decision-record.md) and [clean-slate policy](docs/governance/clean-slate-policy.md).

## Before completing work

Run required [reviews](docs/governance/review-checklists.md); consequential decisions cannot depend on unverified material assumptions.

## Scope changes

Require owner approval and an updated [milestone](docs/templates/milestone.md) before expanding scope.

## Automatic pushes

- Commit frequently during work.
- Do not push intermediate worktree commits merely because they exist.
- Push approved specifications and implementation plans after committing them.
- After reviewed work is merged into main and fresh verification passes, push main automatically.
- Never force-push.
- Stop and report authentication failure, rejection, or remote divergence instead of rewriting history.
- Do not push experimental, incomplete, or blocked work unless the project owner requests it.
