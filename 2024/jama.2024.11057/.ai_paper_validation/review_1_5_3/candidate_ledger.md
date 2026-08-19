# Stable Candidate Ledger

All candidates are **Pending Human Adjudication**. Similarities were reviewed before stable-ID assignment; the three records below concern different printed facts, comparators, and consistency rules and were not merged. No candidate-count limit was applied.

## C001 — Quit-date pre-message duration conflicts between the main article and both support documents

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Checker provenance:** `checkers/cross_source_consistency.md`
- **Exact source locations:** [D001 main article, PDF p. 3](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3); [D002 study protocol, PDF p. 2](../../joi240078supp1_prod_1739900423.22574.pdf#page=2); [D003 results supplement, PDF p. 2](../../joi240078supp2_prod_1739900423.24574.pdf#page=2).
- **Printed evidence:** D001 states that users who set a quit date receive messages for **6 weeks before** and 8 weeks after the quit date. D002 states **a week before** and 8 weeks afterward. D003 states **1 week preceding** and 8 weeks afterward.
- **Reported-versus-comparator:** `6 weeks before` versus `1 week before` for the same named intervention, quit-date subgroup, temporal anchor, and unit. The three sources agree on the 8-week post-quit segment.
- **Consistency rule:** Matched descriptions of one intervention component cannot simultaneously specify unequal pre-quit durations without a version or scope qualifier.
- **Calculation or logical comparison:** `6 weeks != 1 week`; the absolute difference is 5 weeks.
- **Direct observation versus inference:** The printed duration conflict is direct. A program-version change, outdated support text, or main-article transcription issue is possible but not established by the supplied package.
- **Source-grounded alternatives:** The main article may describe a different intervention release; the two support documents may describe an earlier release; or one occurrence may be a production error. No supplied delivery log or version history resolves which schedule participants received.
- **Quality-control relevance:** A reader or implementation reviewer could extract conflicting intervention exposure durations from the supplied documents.
- **Potential downstream evidence impact:** If confirmed, an evidence extractor or intervention-description review could copy the wrong pre-quit duration; this observation does not establish a changed trial conclusion.
- **Exact human question:** What pre-quit message duration was actually delivered during the trial, and were all three documents intended to describe the same program version?
- **Human verification steps:** Check trial-period delivery specifications, version history, participant message logs, and editorial source files; then reconcile the duration or add version/effective-date qualifiers.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 4 labels motivation and confidence as median (IQR) but prints single parenthetical dispersion values

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** `checkers/numeric_consistency.md`, relationship `N052`
- **Exact source locations:** [D003 results supplement, PDF p. 12](../../joi240078supp2_prod_1739900423.24574.pdf#page=12), eTable 4; comparator convention in the same table; [D001 main article, PDF p. 4](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), Table 1.
- **Printed evidence:** eTable 4 labels motivation and confidence as `median (IQR)` but prints motivation as `4.1 (0.8)` in both response groups and confidence as `3.2 (1.1)` and `3.5 (1.1)`. Other median-IQR rows in the same table use lower-to-upper intervals, such as `30.0 (27.0-30.0)` and `4.0 (3.0-5.0)`. D001 Table 1 likewise uses interval-form IQRs for these scales.
- **Reported-versus-comparator:** The summary label calls for a median plus an interquartile range, while the displayed parenthetical contains one number and follows the visual form ordinarily used for a standard deviation.
- **Consistency rule:** Under the source's own table convention, `median (IQR)` is displayed as `median (Q1-Q3)`, not as a single parenthetical number.
- **Calculation or logical comparison:** Expected two IQR bounds; observed one parenthetical value for each affected cell. Rounding cannot convert a single dispersion number into two interval endpoints.
- **Direct observation versus inference:** The label/display mismatch is direct. That the cells may instead be means (SDs) is an inference, not a locally proven correction.
- **Source-grounded alternatives:** The rows may be intended as means (SDs), or the source may have used an unstated one-number IQR convention only for these cells. Participant-level data and an explanatory note are not supplied.
- **Quality-control relevance:** A data extractor could encode these as medians and IQRs even though the printed parentheticals resemble SDs.
- **Potential downstream evidence impact:** If confirmed, an evidence table or synthesis could copy the wrong summary-statistic type; this observation does not establish an error in treatment-effect estimates.
- **Exact human question:** Were the motivation-to-quit and confidence-to-quit entries intended to be means (SDs), or what source-defined convention makes a single number an IQR in these rows?
- **Human verification steps:** Compare the analysis output and table-production file with the manuscript labels; confirm the intended summary statistic and both group values.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eAppendix C prints IPWR once for a result otherwise defined and labelled as IPRW

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Checker provenance:** `checkers/statistical_pass_2.md`, relationships `S007`, `S019`, and `S020`
- **Exact source locations:** [D003 results supplement, PDF p. 5](../../joi240078supp2_prod_1739900423.24574.pdf#page=5), eAppendix C; [D003 results supplement, PDF p. 14](../../joi240078supp2_prod_1739900423.24574.pdf#page=14), eTable 5; [D001 main article, PDF p. 4](../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4), Statistical Methods.
- **Printed evidence:** D003 p. 5 defines `IPRW` as inverse probability of retention weighting and uses `IPRW` for the 30-day result and later discussion, but the repeated-PPA sentence prints `IPWR` with RR 2.21 (95% CI 1.67-2.93). D003 eTable 5 and D001 label the same analysis `IPRW`.
- **Reported-versus-comparator:** Undefined `IPWR` versus defined `IPRW` for the same weighted repeated-PPA result; the numeric RR and interval match.
- **Consistency rule:** A method abbreviation should match its explicit expansion and the label attached to the same result elsewhere.
- **Calculation or logical comparison:** `IPWR != IPRW`; the final two letters are transposed, and the package defines only `IPRW`.
- **Direct observation versus inference:** The two printed strings are direct observations. A typographical transposition is plausible but remains an inferred explanation.
- **Source-grounded alternatives:** `IPWR` could be an unstated second abbreviation, but no source defines it and the matching table uses `IPRW`.
- **Quality-control relevance:** An undefined transposed abbreviation can create avoidable ambiguity about whether the repeated-PPA result used the stated retention-weighting analysis.
- **Potential downstream evidence impact:** If confirmed, a data extractor or methods summary could preserve an undefined method label; the numeric treatment-effect result itself is consistent across the supplied locations.
- **Exact human question:** Does `IPWR` on D003 p. 5 refer to the defined IPRW analysis for RR 2.21, and should the label be reconciled with the rest of the package?
- **Human verification steps:** Compare the analysis output and manuscript production file for the repeated-PPA sentence with eTable 5 and the defined method name.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
