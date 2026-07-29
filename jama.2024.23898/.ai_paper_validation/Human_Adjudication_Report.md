# AI Paper Validation — Human Adjudication Report

## Disposition

Scoped scientific audit completed after the user recorded authorization for the AI investigation. Five accepted issues are listed below; all are **Minor**. One additional statistical lead (a day-5 EQ-5D-5L comparison) is excluded as **Uncertain** because the supplied package does not report the needed omnibus or multiplicity-analysis result. Source PDFs were not modified.

## AI Training Restriction Summary

| Document ID | Filename | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|---|
| JAMA-2024-23898-MAIN | `jama_paterson_2024_oi_240139_1741633738.12862.pdf` | Explicit AI Training Restriction | PDF p. 1 (printed p. 39) footer, repeated pp. 2-10: “© 2024 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; subsequent investigation authorized by the user. |
| JAMA-2024-23898-SUPP-01-PROTOCOL | `joi240139supp1_prod_1741633738.16362.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF pp. 1-3, 55, 62-66 and metadata; p. 55 is a non-AI confidentiality clause. | No |
| JAMA-2024-23898-SUPP-02-SAP | `joi240139supp2_prod_1741633738.17362.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF p. 1, pp. 36-40, metadata, and attachment inventory; no relevant language located. | No |
| JAMA-2024-23898-SUPP-03-RESULTS | `joi240139supp3_prod_1741633738.18862.pdf` | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 footer: generic “© 2024 American Medical Association. All rights reserved”; metadata had no relevant language. | No |
| JAMA-2024-23898-SUPP-04-DATA-SHARING | `joi240139supp4_prod_1741633738.20861.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 and metadata; data-proposal approval concerns access to deidentified data, not AI training. | No |

This compliance screen is separate from the scientific issue list and is not legal advice.

## Accepted Scientific Issues

### 1. Confidence-interval level differs within the subgroup eFigure

- **Category / severity:** Presentation inconsistency / Minor
- **Issue:** The results-supplement eFigure labels its intervals as both 99% and 95% CIs.
- **Evidence:** `JAMA-2024-23898-SUPP-03-RESULTS`, `joi240139supp3_prod_1741633738.18862.pdf`, PDF p. 2, eFigure key: “99% CI”; sentence below the figure: “The numbers on the right are the within-subgroup relative risks and 95% confidence interval.” The Overall row is `0.97 (0.88, 1.07)`. `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF p. 5, Primary Outcome calls the identical result `0.97 [95% CI, 0.88 to 1.07]`.
- **Comparison / rule:** Identical estimate and endpoints have two conflicting confidence-level labels; `99% ≠ 95%` (no rounding tolerance applies).
- **Bounded impact:** The interval label is ambiguous; this does not challenge the point estimate or printed limits.
- **Human verification:**
  1. Compare the eFigure key and sentence on Supplement 3 PDF p. 2.
  2. Compare its Overall row with the main article’s primary-outcome interval on PDF p. 5.
  3. Confirm the CI level used for the eFigure and correct the conflicting descriptor.

### 2. Figure 2 calls primary-analysis participants treatment recipients

