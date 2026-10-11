# Numeric Consistency Review — Main Source Shard

Runtime ID: 01a129b4-c3f5-7492-bb6b-2461f3c7811e; model gpt-6.1-sol; reasoning medium; FRESH_SPAWN. Scope DOC001 REPORT pp1–10, all M001–M127 bundles, 99 numeric relationships N001–N099 in relationships/numeric_relationship_inventory.md. Five findings and nine excluded observations. Support/plan/cross-source numeric checks separately assigned; no gaps in main scope. Source authority and CPU derivative provenance in inventory. No C IDs or adjudications assigned. All findings pending independent inclusion screening.

### F-NUM-001

**Issue:** Opposite printed signs for the primary between-arm knee-pain estimate.

**Exact locations and roles:** REPORT [main p2 Key Points](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) versus REPORT [p1 abstract](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), REPORT [p6 Table2 primary row](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), REPORT [p7 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7). Relationship N094.

**Printed inputs:** Key Points mean difference0.30; other three locations−0.3. All carry95%CI−6.9to6.4;Key Points/Table2/bodyP=.94. Arm changes−19.9K/−20.2P.

**Rule and calculation:** Matching same population,outcome,week24,CI andP. Half-unit intervals[.295,.305] and[−.35,−.25] havegap.545;relative gap.545/.3=1.8167>0.05. P−K=−.3 aligns negative copies. Reversing the contrast could yield+.3, but the CI would also reverse to−6.4to6.9 rather than remain identical.

**Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Signed primary between-group change in knee VAS over24weeks.

**Why context does not resolve it:** A printed sign changes the extracted direction; category2 applies even when the intended copy is reconstructable.

**Alternatives:** Key Points may intend the opposite group contrast or absolute magnitude; neither convention is stated and identicalCI does not distinguish it.

**Human question:** Which signed contrast and group order should accompany the primary mean difference in Key Points?

### F-NUM-002

**Issue:** Placebo omega-3 percentage differs by a decimal place from its printed mass concentration and Methods copy.

**Exact locations and roles:** REPORT [main p9 Discussion second paragraph](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9) versus REPORT [p2 Interventions last line continuing p3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2). Relationship N002.

**Printed inputs:** Both locations describe placebo withoutEPA/DHA andless than5mg/g otheromega3. Methods gives(0.5%);Discussion gives(0.05%).

**Rule and calculation:** 1g=1000mg;5mg/g×100/1000=.5%. Allow5±.5mg/g→percentagebound[.45,.55]%;printed.05%→[.045,.055]%. Gap.395percentage points;relative gap.395/.05=7.9>0.05. Compared printed copies.5[.45,.55] versus.05[.045,.055] yield samegap. The calculation compares parenthetical representations of the same upper bound, not actual unobserved concentrations.

**Focus area:** A/C, numerical intervention composition. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Placebo comparator omega-3 upper-bound composition used in interpreting the randomized exposure.

**Why context does not resolve it:** Category2 applies to the substituted decimal magnitude; source copies could produce tenfold different extracted concentration bounds.

**Alternatives:** Actual oil concentration might satisfy both loose inequalities, but that does not equate the two parenthetical unit conversions. If.05% is the intended composition bound, its equivalent is.5mg/g; if5mg/g is intended, its equivalent is.5%.

**Human question:** What mass-concentration and percent upper bound describe the randomized placebo composition?

### F-NUM-003

**Issue:** ICOAP intermittent item count does not reproduce the printed raw subscale range.

**Exact locations and roles:** REPORT [main p5 Table1 footnoteg](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) versus REPORT [p4 Post Hoc Outcomes](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4); Table2 posthocrows refer toTable1 descriptions [p6](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6). Relationship N004.

**Printed inputs:** Table1 says5questionsconstant and8intermittent. Methods statesitem score0–4, raw constant 0–20, intermittent 0–24,total 0–44, thenrescaling0–100.

**Rule and calculation:** An additive8-item0–4 subscale hasmaximum32, not24;5+8items yieldtotal maximum52, not44. Methodsconstant5×4=20 supports the item-sum reading. Even mandatedhalf-unit allowances give8[7.5,8.5]×4[3.5,4.5]=[26.25,38.25] versus24[23.5,24.5]:gap1.75/24=.0729>0.05. The primary discrepancy is the intermittent subscale; the total is a consequential occurrence, not a separate finding. No external instrument definition used.

**Focus area:** C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The item-count denominator and raw-to 0–100 normalization for the reported intermittent/totalICOAP outcome summaries.

