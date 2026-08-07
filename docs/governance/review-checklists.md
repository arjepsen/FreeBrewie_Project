# Review checklists

Apply every required question before approving a decision, deliverable, or
milestone. Record each result as pass, fail, or inapplicable with a reason.
Any failed required question blocks completion unless it is explicitly marked
inapplicable with a reason.

## Scope review

- [ ] Pass / fail: Are all deliverables authorised by the active milestone?
- [ ] Pass / fail: Are the milestone's explicit exclusions still excluded from the work?
- [ ] Pass / fail: Has the owner approved every scope change or expansion?

## Provenance review

- [ ] Pass / fail: Does every hardware-fact, observable-behaviour,
  historical-observation, and asset-review record identify its source and source
  location?
- [ ] Pass / fail: Does every such record identify its extraction date,
  extractor, and dependent decisions? If no decision depends on it, does the
  field state none and explain why rather than remain blank?
- [ ] Pass / fail / inapplicable with reason: Where the evidence class makes a
  factual claim whose basis may be direct or inferred, are that distinction,
  independent confirmation, and conflicts recorded? Mark this question
  inapplicable only when those evidence-class-specific concepts genuinely do not
  apply.

## Assumption review

- [ ] Pass / fail: Does every assumption state the cheapest available check?
- [ ] Pass / fail: Does every assumption state confidence and a verification action?
- [ ] Pass / fail: Is provisional use limited to facts with recorded high
  confidence, time-consuming verification, and progress-impeding delay?
- [ ] Pass / fail: Are all safety-critical, consequential, and hard-to-reverse
  decisions blocked until their material assumptions are verified?

## Independent-decision review

- [ ] Pass / fail: Does the decision rationale stand without consulting legacy code or historical implementation?
- [ ] Pass / fail: Do the alternatives compare current requirements, approved evidence, assumptions, consequences, and risks?
- [ ] Pass / fail: If historical comparison occurred, did it follow provisional independent reasoning and avoid substituting for rationale?

## Asset review

- [ ] Pass / fail: Are the asset's ownership and licence or permission evidence recorded?
- [ ] Pass / fail: Are suitability and technical fitness reviewed for the intended use?
- [ ] Pass / fail: Are structural UI assets marked for recreation rather than reuse?

## Completion review

- [ ] Pass / fail: Do all measurable completion criteria pass?
- [ ] Pass / fail: Do conflicts and verification debt remain visible in the milestone and dependent records?
- [ ] Pass / fail: Are all scope changes approved by the owner?
- [ ] Pass / fail: Have all required reviews passed or been explicitly marked inapplicable with a reason?
