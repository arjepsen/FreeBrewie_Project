# FreeBrewie Project Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Establish the approved clean-slate governance foundation and the records needed to begin a separately designed hardware-baseline milestone.

**Architecture:** This documentation-only foundation separates project entry guidance, binding policy, reusable record templates, and milestone control. Historical repositories remain external and uninspected. Shell acceptance checks verify required language, fields, links, and exclusions without adding a documentation framework or product dependency.

**Tech Stack:** Markdown, Git, POSIX shell commands, rg.

## Global Constraints

- All production software architecture and source code will be newly designed and written.
- Current requirements and verified hardware constraints will drive decisions.
- Historical repositories remain external, read-only, unimported, and are not build dependencies.
- No historical repository may be inspected while executing this plan.
- This plan must not design or implement the Linux image, SOM application, MCU firmware, interfaces, UI technology, communication protocol, brewing logic, or other product implementation.
- No empty product or subsystem skeleton directories may be created.
- Historical choices are not requirements, defaults, or sufficient justification for new decisions.
- A high-confidence assumption is temporarily acceptable only when verification is time-consuming and delay impedes progress; it cannot support a safety-critical, consequential, or hard-to-reverse decision until verified.
- The original UI is a future user-equivalence target; its technology, architecture, and internal logic will be independently selected and created.

---

## Planned file map

- README.md: project entry point, current status, boundary summary, and navigation.
- PROJECT.md: project charter, goals, non-goals, and authority boundary.
- CONTRIBUTING.md: contributor and coding-agent workflow and scope gates.
- docs/governance/clean-slate-policy.md: independent-derivation and prohibited-reuse rules.
- docs/governance/reference-material-policy.md: evidence classes, inspection, provenance, verification, and uncertainty rules.
- docs/governance/review-checklists.md: scope, provenance, assumption, decision, asset, and completion reviews.
- docs/templates/hardware-fact.md: individual hardware claim and verification record.
- docs/templates/observable-behaviour.md: externally visible compatibility evidence.
- docs/templates/historical-observation.md: historical lesson isolated from requirements.
- docs/templates/decision-record.md: fresh-reasoning decision record.
- docs/templates/asset-review.md: asset ownership, permission, suitability, and fitness review.
- docs/templates/milestone.md: scope and approval-gate record.
- docs/roadmap.md: deliberately coarse milestone sequence.
- docs/milestones/000-project-foundation.md: foundation outcome and completion evidence.
- docs/milestones/001-hardware-baseline.md: next discovery milestone brief.

### Task 1: Project entry point and charter

**Files:**
- Create: README.md
- Create: PROJECT.md

**Interfaces:**
- Consumes: docs/superpowers/specs/2026-08-06-project-foundation-design.md.
- Produces: stable entry and charter pages referenced by contribution and milestone documents.

- [ ] **Step 1: Confirm the entry-point acceptance check fails**

Run:

    test -f README.md &&
      test -f PROJECT.md &&
      rg -q "clean-slate" README.md &&
      rg -q "Current milestone" README.md &&
      rg -q "Whole-system monorepo" PROJECT.md &&
      rg -q "Out of scope" PROJECT.md

Expected: non-zero because README.md and PROJECT.md do not exist.

- [ ] **Step 2: Create README.md**

Use these sections:

    # FreeBrewie
    One-sentence clean-slate whole-system purpose.

    ## Current milestone
    Only project-foundation work is authorised; no technical subsystem is being designed or implemented.

    ## Start here
    Relative links to PROJECT.md, CONTRIBUTING.md, both governance policies, the roadmap, and the active milestone.

    ## Clean-slate summary
    Independent derivation; external read-only historical references; verified hardware facts; no inherited architecture or logic.

Do not name a Linux distribution, build system, programming language, UI framework, protocol, or brewing architecture.

- [ ] **Step 3: Create PROJECT.md**

Use these headings and content:

    # Project charter
    ## Mission
    Define a maintainable, efficient, extensible, independently designed replacement for the existing hardware.
    ## Whole-system monorepo
    Name eventual workstreams without claiming architectural boundaries.
    ## Clean-slate definition
    State independent derivation and permit equal conclusions only with fresh justification.
    ## Project-level quality goals
    Efficiency, responsiveness, maintainability, extensibility, and verifiability; later milestones make these measurable.
    ## Current authority
    Authorise governance-foundation work only.
    ## Out of scope
    Exclude legacy inspection and every technical area in Global Constraints.

- [ ] **Step 4: Run the acceptance and formatting checks**

