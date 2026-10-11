# Stable Candidate Ledger

All candidates below are **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, cross-source, and statistical-pass-1 proposals. No candidate was deleted, ranked, or assigned severity or validity.

## C001 — Women’s quantitative 10.2 µg Hb/g PPV difference point estimate is absent

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC001 and XC001 (genuine duplicate merged before stable-ID assignment); relationship N062.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women/Quantitative/10.2, Difference in PPV cell; comparator counts at PDF p. 6, eTable 4, same population/test/cutoff.
- **Source evidence:** eTable 5 prints aspirin PPV 15.9%, placebo PPV 34.1%, only `-` in the difference point-estimate position, and 95% CI [-34.7, -1.3]. eTable 4 prints aspirin TP/FP 11/58 and placebo TP/FP 14/27.
- **Consistency rule and calculation:** The named contrast is aspirin minus placebo. `(11/(11+58) - 14/(14+27)) × 100 = -18.204...`, which rounds to -18.2 percentage points; 15.9 − 34.1 likewise gives -18.2. A lone minus sign is not a numeric point estimate.
- **Alternative source-grounded interpretation:** The numeric characters may have been lost in table production, or an undocumented dash convention may have been intended; the supplied page does not explain it.
- **Exact human question:** Does the visible dash reflect clipping of the diagnostically count-derived -18.2 value, or did the unprovided source output use a different point estimate or dash convention?
- **Status:** Pending Human Adjudication.

## C002 — Women’s quantitative 17.0 µg Hb/g PPV difference point estimate is absent

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC002 and XC002 (genuine duplicate merged before stable-ID assignment); relationship N062.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women/Quantitative/17.0, Difference in PPV cell; comparator counts at PDF p. 6, eTable 4, same population/test/cutoff.
- **Source evidence:** eTable 5 prints aspirin PPV 17.1%, placebo PPV 42.9%, only `-` in the difference point-estimate position, and 95% CI [-48.4, -0.7]. eTable 4 prints aspirin TP/FP 6/29 and placebo TP/FP 9/12.
- **Consistency rule and calculation:** `(6/(6+29) - 9/(9+12)) × 100 = -25.714...`, which rounds to -25.7 percentage points. Subtracting the rounded displayed PPVs gives -25.8, a 0.1-point rounding difference; neither value is printed in the named point-estimate position.
- **Alternative source-grounded interpretation:** The dash may be a truncated negative value or an undocumented omission convention; exact unrounded source output is not supplied.
- **Exact human question:** Does the visible dash reflect clipping of the diagnostically count-derived -25.7 value, or did the unprovided source output use a different point estimate or convention?
- **Status:** Pending Human Adjudication.

## C003 — Women’s qualitative 10.2 µg Hb/g PPV difference point estimate is absent

- **Category:** Numeric or arithmetic inconsistency.
- **Checker provenance:** NC003 and XC003 (genuine duplicate merged before stable-ID assignment); relationship N062.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5, Women/Qualitative/10.2, Difference in PPV cell; comparator counts at PDF p. 6, eTable 4, same population/test/cutoff.
- **Source evidence:** eTable 5 prints aspirin PPV 9.7%, placebo PPV 31.2%, only `-` in the difference point-estimate position, and 95% CI [-38.9, -3.9]. eTable 4 prints aspirin TP/FP 6/56 and placebo TP/FP 10/22.
- **Consistency rule and calculation:** `(6/(6+56) - 10/(10+22)) × 100 = -21.572...`, which rounds to -21.6 percentage points. Subtraction of displayed rounded PPVs gives -21.5; the 0.1-point difference is explainable by rounding, but the source prints no numeric estimate.
- **Alternative source-grounded interpretation:** The repeated dash may reflect a production omission or undocumented convention rather than failure to calculate the contrast.
- **Exact human question:** Does the visible dash reflect clipping of the diagnostically count-derived -21.6 value, or did the unprovided source output use a different point estimate or convention?
- **Status:** Pending Human Adjudication.

## C004 — eTable 5 visible cutoff header truncates after “[µg”

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** XC004; relationships N057-N062 and matched main-paper cutoff relationships N005, N013-N030.
- **Exact source locations:** DOC-004, `joi190039supp3_prod.pdf`, PDF p. 7, eTable 5 visible header showing `Cutoff` with `[µg` on the next line and no visibly rendered `Hb/g]`; comparator at PDF p. 6, eTable 4 visible header `Cutoff [µg Hb/g]`, for the same day-2 per-protocol tests and 10.2/17.0 cutoff values.
- **Source evidence and rule:** The visible header ends after the mass-unit prefix and does not render the denominator or closing bracket needed for the matched fecal concentration scale. The outcome columns change from sensitivity/specificity to PPV/NPV, but the FIT cutoff scale does not.
- **Alternative source-grounded interpretation:** The PDF text-object layer contains a detached `Hb/g]` fragment, supporting a rendering/layout-clipping explanation rather than a different intended unit; the supplied page does not visibly connect that fragment to the header.
- **Exact human question:** Was `Hb/g]` intended to render as part of the eTable 5 cutoff header, and does the author-approved production source show the full `µg Hb/g` scale?
- **Status:** Pending Human Adjudication.

## C005 — One SAP occurrence omits the microgram prefix from the 10.2 cutoff

- **Category:** Measure, label, or scale inconsistency.
- **Checker provenance:** SP1-001; statistical relationship S017 with cross-references S014, S004, and S006.
- **Exact source locations:** DOC-003, `joi190039supp2_prod.pdf`, PDF p. 6, §3.2 (`17 μg Hb/g feces and 10.2 Hb/g feces`); comparator at DOC-003 PDF p. 8, §5.4 (`10.2 μg Hb/g feces`), and DOC-001 `jama_brenner_2019_oi_190039.pdf`, PDF pp. 1 and 5.
- **Source evidence and rule:** These locations identify the same lower quantitative-FIT cutoff, but the p. 6 occurrence lacks `μg`, which defines the numerator unit of the scale.
- **Alternative source-grounded interpretation:** The second threshold may be intended to inherit `μg` grammatically from the preceding 17-unit threshold; the source does not make that inheritance explicit.
- **Exact human question:** Does DOC-003 p. 6 intentionally inherit `μg`, or should the lower cutoff be printed explicitly as `10.2 μg Hb/g feces`?
- **Status:** Pending Human Adjudication.

## Registration summary

- Temporary proposals reviewed: 8 (NC001-NC003, XC001-XC004, SP1-001).
- Genuine duplicate merges before stable IDs: NC001/XC001; NC002/XC002; NC003/XC003.
- Stable candidates registered: 5 (C001-C005).
- Stable candidate status: Pending Human Adjudication for every ID.
