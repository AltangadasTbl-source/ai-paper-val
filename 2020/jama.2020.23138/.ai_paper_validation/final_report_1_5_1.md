# Quantitative Quality-Control Consistency Review — JAMA 2020.23138

## Pending Human Adjudication

Every observation in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination of paper validity or a conclusion-level finding.

## Executive Quality-Control Summary

Complete source coverage and two statistical passes produced 14 stable, source-linked reporting-consistency candidates (C001-C014). The candidates are small, preventable defects or ambiguities that may matter if confirmed because a downstream evidence extractor, systematic review, meta-analysis, or guideline could copy an inconsistent number, label, time point, or direction. This report does not assert that propagation occurred, that any pooled result changed, or that the paper's conclusions changed.

## Package and Reused-Evidence Provenance

The package contains five supplied PDFs: the main article (12 pages), protocol (69), statistical analysis plan (45), results supplement (20), and data-sharing statement (1). Native reusable page text covered all 12 main-article pages and all 20 results-supplement pages. The remaining 115 pages received fresh direct-source mapping. Reused text and rendered material were used as locators and transcription aids; candidate evidence was mechanically rechecked against the cited source PDF pages.

## Scope, Complete Coverage, and Exclusions

All 147 direct-source PDF-page units were mapped: 32 reusable-backed and 115 fresh-required. No direct DOC, DOCX, workbook, or CSV source was present. The review covered numeric, denominator, statistical, cross-document, label/scale, and rate/count relationships. Coherent display-zero P values alone were excluded; no candidate was created for display-zero formatting alone. There was no review queue, top-N subset, deferred-by-cap section, ranking, or candidate limit.

## Quantitative and Statistical Relationship Coverage

The complete relationship inventory contains 125 numeric relationships and 90 inferential-statistical relationships. Both independent statistical passes are recorded as `PASS_1_COMPLETE` and `PASS_2_COMPLETE`. Candidate discovery, mechanical recheck, and quality audit all retain the same stable ID set: C001-C014.

## Candidate Index

| ID | Candidate |
|---|---|
| C001 | Randomized total differs between the flow diagram and article population |
| C002 | Baseline digoxin NT-proBNP summaries differ between main Tables 1 and 3 |
| C003 | Baseline digoxin 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2 |
| C004 | Baseline digoxin apical heart-rate mean differs between main Table 1 and eTable 2 |
| C005 | Baseline digoxin radial-pulse SD differs between main Table 1 and eTable 2 |
| C006 | Protocol assigns both PCS and physical-functioning labels to the primary endpoint |
| C007 | Protocol outcome wording says BNP while assay and results say NT-proBNP |
| C008 | SAP AFEQT template footnote calls the scale a visual-analogue score |
| C009 | SAP reverses the favorable direction for E/e-prime |
| C010 | SAP NT-proBNP heading says six months but its table includes a 12-month row |
| C011 | SAP EHRA example uses an undefined class 3a |
| C012 | SAP ambulatory-HR template uses monitor duration where the visit time point is expected |
| C013 | Results-supplement heart-rate table describes higher values as better quality of life |
| C014 | Main Table 3 uses a universal higher-is-better footnote for lower-is-better measures |

## Candidate Evidence Cards

## C001 — Randomized total differs between the flow diagram and article population

**Candidate statement:** Figure 1 prints 161 randomized, while the article population is 160; the source also prints a replacement explanation that narrows the question to clear population labeling.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 1](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=1>), [PDF p. 3](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=3>), and [PDF p. 4](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4>).

**Source evidence:** Figure 1 prints 551 assessed, 390 excluded, and 161 randomized; its treatment boxes show 80 in each arm. The abstract and Results describe 160 participants. Page 4 states that one randomized person did not complete baseline assessment or start treatment and was replaced to maintain sample size.

**Reported-versus-comparator:** 161 initial randomized events versus 160 participants in the replacement-maintained treated/full-analysis cohort.

**Reasoning procedure:** Compare the flow totals, arm totals, and page-4 replacement statement; distinguish direct printed facts from the inferred population labels.