Run:

    test -f README.md &&
      test -f PROJECT.md &&
      rg -q "clean-slate" README.md &&
      rg -q "Current milestone" README.md &&
      rg -q "Whole-system monorepo" PROJECT.md &&
      rg -q "Out of scope" PROJECT.md
    git diff --check

Expected: both commands exit 0 and the formatting check emits nothing.

- [ ] **Step 5: Commit**

Run:

    git add README.md PROJECT.md
    git commit -m "docs: add project charter and entry point"

Expected: commit succeeds.

### Task 2: Binding clean-slate and reference policies

**Files:**
- Create: docs/governance/clean-slate-policy.md
- Create: docs/governance/reference-material-policy.md
- Create: CONTRIBUTING.md

**Interfaces:**
- Consumes: PROJECT.md and the approved design.
- Produces: rules binding all later milestones and referenced by all templates.

- [ ] **Step 1: Confirm the policy check fails**

Run:

    test -f docs/governance/clean-slate-policy.md &&
      test -f docs/governance/reference-material-policy.md &&
      test -f CONTRIBUTING.md

Expected: non-zero because the files do not exist.

- [ ] **Step 2: Write the clean-slate policy**

Create docs/governance/clean-slate-policy.md with:

    # Clean-slate policy
    ## Rule
    All production architecture and source are newly designed from current requirements and approved evidence.
    ## Permitted outcomes
    A decision may match an old one only when independently justified.
    ## Prohibited foundations
    Legacy architecture, modules, algorithms, control logic, state machines, protocols, and internal application logic.
    ## Permitted reference uses
    Verified hardware facts, approved observable-behaviour targets, historical risk evidence, and approved assets.
    ## Independent derivation
    Problem, requirements, evidence, assumptions, alternatives, rationale, consequences, and verification criteria.
    ## Incidental exposure
    Disclose exposure and revisit choices whose independence cannot be established.
    ## Enforcement
    Scope, provenance, assumption, decision, and completion reviews; owner escalation on material conflict or uncertainty.

- [ ] **Step 3: Write the reference-material policy**

Create docs/governance/reference-material-policy.md with:

    # Reference-material policy
    ## Source boundary
    Original, newer, and previous-attempt repositories stay external, read-only, unimported, and outside builds.
    ## Evidence classes
    Hardware fact; observable behaviour; historical observation; legacy implementation; authoritative document; asset.
    ## Inspection authorisation
    Require milestone purpose and permitted evidence class before inspection.
    ## Provenance
    Exact claim, source, source location, extraction date, extractor, and dependent decisions.
    ## Verification
    Direct versus inferred evidence, independent confirmation, status, confidence, conflicts, and cheap-first verification.
    ## Assumptions
    Apply the exact assumption constraint in Global Constraints; require verification action and blocked-decision fields.
    ## Historical comparison
    Compare only after initial requirements, alternatives, and provisional reasoning, except early factual hardware discovery.
    ## UI and assets
    Separate user-equivalent behaviour from implementation; review each asset for ownership, permission, suitability, and fitness.
    ## Escalation
    Ask the owner about unavailable, conflicting, or consequentially uncertain evidence.

- [ ] **Step 4: Write CONTRIBUTING.md**

Use this workflow and link each step to its governing document or template:

    # Contributing
    ## Before starting work
    Read PROJECT.md, find the active milestone, confirm scope, and stop on mismatch.
    ## Before inspecting reference material
    Record milestone purpose and evidence category; require explicit inspection authority.
    ## Before making a material decision
    Establish fresh requirements, alternatives, and rationale using the decision template.
    ## Before completing work
    Run required reviews; consequential decisions cannot depend on unverified material assumptions.
    ## Scope changes
    Require owner approval and an updated milestone before expanding scope.

- [ ] **Step 5: Validate and commit**

Run:

    rg -q "Independent derivation" docs/governance/clean-slate-policy.md
    rg -q "Hardware fact" docs/governance/reference-material-policy.md
    rg -q "Before inspecting reference material" CONTRIBUTING.md
    git diff --check
    git add CONTRIBUTING.md docs/governance/clean-slate-policy.md docs/governance/reference-material-policy.md
    git commit -m "docs: establish clean-slate reference policies"

Expected: every command exits 0.

### Task 3: Evidence and asset templates

**Files:**
- Create: docs/templates/hardware-fact.md
- Create: docs/templates/observable-behaviour.md
- Create: docs/templates/historical-observation.md
- Create: docs/templates/asset-review.md

**Interfaces:**
- Consumes: docs/governance/reference-material-policy.md.
- Produces: copyable record contracts for hardware and compatibility work.

