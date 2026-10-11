# Main-paper quantitative evidence map

Fresh mapper runtime: 01a129b4-045d-7910-b98e-2eeafcaa15c0. Scope: DOC-001, `jama_cooper_2018_oi_180132.pdf`, physical PDF pages 1–10 (printed 2211–2220). Document role: REPORT. All assigned units mapped; no fresh-required units. This artifact reconstructs evidence only and assigns no candidates or judgments. Keys M001–M088 are local mapping keys; coordinator/checkers assign global numeric/statistical IDs.

## Evidence and coverage

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely, current source coverage, coverage manifest, tooling record, and relevant evidence-asset inventory. Reused source-matched full-document native and layout text under `.ai_paper_validation/review_1_5_2/preprocessing/{native_text,layout_text}/DOC-001.txt`. Complete page sequence read in physical order. Visually inspected reusable rendered pages 01, 04, 05, 06, 07 for the abstract, flow, every baseline/outcome table cell, box plots, axes, patient-count alignment and ordinal distribution. Images under `.ai_paper_validation/review_1_5_2/preprocessing/rendered_pages/`. Source-matched native text has precedence over layout artifacts; no new OCR or rendering was needed. Historical derivative engine/version unspecified; curator source-match engine Poppler pdftotext/pdftoppm 25.03.0, CPU. DOC-001 layout's reported axis-placement difference has no bearing on Table 1 transcription; figure axes were read visually on physical p6.

Evidence links below resolve from this extraction directory to the supplied PDF. H = hypothermia, N = normothermia. Unless otherwise stated, contrast is H versus N, and CIs are 95%. Every table row contains both groups and all displayed measures; a key may represent several inseparable numeric/inferential relationships.

| PDF page | Printed page | Assigned content | Mapping | Status |
|---:|---:|---|---|---|
| 1 | 2211 | Abstract all quantitative statements | M001–M009 | COMPLETE |
| 2 | 2212 | Key Points, design, interim, eligibility, measurements | M010–M017 | COMPLETE |
| 3 | 2213 | Randomization, temperature protocol, outcome definitions, power and analyses | M018–M030 | COMPLETE |
| 4 | 2214 | Flow, remaining analysis methods, population, temperatures | M031–M048 | COMPLETE |
| 5 | 2215 | Table 1 all rows/footnotes, results and adverse events | M049–M066; matching results M006–M009, M075–M078 | COMPLETE |
| 6 | 2216 | Figure 2 all counts/axes/caption and per-protocol/as-treated pneumonia | M067–M074 | COMPLETE |
| 7 | 2217 | Table 2 all rows/footnotes, Figure 3, subgroup/post hoc/discussion | M075–M086 | COMPLETE |
| 8 | 2218 | Discussion, limitations, conclusions, correction notice | M087–M088 | COMPLETE |
| 9 | 2219 | Disclosures, personnel, references, data-sharing pointer | No applicable trial-result quantities; metadata only | COMPLETE |
| 10 | 2220 | References continuation | No applicable trial-result quantities; bibliographic numbers only | COMPLETE |

## Abstract and Key Points

