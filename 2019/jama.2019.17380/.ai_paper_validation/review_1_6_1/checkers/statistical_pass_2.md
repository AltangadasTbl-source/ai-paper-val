# Statistical consistency review — pass 2, bounded shard A

Runtime task: /root/statistics_pass2; fresh qc161_statistical_consistency_reviewer, gpt-6.1-sol/high, FRESH_SPAWN, distinct from pass 1. The coordinator records the exact spawn runtime ID. Assigned scope is exclusively the 108 records S001–S108 in statistics/parts/relationship_inventory_a.md. Shard B covers S109–S140 separately; the coordinator merges its durable output and updates the canonical inventory. This agent modifies no inventory or source.

## Evidence and complete checks

QUALITY_CONTROL_SCOPE.md and the complete review contract were read. The complete current ledger C001, C002, C003, C004, C005, initial inclusion screen, completed mechanical recheck, and pass-1 findings/exclusions were considered before revisiting every assigned relationship. Exact supplied sources remain authoritative. REPORT denotes the retrospective main article and results supplement; PLAN denotes the prospective protocol and implemented addendum.

Direct CPU Poppler pdftotext -layout rereads covered main physical pp.1–4 and8–9, results supplement pp.9–15, and plan pp.32–33. Existing direct-source Poppler renders preprocessing/numeric-main-p8.png, numeric-main-p9.png, numeric-supp2-p18.png and numeric-supp2-p19.png were visually inspected in full. The mechanical recheck's source-confirmed randomized arm and subgroup counts were reused for count comparisons. Every printed observed mean, arm change, contrast, rate, rate difference, HR and interval in the assigned row families was revisited; all 52 forest rows were visually revisited. No external evidence, earlier-run conclusions, source mutation, additional derivative or GPU was used.

For each table family, the checks include point containment, endpoint order, scale/null, numerical direction, applicable confidence and significance rules, displayed counts and population, matching narrative/figure occurrences, stated adjustment/model, and implications of all five recheck records. For every forest row, the point lies inside its ordered graphical interval; primary eGFR intervals cross0 and ACR intervals cross1. Each repeated P is attached to a subgroup-family interaction, not a separate subgroup treatment-effect test. For every event tuple, both rates and their intervals, rate difference/interval, HR/interval, event counts and HR-null P were checked. Every event HR interval includes1, compatible with nonsignificance; the displayed1.00/.05 boundary is not an independent contradiction.

The report states a two-sided P<.05 treatment-by-year5 test,95% intervals, participant random-intercept mixed models and Rubin combination. The significant/non-significant decision agrees with every reported year5 tuple. No noninferiority/equivalence margin or multiplicity adjustment is invented. Exact standard errors, Rubin degrees of freedom, covariance and unrounded outputs are absent. Cox test subtype, tie handling and variance estimator are absent, preventing exact inversion under an assumed Wald calculation. Arm summaries and adjusted contrasts are not substituted for each other. The reported coherent mixed-model and Cox choices are not questioned, and no preferred method is proposed.

## Reconciliation with the stable ledger

- C001 remains the existing PLAN/REPORT adherence-definition comparison. S013–S018 and S031–S036 use the reported1032-participant questionnaire restriction; their inferential tuples do not add a distinct issue. The planned continuous80% membership and its results are absent, so no numerical consequence is inferred.
- C002 and C003 concern the primary model specification and population correspondence, respectively. S003/S006 retain these ledger implications. The displayed Table2 time-point contributor counts are not the full imputed population; follow-up blood/urine overlap is absent. PLAN §15c does not say “only,” so the mechanical recheck's minimum-inclusion-guarantee alternative is retained. No exact reduced planned population is inferred.
- C004 remains one consolidated REPORT count-to-summary alignment pattern over S043–S094. The recheck's52 display occurrences comprise22 independently reconstructable arm/stratum mismatches and30 pattern occurrences lacking independent arm-stratum comparators. Equal87/87 BMI counts do not independently establish a discrepancy. Nothing in that count comparison establishes changed adjusted point estimates, CIs, P values or subgroup tests, and an independent-sample SE reconstructed from these SDs would not be the reported imputed longitudinal analysis.
- C005 remains the eTable7 analysis-N comparison affecting S025–S030:504+440=944 and477+467=944, whereas1311−320=991. These exact constructions differ by47. The point estimates and their inference are internally compatible; missing specimen/eligibility accounting does not justify a separate candidate for each row.

No previously screened finding is re-emitted. All five stable candidates remain Pending Human Adjudication. Reproduced evidence states and current classifications are retained; neither an adjudication nor an effect-size consequence is assigned.

## Explicit per-relationship pass-2 records

The exact source location and complete-family definitions are those of the same ID in statistics/parts/relationship_inventory_a.md; source-page links are also collected below. Each outcome records the row's result after the common complete checks above, including relevant ledger implications. “Ordered/contained” covers all printed arm mean, change and contrast intervals on that row, not only the compact contrast shown here.

