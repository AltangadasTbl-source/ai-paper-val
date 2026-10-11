# Numeric consistency checker — main article

Scope: DOC-001 main article physical PDF pages 1–10, REPORT; all 116 extracted main relationships, stable N001–N116, numeric review COMPLETE. The main inventory retains every baseline row, adverse-event row, participant-flow branch, printed numerator/denominator/percentage, summary scale, and repeated main occurrence. Source-reading and self-screening followed the complete QUALITY_CONTROL_SCOPE.md and review contract. Statistical power/model/test logic and cross-document comparisons have independent assigned reviewers. No old review conclusions or external sources were read.

Direct authority: main PDF p6 was freshly extracted by pdftotext and rendered by pdftoppm (Poppler 26.01.0, CPU), then visually read. Fresh derivatives: preprocessing/numeric_main/main-page-006-layout.txt and preprocessing/numeric_main/main-page-006.png. Reusable native page files for all ten pages and page6 image supported location and transcription. The direct render confirms Table2 hierarchy and the printed totals; it agrees with reusable text.

## Completed arithmetic and identity checks

Randomized307+303=610; death11+17=28; survivors296+286=582=610−28. Complete282+269=551 and imputed14+17=31 partition582; each arm and withdrawal/incomplete split reconciles. Death, eligibility, female, adherence and patient-reported improvement percentages reconcile at printed precision. Every Table1 count/percentage was checked using307/303; sex, living arrangements, stroke types and mRS partitions sum to each arm. Vessel territory overlap is expressly allowed by footnotec. Median subscale sums need not equal total-score medians. Outcome summaries are within supplied scale bounds. Primary abstract/Key Points/body estimates and populations match. Mean differences are explicitly adjusted; ordinal OR is explicitly ordinal-logistic adjusted odds, distinct from a risk ratio or median ratio. Events and affected participants are distinct units. Serious126+129=255 and interest79+67=146 match narrative totals and repeated abstract figures. Table2 stroke, cardiac and trauma partitions reproduce; other Table2 additive relationships are addressed below.

## Findings

### F-NUM-001

**Title:** Table2 adverse-event category counts do not reconcile with displayed totals in two arm-specific relationships.

**Relationships:** N073–N097 (M-A01–M-A25), N115 (M-A43). Same additive-total rule and same displayed event-classification structure; consolidated as one pattern, without treating each affected row as an independent issue.

**Source locations and document roles:** REPORT [main article physical p6, printed1528, Table2](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), serious-event column headers, top-level categories, and infection subtype block. REPORT [p6 Adverse Events narrative](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) corroborates126/129 serious events and55/44 infections. REPORT [p1 abstract](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=1) repeats these totals. Abstract and narrative are corroboration; the numeric mismatch is within Table2 itself. Relationship type proposed S_W; all relationships S_W.

**Printed inputs:** Header is Events, No., levodopa n=126, placebo n=129. Levodopa top-level serious categories are infection55, stroke16, major extracranial bleeding5, cardiac event12, cancer4, trauma4, kidney failure6, epileptic seizure3, deep vein thrombosis/pulmonary embolism3, electrolyte disorder2, fracture1, traumatic intracerebral hemorrhage0, other32. Placebo infection parent44 has subtype rows pulmonary17, urinary15, abdominal7, meningoencephalitis/encephalitis2, unspecified2, other9. Nested subtypes are counted only within their parent, not again in the top-level sum.

**Rule and calculation:** A displayed event total and its category/subtype counts should reconcile, or the event-to-category counting rule must identify why a count has multiple classifications. Levodopa serious top-level sum55+16+5+12+4+4+6+3+3+2+1+0+32=143, compared with header126. Placebo infection subtype sum17+15+7+2+2+9=52, compared with parent44. As a contrast within the same display, stroke15+1=16 and18+1=19; cardiac5+5+2=12 and1+2+0=3; trauma4=4 and5=5. These contrasts support the additive reading.