Source [abstract p1](../../../jama_cooper_2018_oi_180132.pdf#page=1).

| Key | Location/quantity | Exact printed content and relationship |
|---|---|---|
| M001 | Abstract design | 511 recruited/randomized; 6 countries; first enrollment December 5, 2010; last November 10, 2017; final follow-up May 15, 2018. |
| M002 | Abstract intervention groups | H randomized 266; N 245. |
| M003 | Abstract temperatures/duration | H 33°C–35°C at least 72 h and up to 7 d if intracranial pressure elevated, gradual rewarming; N target 37°C; both groups temperature management 7 d. |
| M004 | Abstract primary endpoint | Favorable neurologic outcome or independent living, GOS-E 5–8 on scale 1–8, blinded assessment 6 months after injury. |
| M005 | Abstract population/demographics | Among 511 randomized, 500 provided ongoing consent; mean age 34.5 y (SD 13.4); **402 men (80.2%)**; 466 completed primary evaluation. Bold retains literal printed value. |
| M006 | Abstract cooling/recovery | Initiation median 1.8 h after injury (IQR 1.0–2.7); rewarming median 22.5 h (IQR 16–27). |
| M007 | Abstract primary estimate | H 117 (48.8%), N 111 (49.1%); printed risk difference **0.4%**, CI −9.4% to 8.7%; RR with H 0.99 (0.82–1.19); P=.94. Matching body p5 and Table 2 p7 print difference −0.4; values recorded separately without normalization. |
| M008 | Abstract adverse events | Pneumonia H 55.0% vs N 51.3%; increased intracranial bleeding H 18.1% vs N 15.4%. Match p5 narrative/Table 2. |
| M009 | Abstract conclusion | Early H versus N did not improve neurologic outcomes at 6 months; findings do not support early prophylactic H. |
| M010 | Key Points p2 | Trial 511 adults; favorable neurologic outcomes at 6 months H 48.8%, N 49.1%; difference not statistically significant; same conclusion as M009. |

## Design, treatment, outcome and statistical specifications

Source [methods p2](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p3](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p4](../../../jama_cooper_2018_oi_180132.pdf#page=4).

| Key | Exact source unit | Reconstructed relationship/specification |
|---|---|---|
| M011 | p2 introduction | Historical context only: about 50% severe-TBI death/severe disability; prior trial n=392; two subsequent trials stopped at ≤50% planned recruitment; meta-analysis temperature 33–35°C, cooling >48 h, rewarming <0.25°C/h. Not current-trial outcomes. |
| M012 | p2 design | Planned 510; multinational Australia, New Zealand, France, Switzerland, Saudi Arabia, Qatar; dates match M001. Deferred consent, later relative/patient consent. |
| M013 | p2 oversight | Planned blinded interim conduct/progress/safety analyses after 125 and 250 recruits; additional safety analyses recommended after Eurotherm publication at 300,350,400,450 recruits. |
| M014 | p2 participants | 5 out-of-hospital/paramedic agencies,14 EDs; estimated age18–60; GCS<9; actual/imminent intubation. |
| M015 | p2 exclusion/enrollment | Out-of-hospital exclusions include SBP<90 mm Hg, sustained tachycardia>120/min, suspected pregnancy/uncontrolled bleeding, GCS3 plus unreactive pupils, nonstudy destination; ED enrollment permitted up to3 h after injury, additional ED exclusions eTable1. |
| M016 | p2 data collection | Follow to death or6 months after randomization; hourly temperature/intracranial pressure during first96 h. |
| M017 | p2–p3 randomization | Patient randomization 1:1, sealed opaque envelopes, variable permuted blocks2 and4; strata out-of-hospital versus ED and ambulance/geographic region; treating clinicians unblinded; independent blinded structured telephone primary assessors. |
| M018 | p3 induction | H exposure, bolus up to2000 mL IV ice-cold4°C 0.9% saline, surface wraps in ED; initial core35°C then33°C after assessment excluding significant bleeding risk. |
| M019 | p3 maintenance | 33°C or35°C if persistent bleeding concerns for at least72 h after randomization; possible35°C/normothermic rewarming for bleeding instability; otherwise33°C±0.5°C. |
| M020 | p3 rewarming | At72 h assess ICP; if<20 mm Hg gradual controlled rewarming at target up to0.25°C/h; sustained ICP>20 during rewarming prompts recooling/reassessment; maximum hypothermia7 d; once37°C maintain normothermia through7 d. |
| M021 | p3 N and cointerventions | No exposure/cold fluids, warm as required; ICU37°C±0.5°C; wraps for pyrexia/refractory intracranial hypertension; other ICP therapy allowed both groups. |
| M022 | p3 outcome scale | GOS-E1 death;2 vegetative;3–4 severe disability;5–6 moderate disability;7–8 good recovery; primary percentage favorable5–8 at6 months after injury. |
| M023 | p3 secondary definitions | Ordinal GOS-E; hospital-discharge and6-month mortality; adverse events within10 d (intracranial/extracranial bleeding,pneumonia,bloodstream/other infections); also ventilation and ICU/hospital stay reported. Sliding dichotomy neurologic function, complier average causal effect,quality of life,cost-effectiveness explicitly not reported here. |
| M024 | p3 plan/publication | SAP published before study completion, update before data lock/unblinding. Sample500 permits dropout/lost consent/crossover and interim analyses; final510 in2017 after blinded combined withdrawal/loss review. |
| M025 | p3 power | 364 evaluable gives82% power, two-sided P=.05, absolute15% favorable-outcome increase from estimated50% baseline. |
| M026 | p3 historical power basis | Prior46% favorable improvement: RR1.46 (1.12–1.92),P=.006; another prior subgroup<45 y/hypothermic arrival50% favorable increase,P=.02. These are historical rationale, not POLAR results. |
| M027 | p3 analysis population/missingness | All a priori analyses by randomized group excluding consent withdrawals unless otherwise indicated; no missing-data imputation. |
| M028 | p3 binary analyses | Primary favorable GOS-E6 months and secondary mortality/adverse events unadjusted χ² equal-proportions test; frequencies(percentages), RR and risk difference each95%CI. |
| M029 | p3–p4 adjusted sensitivity | Hierarchic multivariable log-binomial regression adjusted for extended IMPACT-TBI; strata(location/site) random effects; RR95%CI. Extended score predicts unfavorable outcome from age,GCS motor,pupil reactivity,CT Marshall,hypotension,hypoxia. |
| M030 | p4 ordinal/survival | Ordinal logistic GOS-E; proportional odds justified with score test; OR95%CI. Cox survival censored6 months/last contact; Kaplan–Meier/log-rank; PH visually assessed log-cumulative hazard plots. |
| M031 | p4 subgroup/temperature | Prespecified surgical hematoma and any significant intracranial hematoma subgroups; logistic treatment×subgroup interaction. Time-to33°C effect on favorable outcome compared by unadjustedχ² frequencies(percentages). |
| M032 | p4 per-protocol/as-treated | Both exclude ineligible entry patients; cooling compliance≤35°C for>48 h within96 h randomization; noncompliers excluded(per protocol) or transferred opposite treatment(as treated). Sensitivity majority first72 h instead of96 h. Post hoc missingness and adequate-dose comparison described in Supplement1. |
| M033 | p4 inference | SAS9.4; two-sidedP<.05 significance; no multiple-comparison adjustment, all secondary outcomes exploratory. |

## Flow and observed temperatures

Source [Figure 1 and results p4](../../../jama_cooper_2018_oi_180132.pdf#page=4).

| Key | Location | Printed counts/quantities and matching occurrence |
|---|---|---|
| M034 | Figure1 top | 511 randomized:231 out of hospital,280 in hospital; H266,N245. Numbers screened not recorded. |
| M035 | Figure1 H flow | Primary240; no outcome data16; withdrew consent6; lost follow-up4; six-month mortality256. These are separate boxes/items as printed, not recast as overlapping categories. |
| M036 | Figure1 N flow | Primary226; no outcome data13; withdrew consent5; lost follow-up1; six-month mortality239. |
| M037 | p4 participants | 8 nonrandomized run-in patients excluded;511 enrolled;231(45%) out-of-hospital;H266,N245;11 withdrawal(H6,N5),500 evaluable. |
| M038 | p4 protocol receipt | Full protocol293: H132,N161; points to eTable8. Primary evaluatedH240,N226. |
| M039 | p4 overall baseline | Mean age34.5(SD13.4);medianGCS6(IQR4–7);diffuse injury70.6%;injury→randomization median1.9 h(IQR1.0–2.7). |
| M040 | p4 temperature direction | Core temperature significantly lower H than control first96 h (Figure2A); no numerical P printed here. |
| M041 | p4 initial target | H233(89.6%) reached35°C; injury→35°C median2.5 h(IQR0.8–5.5); eTable2 pointer. |
| M042 | p4 final target | H186(71.5%) reached33°C; injury→33°C median10.1 h(IQR6.8–15.9); eTable2 pointer. |
| M043 | p4 short cooling | H85 evaluable(33%) received<48 h at33–35°C;27% never33°C because complications/decisions; eFigures3,4/eTable3 pointers. |
| M044 | p4 duration | H cooling until rewarming median72.2 h(IQR69.8–77.3);rewarming median22.5 h(IQR16–27);34 paused for increasedICP. |
| M045 | p4–p5 ICP | Mean daily ICP similar groups during induction,maintenance,rewarming(Figure2B/eFigure1); elevatedICP therapy intensity similar(eTable4). |
| M046 | p5 additional outcomes | No significant group differences time-to-target(eTable7),ventilation,ICU/hospital stay,meanGOS-E6 months,unfavorableGOS-E survivors(eTable5); numerical counterparts in support scope. |
| M047 | p5 propofol | 3 diagnosed infusion syndrome,H2,N1;N case nonprotocol late-rescue cooling;1 of3 died. Match p8 three episodes. |
| M048 | p5 per-protocol/as-treated narrative | No significant baseline differences(eTables8,10);favorable primary not different(eTables9,11);premature rewarming due lesser injury/bleeding(eTable3/eFigures3,6). |

## Table 1 complete row transcription

Source [Table 1 p5](../../../jama_cooper_2018_oi_180132.pdf#page=5). Title: Demographic and Prerandomization Characteristics of the Patients at Baseline (Intent-to-Treat Population). Header No./Total (%), H n=260,N n=240. Bare counts use those group totals; explicit denominators supersede header. Order H;N.

| Key | Row/group | H printed | N printed |
|---|---|---|---|
| M049 | Sex | Men207(79.6);women53(20.4) | Men194(80.8);women46(19.2) |
| M050 | Age mean(SD),y | 35.0(13.5) | 34.1(13.4) |
| M051 | GCS overall median(IQR) | 6(4–7) | 6(4–7) |
| M052 | GCS motor median(IQR) | 3(1–4) | 3(2–5) |
| M053 | One/both pupils reacting | 220(84.6) | 202(84.2) |
| M054 | Hypotension out-of-hospital/ED | 26/257(10.1) | 27/239(11.3) |
| M055 | Hypoxia out-of-hospital/ED | 37/256(14.5) | 39/237(16.5) |
| M056 | Scene temperature mean(SD),°C | 36.0(1.2) | 35.9(1.0) |
| M057 | CT diffuse I normal | 18(6.9) | 17(7.1) |
| M058 | CT diffuse II | 152(58.5) | 128(53.3) |
| M059 | CT diffuse III/IV | 18(6.9) | 20(8.3) |
| M060 | CT evacuated massV;nonevacuatedVI | 69(26.5);3(1.2) | 72(30.0);3(1.3) |
| M061 | Probability unfavorable6mo,IMPACT-TBI(core+CT),mean(SD) | 0.46(0.24) | 0.46(0.23) |
| M062 | Injury Severity Score median(IQR) | 26.0(18.0–34.0) | **20.0(20.5–35.0)** literal visual reading |
| M063 | Cause:vehicle;motorcycle;bicycle;pedestrian | 84(32.3);29(11.2);20(7.7);28(10.8) | 89(37.1);18(7.5);20(8.3);37(15.4) |
| M064 | Cause:hit by object;fall/jump;other | 24(9.2);60(23.1);15(5.8) | 16(6.7);54(22.5);6(2.5) |
| M065 | Positive ethanol;ethanol>51mg/dL | 92/208(44.2);74/208(35.6) | 89/193(46.1);69/193(35.8) |
| M066 | Injury→randomization median(IQR),h | 1.8(1.0–2.7) | 2.0(1.1–2.8) |

Table 1 footnotes mapped with corresponding keys: a highest reliable prerandomization GCS,overall range3–15,lower=lower consciousness,GCS6 unconscious. b some GCS>3 with small unreactive pupils. c hypotensionSBP<90mmHg. d hypoxiaSpO₂<90%. e scene temperature availableH162,N143. f MarshallI–VI;I normal,II diffuse,III/IV raisedICP signs,V/VI mass lesion;firstCT;evacuated hematoma<24h with preoperative firstCT classifiedV. g IMPACT valid GCS<13,6mo poorGOS-E≤4 probability0–1,1=100%,covariates age,motor,pupil,hypoxia,hypotension,CT. h Injury Severity Score0–75,higher=greater severity,27 severe/multitrauma.

## Figure 2 and non-ITT pneumonia

Source [Figure 2 p6](../../../jama_cooper_2018_oi_180132.pdf#page=6). Figure title hourly temperature and ICP first4d(96h) postrandomization,N=500. Visual source inspection confirms complete axis/caption mapping.

| Key | Element | Exact mapping |
|---|---|---|
| M067 | Figure2A axes/data | Temperature°C,y ticks28,30,32,34,36,38,40,42; x ticks0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96h. H blue,N pale boxes. Observed box medians/IQR/whiskers are plotted without printed numeric labels; H drops toward33°C then rises after72h, N near37°C. Do not treat visual readings as exact numeric estimates. |
| M068 | Figure2A H patient counts | At0 then intervals1–6,7–12,…,91–96h:162,258,260,258,253,248,242,238,236,229,225,227,223,197,193,185,185. |
| M069 | Figure2A N patient counts | Same positions:143,234,238,234,231,224,222,217,214,208,205,202,200,190,189,187,183. |
| M070 | Figure2B axes/data | ICPmmHg,y ticks0,5,10,15,20,25,30,35;same x ticks0–96 by6;16 interval boxes per arm,no0h box. H/N trajectories similar near low-teens mmHg; values unlabelled. |
| M071 | Figure2B counts | Intervals1–6 through91–96h,H133,193,194,188,192,189,188,187,183,178,176,175,172,167,164,159;N132,181,181,179,183,178,176,173,173,167,166,162,158,151,150,142. |
| M072 | Figure2 caption | Observed,no imputation;box25th–75th percentile,interior median;whiskers furthest within1.5IQR;line connects6h-block medians;offset boxes;right tick included;0–6 represents1–6,6–12 represents7–12;unique contributors per interval,up to6 hourly observations each;per-patient observations mediantemperature6(IQR5–6),ICP6(IQR6–6). |
| M073 | p6 per-protocol pneumonia | H70.5%,N57.1%;absoluteRD13.3%(CI2.4–24.2);unadjustedRR1.23(1.04–1.47),P=.02;eTable9. |
| M074 | p6 as-treated pneumonia | H70.7%,N54.6%;RD16.1%(5.7–26.5);unadjustedRR1.29(1.09–1.53),P=.003;eTable11. Sensitivity analyses consistent(eFigures5,7). |

## Table 2 complete transcription and matching claims

Source [Table 2 and Figure 3 p7](../../../jama_cooper_2018_oi_180132.pdf#page=7). Title Primary and Secondary Outcomes, Adverse Events, and Subgroups. Intention-to-treat; n/N(%) unless indicated. Difference H−N in percentage points; RR H/N; all95%CI. Primary/secondary binary unadjustedχ² per M028; adjustment only expressly specified row M076. Printed bleeding rows retained literally and not reassigned.

| Key | Outcome | H n/N(%) | N n/N(%) | Absolute difference(95%CI) | RR(95%CI) | P |
|---|---|---|---|---|---|---|
| M075 | FavorableGOS-E5–8 | 117/240(48.8) | 111/226(49.1) | −0.4(−9.4 to8.7) | 0.99(0.82–1.19) | .94 |
| M076 | Severity-adjusted favorable,IMPACT-TBI | Not repeated | Not repeated | Not printed | 0.98(0.87–1.11) | .75 |
| M077 | Death in hospital | 52/260(20.0) | 43/239(18.0) | 2.0(−4.9 to8.9) | 1.11(0.77–1.60) | .57 |
| M078 | Death6mo | 54/256(21.1) | 44/239(18.4) | 2.7(−4.3 to9.7) | 1.15(0.80–1.64) | .45 |
| M079 | Pneumonia | 143/260(55.0) | 123/240(51.3) | 3.8(−5.0 to12.5) | 1.07(0.91–1.27) | .40 |
| M080 | Bacteremia | 19/260(7.3) | 12/240(5.0) | 2.3(−1.9 to6.5) | 1.46(0.72–2.95) | .29 |
| M081 | Other infection | 36/260(13.8) | 38/240(15.8) | −2.0(−8.2 to4.3) | 0.87(0.57–1.33) | .53 |
| M082 | New/increased intracranial bleeding | 47/260(18.1) | 37/240(15.4) | 2.7(−3.9 to9.2) | **1.23(0.43–3.5)** | **.70** |
| M083 | New significant extracranial bleeding | 8/260(3.1) | 6/240(2.5) | 0.6(−2.3 to3.5) | **1.17(0.79–1.74)** | **.43** |
| M084 | Surgically removed hematomas:yes;no | 22/66(33.3);95/174(54.6) | 27/68(39.7);84/158(53.2) | −6.4(−22.6 to9.9);1.4(−9.3 to12.2) | 0.84(0.54–1.32);1.03(0.84–1.25) | .44;.79 |
| M085 | Any intracranial mass lesionV+VI:yes;no | 22/69(31.9);95/171(55.6) | 28/71(39.4);83/155(53.5) | −7.6(−23.4 to8.3);2.0(−8.8 to12.8) | 0.81(0.52–1.27);1.04(0.85–1.27) | .35;.72 |

M075 matches p5 narrative exactly (absoluteRD−0.4 percentage points), and p1 M007 apart from its independently recorded printed sign. M076 matches p5 qualitative adjusted similarity. M078 matches p5 all cells. p5 ordinalGOS-E gives unadjustedOR0.97(0.71–1.34),P=.88; p5 time-to-death unadjustedHR1.13(0.76–1.69),P=.54,points to eFigure2. These two additional inferential relationships belong to M078's secondary-result bundle and must each receive a statistical inventory entry. M079/M082 match p1/p5 adverse-event percentages. Table 2 footnote b repeats IMPACT definition from Table1; c treatment×surgically removed hematoma interactionP=.43;d treatment×any mass lesion interactionP=.33; p6 narrative says neither interaction significant. Each interaction is a separate statistical relationship under M084/M085.

M086 — Figure 3: title GOS-E distribution at6 months **after randomization** (primary descriptions specify after injury). Two stacked horizontal percentage bars(H,N),x ticks0–100 by10;each cell width proportion with score;vertical hyphenated line indicates midpoint dichotomy. Legend1death,2vegetative,3lower severe disability,4upper severe disability,5lower moderate disability,6upper moderate disability,7lower good recovery,8upper good recovery;5–8 favorable. No exact cell percentages/counts printed: graph is a visual distribution, not additional precise tabular values. Visual split near51% unfavorable in each group agrees with displayed favorable proportions; source graphic contains all8 ordered categories per arm. p6–p7 post hoc narratives state no significant differences for missingness scenarios(eTable12) or adequate-dose versus controls(eTable13); p7 discussion states no increased favorable outcomes and no benefit in secondary outcomes,mortality,prespecified subgroups,per-protocol/as-treated analyses. Three prior higher-quality trials had no benefit,two ended≤50% projected sample;historical only.

## Discussion and remaining units

M087 — [p8 discussion/limitations](../../../jama_cooper_2018_oi_180132.pdf#page=8): protocol≥72h;initiation median1.8h;time-to33°C>10h;most cooled>48h;rewarming median22.5h;34 rewarming pauses;noICP/therapy-intensity effect;per-protocol pneumonia increased;3 infusion-syndrome episodes. Limitations explicitly print19% hypothermia withdrawn early and a further13% did not reach33°C. Record alongside p4's27% never final33°C and71.5% reached, without recasting denominators. Blinded assessors contrasted with unblinded clinicians/families. Conclusions repeat no6mo neurologic improvement with earlyH.

M088 — [p8 article information](../../../jama_cooper_2018_oi_180132.pdf#page=8): acceptedOctober8,2018;publishedOctober24,2018;correctionNovember12,2018 mentions IMPACT-TBI score in Methods. No change history inferred. p9 independent statistical review named and Supplement3 sharing pointer;no additional result estimates. p9–10 references contain bibliography/calendar/page/identifier numbers only;not trial-result relationships,not followed externally.

## Handoff completeness and limitations

88 local evidence bundles M001–M088 cover all10 pages, both complete tables,all3 figures,all matching quantitative narrative and abstract claims,all analysis-method and design specifications relevant to results. Many bundles have multiple component relationships; global inventories must expand,not treat88 as an upper limit. Explicit additional inferential components: ordinalOR,time-to-deathHR,both interaction tests,power,adjustedRR,all unadjusted table rows,and both non-ITT pneumonia results. No scientific coverage gap. Source graphics do not print exact Figure2 box quartiles/whiskers or Figure3 category shares;their complete visible structure is recorded,with no invented numerical extraction. Historical engines are unrecorded but the curator established direct-source native matching. No source or reused artifact was altered.
