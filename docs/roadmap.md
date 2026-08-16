# Roadmap

This roadmap orders governance and future discovery work. Later entries are not architecture commitments.

1. **Project foundation**
   - Outcome: Establish the charter, clean-slate policies, governance templates, reviews, and milestone controls for subsequent work.
   - Principal exclusion: No technical subsystem design, implementation, or historical repository inspection.
2. **Hardware baseline**
   - Outcome: Verify and record the material hardware facts needed to define the current system boundary.
   - Principal exclusion: No Linux, application, firmware, protocol, brewing-logic, or UI design.
3. **Linux-image requirements and design**
   - Activation: May become active only when the platform-enablement evidence gate records complete initial-gate coverage and explicitly permits requirements work, even while milestone 001 remains active for first-bring-up or later-integration evidence.
   - Outcome: Define and approve the requirements and independent design scope for the Linux image using the gate's verified inputs and mandatory constraints.
   - Principal exclusion: No implementation work or selections beyond what that separately approved milestone authorises.
4. **Linux-image implementation**
   - Activation: Remains inactive until a separately approved Linux-image requirements and design milestone produces an approved design.
   - Outcome: Implement and verify the approved Linux-image design.
   - Principal exclusion: No unapproved expansion into other subsystems or redesign of the approved requirements.
5. **System requirements and subsystem planning**
   - Outcome: Establish system-level requirements and plan bounded, independently approved subsystem work.
   - Principal exclusion: No subsystem implementation or architecture commitment before its individual approval.
6. **Individually approved subsystem milestones**
   - Outcome: Deliver separately authorised subsystem work against approved requirements, evidence, and review gates.
   - Principal exclusion: No work outside the scope of the individual approved milestone.