| S ID | Pass 2 | Row-specific reconciliation and limits |
|---|---|---|
| S001 | PASS_2_COMPLETE | D baseline observed means86.3/85.3 and95%CIs ordered/contained; observed701/607 are contributors, not full randomized703/609. |
| S002 | PASS_2_COMPLETE | D year2 changes−5.2/−6.1;contrast0.9(−0.6,2.5) ordered/contained; source reserves primary inference for year5. |
| S003 | PASS_2_COMPLETE | D year5 difference0.9(−0.7,2.5),P=.25 supports nonsignificance; matches abstract/narrative. C002/C003 remain specification comparisons, C004 concerns forest N pairing. |
| S004 | PASS_2_COMPLETE | Omega baseline85.7/86.0 and95%CIs ordered/contained;657/651 contributors reconcile1308 measured baseline values. |
| S005 | PASS_2_COMPLETE | Omega year2 contrast−0.3(−1.8,1.3) ordered/contained; subtracting rounded−5.7/−5.5 permits−0.3. |
| S006 | PASS_2_COMPLETE | Omega year5 difference0.9(−0.7,2.6),P=.27 supports nonsignificance and matched text; C002/C003/C004 do not supply another estimate/test issue. |
| S007 | PASS_2_COMPLETE | Complete-case D baseline86.2/85.4 andCIs ordered/contained;495+437=932 agrees with title and1312−376−4. |
| S008 | PASS_2_COMPLETE | Complete-case D year2 difference1.18(−.59,2.95) ordered/contained;443/389 contributors may be less than endpoint-complete N. |
| S009 | PASS_2_COMPLETE | Complete-case D year5 .87(−.83,2.58),P=.32 supports robustness narrative; no invented exact MI test inversion. |
| S010 | PASS_2_COMPLETE | Complete-case Omega baseline86.0/85.6 andCIs ordered/contained;470+462=932. |
| S011 | PASS_2_COMPLETE | Complete-case Omega year2−.93(−2.66,.81) ordered/contained;424+408=832 equals D year2 contributor total. |
| S012 | PASS_2_COMPLETE | Complete-case Omega year5 .09(−1.61,1.80),P=.92 supports nonsignificance; endpoint counts470/462 match baseline. |
| S013 | PASS_2_COMPLETE | Adherent D baseline86.2/85.8 ordered/contained;544+485=1029 measured values within1032 adherent participants. C001 definition retained. |
| S014 | PASS_2_COMPLETE | Adherent D year2 .73(−.89,2.36) ordered/contained; count reduction does not redefine1032 imputed adherence population. |
| S015 | PASS_2_COMPLETE | Adherent D year5 .89(−.74,2.52),P=.28 supports stated robustness; C001 addresses population rule rather than incompatible inference. |
| S016 | PASS_2_COMPLETE | Adherent Omega baseline86.2/85.5 ordered/contained;517+513=1030 measured values within1032. C001 retained. |
| S017 | PASS_2_COMPLETE | Adherent Omega year2−.48(−2.10,1.14) ordered/contained; no year2 primary significance claim. |
| S018 | PASS_2_COMPLETE | Adherent Omega year5 .42(−1.22,2.06),P=.61 compatible; C001 supplies existing definition discrepancy only. |
| S019 | PASS_2_COMPLETE | Full ACR D baseline geometric means3.3/3.2 with ordered/containedCIs;702+609=1311 measured baseline; ratio reference1. |
| S020 | PASS_2_COMPLETE | Full ACR D year2 ratio1.14(.96,1.37) ordered/contained; arm geometric changes1.79/1.57 agree with numerical direction. |
| S021 | PASS_2_COMPLETE | Full ACR D year5 .99(.84,1.17),P=.90 compatible; ratio-null1 and label active/placebo retained. Forest N issue is C004. |
| S022 | PASS_2_COMPLETE | Full ACR Omega baseline3.3/3.2 ordered/contained;658+653=1311; missing baseline1 is source-defined. |
| S023 | PASS_2_COMPLETE | Full ACR Omega year2 .97(.81,1.16) ordered/contained; changes1.66/1.71 support ratio direction. |
| S024 | PASS_2_COMPLETE | Full ACR Omega year5 .96(.81,1.14),P=.64 compatible;2.94/3.05 matches direction and forest summary. |
| S025 | PASS_2_COMPLETE | Complete-case ACR D baseline3.0/3.1 ordered/contained;504/440 identifies944; conflicting991 footnote already C005. |
| S026 | PASS_2_COMPLETE | Complete-case ACR D year2 1.20(1.00,1.44) ordered/contained; no printed year2 significance decision; C005N remains unresolved. |
| S027 | PASS_2_COMPLETE | Complete-case ACR D year5 1.03(.86,1.22),P=.77 compatible; population accounting is existing C005, not another test issue. |
| S028 | PASS_2_COMPLETE | Complete-case ACR Omega baseline3.1/3.0 ordered/contained;477+467=944, reiterating C005. |
| S029 | PASS_2_COMPLETE | Complete-case ACR Omega year2 .96(.80,1.15) ordered/contained;433+412=845 equals D year2 contributor total. C005 retained. |
| S030 | PASS_2_COMPLETE | Complete-case ACR Omega year5 .93(.78,1.11),P=.44 compatible; same unresolved944/991 population issue C005. |
| S031 | PASS_2_COMPLETE | Adherent ACR D baseline3.1/3.1 ordered/contained;545+486=1031 measured baseline within1032. C001 retained. |
| S032 | PASS_2_COMPLETE | Adherent ACR D year2 1.20(1.00,1.43) ordered/contained; no year2 significance claim; C001 definition unchanged. |
| S033 | PASS_2_COMPLETE | Adherent ACR D year5 1.02(.85,1.22),P=.87 compatible; no distinct issue beyond C001 membership rule. |
| S034 | PASS_2_COMPLETE | Adherent ACR Omega baseline3.1/3.1 ordered/contained;517+514=1031 measured baseline within1032. |
| S035 | PASS_2_COMPLETE | Adherent ACR Omega year2 .96(.80,1.16) ordered/contained;461+441=902 contributors and different missingness than D are not contradictory. |
| S036 | PASS_2_COMPLETE | Adherent ACR Omega year5 .99(.83,1.19),P=.94 compatible; C001 retained without inventing planned80% results. |
| S037 | PASS_2_COMPLETE | UTI-excluded ACR D baseline3.3/3.1 ordered/contained;680+582=1262 visits, explicitly a visit-exclusion analysis. |
| S038 | PASS_2_COMPLETE | UTI-excluded ACR D year2 1.16(.97,1.39) ordered/contained; count and scale correspond to UTI-excluded visits. |
| S039 | PASS_2_COMPLETE | UTI-excluded ACR D year5 .99(.84,1.17),P=.90 compatible; no contradiction with full-population null result. |
| S040 | PASS_2_COMPLETE | UTI-excluded ACR Omega baseline source3.3(2.9,3.7)/3.1(2.8,3.6) ordered/contained; inventory-only upper endpoint3.6 must read3.7. No scientific finding. |
| S041 | PASS_2_COMPLETE | UTI-excluded ACR Omega year2 .96(.80,1.15) ordered/contained;482+477=959 agrees with D contributor total. |
| S042 | PASS_2_COMPLETE | UTI-excluded ACR Omega year5 .98(.83,1.16),P=.80 compatible; rounded arm-change quotient is not substituted for adjusted contrast. |
| S043 | PASS_2_COMPLETE | D forest overall point positive,CI crosses0; mean direction matches Table2.703/609 pairing remains C004; adjusted inference unaffected by a crude SE reconstruction. |
| S044 | PASS_2_COMPLETE | D White point positive,CI crosses0;family interactionP=.58. Independent451/406 assignment comparison is already C004. |
| S045 | PASS_2_COMPLETE | D Black point positive,CI crosses0;sameP=.58 family test. Independent148/130 comparison is C004. |
| S046 | PASS_2_COMPLETE | D ACR<30 point positive,CI crosses0;familyP=.36. Printed635/559N is C004 pattern occurrence without independent stratum comparator. |
| S047 | PASS_2_COMPLETE | D ACR≥30 point positive,CI crosses0;P=.36 family test.67/50N retained in C004 without alternative membership invented. |
| S048 | PASS_2_COMPLETE | D<20 point positive,CI crosses0;familyP=.15.110/85 independent counts repeat C004. |
| S049 | PASS_2_COMPLETE | D20–<30 point positive,CI crosses0;P=.15 family test.230/203 independent counts repeat C004. |
| S050 | PASS_2_COMPLETE | D≥30 point negative,CI crosses0;P=.15 family test; direction follows−12.3 versus−11.5.332/297 count comparison is C004. |
| S051 | PASS_2_COMPLETE | D eGFR≥60 point positive,CI crosses0;familyP=.18.612/531 is retained C004 pattern occurrence. |
| S052 | PASS_2_COMPLETE | D eGFR<60 point positive,CI crosses0;P=.18.89+76=165 agrees with overall baseline total, without independent arm allocation. |
| S053 | PASS_2_COMPLETE | D BMI<25 point positive,CI crosses0;familyP=.79;87/87 equalNs do not independently establish C004. |
| S054 | PASS_2_COMPLETE | D BMI25–<30 point near0,CI crosses0;P=.79.228/205 C004 pattern occurrence has no independent assignment comparator. |
| S055 | PASS_2_COMPLETE | D BMI≥30 point positive,CI crosses0;P=.79. Missing parenthesis is evident typography;364/294 retained C004 pattern. |
| S056 | PASS_2_COMPLETE | D within Omega placebo point near0 positive,CI crosses0;interactionP=.42 matches report.333/320 known armN repeats C004. |
| S057 | PASS_2_COMPLETE | D within Omega active point positive,CI crosses0;P=.42;370/289 known armN repeats C004. |
| S058 | PASS_2_COMPLETE | Omega forest overall positive point,CI crosses0; mean direction matches Table2;659/653N remains C004. |
| S059 | PASS_2_COMPLETE | Omega EPA/DHA≤2.2 positive point,CI crosses0;familyP=.72.332/347N remains C004 pattern with independent stratum counts absent. |
| S060 | PASS_2_COMPLETE | Omega EPA/DHA>2.2 positive point,CI crosses0;P=.72.308/292N retained without inventing alternative allocation. |
| S061 | PASS_2_COMPLETE | Omega ACR<30 positive point,CI crosses0;familyP=.70.596/598N remains existing C004 pattern. |
| S062 | PASS_2_COMPLETE | Omega ACR≥30 near0 negative point,CI crosses0;P=.70; adjusted point need not equal crude−1.0 difference.62/55N retained in C004. |
| S063 | PASS_2_COMPLETE | Omega hsCRP≤.2 positive point,CI crosses0;familyP=.73;334/335N is C004 pattern, no exact adjusted test reconstructed. |
| S064 | PASS_2_COMPLETE | Omega hsCRP>.2 positive point,CI crosses0;P=.73;323/316N is retained C004 occurrence. |
| S065 | PASS_2_COMPLETE | Omega fish<1.5 positive point,CI crosses0;familyP=.51.354/329N retained in C004. |
| S066 | PASS_2_COMPLETE | Omega fish≥1.5 near0 positive point,CI crosses0;P=.51.295/310N retained in C004. |
| S067 | PASS_2_COMPLETE | Omega within D placebo near0 positive point,CI crosses0;P=.42.289/320 known armN comparison is C004. |
| S068 | PASS_2_COMPLETE | Omega within D active positive point,CI crosses0;P=.42.370/333 known armN comparison is C004. |
| S069 | PASS_2_COMPLETE | D ACR forest overall point near1,CI crosses1;P=.89 versus table.90 is peripheral secondary display comparison.703/609 alignment remains C004. |
| S070 | PASS_2_COMPLETE | D ACR White point near1,CI crosses1;familyP=.30;451/406 independently supported count comparison is C004. |
| S071 | PASS_2_COMPLETE | D ACR Black point>1,CI crosses1;P=.30; numerical2.90/3.29 direction clear despite favor arrows;148/130 count pattern is C004. |
| S072 | PASS_2_COMPLETE | D ACR<30 point near1,CI crosses1;familyP=.99;635/559N retained as C004 occurrence without independent stratum count. |
| S073 | PASS_2_COMPLETE | D ACR≥30 point near1,CI crosses1;P=.99;67/50N retained as C004 occurrence. |
| S074 | PASS_2_COMPLETE | D ACR D<20 point>1,CI crosses1;familyP=.77;110/85N independently repeats C004. |
| S075 | PASS_2_COMPLETE | D ACR D20–<30 point<1,CI crosses1;P=.77;230/203N independently repeats C004. |
| S076 | PASS_2_COMPLETE | D ACR D≥30 point>1,CI crosses1;P=.77;332/297N independently repeats C004. |
| S077 | PASS_2_COMPLETE | D ACR eGFR≥60 point<1,CI crosses1;familyP=.69;612/531N retained in C004 without independent arm-stratum count. |
| S078 | PASS_2_COMPLETE | D ACR eGFR<60 point>1,CI crosses1;P=.69;89/76N is pattern occurrence, sum165 alone does not fix arm allocation. |
| S079 | PASS_2_COMPLETE | D ACR BMI<25 point<1,CI crosses1;familyP=.21; equal87/87Ns are not independently discrepant. |
| S080 | PASS_2_COMPLETE | D ACR BMI25–<30 point<1,CI crosses1;P=.21;228/205N retained in C004. |
| S081 | PASS_2_COMPLETE | D ACR BMI≥30 point>1,CI crosses1;P=.21;364/294N retained in C004; no subgroup significance inferred from familyP. |
| S082 | PASS_2_COMPLETE | D ACR within Omega placebo point<1,CI crosses1;interactionP=.53;333/320 known armN independently repeats C004. |
| S083 | PASS_2_COMPLETE | D ACR within Omega active point>1,CI crosses1;P=.53;370/289 known armN independently repeats C004. |
| S084 | PASS_2_COMPLETE | Omega ACR overall point<1,CI crosses1;P=.64 matches eTable6;659/653N alignment is existing C004. |
| S085 | PASS_2_COMPLETE | Omega ACR EPA/DHA≤2.2 point near1,CI crosses1;familyP=.50;332/347N is C004 pattern occurrence. |
| S086 | PASS_2_COMPLETE | Omega ACR EPA/DHA>2.2 point<1,CI crosses1;P=.50;308/292N retained in C004. |
| S087 | PASS_2_COMPLETE | Omega ACR<30 point<1,CI crosses1;familyP=.79;596/598N retained in C004. |
| S088 | PASS_2_COMPLETE | Omega ACR≥30 point<1,CI crosses1;P=.79;62/55N retained without independent arm-stratum reconstruction. |
| S089 | PASS_2_COMPLETE | Omega ACR hsCRP≤.2 point<1,CI crosses1;familyP=.31;334/335N retained in C004. |
| S090 | PASS_2_COMPLETE | Omega ACR hsCRP>.2 point>1,CI crosses1;P=.31;323/316N retained in C004. |
| S091 | PASS_2_COMPLETE | Omega ACR fish<1.5 point near1,CI crosses1;familyP=.68; equal rounded2.94 summaries do not identify exact adjusted ratio.354/329N retained in C004. |
| S092 | PASS_2_COMPLETE | Omega ACR fish≥1.5 point near1,CI crosses1;P=.68; adjusted graph need not equal crude2.94/3.15.295/310N retained in C004. |
| S093 | PASS_2_COMPLETE | Omega ACR within D placebo point<1,CI crosses1;interactionP=.53;289/320 known armNs independently repeat C004. |
| S094 | PASS_2_COMPLETE | Omega ACR within D active point near1,CI crosses1;P=.53;370/333 known armNs independently repeat C004. |
| S095 | PASS_2_COMPLETE | D composite85/79 events sum164;rates,RD andHR.92(.68,1.25) contained/ordered;P=.61 matches narrative. Person-time/Cox test subtype absent. |
| S096 | PASS_2_COMPLETE | D≥40% decline42+38=80;HR.97(.63,1.51),P=.90 compatible; rates/RD contained/ordered, and subset counts below composite. |
| S097 | PASS_2_COMPLETE | D ACR doubling111+74=185;HR1.34(1.00,1.80),P=.05 andRD1.1(.0,2.2) support precision-compatible nonsignificance under strictP<.05. |
| S098 | PASS_2_COMPLETE | Omega composite86+78=164 matches D margin;HR1.11(.81,1.50),P=.52 compatible;2.7−2.5 versusRD.3 reconciles display ranges. |
| S099 | PASS_2_COMPLETE | Omega≥40% decline40+40=80 matches D margin;HR.99(.64,1.54),P=.97 compatible;RD0(-.7,.7) contained/ordered. |
| S100 | PASS_2_COMPLETE | Omega ACR doubling96+89=185 matches D margin;HR1.08(.81,1.44),P=.60 compatible;rates/RD contained/ordered. |
| S101 | PASS_2_COMPLETE | D≥40%/kidney failure46+39=85;HR1.03(.68,1.58),P=.88 compatible; rounded1.7/1.7 rates permitRD.1. |
| S102 | PASS_2_COMPLETE | D≥30%/kidney failure/death125+130=255;HR.82(.64,1.05),P=.12 compatible;3.4−4.2 versusRD−.7 reconciles display ranges. |
| S103 | PASS_2_COMPLETE | D≥30%/kidney failure87+92=179;HR.82(.61,1.09),P=.17 compatible; event hierarchy87≥83,92≥91 andRD direction consistent. |
| S104 | PASS_2_COMPLETE | D≥30% decline83+91=174;HR.79(.59,1.06),P=.12 compatible;rates/RD ordered/contained and30% event counts exceed40% counts. |
| S105 | PASS_2_COMPLETE | Omega≥40%/kidney failure44+41=85 matches D margin;HR1.07(.70,1.63),P=.77 compatible;rate/RD direction consistent. |
| S106 | PASS_2_COMPLETE | Omega≥30%/kidney failure/death125+130=255 matches D margin;HR.96(.75,1.23),P=.77 compatible;rates/RD contained/ordered. |
| S107 | PASS_2_COMPLETE | Omega≥30%/kidney failure85+94=179 matches D margin;HR.89(.66,1.19),P=.44 compatible;sourceRD−.4(−1.4,.6) retained. |
| S108 | PASS_2_COMPLETE | Omega≥30% decline81+93=174 matches D margin;HR.86(.64,1.15),P=.31 compatible;3.3−3.9 versusRD−.5 reconciles display ranges. |

