# Numeric consistency review — Workflow 1.6.2

Status: COMPLETE. Exact scope: DOC-001 REPORT physical PDF pages 1–10; DOC-002 PLAN physical PDF pages 1–45; DOC-003 REPORT physical PDF pages 1–36; every count, denominator, percentage, subtotal, model-versus-crude distinction, and effect-measure identity component in the complete mapped union. The stable inventory contains 104 groups, N001–N104, including all 96 mapper numeric records and eight numeric cross-references to inferential displays. No older scientific conclusions or external evidence were used.

All observations were self-screened against QUALITY_CONTROL_SCOPE.md. Integer participant counts are exact, and findings remain above the threshold even if their inputs are conservatively allowed half a displayed unit. Percentages and intervals allow their own half-unit rounding intervals. Grouped findings preserve every affected location. No candidate IDs or adjudication fields are assigned.

## Findings

### F-NUM-001

The abstract uses different denominators within its displayed phase-2 allocation percentages.

- Exact locations and roles: REPORT [main p.1, RESULTS, both phase-1 nonabstainer paragraphs](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.6, Figure 2 nonabstainer phase-2 branches](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=6).
- Printed inputs: CNRT 191 nonabstainers, 151 rerandomized, 40 assigned continuation; continuation 90(47%), increase 50(33%), switch 51(34%). VAR157 nonabstainers, 122 rerandomized, 35 assigned continuation; increase 39(32%), switch 41(34%), continuation 77(49%).
- Rule and calculation: one paragraph identifies the 191/157 nonabstainers as the population for the listed end-of-treatment groups. Their group counts sum 191 and 157. Continuation percentages reproduce 90/191=47.120% and 77/157=49.045%; other percentages instead approximate 50/151=33.113%,51/151=33.775%,39/122=31.967%,41/122=33.607%. With common nonabstainer denominators, the four count ratios are 26.178%,26.702%,24.841%,26.115%. Conservative half-unit input-derived intervals are[25.8486,26.5092], [26.3708,27.0341], [24.4444,25.2396], [25.7143,26.5176]%. Compared with printed intervals[32.5,33.5], [33.5,34.5], [31.5,32.5], [33.5,34.5]%, relative gaps are 0.18154,0.19017,0.19564,0.20537, all above 0.05. Counts themselves reconcile.
- Focus area: A. Proposed review domain: statistical_results. Proposed relationship: S_W. Related inventory: N008,N009.
- **Qualifying route:** Route A, category 3.
- **Affected result or extracted value:** allocation proportions of the four noncontinuation rescue groups in the abstract.
- **Why context does not resolve it:** counts and percentages within the same display qualify under category3. Both denominators are printed, but no labels distinguish which one applies to each group; the common population and continuation percentages do not share the noncontinuation denominator.
- Alternatives: percentages may intentionally describe the rerandomized subset for switch/increase and the full nonabstainer population for continuation. That would require separate denominator labels.
- Exact human question: “Which denominator is intended for each abstract phase-2 allocation percentage, and should the four switch/increase percentages describe all phase-1 nonabstainers or only those rerandomized?”

### F-NUM-002

The employment percentage in the main results narrative does not reconcile with the displayed employment counts.

- Exact locations and roles: REPORT [main p.4, Baseline Characteristics and Participant Flow, first paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=4); REPORT [main p.5, Table, Employment Yes/No and both n=245 headers](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5).
- Printed inputs: narrative 490 participants and “>79% employed”; Table181(73.9%) of 245 CNRT and 179(73.1%) of 245 VAR, with unemployed64/66.
- Rule and calculation: (181+179)/(245+245)×100=73.4694%. Employment counts completely partition each arm. Conservatively allowing both employed counts half a unit and the narrative total 490 half a unit gives[73.1906,73.7487]%. Even replacing the strict >79 threshold by 78.5%, the gap is4.7513 points and relative discrepancy4.7513/79=0.06014>0.05.
- Focus area: A. Proposed review domain: statistical_results. Proposed relationship: S_W. Related inventory: N005,N031,N032,N045.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** overall employed percentage in the reported sample.
- **Why context does not resolve it:** the paragraph and Table both describe the same490-person sample; neither gives a separate employment analysis set or definition that could produce a value above 79%. A reader could extract either the narrative percentage or the complete Table counts.
- Alternatives: the narrative may refer to another employment definition or denominator; no such definition is supplied locally.
- Exact human question: “What employment numerator and denominator underlie the narrative >79%, given the Table’s360 employed participants among490?”

