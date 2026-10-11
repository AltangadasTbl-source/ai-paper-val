# Stable Candidate Ledger

All candidates are **Pending Human Adjudication**. Registration follows the independent initial screen and main-result source order. Stable IDs are never deleted. No previous-run candidate or adjudication artifact was used.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article Table 2 time rows and footnotes vs REPORT main article Statistical Analysis | reproduced | CONFIRMED | F-ST1-001 |
| C002 | protocol_report | P_R | P_R | PLAN SAP section 7.5.2 vs REPORT main article Methods and Figure 3 age subgroups | reproduced | CONFIRMED | F-XS-001 |

Evidence states are reproduced as assigned by the fresh mechanical rechecker; the fresh quality-control auditor confirmed inclusion for both IDs. The classification table is finalized for reporting. F-ST1-002 is preserved as duplicate statistical-checker provenance for C002, with its additional contextual location retained; its screening decision is SCREENED_OUT/DUPLICATE_OF_INCLUDED and therefore it is not an additional INCLUDE finding in the classification table.

## C001 — Identification of the adjusted time-effect outputs

**Candidate statement:** Table 2 gives two adjusted time-effect outputs for each of door-to-balloon and door-to-needle time, without identifying the separate analysis targets that produced its difference and beta-coefficient columns.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2 time rows and footnotes vs REPORT main article Statistical Analysis

**Finding IDs:** F-ST1-001

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** Every cited and contextual page was found and source-confirmed; printed inputs, half-unit display bounds and the method-identification comparison were reproduced without a transcription or classification change. See [complete recheck facts](verification/evidence_recheck.md).

**Checker provenance:** Fresh statistical pass 1 main/PLAN shard; independently included by root/screen_initial.

**Classification rationale:** All conflicting method/output descriptions are in the main REPORT. The issue concerns statistical-method identification and the quantity extracted. No PLAN location is a conflicting comparator.

**Classification ambiguity:** The two outputs may intentionally target distinct conditional, marginal, transformed, or otherwise defined quantities; the supplied descriptions do not identify the mapping. No equality of those quantities is assumed.

