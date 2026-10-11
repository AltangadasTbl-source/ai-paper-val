# Statistical relationship inventory — tables B, second-pass bounded shard

Mechanical source-linked split of first-pass statistics/parts/tables_b_plan.md. Scope: S5001–S5066, 66 inferential records, results eTables8–10/12. All first-pass evidence below is preserved unchanged. Fresh pass-2 agent adds its independent completion facts.

Fresh pass-2 runtime: root/stat2_tables_b; gpt-6.1-sol/high; FRESH_SPAWN. All 66 assigned records now have PASS_1_COMPLETE and PASS_2_COMPLETE. Exact source pp45–50/52, the complete current ledger, all screening decisions/justifications, and the complete source recheck were independently read. New findings: 0; C018 is reproduced and retained without re-emission. Checker details and exclusions: checkers/statistical_parts/pass2_tables_b.md. The original 120-record first-pass header below documents the parent artifact's historical scope; this current split contains only the 66 enumerated records.

# Statistical pass 1 inventory: tables B and plan methods

Fresh statistical shard: /root/stat1_tables_b_plan; model gpt-6.1-sol; reasoning high; FRESH_SPAWN. Scope: DOC-006 eTables8–13 physical pp45–53; DOC-003 entire protocol statistical-method and numerical decision-rule content; DOC-004 entire parent SAP statistical-method and numerical decision-rule content. Historical inferential statements are tracked as supplied PLAN facts, separately from SELECT2 outcomes. Main-report methods, DOC-005 and other result displays are separate assigned shards.

Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Mapping aids: support_parts/results_b_admin.md, protocol.md and trial_sap_a.md/trial_sap_b.md. Final authority: direct Poppler layout extraction for DOC-003/006 and source-matched images for scanned DOC-004. Direct transient command pdftotext -layout -f N -l N source.pdf -. Visually read DOC-006 pp45–53; protocol pp13,80,81 and parent SAP pp10,11,12,16,40; existing mapper visual records cover other plan pages. No new derivative, Python, web or prior conclusions used. Reused sources/assets preserved. CPU inspection; engine/version for reused renders recorded in evidence_asset_inventory.md, unrecorded legacy engine versions remain limitations.

120 records: S5001–S5120. Every displayed estimate/CI pair and interaction test in eTables8–10 is independent:24+6+10+6+10+6; eTable12 adds4. Plan methods/rules37; historical inferential pairs/tests17. A Bayesian threshold vector is one complete decision rule, with every row calculated independently within that record.

Shared table definitions:95%CI; ordinal ratio null1, binary RR null1, RD null0. eTable8 is within each received-treatment arm, profile versus concordant reference: concordant ASPECTS<6/core≥70mL, D1 ASPECTS<6/core<70, D2 ASPECTS6–10/core≥70. N163EVT/N156MM. eTable9 is randomized EVT-versus-MM treatment effect within CTP/MRI profile, eTable10 within composite-core profile. Interaction always compares treatment-effect modification across profiles. No individual effect-test P is supplied in those tables. N/A cells have no numerical estimate/test to enumerate.

Numeric context for matching: eTable8 FI:EVT32/163,MM10/156; concordant10/75 vs3/82; D1 21/76 vs7/63; D2 1/12 vs0/11. Ambulation62/163vs27/156;concordant18/75vs8/82;D1 41/76vs19/63;D2 3/12vs0/11. mRS5–6 75/163vs97/156;concordant42/75vs59/82;D1 25/76vs28/63;D2 8/12vs10/11. eTable9 FI MM/EVT concordant3/83vs10/74;D1 7/63vs21/76;D2 1/11vs0/12(N/A). Ambulation8/83vs18/74;19/63vs41/76;3/11vs0/12(N/A). mRS5–6 60/83vs41/74;28/63vs25/76;10/11vs8/12. eTable10 FI8/118vs18/112;2/28vs13/38;2/12vs0/14(N/A);ambulation19/118vs35/112;8/28vs24/38;4/12vs0/14(N/A);mRS5–6 74/118vs53/112;14/28vs13/38;11/12vs9/14. Cross-table FI/ambulation cell attribution is preserved for numeric/cross-source review, without assuming same analysis set.

