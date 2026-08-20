# Stable Candidate Ledger

All candidates below are **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, cross-source, and statistical-pass-1 artifacts. No candidate was removed, merged, or renumbered after registration.

## Registration summary

| Stable ID | Merged provisional provenance | Primary category | Short statement |
|---|---|---|---|
| C001 | CROSS-CAND-001; STAT1-CAND-001 | Cross-document numeric inconsistency | The same 205/291 control room-sharing result is printed as 70.4% and 70.5%. |
| C002 | NUM-CAND-001; CROSS-CAND-002 | Numeric or arithmetic inconsistency | eTable 2 prints 917/1263 as 72.7%, while the fraction and main article support 72.6%. |
| C003 | NUM-CAND-002 | Denominator, proportion, or total inconsistency | eTable 2 percentages use reduced education and marital-status denominators without labeling them. |
| C004 | NUM-CAND-003 | Denominator, proportion, or total inconsistency | eTable 3 percentages use several reduced denominators despite full group-N headings and no missingness labels. |
| C005 | NUM-CAND-004; CROSS-CAND-003; STAT1-CAND-002 | Measure, label, or scale inconsistency | Linked eTable 5 and eFigure use non-equivalent infant-age thresholds, ≥60 versus >60 days. |

## C001 — Matched 205/291 room-sharing result is printed as both 70.4% and 70.5%

- **Status:** Pending Human Adjudication
- **Exact source locations:** DOC-001, `jama_moon_2017_oi_170077.pdf`, PDF p. 7, Table 3, Room Sharing Without Bed Sharing, BF NQI/BF mHealth control arm; DOC-003, `joi170077supp2_prod.pdf`, PDF p. 9, eTable 5, Sleep Location, All-race Breastfeeding/Breastfeeding control row.
- **Printed evidence:** DOC-001 prints `205/291 (70.4)`; DOC-003 prints `N=291`, `205 (70.5%)` for the matched result.
- **Comparator and rule:** Same outcome, all-race control group, age criterion as labeled in the tables, numerator, denominator, raw measure, and one-decimal precision should give one displayed percentage.
- **Diagnostic calculation:** `205 / 291 × 100 = 70.446735%`; conventional one-decimal rounding gives 70.4%.
- **Direct observation versus inference:** The two percentages and shared 205/291 are direct observations. The conventional rounding result is diagnostic arithmetic, not a claim about the production system.
- **Alternative source-grounded interpretation:** An unreported rounding/export rule or transcription difference may exist; no supplied source identifies another denominator for this row.
- **Exact human question:** Which percentage was intended for the matched 205/291 result, and were both displays produced from the same unrounded data and rounding rule?

## C002 — eTable 2 reports 917/1263 as 72.7% while the printed fraction supports 72.6%

- **Status:** Pending Human Adjudication
- **Exact source locations:** DOC-003, `joi170077supp2_prod.pdf`, PDF p. 3, eTable 2, respondent infant age 8–11 weeks; DOC-001, `jama_moon_2017_oi_170077.pdf`, PDF p. 5, Table 1 age counts; DOC-001 PDF p. 8, discussion statement that 72.6% responded at 8–12 weeks.
- **Printed evidence:** eTable 2 declares respondent N=1263 and prints `917 (72.7%)`. Main Table 1 counts 205+214+262+236 total 917; the main discussion prints 72.6%.
- **Comparator and rule:** A percentage adjacent to a count and declared total should reproduce that fraction at the displayed precision; matched aggregate displays should agree after population and precision matching.
- **Diagnostic calculation:** `917 / 1263 × 100 = 72.6049%`, conventionally 72.6% to one decimal.
- **Direct observation versus inference:** Count, denominator, and competing percentages are direct. The rounding conclusion is diagnostic. The main discussion's 8–12-week wording is not presumed identical at its endpoint; the fraction mismatch within eTable 2 stands independently.
- **Alternative source-grounded interpretation:** An unreported denominator, age-bin boundary, or export rule might have been used, although the eTable age rows total 1263.
- **Exact human question:** Does eTable 2 use exactly 917 of 1263 for this percentage, and which one-decimal percentage and age-bin label were intended?