- [ ] **Step 1: Confirm templates are absent**

Run:

    for file in hardware-fact observable-behaviour historical-observation asset-review; do
      test -f "docs/templates/${file}.md" || exit 1
    done

Expected: non-zero.

- [ ] **Step 2: Create hardware-fact.md**

Include these literal fields:

    # Hardware fact: <short claim>
    - Record ID:
    - Status: proposed | provisionally accepted | verified | disputed | superseded
    - Claim:
    - Scope or hardware revision:
    - Source:
    - Source location:
    - Evidence type: direct | inferred
    - Verification method:
    - Independent confirmation:
    - Confidence: low | medium | high
    - Known conflicts or limitations:
    - Decisions depending on this fact:
    - Verification cost: quick | time-consuming
    - Next verification action:
    - Recorded by and date:
    - Verified by and date:

State that derived files with one origin are not independent confirmation and consequential decisions require verified material facts.

- [ ] **Step 3: Create behaviour and history templates**

observable-behaviour.md must include: record ID, preconditions, action, user-visible result, timing, source, reproduction evidence, compatibility importance, defect status, and verification.

historical-observation.md must include: record ID, source, observation, evidence, historical version, suspected consequence, lesson or question, and current decisions that considered it. Include verbatim:

    This observation is not a current requirement, default, or design justification.

- [ ] **Step 4: Create asset-review.md**

Include:

    # Asset review: <asset name>
    - Asset ID:
    - Description and intended use:
    - Original source and location:
    - Copyright owner:
    - Licence or permission evidence:
    - Branding status: branding | structural UI | other
    - Reuse decision: approved | rejected | recreate | pending
    - Suitability review:
    - Technical-fitness review:
    - Required attribution:
    - Approved by and date:
    - Related decision:

State that structural UI assets are recreated and pending assets cannot enter a deliverable.

- [ ] **Step 5: Validate and commit**

Run:

    rg -q "Verification cost: quick | time-consuming" docs/templates/hardware-fact.md
    rg -q "user-visible" docs/templates/observable-behaviour.md
    rg -q "not a current requirement, default, or design justification" docs/templates/historical-observation.md
    rg -q "Reuse decision: approved | rejected | recreate | pending" docs/templates/asset-review.md
    git diff --check
    git add docs/templates/hardware-fact.md docs/templates/observable-behaviour.md docs/templates/historical-observation.md docs/templates/asset-review.md
    git commit -m "docs: add evidence and asset templates"

Expected: every command exits 0.

### Task 4: Decision, milestone, and review controls

**Files:**
- Create: docs/templates/decision-record.md
- Create: docs/templates/milestone.md
- Create: docs/governance/review-checklists.md

**Interfaces:**
- Consumes: governance policies and evidence-template fields.
- Produces: approval gates used by the roadmap and future milestones.

- [ ] **Step 1: Confirm control files are absent**

Run:

    test -f docs/templates/decision-record.md &&
      test -f docs/templates/milestone.md &&
      test -f docs/governance/review-checklists.md

Expected: non-zero.

- [ ] **Step 2: Create decision-record.md**

Use:

    # Decision: <title>
    - Decision ID:
    - Status: proposed | approved | superseded | rejected
    - Milestone:
    - Owner:
    - Date:
    ## Current problem and scope
    ## Current requirements
    ## Approved evidence
    ## Assumptions and unknowns
    ## Alternatives considered
    ## Decision and independent rationale
    ## Consequences and risks
    ## Verification criteria
    ## Historical comparison
    ## Approval

State that historical comparison is optional, occurs only after provisional independent reasoning, and never substitutes for rationale.

- [ ] **Step 3: Create milestone.md**

Fields: status, owner, purpose, entry criteria, authorised work, explicit exclusions, evidence permitted, reference-inspection authority, deliverables, measurable completion criteria, assumptions, dependent decisions, required reviews, approval, and next milestone. Require owner approval before scope expansion.

- [ ] **Step 4: Create review-checklists.md**

Add pass/fail questions under:
- Scope review: authorised deliverables and exclusions.
- Provenance review: exact sources and direct/inferred distinction.
- Assumption review: cheap checks, confidence, verification action, and blocked consequential decisions.
- Independent-decision review: rationale stands without legacy code and compares current alternatives.
- Asset review: ownership, permission, suitability, technical fitness, and structural-asset recreation.
- Completion review: criteria pass, conflicts and verification debt remain visible, and scope changes are approved.

Any failed required question blocks completion unless explicitly marked inapplicable with a reason.

