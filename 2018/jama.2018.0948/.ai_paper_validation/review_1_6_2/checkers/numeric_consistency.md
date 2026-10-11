# Numeric consistency review — main-paper scope

Runtime ID: 01a129b7-ee71-7271-9299-3cf9a52ee2fb. Assigned scope: DOC-001 N001–N079, 79 relationships, all completed in `../relationships/numeric_relationship_inventory.md`. Source role REPORT. Distinct support-only numeric checks are in the separately assigned support shard; cross-document matching belongs to the cross-source checker. One finding and seven excluded-observation patterns. No old findings or report conclusions were read. No candidate IDs or adjudications are assigned here.

## Findings

### F-NUM-001

The main-secondary deterioration rate-difference interval includes zero while its displayed P value is significant.

- **Exact source locations and roles:** REPORT [main article PDF p.7 Table3, Significant clinical deterioration event row and footnotes a/f](../../../jama_parshuram_2018_oi_180015.pdf#page=7); repeated REPORT [p.1 abstract Results](../../../jama_parshuram_2018_oi_180015.pdf#page=1) and REPORT [p.6 Secondary Outcome paragraph](../../../jama_parshuram_2018_oi_180015.pdf#page=6). Relationships N053/N065/N074, statistical S011.
- **Printed inputs:** adjusted between-group rate difference −0.34 per1000 patient-days, 95% CI −0.73 to0.05; adjusted rate ratio0.77,95% CI0.61 to0.97; P=.03. Table3 footnote a states that the deterioration difference model was not adjusted for baseline values. Footnote f states that the Poisson ratio model adjusts baseline event rates and clusters by center. Methods p.5 uses two-sided significance .05. The abstract displays the difference, its interval, the ratio and its interval, then P=.03 together.
- **Rule and reproduced calculation:** the difference null is0. The reported difference interval has −0.73<0<0.05; P=.03<.05. The ratio null is1;0.61<0.77<0.97<1, so the ratio interval agrees with the P value. The difference interval and significant P do not express the same significance reading. Table3's separate model footnotes do not remove this route A category 1 observation; they are retained as an alternative attribution. Half-unit bounds on the displayed difference interval endpoints are [−0.735,−0.725] and[0.045,0.055], so every allowed interval contains0; the displayed P half-unit interval[.025,.035] remains below.05. The display-precision rule does not screen route A category 1 conflicts; relative discrepancy is not applicable to this inferential-null comparison.
- **Focus area:** B, estimate and test logic.
- **Proposed review domain:** statistical_results.
- **Proposed relationship type:** S_W; all compared locations are within the REPORT main article.
- **Qualifying route:** Route A, category 1.
- **Affected result or extracted value:** significance of the absolute main-secondary significant-clinical-deterioration rate difference, and interpretation of P=.03 beside −0.34 (−0.73 to0.05).
- **Why context does not resolve it:** route A category 1 explicitly retains interval/P observations when separate analyses are a possible explanation. A reader extracting the absolute difference with the displayed P obtains an interval including the null and a significant test reading.
- **Source-grounded alternatives and missing definition:** P=.03 may refer exclusively to the baseline-adjusted rate ratio rather than the absolute difference, which was calculated without baseline adjustment according to footnote a. This is supported by the ratio interval. No separate P value for the absolute difference or explicit restriction of the shared P column to ratios is printed. No reanalysis or preferred method is proposed.
- **Exact human question:** Does P=.03 apply only to the baseline-adjusted rate ratio, and which test reading should accompany the absolute rate difference −0.34 (95% CI −0.73 to0.05) in result extraction?
- **Direct-source confirmation:** current direct layout extraction read at pp.1,6,7; exact current source p.7 freshly CPU-rendered and visually inspected at `preprocessing/numeric-main-source-p7.png`. Values and model footnotes match the supplied source. Engine Poppler25.03.0; no OCR.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.1,9; N001 | Abstract and limitations call144539 discharges patients. Immediate abstract sentence explicitly identifies discharge count and the flow definition includes deaths/period-end inpatients; no competing exact unique-patient total is printed. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p.5 Table1 ICU overnight staff; N031–N033 | BedsidePEWS ICU physician categories2+5+1=8, with20+50+10=80%. Each individual count/percentage reconciles with10; the table never says every hospital has an ICU physician physically in-house overnight or that these categories exhaust all hospitals. Inferring a missing count requires an unprinted completeness assumption. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 pp.3,9 run-in descriptions; N011 | Figure specifies extensions of1,5,6 additional weeks while limitations says extended run-in lasting1,5,6 weeks. The immediate limitation refers to the same three extensions; the5-week standard run-in is printed explicitly. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 pp.6–8 adjusted results; N042–N049,N051–N063,N067–N068 | Adjusted mean/rate differences and ratios differ from crude between-group calculations; all are labeled adjusted, clustered, and often baseline-adjusted. Consolidated model-versus-crude observation covers all affected rows, including Table3 sign differences across separately adjusted ratio/difference models. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p.8 Figure2 x axis; N071 | X-axis label mentions baseline and intervention while caption expressly defines horizontal/vertical coordinates as baseline/intervention and vertical axis is intervention. Axis wording resolves within the figure and does not change a printed numeric value. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.8 Figure2 line descriptions; N072 | Caption assigns dashed orange to BedsidePEWS and solid blue to usual care, while plotted legend assigns them oppositely. This is a line-key attribution difference; the legend identifies each curve immediately, the caption prints both slopes, and no exact hospital result or quantitative extraction is reversed by this comparison. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.8 discussion; N073 | Prose excludes differences greater than0.8 in either direction although upper limit is0.81; prose one-decimal interval[.75,.85] overlaps limit two-decimal interval[.805,.815], discrepancy0, relative discrepancy0. | ROUNDING_OR_DISPLAY_PRECISION |

## Coverage and limitations

All79 numeric relationships were checked. Flow, randomized/received/analyzed totals, totals across groups, count/denominator/percentage pairs, event rates, narrative event sums, repeat counts, documentation totals and effect-measure labels were reviewed. Exact rate calculations and all per-ID outcomes are in the inventory. Every directly recomputable event rate and percentage reconciles. Each OR is identified with logistic modeling and each RR with Poisson rate modeling; none is presented as a crude risk ratio or rate difference.

Intervention ICU discharge denominators are not numerically printed in main Table3, so exact denominator extraction is unavailable here; consistency witnesses in the inventory show the two event/rate rows do not themselves conflict. Hospital graph coordinates are not exact labeled numeric inputs. Per-patient ICU denominators686/967 were read as contextual support; the separate support checker owns their complete review. These are limits of supplied numeric detail, not unchecked assigned relationships. No scientific coverage gap remains in the assigned main scope.
# Support numeric consistency checker

Runtime ID: 01a129b8-0e37-7521-8c6c-85aed6ede96e. Optional disjoint numeric shard, gpt-6.1-sol / medium, fresh spawn. Scope: all internal numeric relationships DOC-002 pp. 1–37 (PLAN), DOC-003 pp. 1–7 (PLAN), DOC-004 pp. 1–14 (REPORT), grouped in 93 records N080–N172 in relationships/parts/numeric_support_inventory.md. Main article relationships and source-to-source matching are separately assigned. Statistical inferential compatibility and printed SAP implementation are assigned to statistical specialists. Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely; used current source-linked mapper evidence and targeted direct source extraction, no legacy scientific conclusion or external evidence.

## Methods and complete check coverage

Direct tools: Poppler pdftotext 25.03.0 layout extraction of DOC-004 pp. 1–7 and 8–14, DOC-003 pp. 1–7, DOC-002 pp. 14–15 and 29–30. Derivatives: preprocessing/numeric-support-results-p1-7.txt, preprocessing/numeric-support-results-p8-14.txt, preprocessing/numeric-support-sap.txt, preprocessing/numeric-support-protocol-p14-15.txt, preprocessing/numeric-support-protocol-p29-30.txt. Direct visual confirmation of DOC-002 p. 29 used Poppler pdftoppm 25.03.0, CPU, 100 dpi, preprocessing/numeric-support-protocol-p29.png. The package tooling record establishes native text and rendering available; no OCR, fallback interpreter, source modification, or reused-asset modification occurred.

All 21 hospital rows and both arm totals in eTable 2 and eTable 3 were checked. Exact eTable 2 totals reproduced:
- PEWS discharges 26664/50173/76837; mortality 52/97; non-DNR mortality 26/42.
- Usual care discharges 46718/94366/141084; mortality 61/147; non-DNR mortality 16/47.
- Every hospital baseline+post discharge count equals its printed total; every mortality count/rate reconciles; non-DNR counts never exceed total deaths.

Exact eTable 3 totals reproduced:
- PEWS patient-days 129700/251859; deterioration 80/127; arrest 15/27; potentially preventable arrest 11/21.
- Usual care patient-days 162497/307584; deterioration 144/259; arrest 18/32; potentially preventable arrest 12/29.
- All six event-rate cells per hospital and per total satisfy half-unit precision; potentially preventable arrest ≤ arrest ≤ deterioration in both periods.

eTable 4: patient denominators 393/686/531/967; every mortality, predicted mortality and technology-use count/percentage checked in all four groups; all 15 effect identities agree with linear mean-difference or binomial identity risk-difference methods. Four median/IQR rows, all mean/SD summaries, ICU aggregation, VFD 0–28 and PELOD 0–71 ranges checked. All point estimates lie within properly ordered 95% intervals; inferential compatibility reviewed independently by the statistical agents. No crude-column subtraction was used to dispute adjusted effects.

eTable 5: anticipated deaths 99389×5.1/1000 = 506.8839 → 507; anticipated deterioration events 397556×2/1000 = 795.112 → 795. Actual 244/144539×1000 = 1.68813 → 1.7 and 386/559443×1000 = 0.689972 → .69. Actual discharges 50173+94366 = 144539; actual patient-days 251859+307584 = 559443; actual events 97+147 = 244 and 127+259 = 386. Coefficient/standard-deviation comparison satisfies half-unit intervals, as detailed in N170. Figure documentation caption 2588+2832 = 5420; hospital identifiers 10+11 = 21. No exact histogram frequencies were fabricated from unlabeled bars.

Protocol: all current support map quantities reviewed; 686+1388 = 2074 historical validation patients; 14 historical hospital mortality rates average 5.10643 → 5.11; 397556/99389 = 4 days LOS; .31×2 = .62 SCDE reduction; .41×.75 = .3075 → .3 code-blue reduction. Statistical agents own sample-size model reproduction and planned-versus-reported design comparisons. One reproduced protocol numeric inconsistency remains below.

## Findings

### F-NUM-101

**Title:** Protocol mortality absolute reduction printed as 0.9% in the appendix versus 0.09% in the power specification.

**Relationship inventory:** N087.  
**Compared locations and roles:** PLAN DOC-002 [PDF p. 29, Power & Sample Size Appendix, all-cause mortality paragraph](../../../joi180015supp1_prod.pdf#page=29); PLAN DOC-002 [PDF p. 14, section 2.11 Sample size and assumptions](../../../joi180015supp1_prod.pdf#page=14); PLAN DOC-002 [PDF p. 1, mortality power summary](../../../joi180015supp1_prod.pdf#page=1). Both compared locations are prospective PLAN content. Within one protocol, provisional relationship type P_P; all relationships P_P; proposed review domain plan_material. No classification ambiguity.

**Printed inputs:** Appendix p. 29: 18% relative risk reduction corresponds to absolute risk reduction 0.9%; same page baseline 5.1 deaths/1000 discharges. Section 2.11 p. 14: 18% relative risk reduction, absolute risk reduction 0.09%, baseline 5.1/1000. Summary p. 1 uses 0.9 deaths/1000 admissions, corroborating the smaller percentage scale. Shared inputs are 20-hospital power base, alpha .05 and power 80%.

**Rule and calculation:** Convert deaths per thousand to a percentage, then multiply by relative reduction. 5.1×.18/10 = .0918% absolute reduction. With printed baseline half-unit [5.05,5.15]/1000 and relative reduction [17.5%,18.5%], the recomputed absolute-percentage interval is [.088375%,.095275%]. Printed .9% has half-unit interval [.85%,.95%]; minimum gap = .85−.095275 = .754725 percentage points; relative discrepancy = .754725/.9 = .8385833, above .05. For the two printed percentage copies, .09% has interval [.085%,.095%], so minimum gap to .9% is .755 percentage points, relative discrepancy .755/.9 = .8388889. The appendix absolute reduction also exceeds its stated baseline risk .51%, establishing the differing magnitude independently.

**Focus area:** D, power assumptions for primary hospital mortality.  
**Qualifying route:** Route A, category 2.  
**Affected result or extracted value:** The absolute mortality reduction underlying the planned primary-outcome power calculation: a reader may extract .9% from the appendix or .09% from the main power specification.  
**Why context does not resolve it:** Route A category 2 applies to the reproduced decimal/scale discrepancy that changes the printed magnitude. The smaller percentage is reconstructible, but the explicitly printed appendix quantity remains a distinct extractable power input.  
**Alternative interpretations:** The appendix may intend .9 deaths per thousand (approximately .09%) while displaying a percent sign, or may intend a different absolute-reduction scenario. The latter does not reconcile with the same paragraph’s 18% relative reduction and the printed baseline mortality. No different scenario or amendment is disclosed there.  
**Exact human question:** Which absolute mortality reduction was intended for the appendix’s 18% power scenario, and how should the printed .9% be reconciled with .09% in section 2.11 and .9 deaths per thousand in the summary?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p.11, eTable 3, low event-rate cells: E post arrest/PP; F post PP; H post arrest and baseline/post PP; I baseline arrest and baseline/post PP; J baseline/post arrest and baseline/post PP; O baseline arrest/PP and post PP; Q baseline PP; T baseline PP | Some crude relative differences from two-decimal rates exceed .05 before allowing displayed precision. Every exact quotient falls within its printed rate’s ±.005 interval; half-unit input intervals broaden this overlap. Examples 1/17779×1000=.056246 lies within .06±.005; 1/28698×1000=.034846 lies within .03±.005. Remaining discrepancy zero. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p.30, Stat Calls power paragraph | 8.13×.181=1.47153 versus printed1.45. Half-unit product interval[1.4665625,1.4765025], output[1.445,1.455], gap.0115625; relative gap.00797414≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 pp.7,13, PIM2 upper illustrative probability | Inverse-logit(+9.7778)×100 = 99.99433072% versus99.9%. The rounded input interval gives approximately[99.99433044%,99.99433100%]; output[99.85%,99.95%]; gap .04433044/99.9 = .00044375≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p.30, Code Blue power paragraph | Wording repeats the per-thousand scale in “0.3/1000 events per thousand patient days”; printed .75 rate and .41 reduction immediately determine about .3 events/1000. The arithmetic and intended scale are clear. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p.12, eTable 4 exclusion caption | 55(3.2%) has no explicit percentage denominator. Using the post-period population before exclusion,1653+55=1708, yields3.22014%. Assuming all baseline+post patients instead would be unsupported; no printed denominator conflicts. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 pp.12–13, eTable 4 effect column | Several adjusted differences differ from crude descriptive-column subtraction (for example total ICU LOS9.4−9.0=.4 versus1.28). Hospital-baseline-adjusted GEE is explicitly used; no effect is stated crude. | MODEL_VERSUS_CRUDE |
| REPORT DOC-004 p.11, eTable 3 PEWS baseline deterioration total | Additional glyph after80 does not alter the count: individual rows sum80 and80/129700×1000=.616808 rounds.62; typography makes the numeric reading clear. | NOTATION_OR_TYPOGRAPHY |

## Completion and limitations

93 support relationships complete, 1 finding, 7 excluded-observation patterns. No scientific coverage limitation. Raw patient records and fitted GEE output are not supplied; this limits reproduction of model-based means/effects but does not prevent checking all supplied numeric relationships. Figure bars are unlabeled; only truthful approximate visual values from the current map were used as context. Candidate IDs and human adjudication are reserved to downstream stages.


## Canonical numeric-check merge

The coordinator merged two disjoint completed shards without loss: main N001-N079 (79 relationships) and support N080-N172 (93 relationships). Total: 172 numeric relationships, two findings (F-NUM-001 and F-NUM-101), 14 excluded-observation patterns. Both original shard scopes remain represented in their durable records. Relative links in the appended support text were adjusted for this canonical file's directory.