**Why context does not resolve it:** The two numeric specifications cannot jointly identify the scoring denominator; no weighting, excludeditems ordifferentitemmaximum is stated. This changes which normalization a reader reconstructs for a printed outcome.

**Alternatives:** Eight questions could include items excluded from the raw total, or a weighted score might use a different rawmaximum. Those definitions are not supplied. The finding does not assume any externally preferred instrument version.

**Human question:** How many scored intermittent items contributed to the0–24rawscale, and which denominator was used to rescale the intermittent and total scores?

### F-NUM-004

**Issue:** The main ICOAP total between-arm change does not reproduce the two printed model-based arm changes.

**Exact locations and roles:** REPORT [main p6 Table2 post hoc ICOAP total row](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6); method REPORT [p4 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) continuing REPORT [p7](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7). Relationship N070.

**Printed inputs:** Kchange−9.9(CI−13.3to−6.57);Pchange−8.2(CI−11.9to−4.5);between-arm change2.05(CI−2.64to6.74),P.39. Source sayschanges andbetween-arm contrasts are linear combinations of estimated coefficients.

**Rule and calculation:** P−K=−8.2−(−9.9)=1.7. Half-unitinputsK[−9.95,−9.85],P[−8.25,−8.15]→contrast[1.60,1.80];printed2.05→[2.045,2.055];gap.245;relative gap.245/2.05=.11951>0.05. This sameP−K rule reproduces the remaining continuous Table 2 rows underprecision: primary−.3;effusion−1.75;WOMACtotal[3,5] overlaps3.0;weight-bearing3;nonweightbearing2;function51;hand1.3;back−1.3;strength[−2.4,−2.2] overlaps−2.2;AQoL−.01;hsCRP.64;TG.15;HDL−.03;LDL[.00545,.01555] overlaps.01;glucose.04;ICOAP constant[2.8,3.0] overlaps2.95;intermittent1.5. The binary response ratio is not a continuous difference and is excluded from this reproduction family.

**Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** ICOAP total mean between-arm change and the placebo mean within-arm change at24weeks.

**Why context does not resolve it:** Category4 applies because the samearm-change contrast rule reproduces other continuous rows. These are modeled arm changes versusmodeleddifference, notcrudefollow-up minus baseline.

**Alternatives:** The contrast could arise from a different model, population or adjustment from the displayed arm changes, but the shared table and method do not identify such a distinction. Repeated placebo intermittent and total changes could reflect a transcription pattern; production mechanism is not established.

**Human question:** Which armchange and between-armcontrast belong to the ICOAP total model, and were all three estimates obtained from the same model and population?

### F-NUM-005

**Issue:** The OMERACT-OARSI response contrast is numerically a ratio under a shared mean-difference heading without its printed footnote definition.

**Exact locations and roles:** REPORT [main p6 Table2 response row, column heading and footnotes](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6). Relationship N062. This main-source finding uses no cross-document classification.

**Printed inputs:** K50(47%)[n107],P45(41%)[n110];effect1.14(.84to1.55),P.39,superscriptf. Shared effectcolumn says'Between-group difference in change,mean(95%CI)'. Footnotes runa–e; nofdefinition appears on suppliedpage.

**Rule and calculation:** Diagnostic crudeRR=(50/107)/(45/110)=1.1423, matching1.14. Half-unitinputintervalRR[1.10815,1.17745] overlapsprinted1.14[1.135,1.145]. BycontrastabsoluteK−Pprobability difference=.05820,interval[.04494,.07146],or4.494–7.146percentage points; neither probability norpercentage-point difference overlaps1.14 as printed. Probabilityscalegap1.135−.07146=1.06354,relative gap1.06354/1.14=.93293>0.05;percentage-point scale gap4.494−1.145=3.349,relative2.938>0.05. This diagnostic identifiesquantity,not an assertion that a model must equal a crudeRR. The reportedlower/upperlimits are consistent with ratio-scale meaning and not a defined mean-difference exception.

**Focus area:** C,effect-measureidentity. **Proposed review domain:** statistical_results. **Proposed relationship:** S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** Whether1.14(.84–1.55) is extracted as a risk ratio or mean/absolute difference for OMERACT-OARSIresponse.

**Why context does not resolve it:** The shared headingnames a different mathematicalquantity; its absentexception footnote leaves no explicit ratio label orgrouporder. Treating1.14 as mean/absolutedifference changes the extracted effect measure andnullvalue. The arithmetic strongly suggests a ratio, but does not supply the missing source definition.

**Alternatives:** Superscriptf may intend an exception labeling anRR; another ratio measure could also be intended. A later source may clarify, which the independent cross-source shard will compare; this card records the suppliedmainpage's explicit shared heading and numericidentity.

