# Canonical Statistical Relationship Inventory

**Pass status:** PASS_1_COMPLETE and PASS_2_COMPLETE for every S001-S038 relationship.

Fresh-part union with global IDs S001-S038. `Temp` preserves source-part IDs. Both completed pass statuses are recorded above. No relationship was omitted or count-capped.

| Global ID | Temp | Location | Population / contrast / printed statistic or rule | Coverage note |
|---|---|---|---|---|
| S001 | MS001 | DOC-001 p.3 | Primary ITT/PP BMV-ETI; two-sided95% CI/lower>-1%; published 1-sided97.5%. | Preserve rule/sidedness. |
| S002 | MS002 | DOC-001 pp.1,4 | ITT diff .11%; 1-sided97.5% CI -1.64% to infinity; P=.11. | Compare under stated rule. |
| S003 | MS003 | DOC-001 p.4 | Hierarchical diff .05%; CI -1.70% to infinity; centre random effect. | Distinct model. |
| S004 | MS004 | DOC-001 p.4 | PP 4.3% vs4.2%; diff .08%; CI -1.74% to infinity;P=.12. | Distinct population. |
| S005 | MS005 | DOC-001 p.3 | Secondary chi-square proportions; 95% OR/difference CIs; alpha .05/no multiplicity. | Rule. |
| S006 | MS006 | DOC-001 p.6 | ITT 28-day survival diff .1;CI -1.8,2.1;P=.90. | Rate. |
| S007 | MS007 | DOC-001 p.6 | ITT CPC distribution P=.68. | Multicategory. |
| S008 | MS008 | DOC-001 p.6 | Admission diff -3.7;CI -7.7,.3;P=.07. | Rate. |
| S009 | MS009 | DOC-001 pp.4,6 | ROSC diff -4.7;CI -8.8,-.5;P=.03. | Direction key. |
| S010 | MS010 | DOC-001 p.6 | PP survival diff .1;CI -10,9.7;P=.99. | Preserve displayed scale. |
| S011 | MS011 | DOC-001 p.6 | PP CPC distribution P=.76. | Multicategory. |
| S012 | MS012 | DOC-001 p.6 | PP admission diff -4.0;CI -7.6,.6;P=.055. | Rate. |
| S013 | MS013 | DOC-001 p.6 | PP ROSC diff -5.6;CI -9.9,-1.3;P=.01. | Numeric reconciliation relevant. |
| S014 | MS014 | DOC-001 pp.1,4,6 | Difficulty diff4.7;CI1.5,7.9;P=.004. | Rate. |
| S015 | MS015 | DOC-001 pp.1,4,6 | Failure diff4.6;CI2.8,6.4;P<.001. | Non-zero inequality display. |
| S016 | MS016 | DOC-001 pp.1,4,6 | Regurgitation diff7.7;CI4.9,10.4;P<.001. | Non-zero inequality display. |
| S017 | MS017 | DOC-001 p.4 | Centre5 CCF diff-1;CI-4,2;P=.70. | Post-hoc quantitative. |
| S018 | MS018 | DOC-001 p.4 | Centre5 pauses diff11s;CI7,15;P<.001. | Unit seconds. |
| S019 | MS019 | DOC-001 p.3 | 956/group,80%,95% CI,5000 simulations,2000 target. | Planning. |
| S020 | MS020 | DOC-001 pp.3,6 | IDS>5; VAS0-100mm;Han>2; medians/IQRs. | Label/scale. |
| S021 | AS001 | DOC-002 pp.11,35-36 | ITT/PP definitions. | Defined. |
| S022 | AS002 | DOC-002 pp.11,36-37 | 95% CI BVM-TI, lower >-.01. | Defined. |
| S023 | AS003 | DOC-002 p.36 | H0<=-.01/H1>=-.01; difference after NI. | Defined. |
| S024 | AS004 | DOC-002 pp.11,37 | Chi-square/95% OR+difference; t/MW. | Defined. |
| S025 | AS005 | DOC-002 pp.11,36 | Interim 50/75%. | Planned. |
| S026 | AS006 | DOC-002 pp.11,37 | 3%,2%,1%,956/group,.8,.025,2000,5000. | Planning. |
| S027 | AS007 | DOC-002 p.37 | Safety chi-square/OR; logistic exploratory. | Defined. |
| S028 | AS008 | DOC-002 p.37 | Worst-case primary missing; multiple-imputation sensitivity. | Defined. |
| S029 | AS009 | DOC-002 pp.64-66 | Revised summary repeats S021-S026. | Cross-version agreement. |
| S030 | BS001 | DOC-002 pp.120-121 | SAP margin -.01,H0/H1,two-sided alpha .05. | Defined. |
| S031 | BS002 | DOC-002 p.124 | 95% CI/lower >-.01; exact CI; ITT/PP/AT. | Published one-sided 97.5 corresponding form. |
| S032 | BS003 | DOC-002 pp.120,123 | Interim cancelled/only final/no multiplicity; primary missing no success; no secondary imputation. | Defined. |
| S033 | BS004 | DOC-002 pp.123-124 | Nonmissing categorical denominators/one-decimal; secondary chi-square/CI; t/MW. | Defined. |
| S034 | BS005 | DOC-002 p.124 | Safety ITT/AT; chi-square/Fisher; t/MW. | Defined. |
| S035 | BS006 | DOC-003 p.3 | Post-hoc P=.63,diff.4,CI[-2.2,1.3]. | CI/P coherent. |
| S036 | BS007 | DOC-003 p.3 | Post-hoc P=.31,diff.9,CI[-.9,2.7]. | CI/P coherent. |
| S037 | BS008 | DOC-002 p.122 vs pp.114-116 | SAP safety list predates aspiration-pneumonia/BVM-failure additions. | VERSIONED_DEFINITION_DIFFERENCE. |
| S038 | BS009 | DOC-002 rendered p.103 | IDS 0<IDS<=5 slight, IDS>5 moderate-major, infinity impossible; main calls >5 difficult. | Definitions agree; score 5 is slight difficulty; no candidate. |

Temporary-ID provenance: MS001-M020=`parts/main_statistical_relationships.md`; AS001-AS009=`parts/support_a_statistical_relationships.md`; BS001-BS009=`parts/support_b_statistical_relationships.md`.

## Display-zero convention

No `P=0`, `p=.000`, or equivalent display-zero occurs in the mapped main/support relationships. `P<.001` is an inequality display, not display zero; no `DISPLAY_ZERO_NOT_CANDIDATE` record is required.
