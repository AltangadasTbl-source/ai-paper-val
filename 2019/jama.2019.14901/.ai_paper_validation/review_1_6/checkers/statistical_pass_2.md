# Statistical consistency pass 2 — Workflow 1.6

- Runtime agent ID: /root/statistical_pass_2
- Preset: qc16_statistical_consistency_reviewer
- Model: gpt-6.1-sol
- Reasoning effort: high
- Start mode: FRESH_SPAWN
- Pass: 2, distinct from /root/statistical_pass_1
- Relationship coverage: 137/137 registered S groups, every grouped subcomparison included.
- Sequential scopes: core S001–S043 (43 groups), then results S044–S137 (94 groups); each scope is below120 groups.
- Cross-lane candidate and recheck coverage: C001–C032, all32 records read completely.
- Genuinely new candidate observations: 0.
- Requested classification/evidence-state repairs: 0.
- Status: COMPLETE; every S record has an explicit PASS_2_COMPLETE entry in statistics/relationship_inventory.md.

## Evidence basis and inferential boundaries

Inputs read completely: statistics/relationship_inventory.md, candidate_ledger.md and verification/evidence_recheck.md, the full current source-linked cross-lane ledger and mechanical recheck. Their combined normalized text is below the200000-character context bound. Targeted source matching used the current direct Poppler26.01.0 layout records for the main article and results supplement, plus extraction/support_results_quantitative_evidence.md. The mechanical recheck includes direct-source page/visual confirmation and current source-matched calculations; these checks were not repeated unnecessarily. This pass used no new extraction, OCR, installation, Python calculation, external source, web evidence or legacy review conclusions. Supplied sources and reusable assets are unchanged.

The comparison document roles are assigned by content: main article and non-plan results supplement REPORT; protocol/SAP bundle, including historical trial background, PLAN. The inventory preserves exact links, printed tuples, models, populations and missing definitions for every relationship. The decision table below records the second-pass reasoning rather than copying the complete tuples.

Every displayed effect/interval was revisited for point containment, endpoint ordering, sign, direction, labels and scale. Every repeated result was revisited after population, time, denominator, contrast and inferential-object matching. Counts/proportions were not treated as person-time rates, and Kaplan–Meier risk-table attrition was not treated as event counts. Rounded median and IQR summaries were not treated as sufficient inputs for mean/rank tests, pooled subgroup medians or a difference estimator. Adjusted odds ratios, subgroup risk differences, interactions, and time-to-event log-rank results remain distinct statistical objects.

Interval/P/statistic/SE compatibility was evaluated quantitatively only where compatible supplied definitions and inputs exist. Pearson, likelihood-ratio, continuity-corrected and Fisher calculations recorded in pass1/recheck are conditional diagnostic calculations; their agreement identifies a source-compatible possibility, not the authors' chosen convention. A qualitative agreement between a crossing-zero interval and a non-significant P value does not establish their exact inferential construction. No sidedness, degrees of freedom, covariance, variance estimator, multiplicity adjustment, denominator, model or estimand mapping was supplied from convention alone.

No coherent display-zero P tuple occurs in the registered inventory. The policy remains DISPLAY_ZERO_NOT_CANDIDATE for otherwise compatible finite-precision P=0 displays. Zero event counts and near-unit P displays are not zero-P contradictions. No tiny tail probability or replacement threshold was computed.

## Cross-stratum counts, denominators and composite identities