### F-NUM-003

The abstract and body provide different lower credible limits for the same primary CNRT rescue contrast.

- Exact locations and roles: REPORT [main p.1, CNRT RESULTS paragraph, absolute RD](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.5, Smoking Cessation End of Phase 2, CNRT paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5); REPORT [supplement p.21, eTable 4 CNRT increase and switch versus stay rows](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21).
- Printed inputs: abstractRD 6%,95%CrI6%–11%, applying to either increase or switch; bodyRD 6%,95%CrI2%–11%; eTable 4 increase6%(2%–11%), switch6%(2%–10%).
- Rule and calculation: compare matching  printed lower limits6% versus 2%; half-unit intervals[5.5,6.5] and[1.5,2.5]% are separated by 3 points, relative discrepancy3/6=0.50. The upper10% versus 11% intervals touch and do not independently qualify.
- Focus area: B. Proposed review domain: statistical_results. Proposed primary relationship: S_C; all relationships:S_C,S_W. Related inventory: N064,N098.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** lower 95% credible limit for the primary week-12 CNRT rescue-versus-continuation RD.
- **Why context does not resolve it:** category2 applies to a substituted printed interval limit with a reproduced magnitude difference. The abstract supplies no alternative analysis or population; its lower bound can be extracted independently.
- Alternatives: abstract may report a different posterior contrast or combine the two strategies, but no distinct computation is identified. The body groups both strategies; eTable 4 separates them.
- Exact human question: “Which95% credible interval belongs to each CNRT rescue-versus-continuation primary contrast, and what analysis produced the abstract’s6% lower limit?”

### F-NUM-004

The direction of the primary VAR-to-CNRT switch contrast differs between its signed result, narrative, and supplementary table.

- Exact locations and roles: REPORT [main p.1, VAR RESULTS paragraph, RD−3% and its immediately following comparison](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=1); REPORT [main p.5, VAR Smoking Cessation End of Phase 2 paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=5); REPORT [main p.7, Figure 3 VAR nonabstainer switch/continue rows](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7); REPORT [supplement p.21,eTable 4 VAR nonabstainer switch CNRT versus stay VAR row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=21).
- Printed inputs: switch CNRT0%(0%–0%),0/41; stay VAR3%(1%–4%),2/77. Main body explicitly describes switching relative to continuation and printsRD−3%(−4%to−1%), yet says “continuing was worse than switching.” Abstract placesRD−3% beside “continuing ... was worse than switching to a higher dosage.” eTable 4 labels switch CNRT versus stay VAR but prints+3%(+1%to+4%),NNT 39.
- Rule and calculation: for switch-minus-stay the displayed model probabilities imply negative direction; no crude estimate is substituted. The body supplies that signed contrast explicitly. The +3% versus−3% copies have half-unit intervals[2.5,3.5] and[−3.5,−2.5]%, gap5 points, relative discrepancy5/3=1.6667. Credible limits have reversed signs as well. “Continuing worse” is the opposite direction from switch 0% versus continue3%.
- Focus area: B. Proposed review domain: statistical_results. Proposed primary relationship:S_C; all relationships:S_C,S_W. Related inventory:N064,N097,N098.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** signed primary switch-versus-continuation RD, interval direction, and which rescue strategy the −3% result describes.
- **Why context does not resolve it:** category2 covers a printed sign/reference direction conflict. The table label matches other rescue-minus-stay rows, but no magnitude-only convention is stated. The abstract’s higher-dosage clause names a different rescue comparison.
- Alternatives: eTable 4 may report absolute magnitudes/NNT while the main body uses signed RDs; its interval and contrast label would then require an explicit convention. The body narrative may intend switching worse than continuation. The abstract may intend the positive higher-dose contrast rather than the adjoining−3%result.
- Exact human question: “What reference orientation and sign convention are intended for the VAR-to-CNRT switch contrast, and which comparison should the body and abstract direction statements accompany?”

### F-NUM-005

The six-month CNRT summary reports rate values that differ from the detailed result and figure.