Descriptive-only inspection: eTable11 MRI-follow-up groupsN101MM/24mTICI0–2a/79mTICI2b–3, medians(IQR)CTP/MRI95(56,135)/125(76,179)/68(37,142); composite63(22,102)/91(71,142)/45(16,90);CT69(31,122)/107(87,152)/60(24,110). Each median lies within ordered IQR, no inferential CI/test. eTable13 core minus follow-up:162−143=19,140−90=50,93−11=82mL; each exceeds≥10mL threshold. 'Significant' there explicitly means volume threshold, not an unstated P test. These displays have no omitted inferential estimate/test.

### S5001 — eTable8 ordinal D1 EVT

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.91 (0.50,1.65)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR0.91 inside[.50,1.65], including1; D1-versus-concordant within EVT differs from across-arm treatment effects. No own-effect P; C002 supplies the population context.

### S5002 — eTable8 ordinal D1 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.50 (0.94,2.40)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.50 inside[.94,2.40], including1; MM within-arm D1 contrast has no own-effect P. Interaction.20 tests effect modification rather than this coefficient.

### S5003 — eTable8 ordinal D2 EVT

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.01 (0.53,1.92)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR1.01 inside[.53,1.92], including1. D2 EVT ordinal effect can coexist with sparse favorable binary counts; C018 identifies separately conflicting cross-table attribution.

### S5004 — eTable8 ordinal D2 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.65 (0.43,0.99)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms OR.65 inside[.43,.99], excluding1 toward worse D2 MM outcome. Interaction.26 is not its own-effect P; MM6(6,6) supplies descriptive context, not an effect CI.

### S5005 — eTable8 mRS0–2 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.51 (0.16,1.56)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.51 inside[.16,1.56], including1. Adjusted profile effect need not equal crude(21/76)/(10/75)=2.072; no method reproducing these adjusted rows from crude counts is established.

### S5006 — eTable8 mRS0–2 D1 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.055 (−0.201,0.092)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD−.055 inside[−.201,.092], including0; its sign agrees with paired adjusted RR.51. Do not replace adjustment with observed28%−13%=15 percentage points.

### S5007 — eTable8 mRS0–2 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.26 (0.17,9.43)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.26 inside[.17,9.43], including1; positive adjusted D1 MM direction agrees with paired RD+.040. No matched own-effect test printed.

### S5008 — eTable8 mRS0–2 D1 MM RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.040 (−0.059,0.138)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.040 inside[−.059,.138], including0; same direction as RR1.26. Exact confidence/test reconstruction needs the absent fit and variance output.

### S5009 — eTable8 mRS0–2 D2 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.85 (0.12,5.79)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.85 inside[.12,5.79], including1; paired RD+.010 points oppositely. No shared fitted-risk pair, standardization or RD derivation is supplied, so a common-risk identity is not assumed.

### S5010 — eTable8 mRS0–2 D2 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.010 (−0.395,0.415)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RD+.010 inside[−.395,.415], including0; paired RR.85 reverses point direction. The observed count1/12 remains separate from an adjusted estimand; missing RR/RD mapping is recorded without a new finding.

### S5011 — eTable8 mRS0–3 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.86 (0.43,1.71)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR.86 inside[.43,1.71], including1; paired RD+.043 on p46 reverses point direction. A shared fitted-risk identity is absent and cannot be inferred from similar-model wording.

### S5012 — eTable8 mRS0–3 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.043 (−0.125,0.211)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.043 inside[−.125,.211], including0; opposite paired RR.86 direction is the same conditional mapping observation, consolidated in the pass-2 exclusion table.

### S5013 — eTable8 mRS0–3 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.24 (0.38,4.07)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 confirms RR1.24 inside[.38,4.07], including1; positive direction agrees with RD+.060. MM19/63 and8/82 are descriptive risks, not replacements for the adjusted estimate.