**Human question:** What effect measure andreference group does1.14(.84–1.55) represent, and what definition belongs to footnote f?

## Excluded observations

Only apparent issues considered and not emitted are listed. Reconciled routine checks remain in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| MainFigure1p3 versusResultsp7 | Pdiscontinuers21vs23:intervals[20.5,21.5]/[22.5,23.5],gap1/23=.04348≤.05. Consequentialtotalcompleters224vs222:suminterval[223,225]versus[221.5,222.5],gap.5/222=.00225≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| MainTable3p8 participantswithAE | K67(50.7%)under130header:recomputed interval[50.95785,52.12355]%,printed[50.65,50.75]%;gap.20785/50.7=.00410≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| MainTable3p8 versusabstractp1/narrativep8 | Pextremity6vs5:half-unitintervals[5.5,6.5]/[4.5,5.5]touch;gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| MainTable1p5 BMI/medication count percentages | Apparentheaderfractiondifferences16(13),25(20),38(30),25(20),11(9),19(15):half units pluspossiblyvariable-specific denominators leavezeroor≤.05relative gap;none qualifies. | ROUNDING_OR_DISPLAY_PRECISION |
| MainTable1p5 WORMS | 128/129 availablegradecountsversusrandomized130/132headers;roundedgradepercentages sum101%/99%. Missingvariablevalues androundingdo not implyallparticipantsmustcontribute. | CONTEXT_RESOLVES |
| MainTable1p5 versusTable2p6 strengthbaseline | Placebomean65.8versus65.9:half-unitintervalstouch,gap0;also descriptivebaselinecopy. | ROUNDING_OR_DISPLAY_PRECISION |
| MainTable2p6 longitudinalchanges andWOMACsubscale changes | Model changeisnotcrudefinalminusbaseline. Separatelyadjustedsubscale changes−51−23vs−87K/−48−21vs−83P neednotaddtoseparatelymodeledtotal;no common model decomposition stated. | MODEL_VERSUS_CRUDE |
| Mainp3/p5 WOMACMCII/MCID | 'Increase'forimprovementonhigher-worse scalesisfield-resolvable wording;no computed classification result contradicted. | TERMINOLOGY_OR_WORDING |
| Mainp7 posthocnarrative | 'There were no changes in post hoc outcomes' read withimmediately preceding between-arm comparisons andTable2nonsignificant post hoc contrasts;doesnotidentifywithin-arm zero hypothesis. | CONTEXT_RESOLVES |

## Completion and limitations

Main numeric shard complete:99relationships,5findings,9excluded observations;all10sourcepages and127mapperbundles considered,withall table cells preserved. No scientific coverage gap. Support/plan/cross-sourcechecks ownedfreshsupport numeric shard. No supplied raw data formean reconstruction; no inferredcrudemodel or invented graphic coordinates. Direct CPU tooling used;derivatives recorded in relationship inventory.
# Numeric Support Consistency Review

Fresh optional shard runtime 01a129b5-97cf-7843-9ca2-d5d4de552d64; gpt-6.1-sol/medium. Complete scope DOC-002 PLAN pp1–15, DOC-003 PLAN p1, DOC-004 REPORT pp1–15, and matching numeric REPORT repetitions against DOC-001. Inventory N101–N198: 98 relationships, including every65 inferential row. Four findings, ten excluded-observation rows. No scientific gap. Source-linked fresh support and main maps used without old conclusions. Direct Poppler26.01.0 native layout extraction and CPU renders pp3,5,6,8,11; noOCR. Visual confirmations match printed source. Raw participant-event linkage and model-specific summary definitions are absent.

All intervals below allow half of the last displayed unit for each input and the target. Reconciliation records belong in the inventory. Statistical CI/P and sample-size-method logic remain covered by independent S passes.

### F-NUM-101

**Title:** Week4 WOMAC weight-bearing pain change columns do not reconcile with the printed between-group difference.

**Locations and roles:** REPORT [DOC-004 p5 eTable4, weight-bearing pain week4](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5); REPORT same page function week4 corroborates the repeated −84/−103 tuples. Relationship S_W; proposed review domain statistical_results; focus A/B/C; numeric N132.

**Printed inputs:** K change −84 (−122 to−46), P change −103 (−141 to−65), difference3 (−10 to16), P=.66. Final/baseline K100/127 and P108/141. The function week4 row separately prints those identical arm-change tuples and difference−19 (−73 to35), P=.48.

