# Statistical Consistency Review — Pass 1

**Status:** COMPLETE. This is an independent first pass over the complete canonical statistical inventory (`S001`–`S038`). It uses only fresh direct-source PDF pages, their fresh OCR, and the freshly rendered page images listed below. No legacy audit derivative, web source, candidate ledger, or adjudication was used.

## Method and evidence boundary

- **Exact sources checked:** DOC001 `jama_driver_2018_oi_180054.pdf` pp. 1–10; DOC002 `joi180054supp1_prod.pdf` pp. 9, 11, 19–21; DOC003 `joi180054supp2_prod.pdf` pp. 2–6 and 10.
- **Fresh evidence assets checked:** `preprocessing/ocr_text/DOC001-page-001.txt`, `003.txt` through `010.txt`; `DOC002-page-009.txt`, `011.txt`, `019.txt` through `021.txt`; `DOC003-page-002.txt` through `006.txt` and `010.txt`. Rendered images `preprocessing/rendered_pages/DOC001-page-007.png`, `DOC003-page-002.png`, and `DOC003-page-004.png` were visually checked where table/figure layout was material.
- **Checks applied where defined:** endpoint order; point-estimate containment; effect sign/direction and group ordering; displayed numerator/denominator arithmetic; label, unit, and population matching; direct matched-result repetitions; and interval/P/test/HR compatibility only under supplied definitions. The main article specifies 95% CIs, chi-square tests for binary outcomes, Wilcoxon rank-sum tests and Hodges-Lehmann differences for continuous outcomes, and log-rank/Cox analyses for duration (DOC001 p. 4). It does **not** state the confidence-interval construction or all variance details needed to force equality between every CI and every P value, especially in sparse rows; such checks are marked limited rather than inferred.
- **Display-zero rule:** No coherent `P = 0`, `P = .000`, or equivalent display zero was present. Printed `P < .001` values were treated as bounded displays, not reconstructed and not made candidates.

## Relationship records

### S001 — PASS_1_COMPLETE

DOC001 p. 3 and DOC002 p. 19 both state 374 difficult-airway patients, 80% power, a 9-percentage-point contrast (95% versus 86%), and two-sided alpha .05. DOC001 reports that stopping occurred after more than 374 such patients and reports 380; 380 satisfies the stated `>374` rule. No incompatible result statistic is supplied or inferred. **No proposed candidate signal.**

### S002 — PASS_1_COMPLETE

DOC001 p. 4 explicitly assigns difference-in-proportion/95% CI plus chi-square to binary outcomes, Hodges-Lehmann difference/95% CI plus Wilcoxon rank-sum to continuous outcomes, and log-rank/Cox HR to duration. The relationship is a method-definition record; it supports the compatible checks below. No internal conflict in the stated rules was found. **No proposed candidate signal.**

### S003 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 preoxygenation rows have ordered difference intervals containing their displayed differences (`−3`, `0`, `2`, `−2`, `3`). Their P values (.31, .93, .27, .32, .13) are all above .05 and their rounded intervals include zero; raw proportions reproduce the displayed directions subject to percentage rounding. **No proposed candidate signal.**

### S004 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 sedative rows have ordered intervals containing `−2`, `−1`, and `0`; P values (.37, .54, .99) are directionally compatible with zero-containing intervals. The no-sedative footnote supplies the nonexclusive sedation context and does not alter the tested rows. **No proposed candidate signal.**

### S005 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 neuromuscular-blockade rows have ordered intervals containing `−2`, `−5`, and `2`; P values (.23, .19, .54) are compatible with zero-containing intervals and raw percentage directions. **No proposed candidate signal.**

### S006 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 position rows have ordered intervals containing `−7`, `5`, and `2`. The rounded zero endpoints with P values .06 and .11 are not discordant: endpoint rounding and an unspecified CI construction preclude a stricter equality test. The `.42` row also contains zero. **No proposed candidate signal.**

