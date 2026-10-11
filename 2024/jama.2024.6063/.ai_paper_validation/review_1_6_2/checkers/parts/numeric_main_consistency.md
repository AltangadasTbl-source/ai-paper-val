# Numeric Consistency Review — Main Source Shard

Runtime ID: 01a129b4-c3f5-7492-bb6b-2461f3c7811e; model gpt-6.1-sol; reasoning medium; FRESH_SPAWN. Scope DOC001 REPORT pp1–10, all M001–M127 bundles, 99 numeric relationships N001–N099 in relationships/numeric_relationship_inventory.md. Five findings and nine excluded observations. Support/plan/cross-source numeric checks separately assigned; no gaps in main scope. Source authority and CPU derivative provenance in inventory. No C IDs or adjudications assigned. All findings pending independent inclusion screening.

### F-NUM-001

**Issue:** Opposite printed signs for the primary between-arm knee-pain estimate.

**Exact locations and roles:** REPORT [main p2 Key Points](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) versus REPORT [p1 abstract](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), REPORT [p6 Table2 primary row](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), REPORT [p7 Primary Outcome](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7). Relationship N094.

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

**Exact locations and roles:** REPORT [main p9 Discussion second paragraph](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9) versus REPORT [p2 Interventions last line continuing p3](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2). Relationship N002.

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

**Exact locations and roles:** REPORT [main p5 Table1 footnoteg](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) versus REPORT [p4 Post Hoc Outcomes](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4); Table2 posthocrows refer toTable1 descriptions [p6](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6). Relationship N004.

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

**Exact locations and roles:** REPORT [main p6 Table2 post hoc ICOAP total row](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6); method REPORT [p4 Statistical Analyses](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) continuing REPORT [p7](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7). Relationship N070.

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

**Exact locations and roles:** REPORT [main p6 Table2 response row, column heading and footnotes](../../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6). Relationship N062. This main-source finding uses no cross-document classification.

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