[REPORT main Table2, PDF p8](../../../jama_thille_2019_oi_190108.pdf#page=8), [REPORT hypercapnic eTable3, PDF p6](../../../joi190108supp2_prod.pdf#page=6) and [REPORT nonhypercapnic eTable4, PDF p7](../../../joi190108supp2_prod.pdf#page=7) are matched by endpoint/time/arm. The denominator partition is HF48+254=302, NIV63+276=339; stratum totals111+530=641. Full-arm denominators are retained for binary outcomes, while mortality among reintubated uses the explicitly printed conditional denominators.

| Matched outcome | HF stratum sum | NIV stratum sum | Main printed counts | Second-pass result |
|---|---|---|---|---|
| Day7 reintubation |10+45=55|5+35=40|55/40|Reconciles|
| Day7 respiratory failure |24+64=88|14+56=70|88/70|Reconciles; C014/C025 concern effect/P displays|
| Reintubation48h |4+32=36|2+22=24|36/24|Reconciles|
| Reintubation72h |9+38=47|4+26=30|47/30|Reconciles|
| ICU reintubation |10+49=59|6+35=41|59/41|Reconciles|
| Criteria met during ICU stay |11+54=65|7+42=49|65/49|Reconciles; criterion cutoff separate|
| ICU deaths |5+21=26|2+19=21|26/21|Reconciles; exact mortality tests still unspecified|
| ICU death or reintubation |11+53=64|6+45=51|64/51|Reconciles|
| ICU deaths among reintubated |4+17=21|2+9=11|21/59 and11/41|Both conditional numerators and denominators reconcile|
| Hospital deaths |7+39=46|8+46=54|46/54|Reconciles|
| Day90 deaths |11+54=65|12+50=62|65/62|Reconciles; C011 contrast and C028 test alignment separate|

Within hypercapnic patients, deaths+reintubations−deaths-among-reintubated reproduce composites: HF5+10−4=11 and NIV2+6−2=6. Within nonhypercapnic patients, HF21+49−17=53 and NIV19+35−9=45. Main totals likewise give HF26+59−21=64 and NIV21+41−11=51. These exact identities do not determine any unavailable covariance, CI construction or test.

[REPORT eTable2, PDF pp3–4](../../../joi190108supp2_prod.pdf#page=3) provides both baseline strata and categorical partitions. All intubation and weaning classes sum to their respective group totals; complementary ventilator/SBT categories reproduce identical P values as expected. Cough and secretion cells use their explicit nonmissing denominators, whose pooled totals corroborate the main article; their complementary percentages are the existing C005–C008 observations. Multiple chronic disease components may overlap under the supplied footnote, so no invalid exclusivity identity is imposed.

## Explicit relationship decisions

The canonical inventory contains PASS_2_COMPLETE plus the corresponding decision in every S row. Each baseline row decision covers both nonhypercapnic and hypercapnic comparisons; each historical group decision covers every printed outcome in that group. Existing-candidate references identify duplicate implications without new IDs, renumbering or suppression.

### Core scope: 43 groups

| S ID | Pass2 state | Second-pass decision and recheck implication |
|---|---|---|
| S001 | PASS_2_COMPLETE | Baseline lung-disease counts sum from both PaCO2 strata; .02 and higher NIV prevalence agree. Exact baseline test variant absent; no new candidate. |
| S002 | PASS_2_COMPLETE | Primary 55/302 versus40/339 recombines S111/S124; group and difference intervals ordered/contained and direction agrees throughout. Figure log-rank kept separate; no new candidate. |
| S003 | PASS_2_COMPLETE | RF 88/302 versus70/339 recombines S112/S125. Existing C014 captures -8.7 versus -8.5; C025 captures .01 versus .02 with compatible different chi-square variants. No added CI contradiction. |
| S004 | PASS_2_COMPLETE | 48-hour 36/302 versus24/339 equals4+32 versus2+22; negative difference/ordered CI/P=.04 compatible. No new candidate. |
| S005 | PASS_2_COMPLETE | 72-hour 47/302 versus30/339 equals9+38 versus4+26; negative difference/ordered CI/.009 compatible. No new candidate. |
| S006 | PASS_2_COMPLETE | ICU reintubation 59 versus41 equals10+49 versus6+35; .009 repeats supplement and may be truncated. Counts are patient risks, with no person-time denominator; no new candidate. |
| S007 | PASS_2_COMPLETE | Existing C015 preserves the percent-heading/day-unit question. .5 is inside ordered CI; estimator cannot be inferred by subtracting displayed medians or subgroup stay summaries. |
| S008 | PASS_2_COMPLETE | Existing C016 preserves hospital-stay contrast-unit question. 2.3 is inside ordered CI; median/IQR summaries do not determine difference estimator or P. |
| S009 | PASS_2_COMPLETE | 26 versus21 equals5+21 versus2+19. Existing C031 remains a conditional standard chi-square diagnostic; statistic, variant, adjustments and actual mortality denominator absent. No new CI inconsistency. |
| S010 | PASS_2_COMPLETE | Hospital deaths46 versus54 equals7+39 versus8+46. Direction positive and CI crosses zero; .80 can be truncation of Pearson .808084. No new candidate. |
| S011 | PASS_2_COMPLETE | Day28 mortality33 versus39, difference .6 and ordered CI agree qualitatively with .82. No subgroup day28 counts or row-specific test supplied; do not invent them. |
| S012 | PASS_2_COMPLETE | Day90 deaths65 versus62 equals11+54 versus12+50. C002 keeps conflicting65/302 percentage displays; C028 record_input_error keeps table/curve test alignment unestablished. No CI/log-rank equivalence assumed. |
| S013 | PASS_2_COMPLETE | Criteria-positive65 versus49 equals11+54 versus7+42. Ordered negative CI/P=.02 coherent; C021 cutoff question may affect definition but does not determine revised counts. |
| S014 | PASS_2_COMPLETE | Composite64 versus51 equals11+53 versus6+45 and death+reintubation-overlap. C013 not_reproduced: one-decimal component rounding gives exactly -6.2; no new candidate. |
| S015 | PASS_2_COMPLETE | Conditional deaths21/59 versus11/41 equal pooled subgroup deaths/conditional denominators, not full302/339. Difference/CI compatible; LR .352735 can explain .35. No new candidate. |
| S016 | PASS_2_COMPLETE | Continuation86/339 versus106/302 reproduces -9.7; ordered negative CI and P<.01 agree. No subgroup continuation cells available; no inferred partition. |
| S017 | PASS_2_COMPLETE | 291-254=37 and positive ordered CI/P<.001 agree. Blood-gas measured n and variance/test/CI construction absent; no reconstruction using treatment header n. |
| S018 | PASS_2_COMPLETE | Rounded21%/19% permits1.2pp with undisplayed precision; ordered crossing-zero CI/P=.72 agrees. Measurement numerators/denominators absent; no new candidate. |
| S019 | PASS_2_COMPLETE | Time-to-reintubation -5 lies within ordered -42 to32; P=.76 and narrative agree. Difference estimand unknown; subtraction of rounded medians is not an applicable identity. |
| S020 | PASS_2_COMPLETE | 39/41 versus57/59 supports -1.5 and96/100 pooled criteria compliance; full-cohort S013 is a different denominator. .99 can reflect near-unit Fisher/Yates display; no new candidate. |
| S021 | PASS_2_COMPLETE | Hypercapnic111=48+63; 10/48 versus5/63 in S111 supports -12.9 and .049. Proportion test kept distinct from Figure3A log-rank; no new candidate. |
| S022 | PASS_2_COMPLETE | Nonhypercapnic530=254+276; S124 repeats -5.0 and CI. Existing C026 remains nearest-rounding question with explicit truncation alternative; Figure3B log-rank .11 is a separate output. |
| S023 | PASS_2_COMPLETE | Interaction .25 and absence-of-interaction narrative agree; subgroup risk-difference/OR arithmetic cannot reconstruct an unspecified interaction model, covariance or statistic. No new candidate. |
| S024 | PASS_2_COMPLETE | Adjusted OR .60 lies between .38/.93, positive ratio scale with protective direction. CI-based Wald approximation is diagnostic only; unadjusted risk differences are different estimands. |
| S025 | PASS_2_COMPLETE | Identical .02 with/without center random effect is possible after display rounding. eTable5 counts are not model coefficients; C017/C018 concern center IQR, not fitted inference. No new candidate. |
| S026 | PASS_2_COMPLETE | Overall reintubation curve .02 agrees directionally with primary count comparison; risk-table losses are not assumed events. Exact log-rank event/censor inputs absent. |
| S027 | PASS_2_COMPLETE | Hypercapnic curve .049 agrees with lower NIV trajectory; identical proportion-test display does not establish the same test. Event/censor data absent; no new candidate. |
| S028 | PASS_2_COMPLETE | Nonhypercapnic curve log-rank .11 need not equal prose proportion .10 or eTable4 .1057. C026 compares prose/table only; no new curve-P contradiction. |
| S029 | PASS_2_COMPLETE | Main methods explicitly separate proportion chi-square from curve log-rank. C025/C031/C032 retain named exact-test limits; C028 common-test assignment is unsupported. C027 endpoint count and C021 threshold stay separate. |
| S030 | PASS_2_COMPLETE | Historical Nava narrative/table n97=48+49, 24% to8%/.027 and direction agree. Original historical test definitions absent; no new candidate. |
| S031 | PASS_2_COMPLETE | All four Ferrer2006 and five Ferrer2009 table outcomes agree with respective significance/direction narratives. Historical methods and exact measurement n absent; no new candidate. |
| S032 | PASS_2_COMPLETE | Existing C022 preserves Su400 versus406 with narrative approximation alternative. Ornico38=20+18 and5%/39%/.016 agree; Su nonsignificant outcomes agree. |
| S033 | PASS_2_COMPLETE | Both Nava reintubation4/48 versus12/49 and ICU deaths3/48 versus9/49 reconcile counts/percentages; .027/.064 align narrative. Historical test not inferred. |
| S034 | PASS_2_COMPLETE | All Ferrer2006 ARF, reintubation, infection and ICU-death counts/denominators/percentage directions checked; .029/.12/NS/.015 narrative coherent. No supplied exact historical test. |
| S035 | PASS_2_COMPLETE | All five Ferrer2009 ARF, reintubation, pneumonia, ICU and day90 death tuples checked; percentage/direction and stated significance coherent. No historical CI/test reconstruction. |
| S036 | PASS_2_COMPLETE | Khilnani5/20 versus3/20 and18.3/16.1-day mean/SD summaries have coherent labels and nonsignificant .44/.34. Original test/variance absent; no new candidate. |
| S037 | PASS_2_COMPLETE | Su failure, reintubation and mortality ratios reconcile within202/204 arms and nonsignificant P labels. C022 alone tracks narrative400 versus406; no new inferential observation. |
| S038 | PASS_2_COMPLETE | Ornico1/20 versus7/18 and0% versus4/18 agree5%/39%/22%; .016/.041 and narrative direction coherent. Zero mortality count is not P=0. |
| S039 | PASS_2_COMPLETE | Historical28% to15%/.03 has coherent direction and significance. Cohort denominators, test, censoring and interval absent; no new candidate solely missing inputs. |
| S040 | PASS_2_COMPLETE | PLAN primary proportion chi-square, predictor t/Mann-Whitney/chi-square/Fisher/logistic rules are separate methods, not fitted outputs. REPORT does not supply every selected variant; no candidate solely missing definitions. |
| S041 | PASS_2_COMPLETE | PLAN logistic OR and Cox hazard-ratio stages are distinct, with .20/.05 selection thresholds. Enrollment-origin plans do not establish the eFigure actual origin; existing C024 labels remain the observed mismatch. |
| S042 | PASS_2_COMPLETE | PLAN mortality Kaplan-Meier/log-rank and Cox stages do not identify main Table2 exact day90 test. Subgroup definitions align threshold>45/<=45; C028 retains unsupported alignment. |
| S043 | PASS_2_COMPLETE | 18%-10%=8pp;590 inflated10%=649 then target650 agrees REPORT/PLAN. Exact sample-size formula/correction absent; no new power reconstruction. |

### Results scope: 94 groups

| S ID | Pass2 state | Second-pass decision and recheck implication |
|---|---|---|
| S044 | PASS_2_COMPLETE | Same88/302 versus70/339 as S003; existing C025: Pearson .012786 rounds .01, Yates .016490 rounds .02. Both standard variants reproduce printed values; exact common convention unresolved. |
| S045 | PASS_2_COMPLETE | RR>25 counts74/302 versus63/339 and .07 agree conditional Pearson. Criteria can overlap; not a component-total identity. No new candidate. |
| S046 | PASS_2_COMPLETE | Distress57/302 versus46/339 and .07 coherent conditional Pearson. Repetition of .07 with S045 is expected finite precision, not evidence of duplicated results. |
| S047 | PASS_2_COMPLETE | Acidosis21/302 versus18/339 and .38 coherent conditional Pearson. Ordinary ARF threshold distinct from C021 severe-reintubation threshold; no new candidate. |
| S048 | PASS_2_COMPLETE | Hypoxemia52/302 versus36/339/.02 compatible standard diagnostics; criteria may overlap, no forced sum to88/70. |
| S049 | PASS_2_COMPLETE | ICU reintubation59/302 versus41/339 and .009 repeat main S006; truncation possible. Summed strata and center-primary count horizon kept distinct. |
| S050 | PASS_2_COMPLETE | Severe respiratory-failure criterion46/302 versus42/339/.30 compatible diagnostics; not limited to actually reintubated59/41 unless source says so. |
| S051 | PASS_2_COMPLETE | RR>35 criterion34/302 versus32/339/.45 compatible conditional Pearson; denominator full cohort retained and overlap allowed. |
| S052 | PASS_2_COMPLETE | Distress criterion39/302 versus37/339/.43 compatible conditional Pearson; no forced exclusive-category total. |
| S053 | PASS_2_COMPLETE | Acidosis criterion12/302 versus9/339/.35 compatible conditional Pearson. Same counts/P as ineffective-cough reason S066 are allowed distinct labels. |
| S054 | PASS_2_COMPLETE | Hypoxemia criterion24/302 versus19/339/.24 compatible conditional Pearson; no new denominator or scale issue. |
| S055 | PASS_2_COMPLETE | Hemodynamic failure10/302 versus6/339/.21 coherent conditional Pearson; reason/criteria cells can overlap and exceed event sum. |
| S056 | PASS_2_COMPLETE | Neurological failure18/302 versus19/339/.85 coherent conditional Pearson; equal rounded6% does not imply identical exact proportions or P=1. |
| S057 | PASS_2_COMPLETE | Arrest7/302 versus3/339/.20 is compatible two-sided Fisher .203196; same counts in S061/.14 can use Pearson. No source-established common variant. |
| S058 | PASS_2_COMPLETE | Cardiogenic edema9/302 versus7/339/.46 coherent conditional Pearson; whole-cohort percentage denominator and count labels preserved. |
| S059 | PASS_2_COMPLETE | Upper-airway obstruction6/302 versus6/339/.84 coherent Pearson .839767; equal counts with unequal denominators need not imply P=1. |
| S060 | PASS_2_COMPLETE | Aspiration1/302 versus2/339/.99 has Fisher/Yates near-unit diagnostic; export/cap convention absent. No independent contradiction from near-unit display. |
| S061 | PASS_2_COMPLETE | Pneumonia7/302 versus3/339/.14 compatible Pearson .143932; S057/.20 has compatible Fisher alternative, no sole duplicate-count candidate. |
| S062 | PASS_2_COMPLETE | Atelectasis9/302 versus4/339/.11 coherent conditional Pearson; denominator is not number reintubated. |
| S063 | PASS_2_COMPLETE | Pleural effusion2/302 versus3/339/.75 coherent conditional Pearson; rounded1% in both arms does not imply P=1. |
| S064 | PASS_2_COMPLETE | Pneumothorax1/302 versus2/339/.99 repeats S060 with compatible near-unit test/display explanation; no new candidate. |
| S065 | PASS_2_COMPLETE | Secretion-clearance reason18/302 versus18/339/.72 coherent conditional Pearson; equal counts differ by denominator. |
| S066 | PASS_2_COMPLETE | Ineffective-cough reason12/302 versus9/339/.35 differs in time/population meaning from baseline S109; no unsupported cross-row event identity. |
| S067 | PASS_2_COMPLETE | Respiratory-muscle weakness15/302 versus9/339/.12 coherent conditional Pearson; rounded percentage precision and test choice preserved. |
| S068 | PASS_2_COMPLETE | Hypoventilation0/302 versus2/339/.50 compatible Fisher .500887; zero event count is not display-zero P. |
| S069 | PASS_2_COMPLETE | Hypercapnic coma4/302 versus1/339/.14 coherent conditional Pearson. Repeated tuple S070 can occur for different reasons; no evidence of exclusivity. |
| S070 | PASS_2_COMPLETE | Septic shock4/302 versus1/339/.14 coherent conditional Pearson and exact repeat S069; distinct reason labels do not require distinct counts/P. |
| S071 | PASS_2_COMPLETE | Cardiogenic shock2/302 versus0/339/.22 compatible Fisher .221582; no zero-P candidate and no imposed Pearson convention. |
| S072 | PASS_2_COMPLETE | Hemorrhage3/302 versus0/339/.07 compatible Pearson .065857; sparse counts do not authorize changing the chosen source test by convention. |
| S073 | PASS_2_COMPLETE | Neurologic event7/302 versus7/339/.83 coherent conditional Pearson; unequal denominators explain non-unit P despite identical numerators. |
| S074 | PASS_2_COMPLETE | Surgery3/302 versus1/339/.26 coherent conditional Pearson; reasons can overlap, no forced sum to59/41. |
| S075 | PASS_2_COMPLETE | Both age strata70/69 and70/67 with SD/year labels checked; rounded summaries and actual measured n/test/variance missing prevent exact P reconstruction. No new candidate. |
| S076 | PASS_2_COMPLETE | Both male-sex ratios167/254 versus190/276 and28/48 versus40/63 checked; sums195/230 match main sex counts, printed P diagnostics coherent. |
| S077 | PASS_2_COMPLETE | Both BMI mean/SD strata28/28 and31/31 checked on kg/m2 scale; equal rounded means permit .8387/.8397. Exact observations/test/variance missing. |
| S078 | PASS_2_COMPLETE | Both SAPSII mean/SD strata56/56 and54/51 checked against points scale/footnote; rounded means and unknown data/test do not determine .9481/.4512. |
| S079 | PASS_2_COMPLETE | All six intubation classes in both strata sum254/276 and48/63 and recombine main classes. Nonhypercapnic .8290 coherent omnibus diagnostic; hypercapnic dash is not a P=0 or missing numeric contradiction. |
| S080 | PASS_2_COMPLETE | Both age>65 ratios188/254 versus199/276 and35/48 versus38/63 checked; counts recombine223/237, P diagnostics coherent. |
| S081 | PASS_2_COMPLETE | Both chronic-cardiac ratios126/254 versus138/276 and19/48 versus23/63 checked; sums145/161 match main. Disease subtypes may overlap under source footnote. |
| S082 | PASS_2_COMPLETE | Both chronic-lung ratios54/254 versus80/276 and33/48 versus46/63 checked; sums87/126 reproduce S001, within-stratum .0409/.6230 coherent. |
| S083 | PASS_2_COMPLETE | Both SOFA mean/SD strata4.3/4.4 and3.6/4.3 checked on points scale0-24; exact n/data/test/variance absent, no inferred P contradiction. |
| S084 | PASS_2_COMPLETE | Both ventilation-duration medians/IQRs5/6 and6/5 ordered on day scale; subgroup medians cannot be pooled by weighted arithmetic. Printed P not reconstructed from IQR. |
| S085 | PASS_2_COMPLETE | Both three-class weaning comparisons checked; category sums and conditional omnibus .5533/.3187 agree. C003/C004 preserve percentage-allocation questions; C001 main corroborates subgroup sums. |
| S086 | PASS_2_COMPLETE | Both assist-control ratios37/254 versus45/276 and5/48 versus4/63 checked; complements S087 and repeated P are expected, not duplicated-result candidates. |
| S087 | PASS_2_COMPLETE | Both pressure-support ratios217/254 versus231/276 and43/48 versus59/63 complete S086 partitions exactly; same .5806/.4367 expected. |
| S088 | PASS_2_COMPLETE | Both pressure-support mean/SD strata9.4/9.2 and10.4/9.9 checked on cmH2O scale; pressure-support subset n may differ from full cohort and exact test/variance absent. |
| S089 | PASS_2_COMPLETE | Both PEEP mean/SD strata5.7/5.8 and5.9/6.0 checked on cmH2O scale; exact measured n/data/test absent. No new candidate from rounded moments. |
| S090 | PASS_2_COMPLETE | Both tidal-volume strata480/480 and409/479 checked on ml scale; .009 direction plausible; no exact t/P reconstruction absent actual n/test/variance. |
| S091 | PASS_2_COMPLETE | Both tidal-volume strata7.9/7.9 and6.7/7.7 checked on ml/kg scale; different normalization from S090 permits different P. No unreported individual weight mapping assumed. |
| S092 | PASS_2_COMPLETE | Both before-SBT respiratory-rate strata22/22 and23/22 checked on breaths/min scale; equal rounded means permit non-unit P. Actual n/data/test absent. |
| S093 | PASS_2_COMPLETE | Both FiO2 strata34/35 and38/37 checked as percent fractions; existing C030 is wording, not numeric gas result. Exact test/n/variance absent. |
| S094 | PASS_2_COMPLETE | Both PaO2:FiO2 strata281/281 and236/247 checked on mmHg scale; mean of ratios need not equal ratio of means. No numeric consequence inferred from C029/C030 wording. |
| S095 | PASS_2_COMPLETE | Both before-SBT pH strata7.45/7.45 and7.43/7.43 checked on pH scale; SD/order coherent. Rounded equality does not determine .6397/.9343. |
| S096 | PASS_2_COMPLETE | Both before-SBT PaCO2 strata37/37 and51/51 checked; C019 record_input_error preserved because measurement partition/actual n unestablished. No variance identity applied to header n as fact. |
| S097 | PASS_2_COMPLETE | Both T-piece ratios161/254 versus172/276 and27/48 versus34/63 checked; exact complements S098 justify repeated .7996/.8108. |
| S098 | PASS_2_COMPLETE | Both low-pressure-support ratios93/254 versus104/276 and21/48 versus29/63 complete S097 partitions. Same P values are expected under complementary coding. |
| S099 | PASS_2_COMPLETE | Both SBT-duration medians60/60 and60/60 have ordered IQRs; equal medians/IQRs need not yield P=1. Individual data/selected rank or mean test absent. |
| S100 | PASS_2_COMPLETE | Both end-SBT systolic-pressure strata135/135 and140/136 checked on mmHg scale; end-SBT measured n differs from pre-SBT and group headers. No inferred t/P contradiction. |
| S101 | PASS_2_COMPLETE | Both end-SBT diastolic-pressure strata66/68 and71/69 checked on mmHg scale; exact measured n/data/test absent. No new candidate. |
| S102 | PASS_2_COMPLETE | Both end-SBT heart-rate strata92/91 and90/96 checked on beats/min scale; exact measured n/data/test absent. Non-significant .3496/.0903 compatible qualitatively. |
| S103 | PASS_2_COMPLETE | Both end-SBT respiratory-rate strata23/23 and24/23 checked on breaths/min scale; rounding and missing n/test permit printed .2576/.4892. |
| S104 | PASS_2_COMPLETE | Both end-SBT saturation strata97/97 and95/95 checked on percent scale; equal rounded means do not imply P=1. Unknown n/data/test prevents exact inference. |
| S105 | PASS_2_COMPLETE | Both end-SBT PaO2 strata89/87 and75/81 checked on mmHg scale; existing C029 expansion wording does not establish wrong gas measurements. Actual n/test/variance absent. |
| S106 | PASS_2_COMPLETE | Both end-SBT pH strata7.46/7.46 and7.42/7.43 checked on pH scale; before-SBT S095 is distinct timepoint. No unreported common observation set assumed. |
| S107 | PASS_2_COMPLETE | Both end-SBT PaCO2 strata37/37 and53/52 checked on mmHg scale; no CI; abbreviated row label inherits table context, exact data/n/test missing. C019 concerns different before-SBT moment. |
| S108 | PASS_2_COMPLETE | Both steroids ratios35/254 versus38/276 and7/48 versus15/63 checked; sums42/53 match main baseline counts. .9970/.2270 conditional diagnostics coherent. |
| S109 | PASS_2_COMPLETE | Both cough comparisons checked with actual239/263 and45/59 denominators. Existing C005/C006 concern complementary percentages69/73, while .1674/.6561 match count-based Pearson diagnostics. No new P candidate. |
| S110 | PASS_2_COMPLETE | Both secretion comparisons checked with actual242/265 and46/61 denominators. C007/C008 concern complementary percentages57/62; .0864/.5465 match exact count diagnostics. No new P candidate. |
| S111 | PASS_2_COMPLETE | Hypercapnic10/48 versus5/63 supports -12.9/.0489 and repeats S021; CI contains estimate and excludes zero in stated direction. Exact CI/test variant absent; no new candidate. |
| S112 | PASS_2_COMPLETE | Hypercapnic24/48 versus14/63 supports -27.8/.0022; with S125 yields88/70. Ordered negative interval/direction compatible; no inferred CI construction. |
| S113 | PASS_2_COMPLETE | Hypercapnic4/48 versus2/63 supports -5.2/.2337; with S126 yields36/24. Ordered crossing-zero interval compatible; no new candidate. |
| S114 | PASS_2_COMPLETE | Hypercapnic9/48 versus4/63 supports -12.4/.0441; with S127 yields47/30. Negative ordered interval compatible; no extrapolation across tests. |
| S115 | PASS_2_COMPLETE | Hypercapnic10/48 versus6/63 supports -11.3/.0928; C009 keeps ordinary-rounding9% question with explicit truncation alternative. Combines with S128 to59/41. |
| S116 | PASS_2_COMPLETE | Hypercapnic11/48 versus7/63 supports -11.8/.0946; with S129 yields criteria65/49. C021 threshold question does not establish changed patient counts. |
| S117 | PASS_2_COMPLETE | Hypercapnic ICU-stay .6 lies in -4.0 to5.2; day scale/median IQRs ordered. Equal medians13/13 do not force contrast0; exact estimator/test/variance absent. |
| S118 | PASS_2_COMPLETE | Hypercapnic hospital-stay2.5 lies in -4.9 to9.9; day scale ordered. Displayed26-24 is not necessarily the supplied contrast estimator; exact inferential definition absent. |
| S119 | PASS_2_COMPLETE | Hypercapnic5/48 versus2/63 supports -7.2/.1199; combines with S132 to26/21. Ordered crossing-zero CI coherent, no new candidate. |
| S120 | PASS_2_COMPLETE | Hypercapnic composite11/48 versus6/63 supports -13.4/.0523 and death+reintubation-overlap identities. C010 percentage9% question bounded by truncation alternative. |
| S121 | PASS_2_COMPLETE | Hypercapnic conditional4/10 versus2/6 supports -6.7 and composite overlap; .9999 compatible near-unit Fisher/Yates/export convention. Full48/63 denominators not substituted. |
| S122 | PASS_2_COMPLETE | Hypercapnic7/48 versus8/63 supports -1.9/.7735; with S135 sums hospital deaths46/54. Ordered crossing-zero CI and direction coherent. |
| S123 | PASS_2_COMPLETE | Hypercapnic11/48 versus12/63 supports -3.9/.6183; combines with S136 to65/62. CI/order/sign coherent; no event-time test inferred from risks. |
| S124 | PASS_2_COMPLETE | Nonhypercapnic45/254 versus35/276 supports -5.0/.1057 and repeats S022. C026 retains nearest-rounding question plus reproducible prose truncation alternative. |
| S125 | PASS_2_COMPLETE | Nonhypercapnic64/254 versus56/276 supports -4.9/.1775 and combines with S112 to88/70. No new CI/test/denominator issue. |
| S126 | PASS_2_COMPLETE | Nonhypercapnic32/254 versus22/276 supports -4.6/.0785; with S113 matches36/24. Ordered crossing-zero CI compatible. |
| S127 | PASS_2_COMPLETE | Nonhypercapnic38/254 versus26/276 supports -5.5/.0505. Upper CI0.0 may represent positive endpoint rounded to one decimal; no significance-boundary contradiction. |
| S128 | PASS_2_COMPLETE | Nonhypercapnic49/254 versus35/276 supports -6.6/.0374; with S115 equals59/41. Ordered negative CI/direction compatible. |
| S129 | PASS_2_COMPLETE | Nonhypercapnic54/254 versus42/276 supports -6.0/.0712; with S116 equals65/49. Count-positive criteria population distinct from actual reintubated. |
| S130 | PASS_2_COMPLETE | Nonhypercapnic ICU-stay .5 lies in -1.8 to2.8; IQR/day labels coherent. P=.4087 need not match main .55 because subgroup/whole-cohort differ; estimator/test absent. |
| S131 | PASS_2_COMPLETE | Nonhypercapnic hospital-stay2.0 lies in -2.2 to6.2; IQR/day labels coherent. P=.4181 not pooled to main .31; estimand/test/variance absent. |
| S132 | PASS_2_COMPLETE | Nonhypercapnic21/254 versus19/276 sums to main deaths26/21 with S119. Existing C032 remains conditional standard-test mismatch .5548 versus Pearson .546885; exact variant/adjustment/n unavailable. |
| S133 | PASS_2_COMPLETE | Nonhypercapnic composite53/254 versus45/276 supports -4.6/.1766 and overlap identities; with S120 yields64/51. No new inferential candidate. |
| S134 | PASS_2_COMPLETE | Nonhypercapnic conditional17/49 versus9/35 supplies composite overlap and pooled21/59 versus11/41. C012 retains -8.9 ordinary-rounding question with explicit truncation alternative; P=.3801 compatible. |
| S135 | PASS_2_COMPLETE | Nonhypercapnic39/254 versus46/276 supports positive1.3/.6808; with S122 yields46/54. Hospital mortality direction can differ from ICU/day90; no forced sign agreement across different horizons. |
| S136 | PASS_2_COMPLETE | Nonhypercapnic54/254 versus50/276 gives -3.143900pp; C011 retains printed -3.8 discrepancy under unadjusted absolute-difference interpretation. .3626 matches Pearson and CI/order/containment remain coherent. |
| S137 | PASS_2_COMPLETE | Existing C024 preserves extubation-title/intubation-axis mismatch. C028 record_input_error preserves unestablished common table/curve test/origin. Risk losses cannot establish events; .37 log-rank not reconstructed. |

## Complete cross-lane candidate implications

The complete ledger/recheck was considered, including candidates without a primary S identifier. This table documents all32 existing candidates; it adds no candidate and proposes no current classification or evidence-state change.

| Existing stable ID | Implication considered in this pass |
|---|---|
| C001 | Main weaning category sums reproduce; integer allocation can explain percentage. Existing conditional rounding question; no statistical P consequence established. |
| C002 | S012/S013 share65/302 but print21%/22%; preserve direct display difference separately from C028 test-alignment issue. |
| C003 | S085 nonhypercapnic HF class total and omnibus P reconcile; integer category-balancing alternative retained. |
| C004 | S085 nonhypercapnic NIV class total and omnibus P reconcile; exact percentage-allocation rule absent. |
| C005 | S109 hypercapnic HF percentage follows complement; count-based P is coherent. |
| C006 | S109 hypercapnic NIV percentage follows complement; count-based P is coherent. |
| C007 | S110 hypercapnic HF percentage follows complement; count-based P is coherent. |
| C008 | S110 hypercapnic NIV percentage follows complement; count-based P is coherent. |
| C009 | S115 count contrast/P/CI reconcile;9% remains conditional on unknown rounding, with truncation reproduced. |
| C010 | S120 composite contrast/P/CI and overlap reconcile;9% remains conditional on unknown rounding. |
| C011 | S136 printed effect cannot be obtained by ordinary unadjusted difference, one-decimal component rounding, or truncation; actual alternative estimand undefined. P/CI are not independently challenged. |
| C012 | S134 precise difference rounds -9.0; -8.9 admits truncation. Preserve the named precision convention question without asserting changed significance. |
| C013 | S014 two-stage component rounding explicitly reproduces -6.2. Preserve not_reproduced; no ID removal and no new residual contradiction. |
| C014 | S003 matched main respiratory-failure effects differ with identical CI/P; count arithmetic supports the table value. Existing direct observation. |
| C015 | S007 day-scale row and percentage contrast heading require unit clarification; no requirement that contrast equal rounded-median subtraction. |
| C016 | S008 same unit question applied to distinct hospital row; estimator and normalization absent. |
| C017 | S025 center-random-effect paragraph does not reconcile the descriptive HF IQR; complete center denominator vector supports existing observation. No fitted model inferred. |
| C018 | S025 center-model paragraph does not reconcile descriptive NIV IQR; existing matched-vector observation stays distinct from C017. |
| C019 | S096 both strata read; actual measured-n and same-observation partition unestablished. Preserve record_input_error and do not turn a header-n variance diagnostic into a fact. |
| C020 | PLAN duration arithmetic may include omitted3-month follow-up; no impact on actual analysis time or outcomes inferred. Existing P_P comparison. |
| C021 | S013/S029/S116/S129 criterion counts have differing supplied threshold definitions; no alternative event counts or P values can be derived from cutoffs alone. |
| C022 | S032/S037400 versus406 is PLAN background content; rounding to two significant figures plausible. Existing P_P, historical P tuples remain coherent. |
| C023 | PLAN readiness text/worksheet differ with optional local-procedure framing; no actual subgroup membership change inferred. |
| C024 | S137 title/axis conflict directly retained; actual origin not established by the labels. Distinct from C028 alignment limitation. |
| C025 | S003/S044 matched printed P values differ; Pearson and Yates each reproduce one side. Exact common convention absent, so evidence remains a conditional reporting-label/test question. |
| C026 | S022/S124 nearest-rounding bins are disjoint, but truncation reproduces prose .10. Figure log-rank .11 is a different inferential object. |
| C027 | S029/S040-S043 methods and endpoint counting do not provide amendment removing the additional14-day endpoint. Existing concrete count/label comparison, no motive inference. |
| C028 | S012/S029/S137 fixed-time table and curve log-rank equality is unsupported; preserve record_input_error. No exact event/censor/origin inputs permit alignment. |
| C029 | Gas-name expansion comparison is label evidence; S094/S105 numeric means are not thereby disproven. Roles remain PLAN/REPORT. |
| C030 | Fraction expansion comparison is label evidence; S093 numeric oxygen fraction is not thereby disproven. Roles remain PLAN/REPORT. |
| C031 | S009 standard unadjusted diagnostic differs; exact chi-square variant/statistic, any stratification/adjustment and row-specific n missing. Conditional evidence retained without asserting inferential failure. |
| C032 | S132 standard unadjusted diagnostic differs; exact subgroup test/statistic/adjustment/n missing. Main method family corroborates only; primary relationship remains S_W. |

## Missing definitions and completion

The remaining limits are inputs/definitions rather than source coverage: row-specific measured n and identical observation sets for continuous measurements; continuous contrast estimators and any normalizations; exact mean/rank test selection, variance and CI construction; chi-square correction, stratification, adjustment, statistic and actual mortality denominators for C031/C032; test/correction identity across C025 locations; rounding/allocation/truncation conventions for precision observations; interaction statistic/model/covariance; fitted center-model coefficients/SEs; and actual event times, censoring and time origin for survival curves. No unavailable definition alone created a candidate.

C013 remains not_reproduced because a coherent two-stage rounding calculation reproduces the printed contrast. C019 and C028 remain record_input_error because the required measurement-partition and common-test/origin assignments are unsupported. The other29 existing evidence states remain recorded_candidate, including the explicitly conditional C025/C026/C031/C032 observations. These are evidence-record distinctions, not adjudications; no candidate is deleted, no severity/validity/acceptance/final correction is assigned, and every stable ID remains Pending Human Adjudication.

Pass2 is complete for137/137 S groups and all grouped subcomparisons, after two disjoint sequential scopes. All32 stable candidate/recheck implications were considered. Zero genuinely new candidate observations; zero classification or evidence-state repair requests; no coverage gaps. The complete S set, rather than a candidate count, determined completion.

