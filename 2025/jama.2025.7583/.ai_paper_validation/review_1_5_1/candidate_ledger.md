# Stable Candidate Ledger

Candidate discovery was rebuilt from the complete Workflow 1.5.1 relationship maps and checker outputs. Duplicate checker observations were merged only when they concerned the same printed values, comparator, and rule. The stable set contains three distinct candidates. Every candidate remains **Pending Human Adjudication**; no severity, validity, acceptance, exclusion, or correction is assigned.

## C001 — Primary-endpoint midline-shift boundary differs across matched supplied sources

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationships:** N009, N033; S001, S002, S014, S026, S034, S042, S043, S051, S052
- **Exact source locations:** [Main article — PDF p. 3](<../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>); [protocol — PDF p. 7](<../../joi250033supp1_prod_1750956987.76581.pdf#page=7>); [protocol — PDF p. 16](<../../joi250033supp1_prod_1750956987.76581.pdf#page=16>); [results supplement — PDF p. 15](<../../joi250033supp4_prod_1750956987.77981.pdf#page=15>); [SAP — PDF p. 3](<../../joi250033supp5_prod_1750956987.78281.pdf#page=3>).
- **Direct observation:** The main article says “5 mm or greater,” the protocol and results supplement say `≥5 mm`, and the SAP says `>5 mm` for the matched primary-endpoint imaging component.
- **Comparator and rule:** For a measured shift `x`, `x ≥ 5` includes `x = 5`, while `x > 5` excludes it. The inequality difference cannot be reconciled by rounding.
- **Alternative source-grounded interpretations:** The SAP inequality may be typographic or version-specific, or the repeated `≥5 mm` wording may reflect the operational final rule. No supplied source explains this boundary change, and no participant-level imaging data show whether an exactly 5-mm case existed.
- **Checker provenance:** Numeric NC-01; statistical pass-1 P1-STAT-02; complete cross-source provisional endpoint candidate.
- **Exact human question:** Which boundary governed final endpoint adjudication, and should the discrepant supplied document be corrected or annotated?

## C002 — Printed sample-size attrition allowance does not reconcile with the printed target

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Relationships:** N011, N036, N040, N056; S003, S012, S022, S029
- **Exact source locations:** [Protocol — PDF p. 50](<../../joi250033supp1_prod_1750956987.76581.pdf#page=50>); [SAP — PDF p. 5](<../../joi250033supp5_prod_1750956987.78281.pdf#page=5>); [main article — PDF p. 3](<../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=3>).
- **Direct observation:** Protocol and SAP print 142 required participants per group, a 20% loss-to-follow-up assumption, and 342 total participants (171 per group); the main article repeats the 20% allowance and total 342.
- **Comparator and rule:** The stated analysable target is `142 × 2 = 284`. If 20% of enrolled participants are lost, aggregate enrollment needed is `284 / 0.80 = 355`; maintaining two equal whole-participant arms requires rounding `177.5` up to `178` per arm, or 356 total. By comparison, `342 × 0.80 = 273.6`. The printed 342 is 13 below the aggregate loss-fraction result and 14 below the balanced whole-arm target.
- **Alternative source-grounded interpretations:** The authors may have added 20% to 284 (`340.8`) and rounded/design-adjusted to 342, or an unreported sequential-design convention may explain the target. The supplied text does not name that alternative convention.
- **Checker provenance:** Numeric NC-02; statistical pass-1 P1-STAT-01.
- **Exact human question:** Was “20% loss” implemented as a 20% addition rather than a 20% loss fraction, or did an unstated sequential-design calculation produce 342?

## C003 — Standard-care surgery-type counts exceed their shared printed denominator

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Relationships:** N021
- **Exact source location:** [Main article — PDF p. 5](<../../jama_shotar_2025_oi_250033_1750956987.75881.pdf#page=5>), Table 1, Treatment rows.
- **Direct observation:** The standard-care column prints `146/163 (89.6%)` for trepanation burr-hole craniostomy and `18/163 (11.0%)` for trephine craniostomy.
- **Comparator and rule:** `146 + 18 = 164`, exceeding the shared printed denominator 163 by one; the displayed percentages sum to 100.6%. Percentage rounding does not resolve the integer excess.
- **Alternative source-grounded interpretations:** A participant may be counted in both rows, or one numerator/denominator may be typographic. The table does not state overlap or a separate denominator, and the supplied evidence does not identify which value should change.
- **Checker provenance:** Numeric NC-03.
- **Exact human question:** Were any participants counted in both procedure rows; if not, which printed count or denominator should be corrected, and should the overlap/missingness rule be stated?

## Registration summary

- Stable candidate IDs: C001, C002, C003.
- Genuine duplicate merges: the endpoint-boundary observations from three checker lanes were merged into C001; the attrition-arithmetic observations from numeric and statistical lanes were merged into C002.
- No post-ID merge, deletion, suppression, or renumbering is permitted.
- No display-zero P-value candidate was registered.