**Exact source locations:** REPORT [main physical p. 6, Table 2 door-to-balloon and door-to-needle rows, both effect headers, title and footnotes b/c](../../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [main physical p. 3, Statistical Analysis](../../jama_huffman_2018_oi_170166.pdf#page=3). REPORT [main p. 7 process narrative](../../jama_huffman_2018_oi_170166.pdf#page=7) supplies adjacent context, not a separate conflict.

**Source evidence:** Door-to-balloon medians are control 65 (53–105) min, n=4022, and intervention 77 (55–118) min, n=3639. Difference: 6.18 (95% CI −4.78 to 17.14); beta coefficient: 13.00 (3.64–22.36). Door-to-needle medians are 44 (30–67) min, n=1455, and 45 (27–75) min, n=1433. Difference: 0.40 (−5.23 to 6.03); beta coefficient: 5.00 (−5.20–15.20). Both outputs cite the common footnote describing marginal effects and mixed-effects logistic or quantile regression with clustering and temporal trends; footnote c identifies beta coefficients.

**Reported-versus-comparator:** Two distinct effect columns share an adjustment description without a separate time-result model/target mapping. Their distinct values are an observation; neither is asserted to fail arithmetic or its own interval rule.

**Footnote precision:** Both effect headers cite footnote b, but its grammatical subject is the ORs and beta coefficients. It names marginal-effects differences and mixed-effects logistic or quantile regression; it does not separately identify the time Difference column's target. Inclusion does not assume that a conditional coefficient must equal a marginal contrast.

**Reasoning procedure:** Identify the outcome, units, population, contrast, model labels and both reported outputs. Apply display-precision bounds and distinguish a source-grounded method-identification gap from the immediately resolvable percent header. Do not compare modeled effects with crude median differences as an identity test.

**Calculation:** Balloon point bounds [6.175,6.185] and [12.995,13.005] are disjoint; point difference 6.82. Needle bounds [0.395,0.405] and [4.995,5.005] are disjoint; point difference 4.60. Balloon's first CI spans zero, while beta lower-bound display interval [3.635,3.645] excludes zero. These calculations establish different outputs and inferential readings, without asserting they must be equal.

**Affected result or extracted value:** The adjusted intervention time effects, especially balloon 6.18 (−4.78,17.14) versus 13.00 (3.64,22.36), and the analysis quantity to which each belongs.

**Why context does not resolve it:** The column names identify two outputs but the common method text does not map their models, quantiles, standardization targets or reference populations. The minute units are readily identifiable; the adjusted quantity to extract remains unclear.

**Alternative source-grounded interpretations:** An intentionally distinct marginal time contrast and conditional quantile coefficient, or different transformed/model targets, could explain the two columns. The package does not establish which explanation applies. Missing definitions: column-specific model, target, quantile/scale, reference population, and interval construction.

**Potential downstream evidence impact:** An extractor could select a different adjusted time estimate and interval, including a different zero-inclusion reading, if the analysis target is not clarified. No downstream propagation or paper-level conclusion change is asserted.

**Human verification steps:** Read the two rows and footnotes together with the statistical methods, identify the model and estimand for each column, and establish which adjusted time quantity each reported estimate represents.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned and reported age-subgroup specification

**Candidate statement:** The supplied SAP specifies an age split at 65 for the primary-endpoint subgroup analysis, while the report calls age groups split at 50 and 70 prespecified.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP section 7.5.2 vs REPORT main article Methods and Figure 3 age subgroups

**Finding IDs:** F-XS-001

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Mechanical evidence recheck:** All PLAN and REPORT locations, including contextual main p. 2, were found and visually source-confirmed. Cutoffs, effect rows and arm/event sums reproduce; no transcription or classification change was needed. See [complete recheck facts](verification/evidence_recheck.md).

**Checker provenance:** F-XS-001 from the fresh cross-source checker and F-ST1-002 from the independent statistical checker describe one issue. The screen includes F-XS-001 and links the duplicate F-ST1-002 to C002. All locations from both findings are retained.

**Classification rationale:** Prospective SAP content is PLAN; the main results are REPORT. Their age analysis specifications differ. Consistent report repetitions and the SAP-referencing statement are context, not additional S_W relationships.

**Classification ambiguity:** A later prospective amendment may not be supplied. This limits attribution of the specification change, not the observed printed comparison.

**Exact source locations:** PLAN [SAP physical p. 7, section 7.5.2, lines 1243–1254](../../joi170166supp2_prod.pdf#page=7); REPORT [main physical p. 3, Statistical Analysis subgroup sentence](../../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [main physical p. 9, Figure 3 title, all three age rows and adjacent subgroup paragraph](../../jama_huffman_2018_oi_170166.pdf#page=9). REPORT [main physical p. 2, Study Design statement referring to the supplied SAP](../../jama_huffman_2018_oi_170166.pdf#page=2) is contextual.

**Source evidence:** SAP a priori age groups: <65 and >65 years. Reported prespecified groups: <50, 50–69 and ≥70 years. Respective adjusted MACE ORs: 1.53 (0.83–2.79), 0.89 (0.67–1.19), 0.98 (0.71–1.35); adjusted differences: 1.42% (−0.71 to 3.54), −0.57% (−2.02 to 0.88), −0.23% (−3.32 to 2.85). Intervention event/denominators: 58/2079, 297/6606, 247/2623; control: 68/2045, 326/5863, 251/2158.

**Reported-versus-comparator:** The three reported categories cannot be matched to the SAP's two planned categories by variable name alone. The report confirms prespecification without identifying a revised specification in those locations.

**Reasoning procedure:** Match primary 30-day MACE, analysis population, model and age subgroup family. Compare group membership boundaries, not the preferred clinical cutoff. Preserve the possibility of a later amendment without assuming one exists.

**Calculation:** Intervention denominators 2079+6606+2623=11308 and events 58+297+247=602; control denominators 2045+5863+2158=10066 and events 68+326+251=645. The reported middle age group crosses 65, so no merging of the displayed categories recovers the planned split. Uncertainty about age exactly 65 and numeric display precision do not reconcile cutoffs at 50 and 70. Adjusted ORs/RDs cannot be remapped by averaging the displayed effects.

**Affected result or extracted value:** The three age-specific adjusted primary MACE effects and their interpretation as prespecified analyses, compared with effects for the planned split at 65.

**Why context does not resolve it:** The displayed age groups are clear, but neither the adjacent report statements nor the supplied SAP explains how those groups relate to the a priori split. Different category membership is not a field-specific synonym.

**Alternative source-grounded interpretations:** An additional prospective amendment could define the reported groups; an additional analysis may have been displayed; or the planned split may have been performed separately. The supplied evidence does not identify which applies.

**Potential downstream evidence impact:** A reviewer could extract the three reported age effects as the planned age-specific effects even though they do not represent the SAP split. No conclusion change or downstream propagation is asserted.

**Human verification steps:** Confirm the boundaries and all age effects directly, identify any later prospective specification, and establish how the reported analysis relates to the SAP age split.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