### S5014 — eTable8 mRS0–3 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.060 (−0.075,0.196)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.060 inside[−.075,.196], including0, agreeing in direction with RR1.24. Interaction.72 is a distinct contrast; no interval/test conflict is reproduced.

### S5015 — eTable8 mRS0–3 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.19 (0.43,3.28)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.19 inside[.43,3.28], including1; paired RD−.065 reverses point direction. Source supplies no common RR/RD risk pair or transformation, so conditional identity is not promoted.

### S5016 — eTable8 mRS0–3 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.065 (−0.421,0.291)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.065 inside[−.421,.291], including0. Paired RR1.19 has opposing direction; the same missing-model-mapping observation is consolidated once.

### S5017 — eTable8 mRS5–6 D1 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.92 (0.57,1.48)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.92 inside[.57,1.48], including1; lower adjusted D1 EVT adverse risk agrees with RD−.077. The25/76 crude proportion does not identify the adjusted risk.

### S5018 — eTable8 mRS5–6 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.077 (−0.244,0.091)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.077 inside[−.244,.091], including0 and agreeing with RR.92 direction. Effect-adjustment and own-effect variance remain unavailable.

### S5019 — eTable8 mRS5–6 D1 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.69 (0.49,0.97)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR.69 inside[.49,.97], excluding1; paired RD−.076 includes0. Distinct adjusted scales/confidence constructions do not supply a matched interval-versus-own-test conflict under the complete screening rationale.

### S5020 — eTable8 mRS5–6 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.076 (−0.248,0.096)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD−.076 inside[−.248,.096], including0. Paired RR.69 is directionally concordant but has different null inclusion; no shared confidence transform or own-effect P establishes a contradiction.

### S5021 — eTable8 mRS5–6 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.08 (0.69,1.68)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.08 inside[.69,1.68], including1; positive direction agrees with RD+.143. D2 EVT8/12 adverse and3/12 ambulation do not exceed12.

### S5022 — eTable8 mRS5–6 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.143 (−0.212,0.498)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.143 inside[−.212,.498], including0; agrees with RR1.08 direction. Exact regression reconstruction requires absent covariate rows/fitted probabilities.

### S5023 — eTable8 mRS5–6 D2 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.28 (1.01,1.63)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RR1.28 inside[1.01,1.63], excluding1 toward greater D2 MM adverse risk. Paired RD+.324 excludes0 consistently; interaction.02 is separately defined.

### S5024 — eTable8 mRS5–6 D2 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.324 (0.165,0.483)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 confirms RD+.324 inside[.165,.483], excluding0 in the same direction as RR1.28. eTable8 MM10/11 adverse plus0/11 favorable reconciles internally; C018 concerns competing eTables9/10 copies.

### S5025 — eTable8 interaction ordinal D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.20
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.20 as D1 ordinal treatment interaction. It is not the test for OR.91 or1.50; absent interaction covariance/coefficient prevents exact P reconstruction.

### S5026 — eTable8 interaction ordinal D2

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.26
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.26 as D2 ordinal treatment interaction, not the test for MM OR.65 excluding1. No interaction interval is printed to form its own interval/test conflict.

### S5027 — eTable8 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.78
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.78 as D1 functional-independence interaction, not an individual EVT/MM profile effect P. No test statistic or covariance supplies an exact numerical comparison.

### S5028 — eTable8 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.72
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p45 identifies P=.72 as D1 ambulation interaction. The different point directions in RR/RD do not establish an interaction coefficient; no own interaction CI is supplied.

### S5029 — eTable8 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.14
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.14 as D1 mRS5–6 interaction. An MM RR CI below1 beside.14 is a different contrast, so the apparent interval/P conflict is not reproduced.

### S5030 — eTable8 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.02
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p46 identifies P=.02 as D2 mRS5–6 interaction. It is significant at the main stated.05 level but no own interaction CI/statistic permits further numerical compatibility reproduction.