- **Category / severity:** Presentation inconsistency / Minor
- **Issue:** Figure 2 says its curves show patients who “received” treatment, but its day-0 risk counts include randomized participants who did not receive treatment.
- **Evidence:** `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF p. 8, Figure 2 caption: “patients who received intravenous (IV) lidocaine and placebo”; day-0 risk table: IV lidocaine `279`, placebo `278`. PDF p. 3, Figure 1: IV `267 Received` and `12 Did not receive treatment`; placebo `265 Received` and `13 Did not receive treatment`. PDF p. 5 states the primary-analysis groups were `279` and `278`, with `267` and `265` receiving randomized treatment.
- **Calculation / comparison:** `267 + 12 = 279`; `265 + 13 = 278`; and `12 + 13 = 25 = 557 − 532`. The figure therefore uses primary-analysis, not recipient-only, counts.
- **Bounded impact:** The caption mischaracterizes the analysis population; the plotted risk counts are not shown to be wrong.
- **Human verification:**
  1. Record the Figure 2 day-0 risk counts.
  2. Compare with Figure 1 recipient and nonrecipient counts.
  3. If the curves use the primary-analysis groups, qualify or replace “received” in the caption.

### 3. “Prespecified” adherence subgroup overstates prespecification of its definitions

- **Category / severity:** Statistical reporting inconsistency / Minor
- **Issue:** The adherence subgroup is called preplanned/prespecified, although the supplement states that its high, moderate, and low definitions were not predefined.
- **Evidence:** `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF pp. 4-5, specifies the preplanned subgroup “high vs low enhanced recovery protocol adherence” and describes results as “prespecified subgroup analysis.” `JAMA-2024-23898-SUPP-03-RESULTS`, `joi240139supp3_prod_1741633738.18862.pdf`, PDF p. 2, eFigure title: “Prespecified Subgroup Analysis”; rows High `n=191`, Moderate `n=274`, Low `n=92`; footnote: the analysis “was pre-planned, however the definition of high, moderate and low were not pre-defined.”
- **Calculation / comparison:** `191 + 274 + 92 = 557`, the main article’s primary-analysis population. The displayed three-level operationalization differs from the stated high-versus-low subgroup, and its definitions are expressly not predefined.
- **Bounded impact:** Only the prespecification of the operational definitions is overstated; this does not establish that the adherence factor was wholly post hoc or that the interaction estimate is wrong.
- **Human verification:**
  1. Compare the high-versus-low language on main PDF pp. 4-5 with the three Supplement 3 categories.
  2. Confirm the supplement footnote’s “not pre-defined” statement.
  3. Check the dated subgroup specification; if thresholds were not set before analysis, qualify the prespecified claim accordingly.

### 4. “Right hemicolectomy” label includes extended right hemicolectomies

- **Category / severity:** Presentation inconsistency / Minor
- **Issue:** The supplement labels a subgroup “Right Hemicolectomy (n = 301),” but that total requires including the separately listed extended-right-hemicolectomy category.
- **Evidence:** `JAMA-2024-23898-SUPP-03-RESULTS`, `joi240139supp3_prod_1741633738.18862.pdf`, PDF p. 2, eFigure: “Right Hemicolectomy (n = 301).” `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF p. 4, Table 1: right hemicolectomy `137` IV plus `135` placebo; extended right hemicolectomy `10` plus `19`. The planned comparison on the same page is “right colectomy vs nonright colectomy.”
- **Calculation / comparison:** `137 + 135 = 272`; `10 + 19 = 29`; `272 + 29 = 301`. The eFigure total is 29 above the right-hemicolectomy row alone and corresponds to the broader right-colectomy group.
- **Bounded impact:** The subgroup label obscures inclusion of 29 extended procedures; no effect-estimate error is established.
- **Human verification:**
  1. Sum the two Table 1 right-sided procedure categories.
  2. Compare their total with eFigure `n=301`.
  3. Confirm the subgroup-programming definition and relabel it “Right colectomy” if it combines both categories.

### 5. Day-1 nausea percentage is misrounded

- **Category / severity:** Arithmetic inconsistency / Minor
- **Issue:** Table 2 reports `7/237` as `2.9%`, but this is `3.0%` when rounded to one decimal place.
- **Evidence:** `JAMA-2024-23898-MAIN`, `jama_paterson_2024_oi_240139_1741633738.12862.pdf`, PDF p. 6, Table 2, “Clinically important nausea and vomiting,” Day 1, IV lidocaine: `7/237 (2.9)`. Nearby Day 3 is `5/202 (2.5)`.
- **Calculation / comparison:** `100 × 7 ÷ 237 = 2.953586…%`, which rounds to `3.0%` at one decimal. Nearby `100 × 5 ÷ 202 = 2.475248…%`, printed as `2.5%`, supports nearest-one-decimal rounding rather than truncation. Difference: `0.1` percentage point.
- **Bounded impact:** One percentage cell is understated by 0.1 percentage point; the numerator, denominator, and substantive comparison remain unchanged.
- **Human verification:**
  1. Recalculate the Day-1 percentage using numerator 7 and denominator 237.
  2. Apply the table’s documented rounding rule.
  3. Amend to `3.0%` if nearest-one-decimal rounding applies, or document any nonstandard rule/denominator.

## Excluded / Uncertain Item

The Day-5 EQ-5D-5L narrative/table lead is excluded as **Uncertain**. Table 2 reports a time-specific adjusted effect of `−0.057 (95% CI, −0.111 to −0.003), P=.04` on main PDF p. 6, while the article gives blanket null wording. However, the supplied material does not provide the global longitudinal test or multiplicity rule needed to determine whether those statements are inconsistent. No conclusion is implied.