**Display precision:** Every integer input is conservatively allowed its half-unit interval, with the zero count constrained to [0,0.5]. The 13 levodopa serious category counts sum to interval[137,149.5], while printed126 has[125.5,126.5]; gap10.5 and relative discrepancy10.5/126=0.08333, above0.05. Six placebo infection subtype counts sum to[49,55], while printed44 has[43.5,44.5]; gap4.5 and relative discrepancy4.5/44=0.10227, above0.05. Using unconstrained symmetric intervals for zero gives the first gap10 and relative0.07937, still above0.05. No percentage was manufactured or treated as printed.

**Focus area:** A, counts and denominators, including category totals within one display. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category3 (counts within one display). The event-total/subtype additive pattern is reproduced beyond display precision. It also satisfies Route B if category3 is interpreted narrowly as requiring an expressly printed percentage: the mismatch is an in-focus event-count relationship, the category-counting convention is absent from the immediate table, and event totals55/44 or126 may be extracted differently from their categories.

**Affected result or extracted value:** Levodopa total serious events126 versus category sum143; placebo infection events44 versus subtype sum52. These values matter to extracting serious-event and infection-event burdens by treatment group.

**Why context does not resolve it:** This is the within-display count category in route A. The table labels counts as events and does not disclose multiple categories per event. The narrative expressly distinguishes255 events from177 participants, so repeated events in a participant alone do not explain more event classifications than events. The fact that other partitions add establishes an apparent numerical relationship rather than a mere terminology difference.

**Source-grounded alternatives and missing definition:** A single adverse-event record could carry more than one classification, or categories could count event descriptions at a different level from the displayed header/parent totals. The table does not state a mutually exclusive coding convention; these alternatives remain possible and are not declared excluded. The missing definition is whether an event can be assigned multiple top-level serious categories or multiple infection subtypes, and which totals represent event records versus classifications. No preferred corrected number or analysis is proposed.

**Exact human question:** Does Table2 count distinct adverse-event records or multiple classifications per event, and which explicit counting rule reconciles the levodopa serious-category sum143 with126 events and the placebo infection-subtype sum52 with44 infection events?

## Excluded observations

Only apparent issues that were considered and not emitted appear here. Reconciled checks are in the inventory, not this table.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p6 Table2 placebo serious column | Top-level sum139 versus129. Half-unit sum interval[133,145.5] versus[128.5,129.5] gives gap3.5/129=0.02713, at most0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 Table2 levodopa infection block | Subtype sum59 versus55. Half-unit sum interval[56.5,62] versus[54.5,55.5] gives gap1/55=0.01818, at most0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 Table2 levodopa prespecified-interest column | Seventeen rows sum88 versus79. Half-unit sum interval[79.5,96.5] and header[78.5,79.5] touch, gap0. Placebo row sum67 matches67. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp1–3 intervention | Abstract says three times daily39 days; body gives escalation/full-dose/taper over39 days. Immediate dosing schedule identifies full-dose frequency and duration; numerical39-day duration reconciles. | TERMINOLOGY_OR_WORDING |
| REPORT main pp1,2,5,6 primary/secondary continuous outcomes | Raw median difference4 at3 months versus adjusted mean difference−0.90; crude rounded secondary mean differences versus adjusted differences. Explicit model/mean-versus-median labels identify different quantities; no effect-measure identity conflict. | MODEL_VERSUS_CRUDE |

## Scope completion and limitations

116 numeric relationships complete, one consolidated finding, five excluded observations. No numeric result relationship omitted. Continuous secondary denominators are not printed in the main article; they were not assumed equal to the primary full analysis set. Participant-level graphical coordinates are not supplied as raw data. Neither absence alone produces a finding. Exact method-level power/test logic belongs to the statistical reviewer; main numeric scale/unit and denominator checks are complete. Source and reused artifacts were preserved.
# Numeric consistency checker — supplemental REPORT shard

Complete scope: DOC-004 pp1–27, DOC-005 pp1–8, DOC-006 p1, DOC-007 p1. Roles REPORT by content. Stable inventory N121–N233 contains113 relationships: every baseline, secondary, estimand, harm row and aggregate check. Findings1; excluded apparent-observation patterns10. Main-only and primary cross-document matching remain separately assigned. No C IDs assigned. Scope and review contract read completely; no old conclusions or web used.

