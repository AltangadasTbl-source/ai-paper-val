# Cross-Source Consistency Review

## Scope and approach

- **Direct-source scope completed:** all 40 assigned PDF pages: D001 main article pp. 1-9, D002 study protocol pp. 1-15, and D003 results supplement pp. 1-16.
- **Evidence used:** the complete current main and support quantitative evidence maps, source and coverage inventories, and direct-PDF layout/visual confirmation for matched locations. Reused text was used for location and transcription support; the PDFs were the authority for the observation below.
- **Matching rule:** a value was compared only after population, time, contrast, analysis set, model or summary type, measure, scale/unit, reference group, and displayed precision were aligned. Planned protocol targets were not compared as though they were final observed results.
- **Qualifying candidate count:** 1.
- **No C IDs or adjudications are assigned in this checker artifact.**

## Matched-result coverage record

The following cross-source keys were reviewed to completion. Entries marked `No qualifying difference` matched after the stated attributes were aligned; this is a coverage record, not an adjudication.

| Cross-source key | Locations checked | Comparison logic and result |
|---|---|---|
| Main randomized population and arms | D001 pp. 1, 2, 4, 6; D003 pp. 5, 12-14 | The 1,503 randomized main-arm participants (759 intervention; 744 assessment-only control), the separate 178-person waitlist, and the responder populations were kept distinct. No qualifying difference. |
| Primary 7-month 30-day PPA, ITT/missing=vaping | D001 pp. 1, 2, 5-6; D002 pp. 5-6; D003 pp. 4, 11, 14 | Same outcome, 7-month time, main-arm contrast, missing=vaping analysis, percent scale, and rounding: 37.8% versus 28.0%, RD 9.9 percentage points, RR 1.35, OR 1.57, and printed intervals/P threshold match. Protocol defines the outcome/planned analysis rather than reporting a competing result. No qualifying difference. |
| Repeated PPA, ITT/missing=vaping | D001 pp. 5-6; D002 p. 5; D003 pp. 5, 14 | Same 1- and 7-month repeated-PPA definition and main-arm ITT analysis: 17.3% versus 8.2%, RR 2.10, OR 2.34, and displayed intervals/P threshold match where both print the result. No qualifying difference. |
| Complete-case and IPRW 7-month PPA | D001 pp. 4-5; D003 pp. 5, 14 | CCA denominators (521/543 for 30-day PPA; 517/538 for repeated PPA), CCA RRs (1.44; 2.24), and IPRW RRs (1.42; 2.21) match. These were not compared to ITT estimates as though they shared an analysis set. No qualifying difference. |
| Multiple-imputation sensitivity and primary estimate | D001 pp. 4-6; D002 p. 6; D003 pp. 4, 11 | The D003 `OR.miss=+infinity` row supplies P1 37.98%, P0 28.06%, difference 9.92 points, RR 1.35, and OR 1.57, which agree with D001’s rounded missing=vaping primary display. Different `OR.miss` rows are sensitivity analyses, not competing primary results. No qualifying difference. |
| Follow-up and response rates | D001 pp. 1, 4, 6-7; D002 pp. 4, 7; D003 pp. 5, 12-13 | Main-arm 7-month retention is 1,064/1,503 = 70.8%, while arm-specific response is 521/759 = 68.6% and 543/744 = 73.0%; all-source values agree after numerator and denominator are matched. Expected protocol retention is prospective, not a final comparator. No qualifying difference. |
| Baseline characteristics and measure scales | D001 pp. 1, 3-5; D002 p. 15; D003 pp. 3, 7-10, 12-13 | Main Table 1 control values match D003 eTables 1-2; pooled narrative/abstract values are compatible with pooled denominators and displayed rounding. The D003 eTable-2 health-concern value is a median (IQR), whereas D001 Table 1 reports a mean (SD), so they are different summary scales and were not treated as a numerical conflict. PEARLS and loneliness missingness aligns with their post-launch addition. No qualifying difference. |
| Moderator analysis | D001 pp. 4-5; D003 pp. 6, 15; D002 pp. 5-6 | D001’s statement that no moderator remained statistically significant after Holm adjustment matches D003 eTable 6’s adjusted P values and its interaction-model/reference definition. Nominal and adjusted P values were not conflated. No qualifying difference. |
| CTP/e-cigarette outcomes and participant flow | D001 pp. 4, 6-7; D003 pp. 5, 12-14 | These results have no second printed cross-document outcome table. Internal narrative/table/figure occurrences match their appropriate complete-data populations; distinct 1,016 CTP analytic and 1,503 randomized populations were not conflated. No qualifying difference. |
| Intervention message schedule | D001 p. 3; D002 p. 2; D003 p. 2 | Same named intervention, quit-date-dependent schedule, and unit (weeks before/after quit date). The printed pre-quit duration conflicts; detailed candidate below. |

