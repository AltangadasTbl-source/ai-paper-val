# Statistical pass 2 — REPORT shard

Runtime agent: `/root/statistical_pass_2`; model gpt-6.1-sol; effort high; FRESH_SPAWN. This agent differs from both pass-1 agents. Exact scope: S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027, S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067, S068, S069, S070, S071, S072, S073, S074, S075, S076, S077, S078, S079, S080, S081, S082, S083, S084, S085, S086, S087, S088, S089, S090, S091, S092, S093, S094, S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105. PLAN S records belong to a separate fresh pass-2 agent.

Read QUALITY_CONTROL_SCOPE.md and the complete 1.6.2 review contract; the 105-row REPORT inventory; all 21 current ledger classifications and their unique recheck facts; all 34 initial screening decisions; and all 44 excluded-observation rows from the numeric, cross-source, REPORT statistical and PLAN statistical checkers. Duplicate historical transcriptions in the current ledger were not replayed. The complete mechanical recheck, including C003's Route B method specification and C011's 24 supporting signs/three exceptions, is used without deleting or suppressing any stable ID. Direct current-source Poppler 25.03.0 layout reads confirm main pp.3–8 and results supplement pp.5,10–17. Existing current-run exact-source main-p5 render was visually read, particularly all Figure 2 alignments. CPU. No web, external literature, source changes or old-run conclusions.

All per-ID records below reconcile counts/denominators, estimate/test logic, methods, cross-source and recheck implications as applicable. A posterior probability is not converted into a frequentist P value. Missing outcome-specific n, paired weights, degrees of freedom and posterior draws are named limitations rather than assumed methods. No noninferiority/equivalence relationship is supplied. Existing screened findings are not re-emitted.

## New finding

### F-ST2-001

**Title:** Two Table 2 baseline total means do not reproduce the displayed genotype-group aggregation.