**Rule and calculation:** The displayed continuous between-group differences follow placebo-minus-krill arm changes across the table. The two change inputs give −103−(−84)=−19, recomputed half-unit interval [−20,−18]; printed3 interval[2.5,3.5]. Gap20.5, relative discrepancy20.5/3=6.8333. The printed difference does not reproduce with the same subtraction that reproduces other continuous rows. No comparison of crude final-minus-baseline with modeled changes is required.

**Qualifying route:** Route A, category4.

**Affected result or extracted value:** Week4 weight-bearing WOMAC arm changes, their intervals, and between-group contrast.

**Why context does not resolve it:** Category4 applies: the table prints both conflicting pieces; recognizing the identical function row does not establish which weight-bearing cells belong to this analysis.

**Alternatives:** Arm-change cells may reproduce the function row, or the difference may arise from a different unstated analysis. The source does not say these columns use different change contrasts.

**Human question:** Which week4 weight-bearing arm changes and between-group contrast should be extracted, and do these columns describe the same analysis?

### F-NUM-102

**Title:** Week12 hsCRP arm changes do not reproduce the printed between-group estimate.

**Locations and roles:** REPORT [DOC-004 p6 eTable4, hsCRP week12](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6). Relationship S_W; proposed review domain statistical_results; focus B/C; numeric N172. The glucose week12 row on this page corroborates the repeated contrast tuple but is not itself a numeric contrast finding.

**Printed inputs:** K change−.53 (−1.32 to.26), P change.24 (−.55 to1.03), difference.07 (−1.19 to1.33), P=.92. The glucose week12 row also prints .07 (−1.19 to1.33), P=.92 while its own changes are .09/.15.

**Rule and calculation:** Same displayed P-minus-K contrast rule yields .24−(−.53)=.77. Recomputed interval [.760,.780]; printed .07 interval[.065,.075]; gap.685, relative discrepancy .685/.07=9.7857. The week24 hsCRP row reproduces the same rule: −.12−(−.76)=.64. Both hsCRP rows have the same baseline-adjustment footnote.

**Qualifying route:** Route A, category4.

**Affected result or extracted value:** Week12 hsCRP between-group effect estimate and its associated inferential tuple.

**Why context does not resolve it:** Category4 applies; the unstated possibility of different analyses does not explain why the week12 contrast alone fails the displayed-row reproducing rule.

**Alternatives:** The repeated glucose contrast tuple may be associated with another outcome or model, or arm-change cells may describe a different analysis. Exact mechanism is not established.

**Human question:** Which week12 hsCRP contrast and interval belong to the printed arm changes, and do all columns describe the same adjusted analysis?

### F-NUM-103

**Title:** Smaller-by-one-unit WORMS counts and percentages do not reconcile in either treatment column.

