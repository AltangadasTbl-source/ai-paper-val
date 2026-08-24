# Stable Candidate Ledger

This ledger merges only genuine duplicate checker records that compare the same printed statements under the same rule. Five distinct candidates remain. Every candidate is **Pending Human Adjudication**; no severity, validity, disposition, or correction is assigned.

## C001 — Inclusive versus exclusive fluid threshold in the SCD definition

- **Category:** Measure, label, or scale inconsistency
- **Primary relationships:** N004, N026, N041, N045-N048, N083, S010.
- **Exact source locations:** DOC-001 `jama_parshuram_2018_oi_180015.pdf`, PDF p. 4; DOC-002 `joi180015supp1_prod.pdf`, PDF p. 24; DOC-004 `joi180015supp3_prod.pdf`, PDF p. 6.
- **Printed evidence:** The main article defines the SCD fluid component as `60 mL/kg or greater` within 12 hours before ICU admission. Protocol Table 5 and Supplement 3 eTable 1 define the matched component as `>60 mL/kg`.
- **Comparator and rule:** For the same outcome, population, and 12-hour window, `>=60` includes an exposure of exactly 60 mL/kg while `>60` excludes it.
- **Direct observation:** The boundary operators differ across supplied sources.
- **Derived diagnostic reasoning:** Classification could differ for a boundary case; no event-level data establish whether one occurred.
- **Alternative source-grounded interpretations:** The main article may have intended the support-source rule, or both support documents may have omitted an inclusive boundary used in adjudication.
- **Exact human question:** Which boundary rule was operationally applied, and which documents require harmonization?
- **Checker provenance:** CS-01; numeric/cross-source relationship coverage.
- **State:** Pending Human Adjudication.

## C002 — Mortality absolute-risk-reduction percent/unit conflict

- **Category:** Cross-document numeric inconsistency
- **Primary relationships:** N007, N044, S003, S031-S032.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF pp. 1, 14, and 29; DOC-001 `jama_parshuram_2018_oi_180015.pdf`, PDF p. 4.
- **Printed evidence:** Protocol p. 1 states 0.9 deaths per 1,000; p. 14 states 0.09%; Appendix p. 29 states 0.9% for the same approximately 18% RRR from 5.1 deaths per 1,000. The main paper states a detectable reduction of 0.9 per 1,000.
- **Comparator and rule:** `5.1 x 0.178 = 0.9078` per 1,000, which is 0.09078%, not 0.9%.
- **Direct observation:** Appendix p. 29 is tenfold larger on a percent scale than the matched protocol/main-paper descriptions.
- **Derived diagnostic reasoning:** The percent sign may be a unit transcription error; the source does not establish the intended editorial correction.
- **Alternative source-grounded interpretations:** Appendix p. 29 may have intended 0.09% or 0.9 per 1,000; no alternative baseline or denominator is supplied.
- **Exact human question:** What unit was intended on p. 29, and should all matched planning statements use the same scale?
- **Checker provenance:** NC-01, CS-02, P1-01.
- **State:** Pending Human Adjudication.

## C003 — Cardiac-arrest events assigned incompatible resuscitation-scale categories

- **Category:** Measure, label, or scale inconsistency
- **Primary relationships:** N050, N069, S029.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF pp. 11, 24, and 27.
- **Printed evidence:** P. 11 defines cardiac arrest without preceding DNR as scale 6 or 7; Table 5 assigns CPR to 6 and death to 7; Table 6's legend calls events including cardiac arrest scale 4 or 5.
- **Comparator and rule:** The same named seven-category Children’s Resuscitation Intensity Scale cannot assign the same cardiac-arrest class both 4/5 and 6/7 unless a second scale is defined; none is supplied.
- **Direct observation:** The printed discrete category labels conflict.
- **Derived diagnostic reasoning:** The Table 6 legend may contain a transcription error or may refer to an unnamed scale.
- **Alternative source-grounded interpretations:** A separate abstraction scale could have been intended, but the package does not name one.
- **Exact human question:** Does Table 6 intend 6 or 7, or should it identify a different scale?
- **Checker provenance:** NC-02, CS-03, P1-02.
- **State:** Pending Human Adjudication.

## C004 — Preventability threshold excludes and includes rating 4