## Findings

No new finding meets the independent inclusion threshold in this108-relationship shard. No F-ST2 ID is created. The independently screened existing issues are retained through the complete ledger and are not re-emitted.

## Excluded observations

Every pattern is listed once with exactly one reason code. This table records pass-2 reasoning, not additional screening decisions for previously screened findings.

| Location | Observation | Reason code |
|---|---|---|
| Main p.8 Table2; supplement pp.9–10 eTables4–5 | Rounded one-decimal arm changes need not subtract to the separately rounded modeled contrast; half-unit intervals reconcile apparent0.8/.9 and−.2/−.3 differences. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p.8 Table2; supplement pp.9–14 | Exact CI/P inversion requires unrounded estimates, Rubin degrees of freedom and full test implementation not supplied. A normal diagnostic is not the stated complete analysis. | CONDITIONAL_OR_UNREPORTED |
| Main p.9 Table3 D ACR doubling | PrintedP=.05 andlowerHRlimit1.00 do not contradict nonsignificance understrictP<.05; display intervals permit the null boundary. | ROUNDING_OR_DISPLAY_PRECISION |
| Main p.9 Table3; supplement p.15 eTable10 | Rounded incidence-rate subtraction can yield apparent0.2/.3,−.8/−.7 or−.6/−.5 discrepancies; half-unit input intervals overlap the displayedRD intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| Supplement pp.11–14 and18–19 | Adjusted log-ACR contrasts/forest points are not constrained to equal ratios of rounded printed marginal arm changes or differences of observed geometric means. | MODEL_VERSUS_CRUDE |
| Main pp.8–9 andsupplement pp.18–19 | Forest SD/N-based independent-sample tests would replace the reported adjusted imputed longitudinal model; C004 establishes a count pairing issue, not an exact alternative adjusted test. | MODEL_VERSUS_CRUDE |
| Main p.9 Table3 andsupplement p.15 eTable10 | CoxHR need not equal event-count risks or incidence-rate ratios, particularly with differing person-time; exact variance/test subtype is not supplied. | MODEL_VERSUS_CRUDE |
| Supplement pp.18–19 | Reversed favor arrows and overallP in the interaction column have an immediate numerical reading from explicit active/placebo ratio, endpoint context and overall treatment row; no second competing estimate is supplied. | CONTEXT_RESOLVES |
| Supplement p.18 overallD P=.89 versusp.11 eTable6 P=.90 | This secondary ACR display comparison is not a primary/key-secondary contrast and does not change an analysis population or planned decision rule. It cannot establish a qualifying extraction issue under the comparison tiers. | PERIPHERAL_COMPARISON |
| Supplement pp.9 and12 complete-case tables | Endpoint-complete restriction does not imply intermediate year2/covariate completeness; multiple-imputation footnotes are compatible with the stated restrictions. | CONTEXT_RESOLVES |
| Plan pp.32–33 andmain p.3 | Absent full covariance/imputation/code definitions do not independently demonstrate incompatible methods; existing C001/C002/C003 comparisons remain the explicit source-grounded findings. | CONDITIONAL_OR_UNREPORTED |
| Supplement p.14 eTable9 omega baseline,S040 inventory | Direct sourceupperCI3.7 versus derivative locator3.6 is a transcription matter; the sourcepoint3.3 liesinside2.9–3.7. Coordinator notified to repair locator only. | NOT_REPRODUCED |