**Calculation:** `551 - 390 = 161`; `80 + 80 = 160`; `161 - 1 = 160`.

**Alternative source-grounded interpretations:** 161 may be initial allocation events including the pretreatment withdrawal, whereas 160 may be the replacement-maintained treated/full-analysis cohort; the figure does not explicitly label that distinction.

**Mechanical evidence recheck:** Locations and printed totals were found; the arithmetic and replacement explanation were reproduced. Missing are the withdrawn participant's allocated arm, whether the replacement is included in the 161 node, and the intended technical population labels.

**Quality-control relevance:** The flow diagram and population wording could be made more explicit even though the supplied source provides a plausible reconciliation.

**Potential downstream evidence impact:** If confirmed, an extractor could copy 161 or 160 as the trial population without recognizing the distinct population definitions; no conclusion change is established.

**Human verification steps:** Confirm the intended definition of randomized, treated, and full-analysis populations and whether the figure should show the replacement pathway.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Baseline digoxin NT-proBNP summaries differ between main Tables 1 and 3

**Candidate statement:** Repeated baseline digoxin NT-proBNP summaries with displayed n=80 differ between Tables 1 and 3.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 5](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>), [PDF p. 6](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>), and [PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).

**Source evidence:** Table 1 and narrative print 1095 (IQR 715-1527) pg/mL; Table 3 prints 1091 (710-1522) pg/mL for baseline digoxin, n=80.

**Reported-versus-comparator:** 1095 (715-1527) versus 1091 (710-1522) pg/mL.

**Reasoning procedure:** Compare the named analyte, arm, baseline time point, displayed denominator, unit, and summary convention.

**Calculation:** Median difference `1095 - 1091 = 4` pg/mL; IQR endpoint differences `715 - 710 = 5` and `1527 - 1522 = 5` pg/mL.

**Alternative source-grounded interpretations:** An unstated analytic subset, data freeze, or median/IQR convention may differ.

**Mechanical evidence recheck:** Both table cells and narrative repetition were found and calculations reproduced; participant-level data, quartile convention, and table-freeze history are unavailable.

**Quality-control relevance:** Repeated baseline summaries should identify any differing dataset or convention.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either baseline NT-proBNP triple; no effect on the paper's conclusions is established.

**Human verification steps:** Establish whether the tables use the same 80 measurements and the same summary convention, then identify the intended printed triple.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Baseline digoxin 12-lead ECG heart-rate mean differs between main Table 1 and eTable 2

