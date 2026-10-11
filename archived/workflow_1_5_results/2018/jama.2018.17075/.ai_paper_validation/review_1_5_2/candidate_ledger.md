# Stable Candidate Ledger

All records are **Pending Human Adjudication**. Lane observations were merged only when they concerned the same printed values, comparator, and rule. Neighboring bleeding outcomes and neighboring CT-category cells remain separate candidates because each concerns a distinct printed row and value pair. No candidate is based on a display-zero P value.

## C001 — Normothermia Injury Severity Score median is below its printed IQR lower endpoint

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Relationships and provenance:** N024; numeric lane NC-01.
- **Exact source location:** DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF p. 5, Table 1, normothermia Injury Severity Score row.
- **Source evidence:** Median 20.0; IQR 20.5-35.0.
- **Comparator and rule:** For a median with a 25th-75th percentile IQR, Q1 must not exceed the median. The printed lower endpoint exceeds the median by 0.5 ISS points.
- **Direct observation versus inference:** The ordering violation is direct. A digit error or nonstandard convention is only a possible explanation; the source labels the display median (IQR).
- **Human question:** What median and IQR endpoints were intended for the normothermia ISS summary?

## C002 — Primary risk difference has opposite signs in matched main-article locations

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Relationships and provenance:** N028, S006; numeric NC-02, cross-source observation 1, statistical pass-1 OBS-01.
- **Exact source locations:** DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF p. 1 abstract Results; PDF p. 5 Results; PDF p. 7 Table 2.
- **Source evidence:** All locations report 117/240 (48.8%) versus 111/226 (49.1%) and the same CI (-9.4 to 8.7). The abstract prints risk difference +0.4%, while Results and Table 2 print -0.4 percentage points.
- **Comparator and rule:** Under the displayed hypothermia-minus-normothermia order, 117/240 - 111/226 = -0.365 percentage points, which rounds to -0.4, not +0.4.
- **Direct observation versus inference:** The sign disagreement is direct. The subtraction is a diagnostic confirmation. An intentionally absolute or reversed contrast is possible only if an unprinted definition differs.
- **Human question:** Is the abstract missing a minus sign, or was a different/absolute contrast intended but not labelled?

## C003 — Intracranial-bleeding effect and P-value reporting conflicts with matched evidence

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Relationships and provenance:** N034, N064, S008, S023; numeric NC-03 (intracranial component), cross-source observation 2, statistical pass-1 OBS-02.
- **Exact source locations:** DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF p. 7 Table 2, new/increased intracranial bleeding; DOC-003, `joi180132supp2_prod.pdf`, PDF p. 10 eTable 6, same outcome.
- **Source evidence:** Both sources print 47/260 (18.1%) versus 37/240 (15.4%). Main Table 2 prints RR 1.23 (0.43-3.5), P=.70; eTable 6 prints P=.43.
- **Comparator and rule:** The printed counts give a diagnostic crude RR of (47/260)/(37/240)=1.173, rounding to 1.17 rather than 1.23. The P values disagree directly for the same matched row/population. The main-table RR/CI/P display appears paired with the neighboring extracranial row, but that production explanation is not assumed.
- **Direct observation versus inference:** Count/RR incompatibility and cross-source P disagreement are direct supplied-source comparisons. The suspected row transposition is inferred.
- **Human question:** Which RR, CI, and P value belong to the intracranial-bleeding outcome?

## C004 — Extracranial-bleeding effect and P-value reporting conflicts with matched evidence

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Relationships and provenance:** N034, N064, S008, S023; numeric NC-03 (extracranial component), cross-source observation 3, statistical pass-1 OBS-03.
- **Exact source locations:** DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF p. 7 Table 2, new significant extracranial bleeding; DOC-003, `joi180132supp2_prod.pdf`, PDF p. 10 eTable 6, same outcome.
- **Source evidence:** Both sources print 8/260 (3.1%) versus 6/240 (2.5%). Main Table 2 prints RR 1.17 (0.79-1.74), P=.43; eTable 6 prints P=.70.
- **Comparator and rule:** The printed counts give a diagnostic crude RR of (8/260)/(6/240)=1.231, rounding to 1.23 rather than 1.17. The P values disagree directly for the same matched row/population. The main-table RR/CI/P display appears paired with the neighboring intracranial row, but that production explanation is not assumed.
- **Direct observation versus inference:** Count/RR incompatibility and cross-source P disagreement are direct supplied-source comparisons. The suspected row transposition is inferred.
- **Human question:** Which RR, CI, and P value belong to the extracranial-bleeding outcome?

