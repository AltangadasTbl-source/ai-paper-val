# Complete Numeric Relationship Inventory

Coordinator assigns contiguous stable N IDs to the complete disjoint numeric-origin union. Local aliases remain traceable in numeric_id_map.tsv and preserved specialist parts. All 400 relationships checked; each numeric shard contains at most 120 relationships.

# Numeric relationship inventory — main article origins pages 1–6

Runtime: `01a1286a-6645-7930-8d1b-45686ffab070`; fresh numeric reviewer `gpt-6.1-sol`/`medium`. Scope: DOC-001 (`jama_flint_2019_oi_190079.pdf`) PDF pp.1–6. Origin scope is disjoint from the pages7–10/results-supplement and PLAN numeric shards. Counterpart locations outside pp.1–6 are used only to check a first-six-page origin. O=sertraline+olanzapine (64); P=sertraline+placebo (62). Every location in DOC-001 is REPORT. DOC-003 eFigure8 is REPORT. No PLAN conflict is emitted by this shard.

Source authority: direct Poppler26.01.0 `pdftotext -layout` stdout for pp1–6, targeted pp3/4; current complete main/support maps as locators; source-matched reused rendered pp5/6 visually inspected. No new derivatives, OCR, Python, GPU, web, old checker/candidate/report inputs. Direct source files preserved. Each numbered row is one quantitative relationship; a row may test both arms or several components of one partition. Inferential P-value/test calculations belong to the statistical reviewer; numeric estimate/unit/repeat relationships are covered here.

Tolerances: integer totals exact; one-decimal percentages normally ±0.05 percentage points with midpoint ties accepted in either direction; percentage sums permit cumulative displayed rounding, never unexplained integer deficits. Rounded group means/SDs admit their displayed precision. A result labeled COMPATIBLE is not a finding or adjudication. There is no candidate limit.

| Local relationship | Exact source scope | Printed inputs and reproducible check | Tolerance/identity condition | Outcome |
|---|---|---|---|---|
| N001 | Abstract arm allocation; pp1/3/6 | 64+62=126; all printed randomized totals126 | Exact count | Reconciles |
| N002 | Abstract women; p1 versus Table1 p5 | 37+41=78; 78/126×100=61.9048%, printed61.9% | ±0.05pp | Reconciles |
| N003 | Abstract completion; p1 versus flow p3 | 43+24+13+34=114; 126−8−4=114;114/126×100=90.4762%, printed90.5% | ±0.05pp | Reconciles: includes relapse endpoints; completion in remission alone67 is a different node |
| N004 | Abstract mean age; p1 versus Table1 p5 | (64×55.0+62×55.7)/126=55.3444, printed55.3 | ±0.1y allowing component rounding | Reconciles |
| N005 | Abstract age SD; p1 versus Table1 p5 | Pooled SD from rounded group moments≈14.946, printed14.9 | Group SD rounding ±0.05; final±0.05 | Compatible rounding; raw moments unavailable |
| N006 | Relapse O; pp1/2/6 | 13/64×100=20.3125%, printed20.3%; same count/denominator repeated | ±0.05pp | Reconciles |
| N007 | Relapse P; pp1/2/6 | 34/62×100=54.8387%, printed54.8%; same count/denominator repeated | ±0.05pp | Reconciles |
| N008 | Relapse treatment measure; pp1/6 | Adjusted Cox HR0.25(0.13–0.48); crude RR=(13/64)/(34/62)=0.3704 | Distinct adjusted time-to-event vs crude risk estimands | No discrepancy: HR is correctly named; crude RR need not equal HR |
| N009 | Abstract sertraline median; p1/Table2 p6 | Pooled150(150–200) versus both arms150(150–200)mg/day | Quantile identity not guaranteed by group summaries | Compatible; no reconstruction of pooled IQR claimed |
| N010 | Abstract olanzapine median; p1/Table2 p6 | Pooled15(10–20) versus both arms15(10–20)mg/day | Quantile identity not guaranteed | Compatible |
| N011 | Abstract daily weight; p1/p7 | 0.13lb/day (0.11–0.15) repeats; treatment×linear-time; quadratic time also present | Printed precision | Reconciles; do not multiply by252 to equate with raw change |
| N012 | Abstract daily waist; p1/p7 | 0.009in/day (0.004–0.014) repeats | Printed precision | Reconciles; same model restriction |
| N013 | Abstract daily total cholesterol; p1/p7 | 0.29mg/dL/day (0.13–0.45) repeats | Printed precision | Reconciles; coefficient not a raw endpoint difference |
| N014 | Abstract daily LDL; p1/p7 | 0.04mg/dL/day (−0.01–0.10) repeats | Printed precision | Reconciles |
| N015 | Abstract daily HDL; p1/p7 | −0.01mg/dL/day (−0.03–0.01) repeats | Printed precision | Reconciles |
| N016 | Abstract daily triglyceride; p1/p7 | −0.153mg/dL/day (−0.306–0.004) repeats; pattern-mixture averaged | Printed precision | Reconciles; distinct calculation conventions retained |
| N017 | Abstract daily glucose; p1/p7 | −0.02mg/dL/day (−0.12–0.08) repeats | Printed precision | Reconciles |
| N018 | Abstract daily HbA1c; p1/p7 versus Table4 p8/eFigure8 DOC003 p9 | −0.0002 printed mg/dL; Table4 and figure label HbA1c% | Exact dimensional identity | RF-CAND-05 |
| N019 | Enrollment stages; Fig1 p3/p6 | 350−81=269; p6 enrolled269 | Exact counts | Reconciles; consented and enrolled denote different stages |
| N020 | Excluded reasons; Fig1 p3 | 60+16+5=81 | Exact counts | Reconciles |
| N021 | Acute exit; Fig1 p3 | 269−74=195 | Exact counts | Reconciles |
| N022 | Acute discontinuation reasons; Fig1 p3 | 31+21+7+5+1+9=74 | Exact counts | Reconciles |
| N023 | Acute-to-stabilization; Fig1 p3 | 195−33=162 | Exact counts | Reconciles |
| N024 | Stabilization exit; Fig1 p3 | 162−15=147 | Exact counts | Reconciles |
| N025 | Stabilization discontinuation reasons; Fig1 p3 | 4+2+1+1+7=15 | Exact counts | Reconciles |
| N026 | Stabilization-to-randomization; Fig1 p3 | 147−21=126 | Exact counts | Reconciles |
| N027 | Not randomized reasons; Fig1 p3 | 12+9=21 | Exact counts | Reconciles |
| N028 | O allocation receipt; Fig1 p3 | 59+5=64;3+2=5 | Exact counts | Reconciles |
| N029 | P allocation receipt; Fig1 p3 | 60+2=62;1+1=2 | Exact counts | Reconciles |
| N030 | O disposition; Fig1 p3 | 43+13+8=64;1+5+1+1=8 | Exact counts | Reconciles |
| N031 | P disposition; Fig1 p3 | 24+34+4=62;1+3=4 | Exact counts | Reconciles |
| N032 | Analysis population; pp3/4/6 | ITT64/62 includes not-as-randomized5/2;119 received allocation vs126 analyzed | Different stages | Reconciles; treatment receipt not analysis exclusion |
| N033 | Acute eligibility/time; pp1/2/3 | 18–85 actual age eligibility satisfies abstract≥18;acute≤12wk; stabilization8wk; randomized36wk | Exact definitions | Compatible; summary lower bound is not an alternative upper bound |
| N034 | Remission/near-remission; pp2/3 | HDRS≤10 vs11–15 with≥50% improvement; no psychosis;MMSE≥24 | Disjoint threshold definitions | No concrete numeric conflict |
| N035 | Randomization strata/sites; pp2/4/5 | 18–59/60–85 partitions eligibility;4 named sites;1:1 target with actual64/62 | Blocked allocation may differ overall | Compatible |
| N036 | Intervention/visit schedule; pp1/4 | 4-week taper, weekly first8wk then every4wk through36wk; metabolic every8wk plus termination | Exact time units | Compatible; terminal observations may differ by relapse |
| N037 | Relapse thresholds; p4 | ≥1 criterion;HDRS≥18 vs baseline remitted≤15 | Threshold identity | Compatible; event criteria can overlap |
| N038 | Barnes incident rule/range; pp4/6 | Global0–5;baseline0 then≥2; Table2 positive baseline3/2 participants differs from incident | Exact population/time definitions | Compatible |
| N039 | AIMS descriptions; pp4/6 | p4 each10items0–5;Table2 global0–4;global-positive2/2 participants | Individual items versus named global summary not demonstrably identical | No emitted candidate: item mapping absent; no arithmetic contradiction in reported counts |
| N040 | Simpson-Angus range; pp4/6 | 0–40 methods vs0–36 Table2 explicitly excluding head-dropping | Different item sets | Compatible |
| N041 | UKU adverse-effect range/rule; p4 | Each48items0–3;rule2-point increase or score3or4 with increase | Exact integer range | RF-CAND-04 |
| N042 | Weight threshold; pp4/5 | Gain/loss>7% relative premorbid most-recent pre-episode weight; Table1 same reference definition | Strict thresholds and reference identity | Compatible within main report; PLAN definitions reviewed separately |
| N043 | Power/NNT; p4 | 20% absolute risk difference⇒1/0.20=5;80% power,176 revised128; observed126 | Exact reciprocal;planned vs observed distinct | Reconciles; no observed-vs-target discrepancy claimed |
| N044 | Statistical conventions; pp4/5/6 | All randomized;Cox adjusted3 strata;MAR/pattern-mixture;2-sided overall5%;Holm secondary post hoc | Estimates retain stated model/test identity | No numeric contradiction; inferential diagnostics delegated |
| N045 | Table1 Age means/SD; p5 | 55.0(15.1)/55.7(14.9); Within eligibility18–85; component/pooled repeats N004/005 | Printed resolution; no raw reconstruction | Compatible |
| N046 | Table1 Age18–59; p5 | O36(56.2):100×36/64=56.2500%; P36(58.1):100×36/62=58.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N047 | Table1 Age≥60; p5 | O28(43.8):100×28/64=43.7500%; P26(41.9):100×26/62=41.9355% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N048 | Table1 Men; p5 | O27(42.2):100×27/64=42.1875%; P21(33.9):100×21/62=33.8710% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N049 | Table1 Women; p5 | O37(57.8):100×37/64=57.8125%; P41(66.1):100×41/62=66.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N050 | Table1 White; p5 | O54(84.4):100×54/64=84.3750%; P49(79):100×49/62=79.0323% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N051 | Table1 Black; p5 | O6(9.4):100×6/64=9.3750%; P9(14.5):100×9/62=14.5161% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N052 | Table1 Other race; p5 | O4(6.3):100×4/64=6.2500%; P4(6.5):100×4/62=6.4516% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N053 | Table1 Hispanic; p5 | O6(9.4):100×6/64=9.3750%; P9(14.5):100×9/62=14.5161% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N054 | Table1 Single; p5 | O19(29.7):100×19/64=29.6875%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N055 | Table1 Married; p5 | O28(43.8):100×28/64=43.7500%; P35(56.5):100×35/62=56.4516% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N056 | Table1 Separated/divorced; p5 | O12(18.8):100×12/64=18.7500%; P7(11.3):100×7/62=11.2903% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N057 | Table1 Widowed; p5 | O5(7.8):100×5/64=7.8125%; P5(8.1):100×5/62=8.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N058 | Table1 Education; p5 | 14.4(3.2)/13.4(3.9)y; Nonnegative mean/SD; distinct age/education labels | Printed resolution; no raw reconstruction | Compatible |
| N059 | Table1 With others; p5 | O46(71.9):100×46/64=71.8750%; P49(79):100×49/62=79.0323% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N060 | Table1 Alone; p5 | O17(26.6):100×17/64=26.5625%; P10(16.1):100×10/62=16.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N061 | Table1 Senior residence; p5 | O1(1.6):100×1/64=1.5625%; P1(1.6):100×1/62=1.6129% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N062 | Table1 Inpatient acute baseline; p5 | O41(64.1):100×41/64=64.0625%; P46(74.2):100×46/62=74.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N063 | Table1 Cornell; p5 | O16(25):100×16/64=25.0000%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N064 | Table1 Massachusetts; p5 | O15(23.4):100×15/64=23.4375%; P14(22.6):100×14/62=22.5806% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N065 | Table1 Pittsburgh; p5 | O9(14.1):100×9/64=14.0625%; P10(16.1):100×10/62=16.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N066 | Table1 Toronto; p5 | O24(37.5):100×24/64=37.5000%; P23(37.1):100×23/62=37.0968% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N067 | Table1 ≥2 lifetime episodes; p5 | O47(73.4):100×47/64=73.4375%; P47(75.8):100×47/62=75.8065% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N068 | Table1 Episode duration; p5 | 5.5(3–12)/5.5(2–12)mo;P n60; Median inside IQR;missingP2; explicit n≤62 | Printed resolution; no raw reconstruction | Compatible |
| N069 | Table1 First episode age; p5 | 37(24–50)n62/35(18–51)n61; Median inside IQR;missingO2/P1; onset precedes current group age on average | Printed resolution; no raw reconstruction | Compatible; no participant pairing inferred |
| N070 | Table1 Suicide attempt; p5 | O13(20.3):100×13/64=20.3125%; P12(19.4):100×12/62=19.3548% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N071 | Table1 Resistance; p5 | O3(4.7):100×3/64=4.6875%; P5(8.1):100×5/62=8.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N072 | Table1 Hyperlipidemia; p5 | O18(29):100×18/64=28.1250%; P19(29.7):100×19/62=30.6452% | ±0.05pp; exact .05 ties allow either nearest endpoint | RF-CAND-01 |
| N073 | Table1 Hypertension; p5 | O17(26.6):100×17/64=26.5625%; P22(35.5):100×22/62=35.4839% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N074 | Table1 Diabetes; p5 | O12(18.8):100×12/64=18.7500%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| N075 | Table1 Premorbid weight; p5 | 166.6(34.6)n60/171.4(40.2)n59lb; MissingO4/P3;nonnegative means/SD;lb consistent with stated conversion | Printed resolution; no raw reconstruction | Compatible |
| N076 | Table1 age/sex/race sums; p5 | O36+28=64;27+37=64;54+6+4=64;P36+26=62;21+41=62;49+9+4=62 | Exact counts;rounded percentages need not sum exactly100 | Reconciles; race Other includes unknown |
| N077 | Table1 marital/site sums; p5 | O19+28+12+5=64;16+15+9+24=64;P15+35+7+5=62;15+14+10+23=62 | Exact counts | Reconciles |
| N078 | Table1 living sums; p5 | O46+17+1=64;P49+10+1=60≠62;P79.0+16.1+1.6=96.7% | Exact counts;rounded sum tolerance≤0.15pp | RF-CAND-02 |
| N079 | Table2 HDRS; p6 | 5.3(3.6)/5.6(3.6),scale0–52 higher worse; mean rounded5 footnote | ±0.5 for integer summary | Compatible |
| N080 | Table2 delusions; p6 | 64/64=100%;62/62=100%; score1 absent,range1–7 | Exact100 and score definitions | Reconciles |
| N081 | Table2 hallucinations; p6 | 64/64=100%;62/62=100%; score1 absent,range1–3 | Exact100 and score definitions | Reconciles |
| N082 | Table2 HADS; p6 | 5(2–8)/4(1–7)n61,range0–21,≤7 normal | IQR order; missingP1 explicit | Reconciles; IQR may extend beyond normal despite median normal |
| N083 | Table2 CORE; p6 | 1(0–3)/1(0–4.8),range0–54;median1 minimal | IQR order; interpolation allows decimal4.8 | Reconciles |
| N084 | Table2 CIRS; p6 | 3(1–6)/3(2–5.8),range0–52;excludes psychiatric category | IQR order; interpolation allows decimal5.8 | Reconciles |
| N085 | Table2 MMSE; pp3/6 | 28.1(1.9)/27.9(2.0),range0–30;eligible≥24;footnote mean28 | ±0.5 integer summary; mean≤30 | Reconciles; SD alone cannot establish individual eligibility violation |
| N086 | Table2 DKEFS trails; p6 | 7.9(3.5)n61/8.1(3.6)n59;footnoteh scaled1–19 higher better,normative10 | MissingO3/P3;means within range | Reconciles |
| N087 | Table2 DKEFS color-word/footnote; p6 | 8.6(2.9)n60/7.6(2.8)n58,rowsuperscripti;footnotei Barnes0–5,footnoteh both DKEFS1–19 | Exact footnote identity;means>5 | RF-CAND-03 |
| N088 | Table2 Barnes positive; p6 | 3.0(4.7)/2.0(3.2);3/64=4.6875%;2/62=3.2258% | ±0.05pp;decimal integer counts | Reconciles; default No.(%) is explicit |
| N089 | Table2 AIMS positive; p6 | 2.0(3.1)/2.0(3.2);2/64=3.125%;2/62=3.2258%;global0–4 | ±0.05pp | Reconciles; threshold>0 baseline not incident criterion |
| N090 | Table2 Simpson-Angus; p6 | 1(0–2)/1(0–2),range0–36 excluding item | Exact range and IQR order | Reconciles |
| N091 | Table2 sertraline; pp1/2/6 | 150(150–200)mg/day both;target150–200;50mg pills | Median/IQR within target | Reconciles |
| N092 | Table2 olanzapine; pp1/2/6 | 15(10–20)mg/day both;target15–20;5mg pills | Observed tolerated dosage distinct from target | Compatible;IQR10 not a target adherence inconsistency |
| N093 | Unit conversions; pp5/6 | lb×0.45kg repeated;cholesterol×.0259,glucose×.0555,triglyceride×.0113 to mmol/L;in×2.54cm | Compare internal repeated factors;no external reference | Reconciles; .45 is displayed approximate factor |
| N094 | Secondary time units/count distinction; pp1/4/6 | Daily linear-time interaction anthropometric/metabolic,weekly/four/eight-week assessment schedule;incident participants descriptive | Different parameter/observation units | No rate/count confusion; no person-time totals supplied |
| N095 | Primary age contrast; p6 | HR0.78(0.42–1.46),young vsold; groups defined18–59 vs60–85 | Exact label/reference identity;statistical pass handles interval/P | Compatible |
| N096 | Secondary significance prose; p1/p6/p7 | Weight/waist/total cholesterol significant;LDL/HDL/triglyceride/glucose/HbA1c not;Holm adjusted post hoc | Same coefficient contrast and exploratory convention | No arithmetic contradiction; full P/CI diagnostics statistical lane |

