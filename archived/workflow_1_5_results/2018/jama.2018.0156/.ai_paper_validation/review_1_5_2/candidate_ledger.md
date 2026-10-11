# Stable Candidate Ledger

This ledger is the complete union of distinct signals from fresh numeric, cross-source, and statistical-pass-1 review. Signals were merged only when they concerned the same printed values, comparator, and consistency rule. Stable IDs are never renumbered or suppressed. Every entry remains **Pending Human Adjudication**.

## C001 — Noninferiority narrative reverses the displayed bound direction

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=3` (decision rule) and `jama_jabre_2018_oi_180004.pdf#page=4` (ITT result and narrative).
- **Source evidence:** The lower CI endpoint is `-1.64%`; noninferiority requires the lower endpoint to be greater than `-1.00%`. The narrative says the lower limit was greater than the threshold, “thus noninferiority was not demonstrated.”
- **Consistency rule/calculation:** `-1.64% < -1.00%`; the conclusion is compatible with the displayed values, but the word `greater` is not. Difference from the threshold is `-0.64` percentage points.
- **Alternative/source limitation:** The direction word may be a wording error for `not greater`; no replacement is adjudicated.
- **Human question:** Should the direction statement be revised while retaining the printed conclusion?
- **Discovery provenance:** S002; SP1-01.
- **Status:** Pending Human Adjudication

## C002 — Centre-5 pause contrast mixes a count outcome with seconds

- **Category:** Measure, label, or scale inconsistency
- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=4`, Post-Hoc Analyses.
- **Source evidence:** The text describes the `number of pauses greater than 2 seconds`, reports BMV `27` versus ETI `16`, and labels their difference as `11 seconds` with 95% CI `7 to 15`.
- **Consistency rule/calculation:** `27 - 16 = 11` pauses. The 2-second threshold defines a counted event; it does not make the count difference a duration.
- **Alternative/source limitation:** The values might instead be duration summaries, but that would conflict with the printed `number of pauses` wording.
- **Human question:** Are 27 and 16 counts or time quantities, and what unit applies to the difference and interval?
- **Discovery provenance:** N026; S018; NUM-CAND-003; SP1-05.
- **Status:** Pending Human Adjudication

## C003 — PP day-28 survival point difference does not round from the printed inputs

- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2 PP survival row; DOC-002 `joi180004supp1_prod.pdf#page=123` (categorical rounding rule).
- **Source evidence:** BMV is `54/995 (5.4%)`, ETI is `51/943 (5.4%)`, and BMV minus ETI is printed as `0.1` percentage points.
- **Consistency rule/calculation:** `100 × (54/995 - 51/943) = 0.0189` percentage points, which rounds to `0.0` at one decimal, not `0.1`.
- **Alternative/source limitation:** A different retained estimator or denominator could explain the display, but none is stated for the row.
- **Human question:** Which estimator or denominator produced `0.1`, or should the displayed difference round to `0.0`?
- **Discovery provenance:** N016; S010; NUM-CAND-002; SP1-02.
- **Status:** Pending Human Adjudication

## C004 — PP day-28 survival confidence interval has an unresolved scale/precision inconsistency

- **Category:** Statistical reporting inconsistency
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=3` (secondary proportion analysis rule) and `jama_jabre_2018_oi_180004.pdf#page=6` (Table 2 PP survival row); DOC-002 `joi180004supp1_prod.pdf#page=124` (secondary difference-CI rule).
- **Source evidence:** The percentage-point column prints point difference `0.1`, 95% CI `-10 to 9.7`, and `P=.99` for approximately 1,000 participants per arm.
- **Consistency rule/calculation:** A labelled diagnostic using printed binomial proportions gives SE `1.028756` percentage points and an ordinary Wald 95% interval about `-2.00 to 2.04` (`-1.997498 to 2.035226`), not a `19.7`-point-wide interval. This calculation is diagnostic, not a replacement analysis.
- **Alternative/source limitation:** The exact row-level interval construction and retained data are not supplied; a nonstandard method or transcription/decimal issue remains possible.
- **Human question:** What were the generated interval endpoints, units, exact method, and retained inputs for this row?
- **Discovery provenance:** N020; S010; XSC-02; SP1-03.
- **Status:** Pending Human Adjudication