### S5031 — eTable9 ordinal concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.60 (1.18,2.18)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.60 inside[1.18,2.18], excluding1 toward better EVT ordinal outcome. Randomized within-profile comparison is distinct from eTable8 as-treated within-arm contrast, with C002 retained.

### S5032 — eTable9 ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.87 (1.28,2.74)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR1.87 inside[1.28,2.74], excluding1; P=.66 belongs to D1 interaction rather than this treatment contrast. Point containment/order and better-EVT direction reconcile.

### S5033 — eTable9 ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.46 (1.14,5.32)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms OR2.46 inside[1.14,5.32], excluding1. Better EVT ordinal outcome can involve shifts within poor categories despite printed zero favorable events; C018 retains the separate event-attribution issue.

### S5034 — eTable9 mRS0–2 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 4.62 (1.27,16.71)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR4.62 inside[1.27,16.71], excluding1 for EVT functional independence.10/74 versus3/83 is descriptive support; adjusted RR is not required to equal its crude ratio.

### S5035 — eTable9 mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.68 (1.25,5.76)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.68 inside[1.25,5.76], excluding1 for D1 EVT functional independence; interaction.56 tests between-profile modification, not this effect.

### S5036 — eTable9 mRS0–3 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.98 (1.44,6.17)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR2.98 inside[1.44,6.17], excluding1 for concordant-profile EVT ambulation. No own-effect P or standard error is supplied; count-based crude replacement is unsupported.

### S5037 — eTable9 mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.90 (1.29,2.78)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR1.90 inside[1.29,2.78], excluding1 for D1 EVT ambulation; interaction.38 is a separate contrast. Endpoint order and direction agree.

### S5038 — eTable9 mRS5–6 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.76 (0.61,0.95)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 confirms RR.76 inside[.61,.95], excluding1 toward lower EVT adverse risk. C018's D2 mismatch does not justify a numerical replacement for this concordant adjusted estimate.

### S5039 — eTable9 mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.72 (0.49,1.05)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.72 inside[.49,1.05], including1 for D1 adverse risk; interaction.83 is separately labeled. No same-effect statistical conclusion conflicts.

### S5040 — eTable9 mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.37,0.96)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 confirms RR.59 inside[.37,.96], excluding1 for D2 adverse risk; interaction.40 is not its own P. C018 recheck reproduces MM3+10>11 in this same profile but does not determine an amended fitted RR.

### S5041 — eTable9 interaction ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.66
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D1 interaction P=.66. Across-arm OR intervals cannot reconstruct it without pooled-model covariance; no explicit interaction statistic is supplied.

### S5042 — eTable9 interaction ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.18
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ordinal D2 interaction P=.18. The OR2.46 CI excluding1 tests a different effect, and C018 count issues do not supply an alternative interaction value.

### S5043 — eTable9 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.56
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies independence D1 interaction P=.56. It is not the test for RR2.68; no matched interaction interval, covariance or statistic is available.

### S5044 — eTable9 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p47 identifies ambulation D1 interaction P=.38. It is not the test for RR1.90; no new interval/test conflict is reproduced.

### S5045 — eTable9 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.83
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D1 adverse interaction P=.83; RR.72 is a within-D1 treatment effect. Both printed contrasts are distinct; covariance and exact test definition are absent.

### S5046 — eTable9 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.40
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p48 identifies D2 adverse interaction P=.40, not the test for RR.59 whose CI excludes1. C018 is preserved without substituting count-derived interaction inference.

### S5047 — eTable10 ordinal concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.65 (1.26,2.16)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.65 inside[1.26,2.16], excluding1 for concordant composite-profile EVT benefit. C003 addresses planned composite hierarchy; no additional estimate conflict is supplied.

### S5048 — eTable10 ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.80 (1.00,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR1.80 inside[1.00,3.22], containing printed null1. No own-effect P or significant narrative is paired with it, so this endpoint alone is not a category1 finding; interaction.61 is distinct.

