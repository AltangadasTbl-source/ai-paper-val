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
- Pass 2: pending fresh independent stage.

### S5002 — eTable8 ordinal D1 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.50 (0.94,2.40)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5003 — eTable8 ordinal D2 EVT

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.01 (0.53,1.92)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5004 — eTable8 ordinal D2 MM

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 0.65 (0.43,0.99)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5005 — eTable8 mRS0–2 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.51 (0.16,1.56)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5006 — eTable8 mRS0–2 D1 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.055 (−0.201,0.092)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5007 — eTable8 mRS0–2 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.26 (0.17,9.43)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5008 — eTable8 mRS0–2 D1 MM RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.040 (−0.059,0.138)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5009 — eTable8 mRS0–2 D2 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.85 (0.12,5.79)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5010 — eTable8 mRS0–2 D2 EVT RD

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.010 (−0.395,0.415)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5011 — eTable8 mRS0–3 D1 EVT RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.86 (0.43,1.71)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5012 — eTable8 mRS0–3 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.043 (−0.125,0.211)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5013 — eTable8 mRS0–3 D1 MM RR

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.24 (0.38,4.07)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5014 — eTable8 mRS0–3 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.060 (−0.075,0.196)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5015 — eTable8 mRS0–3 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.19 (0.43,3.28)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5016 — eTable8 mRS0–3 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.065 (−0.421,0.291)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5017 — eTable8 mRS5–6 D1 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.92 (0.57,1.48)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5018 — eTable8 mRS5–6 D1 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.077 (−0.244,0.091)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5019 — eTable8 mRS5–6 D1 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.69 (0.49,0.97)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5020 — eTable8 mRS5–6 D1 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD −0.076 (−0.248,0.096)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5021 — eTable8 mRS5–6 D2 EVT RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.08 (0.69,1.68)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5022 — eTable8 mRS5–6 D2 EVT RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.143 (−0.212,0.498)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5023 — eTable8 mRS5–6 D2 MM RR

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.28 (1.01,1.63)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5024 — eTable8 mRS5–6 D2 MM RD

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRD 0.324 (0.165,0.483)
- Checks/calculation: Point contained; endpoints ordered; ratio direction uses null1 and RD uses null0. No same-contrast P is printed; interaction is separately tracked. Within-arm adjusted profile-versus-concordant contrast; do not equate with crude profile ratio/difference.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5025 — eTable8 interaction ordinal D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.20
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5026 — eTable8 interaction ordinal D2

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.26
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5027 — eTable8 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.78
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5028 — eTable8 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p45](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=45); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.72
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5029 — eTable8 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.14
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5030 — eTable8 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p46](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=46); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=.02
- Checks/calculation: Tests treatment×imaging-profile effect modification, rather than either individual within-arm estimate's null. The printed heading establishes distinct contrast; no interval supplied for the interaction.
- Definitions/limits: Interaction coefficient/covariance/test statistic not supplied; do not infer a Wald test from the arm-specific intervals.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5031 — eTable9 ordinal concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.60 (1.18,2.18)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5032 — eTable9 ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.87 (1.28,2.74)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5033 — eTable9 ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.46 (1.14,5.32)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5034 — eTable9 mRS0–2 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 4.62 (1.27,16.71)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5035 — eTable9 mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.68 (1.25,5.76)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5036 — eTable9 mRS0–3 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.98 (1.44,6.17)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5037 — eTable9 mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.90 (1.29,2.78)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5038 — eTable9 mRS5–6 concordant

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.76 (0.61,0.95)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5039 — eTable9 mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.72 (0.49,1.05)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5040 — eTable9 mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.37,0.96)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5041 — eTable9 interaction ordinal D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.66
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5042 — eTable9 interaction ordinal D2

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.18
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5043 — eTable9 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.56
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5044 — eTable9 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p47](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=47); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5045 — eTable9 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.83
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5046 — eTable9 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p48](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=48); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.40
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5047 — eTable10 ordinal concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.65 (1.26,2.16)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5048 — eTable10 ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 1.80 (1.00,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5049 — eTable10 ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aGenOR 2.66 (1.34,5.28)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5050 — eTable10 mRS0–2 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.88 (1.34,6.20)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5051 — eTable10 mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 3.71 (0.93,14.82)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5052 — eTable10 mRS0–3 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 2.21 (1.41,3.48)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5053 — eTable10 mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 1.83 (1.04,3.22)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5054 — eTable10 mRS5–6 concordant

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.75 (0.60,0.92)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5055 — eTable10 mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.90 (0.52,1.56)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5056 — eTable10 mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: aRR 0.59 (0.39,0.88)
- Checks/calculation: 95% CI contains estimate; endpoints ordered. Treatment effect is EVT versus MM within the named imaging stratum. Higher favorable-outcome ratios and lower mRS5–6 ratios denote EVT benefit. Interaction P is a separate between-profile treatment-effect test.
- Definitions/limits: No supplied test statistic or standard error; exact numerical P reproduction is not claimed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5057 — eTable10 interaction ordinal D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.61
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5058 — eTable10 interaction ordinal D2

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.13
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5059 — eTable10 interaction mRS0–2 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.71
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5060 — eTable10 interaction mRS0–3 D1

- Location/role: [DOC-006 physical p49](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=49); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.68
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5061 — eTable10 interaction mRS5–6 D1

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.92
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5062 — eTable10 interaction mRS5–6 D2

- Location/role: [DOC-006 physical p50](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=50); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Interaction P=0.38
- Checks/calculation: Interaction against concordant reference; no interaction coefficient/interval is given. This is not the P for the displayed within-stratum treatment effect.
- Definitions/limits: Sidedness/test degrees of freedom/covariance not printed for the interaction; exact P reconstruction unavailable.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5063 — eTable12 CTP/MRI growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:102(61–167); mRS0–2 N46:45(32–88); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5064 — eTable12 composite growth by independence

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS3–6 N290:77(31–127); mRS0–2 N46:23.5(11–48); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5065 — eTable12 CTP/MRI growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:110.5(65.5–174.5); mRS0–3 N96:65.5(32.5–100.5); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5066 — eTable12 composite growth by ambulation

- Location/role: [DOC-006 physical p52](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=52); REPORT. Context and any paired locations are stated below.
- Printed values, model, contrast and population: mRS4–6 N240:85.5(36–144); mRS0–3 N96:31.5(10–67); P<.001
- Checks/calculation: Two disjoint outcome groups each sum to336. All medians lie inside ordered IQRs; IQR is not a treatment-effect CI, so no interval/P contradiction follows. Direction: greater growth with worse function.
- Definitions/limits: Rank-sum data/test statistic and exact tested statistic are absent on the table page; summary quantiles do not reproduce a rank-sum P. No unsupported normal approximation used.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5067 — Discordance superiority rule

- Location/role: [DOC-003 physical p22](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=22); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Prior EVT good-outcome rates 48% vs32%; planned15 percentage-point margin; logistic OR95%CI for discordant imaging comparison (p51); diagram p71.
- Checks/calculation: 48−32=16 percentage points. No executed margin decision supplied. p51 repeats same profile in two word orders, while p22, second p51 paragraph and diagram clearly identify two opposite profiles. Excluded wording observation.
- Definitions/limits: Margin-to-OR decision mapping lacks executed result; no generic preference asserted.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5068 — Functional-independence hierarchy

- Location/role: [DOC-003 physical p37](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: p8/p37: second primary=mRS0–2 at90days. p50: secondary endpoint=mRS0–2 at90days. DOC004p13/p17: secondary.
- Checks/calculation: Same outcome/time receives primary and secondary status inside one dated protocol. F-ST1-502; PLAN/PLAN, P_P.
- Definitions/limits: Status discrepancy directly affects planned hierarchy.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5069 — Protocol primary analysis

- Location/role: [DOC-003 physical p45](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ITT90-day mRS; normal-approximation WMW/GLR; additional generalizedCMH stratified by randomization factors; age,NIHSS,time,core called continuous.
- Checks/calculation: Overall and adjusted rank-based comparisons are separately defined. Continuous stratification language lacks implementation but no numerical contradiction supplied.
- Definitions/limits: Stratum construction and tie/rank implementation missing; generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5070 — Adaptive population partition

- Location/role: [DOC-003 physical p45](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: G1A/B: ASPECTS3–5/core<50; G2A/B: ASPECTS6–10/core≥50; G3A/B: ASPECTS3–5/core≥50. A0–12h/B12–24h. Five cumulative subgroups; DOC004p9 matches.
- Checks/calculation: Imaging definitions partition eligible population; five cumulative alternatives plus overall match J6. No observed boundary-time duplicate enrollment supplied.
- Definitions/limits: Unstated handling of exactly12hours does not establish numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5071 — Projected distributions and standardized effect

- Location/role: [DOC-003 physical p46](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT mRS0–6:4,8,12,16,19,13,28%; MM:1,4,9,14,19,10,43%; effect.34; DOC004pp10–11 repeats.
- Checks/calculation: Both sums100%. Diagnostic half-tie WMW=.59375; sqrt(12)*(.59375−.5)=.324760. Difference from.34 less than5% before rounding; no finding.
- Definitions/limits: Standardized effect and tie-variance definition absent; diagnostic is not ASSISTant reproduction.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5072 — Sample size and power

- Location/role: [DOC-003 physical p46](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: FixedN376=188/arm; power90%, alpha5% in protocol; DOC004p11 one-sided.025. Additional184 gives adaptive560; interim200/380; adaptive91%power/effect.34/one-sided.025.
- Checks/calculation: Arithmetic reproduces. Diagnostic N=4*(1.959964+1.281552)^2/.34^2=363.579. Effect[.335,.345],power[.895,.905],alpha[.0245,.0255] yields approximateN349–379, overlapping376±.5; exactWMW/simulation not reconstructed.
- Definitions/limits: Protocol fixed alpha sidedness absent; two-sided.05/one-sided.025 share critical z.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5073 — First interim tree

- Location/role: [DOC-003 physical p47](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N200 completed90-day. Overall neither→continue; efficacy→stop; futility→select/test subgroup. Selected neither→restrict; efficacy→stop; futility→stop. DOC004pp9–10 repeats.
- Checks/calculation: All branches defined; maximum560, with smaller available analyzedN after enrichment.
- Definitions/limits: No realized interim statistic or relaxed-bound formula supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5074 — Second interim tree

- Location/role: [DOC-003 physical p47](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N380 completed90-day. Overall repeats first tree; selected neither→180 additional; efficacy→stop; futility→stop. DOC004p10 matches.
- Checks/calculation: 560−380=180; both accrual scenarios specified.
- Definitions/limits: No executed N380 decision supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5075 — Final tree

- Location/role: [DOC-003 physical p48](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=48); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolp48 overall560: failure→select/test subgroup; previously selected→test selected. DOC004p10 tests overall or selected and otherwise declares not superior.
- Checks/calculation: Later SAP does not restate overall-failure rescue branch. Actual trial stopped at300 (p12). Apparent final-branch observation excluded because no executed result supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED; preserve both dated descriptions.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5076 — Adaptive simulation scenario 0

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 0,0,0,0,0,0; mean0; adaptiveN426,power2.0%; fixed560,power2.5%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean0; null rates within2.5%; futility59.1%/N426 context coherent. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5077 — Adaptive simulation scenario 1

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .32,.32,.32,.32,.32,.32; mean.32; adaptive376,86.0%; fixed560,95.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.32; diagnostic normal fixed power≈.958; printed copies match. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5078 — Adaptive simulation scenario 2

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .3,.3,.3,.3,.3,.3; mean.3; adaptive393,81.1%; fixed560,93.3%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.3; diagnostic normal power≈.944 differs<5% from.933, not an exact simulation calculation. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5079 — Adaptive simulation scenario 3

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,0,0; mean.16; adaptive500,74.1%; fixed560,45.7%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4=.16. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5080 — Adaptive simulation scenario 4

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,−.1,−.1; mean.1; adaptive502,78.5%; fixed560:21.2%protocol/51.2%SAP; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4−.1*.6=.10. Same supplied input row; fixed powers differ beyond precision. F-ST1-503. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5081 — Adaptive simulation scenario 5

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.3,.3,0,−.1; mean.122; adaptive513,67.1%; fixed560,29.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.2+.3*.2−.1*.18=.122. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5082 — Adaptive simulation scenario 6

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,.5,0,0,0,0; mean.1; adaptive503,70.6%; fixed560,21.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.2=.10. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5083 — Adaptive simulation scenario 7

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,0,0,0,0,0; mean.07; adaptive503,60.5%; fixed560,12.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.14=.07. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5084 — Minimization algorithm

- Location/role: [DOC-003 physical p78](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=78); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Gk=ΣwfIk; variance reduction2ΣwfNk/(K−1)+constant; choose minimum. Protocol weights4,4,3,3,2,blank,1,1 for age,NIHSS,clot,time,core,mismatch,hemisphere,center. SAPp37:3,4,3,3,4,2,2,1 plusASPECTS3; p79/SAPp38 T2probabilities.9/.5/.1.
- Checks/calculation: Probability.9 favors lower imbalance, tie.5 and opposite.1. Later SAP refines factors and weights. No realized allocation discrepancy. Blank weight alone excluded.
- Definitions/limits: No allocation/raw-data audit; later values retained by version.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5085 — Primary missing-outcome rules

- Location/role: [DOC-003 physical p52](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=52); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocol90±15day nominalvisit; retrieveclinic/phone60–120days then ordinal-logisticMI. SAPp16 MAR,30imputations,Rubin pooling/tipping point; ITT352p14.
- Checks/calculation: Broader retrieval window is explicit; later SAP adds MI detail. No executed conflicting imputation calculation.
- Definitions/limits: Exact predictor list absent, generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5086 — Early-window safety

- Location/role: [DOC-003 physical p55](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=55); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolpp55–56 MM mortality increase>20%vsEVT→hold enrollment pendingDSMB.
- Checks/calculation: Absolute/relative scale unspecified but no executed safety decision supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED for missing20%scale alone.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5087 — Bayesian sICH ≤100cc

- Location/role: [DOC-003 physical p58](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=58); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; inclusive triggers24,44,63,82,101 throughN. PriorBeta(.35,.65); posterior Pr(p>.35)>.95; then Pr(EVT>MM+.10)>.95.
- Checks/calculation: PosteriorBeta(.35+s,.65+N−s). Exact incomplete-beta minima24,44,63,82,101; all reproduce.
- Definitions/limits: Step2 has no observed paired data; not assumed executed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5088 — Bayesian sICH >100cc

- Location/role: [DOC-003 physical p59](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=59); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; thenEVT>MM+.10 probability>.95.
- Checks/calculation: Exact incomplete-beta minima11,16,20,24,28,32,36,40,44 reproduce.
- Definitions/limits: Numerical integration of stated beta posterior; no normal approximation.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5089 — Bayesian sICH extracranialICA

- Location/role: [DOC-003 physical p60](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=60); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Same exact minima reproduce every printed row.
- Definitions/limits: Source-specific scope retained, not double counted as independent cause.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5090 — Bayesian mortality ≤100cc

- Location/role: [DOC-003 physical p61](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=61); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; lower limits26,49,71,92,113. Beta(.4,.6);Pr(p>.4)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Exact minima26,49,71,92,113 reproduce.
- Definitions/limits: No executed step2 comparison supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5091 — Bayesian mortality >100cc

- Location/role: [DOC-003 physical p62](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=62); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49. Beta(.4,.6);Pr(p>.4)>.95.
- Checks/calculation: Exact minima12,17,22,26,31,35,40,44,49. N60,s31 tail.9644096>.95;32vs31 differs3.125% and count half-unit intervals touch. Excluded display precision.
- Definitions/limits: Step2EVT>MM+.10 probability>.95; no executed data supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5092 — Bayesian mortality extracranialICA

- Location/role: [DOC-003 physical p63](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=63); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49; Beta(.4,.6),Pr(p>.4)>.95.
- Checks/calculation: Same minima12,17,22,26,31,35,40,44,49; same N60 observation consolidated in excluded row, relative discrepancy≤5%.
- Definitions/limits: Step2 conditional comparison supplied without observed event data.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5093 — Appendix direction and theta

- Location/role: [DOC-003 physical p81](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=81); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Y=MMmRS,X=EVTmRS;H0P(Y≤X)=.5;HAP(Y≤X)=.5+theta;theta=(z.975+z.9)/sqrt(3*560)=.0791. EfficacyZ≥2.604/final≥2.772;futilitytildeZ≤−1.897. DOC004pp39–40 repeats.
- Checks/calculation: Theta=.07908489 reproduces. Positive alternative favors lower MM score rather than EVT; F-ST1-504. Rank-sum orientation also needs clarification.
- Definitions/limits: Hypothesis orientation is explicit, independent of unknown ranking/tie convention; actual stoppingZ absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5094 — SAP300 stopping review

- Location/role: [DOC-004 physical p12](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=12); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: DOC004p12 planned200/380, requested300 review, no alteration/additional interim analyses; apply prespecified boundaries to30090-day cases and stop for efficacy;family-wise.05.
- Checks/calculation: Boundary application at300 differs from stated200/380 schedule, while claiming no alteration. F-ST1-505 asks which calibrated rule applies.
- Definitions/limits: Review and stop explicitly disclosed; no broad critique; .05vsone-sided.025 alone excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5095 — SAP ordinal merge

- Location/role: [DOC-004 physical p14](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Primary mRS5/6 mergedp14/p16 to avoid6→5 counting as success; anticipated distributionp10 has sevenlevels.
- Checks/calculation: Analysis definition and planning distribution are separate objects; no contradictory executed calculation supplied.
- Definitions/limits: Tie handling not assumed beyond source merger.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5096 — SAP WMW transformations

- Location/role: [DOC-004 physical p16](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: WMW superiority95%CI/P;ARD described as probability EVTbetter, formulaARD=2(WMW−.5);NNT=1/ARD;WMW generalized odds95%CI.
- Checks/calculation: Explicit transformation identifies net comparative quantity. Descriptive probability wording apparent issue excluded; no executedARD supplied.
- Definitions/limits: TERMINOLOGY_OR_WORDING; generalized-odds/tie/CI formula absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5097 — SAP functional independence

- Location/role: [DOC-004 physical p17](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–2; derive indicator from imputedmRS, Rubin pooling; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and imputation linkage coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5098 — SAP independent ambulation

- Location/role: [DOC-004 physical p17](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–3; same MI/Rubin; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and population/threshold coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5099 — SAP binary safety/early improvement

- Location/role: [DOC-004 physical p18](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=18); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: sICH24h, worsening≥4NIHSS24h, all-cause death90days, improvement≥8orNIHSS0–1 at24h. Binary logisticMI30, mortalityderivedmRS; modifiedPoissonRR95%CI/Ppp18–21.
- Checks/calculation: Common analysis rule checked separately against each endpoint definition and missingness link; all explicit. Missing early-improvement hypothesis predicate resolved by surrounding binary comparison.
- Definitions/limits: Covariate/pooled-test detail unreported; no numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5100 — SAP descriptive methods

- Location/role: [DOC-004 physical p19](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=19); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Complications cumulativecounts/proportions; reperfusionmTICI≥2bEVTonly; neither hypothesistest norimputation. Discharge sixcategory proportions/noimputationp20.
- Checks/calculation: Descriptive analysis intentionally distinguished from tested binary outcomes; unnamed discharge test has no executedP supplied.
- Definitions/limits: Generic absent discharge test excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5101 — SAP NeuroQoL

- Location/role: [DOC-004 physical p21](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=21); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-dayquality-of-life distribution; median(IQR); median-regression difference95%CI/P; noimputation.
- Checks/calculation: Median contrast compatible with quantile-regression output.
- Definitions/limits: No executed estimate/CI here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5102 — SAP sensitivities/subgroups

- Location/role: [DOC-004 physical p23](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: As-treatedreceived treatment; per-protocol allcriteria/core-lab imaging/assignedtreatment. RepeatWMW. Subgroupsage70,NIHSS20,ICA/M1,time12/6h,core70/100/150,ASPECTS6–10/3–5/0–2,mismatch1.8/15and1.2/10,restrictedsets,hemisphere,US/nonUSpp21–23.
- Checks/calculation: Populations clearly separate; nested thresholds are distinct analyses. Secondary multiplicity not adjustedp14;95%CI. Illustrative forest entries1.00(.50,2.00) are placeholders.
- Definitions/limits: No comparison of illustrative values with trial estimates.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5103 — SAP exploratory imaging

- Location/role: [DOC-004 physical p23](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Section12 exploratory/tertiary may defer; core/ASPECTS ceilings,joint modification,mismatch, compositeunion or larger when union infeasible, age/severity/time/hemisphere/transferetc.
- Checks/calculation: Context identifies same optional tertiary scope; no executed result here. DOC005 secondary-specific SAP separately assigned.
- Definitions/limits: No raw-data/model-preference audit.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5104 — Historical SELECT functional independence

- Location/role: [DOC-003 physical p13](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT30%vsMM13%; adjustedOR2.92,95%CI1.00–7.91,P=.041
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501. No Wald method assumed.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5105 — Historical SELECT ordinal effect

- Location/role: [DOC-003 physical p13](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: AdjustedOR2.01,95%CI1.00–4.03,P=.049
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5106 — Historical SELECT sICH

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT7%vsMM13%,P=.26
- Checks/calculation: Nonsignificant conclusion agrees withP. No matched effectCI; exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5107 — Historical SELECT mortality

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT29%vsMM42%,P=.17
- Checks/calculation: Nonsignificant conclusion agrees withP. Exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5108 — Historical retrospective good outcome

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ASPECTS<7:37%vs≥7:47%,P=.8
- Checks/calculation: Printed nonsignificant conclusion agrees withP; sample size/test absent; no assumed reproduction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5109 — Historical retrospective sICH

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 9%vs9%,P=1.0
- Checks/calculation: Identical rounded percentages and nonsignificantP; no contradiction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5110 — Historical retrospective mortality

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 20%vs22%,P=.8
- Checks/calculation: Small displayed difference with nonsignificantP; no supplied contradictoryCI.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5111 — Historical matched-cohort ordinal effect

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: OR2.56,95%CI2.50–8.47,P=.04
- Checks/calculation: Point contained; endpoints ordered; interval excludesnull1/P<.05 agree. Log-Wald symmetry diagnostic alone does not establish conflicting stated test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5112 — Historical matched-cohort independence

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT25%vsMM0%,P=.04
- Checks/calculation: Reported significance matchesP; sample sizes/test absent; no CI supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5113 — Historical matched-cohort infarct volume

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Mean(SD)EVT87(77)vsMM242(120)mL,P<.001
- Checks/calculation: Direction and significantP consistent; sample size missing, no fabricated t-test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5114 — Historical matched-cohort PH2

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P>.99; stated no significant difference
- Checks/calculation: Conclusion/P agree; no point/interval supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5115 — Historical matched-cohort hemicraniectomy

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.10; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5116 — Historical matched-cohort mortality

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.75; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5117 — Historical meta-analysis sICH

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT0%vsMM12%,P=.24
- Checks/calculation: Stated no significant difference agrees; no sample/test inputs supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5118 — Historical SELECT early-window sICH

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 8/173(5%)vs3/18(17%),P=.072; narrative safety outcomes significantly increased
- Checks/calculation: The sICH P=.072 is not significant at.05 while paragraph explicitly includes it among safety outcomes that significantly increased. Exact test unspecified; see F-ST1-506.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5119 — Historical SELECT early-window worsening

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 14/173(8%)vs5/18(28%),P=.023
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

### S5120 — Historical SELECT early-window mortality

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 15/173(9%)vs7/18(39%),P=.001
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: pending fresh independent stage.

## Complete Bayesian calculation facts

Posterior given s events/N is Beta(a+s,b+N−s). Tail=1−I_t(a+s,b+N−s), evaluated with Lanczos log-gamma and a convergent incomplete-beta continued fraction in JavaScript. This is deterministic integration of source-specified priors and event counts. No Python, external package or normal approximation used. At each N the minimalinteger s is the first with tail>.95; every predecessor checked.

| Prior/threshold | N | Minimum s | Tail at s | Tail at s−1 |
|---|---:|---:|---:|---:|
| Beta(0.35,0.65);t=0.35 | 20 | 11 | 0.961767775 | 0.907160210 |
| Beta(0.35,0.65);t=0.35 | 30 | 16 | 0.977665716 | 0.949620772 |
| Beta(0.35,0.65);t=0.35 | 40 | 20 | 0.971728919 | 0.943879068 |
| Beta(0.35,0.65);t=0.35 | 50 | 24 | 0.968187856 | 0.941671152 |
| Beta(0.35,0.65);t=0.35 | 60 | 28 | 0.966289545 | 0.941479639 |
| Beta(0.35,0.65);t=0.35 | 70 | 32 | 0.965500009 | 0.942468950 |
| Beta(0.35,0.65);t=0.35 | 80 | 36 | 0.965458559 | 0.944154658 |
| Beta(0.35,0.65);t=0.35 | 90 | 40 | 0.965921547 | 0.946243703 |
| Beta(0.35,0.65);t=0.35 | 100 | 44 | 0.966722456 | 0.948552978 |
| Beta(0.35,0.65);t=0.35 | 150 | 63 | 0.960473449 | 0.943979008 |
| Beta(0.35,0.65);t=0.35 | 200 | 82 | 0.959361444 | 0.945000174 |
| Beta(0.35,0.65);t=0.35 | 250 | 101 | 0.960602998 | 0.948205346 |
| Beta(0.4,0.60);t=0.4 | 20 | 12 | 0.961099626 | 0.906027079 |
| Beta(0.4,0.60);t=0.4 | 30 | 17 | 0.964812378 | 0.925698692 |
| Beta(0.4,0.60);t=0.4 | 40 | 22 | 0.970415675 | 0.941869624 |
| Beta(0.4,0.60);t=0.4 | 50 | 26 | 0.954554044 | 0.920363713 |
| Beta(0.4,0.60);t=0.4 | 60 | 31 | 0.964409556 | 0.938913247 |
| Beta(0.4,0.60);t=0.4 | 70 | 35 | 0.952790714 | 0.924044283 |
| Beta(0.4,0.60);t=0.4 | 80 | 40 | 0.963305404 | 0.941342910 |
| Beta(0.4,0.60);t=0.4 | 90 | 44 | 0.954441732 | 0.930280177 |
| Beta(0.4,0.60);t=0.4 | 100 | 49 | 0.964452433 | 0.945653062 |
| Beta(0.4,0.60);t=0.4 | 150 | 71 | 0.964576872 | 0.949726349 |
| Beta(0.4,0.60);t=0.4 | 200 | 92 | 0.956349011 | 0.941476112 |
| Beta(0.4,0.60);t=0.4 | 250 | 113 | 0.951428952 | 0.937144130 |

No scientific scope gaps. Exact P/CI reproductions unavailable where named sidedness/test/variance/covariance or raw ranks are absent; these are recorded per relationship. Every assigned statistical statement was checked, with candidate inclusion independently pending screen.

