# Independent inclusion screen — initial stage

Runtime agent ID: 01a129c2-36f7-71d0-acc6-f76cb4e358b4. Role: qc162_inclusion_screener. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN.

QUALITY_CONTROL_SCOPE.md and the complete Workflow 1.6.2 review contract, including its inclusion-screen section, were read completely. Assigned checker inputs are checkers/numeric_consistency.md (0 findings), checkers/cross_source_consistency.md (8 findings), and checkers/statistical_pass_1.md (12 findings). Every finding was independently screened from supplied source evidence, without prior-run scientific conclusions, external evidence, or a target count. Checker exclusions remain available for the mandatory statistical pass-2 review.

Source confirmation used direct CPU Poppler pdftotext 26.01.0, with commands of the form `pdftotext -f N -l N -layout SOURCE -`, for the complete main REPORT and report supplements and each cited PLAN location; source-linked rendered main Table 2 p.6 and subgroup eFigure p.2 were inspected visually. No new derivative, source change, or reusable-asset change was made. Physical PDF pages, not printed footer numbering, determine all links below. Document roles are DOC-001 main REPORT; DOC-002 protocol PLAN; DOC-003 SAP PLAN; DOC-004 subgroup REPORT; DOC-005 sharing statement REPORT.

## Screening decisions

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-XS-007 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-008 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-001 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C001 |
| F-ST1-002 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C013 |
| F-ST1-003 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-ST1-004 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-005 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C008 |
| F-ST1-006 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C003 |
| F-ST1-007 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-008 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-ST1-009 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-ST1-010 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C004 |
| F-ST1-011 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C005 |
| F-ST1-012 | statistics_pass_1 | initial | SCREENED_OUT | DUPLICATE_OF_INCLUDED | C002 |
| F-ST2-001 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST2-002 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C010 |

## One-sentence independent justifications

