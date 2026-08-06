# FreeBrewie Project Foundation Design

Date: 2026-08-06  
Status: Approved design

## Purpose

This document defines how the clean-slate FreeBrewie project will be governed and organised before technical product design begins. FreeBrewie will be a whole-system monorepo that eventually governs the Linux image, SOM application, MCU firmware, interfaces, UI, integration assets, tests, documentation, and project policy.

The foundation milestone establishes the boundary, evidence policy, staged organisation, and initial milestone sequence. It does not design or implement any product subsystem.

## Clean-slate boundary

All production software architecture and source code will be newly designed and written. Current requirements and verified hardware constraints will drive decisions.

A new decision may match a historical decision, but only when current evidence, alternatives, and independent reasoning establish that it is the right choice. Similarity alone neither validates nor invalidates a decision.

Historical repositories must not supply the foundation for new:

- implementation architecture;
- source or module structure;
- control logic or algorithms;
- state machines;
- communication protocols; or
- internal application logic.

The original Brewie codebase, a newer historical codebase, and the owner's previous clean-slate attempt are reference material, not ancestors of this repository. They will remain external, read-only, will not be imported wholesale, and will never become build dependencies.

Only the following may enter the new repository from reference work:

- independently written fact and observation records;
- citations and provenance;
- approved assets whose ownership and suitability have been confirmed; and
- authoritative documents that may be stored and used under their applicable licences.

Technology choices remain open until their relevant design milestones. Historical use of a 3.x Linux kernel or Qt is evidence about prior implementations, not a requirement or preference for the new system.

Efficiency, responsiveness, maintainability, and extensibility are project-level quality goals. Each technical milestone must turn relevant goals into measurable requirements rather than relying on vague claims of improvement.

## Reference-material policy

Reference information is classified by what may legitimately be learned from it.

### Hardware facts

Hardware facts include component identities, board revisions, electrical connections, buses, pins, peripherals, physical constraints, and measured capabilities. Verified facts may directly constrain new designs.

Each material hardware fact will record:

- the precise claim;
- its source and source location;
- the verification method;
- whether it is directly established or inferred;
- its verification status and confidence;
- known conflicts or limitations; and
- what decisions depend on it.

Cheap verification will happen before a fact is used. A high-confidence assumption may be used temporarily when verification is time-consuming and delaying it would impede progress. Such an assumption must be conspicuous, state how it can be verified, and must not support a safety-critical, consequential, or hard-to-reverse decision until verified.

Verification may come from schematics, component documentation, board inspection, electrical measurement, or agreement between genuinely independent reliable sources. Repetition across files derived from the same original source is not independent confirmation.

### Observable behaviour

Observable behaviour includes screens, navigation, terminology, responses to user actions, timing, and other externally visible device behaviour. It may define an explicit compatibility target when a milestone approves that target.

The initial replacement UI will target user equivalence with the original UI from the historical codebases. It should preserve the screens, visual identity, navigation, terminology, and expected user-visible functionality while permitting minor rendering differences and documented defect corrections. The implementation technology, internal architecture, and application logic will be selected and created independently, with efficiency and extensibility as explicit requirements.

### Historical observations

Historical observations include technologies, architectures, limitations, defects, successful outcomes, and design choices found in earlier work. They may inform questions, tests, and risk analysis, but they do not become requirements, defaults, or sufficient justification for a new choice.

Historical observations will be recorded separately from hardware facts, requirements, and new decisions.

### Legacy implementation

Legacy source structure, algorithms, state machines, protocols, control flow, and internal logic are not reusable design inputs. Incidental exposure to them will be acknowledged rather than hidden. Any affected new decision must still be established from current requirements, approved facts, alternatives, and independent reasoning. If that independence cannot be demonstrated confidently, the decision will be revisited.

### Visual and audio assets

Assets will be evaluated individually. Original branding assets may be reused only after ownership, permission, suitability, and technical fitness are confirmed. Structural UI assets will be recreated. Reusing an asset does not justify carrying forward the software structure that previously presented it.

## Controlled reference workflow

Before reference inspection begins, the active milestone will state the purpose of inspection and the permitted evidence categories. Inspection will produce neutral, independently written records instead of copied implementation material.

Hardware investigation precedes designs that depend on the physical system. Historical design comparison should normally follow initial requirements, alternatives, and a provisional clean-slate decision. Its purpose is to expose missed constraints and known failure modes, not to provide an architecture.

