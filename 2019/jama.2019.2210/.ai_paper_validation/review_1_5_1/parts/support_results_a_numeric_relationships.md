# DOC-003 Results Supplement, Shard A: Numeric Relationship Inventory

Provisional numeric keys are local to this shard. Locations refer to `joi190023supp2_prod.pdf` PDF pages. These are extracted relationships, not candidate determinations.

| Provisional key | Location | Population/time/measure | Printed numeric relationship and matching key |
|---|---|---|---|
| AN001 | p. 2, eFigure 1A | Mean 25(OH)D strata; relapse/death; 0/2/4/6 years | At-risk vectors: <20 ng/mL 114/64/29/10; 20-<30 123/78/32/9; 30-<40 94/70/39/17; 40-<50 39/38/21/8; >=50 43/37/25/7. Match key: `AVG25OHD_POSTHOC|RELAPSE_DEATH|STRATA|RISKSET`. |
| AN002 | p. 3, eFigure 1B | Mean 25(OH)D strata; all-cause death; 0/2/4/6 years | At-risk vectors: <20 114/78/36/13; 20-<30 123/87/37/12; 30-<40 94/76/43/17; 40-<50 39/39/21/8; >=50 43/42/28/7. Match key: `AVG25OHD_POSTHOC|ALL_CAUSE_DEATH|STRATA|RISKSET`. |
| AN003 | p. 4, eTable 1 | Average 25(OH)D stratum; active group | Counts (percent): <20 40 (16%); 20-<30 56 (23%); 30-<40 71 (29%); 40-<50 39 (16%); >=50 42 (17%); total 248 (60%). Match key: `AVG25OHD|ACTIVE|STRATUM_COUNT_PERCENT`. |
| AN004 | p. 4, eTable 1 | Average 25(OH)D stratum; placebo group | Counts (percent): <20 74 (45%); 20-<30 67 (41%); 30-<40 23 (14%); 40-<50 0 (0%); >=50 1 (0.6%); total 165 (40%). Match key: `AVG25OHD|PLACEBO|STRATUM_COUNT_PERCENT`. |
| AN005 | p. 4, eTable 1 | Both treatment groups | Category-count sum: active 40+56+71+39+42=248; placebo 74+67+23+0+1=165. Displayed percentages are rounded. Match key: `AVG25OHD|TREATMENT_TOTALS|CATEGORY_SUM`. |
| AN006 | p. 5, eFigure 2 | Serum 25(OH)D (ng/mL), placebo and vitamin D | Five plotted time points: pre and 1/2/3/4 years after starting supplements, measured within the same calendar month. Values are graphical box-plot summaries without printed numeric medians, quartiles, whiskers, or sample sizes. Match key: `SERUM25OHD|TREATMENT|LONGITUDINAL_BOX_PLOT`. |
| AN007 | p. 6, eTable 2 | Baseline serum 25(OH)D missingness | Missing baseline values: vitamin D group 3 (1%); placebo group 4 (2%); multiple imputation used. Match key: `BASELINE25OHD|MISSINGNESS|MULTIPLE_IMPUTATION`. |
| AN008 | p. 7, eFigure 3A | FokI CC subgroup; placebo/vitamin D; 0/2/4/6 years | At risk placebo 57/37/19/8; vitamin D 92/64/35/9. Match key: `SNP_FOKI_CC|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN009 | p. 8, eFigure 3B | FokI CT | At risk placebo 75/53/24/5; vitamin D 117/89/48/23. Match key: `SNP_FOKI_CT|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN010 | p. 9, eFigure 3C | FokI TT | At risk placebo 25/18/10/3; vitamin D 36/21/10/3. Match key: `SNP_FOKI_TT|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN011 | p. 10, eFigure 3D | BsmI AA | At risk placebo 8/3/1/0; vitamin D 14/11/5/2. Match key: `SNP_BSMI_AA|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN012 | p. 11, eFigure 3E | BsmI AG | At risk placebo 23/13/7/1; vitamin D 42/26/15/3. Match key: `SNP_BSMI_AG|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN013 | p. 12, eFigure 3F | BsmI GG | At risk placebo 119/88/43/13; vitamin D 175/125/72/29. Match key: `SNP_BSMI_GG|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN014 | p. 13, eFigure 3G | CDK2 GG | At risk placebo 49/32/18/5; vitamin D 89/62/34/7. Match key: `SNP_CDK2_GG|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN015 | p. 14, eFigure 3H | CDK2 GA | At risk placebo 77/54/25/7; vitamin D 103/72/46/20. Match key: `SNP_CDK2_GA|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN016 | p. 15, eFigure 3I | CDK2 AA | At risk placebo 24/18/8/2; vitamin D 38/28/12/7. Match key: `SNP_CDK2_AA|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN017 | p. 16, eFigure 3J | ApaI GG | At risk placebo 69/53/30/9; vitamin D 96/73/39/15. Match key: `SNP_APAI_GG|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN018 | p. 17, eFigure 3K | ApaI GT | At risk placebo 61/42/18/5; vitamin D 104/65/40/14. Match key: `SNP_APAI_GT|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN019 | p. 18, eFigure 3L | ApaI TT | At risk placebo 20/9/3/0; vitamin D 31/24/13/5. Match key: `SNP_APAI_TT|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN020 | p. 19, eFigure 3M | TaqI TT | At risk placebo 115/86/42/13; vitamin D 172/122/70/29. Match key: `SNP_TAQI_TT|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN021 | p. 20, eFigure 3N | TaqI TC | At risk placebo 31/16/8/1; vitamin D 54/37/19/4. Match key: `SNP_TAQI_TC|RELAPSE_DEATH|TREATMENT_RISKSET`. |
| AN022 | p. 21, eFigure 3O | TaqI CC | At risk placebo 4/2/1/0; vitamin D 5/3/3/1. Match key: `SNP_TAQI_CC|RELAPSE_DEATH|TREATMENT_RISKSET`. |