### S007 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 start-saturation rows display median difference `0 (0 to 0)`, P=.60, and binary differences `−2 (−6 to 2)`, P=.36 and `1 (−1 to 4)`, P=.32. Every interval is ordered and contains its estimate; the two binary directions reproduce from the available-data fractions. **No proposed candidate signal.**

### S008 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 reports apneic nasal-cannula use `58%` versus `60%`, difference `−2 (−9 to 5)`, P=.51. The interval is ordered, contains the estimate and zero, and agrees with the displayed group direction. **No proposed candidate signal.**

### S009 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 reports senior `−5 (−10 to 0)`, junior `5 (0 to 10)`, and faculty `1 (−1 to 3)` percentage-point differences. All endpoints are ordered and contain the estimates. P=.03 for the first two and .42 for faculty is compatible with rounded boundary values; no CI/P identity can be imposed because CI construction is not specified. **No proposed candidate signal.**

### S010 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 laryngoscope rows have ordered intervals containing `−2`, `1`, and `1`, with directions matching the printed counts. P=.10, .38, and .10 do not create an internally defined CI/P contradiction. **No proposed candidate signal.**

### S011 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 video-screen rows use the stated available-data denominators. The raw directions agree with `9 (2 to 16)`, `−4 (−9 to 2)`, and `−6 (−12 to 0)`; all intervals are ordered and contain the estimates. P=.02, .25, and .04 are directionally compatible with these rounded intervals. **No proposed candidate signal.**

### S012 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 Cormack-Lehane rows use their stated view-available denominators and have ordered intervals containing `−3`, `3`, `1`, and `−1`. Count-derived directions and P values (.39, .39, .66, .44) are compatible with intervals that include zero. **No proposed candidate signal.**

### S013 — PASS_1_COMPLETE

DOC001 p. 6 Table 2 first-device rows match Figure 1 allocation/adherence counts. Differences `91 (88 to 94)`, `−91 (−94 to −88)`, and `0 (−2 to 1)` have ordered bounds, contain their estimates, and agree with group ordering. `P < .001` is a finite bound display, not a display-zero issue. **No proposed candidate signal.**

### S014 — PASS_1_COMPLETE

DOC001 pp. 1, 5, and 7 consistently report difficult-airway primary success as 191/198 (96%) versus 150/182 (82%), difference `14 (8 to 20)`, P<.001. DOC003 p. 2 retains counts and percentages but explicitly recalculates inferential columns for physician clustering: `14 (7 to 21)`, P<.001, interaction .35 versus the main table's .36. Each interval is ordered/contains 14, the event directions match, and the supplied clustered-analysis explanation accounts for distinct intervals/P values. **No proposed candidate signal.**

### S015 — PASS_1_COMPLETE

DOC001 p. 7 reports 156/191 versus 123/177, difference `12 (3 to 21)`, P=.006; DOC003 p. 2 retains the event data but identifies clustered recalculation `12 (2 to 22)`, P=.015. Both intervals contain 12 and exclude zero, directions agree, and DOC003 p. 3 expressly explains the recalculated inferential columns. **No proposed candidate signal.**

### S016 — PASS_1_COMPLETE

DOC001 p. 7 reports difficult-airway duration median difference `−1 (−6 to 3)` seconds, P=.50, versus DOC003 p. 2 clustered `−1 (−6 to 3)`, P=.31. Bounds are ordered and contain −1 and zero. The P values arise from declared clustered versus ordinary analyses; exact recalculation is not possible because physician-level data and variance details are not supplied. **No proposed candidate signal.**

### S017 — PASS_1_COMPLETE

DOC001 pp. 1, 5, and 7 report all-patient success 373/381 versus 328/376, difference `11 (7 to 14)`, P<.001. DOC003 p. 2 gives the declared clustered version `11 (6 to 15)`, P<.001. Point estimates, group direction, and population N=757 match; both intervals are ordered and contain 11. **No proposed candidate signal.**

### S018 — PASS_1_COMPLETE