**Locations and roles:** REPORT [DOC-004 p8 eTable5 smaller−1unit and total rows](../../../joi240048supp3_prod_1727199125.83025.pdf#page=8). Relationship S_W; proposed review domain statistical_results; focus A; numeric N117.

**Printed inputs:** K10(12%) with total107(100%); P16(12%) with total109(100%). All category counts sum exactly107/109.

**Rule and calculation:** K100×10/107=9.3458%; with half-unit inputs recomputed [8.8372,9.8592]%; printed12% interval[11.5,12.5]%;gap1.6408/12=.1367. P100×16/109=14.6789%; recomputed[14.1553,15.2074]%;gap1.6553/12=.1379. Both exceed.05. Other table categories do not give a qualifying mismatch under the stipulated rule.

**Qualifying route:** Route A, category3.

**Affected result or extracted value:** Treatment-specific percentage with one-unit smaller WORMS effusion score at24wk.

**Why context does not resolve it:** Category3 applies; counts and displayed totals identify one denominator, but the printed percentages identify a different quantity.

**Alternatives:** A different denominator or another count may underlie the two12% cells; none is disclosed. Matching12% values across treatment columns does not determine which inputs to retain.

**Human question:** What counts and denominators underlie the smaller−1unit percentages in each treatment group?

### F-NUM-104

**Title:** Selected adverse-event counts change treatment attribution between the main display and the detailed supplement.

**Locations and roles:** REPORT [DOC-001 p8 Table3 reflux/abdominal/cough rows](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8), REPORT [DOC-004 p10 eTable7 cough](../../../joi240048supp3_prod_1727199125.83025.pdf#page=10), REPORT [DOC-004 p11 eTable7 abdominal discomfort and gastroesophageal reflux](../../../joi240048supp3_prod_1727199125.83025.pdf#page=11). Relationship S_C; proposed review domain statistical_results; focus A/B; numeric N190–N191.

**Printed inputs:** Main reflux K1/P3 versus supplement K3/P1; main abdominal discomfort K0/P3 versus supplement K3/Pblank; main cough K2/P0 versus supplement Kblank/P2. Supplement headers on p10 identify K first and P second; p11 continuation retains those columns.

**Rule and calculation:** Compare only explicit matching numbers, without replacing blank cells with zero. Reflux1vs3 half-unit intervals[.5,1.5]vs[2.5,3.5] gap1; relative discrepancy1/1=1 for K and1/3=.3333 for P. Abdominal K0vs3 intervals[−.5,.5]vs[2.5,3.5] gap2; any nonzero gap qualifies for printed zero. Cough P0vs2 intervals[−.5,.5]vs[1.5,2.5] gap1; any nonzero gap qualifies. Direction and magnitude of the treatment-specific counts change; the repeated reversal pattern is consolidated.

**Qualifying route:** Route A, category2.

**Affected result or extracted value:** Treatment-specific reflux, abdominal-discomfort and cough adverse-event counts for safety extraction.

**Why context does not resolve it:** Category2 applies: these are substituted counts/reversed treatment readings, not an unspecified denominator or wording difference. The complete category totals do not determine which treatment-specific entry should be extracted.

**Alternatives:** One display may use another classification or counting basis, or selected treatment columns may have been transposed. No separate count definition is stated for these same event names; no conclusion about production mechanism is made.

**Human question:** Which treatment group and event count apply to each of these three event types, and do the displays use the same event-count definition?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| DOC-004 p3 eTable2 overall header/footnote | Overall167 versus footnote165: half-unit gap1, relative1/165=.00606≤.05. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p3 vs DOC-001 p7 | Threshold-adherent (82+81)/167=97.60% versus narrative95%; allowing both numerator inputs half units yields recomputed proportion[96.7164,98.4985] versus[94.5,95.5], gap1.2164/95=.01280≤.05. Mean consumption99%/96% is a different measure. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p8 eTable5 nochange/larger1 rows | K80/107=74.77% versus72%,P75/109=68.81% versus72%; half-unit interval gaps1.4535/72=.02019 and1.9147/72=.02659≤.05. K12/107=11.21% versus12% intervals overlap. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 pp5–6 eTable4 final/baseline/change families, particularly strength12 | Crude marginal strength changes6.1/4.3 differ from model changes−2.8/−4.2; exact repeated back4 tuple is a diagnostic signal. Mixed-model change and differing contributors need not equal marginal final−baseline; numerical reproduction of a model contradiction is not established. Independent statistical pass must inspect method and inference. | MODEL_VERSUS_CRUDE |
| DOC-004 p5 WOMAC component-change families beyondweek4 | Total-pain modeled changes differ from sums of two modeled subscales at someweeks; baseline adjustment explicitly differs for total/weight-bearing versus non-weight-bearing. No supplied statement requires common model/additivity across those fits. | CONDITIONAL_OR_UNREPORTED |
| DOC-004 p6 responder rows4/8/12/16/20/24 | Ratios of rounded displayed proportions differ slightly from printed log-binomial RR; model-based estimates are not compelled to equal crude ratios. | MODEL_VERSUS_CRUDE |
| DOC-004 pp10–11 vs DOC-001 p8 nasopharyngitis and diarrhea | Explicit1vs2 arm copies have half-unit intervals touching; under mandated display rule remaining gap0. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 pp11–12 vs DOC-001 p8 injury category | Detailed listedK6 versus mainK11 injury-category total is a cross-document safety subgroup count; no primary/key-secondary result, analysis-population size or decision rule changes. No established substituted-digit/reversed-arm mechanism; routeA2 not reproduced. | PERIPHERAL_COMPARISON |
| DOC-004 pp10–13 vs DOC-001 pp7–8 all-event total | Detailed nonblank sumsK96/P107 versus main97/106 differ by1; printed-copy half-unit intervals touch and totals203 match combined detailed203. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-004 p6 glucose12 contrast | .15−.09=.06 versus.07: recomputed[.05,.07] and printed[.065,.075] overlap. Repeated hsCRP inferential tuple is handled by statistical CI/P checking, not arithmetic contrast mismatch. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

Every assigned unit and all65 inferential rows checked. Protocol historical illustrations are not current-trial estimates. No supplied individual data, event-person linkage or exact mixed-model fitted means permits reconstruction of marginal-versus-modeled change differences. The supplement's available-case counts and main modeled-population labels are kept distinct, so no fabricated denominator contradiction is emitted. Both independent statistical passes must retain the strength12 repeated back4 tuple and glucose12 CI/P diagnostics. This artifact assigns no C IDs or human dispositions.
