# Stable Candidate Ledger

All candidates below are **Pending Human Adjudication**. They were merged before stable IDs only when they concern the same printed values, comparator, and consistency rule. No candidate has an AI validity, severity, acceptance, exclusion, or correction disposition.

## C001 — Baseline oxygenation denominators conflict with stated saturation missingness

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** Numeric-check Signal 4; canonical N013 and N017.
- **Exact source locations:** DOC001 `jama_driver_2018_oi_180054.pdf`, PDF p. 5, Table 1 oxygen-saturation rows and footnote b.
- **Direct source evidence:** Group sizes are 381 and 376. Oxygenation rows use denominators 352 and 344. Footnote b states 43 lacked oxygen saturation, split 19 and 24.
- **Comparator and rule:** Available-data denominators imply missing values of 381−352=29 and 376−344=32, total 61; the footnote instead gives 19+24=43 for the same baseline saturation field.
- **Alternative source-grounded interpretation:** Vital-sign labels or group splits may be transposed in the footnote, or the threshold rows may use an unstated different availability time point.
- **Remaining human question:** Which denominators/missingness values describe baseline oxygen saturation, and what distinct field or time point reconciles both displays if both are intended?
- **Status:** Pending Human Adjudication

## C002 — Patient-position rows leave unreported observations in both arms

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** Numeric-check Signal 2; canonical N021.
- **Exact source locations:** DOC001, PDF p. 6, Table 2, “Patient position for intubation”; DOC003, PDF p. 9, postintubation form item 11.
- **Direct source evidence:** Bougie rows are 222, 117, and 39 against n=381; ETT+stylet rows are 244, 96, and 32 against n=376. DOC003 item 11 directs the recorder to select one of four positions, adding `Seated Upright` to the three positions displayed in Table 2.
- **Comparator and rule:** The three displayed position categories sum to 378 and 372, leaving 3 and 4 patients relative to their randomized-arm denominators.
- **Alternative source-grounded interpretation:** The explicit `Seated Upright` form option or missing values may account for the deficits, but the package provides no counts for that fourth option and the residuals cannot be assigned to it.
- **Remaining human question:** Are the three rows intended to exhaust patient positions, and if not, what omitted/missing categories contain the 3 and 4 observations?
- **Status:** Pending Human Adjudication

## C003 — Final-intubator categories exceed the Bougie arm total

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** Numeric-check Signal 1; canonical N024.
- **Exact source locations:** DOC001, PDF p. 6, Table 2 operator rows and footnote f; DOC003, PDF p. 7, postintubation form item 2.
- **Direct source evidence:** Bougie-arm operator counts are 318 senior resident/fellow, 57 junior resident, and 8 faculty against n=381. Footnote f says the rows list the final intubating physician. DOC003 item 2 instructs the recorder to circle one training level from G1, G2, G3, G4+/Fellow, Faculty, PA, or Other.
- **Comparator and rule:** A singular final-intubator classification should assign one category per patient, but 318+57+8=383, exceeding 381 by 2. Each printed percentage separately rounds from its count.
- **Alternative source-grounded interpretation:** Mapping the form's additional PA or Other choices into the displayed table categories, changed intubators, or a transcription/denominator issue could explain the excess; the package does not show the coding map or reconcile the two-count excess.
- **Remaining human question:** Are the operator rows mutually exclusive final-intubator categories, and which value should reconcile their total with 381 if so?
- **Status:** Pending Human Adjudication

## C004 — Video-screen-use categories do not account for their printed denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Provenance:** Numeric-check Signal 3; canonical N026.
- **Exact source locations:** DOC001, PDF p. 6, Table 2 video-screen-use rows and footnote g; DOC003, PDF p. 10, postintubation form item 14.
- **Direct source evidence:** Bougie counts are 218/377, 78/377, and 75/377; ETT+stylet counts are 182/372, 90/372, and 98/372. Footnote g says four values were missing in each randomized group, which produces the printed denominators. DOC003 item 14 includes the three displayed choices plus `N/A - Blade inserted and removed before attempting intubation`.
- **Comparator and rule:** If the displayed never/entire-attempt/during-passage categories partition available observations, the sums are 371 and 370, leaving 6 and 2 observations.
- **Alternative source-grounded interpretation:** The explicit N/A form response may account for some residuals, or the rows may be nonexhaustive or overlapping; the package provides no arm counts for N/A, so the residual 6 and 2 cannot be assigned to it.
- **Remaining human question:** Are these rows intended to partition nonmissing screen use, and if so, what accounts for the 6 and 2 unrepresented observations?
- **Status:** Pending Human Adjudication