Completed 96 relationships. Five distinct local candidates RF-CAND-01 through RF-CAND-05. All assigned source pages and mapped quantitative components inspected; no scientific coverage gap. Limitation: no raw data, paired individual values, unprinted living-arrangement missingness category, or explicit hyperlipidemia denominator supplied. Item-level AIMS mapping does not establish identity with its global summary, so differing ranges alone do not support a candidate. No display-zero P occurs in this scope. Planned power cannot be reconstructed without unprinted assumptions and is not treated as a candidate merely for those omissions. Stable N/C IDs belong to coordinator.



# Numeric relationship inventory: late main report and complete results figures

Runtime UUID: 01a1286a-814f-7b12-a00b-e90ab6064dbe. Fresh numeric-review shard, gpt-6.1-sol/medium. Disjoint origins: DOC-001 physical pp7–10 and DOC-003 pp1–10. Earlier main-paper pages are comparators only. All locations in this shard are REPORT by content. No PLAN-origin relationship is assigned here. Local RL IDs are locators; coordinator assigns global N IDs.

Sources: [main article](../../../jama_flint_2019_oi_190079.pdf#page=7), [results supplement](../../../joi190079supp2_prod.pdf#page=1). Current complete mapper artifacts read; reusable native/rendered assets used as source locators. All nine plots visually inspected; direct Poppler pdftotext source output inspected for main pp7–10 and methods comparator p5. Legacy renders engine PyMuPDF, historical version unavailable. No fresh derivative written, OCR/fallback/web/Python/GPU used. Direct source is final authority.

O=sertraline+olanzapine, P=sertraline+placebo; O64/P62 randomized. Rounding tolerance is half a displayed last unit: ±0.05 percentage point for one-decimal percentages, ±0.005 for two-decimal effects; exact counts have zero tolerance. Printed blanks remain blanks. Paired raw changes, marginal means, model means, mixed-model linear/time² coefficients, pattern-mixture averages, and Poisson model coefficients are not conflated. Holm-adjusted P values are not directly inverted from unadjusted CI widths; exactCIb rows are not forced to normal symmetry. No P display zero occurs.

| Local ID | Source locations, all REPORT | Printed inputs / bounded plot readings | Checks and reproducible rule | Completion |
|---|---|---|---|---|
| N097 | DOC-001 p7 Table3 depression only | O5/P18 | Counts nonnegative; compare mutually exclusive depression/psychosis presentations without equating total events to persons. | COMPLETE |
| N098 | DOC-001 p7 Table3 psychosis only | O0/P1 | Counts, zero accepted. | COMPLETE |
| N099 | DOC-001 p7 Table3 depression and psychosis | O4/P11 | Counts and presentation label. | COMPLETE |
| N100 | DOC-001 p7 Table3 suicide | O0/P3 | Overlapping relapse event count, not independent persons. | COMPLETE |
| N101 | DOC-001 p7 Table3 mania | O0/P0 | Repeated zeros plausible, no contradictory event supplied. | COMPLETE |
| N102 | DOC-001 p7 Table3 hospitalization | O6/P11 | Matched p8 hospitalization numerators. | COMPLETE |
| N103 | DOC-001 p7 Table3 footnotes a,b; p6 relapsers | O events15 vs persons13; P events44 vs persons34 | 5+0+4+0+0+6=15;18+1+11+3+0+11=44. Footnote explicitly permits multiple events. | COMPLETE |
| N104 | DOC-001 p8 hospitalization O | 6/13 (46.2%) | 100×6/13=46.153846; rounding to nearest0.1 gives46.2. | COMPLETE |
| N105 | DOC-001 p8 hospitalization P | 11/34 (32.3%) | 100×11/34=32.352941; rounding to nearest0.1 gives32.4; deviation.052941 percentage point. | CANDIDATE RL-CAND-01 |
| N106 | DOC-001 p7 Cox remission contrast | 2.45;95%CI.98–6.13;P=.06;remission vs near-remission | Positive HR inside ordered positive interval; no reversal inferred from outcome frequency unreported by remission stratum. | COMPLETE |
| N107 | DOC-001 p7 Cox Massachusetts | 1.53;.62–3.76;P=.36;vsCornell | Containment, order, ratio measure/reference. | COMPLETE |
| N108 | DOC-001 p7 Cox Pittsburgh | 1.09;.39–2.98;P=.88;vsCornell | Containment, order, ratio measure/reference. | COMPLETE |
| N109 | DOC-001 p7 Cox Toronto | 1.80;.81–4.03;P=.15;vsCornell | Containment, order, ratio measure/reference. | COMPLETE |
| N110 | DOC-001 p7 sensitivity Cox | Excluded7;HR.22;.11–.43;P<.001 | Distinct population from all-randomized .25;.13–.48; exclusion count matches p3 allocation nonadherence5+2=7 without equating dispositions. | COMPLETE |
| N111 | DOC-001 pp7,8 NNT | 2.8;based on HR;all-randomizedHR.25 | Repeated2.8 agrees. Crude count NNT=1/(34/62−13/64)=2.896350364964. Paper explicitly HR-based; no supplied survival-at-time formula/baseline prediction, so crude/model identity not required. | COMPLETE_METHOD_BOUNDARY |
| N112 | DOC-001 p7 Figure2 O risk counts | weeks0/4/8/12/16/20/24/28/32/36:64/60/57/56/52/52/49/47/44/43 | Monotone nonincrease; endpoint43 matches p3 completion; overall reduction21=13relapse+8other exits. | COMPLETE |
| N113 | DOC-001 p7 Figure2 P risk counts | 62/54/39/36/32/31/28/26/25/24 at same weeks | Monotone nonincrease; endpoint24 matches p3 completion; reduction38=34relapse+4other exits. | COMPLETE |
| N114 | DOC-001 p7 Figure2 curves | O final≈.78,P≈.44;log-rankP<.001;shading95%CI | Probability bounded0–1, O aboveP; Kaplan–Meier with censoring not equated to raw13/64 or34/62. No exact coordinates. | COMPLETE |
| N115 | DOC-001 p7 Figure2 duration; p9 discussion | O36(IQR24.8–36),P19.5(5.3–36);50%P≤20weeks | Quartile order and support0–36; median19.5 supports half≤20; exact count not reconstructable. | COMPLETE |
| N116 | DOC-001 p8 timing narrative; p7 Figure2 | Majority P relapses≤12weeks | 62−36=26 lost from risk set by12weeks. Even subtract all4 nonrelapse exits leaves≥22relapses, >34/2=17. | COMPLETE |
| N117 | DOC-001 p7 weight model | 0.13lb/day;CI.11–.15;adjustedP<.001 | Estimate positive contained, narrative higher, match abstract; time² forbids cumulative extrapolation. | COMPLETE |
| N118 | DOC-001 p7 waist model | 0.009in/day;CI.004–.014;adjustedP=.002 | Positive contained, correct unit/direction, abstract match. | COMPLETE |
| N119 | DOC-001 p7 total cholesterol model | 0.29mg/dL/day;CI.13–.45;adjustedP=.003 | Positive contained, unit/direction, abstract match; relative slope can be positive while both levels decline. | COMPLETE |
| N120 | DOC-001 p7 LDL model | 0.04mg/dL/day;CI−.01–.10;adjustedP=.57 | Containment, zero inclusion and nonsignificance, abstract match. | COMPLETE |
| N121 | DOC-001 p7 HDL model | −.01mg/dL/day;CI−.03–.01;adjustedP=.99 | Containment, zero inclusion, direction, abstract match. | COMPLETE |
| N122 | DOC-001 p7 triglyceride model | −.153mg/dL/day;CI−.306–.004;adjustedP=.25 | Containment and direction; averaged pattern-mixture not an individual dropout subgroup; abstract match. | COMPLETE |
| N123 | DOC-001 p7 glucose model | −.02mg/dL/day;CI−.12–.08;adjustedP=.99 | Containment, zero inclusion, abstract match; curved trajectory not endpoint/252. | COMPLETE |
| N124 | DOC-001 p7 HbA1c model; p8 Table4; DOC-003 p9 | −.0002mg/dL/day;CI−.0021–.0016;adjustedP=.99;Table4HbA1c%;plotHbA1c(%) | Printed incompatible unit labels for same analyte/output; estimate otherwise contained and matches abstract. | CANDIDATE RL-CAND-04 |
| N125 | DOC-001 p7 statin sensitivity | 12:O6/P6 | 6+6=12; counts patients starting/changing, not dose changes/events. | COMPLETE |
| N126 | DOC-001 p7 hypoglycemic sensitivity | 3:O2/P1 | 2+1=3; distinct drugs/subanalysis, no unprinted effect fabricated. | COMPLETE |
| N127 | DOC-001 p7–9 incidence narrative | No statistically significant between-group incident high metabolic differences | All four Table5 intervals contain0; no printed numericP, exactCI reserved b rows. | COMPLETE |
| N128 | DOC-001 p7 akathisia | O4.7%/P4.8%;all but1mild | Nearest integers under randomized denominators3/64=4.6875%,3/62=4.8387%; descriptive possibilities, not printed counts; mild exception arm unspecified. | COMPLETE |
| N129 | DOC-001 p7 tardive dyskinesia | O0%/P3.2% | Consistent potential0/64 and2/62; no count printed; not event rate. | COMPLETE |
| N130 | DOC-001 p7 Simpson–Angus; p5 Poisson; DOC-003 p10 | 0.022points/week;CI.009–.036;adjustedP=.009;plot≈O.56→.73,P.685→.40 over36weeks | Raw score slope contrast≈.01264points/week versus.022; log-slope contrast≈.02231/week. Model-scale question. | CANDIDATE RL-CAND-05 |
| N131 | DOC-001 p7 UKU gain | 17.2%/4.8% | Possible11/64 and3/62; repeated observations counted≥once; pooled14/126=11.11% supports>5% introduction. | COMPLETE |
| N132 | DOC-001 p7 UKU loss | 7.8%/4.8% | Possible5/64 and3/62;pooled8/126=6.35%, supports>5%. | COMPLETE |
| N133 | DOC-001 p7 sedation | 7.8%/3.2% | Possible5/64 and2/62;pooled7/126=5.56%, supports>5%. | COMPLETE |
| N134 | DOC-001 p7 dizziness | 7.8%/3.2% | Same plausible counts as sedation, distinct outcome; repeated percentages do not imply duplicated data. | COMPLETE |
| N135 | DOC-001 p7 nausea | 3.1%/8.1% | Possible2/64 and5/62;pooled7/126=5.56%, supports>5%; not required each arm>5%. | COMPLETE |
| N136 | DOC-001 p7 falls | 20/64(31.3%);11/62(17.7%) | 31.25→31.3 with half-up convention;17.74194→17.7.≥1 fall participants not number of falls. | COMPLETE |
| N137 | DOC-001 p7 SAE | 12/64(18.8%);12/62(19.4%) | 18.75→18.8;19.35484→19.4;participants≥1 event, not total events. | COMPLETE |
| N138 | DOC-001 pp7–8 SAE nature | 1Odeath ruptured aneurysm;all otherSAEs hospitalization | Not summed with psychiatric relapse hospitalizations; SAE distinct all-cause definition; no event total. | COMPLETE |
| N139 | DOC-001 p9 no relapse | 45%P did not relapse;P34/62 relapsed | 100×(62−34)/62=45.1613→45% at whole precision; includes censored/nonrelapsed persons, not 36-weekKM probability. | COMPLETE |
| N140 | DOC-001 pp8–9 4-week taper/36-week trial | 4weeks,36weeks | Matches earlier methods; external historical ages18–65 not current eligibility18–85. | COMPLETE |
| N141 | DOC-001 pp8–9 SI factors | cholesterol.0259;glucose.0555;triglyceride.0113;lb.45;in2.54 | Repeated factors match p6; units apply to levels and their differences. .45 is explicit rounded factor, no external correction. | COMPLETE |
| N142 | DOC-001 p9 Table5 total threshold | above both baseline and240mg/dL | Participant event ≥1 qualifying value;strict above threshold, not sum of repeated high values. | COMPLETE |
| N143 | DOC-001 p9 Table5 LDL threshold | above both baseline and160mg/dL | Separate outcome even when counts/intervals identical total cholesterol. | COMPLETE |
| N144 | DOC-001 p9 Table5 triglyceride threshold | above both baseline and200mg/dL | Participant incidence, exactCIb marker. | COMPLETE |
| N145 | DOC-001 p9 Table5 glucose threshold | above both baseline and126mg/dL | Participant incidence, exactCIb marker. | COMPLETE |
| N146 | DOC-001 p9 Table5 total percentages | 9/64(14.1%),6/62(9.7%) | 14.0625→14.1;9.677419→9.7;valid proportions. | COMPLETE |
| N147 | DOC-001 p9 Table5 LDL percentages | 9/64(14.1%),6/62(9.7%) | Same arithmetic, independently labeled outcome. | COMPLETE |
| N148 | DOC-001 p9 Table5 triglyceride percentages | 4/64(6.3%),2/62(3.2%) | 6.25→6.3half-up;3.225806→3.2. | COMPLETE |
| N149 | DOC-001 p9 Table5 glucose percentages | 4/64(6.3%),4/62(6.5%) | 6.25→6.3;6.451613→6.5. | COMPLETE |
| N150 | DOC-001 p9 Table5 total difference | 4.3percentage points;CI−8–17.2;9/64 vs6/62 | 100×(9/64−6/62)=4.385081→4.4 at nearest.1, outside4.3±.05. | CANDIDATE RL-CAND-02 |
| N151 | DOC-001 p9 Table5 LDL difference | 4.3percentage points;CI−8–17.2;9/64 vs6/62 | Separate matched outcome same calculation4.385081→4.4. | CANDIDATE RL-CAND-03 |
| N152 | DOC-001 p9 Table5 triglyceride difference | 3.0percentage points;CI−6.7–13.3exact | 100×(4/64−2/62)=3.024194→3.0;orderedCI contains estimate/zero;not forced symmetric. | COMPLETE |
| N153 | DOC-001 p9 Table5 glucose difference | −.2percentage points;CI−9.9–9.9exact | 100×(4/64−4/62)=−.201613→−.2;signed absolute unadjusted difference is O−P rather than absolute-value modulus. | COMPLETE |
| N154 | DOC-001 p8 Table4 Weight lb O | Baseline n,value=blank,178.6(39.4);termination=62,183.6(40.9);differenceCI=5.7(3.3–8.1) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N155 | DOC-001 p8 Table4 Weight lb P | Baseline n,value=60,182.5(39.8);termination=59,180.2(42.1);differenceCI=−3.1(−5.4–−.8) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N156 | DOC-001 p8 Table4 Waist inches O | Baseline n,value=63,38.1(5.4);termination=59,38.5(5.2);differenceCI=.6(.1–1.1) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N157 | DOC-001 p8 Table4 Waist inches P | Baseline n,value=58,39.4(5.7);termination=55,38.4(6.4);differenceCI=−.8(−1.5–−.2) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N158 | DOC-001 p8 Table4 Total cholesterol mg/dL O | Baseline n,value=63,209.0(51.3);termination=63,204.8(51.3);differenceCI=−4.7(−14.9–5.6) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N159 | DOC-001 p8 Table4 Total cholesterol mg/dL P | Baseline n,value=blank,220.4(46.8);termination=59,197.4(48.2);differenceCI=−22.3(−32.7–−11.9) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N160 | DOC-001 p8 Table4 LDL mg/dL O | Baseline n,value=62,132.5(42.1);termination=63,128.9(42.3);differenceCI=−2.8(−12.6–6.9) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N161 | DOC-001 p8 Table4 LDL mg/dL P | Baseline n,value=blank,137.7(38.7);termination=59,122.1(44.2);differenceCI=−16.0(−25.8–−6.2) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N162 | DOC-001 p8 Table4 HDL mg/dL O | Baseline n,value=63,54.4(19.6);termination=63,49.7(16.1);differenceCI=−5.0(−9.1–−.9) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N163 | DOC-001 p8 Table4 HDL mg/dL P | Baseline n,value=blank,56.0(16.0);termination=59,52.2(16.0);differenceCI=−3.5(−6.2–−.9) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N164 | DOC-001 p8 Table4 HbA1c % O | Baseline n,value=63,5.9(1.5);termination=62,5.7(1.1);differenceCI=−.2(−.5–.2) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N165 | DOC-001 p8 Table4 HbA1c % P | Baseline n,value=blank,5.9(1.2);termination=58,5.9(1.0);differenceCI=.1(−.1–.2) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N166 | DOC-001 p8 Table4 Triglyceride mg/dL medians O | Baseline n,value=63,134(90–186);termination=63,133(87–206);differenceCI=−3.9(−18–12) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N167 | DOC-001 p8 Table4 Triglyceride mg/dL medians P | Baseline n,value=blank,121(95–169);termination=59,107(80–153);differenceCI=−18(−25–−7) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N168 | DOC-001 p8 Table4 Glucose mg/dL medians O | Baseline n,value=63,90(83–99);termination=63,92(87–104);differenceCI=1.4(−1.8–5) | n≤64 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote permits difference from marginal subtraction; medians not algebraically subtractive. | COMPLETE |
| N169 | DOC-001 p8 Table4 Glucose mg/dL medians P | Baseline n,value=blank,93(85–100);termination=59,94(85–106);differenceCI=2.8(−3.6–6.0) | n≤62 when printed; positiveSD/orderedIQR; estimate in orderedCI; missing-data footnote applies; no filling native blank n. | COMPLETE |
| N170 | DOC-003 p2 eFigure1;DOC-001 p7 comparator | Weight(lb);Day0/50/100/150/200/250;y160/170/180/190/200;O≈179.5→184.5;P≈185.5→181.8;O initial rise andP initial decrease,quadratic curvature | Weight.13lb/day contrastsinitial slopes; modeledLSmeans not rawTable4;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N171 | DOC-003 p3 eFigure2;DOC-001 p7 comparator | Waist(inches);Day0/50/100/150/200/250;y36/37/38/39/40;O≈38.1→38.53;P≈39.13→37.29;contrast(.43−(−1.84))/252≈.0090 | Matches.009in/day;approx±.1in each read;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N172 | DOC-003 p4 eFigure3;DOC-001 p7 comparator | Totalcholesterol(mg/dL);sameDayticks;y180/190/200/210/220/230;O≈207→197;P≈215→194;curved trajectories | Positive relativeinitialslope.29 compatible with falling endpointboth;noendpointslopeidentity;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N173 | DOC-003 p5 eFigure4;DOC-001 p7 comparator | LDL(mg/dL);sameDayticks;y100/110/120/130/140;O≈131→123.5;P≈130.5→112.5;contrast≈.042/day | Matches.04±.005 model rounding plus±1mg/dLplotreading;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N174 | DOC-003 p6 eFigure5;DOC-001 p7 comparator | HDL(mg/dL);sameDayticks;y45/50/55/60;O≈53.4→48.0;P≈54.6→51.8;contrast≈−.0103/day | Matches−.01;±.3mg/dLplot readings;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N175 | DOC-003 p7 eFigure6;DOC-001 p7 comparator | Triglyceride(mg/dL);sameDayticks;y50/100/150/200/250;4curves:Onondropout≈140→144;Odropout≈209→79;Pnondropout≈141→121;Pdropout≈138→119 | Four printed legend strata;no weights/n supplied, averaged−.153 not directly equalonecurve;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE |
| N176 | DOC-003 p8 eFigure7;DOC-001 p7 comparator | Glucose(mg/dL);sameDayticks;y80/90/100/110/120;O≈100→102.5 downthenup;P≈98.5→97 milddecline | Quadratic time; do not equate endpoint difference to linear interaction−.02; blue O/red P; axis values exact, means approximate; bands contain curve, no numerical CI supplied. | COMPLETE |
| N177 | DOC-003 p9 eFigure8;DOC-001 p7 comparator | HbA1c(%);sameDayticks;y5.6/5.8/6.0/6.2;O≈5.90→5.71;P≈5.89→5.76;contrast≈−.000238percentagepoint/day | Model−.0002 numerically matches%;mg/dLunit flaggedRL-CAND-04;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE_WITH_LINKED_CANDIDATE |
| N178 | DOC-003 p10 eFigure9;DOC-001 p7 comparator | SASTotalScore;Week0/8/16/24/32/36;y.2/.4/.6/.8/1.0;O≈.56→.73;P≈.685→.40;logcontrast≈.02231/week | Positive contrast direction agrees;rawpointslabel flaggedRL-CAND-05;blueO/redP exceptfourcurve triglyceride;axis values exact,means approximate;bands containcurve,no numericalCI supplied. | COMPLETE_WITH_LINKED_CANDIDATE |
| N179 | DOC-003 p1 cover; DOC-001 p10 administrative/references | 9eFigures listed;references1–35;grantsidentifiers | Cover matches nine figures;administrative/bibliographic numbers not current-trial outcomes;no additional results. | COMPLETE_NO_APPLICABLE_NEW_RESULTS |

Complete relationships: 83; emitted distinct local candidates: 5. Physical coverage:14/14 assigned pages; nine/nine plotted result panels, all Tables3–5 cells and footnotes, both survival risk rows, all late narrative quantitative occurrences. No scientific coverage gap. Limitations: exact plot coordinates/band confidence levels and dropout weights unavailable; model link/back-transformation, NNT survival computation and paired Table4 subsets unprinted. These limits are reflected in the specific comparison rules, rather than supplied by outside conventions.



# Numeric relationship inventory: protocol first section

Runtime UUID: 01a1286a-9bc9-7b92-a717-2777aa292dbf. Fresh numeric specialist shard; gpt-6.1-sol, medium. Exact origin scope: DOC-002, joi190079supp1_prod.pdf, physical pages 1–21. Every location in this inventory is PLAN by content, including historical results. Other supplied plan/report populations are not silently aligned. Local PF identifiers are provisional; coordinator assigns stable N identifiers. No stable C identifiers or adjudications are assigned here.

Inputs: current support map extraction/parts/support_first_and_results.md and reusable page-specific native/layout files under review_1_5_1/preprocessing/support_001. Normative QUALITY_CONTROL_SCOPE.md and review_contract.md read completely. Direct Poppler pdftotext extraction of p15 was independently checked. Direct source rendering support-first-plan-p21.png was visually inspected and confirms ≥2 and ≥21; native/layout > signs are extraction loss. No web, old candidate decisions, unbundled Python, OCR, or GPU used.

Tolerance: integer counts and explicit phase/measure identities are exact. Displayed one-decimal percentages permit ±0.05 percentage points; integer percentages ±0.5 points, with boundary rounding allowed. Reported rounded means/SDs permit half of their last displayed unit. Planned whole-person flow tolerates integer target rounding and explicitly disclosed conservative assumptions. Simulation power cannot be recomputed without supplied simulation inputs; ordering and printed power/prose identities are checked. Different populations, time points, or models are not interchangeable. Every row has been checked; candidate rows point to complete cards in the paired checker artifact. Inferential test reconstruction is the separate statistical stage's responsibility.

| Local relationship | Exact DOC-002 physical locations | Printed inputs / relationship | Numeric, identity, scale, or consistency check and result |
|---|---|---|---|
| N180 | p1 contents | Navigation pages2, 3, 4, 5, 6, 7, 13, 16, 21, 24, 27, 28, 29, 31, 39 | Administrative locators, not outcome counts; no scientific inconsistency in assigned pages. |
| N181 | p2 lines31–32; p4 lines142–144 | Inpatient psychotic features19%–45%; lifetime15%–20% | Inpatient repeated range identical; lifetime population distinct. |
| N182 | p2 lines50–51; p3 lines109–114; p7 Figure1; p9 lines415–419 | RCT36 weeks; placebo half | Duration and allocation repeated consistently. |
| N183 | p3 lines99, 110–114; p7 Figure1; p11 footnoteA | Historical12-week trial; proposed acute maximum12, minimum4; stabilization8; RCT36 | Proposed full standard course12–20 open-label weeks then36; historical trial distinguished. |
| N184 | p3 aims1–5; p13–15 H1–H3, E1–E2 | Three hypotheses, two exploratory aims; treatment contrast | Five aims map to H1, H2, H3, E1, E2; direction matched. |
| N185 | p4 lines153–154 | Three historical RCTs | Three citation groups22–24; no supplied participant denominator to reconstruct. |
| N186 | p4 lines168–171 | Relapse17%–50%, mean30%, 12 months; post-ECT35%–50%, 12 months | Mean30% inside17%–50%; historical cohorts differ; risks over time, not person-time rates. |
| N187 | p4 lines175–177; p15 lines729–732 | Approximately35% of relapses after discontinuation versus35% relapse after discontinuation described as same historical rate | PF-CAND-03: conditional denominators differ; underlying historical denominator unspecified. |
| N188 | p4 lines178–180 | Relapse27% over8 months among30 | Integer-compatible8/30=26.6667%, rounds27%; event numerator not printed, so compatibility only. |
| N189 | p4 lines183–191; p6 line292 | Maintained-regimen relapse0%–6%/12 months; adverse withdrawals5%/12 weeks | Different event, follow-up and studies; repeated5% agrees. |
| N190 | p5 lines203–205 | Pilot16; akathisia63%; dose14.4±5.5 mg/day | 10/16=62.5%, compatible63% at whole-percent boundary; positive dose and dispersion. |
| N191 | p5 lines212–214 | Sales25%US, 30%world, 4 years | Geographic denominators distinct, no subgroup sum required. |
| N192 | p5 lines224–237 | Receptor/marker identities5HT1A−1019, D2 Taq1A,−141, 5HT2C−759, SNAP25, Leptin−2584, ADRα2a−1291, 5HT2A−1438, D3 ser9gly | Marker coordinates/identifiers not outcomes; signs retained, no arithmetic applied. |
| N193 | p6 lines271–280 | Award6/1/2002–5/31/2007; historical12 weeks; n259, 142 older, 117 younger |142+117=259; historical treatment sertraline+olanzapine vs olanzapine+placebo distinct from continuation contrast. |
| N194 | p6 line280 | Historical sites56, 59, 63, 81; total259 |56+59+63+81=259 exactly. |
| N195 | p6 lines281–283 | Remission OR1.28, CI1.12–1.47, p<.001 | Positive ordered interval contains estimate; longitudinal OR not derived from last-visit risk. |
| N196 | p6 lines282–284 | Last assessment41.9% vs23.9%, NNT5.6;χ²9.53, df1, p.002 | Absolute difference18.0 points; 1/.180=5.5556→5.6; risks not OR. Inferential pair separately reviewed. |
| N197 | p6 lines284–285 | Completers66.7% vs49.2%, NNT5.7;χ²4.4, df1, p.036 | Difference17.5 points; 1/.175=5.7143→5.7. Completers distinct from randomized. |
| N198 | p6 line286 | Age remission OR1.05, CI.80–1.37, p.75 | Ordered positive interval includes estimate and1; numeric label coherent. |
| N199 | p6 lines289–290 | Older gain7.3±10.3 lb, younger13.9±4.0 lb, F(1,226)=14.51, p.0002 | Difference6.6 lb favors less older gain; printed dispersion retained. No age-specific analysis n/model supplied for F reconstruction. |
| N200 | p6 lines291–292; p6 line280 | Younger glucose change8.4±41.3 mg/dL, baseline93.6±20.4, t(df=211)=2.65, p.009; younger117 | Implied unadjusted postmean102.0 is diagnostic only. DF211 exceeds116 under simple within-younger one-sample t, but test/model unidentified; no numeric candidate on an assumed model. Locator passed to coordinator/statistical stage. |
| N201 | p6 lines295–296 | PK young66, old102 | Sum168, both subsets within parent ages117/142. |
| N202 | p6 lines299–300 | Exposure variability.98±.27 vs.96±.30, t(df=166)=.36, p.72 |166=66+102−2; dimensionless ratio distinct from exposure magnitude. Rounded means can support printed t; no incompatibility forced. |
| N203 | p6 lines300–301 | Magnitude1128.9±737.6 versus1027.1±477.6 ug/mL*h; Supplied unequal-variances t(df=102)=1.0, p.32 | Difference101.8. Only if ± denotes sample SD, n66/102 are effective analysis sizes, and ordinary independent-sample Welch–Satterthwaite is the intended estimator, sqrt(737.6²/66+477.6²/102)=102.369578; conditional t=.9944361→1.0 and df100.3006. The source does not specify that estimator, dispersion or effective analysis subset; this diagnostic does not establish a df contradiction. Exact inferential reconstruction is limited by those missing definitions. Unit retained without external pharmacology assumption. |
| N204 | p7 lines303–307 | Historical stabilization3 months, n74, 29 young, 45 old |29+45=74 exactly; three-month historical phase not current8 weeks. |
| N205 | p7 lines307–308; p8 line376 |48 historical combination remitters; 10.4%relapsed; later10% |5/48=10.4167%→10.4%; whole-percent10% is coherent coarser precision. |
| N206 | p7 lines309–310; p15 lines739–741 | Gain1.5 lb/month stabilization vs4.4 acute; 1.5 repeated |Rates distinct from totalgain; repeated1.5 agrees; historical completers can differ from all-participant p6 means. |
| N207 | p7 lines310–315 |6 month age×time glucoseF(3,149)=3.16, p<.03; TG p.08, totalp.07, LDL p.09 |3 monthacute+3 monthstabilization=6 months; significance/trend direction retained; no pooled p reconstruction. |
| N208 | p7 Figure1 and overview | Acute392, 196 aged18–59, 196 aged≥60, 4 sites |196+196=392, distinct age strata and balanced prospective targets. |
| N209 | p7 Figure1; p8 lines373–381 |50% of392→196 stabilization; 10% loss→176 RCT |392×.5=196; 196×.9=176.4→176 whole-person conservative target. |
| N210 | p7 overview; p13 lines591–596 | Target sertraline150 mg/day, olanzapine15 mg/day | Repeated targets agree; not trial-observed doses. |
| N211 | p7 overview; p9 lines427–437 | Full remission HAM-D≤10 on2 assessments; near11–15 and≥50% reduction onlast2 | Adjacent numeric categories disjoint; criterion reproduced with same threshold; near not conventional remission. |
| N212 | p7 lines322–332 | MMSE≥24 atstabilizationend; below24 caseapproval; HAM-D>15 atweek8 allows2 additionalweeks,≤15 bothvisits | Conditional exception explicit; 8+2=10 maximum extension, standard8 remains standard duration. |
| N213 | p7 overview and lines322–324; p9 lines438–445 | MMSE≥24 heading to enter Stabilization, body eligibilityfor RCT atendstabilization | PF-CAND-02: same24-point threshold attached to different phase/time labels. |
| N214 | p7 line334; p9 lines420–422; p13 line609 | Taper4 weeks | Repeated duration agrees; no discontinuation outcome contradiction. |
| N215 | p8 lines336–337; p13 lines626–629; p14 lines646–648 | Age18–59/≥60, full/nearremission, site strata | Same boundaries and three stratification variables in model/randomization. |
| N216 | p8 lines341–349; p9 line391 | Startup4 months+51 active+5 analysis; total5 years |4+51+5=60 months=5 years. |
| N217 | p8 lines341–343 | Recruitment38 months afterstartup4, endmonth6 Year4; RCT month8 Year1 toendmonth7 Year5, 47 months | Absolute end recruitment42=3×12+6; 42−4=38. RCT end55; 55−8=47 elapsedmonths. Inclusive named-month counting does not force48 elapsed. |
| N218 | p8 lines359–360; p7 overview |392/4 sites/38 months=average2.6 site/month |392/152=2.578947→2.6; 2.6×152=395.2 is rounded-rate reconstruction only. |
| N219 | p8 lines362–366 |63/12948.8%; 10/1297.8% |48.8372→48.8; 7.75194→7.8. |
| N220 | p8 lines362–367 | Remission63, near10, total56.6% of129 |73/129=56.5891→56.6; 48.8+7.8=56.6. |
| N221 | p8 lines369–381; p7 Figure1 | Expected60%acute response, conservative50%, 10%stabilization loss, 176 RCT |Expected392×.6×.9=211.68; conservative392×.5×.9=176.4. Explicit50% protection prevents registering ordinary scenario difference. |
| N222 | p8 lines377–388 | Historicalzero relapse/dropout12 weeks; one-thirdremissionweeks6–12; acute6–8 usually | Cohort/time-specific historical descriptions not interchangeable with proposed10%loss. |
| N223 | p9 lines395–403 | Survey50 experts; proposed8 weeks | No actual count endorsing stabilization length printed; no invented percentage. |
| N224 | p9 lines435–437 | Conventional HAM-D<8–10 vsnear11–15 | Different labels explicitly distinguished; no numeric inconsistency. |
| N225 | p9 lines444–445 |1/37 MMSE<24 afterhistoricalstabilization | Fraction2.7027%; n37 MMSE subset need not equal48 allcombinationremitters; no forced denominator mismatch. |
| N226 | p10 lines450–454; p21 lines1017, 1031 | HAM-D17 items; IQCODE26 items | Repeated instrument lengths agree. |
| N227 | p10 lines459–466 | Stroop1–3; threeadditionaltests:recall, coding, Trails4&5 | Three domains/test families, not three task scores; list matches family count. |
| N228 | p10 lines468–469; p15 lines712–713 | Orthostasis1 minstanding after5 supine; criterion≥20 systolic/≥10 diastolicwithin3 min |1 minute is within3; no incompatible measurement timing compelled. |
| N229 | p10 lines473–483 | Premorbidmeanpreviousyear; weight loss; BMIrelativeheight; waistumbilicus | Measures distinct; missing BMI formula not itself candidate; direction andunits retained. |
| N230 | p10 lines484–488 | HOMA primaryglycemicmeasurefromglucose/insulin; HbA1 csecondary | Different constructs/model roles; formula cited but not supplied, not invented. |
| N231 | pp10–11 Table1 | Baseline; acute4, 8, 12; stabilization4, 8; RCT1–8, 12, 16, 20, 24, 28, 32, 36 | RCT8+7=15 visits; open-label1+3+2=6 standardweight visits. |
| N232 | p10 Table1; p14 lines664–665; p16 H2 | Weightall15 RCT follow-ups; H2 up15; minimum8 of15 | Printed count agrees; baseline/endstabilization is separatephase, not a16 th RCT follow-up. |
| N233 | p11 Table1; p14 lines664–665; p16 H2 | Metabolic RCT8, 16, 24, 32, 36; up5, minimum4 of5 | Five listed RCTsamples matchpowerandanalysiscounts. |
| N234 | pp10–11 Table1; p14 lines680–682; p16 H3 | Weightbaseline+acute4, 8, 12+stabilization4, 8; up6, minimum4 of6 | Sixmaximumplannedvisitcolumns; shorteracute may yieldfewer, explicitlyup6. |
| N235 | pp10–11 Table1/footnotesD, E | SCIDbaseline/termination; heightbaseline; labacute4/endacute, stabilizationend | Variableendacute4–12 andtermination substitutions explicit; repeatedendacute4 cancoincidewithweek4, not duplicatepersons. |
| N236 | p11 Table1 | Drugplasmaacute4/endacute, stabilizationend, RCT16/36; biomarkersbaseline/stabilizationend/RCT termination | Phase-specific samples distinct from2–4 sparse PKobservations in a given modeledinterval; no enforcedtotal identity. |
| N237 | p11 Table1 andfootnoteH | Cognition IQCODE baseline; MMSE, recall, Stroop, Trails, codingstabilizationend; selectedtasks RCT termination | Baselinecognitionx refers IQCODE, not early MMSE eligibility. CorroboratesPF034 time-label conflict. |
| N238 | p11 Table1 | EPSEbaseline, acute4/8/12, stabilization4/8, RCT4/8/12/16/20/24/28/32/36 | Periodic9 RCTEPSEvisitsexplicit; fullclinical visits15 includeUKU andotherlogs, different instruments. |
| N239 | p11 Table1, footnotesJ, K | BestGuess RCT termination; Intent-to-Attend RCT week1 | Differentforms/timepoints coherent; no repeatedscore identity. |
| N240 | p11 footnotesA–C | Acute4–12; psychiatrist1, 2, 3, 6, 10; phone stabilization2/6, RCT10/14/18/22/26/30/34 | Clinicalcontact every≤2 weeksafter RCT week8; fitsno>2 weekspriorstatusp16.Extraacute visitsnotweightrowdenominators. |
| N241 | p11 footnotesE–G | Final36 orend; physicalintheweekbeforemedications; clinicalinstrumentlist | Windowandterminationrulesexplicit, no conflictwith36 weekmaximum. |
| N242 | p11 lines525–532 | DNA deliverywithin4 months; 10%regenotyped; laberror.5% | Subsamplingfractionandlaberrorfractionhavedifferentdenominators; notcontradictory. |
| N243 | p12 lines536–540 |96 ancestrymarkers; 20000 burn-ins, 20000 repetitions | Equalcountsnamedfordifferentstages, not accidentalduplicateoutcome; probabilitiesasmodelcovariate. |
| N244 | p12 lines544–551; p6 lines299–301 | Batchevery6 months; exposureAUC/mean; Cpred/obs; 2–4 samples | Ratio dimensionless andAUCtime×concentration, consistentwithhistoricaltwoexposuremeasures. |
| N245 | p12 lines554–559 | Relapse≥1 criterion; HAM-D≥18 plusincrease5; prefer1 week/twoassessments; SADS≥3 | Ascertainmentrulesexplicit; 18 and5 notinterchangeable; baseline11–15 canrequirehigherthan18 todifferby5. |
| N246 | p12 lines560–568; p13 lines642–645 | Mania/hypomania1 week; hospitalizationanyduration; firstestablishingvisit/hospitalstart; timeinweeks | Preferred7-daywaitexceptionexplicit; timeoriginrandomizationagrees. |
| N247 | p12 lines575–580; p15 lines728–730; p8 timeline | Referral48–72 hours; estimated3 relapses/site/year; 176 RCT, 15%/35% | Expected44 relapsesoverall; 4 sites×47/12 years≈15.67 siteyears; 44/15.67≈2.81→approximately3; rateevents/siteyearnotparticipantpercent. |
| N248 | p12 lines583–590 | Lorazepam/benztropinebarred12 hoursbeforetesting; prohibiteddrugsendfirstweek; sertraline50 mg/day | Timinganddoseunitsdistinct; retainedexactly. |
| N249 | p13 lines591–596 | Sertraline50→150 by50 mgsteps, after4 weeks150→200; olanzapine5→15 by5 mgsteps, after7 days15→20 | Twoincrementsreachbothtargets; thirdreachmax; 7 days=1 week, notsertraline4 weekdelay. |
| N250 | p13 lines600–604 | Stabilization8 weeks; sertraline50–200, olanzapine5–20 mg/day | Start, target, maxallwithinranges. |
| N251 | p13 lines609–617; p11 footnoteA; p14 line654 | Minimum10 weekssertralinepre RCT; standardacute4–12+8 stabilization=12–20 |≥12 implies≥10 so notarithmeticallyfalse; looserbounddoesnotestablishdifferentprotocolminimum. |
| N252 | p13 lines614–622 | Sertralineonlyreduction; olanzapine/placebodosechangesallowed | Changeshaveexplicitdifferent rules; notpairedtreatmentdoseidentity. |
| N253 | p13 lines626–638; p15 Table2 text |88/arm, 1:1, total176; two-tailedalpha.05 |88+88=176; 1:1 andhalfallocationagree; alpharepeated. |
| N254 | p13 lines635–636; p14 lines648–652 | Imbalancedcovariater≥.30 versusfivecandidatecovariatesr>.30, p≤.05 | Generalruleinclusiveandnamedcovariatesstrictatboundary; noactualr=.30 printed, so no concrete reportedstatisticaffected. |
| N255 | p14 lines648–650; p10 lines455–460 | Fivevariablesanxiety, medicalburden, executive, psychomotor, treatmentresistance | Exactlyfive; measuresmatched. |
| N256 | p14 lines653–659; p16 lines761–765 |RCT attrition≤10%; prioropenlabel12–20 weeks; vulnerablefirst3 months; status≤2 weeks |Repeatedattritionagrees; clinicalphonevisitsfill RCT in-person4 weekgaps. |
| N257 | p14 lines673–677 | Censormetabolicdata<5% (i.e.<10 RCT participants), n176 |.05×176=8.8; integer<5%allows≤8 andnecessarily<10. Parentheticalislooseupperbound, notclaim9/176<5%. |
| N258 | p14 lines688–700 | Exploratoryagesignificancetestingabsent; callrate<95%ANDMAF<10%; HWE p<.001 | Thresholds/ANDpreserved; nooutcomevaluescontradictlabel.Unreportedconventionnotcandidate. |
| N259 | p15 lines701–704 | Onegenotype/model; mainplusinteractionrandomized; haplotypefrequency<10%excluded | Thresholddistinctfrom MAF andcallrate; modelcountnotparticipantcount. |
| N260 | p15 lines708–713 | NewadverseeventN/%; UKU increase≥2 orscore3; AIMS≥2; Barnes≥2; SAS mean≥2 | Differentinstrumentthresholdsnotinterchanged; SAS mean labelretainedforcross-lanecomparators. |
| N261 | p15 lines712–717 | SSI4 or5≥1; SBPdrop≥20, DBP≥10 within3 min;≥1 fall; RCT week8 onward | Eventriskdenominatorisparticipantsnotfalls; thresholds, timewindowexplicit; multipleeventsnotexclusivesubgroups. |
| N262 | p15 lines725–730 |20%absolute35%−15%over36 weeks; NNT5 |.35−.15=.20; 1/.20=5; not20%relativechange. |
| N263 | p15 Table2 row1 |40%placebo, 15%olanzapine, 10%attrition, power.95 | Inputswithin0–1; contrast25 points; simulationcannotberecreatedwithouttimegenerator. |
| N264 | p15 Table2 row2 |40%, 15%, 15%, power.94 | Increasedattritionreducespower.95→.94. |
| N265 | p15 Table2 row3 |35%, 15%, 10%, power.84 | Mainassumptionsrow; smallercontrast20 pointsreducespower.95→.84. |
| N266 | p15 Table2 row4 |35%, 15%, 15%, power.82 | Increasedattritionreducespower.84→.82. |
| N267 | p15 Table2 row5 |35%, 10%, 10%, power.98 | Greatercontrast25 pointsincreasespower.84→.98; equalRDdifferentbaselineriskneednotequalpower. |
| N268 | p15 Table2 row6 |35%, 10%, 15%, power.97 | Increasedattritionreducespower.98→.97; allpowerswithin0–1. |
| N269 | p15 lines738–747; p7 lines309–310 |Weight1 lb/monthupto9 monthsafter12 weeks; STOP-PD1.5; TG8–10 mg/dL/month4–12 months, STOP-PD9; cholesterollittleafter12–16 weeks |9 within8–10; historyvsassumed RCT different; monthratesnotendpointmeans. |
| N270 | p16 Table3 row1 |4 obs, effect.35, lipid ICC.50 power.74, weight ICC.95 power.77 |Distinct ICC s/measurepower; noalloutcomes≥.80 claimatthiseffect/obs. |
| N271 | p16 Table3 row2 |4 obs, effect.40, power.84 lipid,.85 weight |H3 four-weight.40 power>.80 agrees. |
| N272 | p16 Table3 row3 |4 obs, effect.45, power.89 lipid,.93 weight |Higherstandardizedeffectmonotonicallyincreasesbothpowers. |
| N273 | p16 Table3 row4 |8 obs, effect.35, lipid—, weight.80 |H2 minimum8 weightsand≥.35 power≥.80 agrees; dashnotzero. |
| N274 | p16 Table3 row5 |8 obs, effect.40, lipid—, weight.89 |Higherobs4→8 increasesweightpower.85→.89. |
| N275 | p16 Table3 row6 |8 obs, effect.45, lipid—, weight.95 |Higherobsincreases.93→.95; allprintedpowerswithin0–1. |
| N276 | p16 H2 text | Effect.35 weight↔4.9 lb;.40 TG↔38 mg/dL;.40 cholesterol↔22 mg/dL |Implicit SD14 lb, 95 mg/dL, 55 mg/dL; noexplicitcomparison SDsforcurrentpower population, so noforcedmismatchwithhistoricalweight SD. |
| N277 | p16 lines755–759; p6 lines289–290 |Completerweightyounger16.6±16.5 lb, older10.7±11.3, effect.42 |Difference5.9; sqrt((16.5²+11.3²)/2)=14.14; 5.9/14.14≈.417→.42 diagnosticallycoherent; completerpopdistinctfromp6. |
| N278 | pp17–18 Table4; p7 overview; p21 lines995–997 |4 sites×98 acute=392; 4×44 RCT=176 versus82/site | PF-CAND-01:82×4=328, 64 below392; 98−82=16/site.Candidateidentityiswithinoneplan, notplanned-v-observed. |
| N279 | p17 lines815, 827–829 | Collaboration8 years; 10 pilotprojects, 16 sites, 2500 subjects, 6 monthdata250 patients | Administrativehistorical populations; 250 subset≤2500, notallsubjectslongitudinal. |
| N280 | pp18–19 governance |4 PIsplusMulsant; weeklycalls; quarterlyreports; annual≥1 daymeeting; launch2 days; Years2–4 one-daymeetings | FivecommitteeprincipalsconsistentwithfourPIsplusone; differentmeetingfrequenciescompatible. |
| N281 | p19 lines913–917 |12 videotapedinterviews/rater; historical ICCHAM-D.93–.98, DAS.69–.84 |Ordered ICC rangeswithin0–1; instrumentsdifferent.Noactualnraterssupplied, noinventedtotal. |
| N282 | p20 lines938–939, 971–981; p21 lines987–991 | Shippingevery2 weeks; 100%scaleaudit;>170000 scales,~6%problems; correction2 weeks; 10%doubleentry;.27%entryerror | Auditversusdouble-entryandproblemversusentryerrorhavedifferentdenominators/rules.Noequalityrequired; currenttrialpatientsnot170000 scales. |
| N283 | p21 lines996, 1005–1017; p7 agegroups |Recruit≥18; inclusion18–85 inclusive; SADS≥3; DASanyof3 items≥2; HAM-D17 items≥21 |General≥18 compatiblewithboundedeligibility; 18–59 and≥60 partitioneligible18–85.P21 source≥signsconfirmedvisually. |
| N284 | p21 lines1027–1035; p10 instruments | Substanceusepast3 months; IQCODE26-itemmean≥4; sen84%–93%, spec88%–94% |Repeatedmeanthreshold/instrumentlengthagree; rangeswithin0–100%; screeningmetricsdistinctnotcomplementary. |

## Completion

105 provisional numeric relationships checked across every assigned page, Tables1–4 and Figures1–2; three distinct candidate observations. Administrative units and marker identities are explicitly mapped rather than used as discovery targets. No scientific-coverage gap in DOC-002 pp1–21. Simulation power, unreported historical test/model identities, and unprinted underlying historical-study denominators impose bounded reproducibility limitations; named conditional questions are retained where a printed mismatch exists. Exact inferential compatibility and whole-package report/plan matching belong to their assigned specialist stages.


# Numeric relationship inventory: plan-last shard

Runtime UUID: 01a1286a-b71f-73c2-90f9-22d2fd35e362. Fresh numeric reviewer; gpt-6.1-sol/medium. Exact origins: DOC-002 physical PDF pp22–42 and DOC-004 p1. Counterparts earlier in DOC-002 are locators used only for matched checks. Local PL identifiers await coordinator N assignment. 116 relationships; no count limit applied. Every DOC-002 location is PLAN, including historical STOP-PD data. DOC-004 has no numeric origin. All22 assigned physical pages complete; scientific gaps0.

Inputs: current support_plan_second mapping and source-linked reusable Poppler layout text; current first-plan map and direct source rendering pp10,11,29 where needed. Historical and prospective numbers are distinguished from achieved trial results. Rounding tolerance: one-decimal percentages ±0.05 percentage points, integer counts exact, prospective approximations interpreted with their printed qualifiers. No old candidate/report inputs.

## Base relationships and completed checks

| Local ID | Source locator (DOC-002 PLAN) | Printed inputs / rule / population | Completed numeric checks |
|---|---|---|---|
| N285 | [p22](../../../joi190079supp1_prod.pdf#page=22), lines1037–1038 | Type 1 diabetes: insulin-dependent diabetes with onset <35 years and/or prior documented ketoacidosis; cite157 | Onset age <35 is diabetes definition; neither enrollment lower bound18 nor elderly threshold60. No matched numerical contradiction. |
| N286 | p22 lines1040–1046 | Acute/unstable illness within last3 months; epilepsy excluded if ≥1 grand mal seizure in past12 months; abnormal free T4, low B12/folate, relevant medical causes, neurological extrapyramidal disease | 3-month illness and12-month seizure windows apply different conditions; not conflicting denominators. |
| N287 | p22 lines1056–1059 | Prior sertraline intolerance including heart rate <50 bpm or SIADH serum sodium ≤129 mmol/L | HR<50 bpm and sodium≤129 mmol/L are distinct analytes; boundary/unit labels coherent. |
| N288 | p22 lines1060–1061 | At least6-week trial of sertraline ≥150 mg/day combined with olanzapine ≥15 mg/day for index PD episode | Prior ≥6-week adequate nonresponse is exclusion criterion, distinct from historical ≥3-week exposure; drug minima150/15 match target levels. |
| N289 | p22 lines1049–1065 | Other psychotropics besides sertraline/olanzapine/lorazepam, anticonvulsants with mood-stabilizing properties, pregnancy/breastfeeding, ongoing improvement on different treatment, immediate ECT need excluded | No denominator or outcome count given; treatment exclusions inspected without generalized design concern. |
| N290 | p22 lines1068–1070 | Children below18 excluded | Below18 exclusion agrees adult ≥18 eligibility; age equality belongs eligible side. |
| N291 | p22 lines1072–1088 | Bipolar disorder excluded; moderately severe/severe depression required; delusions required with/without hallucinations; isolated hallucinations insufficient | Diagnostic eligibility lacks an additional numeric result; no unsupported population candidate. |
| N292 | [p23](../../../joi190079supp1_prod.pdf#page=23), lines1090–1100 | DSM-IV substance disorder definition uses12-month pattern; study excludes abuse/dependence within3 months and allows histories more than3 months earlier | DSM12-month diagnostic pattern versus3-month enrollment exclusion explicitly distinct; no numeric conflict. |
| N293 | p23 lines1115–1120 | STOP-PD no more than7 of259 participants had Type1 diabetes | Historical Type1 numerator is ≤7, denominator259; implied ≤2.7027%, not an exact7 count or current-study numerator. |
| N294 | p23 lines1133–1141 | STOP-PD only5% received ≥3-week adequate combined antidepressant/antipsychotic trial during index episode before study; no count given | 5% historical adequate ≥3-week pretreatment is exposure prevalence; no numerator printed. If denominator259, rounding to whole percent permits12–14 people; no assertion of a unique count. |
| N295 | [p24](../../../joi190079supp1_prod.pdf#page=24), lines1146–1157 | 3 material sources: patient/informant interviews; medical/pharmacy records including ATHF treatment adequacy; blood tests for genetics, metabolic analyses, sertraline/olanzapine plasma levels | Enumerated three material sources match three supplied items; blood sample is not an enrolled-person outcome count. |
| N296 | p24 lines1159–1162 | STOP-PD common side effects occurring in >10%: weight gain, somnolence/sedation, GI symptoms, at least1 fall, orthostatic dizziness | >10% historical adverse-event list does not provide exact numerators; incidence/proportion informal wording does not establish person-time rates. |
| N297 | p24 lines1165–1168 | Olanzapine-user increased absolute mortality risk across diagnostic groups estimated0.9% over2–3 years of current use; cite162 | 0.9% absolute mortality risk over2–3years differs background diagnostic population; no trial death count or rate denominator inferable. |
| N298 | p24 lines1175–1177 | Overall relapse risk approximately25% during RCT | Approximately25% overall relapse assumption is not the protocol's arm-specific risks or current observed outcomes; no equality rule available. |
| N299 | p24 lines1179–1182 | ECT up to50% relapse risk in6 months following discontinuation | Up to50% ECT relapse over6months is a different comparator/time; cannot compare directly to current RCT36-week event risk. |
| N300 | p24 lines1189–1194 | Screen within24 hours admission or as close as possible weekends | 24-hour screening goal accommodates weekends; prospective timing, no achieved count. |
| N301 | [p25](../../../joi190079supp1_prod.pdf#page=25), lines1205–1242 | Surrogate consent/participant assent allowed in acute and stabilization; sustained remission/near remission and capacity required for randomized phase; second capacity assessment by independent professional or MacCAT-CR | Acute/stabilization consent differs randomized consent by capacity; no actual flow totals here. |
| N302 | p25 lines1244–1248 | Capacity assessed at end8 weeks stabilization before consent to RCT | 8-week stabilization duration repeats p40 A2 consistently. |
| N303 | p25 lines1252–1254 | Failure to meet remission criteria after12 weeks acute sertraline/olanzapine makes participant ineligible for stabilization/RCT; leave study at12 weeks | Acute maximum12weeks repeats p3/7/39 protocol timeline; excludes nonremitters, no displayed flow count conflict. |
| N304 | [p26](../../../joi190079supp1_prod.pdf#page=26), lines1255–1258 | Significant worsening = CGI change6 or7 (much worse/very much worse), requiring withdrawal during acute/stabilization | CGI change6/7 are scale categories, not scores on HAM-D/SSI; labels directly specified. |
| N305 | p26 lines1260–1267 | In-person research weekly first8 weeks RCT; thereafter every2 weeks alternating research and clinical assessments | Weekly first8 RCT weeks, then alternate research/clinical every2weeks implies each type every4weeks; consistent with four-week research schedule. |
| N306 | p26 lines1269–1273 | Relapse referral within48–72 hours; estimated average3 relapse cases/year/site | 3 cases/year/site is projected event frequency, 48–72hours referral interval; not an incidence proportion. Same projection repeats p12. |
| N307 | p26 lines1275–1283 | High risk includes current plan, index-episode attempt, ≥1 lifetime serious attempt needing inpatient medical care; weekly psychiatrist first6 acute weeks then every2 weeks remainder acute/stabilization | First6 acute weeks weekly psychiatric review is high-risk safety monitoring; ordinary Table1 schedule explicitly supplemented for safety, no forced equality. |
| N308 | p26 lines1293–1300 | Current ideation = SSI score1 or2 on item4 or5; weekly extra psychiatrist visits until resolved/withdrawn | SSI items4/5 and values1/2 are item-specific scales; additional weekly monitoring is conditional, not conflicting general schedule. |
| N309 | p26 lines1302–1308 | Monitor every assessment; sertraline/olanzapine dose reduction to minimum permitted; benztropine for persistent EPSE | General minimum dose permission refers detailed appendix; indication-specific EPSE rule tracked N344. |
| N310 | [p27](../../../joi190079supp1_prod.pdf#page=27), lines1310–1313 | Metabolic parameters at acute week4 and thereafter every8 weeks | 8-week metabolic cadence inspected against direct Table1: phase-end and termination assessments are additional; see N400. |
| N311 | p27 lines1312–1316 | Fasting glucose >100 mg/dL; triglycerides >150 mg/dL; total cholesterol >200 mg/dL; LDL >130 mg/dL trigger PCP referral | Glucose100,TG150,total cholesterol200,LDL130 all mg/dL; clinical referral thresholds differ descriptive analysis baselines by purpose. |
| N312 | [p28](../../../joi190079supp1_prod.pdf#page=28), lines1380–1391 | Quarterly AE/SAE/recruitment/withdrawal reports; SAE to DSMB/coordinating IRB within48 hours; each site to Cornell IRB within48 hours; blinded interim analyses if DSMB requests | Quarterly reports and48-hour SAE notifications apply different operations; request-only interim analysis lacks numeric boundary. |
| N313 | p28 lines1393–1396 | Renewal of STOP-PD U01 identified NCT00056472 | Historical NCT00056472 names earlier STOP-PD renewal; not a numeric trial result or current-registration identity claim. |
| N314 | p28 lines1401–1407 | 50% subjects elderly; female:male approximately2:1 at all sites;4 sites | 50% elderly and approximate female:male2:1 are prospective targets; implied67% women not required to equal achieved61.9%. |
| N315 | p28 lines1409–1415 | Cornell Westchester anticipated13% African American and13% Hispanic; could be higher with NYC recruitment | 13% Black and13% Hispanic belong race/ethnicity axes; cannot sum as mutually exclusive population categories. |
| N316 | p28 lines1417–1419 continuing p29 | Pittsburgh67% white,27.1% African American,2.8% Asian,1.3% Hispanic; minimal other minorities | Pittsburgh race67+27.1+2.8=96.9%; other race unspecified. Hispanic1.3% overlaps race; no exhausted100% partition claimed. |
| N317 | [p29](../../../joi190079supp1_prod.pdf#page=29), lines1420–1421 | McKeesport72% white,25% African American,0% Asian,1.5% Hispanic; minimal other minorities | McKeesport race72+25+0=97%; other race unspecified. Hispanic1.5% distinct axis; no100% contradiction. |
| N318 | p29 lines1423–1426 | Toronto approx40% visible minority;34% Toronto STOP-PD patients Asian/Black/Hispanic | Toronto city40% versus historical site34% differ populations; no exact count denominator supplied. |
| N319 | p29 lines1428–1430 | Massachusetts site expected15–20% Hispanic; Worcester County Census2000 Hispanic15.2%,52% increase1990–2000 | Worcester15.2%2000 and52% relative1990–2000 increase imply approximately10%1990, not67.2%; target15–20 contains15.2. |
| N320 | p29 lines1432–1445 | 5 required cultural training modules;12 additional ethnic-specific modules | Five core modules match five enumerated topics;12 extra ethnic modules need not be a total of persons. |
| N321 | p29 lines1447–1453 | 84.2% white,11.2% African American/Black,4.6% Asian;11.6% Hispanic/Latino; completion at weeks6/12 of12-week study described highly comparable across groups | Race proportions84.2+11.2+4.6=100%;11.6% Hispanic separate ethnicity; see N367–N370 arithmetic. |
| N322 | p29 Table5 | Full row transcription below; randomized259 total derivable from race and independently ethnicity rows | All Table5 cells checked N357–N373. Week6 partition discrepancy emits PL-CAND-01; Week12 reconciles. |
| N323 | p29 lines1461–1464 continuing p30 | Public database once main findings accepted for publication; deidentified baseline/outcome SAS datasets and validation-rule dictionary | Publication acceptance is operational release trigger, not numeric outcome; no independent arithmetic. |
| N324 | [p30](../../../joi190079supp1_prod.pdf#page=30), lines1486–1487 | Personal communications11/13/2009 and1/12/2010 | 2009/2010 communications predate trial recruitment appropriately; dates are not achieved recruitment periods. |
| N325 | p30 lines1489–1497 | All consenting participant blood;38 months recruitment; approximately10 blood samples/month; DNA transfer within4 months of receipt | 10 samples/month×38months≈380 samples. Approximation and sample/consenting-person distinctions prevent equating to392 planned acute participants. |
| N326 | p30 lines1499–1501 | Clinical data electronically submitted every6 months | Clinical submissions every6months repeats maximum6-month generation-to-submission rule p31; boundary operational ambiguity does not yield a printed number contradiction. |
| N327 | p30 lines1502–1512 | DSM-IV nonbipolar PD; clinical psychiatrist interview then SCID-IV-TR; diagnostically unclear cases consensus; baseline depression/psychosis/suicide/anxiety/cognition/medical burden/treatment resistance | Diagnostic three-line assessment and phenotypes have no competing numeric score cutoff in this paragraph. |
| N328 | p30 lines1513–1518 | Weekly quality conference; primary-measure inter-rater reliability annually; historical evaluations each year of5-year STOP-PD | Annual reliability over5-year historical STOP-PD is distinct from prospective weekly conference cadence. |
| N329 | p30 lines1517–1519 | GRID HAM-D total ICC0.93–0.98; DAS conviction ICC0.69–0.84 across annual STOP-PD assessments | ICCs .93–.98 and .69–.84 ordered within[0,1]; range of annual estimates, not CI. Historical same values .93–.98 and .69–.84 at p19 lines916–917 match exactly; no inference from missing sample sizes. |
| N330 | [p31](../../../joi190079supp1_prod.pdf#page=31), lines1520–1523 | Cornell auditing tracked >170,000 individual rating scales over >20 years | >170000 ratings over>20years repeats p20 administrative history; both lower bounds cannot determine exact annual rate. |
| N331 | p31 lines1525–1534 | Verified diagnostic and remaining clinical data submitted within6 months generation; genotype to dbGaP on manuscript acceptance or award end, whichever first; clinical/diagnostic and genotype data eligible release12 months receipt | 6-month submission and12-month release refer different clocks; acceptance/award-end earliest genotype trigger coherent. |
| N332 | p31 lines1536–1547 | 4 consent stipulations; external sharing anonymized among4 institutions | Four consent stipulations numbered1–4; four named institutions match stated collaboration count. |
| N333 | [pp31–39 bibliography](../../../joi190079supp1_prod.pdf#page=31), lines1550–1961 | References1–163 inspected across all pages. Citation numbers, years, volumes, page ranges, title durations/sample descriptors, receptor/variant names identify cited work, not supplied estimates or results. No reference-content inference or external lookup | References1–163 and all pages31–39 inspected as bibliographic identities; citation years/page ranges are not supplied outcome estimates. |
| N334 | [p39](../../../joi190079supp1_prod.pdf#page=39), lines1967–1974 | Up to4 days pre-study withdrawal when feasible; anticonvulsant mood stabilizer withdrawal extended10 days; if withdrawal symptoms, taper slowed to10 days overlapping first acute week | Withdrawal4days vs extended10days applies general versus anticonvulsant/withdrawal-symptom rules; neither is randomized taper. |
| N335 | p39 lines1975–1985 | Existing sertraline/olanzapine may continue adjusted to targets; open-label acute/stabilization; sertraline morning50 mg tablets; olanzapine evening5 mg tablets | Sertraline50mg tablet/olanzapine5mg tablet strengths agree appendix dose multiples. |
| N336 | p39 lines1985–1992 | Start sertraline50 mg/day + olanzapine5 mg/day; day4→100/10 mg/day; day7 targets150/15 mg/day; side effects permit slower schedule with goal targets within14 days | Days1/4/7 doses50/100/150 and5/10/15 are coherent50mg/5mg increments; slower14-day exception explicit. |
| N337 | p39 lines1994–1998 | After7 days at15 mg/day with inadequate psychosis improvement increase to20 mg/day as tolerated; allows maximum by2 weeks treatment | Day7 reach15mg then7days at15 permits20mg byday14, agreeing2weeks; tolerance whole-day schedule. |
| N338 | p39 lines1998–2000 | Partial depressive improvement =17-item HAM-D <16; absent partial improvement after4 weeks at150 mg/day increase to200 mg/day | HAM-D<16 means ≤15 for integer scale; partial improvement differs remission≤10;4weeks at150 then200 coherent. |
| N339 | p39 lines2002–2007 continuing p40 | Halt titration/reduce clinically indicated doses, resume targets when symptoms resolve; if cannot tolerate150/15 after further titration, maintain lower doses | 150/15 targets can be unattainable under side-effect exception; lower allowed doses explicit, not actual target mismatch. |
| N340 | [p40](../../../joi190079supp1_prod.pdf#page=40), lines2008–2009 | Minimum sertraline50 mg/day and olanzapine5 mg/day | 50mg sertraline and5mg olanzapine general minima align stabilization/RCT ranges; EPSE10mg qualified separately. |
| N341 | p40 lines2011–2014 | End second treatment week mean sertraline150 mg/day both age groups; olanzapine14 mg/day younger and13 mg/day older | Historical means150/14/13 do not need to equal prospective150/15 targets; group means need not be tablet multiples. |
| N342 | p40 lines2015–2026 | Sertraline target150 mg/day early; inadequate psychosis response after7 days olanzapine15 mg/day→20 mg/day | Repeated150mg target and15→20 after7days agree p39 PS52/53. |
| N343 | p40 lines2028–2031 | Lorazepam starting0.5–2 mg/day PRN; maximum3 mg/day throughout study; minimum use and earliest withdrawal | Lorazepam0.5–2 initial ≤3maximum; repeated p42 max3 agrees. |
| N344 | p40 lines2033–2036 | Reduce olanzapine in5 mg increments to minimum10 mg/day for EPSE; persistent problematic EPSE permits benztropine max2 mg/day | EPSE-specific olanzapine minimum10 differs general tolerated minimum5 by named indication; no universal minimum identity established. |
| N345 | p40 lines2036–2039 | No lorazepam/benztropine within12 hours before cognition tests; benztropine prescription considered in secondary EPSE statistical analyses | 12hour cognition avoidance repeats p12; benztropine statistical consideration lacks a displayed quantitative result. |
| N346 | p40 lines2041–2054 | 8-week stabilization; sertraline increase/decrease50 mg every7 days within50–200 mg/day; olanzapine increase/decrease5 mg every7 days within5–20 mg/day | 8weeks stabilization;50mg/5mg weekly steps remain ranges50–200/5–20. All endpoints tablet compatible. |
| N347 | p40 lines2048–2051 | Sustained psychosis remission needed; SCID-determined delusion/hallucination relapse exits stabilization; nondelusional worry can permit dose increase | SCID psychotic relapse exits stabilization, nondelusional worry differs event definition; no concrete count contradiction. |
| N348 | p40 lines2056–2062 | After stabilization, remission-eligible participants allocated continue olanzapine vs switch placebo; statistician assignments to site pharmacists; emergency access | Two groups continue versus placebo match trial contrasts; randomization ratio supplied earlier1:1, not contradicted here. |
| N349 | [p41](../../../joi190079supp1_prod.pdf#page=41), lines2063–2065 | 24 hours/day physician availability | 24hours/day is medical emergency availability, not participant-observation person-time. |
| N350 | p41 lines2067–2081 | Same dose at randomization sought; exposure before RCT minimum10/max20 weeks; reductions50 mg every7 days to minimum50 mg/day if agreed; increases prohibited throughout RCT; dose changes described per arm | Sertraline exposure minimum10/max20 printed; acute4–12 + stabilization8 arithmetic checked separately N398; candidate PL-CAND-02. |
| N351 | p41 lines2083–2089 | Matched placebo identical size/weight/appearance to5 mg olanzapine tablets; only statistician/pharmacists unblinded | 5mg matched placebo tablet is nominal olanzapine equivalent, not an assertion of active placebo drug. |
| N352 | p41 lines2091–2093/table | Complete4 starting-pill strata ×5 schedule rows below; Bottle A=open-label olanzapine, B=blinded olanzapine/placebo | All40 BottleA/B cells checked as20 pairs N374–N393; total pills preserved, active drug depends arm. See N399. |
| N353 | p41 lines2094–2105 | Maintain randomization dose sought, change for AE/worsening allowed; daily dose adjusted1 tablet every7 days within5–20 mg/day olanzapine/placebo; changes described each arm | 1tablet/7days =5mg nominal equivalent; range5–20 matches allowed doses and starting strata. |
| N354 | p41 lines2107–2109 continuing p42 | Attempt lorazepam taper/discontinue during acute after depression improves; can continue RCT if needed | Lorazepam taper attempt versus continued need is explicit conditional exception, not treatment-dose inconsistency. |
| N355 | [p42](../../../joi190079supp1_prod.pdf#page=42), lines2110–2113 | RCT lorazepam max3 mg/day for insomnia/anxiety; benztropine max2 mg/day | RCT maxima lorazepam3mg/benztropine2mg repeat p40 consistently. |
| N356 | p42 lines2111–2113 | STOP-PD5/259 (1.9%) required benztropine | 100×5/259=1.9305%→1.9% within0.05pp; historical STOP-PD denominator not current126. |

## Exhaustive historical Table5 percentage checks

Every location is [DOC-002 p29 Table5](../../../joi190079supp1_prod.pdf#page=29), PLAN. Input n and p are printed; k is derived by unique integer compatibility with p±0.05pp, not a printed count. Rounded percentages reconcile individually.

| Local ID | Row/time | Printed n | Printed % | Unique k | Calculation100k/n | Check |
|---|---|---:|---:|---:|---:|---|
| N357 | Asian/week6 | 12 | 75.0 | 9 | 75.000000% | Within0.05pp; integer unique; completion≤randomized |
| N358 | Asian/week12 | 12 | 50.0 | 6 | 50.000000% | Within0.05pp; integer unique; completion≤randomized |
| N359 | Black/week6 | 29 | 75.9 | 22 | 75.862069% | Within0.05pp; integer unique; completion≤randomized |
| N360 | Black/week12 | 29 | 51.7 | 15 | 51.724138% | Within0.05pp; integer unique; completion≤randomized |
| N361 | White/week6 | 218 | 74.8 | 163 | 74.770642% | Within0.05pp; integer unique; completion≤randomized |
| N362 | White/week12 | 218 | 55.5 | 121 | 55.504587% | Within0.05pp; integer unique; completion≤randomized |
| N363 | Hispanic/week6 | 30 | 80.0 | 24 | 80.000000% | Within0.05pp; integer unique; completion≤randomized |
| N364 | Hispanic/week12 | 30 | 53.3 | 16 | 53.333333% | Within0.05pp; integer unique; completion≤randomized |
| N365 | Not Hispanic/week6 | 229 | 73.8 | 169 | 73.799127% | Within0.05pp; integer unique; completion≤randomized |
| N366 | Not Hispanic/week12 | 229 | 55.0 | 126 | 55.021834% | Within0.05pp; integer unique; completion≤randomized |

| Local ID | Location (all PLAN) | Rule / printed inputs | Completed check |
|---|---|---|---|
| N367 | DOC-002 p29 lines1448–1449 and Table5 | 218/259 vs84.2% white | 84.169884% rounds to84.2%; within0.05pp |
| N368 | DOC-002 p29 lines1448–1449 and Table5 | 29/259 vs11.2% Black | 11.196911% rounds to11.2%; within0.05pp |
| N369 | DOC-002 p29 lines1448–1449 and Table5 | 12/259 vs4.6% Asian | 4.633205% rounds to4.6%; within0.05pp |
| N370 | DOC-002 p29 lines1448–1449 and Table5 | 30/259 vs11.6% Hispanic | 11.583012% rounds to11.6%; within0.05pp |
| N371 | DOC-002 p29 Table5 denominators | Race12+29+218 and ethnicity30+229 | Each259; racial composition sums100.0%; race and ethnicity form separate partitions, not combined518-person population |
| N372 | DOC-002 p29 Table5 Week6 | All five counts and percentages from N357,N359,N361,N363,N365 | Race implied9+22+163=194; ethnicity24+169=193. Difference1 person cannot be eliminated by0.05pp rounding. PL-CAND-01 |
| N373 | DOC-002 p29 Table5 Week12 | N358,N360,N362,N364,N366 | Race6+15+121=142; ethnicity16+126=142. Week12≤Week6 each row. Narrative highly comparable has no numerical threshold; no additional candidate |

## Exhaustive blinded-switch table pairs

All cells: [DOC-002 p41 switch table](../../../joi190079supp1_prod.pdf#page=41), PLAN. A=open-label olanzapine, B=blinded olanzapine/placebo. Each tablet nominal5mg. Pill total A+B must equal starting stratum. Continued arm active dose=5(A+B); placebo arm active olanzapine=5A. Values are pill counts, not rates or percentages. Repeated Week3/Week4 rows are explicitly scheduled, not an unexplained copied result.

| Local ID | Week | Starting pills | Printed A | Printed B | A+B | Continued-arm active mg | Placebo-arm active mg | Check |
|---|---|---:|---:|---:|---:|---:|---:|---|
| N374 | 1 | 4 | 3 | 1 | 4 | 20 | 15 | Exact sum; range coherent |
| N375 | 1 | 3 | 2 | 1 | 3 | 15 | 10 | Exact sum; range coherent |
| N376 | 1 | 2 | 1 | 1 | 2 | 10 | 5 | Exact sum; range coherent |
| N377 | 1 | 1 | 1 | 0 | 1 | 5 | 5 | Exact sum; range coherent |
| N378 | 2 | 4 | 2 | 2 | 4 | 20 | 10 | Exact sum; range coherent |
| N379 | 2 | 3 | 2 | 1 | 3 | 15 | 10 | Exact sum; range coherent |
| N380 | 2 | 2 | 1 | 1 | 2 | 10 | 5 | Exact sum; range coherent |
| N381 | 2 | 1 | 1 | 0 | 1 | 5 | 5 | Exact sum; range coherent |
| N382 | 3 | 4 | 1 | 3 | 4 | 20 | 5 | Exact sum; range coherent |
| N383 | 3 | 3 | 1 | 2 | 3 | 15 | 5 | Exact sum; range coherent |
| N384 | 3 | 2 | 1 | 1 | 2 | 10 | 5 | Exact sum; range coherent |
| N385 | 3 | 1 | 1 | 0 | 1 | 5 | 5 | Exact sum; range coherent |
| N386 | 4 | 4 | 1 | 3 | 4 | 20 | 5 | Exact sum; range coherent |
| N387 | 4 | 3 | 1 | 2 | 3 | 15 | 5 | Exact sum; range coherent |
| N388 | 4 | 2 | 1 | 1 | 2 | 10 | 5 | Exact sum; range coherent |
| N389 | 4 | 1 | 1 | 0 | 1 | 5 | 5 | Exact sum; range coherent |
| N390 | Thereafter | 4 | 0 | 4 | 4 | 20 | 0 | Exact sum; range coherent |
| N391 | Thereafter | 3 | 0 | 3 | 3 | 15 | 0 | Exact sum; range coherent |
| N392 | Thereafter | 2 | 0 | 2 | 2 | 10 | 0 | Exact sum; range coherent |
| N393 | Thereafter | 1 | 0 | 1 | 1 | 5 | 0 | Exact sum; range coherent |
| N394 | Starting-dose equivalence | 4 | — | — | 4 | 20 | — | 4 pills×5mg=20mg within5–20mg; stratum-specific taper nonincreasing active placebo-arm dose |
| N395 | Starting-dose equivalence | 3 | — | — | 3 | 15 | — | 3 pills×5mg=15mg within5–20mg; stratum-specific taper nonincreasing active placebo-arm dose |
| N396 | Starting-dose equivalence | 2 | — | — | 2 | 10 | — | 2 pills×5mg=10mg within5–20mg; stratum-specific taper nonincreasing active placebo-arm dose |
| N397 | Starting-dose equivalence | 1 | — | — | 1 | 5 | — | 1 pills×5mg=5mg within5–20mg; stratum-specific taper nonincreasing active placebo-arm dose |

| Local ID | Source locations (PLAN) | Rule / inputs | Completed check |
|---|---|---|---|
| N398 | DOC-002 p41 lines2069–2070 vs p10 Table1 header, p11 footnotes A/D lines491,500–501; p25 lines1244–1248/p40 lines2043–2044; p7 lines326–332 | Printed pre-RCT sertraline 10–20 weeks vs acute 4–12 weeks plus stabilization 8 weeks, with an allowed two additional weekly stabilization visits | Ordinary calculated range 12–20 weeks; lower printed bound may be conservative. Authorized extension permits 12+8+2=22 weeks before RCT while open-label sertraline continues in stabilization. Printed maximum 20 needs exception qualification. PL-CAND-02; p13 repeats minimum 10 and corroborates the lower endpoint |
| N399 | DOC-002 p41 switch table vs p7/p13 four-week taper statement | Week4 retains1 A pill in every stratum; thereafter A0. Four-week interval may include switch at its ending boundary | No weekly-uniform25% reduction requirement printed.1-pill stratum remains5mg active during all four listed weeks, then0. Boundary convention unresolved but table describes four-week transition; no independent timing contradiction established |
| N400 | DOC-002 p27 lines1310–1311 vs p10–11 Table1 | Metabolic week4 acute then every8weeks; direct table marks baseline,acute4/end,stabilization8,RCT8/16/24/32/36 | Current mapper originally misaligned RCT marks as8/12/20/28/36. Direct pp10–11 rendering corrects them. Phase-end and termination extra measurements account for shortened terminal4-week gap. Variable acute end prevents deriving one absolute cadence; no numerical contradiction without schedule-override definition |

## DOC-004 completion and role boundary

[DOC-004 p1](../../../joi190079supp3_prod.pdf#page=1) is data availability with publication and access approval/agreement conditions; no displayed quantitative relationship, no participant dataset supplied. Curator PLAN versus mapper REPORT is a role disagreement outside numeric candidate scope. Content is operational; PLAN is supported by prospective operational-document definition, but administrative disclosure REPORT remains a bounded classification question for coordinator/recheck if ever compared. No candidate solely for role assignment. No PL ID assigned to absent numeric evidence.

## Completion

116/116 local relationships checked,22/22 origin pages covered (DOC-00221 and DOC-0041). Both full tables inspected without sampling; references and administrative units explicitly nonapplicable where no result. Two candidate records in paired checker; no stable C IDs, severity, validity, or disposition assigned. No inferential P/CI compatibility input available in this shard beyond ordered historical ICC ranges; no display-zero P. No scientific-coverage limitation. Underlying historical raw completion counts and any disclosed schedule amendment are not supplied; exact human questions are retained in checker cards.