Authority: exact supplied PDFs. Direct Poppler pdftotext26.01.0 layout corroboration and CPU-rendered DOC-004 pp14,22; reusable images pp10,15,17 used as locators/transcription aids. Newly rendered p14 visually confirms the conjunction and N395. Derivatives preprocessing/numeric_support/DOC-004-layout.txt, DOC-004-p14.png, DOC-004-p22.png; render commands pdftoppm -f14 -l14 -r120 -singlefile -png and -f22 -l22 -r100 -singlefile -png; direct text command pdftotext -layout. Sources and reused assets preserved.

## Findings

### F-NUM-121

**Title:** Combined-exclusion population count does not reconcile with its printed conjunction.

**Exact locations and document roles:** REPORT [DOC-004 eTable2 p13, estimands1,6,7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13); REPORT [DOC-004 eTable3 p14, estimands9 and11](../../../joi250066supp3_prod_1761597796.4701.pdf#page=14). Same supplemental REPORT; proposed relationship S_W; all relationships S_W. Inventory N172,N173,N175,N177,N219,N220.

**Printed inputs:** Full analysis set N582. Estimand6 excludes medication intake<80% and prints N496. Estimand7 excludes at least one week with fewer than5 rehabilitation sessions/week during4weeks and prints N450. Estimand11 uses the same full analysis set and three-month FMA: excludes participants with that rehabilitation criterion “and who took less than 80% of the study medication.” It prints N395 and effect0.32 [−3.25,3.89].

**Rule and reproduced calculation:** Let A be medication nonadherence, B the rehabilitation criterion among N582. Individual excluded counts are582−496=86 and582−450=132. Excluding A∩B cannot remove more than86; retained population must be at least496. Printed395 is101 below this bound. Excluding A∪B could produce395: union loss187 and intersection86+132−187=31. The printed conjunction specifies a different set from the union compatible with its count.

**Display precision:** N6 interval[495.5,496.5]; N7 interval[449.5,450.5]; base interval[581.5,582.5]. Intersection-exclusion retained count must be at least max(N6,N7), hence admissible interval[495.5,582.5]. Printed395 interval[394.5,395.5]. Gap100; relative discrepancy100/395=.253165>.05. Exact integer interpretation gives difference101, but conservative half-unit arithmetic independently qualifies.

**Focus area:** A, analysis-population counts; C, method logic.
**Proposed review domain:** statistical_results.
**Qualifying route:** Route B.

**Affected result or extracted value:** N395 and the population definition for post hoc combined adherence/rehabilitation estimate0.32 [−3.25,3.89].

**Why context does not resolve it:** The conjunction appears inside an explicit exclusion rule. Figure7 PH2 broadly mentions low intake and minimal rehabilitation but does not define the Boolean rule or extra exclusions. The printed N395 cannot identify whether the estimate used a union, an intersection, or another population. This changes an analysis-population size and extraction definition, rather than only synonymous wording.

**Alternatives and missing definitions:** “And” could mean applying each separate exclusion, resulting in A∪B; alternatively additional exclusions or another base population may underlie395. Raw memberships, selection expression and any extra exclusions are not supplied. No preferred analysis is proposed.

**Exact human question:** Does estimand11 exclude participants meeting either criterion, only those meeting both, or another explicitly defined set; and which definition corresponds to N395 and0.32 [−3.25,3.89]?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-004 p10 stroke rows](../../../joi250066supp3_prod_1761597796.4701.pdf#page=10) | Ischemic519 versus259+263=522: recomputed[521,523], printed[518.5,519.5], gap1.5/519=.00289. Hemorrhagic91 versus44+44=88: recomputed[87,89], printed[90.5,91.5], gap1.5/91=.01648. Both≤.05; one repeated pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [DOC-004 p17 eTable6](../../../joi250066supp3_prod_1761597796.4701.pdf#page=17) | Overall145 versus arms67+79=146 and category sums146. Arm sum[145,147] overlaps printed[144.5,145.5], gap0. Three-category[144.5,147.5] and six-category[143,149] sums also overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [DOC-004 p11 NIHSS](../../../joi250066supp3_prod_1761597796.4701.pdf#page=11) | Median[IQR] label with8.2(3.9),8.3(3.8),8.2(3.9) resembles mean(SD). Values retained; wording observation without a reproduced conflicting numerical result. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-004 p7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7) | Two deviations introduction followed by3items; explicit list changes no result or analysis-population count. Substantive plan/report differences belong to other checker scope. | OUT_OF_FOCUS |
| REPORT [DOC-004 p15 modeled effects](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15) | Adjusted effects differ from crude means, including FMA-upper difference.08 versus modeled−.73; source does not label these effects crude. | MODEL_VERSUS_CRUDE |
| REPORT [DOC-004 p15 heading](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15) | Generic Mean Difference on FMA spans NIHSS,PROMIS,mRS,Rivermead; outcome identities supply scales and mRS ratio context. No reproduced computation establishes a calculated-quantity conflict. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-004 p12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12) and [p13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13) | Narrative explicitly calls composite strategy win-ratios but names result odds ratio; table win ratio. Shared result1.06 lacks supplied win/loss counts establishing another computed quantity; strategy identifies result. | TERMINOLOGY_OR_WORDING |
| REPORT [DOC-004 p12](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12) and [p13](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13) | Win-ratio CI upper1.25 versus1.26: intervals[1.245,1.255] and[1.255,1.265] touch, gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [DOC-004 p4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=4) and [p22](../../../joi250066supp3_prod_1761597796.4701.pdf#page=22) | Thirteenacute sites versus12nonzero enrollment labels; a roster can include an inactive site, and all actual recruitment counts sum610. | PERIPHERAL_COMPARISON |
| REPORT [DOC-004 p16 SAE death rows](../../../joi250066supp3_prod_1761597796.4701.pdf#page=16) | Participants died28/17/11 versus death-outcome event records29/18/11 may reflect repeated events; same-quantity half-unit intervals also touch for28vs29 and17vs18, gap0. | ROUNDING_OR_DISPLAY_PRECISION |

## Complete checks and limitations

Every eTable1 count and percentage checked against610/303/307 and arm sums. Apart from screened stroke pattern, row sums reproduce. Living-status, stroke-type, vessel-laterality partitions reproduce. Median/IQR order coherent; medians are not additive across arms or component scales. Source NIHSS summary label retained.

All11estimand rows reviewed; individual retained counts bounded by stated base.610−28=582;582−551=31; other exclusions37,86,132,58. Joint-exclusion count is the sole emitted finding. All10eTable4 rows reviewed for N, counts, summary/effect identity; PRAI51/270=18.8889%,51/276=18.4783%,total546. Continuous SMD diagnostic absolute mean difference divided by equal-weight pooledSD gives.05250,.00416,.00423,.04237,.05325,.02631,.02964,.03966; displayed-input intervals permit all printed SMDs including lower FMA.003 and PROMIS10.031. These diagnostics do not substitute for adjusted effects; mRS medians/IQR cannot reproduce SMD without distribution inputs.

Every harm row arm sum reproduces. SAE severity103+106+46=255,54+54+21=129,49+52+25=126; outcome6+76+29+0+142+2=255,4+40+18+0+65+2=129,2+36+11+0+77+0=126. Qualifying SAE flags death28,hospitalization212,disability23,life-threatening16 sum279 but are not declared exclusive. No unique-participant denominator inferred from event records. eTable6 three partitions total146/67/79; overall145 pattern screened under precision rule. No percentages actually printed despite No.(%) headings; absent percentages alone supply no contradicted result. Twenty-three AE types onp19 are not an exclusive participant partition.

Site totals318+70+57+52+25+24+19+15+13+8+8+1=610. Forest-plot signs and null crossings agree with mean-effect rows. Center and spline/subgroup plots lack exact numerical annotations; no invented count/effect precision. DOC-005 and DOC-007 administrative, no applicable numerical results. DOC-006 implemented linear-regression/pooled coefficient method supplies no numerical outcome/count; method cross-reference to support S-R018 and complete statistical checker. Estimate/test and report/plan comparisons remain independently assigned.

Limitations: raw set memberships and extra exclusions unavailable; unannotated graphical exact quantities cannot be transcribed. All37assigned source units covered; scientific coverage gaps0. Main harm findings are separately owned; supplement supplies no explicit exclusive categories or multiple-events footnote resolving every main display.