- Exact locations and roles: REPORT [main p.7, Secondary Outcomes six-month paragraph](../../../jama_cinciripini_2024_oi_240036_1716416465.98349.pdf#page=7); REPORT [supplement p.10, Secondary Outcomes Summarized Analysis](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10); REPORT [supplement p.11, Continuous Abstinence at6 months for CNRT Non-Abstainers](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11); REPORT [supplement p.16,eFigure 3 CNRT nonabstainer increase/continue rows](../../../joi240036supp2_prod_1716416466.01349.pdf#page=16); REPORT [supplement p.33,eTable 9 six-month CNRT increase versus continuation row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33).
- Printed inputs: main and supplement summaries state CNRT+ 3% and VAR+ 2% provided benefit over continuation0%. Detailed CNRT results and eFigure 3 instead give CNRT+ 6%(4%–9%),3/50, and continue CNRT3%(2%–5%),3/90; eTable 9 gives theirRD 3%(0%–6%),probability 96%.
- Rule and calculation: compare same six-month CNRT cell probabilities, without using crude ratios. Printed increase3%versus 6% half-unit intervals[2.5,3.5] and[5.5,6.5]% have gap2 points, relative discrepancy2/3=0.6667. Printed continue 0% versus 3% intervals[−0.5,0.5] and[2.5,3.5]% have gap2; any positive gap with reference zero qualifies. The numeric3%also appears as the modeled increase-minus-continuationRD rather than increase-arm probability.
- Focus areas:A,B. Proposed review domain:statistical_results. Proposed primary relationship:S_C; all relationships:S_C,S_W. Related inventory:N058,N061,N098,N102.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** six-month CNRT increase and continuation arm probabilities, as distinct from their3percentage-pointRD.
- **Why context does not resolve it:** category2 applies to printed values that change magnitudes; the summary’s parentheses mix arm-specific values and perhaps a difference. Its continuation0%does not match the CNRT figure. The abstract identifies the six-month dose-increase conclusion as a secondary result, but gives no numeric resolution.
- Alternatives: summary3%may be an intended RD, and continuation0%may apply only to VAR. Separate labels are needed if that interpretation is intended.
- Exact human question: “Do the six-month summary parentheses report arm probabilities or risk differences, and what are the intended CNRT increase and continuation probabilities?”

### F-NUM-006

Several EOT+30 narrative values use a decimal scale different from their matched figures and tables.

- Exact locations and roles: all REPORT, [supplement p.10, detailed CNRT nonabstainer probabilities and switchARD, then VAR increase probability](../../../joi240036supp2_prod_1716416466.01349.pdf#page=10); [supplement p.11, VAR increase-versus-continue and increase-versus-switch ARDs, then phase 1-abstainer ARD](../../../joi240036supp2_prod_1716416466.01349.pdf#page=11); [supplement p.15,eFigure 2 switch CNRT-origin and both increased-dose cells](../../../joi240036supp2_prod_1716416466.01349.pdf#page=15); [supplement p.33,eTable 9 EOT+30 switch and increased-VAR rows](../../../joi240036supp2_prod_1716416466.01349.pdf#page=33); [supplement p.34,eTable 10 EOT+30 VAR increase-versus-switch row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=34); [supplement p.35,eTable 11 EOT+30 abstainer row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35).
- Printed inputs and all affected occurrences: p10CNRT switch 1.0%(7.0%–1.3%) versus figure10%(7%–13%); p10CNRT increase 8.0%(5.0%–1.1%) versus figure8%(5%–11%); p10CNRT switch ARD6.0%(3.0%–1.0%) versus table6%(3%–10%); p10VAR increase 8.0%(5.0%–1.1%) versus figure8%(5%–11%); p11VAR increase-versus-continue ARD8.0%(5.0%–1.1%) versus table8%(5%–11%); p11VAR increase-versus-switch ARD8.0%(5.0%–1.1%) versus table8%(5%–11%); p11 responders ARD 1.1%(−1.0%–22%) versus table11%(−1%–22%). These seven narrative occurrences form one repeated decimal-scale pattern; matched locations are independently identified.
- Rule and calculation: for1.0 versus 10%, half-unit intervals[0.95,1.05] and[9.5,10.5]% give gap8.45 and relative8.45/1=8.45; for1.3 versus 13%, [1.25,1.35] versus[12.5,13.5] give11.15/1.3=8.5769; for1.1 versus 11%, [1.05,1.15] versus[10.5,11.5] give9.35/1.1=8.5; for1.0 versus 10%upper ARD limit same 8.45; for1.1 versus 11% ARD, same 8.5. All exceed0.05. Several narrative intervals also print their lower limit above the upper, and their point estimate falls outside the printed endpoint range.
- Focus area:B. Proposed review domain:statistical_results. Proposed relationship:S_W. Related inventory:N058,N060,N102.
- **Qualifying route:** Route A, category 2; the point-outside-interval occurrences independently qualify under category1.
- **Affected result or extracted value:** EOT+30 CNRT switch probability; CNRT and VAR increased-dose credible limits; CNRT switch ARDupperlimit; VAR increased-doseARDupperlimits; phase 1-abstainer RD.
- **Why context does not resolve it:** category2 requires registration of a reproduced numerical decimal slip even when matched figures/tables suggest another reading. Category1 also applies to point-outside-interval displays.
- Alternatives: figures/tables may carry intended decimal scales; narrative may instead describe another analysis, but no such analysis is labelled. The repeated tenfold pattern is an observation, not an assertion about production.
- Exact human question: “Which point estimates and credible limits are intended for each of the seven EOT+30 narrative occurrences, and should their decimal scales match the cited figures and tables?”

### F-NUM-007

The six-month phase 1-abstainer credible limits differ between narrative and table.

- Exact locations and roles: REPORT [supplement p.12, Continuous Abstinence at6 months for Abstainers, final sentence](../../../joi240036supp2_prod_1716416466.01349.pdf#page=12); REPORT [supplement p.35,eTable 11 six-month row](../../../joi240036supp2_prod_1716416466.01349.pdf#page=35).
- Printed inputs: narrativeARD 1.0%(−1.3%–1.1%),posterior probability 55%,small benefit VAR; tableARDforCNRTversusVAR1%(−11%–12%),probability 56%.
- Rule and calculation: matching  six-month initial-responder contrast; lower−1.3 versus−11 half-unit intervals[−1.35,−1.25] and[−11.5,−10.5]% give gap9.15 and relative9.15/1.3=7.0385. Upper1.1 versus 12 half-unit intervals[1.05,1.15] and[11.5,12.5]% give10.35/1.1=9.4091. Both exceed0.05. The55%versus 56%probability copies do not independently qualify.
- Focus area:B. Proposed review domain:statistical_results. Proposed relationship:S_W. Related inventory:N058,N102.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** six-month CNRT-versus-VAR phase 1-abstainer RD credible interval.
- **Why context does not resolve it:** the same population/time point/contrast has materially different interval widths; no different model or posterior summary is identified, and the paragraph’s benefit VARdirection does not define an alternative signed orientation. Its limits are not simple matched tenfold copies of the table limits, so this is separate from F-NUM-006.
- Alternatives: one location may use a different analysis or contrast orientation; reversing sign alone does not reproduce the printed limits.
- Exact human question: “Which six-month phase 1-abstainer RD credible interval is intended, and do the narrative and eTable 11 report the same model and reference orientation?”

## Excluded observations

Only apparent discrepancies are listed here. Reconciled checks remain in the stable inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.5 Table, both Male rows and Sex totals | Each 145(57.1%) of 245 yields 59.184%; half-unit input intervals give [58.8595,59.5092]% versus [57.05,57.15]%, minimum relative gap 0.02994. Female105 + male145 =250 versus 245 has exact relative discrepancy0.02041; relaxed interval gap3.5/245=0.01429. Both are at most0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.6 Figure2 and main pp.1,4 populations | Assessed2232 minus excluded1740=492 versus randomized491; CNRT 245 allocated/treated plus 1 excluded and overall491 versus 490 differ by one person. Relative discrepancies are at most0.00409. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.1,4 total White percentage; p.5 White CNRT row | 287/490=58.571% versus 58%;143/245=58.367% versus 58.3%. Both are within the precision threshold. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.19 eTable3 race and employment totals | VAR-origin switch-to-CNRT race counts sum 43 versus 41; exact relative discrepancy2/41=0.04878. Employment totals49 versus 50 and 38 versus 39 have relative discrepancies0.02000 and 0.02564. Half-unit allowances reduce these gaps further. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.19 eTable3 Employment and Other VAR-origin switch row | Employment entries visibly use percent(count) despite the n(%) header. Other4.9(2) uses the same obvious reversal;2/41=4.878%. The intended quantities are immediately identifiable. | CONTEXT_RESOLVES |
| REPORT supplement p.32 eTable8 footnote b | HeaderN50 versus missingness denominator2/51 differs by one person;1/50=0.02 and the half-unit copy intervals touch. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement p.32 eTable8 continue Ns50/42 versus main Figure2 Ns90/77 | Compliance uses the rerandomized continuation counts; the outcome analysis adds40/35 assigned nonreturners. The difference75 equals those nonreturners. Compliance contributors and intention-to-treat outcome denominators have distinct purposes. | CONTEXT_RESOLVES |
| REPORT main Figure3; supplement eFigures2/3 and eTables5/6 | Posterior probabilities and weighted AE estimates differ from crude n/N, including positive AE estimates for zero observed events. The captions and model descriptions identify modeled estimates. | MODEL_VERSUS_CRUDE |
| REPORT main pp.5,8 VAR increase RD; supplement eTable4 NNT row | RD 18% versus rounded points20%−3%=17% does not exceed the precision threshold. NNT378 reciprocates to 0.26455%, within printed 0% ±0.5%. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p.7 and supplement p.10 secondary VAR continuation count | Contributor count42 versus figure77 distinguishes rerandomized and assigned continuation participants at a secondary time point;42+35=77. It does not change the key primary analysis denominator. | PERIPHERAL_COMPARISON |
| REPORT main pp.5,7 and supplement eTable4 | Corresponding interval copies −5 versus−4,10 versus 11,23 versus 24 have touching half-unit intervals and no qualifying gap. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement pp.11,12 and eTables10/11 pp.34,35 | Six-month posterior probability copies88% versus 89% and 55% versus 56% have touching half-unit intervals. The interval discrepancy is separately F-NUM-007. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN p.13 visit window; p.16 calendar; pp.7,27 screening targets | V2 windows+3 versus+2, calendar arithmetic, and screening≥1000 versus≥3 times enrollment concern plan-internal administrative details. They do not change a primary result, analysis-population size or statistical decision rule. | PERIPHERAL_COMPARISON |
| REPORT main p.4 attendance wording versus abstract and flow | The phrase “did attend rerandomization” for40/35 is resolved by the abstract, continuation assignment and flow. The numeric group counts remain identifiable. | TERMINOLOGY_OR_WORDING |
| REPORT main p.7 average VAR adherence versus eTable8 responder cell | Narrative average≥82% does not state that every treatment-cell mean is≥82%; the active responder cell80% is a distinct component rather than the pooled average. | CONTEXT_RESOLVES |

## Scope closure and limitations

Every assigned grouped display was checked in full; grouped records do not omit rows. Stable inventory records document all primary/secondary numerators, follow-up denominators, baseline category totals, all AE row triples, compliance cells/placebo flags/missingness, NNT identities, protocol numeric rules, and modeled-result distinctions. Scientific numeric coverage gaps:0. Unavailable participant-level data, posterior draws, model exposure denominators and unlabelled density quantiles are not reconstructed. Separate statistical and cross-source specialists own method, decision-rule, and planned-analysis reproduction; numeric components are cross-referenced without assuming an unstated reproducing method.

Direct confirmation used current-source images main pp.4/5 andsupplement pp.19/21 plus fresh Poppler pdftotext26.01.0 layout extraction main p.1 andsupplement pp.10–12, CPU. Fresh derivatives: preprocessing/numeric_checker/main-p1.txt and preprocessing/numeric_checker/support-pp10-12.txt. No OCR, fallback, GPU or Python was used. Sources and reused assets were preserved.

Counts:3 sources;91 physical pages;104 numeric relationship groups;7 findings;15 excluded observations. Artifacts:relationships/numeric_relationship_inventory.md;checkers/numeric_consistency.md.


## Subsequent independent audit clarification

Excluded observation NUM-E10, the EOT plus30-day VAR continuation n42 versus77 comparison, qualifies under Route B through the analysis-population-size exception to the peripheral tier. Its original PERIPHERAL_COMPARISON rationale is superseded. The same observation and every affected location were independently included as F-XS-010 and registered/rechecked as C008 before this audit. No distinct issue or location is missing and no duplicate candidate/finding is emitted.
