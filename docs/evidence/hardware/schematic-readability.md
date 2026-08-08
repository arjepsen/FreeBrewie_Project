# MCU schematic structural-readability report

## Pinned artifact

- Repository: `https://github.com/arjepsen/FreeBrewie-MCU`
- Default branch at retrieval: `main`
- Commit: `31efc798a4eff7208e3ed538215ef2ddfcc02884`
- Artifact: `Documentation/BrewieMCU.kicad_sch`
- Immutable URL: `https://raw.githubusercontent.com/arjepsen/FreeBrewie-MCU/31efc798a4eff7208e3ed538215ef2ddfcc02884/Documentation/BrewieMCU.kicad_sch`
- Git blob: `59cd121791764a0f68dce8ca8aed58621468527a`
- Retrieved: 2026-08-08
- Evidence status: selected, inferred, and non-authoritative

This report assesses file structure and parser suitability only. It does not turn schematic content into hardware-fact claims.

## Format and completeness

The artifact is a UTF-8 KiCad S-expression schematic without a byte-order mark and with CRLF line endings. Strict UTF-8 decoding succeeds; strict ASCII decoding fails because the file contains six micro-sign (`U+00B5`) characters. Its root form is `kicad_sch`, its file-format version marker is `20250114`, and its generator markers are `eeschema` and `9.0`.

GitHub's pinned contents metadata reports 789,976 bytes and blob `59cd121791764a0f68dce8ca8aed58621468527a`. The immutable raw download is exactly 789,976 bytes; `git hash-object --no-filters` produces the same blob identifier, and the raw bytes compare equal to GitHub's base64 content response.

A quote-aware S-expression parser consumed 132,634 lexical tokens into exactly one root form. The parse stack ended empty, with no atom outside the root, extra closing parenthesis, unterminated quoted string, or duplicate explicit UUID among 2,188 UUID fields. The complete file is therefore retrievable and structurally balanced.

## Dependencies

The file has one embedded `lib_symbols` block containing 36 unique symbol-library definitions. All 335 placed symbol instances contain a `lib_id`, and every placed `lib_id` resolves to one of those embedded definitions. No external symbol file or symbol-library table is required to identify the placed symbol structures.

Eight unique non-empty footprint identifiers are referenced but their external footprint libraries are not embedded in this schematic and were not inspected:

- `Capacitor_SMD:C_0402_1005Metric`
- `Diode_SMD:D_SMF`
- `Diode_SMD:D_SOD-523`
- `Package_QFP:TQFP-100_14x14mm_P0.5mm`
- `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm`
- `Package_TO_SOT_SMD:SOT-23`
- `Package_TO_SOT_SMD:SOT-23-6`
- `SOIC127P600X175-8N`

The last identifier is unqualified by a library nickname. This is an unresolved external footprint identifier, but it does not prevent logical schematic structure from being parsed.

There are no top-level sheet, image, or table objects and no external sheet/image/table paths. One `sheet_instances` block contains the root sheet path only. Nine datasheet URLs and one legacy `~` placeholder occur as informational symbol properties; the URLs were not fetched and are not parser dependencies.

## Extractable structures

The structural parse exposes:

- 36 embedded symbol definitions and 335 placed symbol instances using 36 unique, internally resolvable library identifiers;
- component `Reference` and `Value` properties on all 335 placed instances, with no missing field;
- 974 placed pin records, with at least one pin record on every placed symbol instance;
- 18 connector-symbol instances across eight connector library identifiers;
- 196 global labels, 156 junctions, and 511 wire objects;
- zero local labels, hierarchical labels, bus objects, bus-entry objects, sheets, images, and tables; and
- one root-sheet instance record.

Three reference strings (`U2`, `U5`, and `U6`) recur because each has units 1 through 5. There is no duplicate reference-and-unit pair, so these are resolvable multi-unit instances rather than an identifier collision.

## Unresolved structures

`kicad-cli` is not installed in the execution environment, so a native KiCad 9 netlist export or electrical-rules parse could not be run. The quote-aware parser proves syntax and identifier relationships but does not implement KiCad's geometry-to-net, implicit-power, multi-unit electrical, or ERC semantics.

No explicit `no_connect` objects occur. Consequently, absence of a wire at a pin cannot be classified here as intentional or accidental. The eight footprint identifiers remain externally unresolved, the unqualified footprint identifier noted above is a parse warning for later package-level work, and the informational datasheet targets remain unvalidated. There are no unresolved placed symbol-library identifiers and no S-expression parse warnings.

Pin-to-net extraction status: **partial**. Symbol pins, wires, junctions, and global labels are structurally available, but this task did not produce or validate a complete connectivity graph with native KiCad semantics.

## Suitability for fact extraction

**usable-with-limitations**

The artifact is complete, balanced, and internally resolves every placed symbol to an embedded definition. It is usable for later inferred structural extraction of symbol identities, reference/value fields, connector structures, and graphical connectivity primitives. Complete pin-to-net facts must remain unverified until a KiCad 9 netlist/export or an independently checked connectivity resolver confirms the graphical and implicit electrical semantics. The schematic's milestone status remains non-authoritative inferred evidence regardless of parser completeness.

## Required owner input

No owner input is required for the limited structural extraction described above. Before treating pin-to-net extraction as complete, the owner must provide a KiCad 9-generated netlist/connectivity export from this exact blob or approve a reproducible KiCad 9 parsing environment or equivalently verified resolver. Any later need to resolve external footprint libraries or read the referenced datasheets must stay within the approved supporting-artifact boundary or receive explicit milestone scope expansion.