**Candidate statement:** Matched baseline digoxin 12-lead ECG means differ across the main article and results supplement.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 5](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>) and [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp3_prod_1607962892.5372.pdf#page=14>).

**Source evidence:** Main Table 1 prints 100.1 (16.8) /min; eTable 2 prints 100.3 (16.8) beats/min, both for baseline digoxin n=80. Main Table 3 repeats 100.3 (16.8).

**Reported-versus-comparator:** 100.1 (16.8) versus 100.3 (16.8) beats/min.

**Reasoning procedure:** Match arm, baseline time, 12-lead ECG measure, denominator, and SD before comparing the one-decimal means.

**Calculation:** `100.3 - 100.1 = 0.2` beats/min.

**Alternative source-grounded interpretations:** Separate table freezes, ECG processing definitions, or an unlabelled subset may explain the values.

**Mechanical evidence recheck:** Both cells and n=80 were found; the displayed difference was reproduced. Processing rules, source dataset, and table-version history are absent.

**Quality-control relevance:** This is a distinct 12-lead ECG mean cell, not the apical or radial-pulse cell in C004-C005.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either one-decimal baseline ECG mean; no adjusted-effect or conclusion change is established.

**Human verification steps:** Confirm whether both cells summarize the same 80 ECG measurements and identify the intended mean.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Baseline digoxin apical heart-rate mean differs between main Table 1 and eTable 2

**Candidate statement:** Matched baseline digoxin 30-second apical heart-rate means differ across the main article and results supplement.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 5](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>) and [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp3_prod_1607962892.5372.pdf#page=14>).

**Source evidence:** Main Table 1 prints 98.2 (15.1) /min; eTable 2 prints 98.3 (15.1) beats/min, both baseline digoxin n=80.

**Reported-versus-comparator:** 98.2 (15.1) versus 98.3 (15.1) beats/min.

**Reasoning procedure:** Match the 30-second apical assessment, arm, time, denominator, and SD.

**Calculation:** `98.3 - 98.2 = 0.1` beats/min.

**Alternative source-grounded interpretations:** Independent rounding inputs, a distinct source statistic, or an unlabelled measurement/subset distinction may exist.

**Mechanical evidence recheck:** Both cells were found and the difference reproduced; participant set, rounding rule, and table history are not supplied.

**Quality-control relevance:** This is a separate apical mean relationship from C003 and C005.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either apical mean; no treatment-effect or paper-conclusion impact is established.

**Human verification steps:** Verify whether the cells derive from the same 80 apical assessments and which mean is intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Baseline digoxin radial-pulse SD differs between main Table 1 and eTable 2

**Candidate statement:** The SD for matched baseline digoxin radial-pulse data differs across the main article and results supplement.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 5](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=5>) and [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp3_prod_1607962892.5372.pdf#page=14>).

**Source evidence:** Main Table 1 prints 87.8 (12.1) /min; eTable 2 prints 87.8 (12.0) beats/min, both baseline digoxin n=80.

**Reported-versus-comparator:** SD 12.1 versus 12.0 beats/min, with the same displayed mean 87.8.

**Reasoning procedure:** Match the radial-pulse cell by arm, baseline time, denominator, unit, and mean before comparing the SD.

**Calculation:** `12.1 - 12.0 = 0.1` beats/min.

**Alternative source-grounded interpretations:** A table refresh, SD convention, independently computed values, or an unstated subset may explain the difference.

**Mechanical evidence recheck:** Both cells and n=80 were found; the SD difference was reproduced. The source lacks calculation inputs and SD-convention details.

**Quality-control relevance:** This is a separate radial-pulse SD relationship from the two mean discrepancies in C003-C004.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either radial-pulse SD; no adjusted-effect or conclusion change is established.

**Human verification steps:** Confirm common observations and SD convention, then identify the intended SD.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Protocol assigns both PCS and physical-functioning labels to the primary endpoint

**Candidate statement:** Protocol primary-endpoint wording alternates between the SF-36 physical component summary (PCS) and the physical-functioning domain, while the SAP and article identify PCS.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp1_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp1_prod_1607962892.5372.pdf#page=14>), [PDF p. 21](<../joi200126supp1_prod_1607962892.5372.pdf#page=21>), [PDF p. 22](<../joi200126supp1_prod_1607962892.5372.pdf#page=22>), [PDF p. 54](<../joi200126supp1_prod_1607962892.5372.pdf#page=54>), [PDF p. 56](<../joi200126supp1_prod_1607962892.5372.pdf#page=56>), [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 18](<../joi200126supp2_prod_1607962892.5372.pdf#page=18>), and [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 6](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>).

**Source evidence:** Protocol pp.14/22/54 name six-month PCS; pp.21/56 call the primary measure physical functioning. The SAP and article identify PCS, while physical functioning is separately reported.

**Reported-versus-comparator:** PCS versus physical-functioning domain as the named primary endpoint.

**Reasoning procedure:** Compare the endpoint labels across protocol, SAP, and article; the rule is measure-label identity rather than arithmetic.

**Calculation:** Not applicable; this is a label-identity comparison.

**Alternative source-grounded interpretations:** Physical-functioning wording may be drafting carryover or a superseded label; amendment history is not supplied.

**Mechanical evidence recheck:** Each cited statement was found. The package does not supply amendment history or an explicit statement equating the two measures.

**Quality-control relevance:** Primary-outcome naming should distinguish PCS from the separately reported physical-functioning domain.

**Potential downstream evidence impact:** If confirmed, an extractor could classify the primary endpoint as PCS or physical functioning; no change to the reported PCS estimate or paper conclusion is established.

**Human verification steps:** Confirm the intended primary endpoint throughout and whether protocol pp.21/56 require clarification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Protocol outcome wording says BNP while assay and results say NT-proBNP

**Candidate statement:** Protocol outcome lists say BNP while the protocol assay, SAP, and reported result identify NT-proBNP.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp1_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp1_prod_1607962892.5372.pdf#page=14>), [PDF p. 22](<../joi200126supp1_prod_1607962892.5372.pdf#page=22>), [PDF p. 41](<../joi200126supp1_prod_1607962892.5372.pdf#page=41>), [PDF p. 54](<../joi200126supp1_prod_1607962892.5372.pdf#page=54>), [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 40](<../joi200126supp2_prod_1607962892.5372.pdf#page=40>), and [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).

**Source evidence:** The protocol outcome lists use BNP; its assay section identifies NT-proBNP; the SAP uses BNP (NTproBNP); and the article reports NT-proBNP.

**Reported-versus-comparator:** BNP outcome wording versus NT-proBNP assay, SAP, and results wording.

**Reasoning procedure:** Compare the printed analyte labels. The supplied sources do not declare the labels interchangeable, and no numeric conversion is the rule.

**Calculation:** Not applicable; this is an analyte-label comparison.

**Alternative source-grounded interpretations:** BNP may have been used as informal peptide-family shorthand, but the package does not say so.

**Mechanical evidence recheck:** Relevant locations and labels were found. Protocol PDF page 15 contains no BNP or NT-proBNP evidence and is not used here.

**Quality-control relevance:** Outcome and assay terminology should consistently identify the analyte.

**Potential downstream evidence impact:** If confirmed, an extractor could classify the biomarker as BNP rather than NT-proBNP; no numeric-result or conclusion change is established.

**Human verification steps:** Confirm the intended biomarker outcome and whether the protocol outcome lists should be standardized.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — SAP AFEQT template footnote calls the scale a visual-analogue score

**Candidate statement:** An SAP template headed AFEQT overall score applies a footnote calling its 0-100 range a visual analogue score.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 17](<../joi200126supp2_prod_1607962892.5372.pdf#page=17>), [PDF p. 19](<../joi200126supp2_prod_1607962892.5372.pdf#page=19>), [PDF p. 36](<../joi200126supp2_prod_1607962892.5372.pdf#page=36>), [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>), and [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 16](<../joi200126supp3_prod_1607962892.5372.pdf#page=16>).

**Source evidence:** The SAP defines AFEQT and headings name AFEQT overall score; the p.36 footnote says visual analogue score. EQ-5D VAS is separately named.

**Reported-versus-comparator:** AFEQT overall score versus visual analogue score label.

**Reasoning procedure:** Compare the measure names and table context; a shared 0-100 range does not establish measure identity.

**Calculation:** Not applicable; shared numerical range is not an identity calculation.

**Alternative source-grounded interpretations:** The footnote may have been copied from the preceding EQ-5D VAS template.

**Mechanical evidence recheck:** The AFEQT heading and footnote were found. The package does not document why the footnote appears in that template.

**Quality-control relevance:** The table footnote should name the measure it describes.

**Potential downstream evidence impact:** If confirmed, an extractor could mislabel AFEQT as a visual-analogue measure; no paper-conclusion effect is established.

**Human verification steps:** Verify the intended AFEQT score anchors and replace or clarify the footnote if needed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — SAP reverses the favorable direction for E/e-prime

**Candidate statement:** Two SAP statements give opposed favorable-direction rules for the E/e-prime contrast.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 20](<../joi200126supp2_prod_1607962892.5372.pdf#page=20>), [PDF p. 37](<../joi200126supp2_prod_1607962892.5372.pdf#page=37>), and [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).

**Source evidence:** SAP p.20 states lower E/e-prime is better; p.37 says higher values and a positive difference favor digoxin. The reported adjusted difference is -0.1 (-1.1 to 0.9).

**Reported-versus-comparator:** Lower/negative favorable versus higher/positive favorable for the same digoxin-minus-bisoprolol contrast.

**Reasoning procedure:** Compare the two direction rules; they cannot both define the favorable direction for that signed contrast.

**Calculation:** Not applicable; the reported -0.1 interval is contextual and internally coherent, not an arithmetic contradiction.

**Alternative source-grounded interpretations:** The p.37 sentence may be generic higher-is-better boilerplate.

**Mechanical evidence recheck:** Both direction statements and the reported estimate were found; no source says that the fitted model or conclusion was reversed.

**Quality-control relevance:** C009 concerns the two opposed SAP statements and is distinct from C014's main-table footnote scope.

**Potential downstream evidence impact:** If confirmed, an extractor could reverse favorable-direction coding for E/e-prime; no observed reversal or conclusion change is established.

**Human verification steps:** Confirm the intended E/e-prime direction wording on SAP p.37.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C010 — SAP NT-proBNP heading says six months but its table includes a 12-month row

**Candidate statement:** The SAP NT-proBNP table heading says “at 6 months” while the displayed template includes baseline, 6-month, and 12-month rows.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 17](<../joi200126supp2_prod_1607962892.5372.pdf#page=17>), [PDF p. 21](<../joi200126supp2_prod_1607962892.5372.pdf#page=21>), [PDF p. 40](<../joi200126supp2_prod_1607962892.5372.pdf#page=40>), and [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>).

**Source evidence:** SAP p.40 is headed NT-proBNP “at 6 months” but displays baseline, 6-month, and 12-month rows. SAP p.21 plans both follow-ups and the article reports both.

**Reported-versus-comparator:** A six-month-only heading versus a table containing a 12-month row.

**Reasoning procedure:** Compare the follow-up set named by the heading with the displayed row labels and stated analysis plan.

**Calculation:** Not applicable; pg/mL and ng/L are equivalent-unit context, not an independent contradiction or a second candidate.

**Alternative source-grounded interpretations:** The title may be an unrevised template heading; the evidence does not show that the 12-month result was unplanned or omitted.

**Mechanical evidence recheck:** Heading, rows, plan, and article result were found; the mismatch is limited to the time heading.

**Quality-control relevance:** Table headings should identify all displayed follow-up time points.

**Potential downstream evidence impact:** If confirmed, an extractor could miss or misclassify the planned 12-month NT-proBNP row; no numeric-effect or conclusion change is established.

**Human verification steps:** Confirm whether p.40 should name both 6- and 12-month NT-proBNP analyses.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C011 — SAP EHRA example uses an undefined class 3a

**Candidate statement:** An SAP example uses EHRA class 3a although the same page defines the set as 1, 2a, 2b, 3, and 4.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 18](<../joi200126supp2_prod_1607962892.5372.pdf#page=18>).

**Source evidence:** The SAP defines modified EHRA classes `{1, 2a, 2b, 3, 4}` and illustrates two-class improvement with “3a” to 2a.

**Reported-versus-comparator:** Example class 3a versus the explicitly defined category set.

**Reasoning procedure:** Apply set membership: `3a` is not among the printed classes.

**Calculation:** `3a ∉ {1, 2a, 2b, 3, 4}`.

**Alternative source-grounded interpretations:** “3a” may be a typographic substitution for class 3; that is inferred, not directly declared.

**Mechanical evidence recheck:** Definition and example were found. The source does not say whether any realized result used class 3a.

**Quality-control relevance:** An example implementing a binary-improvement rule should use a defined category.

**Potential downstream evidence impact:** If confirmed, an implementer could copy an undefined EHRA category into the binary-improvement rule; no reported-result or conclusion change is established.

**Human verification steps:** Confirm whether the example intended baseline EHRA class 3 and clarify it if needed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C012 — SAP ambulatory-HR template uses monitor duration where the visit time point is expected

**Candidate statement:** The SAP ambulatory-heart-rate row uses `24-hour` in a `Time point` cell, while the result is labeled end uptitration; the recheck confirms this is not a baseline-placement issue.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 20](<../joi200126supp2_prod_1607962892.5372.pdf#page=20>), [PDF p. 38](<../joi200126supp2_prod_1607962892.5372.pdf#page=38>), and [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 9](<../joi200126supp3_prod_1607962892.5372.pdf#page=9>).

**Source evidence:** SAP p.20 says the 24-hour ambulatory measure is collected once with no baseline score. Direct visual recheck of p.38 shows `24-hour` in the ambulatory row's `Time point` cell; the nearby Baseline cell belongs to the separate 12-lead ECG section. The results supplement labels the measure end uptitration.

**Reported-versus-comparator:** `24-hour` monitor duration in the Time point cell versus the end-uptitration visit label.

**Reasoning procedure:** Interpret the column heading as visit timing and distinguish monitor duration from a visit label; this is a narrowed source-grounded question, not a claim of known timing error.

**Calculation:** Not applicable.

**Alternative source-grounded interpretations:** The template may intentionally use duration in that column while leaving visit timing implicit.

**Mechanical evidence recheck:** Direct visual inspection confirmed the `24-hour` cell and corrected the stale baseline-placement premise. No explicit SAP declaration explains the intended column use.

**Quality-control relevance:** Timing and duration labels should be distinguishable for structured data extraction.

**Potential downstream evidence impact:** If confirmed, an extractor could label monitor duration as the assessment visit or omit end uptitration; no numerical or conclusion effect is established.

**Human verification steps:** Determine whether p.38 should identify end uptitration in the Time point cell rather than repeat monitor duration.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C013 — Results-supplement heart-rate table describes higher values as better quality of life

**Candidate statement:** A results-supplement heart-rate table in beats/min carries a footnote stating that higher values represent better quality of life.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi200126supp3_prod_1607962892.5372.pdf — PDF p. 14](<../joi200126supp3_prod_1607962892.5372.pdf#page=14>), [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 4](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=4>), and [PDF p. 6](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>).

**Source evidence:** eTable 2 contains beats/min outcomes and footnote a says higher values represent better quality of life in the digoxin arm. The same clause appears on an AFEQT quality-of-life table on supplement p.16.

**Reported-versus-comparator:** Heart-rate measure in beats/min versus quality-of-life direction language.

**Reasoning procedure:** Compare the measure unit and table identity with the footnote language; no supplied definition equates heart rate with a QoL scale.

**Calculation:** Not applicable.

**Alternative source-grounded interpretations:** The clause may be copied from QoL eTables and may only have intended to state contrast direction.

**Mechanical evidence recheck:** The heart-rate table and footnote were found. The evidence does not establish that a heart-rate effect was interpreted incorrectly elsewhere.

**Quality-control relevance:** A footnote should describe the measure in the table where it appears.

**Potential downstream evidence impact:** If confirmed, an extractor could misclassify a heart-rate contrast as a quality-of-life interpretation; no paper-conclusion effect is established.

**Human verification steps:** Confirm whether the QoL clause should be removed or replaced with a heart-rate-specific direction statement.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C014 — Main Table 3 uses a universal higher-is-better footnote for lower-is-better measures

**Candidate statement:** Main Table 3 applies an unqualified higher-is-better footnote while including NYHA score and E/e-prime, which supplied text defines as lower-is-better.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_kotecha_2020_oi_200126_1607962892.52158.pdf — PDF p. 6](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=6>), [PDF p. 7](<../jama_kotecha_2020_oi_200126_1607962892.52158.pdf#page=7>), and [joi200126supp2_prod_1607962892.5372.pdf — PDF p. 20](<../joi200126supp2_prod_1607962892.5372.pdf#page=20>).

**Source evidence:** Table 3 footnote b says higher values indicate better response with digoxin; the table includes NYHA score and E/e-prime, for which supplied text defines lower values as better. Their printed adjusted differences are -0.6 and -0.1.

**Reported-versus-comparator:** Universal higher-is-better footnote versus lower-is-better directions for NYHA and E/e-prime.

**Reasoning procedure:** Test the scope of the unqualified footnote across all listed measures. This is distinct from C009, which compares opposed SAP statements for E/e-prime.

**Calculation:** Unadjusted NYHA means give `1.5 - 2.0 = -0.5`, directionally consistent with adjusted -0.6; the adjusted/unadjusted difference is not a candidate.

**Alternative source-grounded interpretations:** The footnote may have been intended only for applicable higher-is-better outcomes, but its scope is not delimited.

**Mechanical evidence recheck:** The footnote, lower-is-better context, and estimates were found. The evidence does not establish that every Table 3 row or fitted result is directionally reversed.

**Quality-control relevance:** Mixed-direction outcome tables need measure-specific direction statements or clear exceptions.

**Potential downstream evidence impact:** If confirmed, an extractor could assign the wrong favorable direction to lower-is-better rows; no conclusion change is established.

**Human verification steps:** Confirm whether Table 3 should limit the higher-is-better statement and explicitly state lower-is-better exceptions.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a human confirms a candidate, the immediate risk is limited to downstream copying of a population total, baseline summary, endpoint/analyte label, direction convention, or time-point label. Systematic reviewers, meta-analysts, guideline authors, and other extractors may benefit from resolving such details before reuse. The supplied package does not establish any actual propagation, effect on a pooled estimate, guideline impact, clinical impact, or change in the paper's conclusions.

## Limitations and Missing Definitions

The supplied package contains no participant-level data, table-generation programs, protocol/SAP amendment history, table-freeze history, or complete inferential implementation details. Exact reconstruction can be limited by missing degrees of freedom, variance estimator, covariance, sidedness, realized model route, and estimand mapping. These gaps are retained as candidate-specific human questions. The recheck also corrected two nuances: C001 has a printed replacement explanation, and C012's `24-hour` cell is not under Baseline. Current evidence supports neutral reporting-consistency questions only.

## Human Adjudication Checklist

- Confirm each candidate against the cited source PDF page(s).
- Decide whether the stated comparator and rule apply to the intended population, measure, time point, model, or table version.
- Record validity, importance, action, initials, and notes in every card.
- If a correction is adopted, preserve the original location and document the authoritative replacement outside this review report.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Source and reused-evidence inventories, coverage records, relationship inventories, checker outputs, mechanical recheck, and quality audit are retained under [review_1_5_1](<review_1_5_1/>). Source coverage is complete for all five direct PDF sources. This Markdown report was assembled from the stable candidate ledger and canonical review artifacts; direct-source links above are relative to `.ai_paper_validation/` and end in the applicable PDF page anchor.

### Agent execution

The execution manifest records the coordinator, reuse curator, four mappers, numeric and cross-source reviewers, two distinct high-effort statistical-pass agents, evidence rechecker, quality auditor, and report generator: [agent_execution_manifest.md](<review_1_5_1/agent_execution_manifest.md>).

### Performance

- **Target basis:** Five supplied PDFs contain 147 pages requiring complete mapping; reusable page-level quantitative text exists for the 12-page main article and 20-page results supplement, while protocol, SAP, and data-sharing pages require fresh direct-source inspection. The package is larger than the 102-unit calibration example but has a comparable reusable native-text pathway and no workbook or CSV complexity.
- **Total source units:** 147
- **Fresh-source units:** 115
- **Target elapsed minutes:** 50-75
- **Started UTC:** 2026-08-18T23:23:00Z
- **Finished UTC:** 2026-08-19T00:01:21Z
- **Observed elapsed minutes:** 38.4
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 known; complete estimate __ |

Authoritative response-level runtime token counts were not exposed for any manifested agent, so the known token subtotal is 0 while the complete total and price remain explicitly unavailable rather than estimated. Cached input and cache-write counts are input subsets, and reasoning counts are output subsets; none is added again to package totals. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not invoices. Per-agent detail is retained in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>).