## C005 — PP ROSC ETI percentage conflicts with its count, denominator, and signed difference

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=6`, Table 2 PP ROSC row.
- **Source evidence:** BMV is `342/995 (34.4%)`; ETI is `377/943 (30.0%)`; BMV minus ETI is `-5.6` percentage points with CI `-9.9 to -1.3` and `P=.01`.
- **Consistency rule/calculation:** `100 × 377/943 = 39.979%`, which rounds to `40.0%`, not `30.0%`. `34.37% - 39.98% = -5.61` points, matching the printed `-5.6`; the displayed percentages instead imply `+4.4`.
- **Alternative/source limitation:** The count and signed difference support `40.0%`, but no correction is adjudicated.
- **Human question:** Should ETI read `377/943 (40.0%)`, or does another numerator, denominator, or PP definition apply?
- **Discovery provenance:** N019; S013; NUM-CAND-001; XSC-01; SP1-04.
- **Status:** Pending Human Adjudication

## C006 — Main article and eTable report different contributing-centre counts

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=2` and DOC-003 `joi180004supp2_prod.pdf#page=2`.
- **Source evidence:** The main Methods state `20` EMS centres (`15` France, `5` Belgium). eTable 1 contains 21 distinct investigator-centre rows, each with at least one participant across the arms; their arm totals reconcile to 1018 and 1022.
- **Consistency rule/calculation:** Counting the displayed eTable rows gives `21`, not `20`, for the enrolled trial.
- **Alternative/source limitation:** One EMS centre may map to multiple investigator-centre records, but no centre crosswalk is supplied.
- **Human question:** Do the 21 investigator-centre rows represent 20 EMS centres; if so, what is the mapping?
- **Discovery provenance:** N044; XSC-03.
- **Status:** Pending Human Adjudication

## C007 — Published primary-endpoint description omits the amended baseline-disability qualification

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** DOC-001 `jama_jabre_2018_oi_180004.pdf#page=1` and `#page=3`; DOC-002 `joi180004supp1_prod.pdf#page=110`.
- **Source evidence:** The article defines favourable outcome as CPC `1 or 2`. The later protocol amendment says a participant with neurologic disability before randomization is favourable if survival retains the same disability degree.
- **Consistency rule/calculation:** The amendment can classify a baseline-disabled survivor as favourable even when a CPC-1-or-2-only description would not; the reported counts are labelled only with the narrower article wording.
- **Alternative/source limitation:** The article may be abbreviated or no participant may have required the qualification; participant-level classification evidence is not supplied.
- **Human question:** Which algorithm produced the primary counts, and did any participant rely on the baseline-disability qualification?
- **Discovery provenance:** N041; N051; S037; XSC-04.
- **Status:** Pending Human Adjudication

## C008 — Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** DOC-002 `joi180004supp1_prod.pdf#page=110`; DOC-001 `jama_jabre_2018_oi_180004.pdf#page=1`, `#page=4`, and `#page=6`.
- **Source evidence:** The amended protocol defines technique failure as 28-day mortality, regurgitation, or failure to ventilate/intubate. The article reports ETI failure `21/996 (2.1%)` and ITT ETI 28-day deaths `54/1022`.
- **Consistency rule/calculation:** The flow shows 24 participants outside the 999-person ETI safety display, while the failure row has a further three-person denominator reduction to 996. Under the conservative conditional alignment, `54 - 24 - 3 = 27`, still greater than 21. The exact participant-set alignment is not mechanically established from aggregate displays.
- **Alternative/source limitation:** The article’s `failure` row may be a narrower procedural endpoint or may use an unsupplied final definition or actual-treatment population; the row does not define it and no participant crosswalk is supplied.
- **Human question:** What exact definition and source population produced the Table 3 failure row, and is it intentionally distinct from protocol technique failure?
- **Discovery provenance:** N012; N022; N051; S015; S037; XSC-05.
- **Status:** Pending Human Adjudication

## Registration totals

- Stable candidate IDs: C001 C002 C003 C004 C005 C006 C007 C008.
- Candidate count: 8.
- Every candidate remains Pending Human Adjudication; this ledger contains no AI validity or severity disposition.
