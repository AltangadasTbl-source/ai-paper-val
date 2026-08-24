# Stable Candidate Ledger

All four distinct records below were registered after merging genuine duplicate proposals from the numeric, statistical-pass-1, and cross-source lanes. Similar proposals were merged only when they concerned the same printed values, comparator, and consistency rule. Every record remains **Pending Human Adjudication**; no validity, importance, severity, acceptance, exclusion, or correction decision is made.

The source-page image resolved the main-text ARISCAT phrase as “score” followed by superscript reference 18 and then “of 26 or greater”; therefore the extraction-only “18 of 26” proposal did not receive a candidate ID. The eTable 8 effect-measure omission was retained as a limitation rather than registered because an absent definition alone, without a conflicting printed measure label, does not meet the candidate threshold.

## C001 — Hypoxemia confidence-interval endpoint sign differs between abstract and Table 3

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Relationship provenance:** N004; S002; proposals P-N004, P1, and CS-01.
- **Exact source locations:** DOC-001, `jama_bluth_2019_oi_190055_16092.pdf`, PDF p. 1 abstract and PDF p. 9 Table 3.
- **Source evidence:** Both locations report intraoperative hypoxemia of 49/989 (5.0%) versus 134/987 (13.6%), an absolute difference of −8.6 percentage points, and P<.001. The abstract prints 95% CI −11.1 to +6.1; Table 3 prints −11.1 to −6.1 and RR 0.51 (0.40 to 0.65).
- **Reported-versus-comparator:** Abstract upper endpoint +6.1 versus Table 3 upper endpoint −6.1 for the same matched result.
- **Consistency rule:** The same population, outcome, contrast, estimate, and confidence level must have the same interval at the same precision; the point estimate must also lie within its interval. The abstract interval contains −8.6 but crosses 0, while the Table 3 interval is wholly negative and agrees with the RR interval and P<.001.
- **Calculation:** 5.0−13.6=−8.6 percentage points. The printed endpoint sign changes the upper endpoint by 12.2 percentage points.
- **Direct observation and inferred explanation:** The sign difference is directly printed. A dropped minus sign is plausible but is not adopted as a correction.
- **Alternative source-grounded interpretations:** Either the abstract or Table 3 may contain the production error; the package does not designate an authoritative analysis-output value.
- **Exact remaining human question:** What was the intended upper endpoint for the high-minus-low hypoxemia risk-difference CI, and which supplied location should be corrected?

## C002 — DIC row finite risk ratio and narrow interval do not reconcile with zero comparator events

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Relationship provenance:** N040; S027; proposals P-N040 and P2.
- **Exact source locations:** DOC-001, `jama_bluth_2019_oi_190055_16092.pdf`, PDF p. 9 Table 3; Table 3 method footnote continues on PDF p. 10 and the analysis method is described on PDF p. 4.
- **Source evidence:** The disseminated intravascular coagulation row prints 1/989 (0.1%) versus 0/987, absolute difference 0.1 (95% CI −0.1 to 0.3), RR 2.00 (95% CI 1.91 to 2.09), and P>.99. The table identifies the effect column as risk ratio and says RR intervals used a Wald likelihood-ratio approximation.
- **Reported-versus-comparator:** A finite RR of 2.00 with a narrow interval excluding 1 is shown against an uncorrected printed risk ratio whose low-group risk is zero; the same row prints P>.99.
- **Consistency rule:** Under the printed risks, (1/989)/(0/987) is not a finite value. Any zero-cell correction or alternate estimator needed to produce a finite RR must be identified before the displayed effect can be reconciled; an interval excluding 1 also conflicts directionally with P>.99 if they summarize the same inferential comparison.
- **Calculation:** High risk=1/989≈0.00101; low risk=0/987=0; their direct ratio has a zero denominator. The displayed CI [1.91,2.09] excludes 1.
- **Direct observation and inferred explanation:** Counts, RR, CI, and P value are directly printed. A zero-cell correction, cell alignment issue, or transcription error is possible but not established.
- **Alternative source-grounded interpretations:** An unstated correction, estimator, or analysis population might have been used; the package supplies no definition that reproduces the displayed RR/CI.
- **Exact remaining human question:** Which estimator and zero-cell rule produced the DIC RR/CI, and are the RR, interval, and P-value cells aligned with the 1-versus-0 event row?