## C005 — As-treated evacuated-mass-lesion cell reverses count and percentage order

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationships and provenance:** N069, S028; numeric NC-04, statistical pass-1 OBS-04.
- **Exact source location:** DOC-003, `joi180132supp2_prod.pdf`, PDF p. 18, eTable 10, normothermia (n=196), evacuated mass lesion V.
- **Source evidence:** Under the `No. (%)` header, the cell prints 34.7 (68).
- **Comparator and rule:** 68/196 x 100 = 34.69%, rounding to 34.7%; the values reconcile as 68 (34.7), opposite the printed header order.
- **Direct observation versus inference:** The header/cell order inconsistency is direct. The proposed token reversal is diagnostic, not a final correction.
- **Human question:** Were the intended count and percentage 68 and 34.7%, respectively?

## C006 — As-treated non-evacuated-mass-lesion cell reverses count and percentage order

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationships and provenance:** N069, S028; statistical pass-1 OBS-05.
- **Exact source location:** DOC-003, `joi180132supp2_prod.pdf`, PDF p. 18, eTable 10, normothermia (n=196), non-evacuated mass lesion VI.
- **Source evidence:** Under the `No. (%)` header, the cell prints 1 (2).
- **Comparator and rule:** Read literally, 1/196 is 0.51%, not 2%. Reversing the two tokens gives 2/196 = 1.02%, which rounds to 1%; thus the values reconcile as 2 (1), opposite the printed order.
- **Direct observation versus inference:** The denominator/percentage mismatch is direct. The proposed token reversal is diagnostic, not a final correction.
- **Human question:** Were the intended count and percentage 2 and 1%, respectively?

## C007 — Adjusted odds-ratio confidence-interval string is malformed

- **Status:** Pending Human Adjudication
- **Category:** Statistical reporting inconsistency
- **Relationships and provenance:** N072, S032; statistical pass-1 OBS-06.
- **Exact source location:** DOC-003, `joi180132supp2_prod.pdf`, PDF p. 22, post-hoc adequate-cooling Results.
- **Source evidence:** The printed string is `adjusted odds ratio hypothermia vs normothermia; 0.95 (0.55-275 1.64) P = .84`.
- **Comparator and rule:** A two-sided 95% CI for one OR requires two unambiguous ordered endpoints. The displayed token sequence does not identify such endpoints. Interpreting it as 0.55-1.64 is conjectural and cannot be verified from the supplied model coefficients or SE.
- **Direct observation versus inference:** The malformed interval string is direct in native, layout, and rendered source evidence. Any intended deletion/substitution is inferred.
- **Human question:** What exact lower and upper 95% CI endpoints were intended, and what does the printed `275` token represent?

## C008 — Abstract male count conflicts with its percentage and Table 1 total

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Relationships and provenance:** N004, N020; numeric NC-05.
- **Exact source locations:** DOC-001, `jama_cooper_2018_oi_180132.pdf`, PDF p. 1 abstract Results; PDF p. 5 Table 1.
- **Source evidence:** The abstract states 500 participants with ongoing consent and 402 men (80.2%). Table 1 totals 207+194=401 men among 260+240=500 participants and its arm percentages are 79.6% and 80.8%.
- **Comparator and rule:** 402/500=80.4%, not 80.2%; 401/500=80.2%, matching the table subtotal and displayed abstract percentage.
- **Direct observation versus inference:** The arithmetic and cross-location count mismatch are direct. A typographical count error or different unreported denominator is only a possible explanation.
- **Human question:** Is the abstract count intended to be 401, or was a distinct sex denominator used but not reported?