## C005 — Main Table 3 reverses duration confidence-interval endpoints

- **Category:** Statistical reporting inconsistency
- **Provenance:** Statistical pass-1 P1-SIGNAL-001 and cross-source Signal B, merged as the same values/comparator/rule; canonical S019 and S036.
- **Exact source locations:** DOC001, PDF p. 7, Table 3 all-patient first-attempt duration; DOC003 `joi180054supp2_prod.pdf`, PDF p. 2, eTable 1, with clustering footnote on p. 3.
- **Direct source evidence:** Main Table 3 prints group medians 38 versus 36 seconds and difference `1 (4 to −1)` seconds. The supplement’s physician-clustered eTable prints the same medians and point difference as `1 (−1 to 4)` seconds.
- **Comparator and rule:** A confidence interval is printed lower-to-upper; 4 is greater than −1, while the reordered endpoints −1 to 4 contain the point estimate 1.
- **Alternative source-grounded interpretation:** The main display may contain a typographical transposition. The eTable uses a clustering-adjusted analysis and therefore corroborates endpoint ordering but does not prove the unadjusted interval-generation output.
- **Remaining human question:** What were the calculated unadjusted interval endpoints, and does the production source confirm the intended Table 3 order?
- **Status:** Pending Human Adjudication

## C006 — Published duration outcome uses a different endpoint from the protocol

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** Statistical pass-1 P1-SIGNAL-002 and cross-source Signal A, merged as the same outcome-definition comparison; canonical N007, N038, N048, S016, S019, S025, S026, S032, S035-S037.
- **Exact source locations:** DOC002 `joi180054supp1_prod.pdf`, PDF pp. 9-10; DOC001, PDF pp. 3 and 7; DOC003, PDF p. 3.
- **Direct source evidence:** The protocol defines first-attempt time to intubation from attempt beginning to ETT-cuff inflation in the trachea. The article and supplementary eTable define reported duration from blade entry into the mouth to blade removal.
- **Comparator and rule:** Cuff inflation and blade removal are distinct end events and can yield different seconds; matched outcome labels/results require an endpoint mapping or amendment.
- **Alternative source-grounded interpretation:** An intentional amendment, two distinct measures, or a recording/terminology change may explain the difference; no supplied amendment resolves it.
- **Remaining human question:** Direct tabular evidence establishes that the published medians and differences use blade removal, but which terminal event generated each Kaplan-Meier curve and hazard ratio remains unresolved; where is any dated amendment or analysis mapping?
- **Status:** Pending Human Adjudication

## C007 — Reported 507-patient interim set differs from the protocol’s first-500 analysis set

- **Category:** Cross-document numeric inconsistency
- **Provenance:** Statistical pass-1 P1-SIGNAL-004; canonical S033 and S038.
- **Exact source locations:** DOC002, PDF p. 21, section 8.6.2; DOC003, PDF p. 6, eAppendix 1.
- **Direct source evidence:** The protocol states that the interim analysis will be performed after 500 patients are enrolled and specifically describes analysis of data from the first 500 patients. The eAppendix states it occurred after 507 and reports 250/257 versus 213/250, whose denominators sum to 507.
- **Comparator and rule:** The protocol's first-500 analysis set differs from the reported 507-patient denominators. The eAppendix arithmetic is internally consistent, and the phrase “after 500” alone does not require an analysis at exactly 500.
- **Alternative source-grounded interpretation:** Operational enrollment overshoot, data cleaning, or a permitted trigger window may explain the difference; no such window or amendment is supplied.
- **Remaining human question:** Was 507 an authorized operational trigger, and what contemporaneous note or amendment defines the allowed interval around 500?
- **Status:** Pending Human Adjudication

## Checked signal not registered

The protocol/form/article attempt-switch boundary was reviewed across statistical and cross-source lanes. It was not assigned a stable candidate because the form separately records device switching and the article’s first-device-success rule can reconcile outcome status; no supplied numeric result or denominator is shown to conflict under those definitions. This is not a suppressed assigned candidate ID because stable IDs were created only after cross-lane merging and threshold review.

## Ledger completeness

- Distinct stable candidates: 7 (`C001`-`C007`).
- Duplicate merge: the reversed interval signal from two lanes became C005; the duration-endpoint signal from two lanes became C006.
- No stable ID was deleted, renumbered, or merged after registration.
