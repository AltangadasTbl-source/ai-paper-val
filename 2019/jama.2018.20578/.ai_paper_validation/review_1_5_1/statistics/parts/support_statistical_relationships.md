# Support Statistical Relationship Inventory Part

All records are source mappings, not diagnoses or candidate determinations.

## SS001 — Bayesian and frequentist analysis definitions

- **Source:** DOC-002 p. 6; DOC-003 pp. 3-4.
- **Printed definitions:** Bayesian hierarchical pairwise meta-analysis; HR with 95% CrI; Poisson likelihood and log link for event/person-time studies; logged reported HRs and their SEs when available; fixed/random model selection by DIC; MCMC 5,000 adaptation then 100,000 iterations x 4 chains; PSRF cutoff 1.056. Frequentist `meta` analysis uses random-effects Mantel-Haenszel RR/95% CI for ARD. Two-sided frequentist P cutoff is 0.05. Bayesian 95% CrI excluding 1 is significant.
- **Formula labels:** 10-year risk = (no-aspirin primary-event risk / mean follow-up years) x 10. ARD uses no-aspirin event count / participants as baseline risk and RR with its CI; negative favors aspirin.

## SS002 — Model-selection rule and DIC values

- **Source:** DOC-003 pp. 4-6; numeric matrix in SN002.
- **Rule:** DIC difference >3 is important; use lowest DIC. Within 3 units, select random if fixed-effect I2 >25%. `I2` thresholds are <25 low, 25-50 moderate, >50 high. The 44 printed outcome/subgroup DIC comparisons, I2 values, and selected models are fully mapped in SN002.

## SS003 — ARD, NNT/NNH, and endpoint-scale relationships

- **Source:** DOC-003 pp. 4, 15-18.
- **Relationships:** eTable 3 presents ARD and intervals with NNT/NNH only when ARD is statistically significant; eTable 5 presents rates per 10,000 participant-years rather than risk/proportion; eTable 6 presents HR (95% CrI), while eFigure 4 presents frequentist RR (95% CI). Corresponding full numeric matrices are SN003, SN005, and SN006.

## SS004 — Funnel-plot small-study test

- **Source:** DOC-003 p. 21.
- **Printed values:** Egger test estimate -0.47, SE 0.77, t=-0.59, P=0.57. The source does not state degrees of freedom or a separate sidedness rule on this page; no unprinted compatibility calculation is imposed.

## SS005 — eTable 4 total-stroke inferential relationships

- **Source:** DOC-003 p. 16.
- **Printed HR (95% CrI), I2:** all 0.93 (0.86,1.02), I2=1; low risk 0.95 (0.79,1.16), I2=6; high risk 0.89 (0.77,1.03), I2=11; diabetes 0.78 (0.61,1.00), I2=13, with exact upper endpoint 1.004. Companion ARR (95% CI) and count denominators are SN004.

## SS006 — eFigure 4 frequentist forest-plot outcome summaries

- **Source:** DOC-003 pp. 22-26; direct-rendered source pages checked. Experimental=aspirin, control=no aspirin; RR with 95% CI. Summary values are fixed/random RR; heterogeneity is I2, tau2, P.
- **Composite (p.22):** totals 81,623/80,057; fixed 0.90 (0.86,0.94), random 0.90 (0.86,0.94); I2=0%, tau2=0, P=0.75.
- **All-cause mortality (p.22):** 81,623/80,057; fixed/random 0.97 (0.93,1.02); I2=0%, tau2=0, P=0.60.
- **Cardiovascular mortality (p.23):** 81,623/80,057; fixed 0.94 (0.86,1.03), random 0.95 (0.87,1.03); I2=0%, tau2=0, P=0.50.
- **All myocardial infarction (p.23):** 81,623/80,057; fixed 0.87 (0.81,0.93), random 0.86 (0.76,0.97); I2=61%, tau2=0.0273, P<0.01.
- **Total stroke (p.24):** 81,623/80,057; fixed 0.94 (0.88,1.02), random 0.94 (0.87,1.01); I2=0%, tau2=0, P=0.51.
- **Ischaemic stroke (p.24):** 65,316/63,752; fixed/random 0.87 (0.80,0.96); I2=0%, tau2=0, P=0.55.
- **Incident cancer (p.24):** 63,048/61,475; fixed 1.01 (0.97,1.05), random 1.00 (0.95,1.06); I2=36%, tau2=0.0026, P=0.12.
- **Cancer mortality (p.25):** 75,353/73,781; fixed/random 1.03 (0.96,1.11) and 1.03 (0.94,1.12); I2=21%, tau2=0.0044, P=0.24.
- **Major bleeding (p.25):** 74,715/73,143; fixed/random 1.42 (1.30,1.55); I2=0%, tau2=0, P=0.54.
- **Intracranial bleeding (p.25):** 80,985/79,419; fixed/random 1.33 (1.14,1.57) and 1.33 (1.13,1.57); I2=0%, tau2=0, P=0.93.
- **Major gastrointestinal bleeding (p.26):** 70,336/70,465; fixed 1.56 (1.38,1.78), random 1.55 (1.37,1.77); I2=0%, tau2=0, P=0.54.
- **Direct-source row inventory:** pp. 22-26 contain every displayed individual-study events, totals, RR, 95% CI, and fixed/random weights. They remain in the direct forest-plot source unit; OCR is only a locator/transcription aid. Later rechecking should verify a selected row directly against the indicated PDF page before using a row-level value in a candidate.

## SS007 — Sensitivity-analysis inferential relationships

- **Source:** DOC-003 p. 18; complete 11-outcome x 4-analysis HR/CrI matrix in SN006.
- **Labels:** <=100 mg daily, double-blind placebo controlled, studies since 2000, and excluding asymptomatic PAD. The MI <=100 mg displayed CI endpoint is 1.00 with footnote exact upper endpoint 0.9989; this is an explicit rounding/footnote definition, not treated as a display contradiction in this mapping.

## SS008 — Statistical relationship pending matched-source review

- **Source locations:** DOC-003 p. 16 and p. 24, interpreted with endpoint definition on p. 9 and protocol statement DOC-002 p. 7.
- **Observation:** eTable 4 total-stroke HR is based on 12 studies and 73,883/72,317; frequentist total-stroke forest plot reports 13 displayed study rows and 81,623/80,057. ASCEND is 7,740 per arm on p.24, while p.9 says its all-stroke outcome is not included. The source units do not state whether the forest row has a distinct intended endpoint convention. This needs later cross-source and direct-source recheck; it is not a candidate finding here.