## C003 — Protocol analysis sentence combines odds-ratio and relative-risk labels

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationship provenance:** S202; proposal P3.
- **Exact source locations:** DOC-002, `joi190055supp1_prod_16092.pdf`, physical PDF p. 23 (footer page 22), section 8.2 Analysis; comparator definitions in DOC-004, `joi190055supp3_prod_16092.pdf`, PDF pp. 1-3.
- **Source evidence:** The protocol states that “the odds ratio relative risks with corresponding 95% confidence levels interval” will be calculated using logistic regression. The final SAP separately identifies the primary effect as a risk ratio.
- **Reported-versus-comparator:** One planned-analysis phrase attaches both odds-ratio and relative-risk labels to the same output without a separator, alternative-analysis definition, or conversion rule.
- **Consistency rule:** Odds ratio and risk ratio are distinct effect measures and must not be used as interchangeable labels for one numeric result unless the transformation or separate analyses are specified.
- **Calculation:** No arithmetic is needed; the reproducible check is the compound measure label against the separately named risk-ratio estimand in the supplied final SAP.
- **Direct observation and inferred explanation:** The compound phrase is directly printed. An editing artifact, intended alternative analyses, or an unreported conversion are possible explanations.
- **Alternative source-grounded interpretations:** Because the protocol preceded the final SAP, the later risk-ratio specification may supersede this wording, but it does not resolve what the protocol phrase itself intended.
- **Exact remaining human question:** Was section 8.2 intended to specify an odds ratio, a risk ratio, or distinct analyses, and should the compound label be clarified in the archived protocol?

## C004 — eFigure 11 mortality values are described as extra-pulmonary complications

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationship provenance:** N218; S214; proposals P-N218, P5, and CS-03.
- **Exact source locations:** DOC-005, `joi190055supp4_prod_16092.pdf`, PDF p. 41 eFigure 11; comparison with DOC-005 PDF p. 40 eFigure 10 and DOC-001 PDF p. 10 Table 3.
- **Source evidence:** eFigure 11 is titled “Probability of death in the first 5 postoperative days,” labels its effect “hazard ratio for 5-day mortality,” and prints 0.5% versus 0.3%, HR 1.67 (0.40 to 6.97), P=.484. Its narrative calls the same 0.5%/0.3% values “the rate of postoperative extra-pulmonary complications.” eFigure 10 separately reports extra-pulmonary complications as 16.9% versus 15.2%, HR 1.12.
- **Reported-versus-comparator:** The eFigure 11 narrative outcome noun conflicts with its title, y-axis, mortality effect label, and matching Table 3 mortality values.
- **Consistency rule:** A figure narrative must identify the same outcome as its displayed values and effect estimate. Mortality and postoperative extra-pulmonary complications are separately defined and numerically distinct outcomes in the supplied package.
- **Calculation:** No rounding issue applies: mortality is 5/989≈0.5% versus 3/987≈0.3%, whereas the separate extra-pulmonary composite is 16.9% versus 15.2%.
- **Direct observation and inferred explanation:** The conflicting outcome labels and values are directly printed. Carry-forward wording from eFigure 10 is plausible but not established as the correction.
- **Alternative source-grounded interpretations:** The narrative sentence may refer to a neighboring figure, but no cross-reference says so and its printed values match eFigure 11 mortality.
- **Exact remaining human question:** Which outcome should the eFigure 11 narrative name, and does the final production source require correction of the figure narrative or another linked representation?

## Registration Summary

- **Stable candidate IDs:** C001, C002, C003, C004
- **Candidate count:** 4
- **Disposition for every stable ID:** Pending Human Adjudication
- **Display-zero-only candidates:** 0