- **Category:** Measure, label, or scale inconsistency
- **Primary relationships:** N050, N071, N083, S029.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF pp. 11 and 28; DOC-004 `joi180015supp3_prod.pdf`, PDF p. 6; DOC-001 `jama_parshuram_2018_oi_180015.pdf`, PDF p. 7.
- **Printed evidence:** Protocol p. 11 says `>4` but immediately includes ratings 4, 5, and 6; protocol Table 7 says 4 or more; Supplement 3 likewise defines 4-6 as potentially preventable, and the main-paper footnote describes rating 4 as more than likely preventable.
- **Comparator and rule:** On the stated six-point scale, `>4` selects 5-6, whereas `>=4` selects 4-6.
- **Direct observation:** The threshold notation and explicitly included categories are incompatible.
- **Derived diagnostic reasoning:** The p. 11 greater-than sign may be typographic, but the source does not prove the operational rule.
- **Alternative source-grounded interpretations:** Table 7/final reporting may state the operative definition; alternatively p. 11 may reflect a stricter intended threshold.
- **Exact human question:** Was the applied threshold greater than 4 or 4 or more?
- **Checker provenance:** NC-03, CS-04, P1-03.
- **State:** Pending Human Adjudication.

## C005 — The same SCDE reference count is labelled annual and two-year

- **Category:** Denominator, proportion, or total inconsistency
- **Primary relationships:** N074-N075, S033.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF pp. 14 and 30.
- **Printed evidence:** P. 14 describes 1,052 urgent ICU admissions per year from four hospitals and uses a 40% SCDE assumption with 2 events per 1,000 patient-days. P. 30 states that 1,052 urgent PICU admissions occurred in two years following 31 January 2007, alongside 55,963 discharges and 150 code-blue events.
- **Comparator and rule:** The same reference count cannot simultaneously be an annual count and an unannualized two-year count; a rate/power input must align its count, observation period, and denominator.
- **Direct observation:** The supplied period labels differ for the identical 1,052 count.
- **Derived diagnostic reasoning:** One label could be shorthand or error; the package gives no year-stratified counts or period-specific patient-day denominator.
- **Alternative source-grounded interpretations:** P. 14 may annualize a separately defined dataset, or p. 30 may describe a broader extraction window; neither interpretation is explicitly stated.
- **Exact human question:** What observation period and patient-day denominator support the 1,052-admission count and the 2-per-1,000 SCDE planning rate?
- **Checker provenance:** NC-04; independently reviewed as unresolved/nonreconcilable period provenance by cross-source pass.
- **State:** Pending Human Adjudication.

## C006 — Stat-call absolute reduction does not reproduce from the printed inputs

- **Category:** Numeric or arithmetic inconsistency
- **Primary relationships:** S035.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF p. 30.
- **Printed evidence:** The stat-call planning paragraph prints a baseline rate of 8.13 calls per 1,000 patient-days, maximum relative risk reduction 0.181, and corresponding absolute risk reduction of 1.45 calls per 1,000 patient-days.
- **Comparator and rule:** An absolute reduction derived from a baseline rate and relative reduction is their product: `8.13 x 0.181 = 1.47153` calls per 1,000 patient-days, which rounds to 1.47, not 1.45.
- **Direct observation:** The displayed product does not reproduce the printed absolute reduction at the shown two-decimal precision.
- **Derived diagnostic reasoning:** Even allowing half-unit rounding in the last displayed digits for 8.13 and 0.181 gives an approximate product range of 1.4666 to 1.4765, which does not include 1.45.
- **Alternative source-grounded interpretations:** The calculation may have used more precise undisplayed baseline or relative-reduction inputs, or 1.45 may be a transcription/rounding defect; the package does not supply the underlying power-calculation output.
- **Exact human question:** What unrounded inputs or calculation produced 1.45 per 1,000, and if none did, which displayed value requires correction?
- **Checker provenance:** Final evidence-quality omission review of S035; direct source confirmation.
- **State:** Pending Human Adjudication.

## C007 — Urgent PICU admission rates do not match the printed counts and denominators at conventional rounding

- **Category:** Denominator, proportion, or total inconsistency
- **Primary relationships:** N075.
- **Exact source locations:** DOC-002 `joi180015supp1_prod.pdf`, PDF p. 30.
- **Printed evidence:** The four-hospital reference table prints 1,052 unplanned PICU admissions, 7,300 PICU discharges, 55,963 hospital admissions/discharges, 14.5% per PICU discharges, and 18 per 1,000 hospital discharges.
- **Comparator and rule:** `1,052 / 7,300 x 100 = 14.41096%`, conventionally 14.4% to one decimal; `1,052 / 55,963 x 1,000 = 18.79778`, conventionally 19 to a whole number.
- **Direct observation:** Neither printed rate is the conventional rounded result of its displayed integer numerator and denominator.
- **Derived diagnostic reasoning:** The deviations are small but use different apparent directions: 14.5% is above the calculated value, while 18 per 1,000 is below the calculated value.
- **Alternative source-grounded interpretations:** The table may use undisplayed source denominators or a nonstandard rounding/truncation convention; neither is named in the supplied package.
- **Exact human question:** Which exact denominators and rounding convention produced 14.5% and 18 per 1,000, or should either displayed rate be changed to match the printed counts?
- **Checker provenance:** Final evidence-quality omission review of the N075 reference table; direct source confirmation.
- **State:** Pending Human Adjudication.