## Source links, limits and handoff

REPORT [main methods p.3](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [matched results p.4](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [Table2/Figure3 p.8](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [Table3/Figure4 p.9](../../../jama_de_boer_2019_oi_190122.pdf#page=9); REPORT [eTable4 p.9](../../../joi190122supp2_prod.pdf#page=9), [eTable5 p.10](../../../joi190122supp2_prod.pdf#page=10), [eTable6 p.11](../../../joi190122supp2_prod.pdf#page=11), [eTable7 p.12](../../../joi190122supp2_prod.pdf#page=12), [eTable8 p.13](../../../joi190122supp2_prod.pdf#page=13), [eTable9 p.14](../../../joi190122supp2_prod.pdf#page=14), [eTable10 p.15](../../../joi190122supp2_prod.pdf#page=15), [eFigure2 p.18](../../../joi190122supp2_prod.pdf#page=18), [eFigure3 p.19](../../../joi190122supp2_prod.pdf#page=19); PLAN [implemented analysis p.32](../../../joi190122supp1_prod.pdf#page=32) and[continuation p.33](../../../joi190122supp1_prod.pdf#page=33).

Completed108/108 assignedS records, each explicitlyPASS_2_COMPLETE. New findings0; excluded patterns12. No scientific coverage gap remains within the assigned scope. Exact numerical graphical subgroup endpoints, unrounded model outputs, Rubin degrees of freedom/covariance, Cox test/variance/tie details, individual person-time, blood/urine overlap, planned80% adherence membership, additional amendments and full imputer details are absent. These limits restrict reconstruction without omitting supplied evidence. The coordinator must merge disjoint shardB, mechanically update inventoryPass2 fields from the108 per-ID records, and repair S040's derivative-only locator without changing source or stable candidates.

# Statistical pass 2 — disjoint shard B merge

The following 32-record output is merged without loss from the distinct fresh shard-B agent. Only literal relative-link prefixes are adjusted by one parent level to remain truthful from this canonical checker location. Shard A covers S001 through S108; shard B covers S109 through S140; together every one of the 140 stable relationships is PASS_2_COMPLETE. Combined new findings: 0. Combined excluded observations: 36 (12 in A; 24 in B). No pass-2 inclusion-screener stage is applicable because there are no pass-2 findings.

# Statistical pass 2 — bounded shard B

Runtime agent ID: /root/statistics_pass2_b. Fresh optional statistical pass-2 shard, gpt-6.1-sol/high; start mode FRESH_SPAWN. Assigned and completed scope: S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140. The distinct mandatory pass-2 agent owns S001–S108. This artifact does not edit the inventory; the coordinator merges these explicit completion records.

The complete QUALITY_CONTROL_SCOPE.md and review contract were read, along with the current ledger C001, C002, C003, C004, C005, initial screening table, completed mechanical recheck, complete pass-1 checker, assigned inventory part B, and relevant current source-linked quantitative mappings. Each relationship was revisited for count/denominator, estimate/test, method, cross-source, and recheck implications. Every candidate was considered where it bears on the assigned relationships. No earlier-run candidate, screening, quality or report conclusions, external literature, or web input was used. No new finding count was sought.

## Source authority and tooling

Roles are determined by content: main article and supplementary result tables/figures are REPORT; original prospective protocol and implemented analytic addendum are PLAN. Physical PDF pages identify locations. Direct CPU Poppler pdftotext -layout reread main physical pp.2–4 and 6–10; plan pp.14,17–20,23,31–33; results supplement pp.2–4,9–14,17–19. Current source-linked maps supplied full contextual transcriptions, rather than older scientific decisions. Exact raster graph confirmation used current direct-source renders preprocessing/numeric-supp2-p18.png and preprocessing/numeric-supp2-p19.png; a unique direct CPU Poppler pdftoppm render of source results supplement p.17 was created as preprocessing/st2b-supp2-p17.png using -f 17 -l 17 -singlefile -scale-to 1600 -png. Engine: available direct Poppler 26.01.0. No OCR or fallback capability was needed, and sources/reused assets were preserved. Supplement p.17 printed r values and complete-data caption were visually confirmed. Unprinted graph coordinates were not invented.

Exact source links below are relative to this shard file. Abbreviations in the completion table refer to these authorities:

- REPORT main: [p.2](../../../jama_de_boer_2019_oi_190122.pdf#page=2), [p.3](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.6](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [p.7](../../../jama_de_boer_2019_oi_190122.pdf#page=7), [p.8](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p.9](../../../jama_de_boer_2019_oi_190122.pdf#page=9), [p.10](../../../jama_de_boer_2019_oi_190122.pdf#page=10).
- PLAN protocol/addendum: [p.14](../../../joi190122supp1_prod.pdf#page=14), [p.17](../../../joi190122supp1_prod.pdf#page=17), [p.18](../../../joi190122supp1_prod.pdf#page=18), [p.19](../../../joi190122supp1_prod.pdf#page=19), [p.20](../../../joi190122supp1_prod.pdf#page=20), [p.23](../../../joi190122supp1_prod.pdf#page=23), [p.31](../../../joi190122supp1_prod.pdf#page=31), [p.32](../../../joi190122supp1_prod.pdf#page=32), [p.33](../../../joi190122supp1_prod.pdf#page=33).
- REPORT results supplement: [pp.2–4 laboratory methods, starting p.2](../../../joi190122supp2_prod.pdf#page=2), [p.9](../../../joi190122supp2_prod.pdf#page=9), [p.10](../../../joi190122supp2_prod.pdf#page=10), [p.11](../../../joi190122supp2_prod.pdf#page=11), [p.12](../../../joi190122supp2_prod.pdf#page=12), [p.13](../../../joi190122supp2_prod.pdf#page=13), [p.14](../../../joi190122supp2_prod.pdf#page=14), [p.17](../../../joi190122supp2_prod.pdf#page=17), [p.18](../../../joi190122supp2_prod.pdf#page=18), [p.19](../../../joi190122supp2_prod.pdf#page=19).

## Explicit relationship completion records

| S ID | Pass-2 source-grounded review, screening and recheck implications | Pass 2 |
|---|---|---|
| S109 | REPORT main p.4: vitamin D biomarker 41.4(SD11.0) versus 29.8(SD11.1)ng/mL, P<.001. Positive separation agrees with the narrative. Exact N and test are absent; no independent-sample t test inferred. C001 does not establish a different biomarker N or P. | PASS_2_COMPLETE |
| S110 | REPORT main p.4: omega index 3.6%(SD1.0%) versus 2.3%(SD.8%), P<.001. Positive separation and EPA+DHA/total-fatty-acids definition agree. Exact N/test absent; no statistical incompatibility established. | PASS_2_COMPLETE |
| S111 | REPORT supplement p.17 left: r=−.05, biomarker baseline→2 and eGFR baseline→5; complete-data caption visually confirmed. Main p.4 nonsignificance is not contradicted. Exact N/estimator/test absent; graphical correlation does not establish replacement of the planned association model. | PASS_2_COMPLETE |
| S112 | REPORT supplement p.17 right: r=−.02 with the same time windows and complete-data caption. Omega-index caption and main p.3 definition resolve DHA/EPA axis wording. No invented test or denominator. | PASS_2_COMPLETE |
| S113 | REPORT main p.4: full-population change −12.7(−13.6,−11.7), contained, ordered and declining. C003 supplies an inclusion-definition comparison, without a counterfactual change or any-biosample union N. | PASS_2_COMPLETE |
| S114 | REPORT main p.4/supplement p.9: endpoint-complete N932, overall −12.4(−13.3,−11.4), contained and ordered. Arm totals495+437=470+462=932; Figure1 totals259+236+211+226=932. Difference from the full-population result is population-specific. | PASS_2_COMPLETE |
| S115 | REPORT main p.4/supplement p.11: overall ACR5.1(4.6,5.7) and9.2(8.4,10.1), contained and ordered. Approximately threefold increase agrees with modeled arm ratios2.97/3.02/2.94/3.05. C005 concerns a separate complete-case population. | PASS_2_COMPLETE |
| S116 | PLAN p.14/REPORT main p.2: individual2×2factorial assignment and blocks8; random intercepts address repeated participant measurements. Additional sex/race strata do not establish a changed result or decision rule. No clustering or paired-test contradiction inferred. | PASS_2_COMPLETE |
| S117 | PLAN pp.17,31–32/REPORT main p.2: original ACR0→4 and amended eGFR0→5 distinguished by the implemented2016amendment. Current endpoint/time point agrees; earlier histories do not create an unresolved current endpoint. | PASS_2_COMPLETE |
| S118 | PLAN pp.17,32/REPORT main p.3: current≥40%decline/kidney failure/death follows the addendum; ≥30% and additional composites explicitly post hoc. Questionnaire ascertainment does not prove omission of record confirmation. | PASS_2_COMPLETE |
| S119 | PLAN pp.31–32§15c/REPORT main pp.3–4,6: C003 retained as the already-screened definition comparison. Plan says all follow-up biosample returners are included without only; a minimum-guarantee interpretation remains possible. Reported N1312 confirmed; blood1090/urine1091 do not establish the union or a smaller planned N. | PASS_2_COMPLETE |
| S120 | PLAN p.32/REPORT main p.3: planned10 versus reported20datasets, both combined with Rubin rules. C003 concerns operational inclusion, not proof that increasing M changed estimates. Full imputation definitions absent; no additional incompatibility established. | PASS_2_COMPLETE |
| S121 | PLAN pp.32–33/REPORT main pp.3,8: C002 recheck confirms Equation2 versus routine age/sex/baselineACR and time interactions, with conditional sensitivity wording. Already-screened specification issue retained; no numerical impact or preferred adjustment asserted. | PASS_2_COMPLETE |
| S122 | REPORT main pp.3,8/supplement p.11: categorical time, participant intercept and treatment×time fit repeated measurements; logACR implies geometric ratios. C002 is a specification comparison, not a separate incoherent applied model. C004/C005 do not authorize crude recomputation of adjusted estimates. | PASS_2_COMPLETE |
| S123 | PLAN p.32/REPORT main pp.4,8–9: interaction P=.42>.05 supports the marginal contrasts under the stated rule. Neighboring categorical-time text/Equation2 resolves the missing time-only term in Equation1. C004 does not demonstrate a changed interaction P. | PASS_2_COMPLETE |
| S124 | REPORT main p.3/PLAN pp.18,32: two-sided P<.05 per intervention and current primary inference at year5. P=.25/.27 and CIs crossing0 support no significant difference. Secondary analyses exploratory; no noninferiority/equivalence or alternative multiplicity rule imposed. C005 remains the separate ACR N issue. | PASS_2_COMPLETE |
| S125 | PLAN p.33/REPORT main pp.3,8–9: Wald subgroup interaction families D.58/.36/.15/.18/.79; omega.72/.70/.73/.51; other assignment.42 all>.05. BMI/fish additions disclosed. C004 retained without recalculating adjusted subgroup tests. | PASS_2_COMPLETE |
| S126 | REPORT main pp.9–10: favorable D subgroup points are explicitly qualified because CIs cross0 and interactions are nonsignificant. Hypothesis-generating interpretation agrees with the printed information. C004 does not establish changed adjusted subgroup intervals. | PASS_2_COMPLETE |
| S127 | PLAN pp.19,33/REPORT main pp.3–4/supplement pp.10,13: C001 retains continuous≥80% versus≥2/3 at≥4/6assessments, N1032 per intervention. Different predicates confirmed; individual membership and planned-subset N absent. No duplicate finding. | PASS_2_COMPLETE |
| S128 | REPORT main p.3/supplement pp.9,12: endpoint completeness does not imply year2completeness: eGFR443+389=832<932; ACR449+396=845<944. MI can operate within these sets. C005 independently retains944 versus991 and does not turn residual MI into a contradiction. | PASS_2_COMPLETE |
| S129 | REPORT main p.3/supplement p.14: table title specifies excluding symptomatic visits; main wording ties symptoms to urine-collection time. Immediate context identifies the restricted longitudinal observations. No unsupported whole-person deletion requirement. | PASS_2_COMPLETE |
| S130 | PLAN p.33/REPORT supplement p.17: biomarker-substitution LMM and graphical r summaries need not be competing claims; figure does not state replacement. Exact correlation N/estimator/test absent. Prior exclusion retained. | PASS_2_COMPLETE |
| S131 | PLAN p.33/REPORT main pp.3,6,9/supplement p.15current map: discreteCox/Cox wording alone does not establish a model change. Schoenfeld diagnostics and no significant violations stated. Event times, ties and test subtype not inferred; C005 does not change these event populations. | PASS_2_COMPLETE |
| S132 | PLAN p.19: all12power cells revisited withSD1.59,r=.78 andSD25,r=.834,N1200. Diagnostic residual SEs.05745/.79640 give approximately81/90/96/98/>99/>99%ACR and71/79/85/90/94/96.5%eGFR. Rounded inputs and unspecified exact algorithm accommodate the final97% display; no contradiction established. | PASS_2_COMPLETE |
| S133 | PLAN pp.19–20:1500×.8=1200;×.9=1350;×.7=1050. Diagnostic powers~93%/~86% agree. Separate-combination diagnostics~78.4%ACR/~81.1%eGFR are broadly compatible with80% at rounded20%/3.2effects. Rounded adherence inputs permit21%/3.2dilution statements; the applied predicate comparison remains C001. | PASS_2_COMPLETE |
| S134 | PLAN p.20: joint20–30%incidence is a feasible union of the components. Higher incidence permits detectable RR closer to1;90%power requires larger effects than80%. Graph/text direction agrees. Exact binary power algorithm absent; no chosen alternative algorithm substituted. | PASS_2_COMPLETE |
| S135 | PLAN p.33/REPORT main p.3:80%simulation power at2.3 with2000replications, two-sided alpha.05 and no interaction;1058~80%of1320. Preliminary variance/covariance/missingness inputs absent. C002/C003 retained without guessing their power impact. | PASS_2_COMPLETE |
| S136 | REPORT main pp.3,7–8:0.75/year×5=3.75 exceeds primary upperCI limits2.5/2.6. CI-based exclusion agrees with the numbers; not an equivalence claim. Lack of significance for point.9 can coexist with exclusion of3.75. C002/C003 supply no alternative CIs. | PASS_2_COMPLETE |
| S137 | PLAN p.23: parent Haybittle-Peto z3 gives approximately two-sidedP=.002700. Rule expressly concerns parent cancer/CVD primary endpoints and serves as guidance. No DKD interim result or stopping claim supplied. | PASS_2_COMPLETE |
| S138 | PLAN p.17/REPORT main p.3/supplement pp.2–4: postshift×5.49/5.961 and preshift.006801+1.037603×value connect measurements;QC r=.999 and identity narrative agree. Current referenced CKD-EPI formula is not printed, preventing source-only algebraic comparison with the original177.6formula. | PASS_2_COMPLETE |
| S139 | PLAN pp.17–19/read with implementedp.32: original ACR primary/eGFR secondary and co-primary power heading are superseded by current primaryeGFR. LogACR expβ−1wording supplies no competing printed estimate. No current hierarchy ambiguity. | PASS_2_COMPLETE |
| S140 | REPORT main p.7/supplement pp.18–19: eGFR active−placebo null0 and ACR active/placebo null1 identifiable. ACR favor arrows oppose lower-ACR benefit, but ratio, means and immediate context identify numerical direction at once. C004 remains a separate already-screened count issue, not effect reversal. | PASS_2_COMPLETE |

## Cross-lane reconciliation

C001, C002 and C003 remain the existing protocol_report/P_R definition/specification comparisons relevant to S127, S121–S122 and S119–S120. Recheck states are reproduced; no role or relationship correction is required by this shard. No numerical impact of an alternative population or model is established. C003 must not be described as demonstrating 222 exclusions from an any-biosample population: 222 have no follow-up blood, while the union of blood/urine returners may reach1312. The absence of only leaves the exclusive-population versus minimum-guarantee interpretation for human review.

C004 remains a REPORT count-to-summary alignment issue. Its extraction implications do not authorize reconstructing imputed adjusted subgroup tests from mean/SD/N triplets. C005 remains an internal REPORT exact analysis-N construction issue,944 versus991. It does not imply that MI within endpoint-complete subsets is illogical or demonstrate a different printed effect estimate. All five stable IDs remain Pending Human Adjudication; no candidate is removed or suppressed.

## Findings

No new qualifying finding was emitted. Existing screened observations were not re-emitted. Findings count:0.

## Excluded observations

Repeated patterns are listed once; each row has exactly one reason code. No finding IDs or changes to initial screening are introduced.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.4; supplement p.17 | Exact biomarker or correlation tests require absent N/test/estimator definitions; missingness alone does not establish incompatibility. | CONDITIONAL_OR_UNREPORTED |
| REPORT supplement p.17/main p.3 | DHA/EPA axis wording is resolved by the omega-index caption and EPA+DHA/total-fatty-acids definition. | TERMINOLOGY_OR_WORDING |
| PLAN p.33/REPORT supplement p.17 | Graphical r summaries do not establish omission or replacement of planned biomarker mixed models. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.14/REPORT main p.2 | Extra randomization strata are not shown to change a primary/key-secondary result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN pp.17,31–32/REPORT main pp.2–3 | Earlier endpoint/time histories are resolved by the implemented five-year amendment. | CONTEXT_RESOLVES |
| PLAN p.32/REPORT main p.3 | Questionnaire ascertainment does not demonstrate omission of record confirmation. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.32/REPORT main p.3 | Ten versus twenty imputations does not independently establish a changed extracted effect or decision rule. | CONTEXT_RESOLVES |
| PLAN p.32/REPORT main pp.3–4,6 | Follow-up-biosample definition comparison is already C003, with nonexclusive wording and unknown union retained. | DUPLICATE_OF_INCLUDED |
| PLAN pp.32–33/REPORT main pp.3,8 | Primary covariate comparison is already C002. | DUPLICATE_OF_INCLUDED |
| PLAN pp.19,33/REPORT main p.3/supplement pp.10,13 | Adherence predicate comparison is already C001. | DUPLICATE_OF_INCLUDED |
| REPORT main pp.8–9/supplement pp.18–19 | Count-summary alignment is already C004; adjusted tests are not independently contradicted. | DUPLICATE_OF_INCLUDED |
| REPORT supplement p.12 | Complete-case N944 versus991 is already C005. | DUPLICATE_OF_INCLUDED |
| REPORT main p.3/supplement pp.9,12 | Endpoint-complete restrictions coexist with absent year2data and MI; intermediate Ns show the distinction. | CONTEXT_RESOLVES |
| REPORT main p.3/supplement p.14 | Visit-specific UTI title and collection-time condition identify the intended restriction. | CONTEXT_RESOLVES |
| PLAN p.32Equations1–2 | Neighboring categorical-time text and primary equation resolve the missing time-only term; no applied result conflict established. | NOTATION_OR_TYPOGRAPHY |
| PLAN p.33/REPORT main pp.3,8–9 | Absence of a displayed bioavailable-D subgroup alone does not establish a conflicting existing result. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.33/REPORT main pp.3,6 | DiscreteCox/Cox wording and absent individual PH statistics do not establish incompatible applied models. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.19–20 | Small power/dilution diagnostic differences are compatible with rounded inputs and the unspecified exact algorithm. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN p.33/REPORT main p.3 | 1058as approximately80%of1320 does not establish a changed power rule;1320×.8=1056. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN p.33 | Exact simulation power needs unavailable preliminary variance/covariance/missingness inputs. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.23 | Parent interim guidance does not establish a DKD interim or stopping analysis. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.17/REPORT main p.3 | Current CKD-EPI formula is not printed; citation labels cannot establish an algebraic discrepancy. | CONDITIONAL_OR_UNREPORTED |
| PLAN pp.17–19/current p.32 | Original co-primary power heading does not create two competing current primary endpoints. | CONTEXT_RESOLVES |
| REPORT supplement pp.18–19 | ACR favor arrows conflict with lower-ACR benefit, but explicit ratio and immediate context identify numerical direction. | CONTEXT_RESOLVES |

## Limits and handoff

Every supplied location within the32assigned relationships was revisited; no scientific-coverage gap remains. Unavailable inputs: exact correlation N/test; unrounded outputs; full imputation definitions; Cox event times, ties, test subtype and variance estimator; simulation preliminary variance/covariance/missingness; later amendments; individual adherence; blood/urine union; and several independent assignment-specific subgroup counts. Unprinted graphical coordinates are not invented. These limits constrain reconstruction and interpretation.

Pass: PASS_2_COMPLETE. Relationships:32. New findings:0. Excluded observations:24. Candidate context:C001,C002,C003,C004,C005. Artifact:checkers/parts/statistical_pass_2_b.md. Unique derivative:preprocessing/st2b-supp2-p17.png. Canonical inventory and part B remain untouched for coordinator merge.