- **F-XS-001 — Route A, category 1:** The [day-5 EQ-5D interval and P=.04](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) show a statistically significant contrast while the [abstract](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1) and [secondary-results paragraph](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) state no significant difference for any secondary endpoint or quality of life, and a possible separate overall test is an alternative interpretation that cannot remove this always-register conflict.
- **F-XS-002 — Route B:** The [SAP exposed-participant requirement](../../../joi240139supp2_prod_1741633738.17362.pdf#page=13) and [reported safety analysis sets containing 12/13 nonrecipients](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=3) define different participant memberships for the [AE/SAE proportions](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8), leaving the planned-versus-reported safety population unresolved despite the footnote identifying one additional exposed placebo participant.
- **F-XS-003 — Route B:** The [planned cumulative 72-hour opioid endpoint](../../../joi240139supp1_prod_1741633738.16362.pdf#page=17) and [reported 24-hour endpoint with medians 70.6 and 45.0 mg](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) have distinct exact accumulation windows for an abstract-listed secondary outcome and no supplied explanation identifies the reported values as the planned 72-hour quantity.
- **F-XS-004 — Route A, category 5:** The [unconditional primary Edinburgh-versus-rest sensitivity analysis](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15) has no result in the complete supplied REPORT union, and the preceding missingness condition does not qualify this separate paragraph.
- **F-XS-005 — Route A, category 5:** Total hospital stay is [tertiary in the article outcome hierarchy](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4) and [Table 3](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8) but included in the [discussion's named 11-secondary-endpoint set](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), reproducing an outcome-status conflict even if the discussion uses secondary loosely.
- **F-XS-006 — Route B:** The [planned 30-day operation-relative readmission endpoint](../../../joi240139supp2_prod_1741633738.17362.pdf#page=10), repeated in [article methods](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), and [Table 3's 90-day label for 31/34 readmissions](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8) leave the extracted events' observation window unclear, a quantity-changing endpoint comparison rather than a peripheral copy of tertiary numbers.
- **F-XS-007 — Route B:** The [same subgroup display's 99% graphical legend and 95% numeric-interval caption](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2) give incompatible uncertainty definitions for primary-outcome subgroup estimates, and the possibility of distinct graphical/numeric intervals is not identified sufficiently to determine the confidence level a data extractor should attach.
- **F-XS-008 — Route A, category 5:** The [planned binary GI-2 status at 96 hours](../../../joi240139supp2_prod_1741633738.17362.pdf#page=20), [72-hour vomiting burden](../../../joi240139supp2_prod_1741633738.17362.pdf#page=21), and [rescue-antiemetic doses](../../../joi240139supp2_prod_1741633738.17362.pdf#page=22) are missing planned measurements/analyses of abstract-listed key secondary outcomes in the complete supplied REPORT union and cannot be replaced by all-follow-up event counts or PONV-score categories.
- **F-ST1-001:** This reproduces F-XS-001's EQ-5D interval/test-versus-narrative issue, so it is consolidated with F-XS-001 while preserving its additional source/context locations.
- **F-ST1-002:** This reproduces F-XS-007's subgroup confidence-level ambiguity, so it is consolidated with F-XS-007 and preserves all 12 subgroup rows plus the separate overall row as context.
- **F-ST1-003 — Route A, category 5:** The [protocol's primary logit model](../../../joi240139supp1_prod_1741633738.16362.pdf#page=40) is not the [reported primary log-link model](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), and the [disclosed post-analysis SAP update](../../../joi240139supp2_prod_1741633738.17362.pdf#page=3) explains documentary history without supplying the originally stated primary analysis or establishing an earlier prospective replacement.
- **F-ST1-004 — Route A, category 5:** The [planned unadjusted ITT and per-protocol primary estimates/intervals/tests](../../../joi240139supp2_prod_1741633738.17362.pdf#page=20) are absent from the supplied REPORT union, whose [primary display](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) and [footnote](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7) explicitly identify adjusted results rather than the omitted primary model rows.
- **F-ST1-005:** This reproduces F-XS-004's omitted Edinburgh primary sensitivity analysis, so it is consolidated with F-XS-004 and retains its additional discussion/limitation locations.
- **F-ST1-006:** This reproduces F-XS-003's 72-hour versus 24-hour opioid endpoint-window issue, so it is consolidated with F-XS-003 and retains the additional protocol data-collection locations.
- **F-ST1-007 — Route B:** The [endpoint-specific discharge/readiness GLM tables](../../../joi240139supp2_prod_1741633738.17362.pdf#page=26) and [sample GLM commands](../../../joi240139supp2_prod_1741633738.17362.pdf#page=36) conflict with the [general SAP Cox rule](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14) and [reported Cox HRs](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), leaving the planned analysis of two abstract-listed key secondary endpoints unclear even though the implemented report model is explicit.
- **F-ST1-008 — Route B:** The [ERAS subgroup sample command omits age](../../../joi240139supp2_prod_1741633738.17362.pdf#page=38) despite the [specified primary-model minimization covariates and subgroup interaction extension](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), reproducing a plan-internal primary-outcome subgroup adjustment conflict relevant to the [reported ERAS RRs and interaction P=.966](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2) without assuming that the sample command was executed.
- **F-ST1-009 — Route B:** The [GI-2/GI-3 endpoint prose uses surgery as time origin](../../../joi240139supp2_prod_1741633738.17362.pdf#page=9) while the [endpoint-specific survival variables use start of general anesthesia](../../../joi240139supp2_prod_1741633738.17362.pdf#page=34), an exact key-secondary analysis-variable definition conflict that can change elapsed-time construction for the [reported HRs](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) without assuming a particular delay or numerical effect on those estimates.
- **F-ST1-010:** This reproduces F-XS-005's total-hospital-stay outcome-status conflict, so it is consolidated with F-XS-005 and preserves the plans as corroborating hierarchy evidence.
- **F-ST1-011:** This reproduces F-XS-006's readmission endpoint-window issue, so it is consolidated with F-XS-006 and retains the additional SAP dummy-table and protocol time-anchor locations.
- **F-ST1-012:** This reproduces F-XS-002's planned exposed versus reported expanded safety membership issue, so it is consolidated with F-XS-002 rather than creating a separate issue from the same 25 nonrecipients.

## Consolidated issue handoff and classification guidance

Each bullet below is one distinct included issue; the coordinator assigns stable C IDs in source order and replaces PENDING in included and duplicate rows with the same group ID. Duplicate checker provenance and every affected location remain part of that group's evidence, even though a duplicate row is screened out. These are provisional relationship/domain recommendations for the mandatory source recheck, not adjudications.

- **F-XS-001 retained; F-ST1-001 duplicate:** EQ-5D day-5 significant interval/test versus secondary nonsignificance narrative; recommended S_W / statistical_results; union REPORT main pp.1,5,6,7,8; PLAN SAP p.14 corroborates no secondary multiplicity correction and does not create P_R.
- **F-XS-002 retained; F-ST1-012 duplicate:** Safety analysis membership; recommended P_R / protocol_report; union PLAN SAP p.13, REPORT main pp.3,8.
- **F-XS-003 retained; F-ST1-006 duplicate:** Opioid accumulation window; recommended P_R / protocol_report; union PLAN protocol pp.17,33,35, SAP p.11; REPORT main pp.4,5,6.
- **F-XS-004 retained; F-ST1-005 duplicate:** Edinburgh primary sensitivity absent; recommended P_R / protocol_report; union PLAN SAP p.15; REPORT main pp.5,6,7,9 and subgroup p.2, with absence confirmed over every REPORT page.
- **F-XS-005 retained; F-ST1-010 duplicate:** LOS hierarchy conflict; recommended S_W / report_internal_inconsistency; union REPORT main pp.4,7,8; PLAN protocol pp.16,18 and SAP p.10 corroborate tertiary classification rather than establishing an independently demonstrated prospective hierarchy change.
- **F-XS-006 retained; F-ST1-011 duplicate:** Readmission window; recommended P_R with All relationships P_R, S_W / protocol_report; union PLAN protocol pp.16,18, SAP pp.10,27; REPORT main pp.4,8; the protocol's discharge-relative versus operation-relative 30-day anchors are retained as context, without adding a separate peripheral plan-internal tertiary-anchor relationship.
- **F-XS-007 retained; F-ST1-002 duplicate:** Subgroup confidence-level ambiguity; recommended S_W / statistical_results; union REPORT subgroup p.2 and main p.5, PLAN SAP p.15 as corroborating context; absent model output prevents identifying an independently established implemented 95%-versus-planned 99% analysis change, and graphical versus numeric intervals remain a source-grounded alternative.
- **F-XS-008 retained:** Missing key-secondary measurement displays; recommended P_R / protocol_report; union PLAN protocol pp.16,17, SAP pp.20,21,22; REPORT main pp.1,5,6 and complete REPORT union for absence; retain GI-2 binary 96-hour result and the two PONV burden components in one missing-component pattern.
- **F-ST1-003 retained:** Primary logit versus log model; recommended P_R with All relationships P_R, P_P / protocol_report; PLAN protocol p.40, SAP pp.3,14,34; REPORT main pp.5,6; preserve the disclosed after-analysis amendment and uncertainty about contemporaneous intended link without asserting an undisclosed change.
- **F-ST1-004 retained:** Missing unadjusted primary ITT/per-protocol rows; recommended P_R / protocol_report; PLAN SAP p.20; REPORT main pp.5,6,7 and subgroup p.2, plus complete REPORT union for absence.
- **F-ST1-007 retained:** Specific discharge/readiness GLM versus general/reported Cox; recommended P_R with All relationships P_R, P_P / protocol_report; PLAN SAP pp.14,26,36; REPORT main pp.5,7; do not infer GLM family/link or assert that illustrative code was implemented.
- **F-ST1-008 retained:** ERAS primary-outcome subgroup adjustment; recommended P_P / plan_material; PLAN SAP pp.14,15,38; REPORT main p.5 and subgroup p.2 identify the relevant result but do not establish which appendix command was executed.
- **F-ST1-009 retained:** GI-2/GI-3 survival time origin; recommended P_P / plan_material; PLAN protocol p.16, SAP pp.9,33,34; REPORT main pp.6,8 identify/corroborate the affected key-secondary results but do not establish actual variable construction.

## Precision, scope and limitations

The EQ-5D printed upper-limit interval [-0.0035,-0.0025] excludes zero and printed P interval [0.035,0.045] remains below .05; route A category 1 is exempt from relative-discrepancy screening, and the no-benefit discussion language by itself is not the test conflict because the direction favors placebo. None of the remaining included issues compares two rounded copies of an estimate: 24/72-hour windows, 30/90-day boundaries, confidence levels, link/model classes, participant exposure requirements, covariate membership, outcome status, and time-origin definitions are exact design/inference definitions rather than noisy measurements. The safety observation does not claim that the numerical gap 25/558 alone exceeds 5%; it compares the categorical rule requiring IMP exposure against displayed inclusion of nonrecipients. Likewise, no equality between adjusted effects and crude summaries is asserted.

The comparison tiers were applied first: opioid, GI-2/GI-3, PONV and discharge/readiness are abstract-listed key secondary outcomes; primary model and primary-outcome subgroup adjustment are result-relevant statistical design; safety changes the defined analysis population; readmission labels change the quantity represented by 31/34 events rather than comparing peripheral tertiary copies; outcome hierarchy is always-register category 5. The GI time-origin and ERAS adjustment findings are specific conflicting statistical definitions for named reported analyses, not merely missing implementation details; their actual executed models and any quantitative impact remain unestablished.

No scientific source-coverage limitation prevents these screening decisions. Raw participant records, model output, implemented code, unpublished analyses, and contemporaneous complete earlier SAP versions are absent; the screen makes no claim to reconstruct those inputs. Source-grounded alternatives and all checker provenance must carry forward to recheck and human adjudication.

Counts: 20 findings screened; 13 included issues; 7 screened-out finding rows, all DUPLICATE_OF_INCLUDED; 0 screened-out rows under every other reason code; 0 numeric checker findings. All included issues remain Pending Human Adjudication after coordinator registration.

## Pass-2 decisions and consolidated totals

F-ST2-001 qualifies by Route A, category 5: five explicitly planned unadjusted analyses of abstract-listed key secondary outcomes are absent from the supplied REPORT union; these extend the same missing-unadjusted-analysis pattern in C007 without creating another stable ID.

F-ST2-002 qualifies by Route A, category 5: follow-up EQ visual-analogue summaries and postoperative day-1 weight are distinct planned key-secondary components without corresponding supplied REPORT output; these extend C010's missing-component pattern. Exact source confirmation, all additional locations and source-grounded alternatives are recorded in inclusion_screen_pass_2.md and carried into the ledger.

Consolidated totals: 22 finding rows screened; 15 INCLUDE rows; 7 SCREENED_OUT rows, all DUPLICATE_OF_INCLUDED; 13 stable candidate issues; zero under every other screened-out reason code. Pass 2 has two INCLUDE rows and zero screened-out rows; both map to existing IDs. Stable IDs were not renumbered. Added locations receive a fresh evidence recheck.
