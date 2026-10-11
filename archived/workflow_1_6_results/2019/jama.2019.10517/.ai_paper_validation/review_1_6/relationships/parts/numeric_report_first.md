# Numeric relationship inventory — main article origins pages 1–6

Runtime: `01a1286a-6645-7930-8d1b-45686ffab070`; fresh numeric reviewer `gpt-6.1-sol`/`medium`. Scope: DOC-001 (`jama_flint_2019_oi_190079.pdf`) PDF pp.1–6. Origin scope is disjoint from the pages7–10/results-supplement and PLAN numeric shards. Counterpart locations outside pp.1–6 are used only to check a first-six-page origin. O=sertraline+olanzapine (64); P=sertraline+placebo (62). Every location in DOC-001 is REPORT. DOC-003 eFigure8 is REPORT. No PLAN conflict is emitted by this shard.

Source authority: direct Poppler26.01.0 `pdftotext -layout` stdout for pp1–6, targeted pp3/4; current complete main/support maps as locators; source-matched reused rendered pp5/6 visually inspected. No new derivatives, OCR, Python, GPU, web, old checker/candidate/report inputs. Direct source files preserved. Each numbered row is one quantitative relationship; a row may test both arms or several components of one partition. Inferential P-value/test calculations belong to the statistical reviewer; numeric estimate/unit/repeat relationships are covered here.

Tolerances: integer totals exact; one-decimal percentages normally ±0.05 percentage points with midpoint ties accepted in either direction; percentage sums permit cumulative displayed rounding, never unexplained integer deficits. Rounded group means/SDs admit their displayed precision. A result labeled COMPATIBLE is not a finding or adjudication. There is no candidate limit.