### S5049 — eTable10 ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.66 (1.34,5.28)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms OR2.66 inside[1.34,5.28], excluding1. Composite D2 ordinal improvement remains possible within poor mRS categories; C018 concerns disjoint favorable/adverse counts, not this estimate's containment.

### S5050 — eTable10 mRS0–2 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.88 (1.34,6.20)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.88 inside[1.34,6.20], excluding1 for concordant composite-profile EVT independence; crude18/112 versus8/118 is not an adjusted-model reproduction.

### S5051 — eTable10 mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 3.71 (0.93,14.82)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR3.71 inside[.93,14.82], including1 for composite D1 independence. No significant own-effect statement is printed, and interaction.71 is another contrast.

### S5052 — eTable10 mRS0–3 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.21 (1.41,3.48)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR2.21 inside[1.41,3.48], excluding1 for concordant composite-profile ambulation. C003 hierarchy provenance remains separate from the numerically coherent interval.

### S5053 — eTable10 mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.83 (1.04,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR1.83 inside[1.04,3.22], excluding1 for composite D1 ambulation. P=.68 is the interaction and does not contradict this within-stratum interval.

### S5054 — eTable10 mRS5–6 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.75 (0.60,0.92)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 confirms RR.75 inside[.60,.92], excluding1 toward lower concordant-profile EVT adverse risk. Count comparison is descriptive; no own-effect P, statistic or standard error printed.

### S5055 — eTable10 mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.90 (0.52,1.56)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.90 inside[.52,1.56], including1 for composite D1 adverse risk. Interaction.92 is distinct; no matched test conflict.

### S5056 — eTable10 mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.39,0.88)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 confirms RR.59 inside[.39,.88], excluding1 for composite D2 adverse risk. Recheck C018 reproduces MM4+11>12 and2+11>12; this source count pattern is already screened and no fitted replacement is inferred.

### S5057 — eTable10 interaction ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.61
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D1 interaction P=.61; CI1.00–3.22 is for the within-D1 effect. No own interaction interval/statistic exists.

### S5058 — eTable10 interaction ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.13
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ordinal D2 interaction P=.13. CI1.34–5.28 is for the treatment effect, so the apparent interval/P mismatch uses different contrasts.

### S5059 — eTable10 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.71
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite independence D1 interaction P=.71. The RR3.71 interval is not an interaction interval; supplied summary values cannot reconstruct pooled covariance.

### S5060 — eTable10 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.68
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p49 identifies composite ambulation D1 interaction P=.68, distinct from RR1.83 whose interval excludes1. No same-analysis interval/test conflict is reproduced.

### S5061 — eTable10 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.92
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D1 adverse interaction P=.92. It is not the null test for RR.90; coefficient/covariance/test statistic remain absent.

### S5062 — eTable10 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p50 identifies composite D2 adverse interaction P=.38, distinct from RR.59 whose interval excludes1. C018 counts remain registered without inventing their inferential effect.

### S5063 — eTable12 CTP/MRI growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:102(61–167); mRS0–2 N46:45(32–88); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, medians102/45 inside ordered IQR61–167/32–88, and P<.001. The quantiles are IQRs, not effect CIs; ranks/statistic needed for exact P are absent.

### S5064 — eTable12 composite growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:77(31–127); mRS0–2 N46:23.5(11–48); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms290+46=336, composite medians77/23.5 inside IQR31–127/11–48, P<.001. Direction agrees with greater growth in dependence; no CI/test pairing is supplied.

### S5065 — eTable12 CTP/MRI growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:110.5(65.5–174.5); mRS0–3 N96:65.5(32.5–100.5); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, medians110.5/65.5 inside IQR65.5–174.5/32.5–100.5, P<.001. Overlap of IQRs does not contradict a between-group test.

### S5066 — eTable12 composite growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:85.5(36–144); mRS0–3 N96:31.5(10–67); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Direct p52 confirms240+96=336, composite medians85.5/31.5 inside IQR36–144/10–67, P<.001. Full ranked data/test output is needed for numerical P reconstruction; no unsupported normal approximation is used.