**Exact locations and document roles:** REPORT [main Table 2 baseline fifth handgrip, fifth transient paresis and comparator stiffness p.7](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=7); REPORT [Table 2 footnotes a/b, genotype n=16/11 and visit-1 baseline definition p.8](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=8); REPORT [Numbers Analyzed and available-data statement p.4](../../../../jama_stunnenberg_2018_oi_180136.pdf#page=4). Every location belongs to the published report. No PLAN comparison is needed.

**Printed values:** Total Table 2 N=27; genotype n=16 CLCN1 and n=11 SCN4A. Baseline fifth-handgrip mean: total 1.36 seconds, CLCN1 .93, SCN4A 2.59. Baseline fifth transient-paresis mean: total 20.30%, CLCN1 24.35%, SCN4A 9.12%. Comparator baseline stiffness: total 5.65, CLCN1 6.45, SCN4A 4.34. Non-IVR baseline measurements are explicitly from visit 1, start of the first treatment period; these baseline values are not the adjusted treatment-effect estimates.

**Rule and calculation:** For a total formed from two disjoint genotype groups, the aggregate mean is (nC×meanC+nS×meanS)/N. This calculation gives stiffness 5.590370, which reconciles with 5.65 under full display precision. It gives fifth-handgrip 1.606296 and fifth transient paresis 18.145185, each distinct from the printed total. The same-display reproducing method is used to locate the unavailable denominator/weight mapping rather than impose a preferred analysis.

Allow every displayed count its continuous half-unit interval: nC=[15.5,16.5], nS=[10.5,11.5], N=[26.5,27.5]; allow every displayed mean ±.005. Even using independently varying counts, a conservative interval wider than enforcing nC+nS=N, yields:

| Baseline row | Recomputed mean interval | Printed total interval | Interval gap | Relative gap |
|---|---|---|---:|---:|
| Fifth handgrip | [1.508363636,1.708301887] | [1.355,1.365] | .143363636 | .105414439 |
| Fifth transient paresis | [17.202000000,19.124339623] | [20.295,20.305] | 1.170660377 | .057667999 |
| Comparator stiffness | [5.287818182,5.904716981] | [5.645,5.655] | 0 | 0 |

Each affected row exceeds the relative .05 criterion even with conservative full-input precision. Aggregate mean transient paresis was also checked but is excluded below because its conservative interval gap is within .05. Integer-only count arithmetic was not substituted for the normative continuous display rule.

**Focus area:** C, statistical method logic and reported estimate aggregation.

**Proposed review domain:** statistical_results. **Provisional relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 4.

**Affected result or extracted value:** The baseline fifth-handgrip total mean of 1.36 seconds and fifth transient-paresis total mean of 20.30%, including the total versus genotype population/weight interpretation a data extractor attaches to those values. These are within-display aggregation relationships, not peripheral copies across baseline tables.

**Why context does not resolve it:** Category 4 applies: the aggregate mean identity reproduces another baseline row of the same display but does not reproduce these two rows after full display precision. The source does not provide outcome-specific baseline denominators or weights explaining which total and subgroup observations were summarized. The all-available-data statement identifies a possible mechanism but does not identify those baseline subsets. The printed Table 2 treatment-effect methods do not describe these baseline means as adjusted model estimates.

**Source-grounded alternatives and exact missing definitions:** Different available-case baseline subsets or weights may underlie the total and genotype summaries; reported missing outcome assessments make such subsets possible. The subgroup n=16/11 may indicate nominal trial group sizes rather than each row's actual baseline denominators. The reported 31 treatment sets do not themselves establish baseline replication because footnote b identifies only visit 1. Outcome-specific baseline n, total-versus-subgroup sample membership, weighting, and exact summary mapping are unavailable. No participant data are reconstructed and no consequence for a treatment effect is asserted.

**Exact human question:** Which baseline observations, denominators and weights produced the total and genotype means for fifth handgrip and fifth transient paresis, and how do those mappings reconcile the two printed total means with the displayed n=16/11 groups?

## Explicit pass-2 relationship records

The source locations and full printed values remain in the corresponding S row of `statistics/parts/report_relationship_inventory.md`; each row below is an individual pass-2 reasoning record, not a group completion assertion. Candidate references incorporate the final mechanical facts and current classification. All retained candidates remain Pending Human Adjudication.

| S ID | Pass-2 count/estimate/test/method/cross-source/recheck reconciliation | Status |
|---|---|---|
| S001 | .75/3.85=19.48% and .75/1.75=.4286 reproduce the reported clinical threshold/effect-size conversion; distinct plan SD does not imply a changed clinical margin. | PASS_2_COMPLETE |
| S002 | Strict individual >80/<20 advice is retained; rounded 80 is not an exact boundary event. Clinical patient11 override does not satisfy the numerical rule, already C007. PLAN interim-prior questions are C021, not a new realized-decision finding. | PASS_2_COMPLETE |
| S003 | N=27=16+11; all-available completed-period analysis and hierarchical arm means are coherent as reported. Planned primary priors and withdrawal eligibility remain C002/C005; no raw posterior rerun or assumed covariance. | PASS_2_COMPLETE |
| S004 | 685/1000=68.5%→69%; 1.29−1.75=−.46. The post hoc simulation estimand differs from prospective expected posterior probability; incomplete generation inputs prevent exact rerun without a conflicting arithmetic result. | PASS_2_COMPLETE |
| S005 | Explicit mixed model, variance components and P<.10 covariate selection remain coherent. Order .85/period .22 exceed retention threshold; planned interactions are separately C006. Inferential df is unavailable. | PASS_2_COMPLETE |
| S006 | Dependent tests match within-patient crossover structure. Actual paired n/weights and subgroup model mapping are unavailable; C015 records same-display identity gaps, not an assertion that all available cases are identical. C003 retains method comparison, not formal-status change. | PASS_2_COMPLETE |
| S007 | Two-sided P<.05 and unadjusted exploratory interpretation are explicit. No formal secondary-label change is asserted; C003 now Route B for the actual analysis specification. No multiplicity preference proposed. | PASS_2_COMPLETE |
| S008 | Mean ages are inside ordered ranges; unreported rank data prevent P=.09 reconstruction. No changed group size or matched-estimate conflict is established. | PASS_2_COMPLETE |
| S009 | 13/16 and7/11 reproduce percentages; exact binary rank-tail .391304 reproduces .39 and serves as a C009 same-display comparator. | PASS_2_COMPLETE |
| S010 | 2/16 and0/11 reproduce percentages; binary exact rank-tail .498575 reproduces .50 and corroborates C009 comparator method. | PASS_2_COMPLETE |
| S011 | Percentages reconcile under half units; C009 remains reproduced because the binary method matching adjacent rows yields1 rather than .62. Alternative tested categories/coding remain the human question. | PASS_2_COMPLETE |
| S012 | Stiffness median/IQR ordered; direction and P=.002 agree. Rank P cannot be inferred from median difference alone; no additional mismatch. | PASS_2_COMPLETE |
| S013 | Pain median/IQR ordered; SCN4A higher and P=.002 agree. Zero absence is contextually defined, not a changed scale-direction finding. | PASS_2_COMPLETE |
| S014 | Weakness median/IQR ordered; P=.06 is nonsignificant. Quartile overlap does not determine a rank-test P. | PASS_2_COMPLETE |
| S015 | Tiredness median/IQR ordered; P=.16 does not conflict with an inferential interval because none is supplied. | PASS_2_COMPLETE |
| S016 | Handgrip medians/IQRs ordered; P=.40 not mechanically recoverable from summaries. Measurement-duration comparison already C004. | PASS_2_COMPLETE |
| S017 | Eyelid medians/IQRs ordered and higher SCN4A/P=.01 agree. Measurement-duration comparison already C004. | PASS_2_COMPLETE |
| S018 | Timed Up&Go medians/IQRs ordered; P=.49 has no summary-based contradiction. It is not called prespecified, so its addition alone is not Route A5. | PASS_2_COMPLETE |
| S019 | Median/IQR order holds; upper quartiles exceed the stated0–100 range under full precision, already C008. Scoring formula remains missing; P=.82 is not rerun from quartiles. | PASS_2_COMPLETE |
| S020 | SF-36 physical median/IQR order and0–100 range hold; P=.11 needs underlying ranks. No comparison with a different baseline population is forced. | PASS_2_COMPLETE |
| S021 | SF-36 mental median/IQR order/range hold; P=.88 not contradicted by summaries. Treatment inference is separately S069/C013. | PASS_2_COMPLETE |
| S022 | Overall Bayesian3.06 lies inside1.96–4.15 and equals5.56−2.50; N27 matches analyzed flow.100% is rounded posterior area; current frequentist3.12 belongs to another analysis. C002/C005 specify unresolved prospective mapping. | PASS_2_COMPLETE |
| S023 | CLCN1 Bayesian3.84 within2.52–5.16; 100% posterior area compatible. Figure coordinates have uncertainty and reproduce within scope precision; N16 is analyzed population. C002 remains the prior comparison. | PASS_2_COMPLETE |
| S024 | SCN4A1.94 within.35–3.53; 93% above.75 can coexist with95% CrI crossing.75. A posterior tail is not a frequentist P. N11 matches analyzed group. | PASS_2_COMPLETE |
| S025 | Pain.68 contained in−.52–1.89 and clinical posterior45% is below50%, matching narrative. Frequentist.70/CI/P is a separate labeled analysis; C003 concerns specifications. | PASS_2_COMPLETE |
| S026 | Weakness1.48 contained in.18–2.77; 87% above.75 is qualitatively coherent. Frequentist1.56 is an adjusted separate estimate, not forced to the Bayesian mean. | PASS_2_COMPLETE |
| S027 | Tiredness1.23 contained in−.23–2.67; 74% above.75 is coherent. Frequentist1.27 and different CI belong to another analysis. | PASS_2_COMPLETE |
| S028 | First11 cumulative-patient claim is distinct from individual responder count. Caption ID pointer lacks changed printed posterior value; peripheral exclusion retained. No sequential raw data assumed. | PASS_2_COMPLETE |
| S029 | OrderP=.85/periodP=.22 exceed.05/.10. They do not identify treatment interactions without explicit term mapping; already C006. | PASS_2_COMPLETE |
| S030 | Present3.12 and quoted prior2.69 are contained in positive intervals; interval overlap supports descriptive consistency, without an invented equivalence test. | PASS_2_COMPLETE |
| S031 | Patient13 source mean−.05/CrI−.56–.45/2% retained; Figure marker/whisker nearzero is not an exact0–0 interval. Ordered/contained and below20; no new inference mismatch. | PASS_2_COMPLETE |
| S032 | Patient11 zero observed effect and wide prior CrI−12.24–12.16/38% are expressly explained. Invisible plotted whisker is not exact zero CI. Numerical-rule attribution is already C007. | PASS_2_COMPLETE |
| S033 | Patient22.01/CrI−.56–.57/1% gives contained nearzero effect and below20; graphical coordinates and genotype align. C007 distinguishes this numerical nonresponse from patient11. | PASS_2_COMPLETE |
| S034 | Patient4 open marker identifies two sets; 1.1/.27–1.90/81% are ordered, contained and consistent with >80 advice. N/set count reconciles without substituting a frequentist P. | PASS_2_COMPLETE |
| S035 | Patient20 1.13/.14–2.13/rounded80%; half-unit probability permits >80. Graph ordered/contained; no exact boundary decision supplied. | PASS_2_COMPLETE |
| S036 | Patient8 1.2/−.03–2.41/rounded80%; threshold.75 and rounded probability can reconcile. A CrI crossing.75 is not a frequentist significance conflict. | PASS_2_COMPLETE |
| S037 | Patient25 1.65/1.27–2.03/100%; graph alignment and CLCN1 agree, effect inside interval and above threshold. No P=0 inference. | PASS_2_COMPLETE |
| S038 | Patient18 2.55/1.77–3.32/100%; graph approximate2.6 and CrI support same positive effect under display uncertainty. | PASS_2_COMPLETE |
| S039 | Patient19 2.63/1.18–4.01/99%; interval contains estimate, graph/genotype agree and mass above.75 is compatible. | PASS_2_COMPLETE |
| S040 | Patient24 2.64/2.16–3.12/100%; graphical point and interval ordering agree at visual precision, CLCN1 and one set match source. | PASS_2_COMPLETE |
| S041 | Patient12 2.66/1.76–3.56/100%; effect contained, positive clinical posterior and SCN4A graph identity agree. | PASS_2_COMPLETE |
| S042 | Patient15 2.7/2.16–3.24/100%; estimate contained, CLCN1 identity and graph agree within coordinate uncertainty. | PASS_2_COMPLETE |
| S043 | Patient2 3.1/2.63–3.49/100%; open marker/two sets agree. Pass1 approximate lower endpoint2.8 is superseded by exact table locator2.63; no reproduced above-threshold endpoint conflict asserted. | PASS_2_COMPLETE |
| S044 | Patient27 3.14/2.46–3.83/100%; graph and table agree at visual precision; contained ordered interval and CLCN1 identity. | PASS_2_COMPLETE |
| S045 | Patient9 3.2/2.78–3.56/100%; graph/table match, contained estimate and SCN4A identity; graphical endpoint approximations are not exact copies. | PASS_2_COMPLETE |
| S046 | Patient17 3.22/2.94–3.50/100%; graph/table match and ordered containment; CLCN1 identity and one set agree. | PASS_2_COMPLETE |
| S047 | Patient14 3.5/2.81–4.19/100%; graph/table match and ordered containment; graphical uncertainty prevents treating tick estimates as exact numbers. | PASS_2_COMPLETE |
| S048 | Patient30 3.57/2.91–4.23/100%; graph/table agree at visual precision, CLCN1 and positive benefit direction match. | PASS_2_COMPLETE |
| S049 | Patient10 3.7/2.28–5.04/100%; long whisker ordered/contained. Label is below whisker and does not denote a different point estimate. | PASS_2_COMPLETE |
| S050 | Patient1 4.4/4.03–4.85/100%; open marker/two sets and genotype match; graph/interval contain point. | PASS_2_COMPLETE |
| S051 | Patient21 actual whisker approximately3.8–5.0 agrees with table3.80–5.0 and point4.41. InitialF-ST1-011 NOT_REPRODUCED is upheld; historical3.3–5.5 locator superseded, no re-emission. | PASS_2_COMPLETE |
| S052 | Patient16 4.49/3.96–5.03/100%; graph/table align, interval ordered/contained and CLCN1 match. | PASS_2_COMPLETE |
| S053 | Patient28 4.50/4.0–4.99/100%; graph/table align; printed interval precision differs but not its interpretation. | PASS_2_COMPLETE |
| S054 | Patient26 4.65/4.07–5.21/100%; graph/table align at visual precision; positive threshold direction and genotype match. | PASS_2_COMPLETE |
| S055 | Patient5 4.7/4.50–4.87/100%; open marker/two sets match. Pass1 approximate4.5–4.9 remains compatible with exact table endpoints. | PASS_2_COMPLETE |
| S056 | Patient23 exact5.49/4.98–6.04/100%; approximate graph5.5–5.6 cannot establish above-threshold difference. Ordered/contained and CLCN1 match. | PASS_2_COMPLETE |
| S057 | Patient29 6.99/6.59–7.41/100%; graph/table align, contained estimate, CLCN1 and one-set count match. | PASS_2_COMPLETE |
| S058 | Group densities reflect27/16/11 and threshold.75; positive group effects and posterior probabilities match narrative. No exact peak/density or draw reconstruction invented. | PASS_2_COMPLETE |
| S059 | Complementary cumulative curves decrease with threshold; .75/3.85≈20%,2/3.85≈52%,standardized.43/1.14 reconcile. No inferential P supplied. | PASS_2_COMPLETE |
| S060 | Terminal counts27/16/11 agree; SCN4A visual87–89% versus text92.5–93.5% leaves3.5/93=.0376, screened precision. Cumulative nonmonotonicity is not a logical contradiction. | PASS_2_COMPLETE |
| S061 | Mixed stiffness3.12 within2.46–3.78/P<.001 and repeated abstract match; crude3.13 not required. Baseline genotype aggregation5.59037 versus5.65 overlaps full precision and is comparator forF-ST2-001. | PASS_2_COMPLETE |
| S062 | Mixed CLCN1 stiffness3.82 within3.10–4.54/P<.001; adjusted model not forced to equal6.46−2.60. Baseline6.45 contributesF-ST2-001 comparator. | PASS_2_COMPLETE |
| S063 | Mixed SCN4A1.89 within1.01–2.76/P=.002; null classification agrees and df not inferred. Baseline4.34 contributesF-ST2-001 comparator. | PASS_2_COMPLETE |
| S064 | Genotype interaction.004 is distinct from within-group P; no covariance/test statistic for rerun. Direction favors CLCN1 as narrative. | PASS_2_COMPLETE |
| S065 | Mixed pain.70/.18–1.23/P=.01 is contained and significant; Bayesian.68 is different labeled analysis. | PASS_2_COMPLETE |
| S066 | Mixed weakness1.56/1.05–2.06/P<.001 is coherent at null threshold; crude1.47 comparison remains MODEL_VERSUS_CRUDE. | PASS_2_COMPLETE |
| S067 | Mixed tiredness1.27/.58–1.95/P=.001 is contained/significant; no unreported df inferred and Bayesian contrast distinguished. | PASS_2_COMPLETE |
| S068 | SF-36 physical effect7.81/4.72–10.88/P<.001 is contained/positive. C011 orientation retained; C012 period midpoint1.18 versus1.04 has relative.125. Effect7.81 versus7.62 screens under precision. | PASS_2_COMPLETE |
| S069 | Mental6.78/1.64–11.92/P=.001 is retained C013 interval/test discrepancy with df26 diagnosticP=.0117149 and exact df unavailable. C011 orientation; mex period midpoint4.575 versus4.77 gap.03983 screens precision. | PASS_2_COMPLETE |
| S070 | INQoL−14.22/−24.71–−3.74/P=.01 is contained/significant; paired diagnostic.00979 coherent. M−P−14.22 matches; C011 identifies reference header reversal, not a second magnitude finding. | PASS_2_COMPLETE |
| S071 | First-handgrip placebo+.46 outside descending−.30 to−1.23 remains C014; effect−2.85/negative CI/P=.02 coherent. C011 orientation supported. | PASS_2_COMPLETE |
| S072 | Fifth-handgrip total−.97/−2.03–.09/P=.07 crosses null/nonsignificant; period difference matches. C011 sign supported. Its baseline1.36 joinsF-ST2-001 using subgroup baselines. | PASS_2_COMPLETE |
| S073 | Fifth-handgrip CLCN1+.04/−1.11–1.19/P=.95 coherent at null; period mean discrepancy C015. It is a C011 same-sign exception, not a reversal. Baseline.93 contributesF-ST2-001. | PASS_2_COMPLETE |
| S074 | Fifth-handgrip SCN4A−1.96/−3.41–+.51/P=.009 conflict remainsC016; repeated narrative retained and interaction.04 not substituted. Baseline2.59 contributesF-ST2-001. | PASS_2_COMPLETE |
| S075 | Handgrip interaction.04 is a distinct significant genotype comparison; no invented interactiondf. Baseline aggregation does not reconstruct an interaction effect. | PASS_2_COMPLETE |
| S076 | Mean-handgrip−1.44/−2.66–−.22/P=.02 coherent; M−P−1.43 overlaps precision. C011 sign supported, C004 measurement mapping retained. | PASS_2_COMPLETE |
| S077 | First-eyelid−4.25/−8.45–−.05/P=.05 remainsC017 under strictP<.05 printed rule. LatentP≈.0475 fully reconciles underlying inference but cannot remove RouteA1. C011 sign supported. | PASS_2_COMPLETE |
| S078 | Fifth-eyelid−.95/−2.25–.35/P=.14 is nonsignificant; rounding permits paired diagnostic.1451. Perioddifference matches and C011 sign supported. | PASS_2_COMPLETE |
| S079 | Mean-eyelid−2.11/−3.94–−.28/P=.03 contained/significant; paired diagnostic.02549 matches displayed.03; difference identity matches, C011 orientation. | PASS_2_COMPLETE |
| S080 | First TUG−1.25/−2.23–−.28/P=.01 contained/significant; paired diagnostic.01398 matches.01; period difference−1.26 overlaps rounding. C011 orientation. | PASS_2_COMPLETE |
| S081 | Fifth TUG−1.00/−2.01–.03/P=.06 crosses null/nonsignificant; centralpaired.0543 can overlap printed P under input rounding, no new RouteA1. C011 orientation. | PASS_2_COMPLETE |
| S082 | Mean TUG placebo+.07 aboveCIupper+.01 remainsC018. Effect−1.12/negative CI/P=.02 coherent; period difference matches and C011 orientation supported. | PASS_2_COMPLETE |
| S083 | First relaxation−.02/crossing CI/P=.96 coherent. NominalP−M=0 cannot support a sign reversal; C011 exception. C015 preserves .005gap/.02=.25 under operativeM−P. | PASS_2_COMPLETE |
| S084 | Fifth relaxation−.01/crossing CI/P=.87 coherent with coarse tiny-effect precision; M−P−.02 overlaps. C011 header sign differs but no magnitude issue added. | PASS_2_COMPLETE |
| S085 | Mean relaxation−.02/crossing CI/P=.91 can reconcile diagnostic by rounding. It reproduces literalP−M header, C011 exception; opposite predominantM−P mapping discrepancy remainsC015. | PASS_2_COMPLETE |
| S086 | First force32.92/−5.10–70.94/P=.09 coherent; C015 period difference26.73 gap.187576 and C011 orientation retained. Missingweights remain alternative. | PASS_2_COMPLETE |
| S087 | Fifth force24.08/−5.22–53.39/P=.10 coherent; C015 period difference21.81 gap.093646 and C011 orientation retained. | PASS_2_COMPLETE |
| S088 | Mean force37.23/10.19–64.28/P=.009 coherent paired diagnostic.008863; C015 period difference33.75 gap.093070/C011 orientation. | PASS_2_COMPLETE |
| S089 | First paresis−3.7/crossing CI/P=.51 coherent; C015 .136486 relative difference and C011 direction retained. Its unequal decimal precision is explicitly allowed. | PASS_2_COMPLETE |
| S090 | Fifth paresis total−12.25/negative CI/P=.02 coherent; C015 .240408 magnitude gap/C011 orientation. Baseline20.30 versus subgroup aggregation18.145185 exceeds full precision,F-ST2-001. | PASS_2_COMPLETE |
| S091 | Fifth paresis CLCN1−23.85/negative CI/P<.001 coherent; period difference−23.06 within.05, no magnitude addition; C011 sign supported. Baseline24.35 contributesF-ST2-001. | PASS_2_COMPLETE |
| S092 | Fifth paresis SCN4A13.71/−1.96–25.47/P=.02 remainsC010 crossing null/test conflict. C015 .060904 magnitudegap/C011 sign retained; baseline9.12 contributesF-ST2-001. | PASS_2_COMPLETE |
| S093 | FifthparesisinteractionP<.001 matches narrative and differs from subgroupP=.02; no inferred interactionvariance. | PASS_2_COMPLETE |
| S094 | Mean paresis total−7.34/negative CI/P=.02 coherent; C015 .139646 magnitudegap/C011 orientation. Baseline24.11 versusweighted22.594815 screens after full-count precision .012916. | PASS_2_COMPLETE |
| S095 | Mean paresis CLCN1−12.37/negative CI/P<.001 coherent; period difference−12.79 relative.0327 screens precision; C011 orientation. Baseline32.56 participates only in excluded full-count aggregation. | PASS_2_COMPLETE |
| S096 | Mean paresis SCN4A4.46/crossing CI/P=.28 coherent at null. Exact subgroupengine/df unknown; diagnostic.259 is not substituted. C015 .106502/C011 orientation; baseline8.10 contributes excluded aggregation. | PASS_2_COMPLETE |
| S097 | Meanparesisinteraction.002 matches narrative; separate subgroupP values are not substituted and no inference from unstated covariance. | PASS_2_COMPLETE |
| S098 | Needle EMG.67/.23–1.11/P<.001 remainsC019 under dependent-test relation, diagnosticP.0042828 with pairedn unavailable.2.52−1.85=.67; separatecontinuationheader not added toC011. | PASS_2_COMPLETE |
| S099 | All27 patient table points contained/intervals ordered; 23one-set+4two-set=31. Patients8/20 rounded80 may exceed80; patient11 disclosed38% override versusmain attribution remainsC007. Patient21 mismatch screen upheld. | PASS_2_COMPLETE |
| S100 | Maximum four sets and interim stop/continuation paths coherent; observed 27 patients/31 sets fitsdesign. No noninferiority/multiplicity/stopping conclusion inferred beyondexplicit rule. | PASS_2_COMPLETE |
| S101 | Posterior100/45/87/74% matchesmain symptom narratives; positive Placebo−Mexiletine benefit and threshold.75 agree. No frequentistP comparison. | PASS_2_COMPLETE |
| S102 | Individualnormalarmmeans/widepriors/step(diff−.75) coherent; loops1:30 and missingvectorhandling are namedlimits. C002 preservesplanned group prior differences, C021 plan-only prior paths; no new unsupportedimplementation issue. | PASS_2_COMPLETE |
| S103 | Group actual N loops/shared within SD/effectmu.plac−mu.mex identifyresults despiteglossaryswaps. C002 retains explicitprimary prior/robustness comparison; C006 planned interactions absent from code. No assumed arm covariance. | PASS_2_COMPLETE |
| S104 | Binary1CLCN1/0SCN4A yields(c+d)−(a+b) andc−a. Glossary naming resolvedbyequations; screenedF-ST1-208 not re-emitted. C002 primary prior comparison remains; exactposterior draws unavailable. | PASS_2_COMPLETE |
| S105 | Null0/1000 andpositive685/1000,means4.65−4.58=.07/4.67−3.38=1.29 andbias−.46 reconcile. Two simulation regimes distinct from planned expected posterior; code pointers andfull inputabsence not RouteA conflicts. | PASS_2_COMPLETE |

## Excluded-observation reread

All 44 original checker excluded rows were read against Route A categories 1–5 and full-input half-unit precision. This is a provenance audit, not a second set of finding IDs. Reconciled ordinary relationships are recorded above, not counted as exclusions. Original row numbering below follows each checker's Excluded observations table in order. Existing screened findings and included candidates are not re-emitted.

| Original row | Observation reviewed | Pass-2 reason / implication |
|---|---|---|
| NUM-E01 | Placebo Any 2/30 printed 6% | ROUNDING_OR_DISPLAY_PRECISION: remaining gap .166667/6=.027778. Route A3 does not survive precision. |
| NUM-E02 | Other 5/11 printed 46% | ROUNDING_OR_DISPLAY_PRECISION: gap .045455/46=.000988. C009 concerns P, not percentage. |
| NUM-E03 | IVR zero versus 1–9 | CONTEXT_RESOLVES: zero symptom absence is expressly defined. |
| NUM-E04 | IVR weakness/SCN4A stiffness crude versus fitted effect | MODEL_VERSUS_CRUDE: explicitly mixed models, no crude estimate claim. |
| NUM-E05 | Historical NI 30 versus 22 | PERIPHERAL_COMPARISON: no current result or decision input changed. |
| NUM-E06 | Historical OR 1.19% | NOTATION_OR_TYPOGRAPHY: OR and interval identify quantity; no printed digits changed. |
| XS-E01 | Enrollment versus completer genotype/sex | CONTEXT_RESOLVES: 30 enrolled versus 27 analyzed; C001 is separate. |
| XS-E02 | Bayesian versus frequentist estimates | CONTEXT_RESOLVES: explicitly different analyses, no shared CI/P mapping. |
| XS-E03 | Twenty versus thirty recruitment cohorts | CONTEXT_RESOLVES: later Maastricht 10 completes target 30. |
| XS-E04 | Planned posterior .817/.821 versus power 69% | CONTEXT_RESOLVES: different defined simulation estimands and regimes. |
| XS-E05 | Shorter eligibility/CTG description | TERMINOLOGY_OR_WORDING: detailed criteria do not change a statistical population result. |
| XS-E06 | Washout minima 2/3/5 versus 14 days | CONTEXT_RESOLVES: actual duration meets minima. |
| XS-E07 | Dose titration absence | CONDITIONAL_OR_UNREPORTED: target 600 mg does not exclude titration. |
| XS-E08 | Needle EMG procedural detail | CONDITIONAL_OR_UNREPORTED: no incompatible grading threshold reproduced. |
| XS-E09 | Added TUG/paresis and unreported nonkey secondary | CONDITIONAL_OR_UNREPORTED: not called prespecified; no key-secondary absence established. Method comparison already C003. |
| XS-E10 | Inclusive versus strict 80/20 | ROUNDING_OR_DISPLAY_PRECISION: rounded 80 permits >80; no exact boundary event. |
| XS-E11 | Figure 3C patient-ID pointer | PERIPHERAL_COMPARISON: changed posterior not reproduced. |
| XS-E12 | Cross-document baseline copies | PERIPHERAL_COMPARISON: does not exempt within-display aggregation F-ST2-001 or C008/C009. |
| XS-E13 | Calendars and centers | PERIPHERAL_COMPARISON: administrative, no changed primary decision rule. |
| ST1R-E01 | Bayesian/frequentist/crude | MODEL_VERSUS_CRUDE: distinct explicit models do not share required numbers. |
| ST1R-E02 | CLCN1 graph group coordinates | ROUNDING_OR_DISPLAY_PRECISION: visual bounds leave gap at most .05; no exact printed copy. |
| ST1R-E03 | SCN4A terminal 88 versus 93% | ROUNDING_OR_DISPLAY_PRECISION: [87,89] versus [92.5,93.5] gives 3.5/93=.0376. |
| ST1R-E04 | Patient 11 clinical override | DUPLICATE_OF_INCLUDED for numerical-rule attribution already C007; disclosed clinical decision alone is contextually explained. No F-ST2 re-emission. |
| ST1R-E05 | Patients 8/20 rounded 80 | ROUNDING_OR_DISPLAY_PRECISION: unrounded values may exceed 80. |
| ST1R-E06 | Model glossary swaps | TERMINOLOGY_OR_WORDING: equations, observation loops and genotype code identify results. |
| ST1R-E07 | Simulation section pointers | CONTEXT_RESOLVES: named model role and code identify the analysis. |
| ST1R-E08 | Loops 1:30, shorter vectors | CONDITIONAL_OR_UNREPORTED: absent implementation detail lacks a conflicting printed result. |
| ST1R-E09 | Simulation generation inputs | CONDITIONAL_OR_UNREPORTED: missing rerun inputs, no independent numerical conflict. |
| ST1R-E10 | Mental SF-36 period midpoint | ROUNDING_OR_DISPLAY_PRECISION: .190/4.77=.03983; not added to C012. |
| ST1R-E11 | Lower period-effect near differences | ROUNDING_OR_DISPLAY_PRECISION: all listed remaining gaps at most .05; C015 retains 11 other rows. |
| ST1R-E12 | Fifth TUG/mean relaxation central P diagnostics | ROUNDING_OR_DISPLAY_PRECISION: full input intervals can reproduce P; null classification agrees. No Route A1 remains. |
| ST1R-E13 | Patient 11 invisible wide whisker | CONDITIONAL_OR_UNREPORTED: not an exact zero-width printed interval. |
| ST1P-E01 | Secondary interpreted as exploratory | TERMINOLOGY_OR_WORDING: formal secondary label persists. C003 retains Route B actual method comparison. |
| ST1P-E02 | Omitted nonkey secondary/Bayesian results | PERIPHERAL_COMPARISON for isolated nonkey absence; C003 records concrete analysis specification. No added key designation. |
| ST1P-E03 | Added TUG | CONDITIONAL_OR_UNREPORTED: not called prespecified; not a changed key endpoint status. |
| ST1P-E04 | Simulation period versus pair caption | TERMINOLOGY_OR_WORDING: same-section observations and formula identify the pair scenario. |
| ST1P-E05 | Twenty/thirty cohort target | CONTEXT_RESOLVES: later explicit 20+10 schedule. |
| ST1P-E06 | Sodium subtype labels | TERMINOLOGY_OR_WORDING: no structural estimand change established by schematic labels. F-ST1-208 already screened. |
| ST1P-E07 | Blinded code break and clinical advice | CONDITIONAL_OR_UNREPORTED: implementation not supplied; no actual statistical decision contradiction. |
| ST1P-E08 | Random intercept/slope versus arm means | CONDITIONAL_OR_UNREPORTED: covariance/full planned likelihood absent; no assumed equivalence test. |
| ST1P-E09 | Normal/inverse-gamma conjugacy | CONDITIONAL_OR_UNREPORTED: wording alone lacks conflicting implemented posterior; concrete priors already C002. |
| ST1P-E10 | Equality 80/20 operators | CONDITIONAL_OR_UNREPORTED: no exact boundary event; realized decisions cannot be inferred. |
| ST1P-E11 | Standardized effect .34 versus .43 | CONTEXT_RESOLVES: explicit SD 2.19 versus 1.75 explains difference; threshold .75 unchanged. |
| ST1P-E12 | Three-month versus 18–31 month follow-up | PERIPHERAL_COMPARISON: extended clinical follow-up does not change primary endpoint window. |

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main Table 2 mean transient-paresis baselinep.7/genotype n footnotep.8 | Total24.11versus(16×32.56+11×8.10)/27=22.5948148. Allowing every input itscontinuous half unit gives[21.440000,23.7935849]versus[24.105,24.115],gap.3114151/24.11=.0129164≤.05. This row is not added toF-ST2-001. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion and limitations

105 assigned relationships individually PASS_2_COMPLETE; one new finding F-ST2-001, covering two baseline means; one new excluded observation. All 44 original exclusions reread, and all 21 candidate recheck/classification facts considered. Initial 34 decisions not re-emitted. Existing source access is complete; no affected source unit is inaccessible. Exact baseline available-case denominators/weights, outcome-specific paired n/df, individual data/posterior draws, model/amendment records and intended contrast/score definitions remain unavailable. Diagnostic calculations do not replace the reported methods. New finding requires the fresh independent pass-2 inclusion screen before any candidate registration.
