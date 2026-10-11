# Stable Candidate Ledger — Workflow 1.5.1

All entries are quality-control candidates and remain **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, statistical-pass-1, and cross-source checker artifacts. No candidate is based solely on a display-zero P value.

## C001 — Protocol and reported primary endpoint differ on the diabetes-range A1C failure condition

- **Category:** Cross-document numeric inconsistency
- **Relationships:** N002, N038, N087; S001, S008-S010.
- **Checker provenance:** CROSS-CAND-001.
- **Exact source locations:** DOC-002 PDF p. 15; DOC-001 PDF p. 4; DOC-003 PDF p. 30 (explicit global-failure method) and p. 56 (15-participant table).
- **Source evidence:** The protocol defines success as meeting at least one of three component thresholds. The main report additionally requires HbA1c below 6.5% throughout; the supplement method on p. 30 says diabetes-range A1C at 6 and/or 12 months forces failure, and p. 56 lists the corresponding 15 participants.
- **Consistency rule:** The population, 12-month role, components, thresholds, and contrast match, but the added A1C failure condition can change the binary endpoint classification.
- **Alternative source-grounded interpretation:** An unprovided protocol amendment or final SAP revision may have introduced the rule.
- **Exact human question:** Was the throughout-study HbA1c rule prospectively added, and which supplied endpoint definition governed the final analysis?
- **Status:** Pending Human Adjudication.

## C002 — 312 listed 12-month A1C measurements versus 313 participants with A1C available

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships:** N006, N069, N102.
- **Checker provenance:** NUM-CAND-002; CROSS-CAND-002.
- **Exact source locations:** DOC-001 PDF pp. 4-5; DOC-003 PDF p. 8 and pp. 48-50.
- **Source evidence:** The device rows total 282 + 30 + 0 = 312. The main report states 313 complete outcomes, while eTable 8c gives 26 + 29 = 55 missing A1C observations among 368 and no missing A1C among completers, implying 313 available.
- **Consistency rule:** Exhaustive participant-level method counts should reconcile with the matched A1C availability total.
- **Alternative source-grounded interpretation:** One result may use an unlisted method or the method table may not be exhaustive despite its framing.
- **Exact human question:** Which participant or method accounts for the one-observation difference?
- **Status:** Pending Human Adjudication.

## C003 — Figure 3 labels BMI values in kg/m² as “weight”

- **Category:** Measure, label, or scale inconsistency
- **Relationships:** N025.
- **Checker provenance:** NUM-CAND-001; CROSS-CAND-003.
- **Exact source locations:** DOC-001 PDF p. 8 Figure 3 footnote a and p. 6 Table 1; DOC-003 PDF pp. 53-54 provides a supporting BMI distinction.
- **Source evidence:** Figure 3 prints 32.2 (28.2-35.9) and 32.5 (29.3-37.7) kg/m² as baseline “weight”; Table 1 prints the identical triplets as BMI.
- **Consistency rule:** kg/m² and the exact matched values identify BMI, whereas weight is a mass quantity.
- **Alternative source-grounded interpretation:** “Weight” may be shorthand or a figure-label carryover, but the package supplies no literal-weight interpretation for these values.
- **Exact human question:** Should the Figure 3 label read “BMI,” or were different values/units intended?
- **Status:** Pending Human Adjudication.

## C004 — eTables 5-7 leave the comparator scope of a repeated age P value ambiguous

- **Category:** Cross-document numeric inconsistency
- **Relationships:** N098-N101; S022, S024-S026.
- **Checker provenance:** CROSS-CAND-004.
- **Exact source locations:** DOC-003 PDF pp. 39-40, 42-47.
- **Source evidence:** eTables 5, 6, and 7 repeat “Age differed between study groups (p = 0.014)” although their displayed columns compare site, baseline A1C status, and completion status. eTable 3 repeats p=.014 in an overall baseline context but does not itself display treatment-arm columns; treatment-arm attribution is a supported inference from the matched main Table 1 result, not a direct eTable 3 observation.
- **Consistency rule:** A P value is tied to a population and contrast; the repeated note does not clearly state whether it is global treatment-arm context or the table-specific comparison across distinct contrasts.
- **Alternative source-grounded interpretation:** The footnote may intentionally restate a global treatment-arm fact, but its placement does not identify that scope.
- **Exact human question:** Is p=.014 a global treatment-arm note or a table-specific result, and should the repeated footnotes be relocated, relabeled, or replaced?
- **Status:** Pending Human Adjudication.

## C005 — eTable 7 pairs “no statistically significant” with p<0.05

- **Category:** Statistical reporting inconsistency
- **Relationships:** N101; S026.
- **Checker provenance:** NUM-CAND-003; STAT1-CAND-003; CROSS-CAND-005.
- **Exact source locations:** DOC-003 PDF pp. 46-47, eTable 7 footnotes 1-2.
- **Source evidence:** Footnote 1 says no baseline characteristics were statistically significantly different and appends p<0.05; footnote 2 uses p=.014 for a difference and p>0.05 for similarity.
- **Consistency rule:** Under the table's own convention, p<0.05 denotes significance and conflicts with the no-significance wording.
- **Alternative source-grounded interpretation:** The comparator sign or sentence may be a typographical carryover, or may refer to an unstated test family.
- **Exact human question:** What were the completion-status comparison results, and should the inequality or the sentence be corrected?
- **Status:** Pending Human Adjudication.

## C006 — eTable 10b labels one comparison as both chi-squared and Wilcoxon rank-sum

- **Category:** Statistical reporting inconsistency
- **Relationships:** N085, N104; S018, S028.
- **Checker provenance:** NUM-CAND-004; STAT1-CAND-002.
- **Exact source locations:** DOC-003 PDF p. 29 and p. 52.
- **Source evidence:** The eTable 10 method description specifies chi-squared for the between-group proportion, while eTable 10b prints 6/183 versus 7/185, P=.793, with a Wilcoxon rank-sum footnote.
- **Consistency rule:** The same binary comparison cannot carry two incompatible test labels without an explained distinction.
- **Alternative source-grounded interpretation:** The p. 29 description may be general, or the p. 52 footnote may be copied from another row.
- **Exact human question:** Which test generated P=.793 and which method label should be retained?
- **Status:** Pending Human Adjudication.

## C007 — MICE pooled percentages and printed risk difference have incompatible signs

- **Category:** Statistical reporting inconsistency
- **Relationships:** N110; S019, S031.
- **Checker provenance:** STAT1-CAND-001.
- **Exact source locations:** DOC-003 PDF p. 59, eTable 16; method context DOC-003 PDF p. 30.
- **Source evidence:** The table prints AI 32.2% and human 31.9% but an AI-minus-human risk difference of -1.1 percentage points.
- **Consistency rule and calculation:** The displayed percentages imply about +0.3 percentage points. Values that round to 32.2% and 31.9% bound the underlying displayed-value difference at approximately +0.2 to +0.4 percentage points, so ordinary one-decimal rounding cannot directly yield -1.1.
- **Alternative source-grounded interpretation:** The risk difference may be adjusted or standardized under an unstated estimand that differs from the printed pooled marginal percentages.
- **Exact human question:** Does the risk-difference cell use an unreported adjusted estimand, or is one displayed percentage/contrast inconsistent?
- **Status:** Pending Human Adjudication.

## Stable-set summary

- **Stable candidates:** 7 (C001-C007).
- **Cross-lane merge rule:** Only records with the same printed values/statements, comparator, and consistency rule were merged.
- **Required next stage:** Mechanical direct-source recheck of every stable ID.
