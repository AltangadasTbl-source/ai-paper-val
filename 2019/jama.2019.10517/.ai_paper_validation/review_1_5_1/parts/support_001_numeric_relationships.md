# Support 001 numeric relationship inventory

**Scope:** DOC-002 `joi190079supp1_prod.pdf` PDF pp. 1-21. Local IDs are shard-local (`A-N001` onward), not stable package IDs. All locations are direct PDF pages.

| Local ID | PDF page(s) | Printed relationship / definition | Checkability and mapping status |
|---|---:|---|---|
| A-N001 | 2-3 | Proposed RCT duration 36 weeks; acute maximum 12 weeks plus 8-week stabilization. | Planned phase durations; coherent across pp. 2-3. |
| A-N002 | 4-5 | Contextual prevalence/rates: 15%-20%, 19%-45%, 17%-50% (mean 30%), 35%-50%, 27%/8 months/n=30, 0%-6%/12 months. | Contextual cited literature; not a proposed outcome. |
| A-N003 | 6 | Historical STOP-PD N=259; age split 142+117; sites 56+59+63+81. | Both sums equal 259. |
| A-N004 | 6 | Last-assessment remission 41.9% vs 23.9%, NNT 5.6. | ARR=.180; 1/.180=5.56 -> 5.6. |
| A-N005 | 6 | Completed-12-week remission 66.7% vs 49.2%, NNT 5.7. | ARR=.175; 1/.175=5.71 -> 5.7. |
| A-N006 | 6 | Historical age weight gain 7.3 +/- 10.3 lb vs 13.9 +/- 4.0 lb; younger glucose change 8.4 +/- 41.3 mg/dL from 93.6 +/- 20.4 mg/dL. | Units and direction explicit; historical results. |
| A-N007 | 6 | PK pilot n=66 young +102 old; variability and magnitude values. | n total 168; pooled-variance t df=166 accords with n1+n2-2. |
| A-N008 | 7 | Stabilization n=74=29+45; 10.4% of 48 remitters; 1.5 vs 4.4 lb/month. | 10.4% corresponds to approximately 5/48 after rounding. |
| A-N009 | 7 | Figure 1 acute N=392, n=196 per age group; 50% -> N=196; 10% loss -> RCT N=176. | 392/2=196; 196*.90=176.4, compatible with whole-person rounded 176. |
| A-N010 | 8 | 392 recruits / 4 sites / 38 months = printed 2.6/site/month. | Calculation 2.579, rounds 2.6. |
| A-N011 | 8 | 63/129=48.8%; 10/129=7.8%; total 73/129=56.6%. | All values agree with conventional one-decimal rounding. |
| A-N012 | 8 | Planning: 50% acute remission/near-remission ->196 and 10% stabilization noncompletion ->176 RCT. | Same flow arithmetic as A-N009. |
| A-N013 | 9 | RCT 36 weeks; high-risk postdiscontinuation period 3 months; taper 4 weeks; historical 1/37 MMSE <24. | Distinct planned duration/eligibility relationship. |
| A-N014 | 10-11 | Table 1 phase/time schedule, acute 4-12 weeks, stabilization 8, RCT 36; RCT phone assessments weeks 10,14,18,22,26,30,34. | Schedule/measurement timing, not a result table. |
| A-N015 | 11-12 | Genotype recheck 10%, stated error rate .5%; 96 ancestry markers; 20,000 burn-ins plus 20,000 repetitions; 2-4 PK samples/patient. | Planned QC/model quantities. |
| A-N016 | 12 | Relapse numeric thresholds: HAM-D >=18 plus mean absolute increase >=5; SADS severity >=3; referral 48-72 h; expected 3 relapses/year/site. | Outcome definition and service planning; “3” is not an observed event rate. |
| A-N017 | 13 | Drug doses/ranges: acute sertraline 50 ->150 mg/day, possible 200; olanzapine 5 ->15, possible 20; stabilization 50-200 and 5-20. | Doses, units, thresholds explicit. |
| A-N018 | 13 | Randomization N=176=88+88, 1:1; covariate rule requires significant imbalance and r>=.30. | 88 x2=176. |
| A-N019 | 14 | H2 repeat measures: <=15 weights, <=5 cholesterol/triglycerides; post-lipid-treatment data excluded; expected <5%, i.e. <10. H3 <=6 weights over 12-20 weeks. | “<5%” of 176 is <8.8, consistent with “<10.” |
| A-N020 | 14-15 | Genotype exclusions: call rate <95%, MAF <10%, HWE P<.001; haplotypes <10%. Safety adverse-event thresholds and N/% reporting. | Explicit units/scales and rate-count distinction. |
| A-N021 | 15 | H1 assumed relapse 35% placebo vs15% olanzapine: 20-point difference, NNT=5; attrition <=10%. | 1/(.35-.15)=5. |
| A-N022 | 15 | Table 2 power rows: .95, .94, .84, .82, .98, .97 for printed relapse/attrition scenarios. | Simulation outputs; no independent recomputation attempted. |
| A-N023 | 15-16 | H2 assumptions: 1 lb/month continued gain; 1.5 lb/month STOP-PD stabilization; 8-10 mg/dL/month triglycerides and ~9 mg/dL/month STOP-PD. | Planned power inputs/cited historical values. |
| A-N024 | 16 | Table 3 effect/power values; endpoints 4.9 lb, 38 mg/dL, 22 mg/dL; H3 gains 16.6 +/-16.5 vs10.7 +/-11.3 lb, standardized .42. | Approximate standardized difference: 5.9 / pooled SD ~14.1 = .42. |
| A-N025 | 17 | Table 4: four sites each recruit 98 acute and randomize 44 remitted. | Implies 392 and 176, matching A-N009/A-N018. |
| A-N026 | 19-21 | Reliability/data-quality metrics: 12 videos annually; ICC .93-.98 and .69-.84; 100% audit; >170,000 scales; ~6% problems; 10% double entry; .27% error. | Administrative metrics, separately identified from outcomes. |
| A-N027 | 21 | Four sites “each site recruiting 82 patients.” | Implies 328, conflicting with A-N009/A-N025's planned 392 (196x2/98x4). Potential QC observation; no C ID. |

## Numeric observation requiring downstream source recheck

**A-N027:** Direct observation: p. 21 prints 82 patients at each of four sites, while p. 7 Figure 1 prints acute N=392 and p. 17 Table 4 prints 98 acute participants/site. Derived arithmetic: 4 x 82=328 and 4 x 98=392. The source does not state a distinct recruitment population, phase, or time frame for the p. 21 figure. This is a potential denominator/total and cross-section consistency issue, pending exact-source recheck and human explanation; it has no package candidate ID here.

## No-applicable numeric units

PDF p. 1 has no result-relevant numerical relationship beyond contents pagination. No workbook, spreadsheet formula, cached value, CSV, DOC/DOCX, or other structured support file is in this assigned scope; consequently formula-versus-cached-value distinction is not applicable.