- [ ] **Step 5: Validate and commit**

Run:

    rg -q "Decision and independent rationale" docs/templates/decision-record.md
    rg -q "Historical comparison" docs/templates/decision-record.md
    rg -q "Explicit exclusions" docs/templates/milestone.md
    rg -q "Reference-inspection authority" docs/templates/milestone.md
    for review in Scope Provenance Assumption Independent-decision Asset Completion; do
      rg -q "## ${review} review" docs/governance/review-checklists.md || exit 1
    done
    git diff --check
    git add docs/templates/decision-record.md docs/templates/milestone.md docs/governance/review-checklists.md
    git commit -m "docs: add decision and milestone controls"

Expected: every command exits 0.

### Task 5: Roadmap and milestone gates

**Files:**
- Create: docs/roadmap.md
- Create: docs/milestones/000-project-foundation.md
- Create: docs/milestones/001-hardware-baseline.md
- Modify: README.md

**Interfaces:**
- Consumes: milestone template and governance reviews.
- Produces: completed foundation record, proposed discovery brief, and coarse sequence.

- [ ] **Step 1: Confirm milestone files are absent**

Run:

    test -f docs/roadmap.md &&
      test -f docs/milestones/000-project-foundation.md &&
      test -f docs/milestones/001-hardware-baseline.md

Expected: non-zero.

- [ ] **Step 2: Create docs/roadmap.md**

Use only this sequence:

    1. Project foundation
    2. Hardware baseline
    3. Linux-image requirements and design
    4. Linux-image implementation
    5. System requirements and subsystem planning
    6. Individually approved subsystem milestones

For each, add one outcome sentence and one principal exclusion. State verbatim: Later entries are not architecture commitments. Do not add technology selections or subsystem designs.

- [ ] **Step 3: Record milestone 000**

Create docs/milestones/000-project-foundation.md from the template. Set Status: complete only after every planned foundation file exists. Link completion evidence to the charter, policies, templates, reviews, and roadmap. Repeat technical exclusions and state: No historical repository was inspected.

- [ ] **Step 4: Brief milestone 001**

Create docs/milestones/001-hardware-baseline.md with Status: proposed and require a separate brainstorming and approval cycle. Its intended outcome is verified identification of:
- exact SOM and revision;
- exact MCU and revision;
- carrier board and revision;
- storage, memory, display, and input hardware;
- buses and connections among the SOM, MCU, and attached devices; and
- source, confidence, status, conflicts, and assumptions for each material fact.

Exclude Linux, application, firmware, protocol, brewing-logic, and UI design. Permit later, separately authorised historical inspection for hardware facts only.

- [ ] **Step 5: Update README.md**

Link both milestone records. Mark milestone 000 complete and milestone 001 proposed until separately approved. Ensure every Start here link resolves.

- [ ] **Step 6: Validate milestones and local links**

Run:

    rg -q "Later entries are not architecture commitments" docs/roadmap.md
    rg -q "Status: complete" docs/milestones/000-project-foundation.md
    rg -q "No historical repository was inspected" docs/milestones/000-project-foundation.md
    rg -q "Status: proposed" docs/milestones/001-hardware-baseline.md
    python3 -c 'from pathlib import Path; import re,sys; files=[Path("README.md"),Path("PROJECT.md"),*Path("docs").rglob("*.md")]; missing=[]; pat=re.compile(r"\[[^]]+\]\((?!https?://|#)([^)#]+)(?:#[^)]+)?\)"); [(missing.append((str(p),t)) if not (p.parent/t).resolve().exists() else None) for p in files for t in pat.findall(p.read_text())]; print("\n".join(f"{p}: {t}" for p,t in missing)); sys.exit(bool(missing))'

Expected: every command exits 0 and the link checker prints nothing.

- [ ] **Step 7: Run the foundation completion review**

Run:

    rg -n "TBD|TODO|FIXME" README.md PROJECT.md CONTRIBUTING.md docs --glob "*.md" --glob "!superpowers/plans/*.md"
    git diff --check
    git status --short

Expected: the placeholder scan has no matches outside implementation plans; no formatting errors; only planned foundation changes. Manually answer every question in review-checklists.md and confirm that no technical design, product skeleton, or historical inspection occurred.

- [ ] **Step 8: Commit**

Run:

    git add README.md docs/roadmap.md docs/milestones/000-project-foundation.md docs/milestones/001-hardware-baseline.md
    git commit -m "docs: establish foundation milestone gates"
    git status --short --branch

Expected: commit succeeds and the working tree is clean.