| Local relationship | Exact source scope | Printed inputs and reproducible check | Tolerance/identity condition | Outcome |
|---|---|---|---|---|
| RF001 | Abstract arm allocation; pp1/3/6 | 64+62=126; all printed randomized totals126 | Exact count | Reconciles |
| RF002 | Abstract women; p1 versus Table1 p5 | 37+41=78; 78/126×100=61.9048%, printed61.9% | ±0.05pp | Reconciles |
| RF003 | Abstract completion; p1 versus flow p3 | 43+24+13+34=114; 126−8−4=114;114/126×100=90.4762%, printed90.5% | ±0.05pp | Reconciles: includes relapse endpoints; completion in remission alone67 is a different node |
| RF004 | Abstract mean age; p1 versus Table1 p5 | (64×55.0+62×55.7)/126=55.3444, printed55.3 | ±0.1y allowing component rounding | Reconciles |
| RF005 | Abstract age SD; p1 versus Table1 p5 | Pooled SD from rounded group moments≈14.946, printed14.9 | Group SD rounding ±0.05; final±0.05 | Compatible rounding; raw moments unavailable |
| RF006 | Relapse O; pp1/2/6 | 13/64×100=20.3125%, printed20.3%; same count/denominator repeated | ±0.05pp | Reconciles |
| RF007 | Relapse P; pp1/2/6 | 34/62×100=54.8387%, printed54.8%; same count/denominator repeated | ±0.05pp | Reconciles |
| RF008 | Relapse treatment measure; pp1/6 | Adjusted Cox HR0.25(0.13–0.48); crude RR=(13/64)/(34/62)=0.3704 | Distinct adjusted time-to-event vs crude risk estimands | No discrepancy: HR is correctly named; crude RR need not equal HR |
| RF009 | Abstract sertraline median; p1/Table2 p6 | Pooled150(150–200) versus both arms150(150–200)mg/day | Quantile identity not guaranteed by group summaries | Compatible; no reconstruction of pooled IQR claimed |
| RF010 | Abstract olanzapine median; p1/Table2 p6 | Pooled15(10–20) versus both arms15(10–20)mg/day | Quantile identity not guaranteed | Compatible |
| RF011 | Abstract daily weight; p1/p7 | 0.13lb/day (0.11–0.15) repeats; treatment×linear-time; quadratic time also present | Printed precision | Reconciles; do not multiply by252 to equate with raw change |
| RF012 | Abstract daily waist; p1/p7 | 0.009in/day (0.004–0.014) repeats | Printed precision | Reconciles; same model restriction |
| RF013 | Abstract daily total cholesterol; p1/p7 | 0.29mg/dL/day (0.13–0.45) repeats | Printed precision | Reconciles; coefficient not a raw endpoint difference |
| RF014 | Abstract daily LDL; p1/p7 | 0.04mg/dL/day (−0.01–0.10) repeats | Printed precision | Reconciles |
| RF015 | Abstract daily HDL; p1/p7 | −0.01mg/dL/day (−0.03–0.01) repeats | Printed precision | Reconciles |
| RF016 | Abstract daily triglyceride; p1/p7 | −0.153mg/dL/day (−0.306–0.004) repeats; pattern-mixture averaged | Printed precision | Reconciles; distinct calculation conventions retained |
| RF017 | Abstract daily glucose; p1/p7 | −0.02mg/dL/day (−0.12–0.08) repeats | Printed precision | Reconciles |
| RF018 | Abstract daily HbA1c; p1/p7 versus Table4 p8/eFigure8 DOC003 p9 | −0.0002 printed mg/dL; Table4 and figure label HbA1c% | Exact dimensional identity | RF-CAND-05 |
| RF019 | Enrollment stages; Fig1 p3/p6 | 350−81=269; p6 enrolled269 | Exact counts | Reconciles; consented and enrolled denote different stages |
| RF020 | Excluded reasons; Fig1 p3 | 60+16+5=81 | Exact counts | Reconciles |
| RF021 | Acute exit; Fig1 p3 | 269−74=195 | Exact counts | Reconciles |
| RF022 | Acute discontinuation reasons; Fig1 p3 | 31+21+7+5+1+9=74 | Exact counts | Reconciles |
| RF023 | Acute-to-stabilization; Fig1 p3 | 195−33=162 | Exact counts | Reconciles |
| RF024 | Stabilization exit; Fig1 p3 | 162−15=147 | Exact counts | Reconciles |
| RF025 | Stabilization discontinuation reasons; Fig1 p3 | 4+2+1+1+7=15 | Exact counts | Reconciles |
| RF026 | Stabilization-to-randomization; Fig1 p3 | 147−21=126 | Exact counts | Reconciles |
| RF027 | Not randomized reasons; Fig1 p3 | 12+9=21 | Exact counts | Reconciles |
| RF028 | O allocation receipt; Fig1 p3 | 59+5=64;3+2=5 | Exact counts | Reconciles |
| RF029 | P allocation receipt; Fig1 p3 | 60+2=62;1+1=2 | Exact counts | Reconciles |
| RF030 | O disposition; Fig1 p3 | 43+13+8=64;1+5+1+1=8 | Exact counts | Reconciles |
| RF031 | P disposition; Fig1 p3 | 24+34+4=62;1+3=4 | Exact counts | Reconciles |
| RF032 | Analysis population; pp3/4/6 | ITT64/62 includes not-as-randomized5/2;119 received allocation vs126 analyzed | Different stages | Reconciles; treatment receipt not analysis exclusion |
| RF033 | Acute eligibility/time; pp1/2/3 | 18–85 actual age eligibility satisfies abstract≥18;acute≤12wk; stabilization8wk; randomized36wk | Exact definitions | Compatible; summary lower bound is not an alternative upper bound |
| RF034 | Remission/near-remission; pp2/3 | HDRS≤10 vs11–15 with≥50% improvement; no psychosis;MMSE≥24 | Disjoint threshold definitions | No concrete numeric conflict |
| RF035 | Randomization strata/sites; pp2/4/5 | 18–59/60–85 partitions eligibility;4 named sites;1:1 target with actual64/62 | Blocked allocation may differ overall | Compatible |
| RF036 | Intervention/visit schedule; pp1/4 | 4-week taper, weekly first8wk then every4wk through36wk; metabolic every8wk plus termination | Exact time units | Compatible; terminal observations may differ by relapse |
| RF037 | Relapse thresholds; p4 | ≥1 criterion;HDRS≥18 vs baseline remitted≤15 | Threshold identity | Compatible; event criteria can overlap |
| RF038 | Barnes incident rule/range; pp4/6 | Global0–5;baseline0 then≥2; Table2 positive baseline3/2 participants differs from incident | Exact population/time definitions | Compatible |
| RF039 | AIMS descriptions; pp4/6 | p4 each10items0–5;Table2 global0–4;global-positive2/2 participants | Individual items versus named global summary not demonstrably identical | No emitted candidate: item mapping absent; no arithmetic contradiction in reported counts |
| RF040 | Simpson-Angus range; pp4/6 | 0–40 methods vs0–36 Table2 explicitly excluding head-dropping | Different item sets | Compatible |
| RF041 | UKU adverse-effect range/rule; p4 | Each48items0–3;rule2-point increase or score3or4 with increase | Exact integer range | RF-CAND-04 |
| RF042 | Weight threshold; pp4/5 | Gain/loss>7% relative premorbid most-recent pre-episode weight; Table1 same reference definition | Strict thresholds and reference identity | Compatible within main report; PLAN definitions reviewed separately |
| RF043 | Power/NNT; p4 | 20% absolute risk difference⇒1/0.20=5;80% power,176 revised128; observed126 | Exact reciprocal;planned vs observed distinct | Reconciles; no observed-vs-target discrepancy claimed |
| RF044 | Statistical conventions; pp4/5/6 | All randomized;Cox adjusted3 strata;MAR/pattern-mixture;2-sided overall5%;Holm secondary post hoc | Estimates retain stated model/test identity | No numeric contradiction; inferential diagnostics delegated |
| RF045 | Table1 Age means/SD; p5 | 55.0(15.1)/55.7(14.9); Within eligibility18–85; component/pooled repeats RF004/005 | Printed resolution; no raw reconstruction | Compatible |
| RF046 | Table1 Age18–59; p5 | O36(56.2):100×36/64=56.2500%; P36(58.1):100×36/62=58.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF047 | Table1 Age≥60; p5 | O28(43.8):100×28/64=43.7500%; P26(41.9):100×26/62=41.9355% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF048 | Table1 Men; p5 | O27(42.2):100×27/64=42.1875%; P21(33.9):100×21/62=33.8710% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF049 | Table1 Women; p5 | O37(57.8):100×37/64=57.8125%; P41(66.1):100×41/62=66.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF050 | Table1 White; p5 | O54(84.4):100×54/64=84.3750%; P49(79):100×49/62=79.0323% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF051 | Table1 Black; p5 | O6(9.4):100×6/64=9.3750%; P9(14.5):100×9/62=14.5161% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF052 | Table1 Other race; p5 | O4(6.3):100×4/64=6.2500%; P4(6.5):100×4/62=6.4516% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF053 | Table1 Hispanic; p5 | O6(9.4):100×6/64=9.3750%; P9(14.5):100×9/62=14.5161% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF054 | Table1 Single; p5 | O19(29.7):100×19/64=29.6875%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF055 | Table1 Married; p5 | O28(43.8):100×28/64=43.7500%; P35(56.5):100×35/62=56.4516% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF056 | Table1 Separated/divorced; p5 | O12(18.8):100×12/64=18.7500%; P7(11.3):100×7/62=11.2903% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF057 | Table1 Widowed; p5 | O5(7.8):100×5/64=7.8125%; P5(8.1):100×5/62=8.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF058 | Table1 Education; p5 | 14.4(3.2)/13.4(3.9)y; Nonnegative mean/SD; distinct age/education labels | Printed resolution; no raw reconstruction | Compatible |
| RF059 | Table1 With others; p5 | O46(71.9):100×46/64=71.8750%; P49(79):100×49/62=79.0323% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF060 | Table1 Alone; p5 | O17(26.6):100×17/64=26.5625%; P10(16.1):100×10/62=16.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF061 | Table1 Senior residence; p5 | O1(1.6):100×1/64=1.5625%; P1(1.6):100×1/62=1.6129% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF062 | Table1 Inpatient acute baseline; p5 | O41(64.1):100×41/64=64.0625%; P46(74.2):100×46/62=74.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF063 | Table1 Cornell; p5 | O16(25):100×16/64=25.0000%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF064 | Table1 Massachusetts; p5 | O15(23.4):100×15/64=23.4375%; P14(22.6):100×14/62=22.5806% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF065 | Table1 Pittsburgh; p5 | O9(14.1):100×9/64=14.0625%; P10(16.1):100×10/62=16.1290% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF066 | Table1 Toronto; p5 | O24(37.5):100×24/64=37.5000%; P23(37.1):100×23/62=37.0968% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF067 | Table1 ≥2 lifetime episodes; p5 | O47(73.4):100×47/64=73.4375%; P47(75.8):100×47/62=75.8065% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF068 | Table1 Episode duration; p5 | 5.5(3–12)/5.5(2–12)mo;P n60; Median inside IQR;missingP2; explicit n≤62 | Printed resolution; no raw reconstruction | Compatible |
| RF069 | Table1 First episode age; p5 | 37(24–50)n62/35(18–51)n61; Median inside IQR;missingO2/P1; onset precedes current group age on average | Printed resolution; no raw reconstruction | Compatible; no participant pairing inferred |
| RF070 | Table1 Suicide attempt; p5 | O13(20.3):100×13/64=20.3125%; P12(19.4):100×12/62=19.3548% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF071 | Table1 Resistance; p5 | O3(4.7):100×3/64=4.6875%; P5(8.1):100×5/62=8.0645% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF072 | Table1 Hyperlipidemia; p5 | O18(29):100×18/64=28.1250%; P19(29.7):100×19/62=30.6452% | ±0.05pp; exact .05 ties allow either nearest endpoint | RF-CAND-01 |
| RF073 | Table1 Hypertension; p5 | O17(26.6):100×17/64=26.5625%; P22(35.5):100×22/62=35.4839% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF074 | Table1 Diabetes; p5 | O12(18.8):100×12/64=18.7500%; P15(24.2):100×15/62=24.1935% | ±0.05pp; exact .05 ties allow either nearest endpoint | Reconciles |
| RF075 | Table1 Premorbid weight; p5 | 166.6(34.6)n60/171.4(40.2)n59lb; MissingO4/P3;nonnegative means/SD;lb consistent with stated conversion | Printed resolution; no raw reconstruction | Compatible |
| RF076 | Table1 age/sex/race sums; p5 | O36+28=64;27+37=64;54+6+4=64;P36+26=62;21+41=62;49+9+4=62 | Exact counts;rounded percentages need not sum exactly100 | Reconciles; race Other includes unknown |
| RF077 | Table1 marital/site sums; p5 | O19+28+12+5=64;16+15+9+24=64;P15+35+7+5=62;15+14+10+23=62 | Exact counts | Reconciles |
| RF078 | Table1 living sums; p5 | O46+17+1=64;P49+10+1=60≠62;P79.0+16.1+1.6=96.7% | Exact counts;rounded sum tolerance≤0.15pp | RF-CAND-02 |
| RF079 | Table2 HDRS; p6 | 5.3(3.6)/5.6(3.6),scale0–52 higher worse; mean rounded5 footnote | ±0.5 for integer summary | Compatible |
| RF080 | Table2 delusions; p6 | 64/64=100%;62/62=100%; score1 absent,range1–7 | Exact100 and score definitions | Reconciles |
| RF081 | Table2 hallucinations; p6 | 64/64=100%;62/62=100%; score1 absent,range1–3 | Exact100 and score definitions | Reconciles |
| RF082 | Table2 HADS; p6 | 5(2–8)/4(1–7)n61,range0–21,≤7 normal | IQR order; missingP1 explicit | Reconciles; IQR may extend beyond normal despite median normal |
| RF083 | Table2 CORE; p6 | 1(0–3)/1(0–4.8),range0–54;median1 minimal | IQR order; interpolation allows decimal4.8 | Reconciles |
| RF084 | Table2 CIRS; p6 | 3(1–6)/3(2–5.8),range0–52;excludes psychiatric category | IQR order; interpolation allows decimal5.8 | Reconciles |
| RF085 | Table2 MMSE; pp3/6 | 28.1(1.9)/27.9(2.0),range0–30;eligible≥24;footnote mean28 | ±0.5 integer summary; mean≤30 | Reconciles; SD alone cannot establish individual eligibility violation |
| RF086 | Table2 DKEFS trails; p6 | 7.9(3.5)n61/8.1(3.6)n59;footnoteh scaled1–19 higher better,normative10 | MissingO3/P3;means within range | Reconciles |
| RF087 | Table2 DKEFS color-word/footnote; p6 | 8.6(2.9)n60/7.6(2.8)n58,rowsuperscripti;footnotei Barnes0–5,footnoteh both DKEFS1–19 | Exact footnote identity;means>5 | RF-CAND-03 |
| RF088 | Table2 Barnes positive; p6 | 3.0(4.7)/2.0(3.2);3/64=4.6875%;2/62=3.2258% | ±0.05pp;decimal integer counts | Reconciles; default No.(%) is explicit |
| RF089 | Table2 AIMS positive; p6 | 2.0(3.1)/2.0(3.2);2/64=3.125%;2/62=3.2258%;global0–4 | ±0.05pp | Reconciles; threshold>0 baseline not incident criterion |
| RF090 | Table2 Simpson-Angus; p6 | 1(0–2)/1(0–2),range0–36 excluding item | Exact range and IQR order | Reconciles |
| RF091 | Table2 sertraline; pp1/2/6 | 150(150–200)mg/day both;target150–200;50mg pills | Median/IQR within target | Reconciles |
| RF092 | Table2 olanzapine; pp1/2/6 | 15(10–20)mg/day both;target15–20;5mg pills | Observed tolerated dosage distinct from target | Compatible;IQR10 not a target adherence inconsistency |
| RF093 | Unit conversions; pp5/6 | lb×0.45kg repeated;cholesterol×.0259,glucose×.0555,triglyceride×.0113 to mmol/L;in×2.54cm | Compare internal repeated factors;no external reference | Reconciles; .45 is displayed approximate factor |
| RF094 | Secondary time units/count distinction; pp1/4/6 | Daily linear-time interaction anthropometric/metabolic,weekly/four/eight-week assessment schedule;incident participants descriptive | Different parameter/observation units | No rate/count confusion; no person-time totals supplied |
| RF095 | Primary age contrast; p6 | HR0.78(0.42–1.46),young vsold; groups defined18–59 vs60–85 | Exact label/reference identity;statistical pass handles interval/P | Compatible |
| RF096 | Secondary significance prose; p1/p6/p7 | Weight/waist/total cholesterol significant;LDL/HDL/triglyceride/glucose/HbA1c not;Holm adjusted post hoc | Same coefficient contrast and exploratory convention | No arithmetic contradiction; full P/CI diagnostics statistical lane |

Completed 96 relationships. Five distinct local candidates RF-CAND-01 through RF-CAND-05. All assigned source pages and mapped quantitative components inspected; no scientific coverage gap. Limitation: no raw data, paired individual values, unprinted living-arrangement missingness category, or explicit hyperlipidemia denominator supplied. Item-level AIMS mapping does not establish identity with its global summary, so differing ranges alone do not support a candidate. No display-zero P occurs in this scope. Planned power cannot be reconstructed without unprinted assumptions and is not treated as a candidate merely for those omissions. Stable N/C IDs belong to coordinator.

