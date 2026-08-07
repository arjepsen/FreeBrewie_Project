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

A fact may be used provisionally only when all three conditions are recorded:
confidence is high, verification is time-consuming, and delaying use would
impede progress. The record must explain why verification is time-consuming,
how delay would impede progress, and the next verification action. Even when
all three conditions are met, an unverified fact cannot support a
safety-critical, consequential, or hard-to-reverse decision. Those decisions
must be identified and remain blocked until the fact is verified.

## Historical comparison

Compare only after initial requirements, alternatives, and provisional reasoning, except early factual hardware discovery.

## UI and assets

Separate user-equivalent behaviour from implementation; review each asset for ownership, permission, suitability, and fitness.

## Escalation

Ask the owner about unavailable, conflicting, or consequentially uncertain evidence.