DOC001 p. 7 reports 317/371 versus 282/366, difference `8 (3 to 14)`, P=.003; DOC003 p. 2 supplies clustered `8 (2 to 15)`, P=.02. The waveform-available denominators are explicitly outcome-specific, both intervals are ordered/contain 8, and the documented clustering recalculation explains nonidentical inferential values. **No proposed candidate signal.**

### S019 — PASS_1_COMPLETE

DOC001 p. 7 Table 3 prints all-patient duration as 38 versus 36 seconds, difference `1 (4 to −1)`, P=.24. Fresh OCR and the visually checked rendered page both preserve that endpoint order. The point estimate lies numerically between −1 and 4 only after reordering; DOC003 p. 2 prints the same point difference with ordered clustered interval `1 (−1 to 4)`, P=.95. The ordering defect is recorded as **P1-SIGNAL-001** below. The P-value difference itself is not a separate signal because DOC003 p. 3 declares clustered recalculation.

### S020 — PASS_1_COMPLETE

DOC001 p. 7 selected difficult-characteristic subgroups show `13 (3 to 23)`, P=.01; `22 (9 to 36)`, P=.001; and `21 (10 to 33)`, P=.001. Every interval is ordered and contains the effect, and each effect direction matches its reported event proportions. Interaction P values (.31, .25, .63) answer distinct effect-modification tests and do not conflict with within-subgroup P values. **No proposed candidate signal.**

### S021 — PASS_1_COMPLETE

DOC001 p. 7 reports no-difficult-characteristic success as 182/183 versus 178/194, difference `8 (4 to 12)`, P<.001, interaction .36. The complement population totals 377, the interval is ordered and contains 8, and the direction agrees with counts. **No proposed candidate signal.**

### S022 — PASS_1_COMPLETE

DOC001 p. 7 reports C-MAC subgroup success 356/362 versus 321/366, difference `11 (7 to 14)`, P<.001, interaction .46. The interval is ordered/contains 11, its sign agrees with counts, and the interaction test is distinct from the within-subgroup comparison. **No proposed candidate signal.**

### S023 — PASS_1_COMPLETE

DOC001 p. 7 Cormack-Lehane subgroup effects (`3 [0 to 5]`, `31 [19 to 44]`, `48 [27 to 71]`, `60 [17 to 100]`) are ordered, contain their estimates, and match the raw group directions. The grade-4 row pairs a difference CI excluding zero with P=.09. This is a **diagnostic limitation, not a proposed candidate**: the article supplies chi-square as the binary test but does not state the difference-CI construction or whether it is the same inferential procedure; sparse 3/3 versus 2/5 data make mechanical equality inappropriate. Human verification, if desired, is the CI method and its relation to the displayed P value. Interaction P values test a different question. 

### S024 — PASS_1_COMPLETE

DOC001 p. 7 reports actual-first-device success 392/402 versus 309/355, difference `10 (7 to 14)`, P<.001. Denominators sum to 757 and the footnote supplies the randomized classification for withdrawn-before-passage cases. The interval is ordered/contains 10 and matches the event direction. **No proposed candidate signal.**

### S025 — PASS_1_COMPLETE

DOC001 p. 7 reports successful-first-attempt duration 38 versus 34 seconds, difference `4 (2 to 7)`, P<.001, interaction .03. The interval is ordered, contains 4, excludes zero, and matches the medians' direction. The post hoc status is printed but is not an internal quantitative inconsistency. **No proposed candidate signal.**

### S026 — PASS_1_COMPLETE

DOC001 pp. 5 and 8 consistently report difficult-airway log-rank P=.02 and Cox HR 1.29 (95% CI 1.04–1.60), Bougie versus ETT+stylet reference. The ratio estimate is between ordered bounds and above 1, matching the stated direction and P<.05. DOC001 pp. 8 and 10 expressly state that proportional hazards was not upheld; this limits interpretation but is a disclosed qualification, not a contradictory report. **No proposed candidate signal.**

### S027 — PASS_1_COMPLETE