When evidence is unavailable, inconsistent, or consequentially uncertain, the project will ask the owner rather than silently choose an interpretation. Unresolved uncertainty will remain visible until verified or explicitly removed from scope.

## Staged monorepo organisation

The monorepo will separate material by responsibility:

- **Project governance:** the clean-slate policy, contribution rules, reference policy, and scope controls.
- **Evidence:** verified hardware facts, observable behaviour, historical observations, assumptions, and provenance.
- **Requirements:** current project and milestone requirements, separate from both evidence and implementation.
- **Decisions:** independently reasoned decision records.
- **Milestones:** scoped outcomes, entry criteria, completion criteria, and explicit exclusions.
- **Future delivery areas:** the Linux image, SOM application, MCU firmware, interfaces, UI, system integration, and testing.

Future delivery areas name workstreams, not settled architectural boundaries. For example, naming the UI workstream does not decide whether the UI will be a separate process, part of the SOM application, or use any specific framework.

Directories will be created only when approved material for the current milestone needs them. Empty subsystem skeletons will not be generated. Each technical milestone must establish its own internal structure through an approved design before implementation begins.

Shared material must have a clear purpose and owner. A general-purpose `common` area will not be created merely for convenience; genuinely shared interfaces or assets must be placed according to an explicitly approved responsibility.

## Decision records

A material decision record will contain:

- the current problem and scope;
- relevant requirements and approved evidence;
- assumptions and unresolved questions;
- viable alternatives considered;
- the selected alternative and fresh rationale;
- expected consequences and risks;
- verification or review criteria; and
- a separately labelled historical comparison, if one was performed.

References to a historical choice cannot substitute for rationale. A decision is acceptable when a reviewer can understand why it follows from present needs without consulting the legacy implementation.

## Governance workflow

Each future milestone will:

1. State its purpose, authorised scope, and explicit exclusions.
2. Gather only the evidence needed for that scope.
3. Record facts, observations, assumptions, and unknowns in their correct categories.
4. Verify cheap-to-check facts immediately and track costly verification work.
5. Write current requirements without converting historical choices into requirements.
6. Develop and compare fresh alternatives.
7. Record the selected decision and its independent rationale.
8. Optionally compare the provisional decision with historical work to expose missed constraints or failure modes.
9. Revise only when current evidence and reasoning justify doing so.
10. Verify the result against measurable completion criteria before expanding scope.

Every milestone will include assumption, provenance, scope, and completion reviews. Review checklists are sufficient initially. Automated enforcement will be added only when it provides clear and proportionate value.

## Foundation milestone

The project-foundation milestone delivers:

- the project charter and clean-slate boundary;
- reference classification and inspection policy;
- hardware-fact and assumption record formats;
- a separate historical-observation format;
- an independently reasoned decision-record format;
- UI-compatibility evidence and asset-approval rules;
- staged monorepo organisation and contribution rules;
- a milestone roadmap with explicit scope gates; and
- a narrowly scoped brief for the hardware-baseline milestone.

The milestone explicitly excludes:

- inspecting historical repositories;
- performing hardware investigation;
- selecting or designing Linux technologies or the image;
- designing the SOM application or MCU firmware;
- designing a communication protocol;
- designing brewing logic;
- selecting or implementing UI technology; and
- creating implementation skeletons.

The milestone succeeds when a contributor or coding agent can determine what evidence may be used, what must be independently derived, where each record belongs, what work is currently authorised, and when owner approval is required.

## Initial milestone sequence

1. **Project foundation:** Approve and establish the governance described by this design.
2. **Hardware baseline:** Identify the exact SOM, MCU, carrier-board revision, storage, display and input hardware, buses, attached devices, and relevant connections. Produce verified facts and conspicuous assumptions without designing software.
3. **Linux-image requirements and design:** Define measurable boot-time, footprint, performance, maintainability, update, diagnostics, and hardware-support requirements. Independently evaluate current approaches and select one.
4. **Linux-image implementation:** Build and verify only the approved Linux-image design.
5. **System requirements and subsystem planning:** Establish current product requirements before designing the SOM application, MCU firmware, protocol, brewing logic, or replacement UI.
6. **Individually approved subsystem milestones:** Give each subsystem its own evidence gathering, brainstorming, design, plan, implementation, and verification cycle.

The Linux image is therefore the first technical deliverable, preceded by the hardware evidence needed to design it responsibly. Later roadmap entries remain deliberately coarse to avoid prematurely designing those systems.