## C003 — eTable 2 uses reduced education and marital-status denominators without labeling them

- **Status:** Pending Human Adjudication
- **Exact source location:** DOC-003, `joi170077supp2_prod.pdf`, PDF p. 3, eTable 2, headings and education/marital-status rows.
- **Printed evidence:** Headings give respondent/nonrespondent/total N values of 1263/337/1600. Education counts sum to 1258/336/1594 and marital-status counts to 1248/332/1580, with no missing/unknown rows or row-specific N labels.
- **Comparator and rule:** Exhaustive category counts should reconcile with the displayed denominator, or a reduced denominator/missingness basis should be disclosed. Printed percentages reveal reduced bases.
- **Diagnostic calculation:** Unaccounted education counts are 5/1/6 and marital counts 15/5/20. Examples: `88/1258=7.00%` and `640/1248=51.28%`, matching printed values; `640/1263=50.67%` would not match 51.3%.
- **Direct observation versus inference:** Counts, headings, percentages, and absent rows are direct. Implicit missing data are a plausible inference, not established by the table.
- **Alternative source-grounded interpretation:** Variable-specific missing observations likely explain the reduced bases, but the table does not label them.
- **Exact human question:** What denominators were intended for education and marital status, and should missing observations or row-specific N values be displayed?

## C004 — eTable 3 percentages use several reduced denominators despite full group-N headings

- **Status:** Pending Human Adjudication
- **Exact source location:** DOC-003, `joi170077supp2_prod.pdf`, PDF p. 5, eTable 3 headings and Race/Ethnicity, Mother's Education, and Marital Status rows.
- **Printed evidence:** Group headings give N=417/387/421/379. Selected exhaustive-looking rows sum below these headings with no missing/unknown category or row N; the printed percentages correspond to the reduced sums.
- **Comparator and rule:** Category counts and percentage bases should equal the displayed group denominator when categories are presented as exhaustive, or the table should disclose missingness/reduced row denominators.
- **Diagnostic calculation:** BF/BF race sums to 416 rather than 417 and `155/416=37.26%` gives 37.3%, while `155/417=37.17%` gives 37.2%. SS/SS education sums to 377 rather than 379; `87/377=23.08%` gives 23.1%, while `87/379=22.96%` gives 23.0%. Marital totals include 414, 419, and 377 versus headings 417, 421, and 379; discriminating cells likewise track the reduced bases.
- **Direct observation versus inference:** Printed counts, headings, and percentages are direct. The presumed existence of missing observations is an inference.
- **Alternative source-grounded interpretation:** Variable-specific missing data could explain all reduced denominators, but the source does not identify the values or bases.
- **Exact human question:** Were these observations missing, and should the affected eTable 3 rows state row-specific denominators or explicit missing categories?

## C005 — Linked eTable 5 and eFigure use ≥60 versus >60 days for the same display population

- **Status:** Pending Human Adjudication
- **Exact source locations:** DOC-003, `joi170077supp2_prod.pdf`, PDF pp. 9–10, eTable 5 title; DOC-003 PDF p. 11, eFigure title and note directing readers to eTable 5 for sample sizes.
- **Printed evidence:** eTable 5 says outcomes are reported when the infant was `≥60 days` old; the linked eFigure says `>60 days` old.
- **Comparator and rule:** The linked table and figure describe the same four outcomes, groups, race/ethnicity display, and sample-size source, so their eligibility-boundary label should agree or be explicitly distinguished. `≥60` includes day 60; `>60` excludes it.
- **Diagnostic calculation:** No arithmetic is required; this is a direct inequality-label comparison.
- **Direct observation versus inference:** The two labels and figure-to-table reference are direct. Whether any infant was exactly 60 days old and whether numerical results differ are unknown and not inferred.
- **Alternative source-grounded interpretation:** The strict symbol may be informal shorthand, or the two displays may use different populations; neither is established in supplied evidence.
- **Exact human question:** Which age rule generated the linked table/figure data, were exactly-60-day records included, and should the labels be harmonized or distinguished?