DOC001 p. 9 Table 5 composite/hypoxemia/pneumothorax rows have ordered intervals containing the displayed differences (`1`, `−1`, `0`, `−1`) and their raw fractions give the same directions subject to rounding. P=.83, .67, .99, and .31 are compatible with zero-containing intervals. **No proposed candidate signal.**

### S028 — PASS_1_COMPLETE

DOC001 p. 9 Table 5 other-complication rows have ordered intervals containing `1`, `1`, `0`, `0`, and `−1`; signs agree with the stated counts. P=.21, .32, .99, .99, and .08 are compatible with their zero-containing or boundary-rounding intervals. **No proposed candidate signal.**

### S029 — PASS_1_COMPLETE

DOC002 p. 11 states the protocol's two-arm design and whether first-pass success differs by more than 9% absolute. The planned contrast is consistent with DOC002 p. 19's 95% versus 86% sample-size assumptions and DOC001 p. 3's corresponding planning statement. This is a goal/design definition, not a result whose inferential equality can be tested. **No proposed candidate signal.**

### S030 — PASS_1_COMPLETE

DOC002 p. 19 specifies categorical displays, continuous summaries, Kaplan-Meier percentiles with two-sided 95% CIs, and two-sided .05 testing for primary/key-secondary outcomes. It is internally coherent. It does not specify all confidence-interval/test implementations needed to recompute later reported P values. **No proposed candidate signal.**

### S031 — PASS_1_COMPLETE

DOC002 p. 19 specifies 374 difficult-airway patients (187/group), 80% power, 95% versus 86%, and a 9-point difference. DOC001 p. 3 reports the same planning inputs and actual difficult-airway N=380. The planned enrollment cap/extension wording differs from the observed close at 757 total but is not a direct result contradiction; the main article supplies the actual stopping rule for `>374` difficult-airway patients. **No proposed candidate signal.**

### S032 — PASS_1_COMPLETE

DOC002 p. 20 defines planned chi-square primary comparisons and appropriate CIs for categorical/continuous outcomes. Its time-to-intubation endpoint must be read with DOC002 p. 9: start of attempt to ETT-cuff inflation. DOC001 pp. 3 and 7 and DOC003 p. 3 instead define the published duration as blade entry to blade removal. The endpoint-label discrepancy is recorded as **P1-SIGNAL-002** below; no unreported model mapping is assumed.

### S033 — PASS_1_COMPLETE

DOC002 p. 21 states an interim analysis after 500 enrolled patients, only for primary-outcome futility, with stated 1,000-patient sensitivity assumptions. The inferential test and operational allowance around exactly 500 are not supplied. DOC003 p. 6 reports the observed interim at 507; this direct timing difference is **P1-SIGNAL-004** below. **No additional proposed candidate signal.**

### S034 — PASS_1_COMPLETE

DOC003 pp. 2–3 eTable 1 reports physician-clustered primary difficult-airway analysis: identical counts to DOC001, difference `14 (7 to 21)`, P<.001, interaction .35, and ICC <.001 (95% CI <.001 to .03) with upper CI bound used. The effect is contained in ordered bounds and retains group direction. The table explicitly says it recalculates difference/P/interaction for clustering; it therefore does not contradict the ordinary main analysis. **No proposed candidate signal.**

### S035 — PASS_1_COMPLETE

DOC003 pp. 2–3 reports clustered difficult-airway secondaries: success without hypoxemia `12 (2 to 22)`, P=.015 and duration `−1 (−6 to 3)`, P=.31. Intervals are ordered and contain their estimates; counts/medians match DOC001. DOC003's declared clustering recalculation accounts for difference from the unclustered Table 3 inferential displays. **No proposed candidate signal.**

### S036 — PASS_1_COMPLETE

DOC003 pp. 2–3 reports clustered all-patient success `11 (6 to 15)`, P<.001; success without hypoxemia `8 (2 to 15)`, P=.02; and duration `1 (−1 to 4)`, P=.95. Every interval is ordered and contains the point estimate. Counts/medians retain DOC001's values and DOC003 explicitly identifies its recalculation basis. **No proposed candidate signal.**