## Candidate consistency issue: quit-date message duration is printed as 6 weeks in the main article and 1 week in both supplied support documents

**Category:** Cross-document numeric inconsistency.

**Exact linked locations:**

- [D001 main article — PDF p. 3](../../../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3), Intervention description: “Those who set a quit date receive messages **6 weeks before** and 8 weeks after their quit date.”
- [D002 study protocol — PDF p. 2](../../../joi240078supp1_prod_1739900423.22574.pdf#page=2), This is Quitting description: “Those who set a quit date receive messages for **a week before** and 8 weeks afterward.”
- [D003 results supplement — PDF p. 2](../../../joi240078supp2_prod_1739900423.24574.pdf#page=2), eAppendix A: “Users receive messages for **1 week preceding** their quit date and 8 weeks afterward.”

**Printed values and matched attributes:** All three statements describe *This is Quitting*, the quit-date subgroup, the message schedule, and duration in weeks relative to the quit date. Each agrees on the 8-week post-quit segment. The D001 pre-quit segment is 6 weeks; the D002 and D003 pre-quit segments are 1 week.

**Comparison logic:** For the same intervention component, user subgroup, temporal anchor, and unit, `6 weeks before` cannot equal `1 week before` at the printed precision. This is not a comparison of different analysis sets, outcome definitions, or summary statistics.

**Direct observation versus inference:** The conflicting printed durations are direct source observations. The source package does not establish whether the main article describes a different program version, whether the protocol/eAppendix text is outdated, or which schedule trial participants actually received; those are alternative explanations, not conclusions of this review.

**Supported source-grounded alternatives:**

- D002 and D003 may consistently describe a one-week pre-quit schedule, while D001 may describe a six-week schedule for a different version of the same program.
- D001 may contain a transcription or editorial discrepancy, because both supplied support documents independently print one week; the supplied package does not prove that explanation.
- A schedule change could have occurred between documentation versions, but no supplied change record identifies a change from one week to six weeks or establishes its effective date.

**Human verification steps:**

1. Inspect the intervention delivery specification, version history, and participant message logs retained for this trial to identify the pre-quit sequence actually delivered to participants.
2. Confirm whether all three documents intended to describe the trial-period program rather than different program releases.
3. Check editorial production files for D001 p. 3 and the supplement/protocol source text to determine whether “6 weeks” or “1 week” was introduced during manuscript preparation.
4. If a version-specific schedule is confirmed, add the version/effective-date qualifier at each occurrence; otherwise reconcile the printed duration across the article and both support documents.

## Limitations

- The supplied package has no structured datasets, workbooks, or source-level message-delivery logs. Therefore, the review can establish the printed cross-document discrepancy but cannot resolve which schedule was implemented.
- Protocol statements of planned recruitment, sample size, retention, adjustment, and analyses were not called differences merely because final reported conduct/results differed; no source-grounded same-result conflict was shown after purpose and analysis timing were matched.
- Page 8/9 of D001; pages 1 and 8-14 of D002; and pages 1 and 16 of D003 contain no additional matched trial result beyond the mapped administrative, reference, or repeated narrative material.
