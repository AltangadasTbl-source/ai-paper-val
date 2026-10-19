# Independent focused recheck: C004

Scope: C004 only, all three registered point-estimate locations. This follow-up preserves the stable ID and all earlier records. Status remains Pending Human Adjudication. No source or reusable derivative was modified.

## Source confirmation

The supplied-source page images were inspected visually, including the table footnotes: main article PDF page 4 (journal page 595), main article PDF page 9 (journal page 600, Table 2), and results Supplement 4 PDF page 14 (eTable 8). Existing rendered pages were used as exact-page views, not text/OCR authority.

- [Main article, PDF page 4](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4): “Adjusted number needed to treat, defined as 1 divided by the difference in adjusted percent improvement between groups”.
- [Main article, Table 2, PDF page 9](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9), footnote d: “Number needed to treat (NNT) to gain 1 additional 30% improvement, i.e., 1 over the difference in the adjusted percent with 30% improvement or greater.”
- [Results Supplement 4, eTable 8, PDF page 14](../../../joi250046supp4_prod_1755300121.15587.pdf#page=14), footnote d repeats that reciprocal definition.

Percentages must be expressed as proportions in the reciprocal: NNT = 100 / (difference in percentage points). The sources show integer NNTs but do not explicitly specify nearest-integer versus upward rounding or print the underlying unrounded adjusted probabilities.

## Location-by-location reproduction

| Exact location | Source percentages matched | Printed NNT matched | Reciprocal from printed values | Input-rounding reciprocal interval | Nearest-integer display gap and relative gap | Whole-person ceiling interpretation |
|---|---|---|---|---|---|---|
| Main Table 2, pain severity, 6 months, HC vs UC | HC 37.1%; UC 22.9% | 8 (6–11) | 100/14.2 = 7.04225 | Difference 14.1–14.3 percentage points; reciprocal 6.99301–7.09220 | Printed 8 interval 7.5–8.5; gap 0.40780; relative gap 0.050975 | Ceiling of 7.04225 is 8; an underlying difference below 14.285714 percentage points produces an NNT above 7 and ceiling 8. |
| Main Table 2, pain-related interference, 6 months, HC vs UC | HC 40.9%; UC 24.3% | 7 (5–9) | 100/16.6 = 6.02410 | Difference 16.5–16.7; reciprocal 5.98802–6.06061 | Printed 7 interval 6.5–7.5; gap 0.43939; relative gap 0.062771 | Ceiling of 6.02410 is 7; plausible undisplayed differences below 16.666667 produce ceiling 7. |
| Supplement 4 eTable 8, Reminder Letters Added subset, 6 months, PT vs UC | PT 35.6%; UC 21.3% | 8 (5–14) | 100/14.3 = 6.99301 | Difference 14.2–14.4; reciprocal 6.94444–7.04225 | Printed 8 interval 7.5–8.5; gap 0.45775; relative gap 0.057218 | The midpoint gives ceiling 7, but permitted undisplayed differences 14.2 to below 14.285714 give NNT above 7 and ceiling 8. For example PT 35.56%, UC 21.32% both display as printed; their difference 14.24 gives 7.02247 and ceiling 8. |

Half-unit percentage intervals are ±0.05 percentage points per displayed one-decimal input; endpoint inclusivity does not affect these conclusions. The generic nearest-integer discrepancy exceeds the workflow 0.05 threshold in all three locations, but that calculation assumes symmetric nearest-integer rounding for an integer clinical count. It does not establish that the printed integer NNT is incompatible with the reciprocal method.

## Coherent source-grounded alternative

Integer ceiling is compatible with the reciprocal definition and is supported by other rows of the same table: primary 3-month PT vs UC has 26.6% minus 20.8%, reciprocal 17.24 and printed NNT 18; primary HC vs UC has 32.0% minus 20.8%, reciprocal 8.93 and printed NNT 9; primary HC vs PT has 32.0% minus 26.6%, reciprocal 18.52 and printed NNT 19. These examples make a ceiling convention a substantive alternative supported by the display itself.

Direct observations: all three percentage pairs and printed integer NNTs above are present; point reciprocals calculated from rounded percentages differ from the printed integers; all three can reconcile with ceiling and allowable undisplayed probabilities.

Inferred explanation: the authors may have rounded positive NNTs upward using unrounded adjusted probabilities. The sources inspected do not explicitly confirm that convention or provide those probabilities. This is an explanation compatible with supplied evidence, not a claim about the analysis code.

## Recheck fields and classification

- Location found: yes, all three registered affected locations.
- Source values/text matched: yes.
- Comparator matched: yes, the adjusted probabilities and reciprocal definition.
- Consistency rule applicable: reciprocal of adjusted between-group probability difference; the integer presentation convention must also be specified before asserting incompatible point estimates.
- Calculation reproduced: yes as arithmetic on printed inputs; the alleged substantive contradiction is not established once source-supported ceiling and undisplayed rates are allowed.
- Necessary inputs available: displayed probabilities and printed integer NNTs are available.
- Exact missing inputs/definitions: unrounded marginal adjusted probabilities used for each NNT, explicit integer-rounding rule, and confirmation that the displayed probabilities and NNT use identical marginal contrasts.
- Source-grounded alternative interpretation: upward rounding of a positive NNT from unrounded adjusted probabilities.
- Evidence state: **not_reproduced**. Determining fact: all three cited integer point estimates can reconcile with the reciprocal definition under a coherent ceiling convention supported by other rows, including permitted rounding intervals in the reminder subset. This is a fresh follow-up evidence fact; earlier historical state is preserved in its original artifact.
- Compared document roles: REPORT for both the main article and the non-plan results supplement. No PLAN content is needed.
- Primary relationship: S_W. All relationships: S_W. Each alleged point-versus-method issue occurs within its own report; the supplement repeats the pattern rather than conflicting with the main article. No S_C relationship is added merely for recurrence.
- Review domain: statistical_results, because the subject is an effect-measure point calculation.
- Classification change: none.
- Exact remaining human question: Were these NNTs obtained by rounding positive reciprocals upward from unrounded adjusted probabilities, and can the authors provide the input contrasts or rounding convention?

## Bounded downstream implications

C004 concerns integer NNT point presentation. A conventional efficacy synthesis extracting adjusted RRs and their confidence intervals is not directly changed by these three NNT displays. For NNT extraction, decision thresholds, or cost-per-additional-responder calculations, 7 versus 8 or 6 versus 7 can change a derived quantity; those changes would be about 14.3% and 16.7% respectively if an analyst substituted those integer values. That does not demonstrate a trial treatment effect changed: NNT is a reciprocal transformation and integerization of an adjusted absolute difference, and the unrounded differences remain unavailable.

Do not merge C004 with C008 (RR-versus-NNT interval/null coverage) or C009 (an NNT point outside its interval). Their interval questions require their own checks and are not resolved by this point-estimate ceiling explanation.