### S037 — PASS_1_COMPLETE

DOC003 p. 4 eFigure 1 reports all-patient log-rank P=.12 and HR 1.12 (95% CI .97–1.30), Bougie versus ETT+stylet reference. The HR lies within ordered bounds, bounds include 1, and direction/P are consistent. The nonproportional-hazards caveat is printed in the same figure and main narrative; it is a disclosed limitation, not an internal contradiction. **No proposed candidate signal.**

### S038 — PASS_1_COMPLETE

DOC003 p. 6 reports interim results after 507 enrolled: 250/257 (97%) versus 213/250 (85%); denominators sum to 507 and percentages round correctly. It states the protocol futility assumptions and that the trial was not stopped. DOC002 p. 21 says the interim would occur after 500 enrolled, creating **P1-SIGNAL-004** below. No P value or exact futility statistic is supplied, so no unreported calculation was attempted.

## Proposed candidate signals for later registration

These are proposed quality-control signals only. They have no stable `C` ID, severity, disposition, validity judgment, correction, or adjudication.

### P1-SIGNAL-001 — Reversed interval endpoint order in all-patient first-attempt duration

- **Category:** Statistical reporting inconsistency.
- **Exact source locations:** DOC001 [PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7), Table 3; fresh OCR `preprocessing/ocr_text/DOC001-page-007.txt`; visually checked `preprocessing/rendered_pages/DOC001-page-007.png`. Comparator: DOC003 [PDF p. 2](../../../joi180054supp2_prod.pdf#page=2), eTable 1; fresh OCR `preprocessing/ocr_text/DOC003-page-002.txt`.
- **Direct observation:** The main Table 3 prints `1 (4 to −1)` seconds for the all-patient median duration difference. The main table's own column heading calls this a 95% CI. The clustered eTable, for the same displayed medians and point difference, prints `1 (−1 to 4)` seconds.
- **Reproducible rule:** A printed confidence interval has a lower endpoint no greater than its upper endpoint. `4 > −1`; reordering gives `−1 to 4`, which contains the printed estimate 1.
- **Inference and alternatives:** The endpoint-order defect is directly observable. The eTable is a separately clustered analysis, so it is corroborative for the likely intended numerical order rather than proof that a particular editorial correction is required. A typesetting transposition is one possible explanation; the package does not establish it.
- **Human question:** Does the source record or production file confirm that the DOC001 interval was intended to be `−1 to 4` seconds, and if not, what interval endpoints were actually calculated for the ordinary (nonclustered) analysis?

### P1-SIGNAL-002 — Published duration endpoint differs from the protocol's planned time-to-intubation endpoint

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC002 [PDF p. 9](../../../joi180054supp1_prod.pdf#page=9), §2.2; fresh OCR `preprocessing/ocr_text/DOC002-page-009.txt`. DOC001 [PDF p. 3](../../../jama_driver_2018_oi_180054.pdf#page=3), Trial Outcomes, and [PDF p. 7](../../../jama_driver_2018_oi_180054.pdf#page=7), Table 3 footnote; fresh OCR `DOC001-page-003.txt` and `DOC001-page-007.txt`. DOC003 [PDF p. 3](../../../joi180054supp2_prod.pdf#page=3), eTable footnote; fresh OCR `DOC003-page-003.txt`.
- **Direct observation:** The protocol defines first-attempt “Time to intubation” from attempt beginning to inflation of the ETT cuff in the trachea. The main article and eTable define published first-attempt duration from laryngoscope-blade entry into the mouth to blade removal from the mouth.
- **Reproducible rule:** These start/end events are textually different and can yield different measured durations; a result retained under the same first-attempt duration/time-to-intubation outcome family requires an explicit endpoint mapping or amendment record to establish identity.
- **Inference and alternatives:** The difference in definitions is direct. It may reflect an intentional post-protocol amendment, two distinct measures, or a terminology/recording change; no supplied amendment or mapping resolves it. This review does not infer that the numeric Table 3 values are wrong.
- **Human question:** Which endpoint was analyzed for the published duration results, and is there a dated amendment or analysis record explaining the change from ETT-cuff inflation to blade removal?

### P1-SIGNAL-003 — First-attempt boundary differs between protocol and supplied collection form/article definitions

- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC002 [PDF p. 9](../../../joi180054supp1_prod.pdf#page=9), §2.1; fresh OCR `preprocessing/ocr_text/DOC002-page-009.txt`. DOC003 [PDF p. 10](../../../joi180054supp2_prod.pdf#page=10), Attempt #1 form; fresh OCR `preprocessing/ocr_text/DOC003-page-010.txt`. DOC001 [PDF p. 3](../../../jama_driver_2018_oi_180054.pdf#page=3), Trial Outcomes; fresh OCR `preprocessing/ocr_text/DOC001-page-003.txt`.
- **Direct observation:** The protocol ends an attempt on a switch to another tube device even if the blade remains in the mouth. The supplied form ends an attempt only when the blade is removed and separately records a switch. The article defines primary success by placement with the first device passed during the first laryngoscope insertion.
- **Reproducible rule:** These sources apply different explicit boundaries to the same labeled first-attempt construct. A tube-device switch without blade removal is classified at different temporal boundaries by the protocol and form; the article's first-device-success wording may resolve outcome status but does not state the data-form reconciliation rule.
- **Inference and alternatives:** The definition difference is direct. The article rule may have been used to harmonize classification, or the form may simply capture a broader procedural interval; the supplied sources contain no patient-level switched-case classification to test numeric impact.
- **Human question:** What prespecified or documented reconciliation rule converted form-recorded blade-in/blade-out attempts and device switches into the first-attempt outcome analyzed in Table 3?

### P1-SIGNAL-004 — Interim analysis timing is reported at 507 rather than the protocol's 500 enrolled patients

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC002 [PDF p. 21](../../../joi180054supp1_prod.pdf#page=21), §8.6.2; fresh OCR `preprocessing/ocr_text/DOC002-page-021.txt`. DOC003 [PDF p. 6](../../../joi180054supp2_prod.pdf#page=6), eAppendix 1; fresh OCR `preprocessing/ocr_text/DOC003-page-006.txt`.
- **Direct observation:** The protocol says an interim analysis “will be performed after 500 patients are enrolled.” The eAppendix says, “After 507 patients were enrolled,” then gives the interim primary-outcome fractions 250/257 and 213/250, which sum to 507.
- **Reproducible rule:** `507 ≠ 500`; the eAppendix denominator arithmetic is internally correct, but it differs from the protocol's stated interim-enrollment quantity.
- **Inference and alternatives:** The timing difference is direct. Enrollment, data cleaning, or operational timing may explain completion at 507; the supplied package gives no stated permissible window or amendment. No conclusion about the futility decision is inferred because its exact analysis statistic is not supplied.
- **Human question:** Was the interim analysis intentionally performed after 507 rather than 500 enrolled patients, and is there a contemporaneous operational note or amendment defining the allowed trigger window?

## Pass-1 completion and limitations

- **Relationships completed:** 38 of 38 (`S001`–`S038`), each explicitly marked `PASS_1_COMPLETE` above.
- **Proposed distinct signals:** 4 (`P1-SIGNAL-001` through `P1-SIGNAL-004`); registration must independently merge only genuinely duplicate signals and assign stable `C` IDs only after cross-lane review.
- **Display-zero dispositions:** 0 instances requiring `DISPLAY_ZERO_NOT_CANDIDATE`; all `<.001` displays were treated as bounded conventional notation.
- **Limitations:** No individual-level data, confidence-interval construction, test degrees of freedom, covariance, clustering implementation code, or exact interim futility statistic is supplied. Therefore this pass did not reverse-engineer P values, assume sidedness/variance estimators, or equate CIs and P values where the package does not define the same inferential procedure.
