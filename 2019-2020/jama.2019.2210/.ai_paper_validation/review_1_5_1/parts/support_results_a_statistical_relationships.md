# DOC-003 Results Supplement, Shard A: Statistical Relationship Inventory

Provisional statistical keys are local to this shard. Locations refer to `joi190023supp2_prod.pdf` PDF pages. All reported intervals are printed as 95% CIs. These records map reported inferential relationships and do not diagnose candidates.

## Average 25(OH)D Cox model (eTable 1)

Reference stratum is <20 ng/mL. `HR` lines and `AHR` lines are distinct reported models; the sole printed adjustment is vitamin D supplementation. Match base: `AVG25OHD|OUTCOME|STRATUM|MODEL`.

| Provisional key | p. | Outcome; stratum; model | HR (95% CI); P |
|---|---:|---|---|
| AS001 | 4 | Relapse/death; 20-<30 ng/mL; HR | 0.62 (0.37 to 1.02); .06 |
| AS002 | 4 | Relapse/death; 20-<30; AHR | 0.61 (0.37 to 1.01); .05 |
| AS003 | 4 | All-cause death; 20-<30; HR | 0.66 (0.35 to 1.24); .20 |
| AS004 | 4 | All-cause death; 20-<30; AHR | 0.64 (0.34 to 1.20); .16 |
| AS005 | 4 | Relapse/death; 30-<40; HR | 0.47 (0.27 to 0.84); .01 |
| AS006 | 4 | Relapse/death; 30-<40; AHR | 0.44 (0.24 to 0.82); .009 |
| AS007 | 4 | All-cause death; 30-<40; HR | 0.39 (0.18 to 0.84); .02 |
| AS008 | 4 | All-cause death; 30-<40; AHR | 0.33 (0.15 to 0.74); .007 |
| AS009 | 4 | Relapse/death; 40-<50; HR | 0.29 (0.11 to 0.74); .01 |
| AS010 | 4 | Relapse/death; 40-<50; AHR | 0.26 (0.10 to 0.71); .008 |
| AS011 | 4 | All-cause death; 40-<50; HR | 0.44 (0.17 to 1.16); .10 |
| AS012 | 4 | All-cause death; 40-<50; AHR | 0.34 (0.12 to 0.96); .04 |
| AS013 | 4 | Relapse/death; >=50; HR | 0.44 (0.21 to 0.96); .04 |
| AS014 | 4 | Relapse/death; >=50; AHR | 0.40 (0.18 to 0.92); .03 |
| AS015 | 4 | All-cause death; >=50; HR | 0.55 (0.24 to 1.29); .17 |
| AS016 | 4 | All-cause death; >=50; AHR | 0.43 (0.17 to 1.08); .07 |

## Baseline 25(OH)D multiple-imputation Cox model (eTable 2)

Match base: `BASELINE25OHD|OUTCOME|STRATUM|MULTIPLE_IMPUTATION`. The table prints HR rather than adjusted-HR and gives no additional model-adjustment label.

| Provisional key | p. | Outcome; baseline stratum | HR (95% CI); P |
|---|---:|---|---|
| AS017 | 6 | Relapse/death; 0-<20 ng/mL | 1.15 (0.65 to 2.05); .63 |
| AS018 | 6 | Relapse/death; 20-40 ng/mL | 0.46 (0.24 to 0.86); .02 |
| AS019 | 6 | All-cause death; 0-<20 ng/mL | 1.36 (0.66 to 2.81); .41 |
| AS020 | 6 | All-cause death; 20-40 ng/mL | 0.60 (0.28 to 1.30); .20 |

## eFigure 1 post hoc curve annotations

These chart annotations match eTable 1 unadjusted HR results for the respective outcome/stratum, but eTable 1 calls its comparison stratum <20 ng/mL whereas the chart title abbreviates it as `~20 ng/mL`.

| Provisional key | p. | Outcome; comparison | HR (95% CI); P | Main-paper matching key |
|---|---:|---|---|---|
| AS021 | 2 | Relapse/death; ~20 vs 40-50 ng/mL | 0.29 (0.11 to 0.74); .01 | `AVG25OHD_POSTHOC|RELAPSE_DEATH|40_50_VS_LT20|UNADJUSTED_HR` |
| AS022 | 3 | All-cause death; ~20 vs 30-40 ng/mL | 0.39 (0.18 to 0.84); .02 | `AVG25OHD_POSTHOC|ALL_CAUSE_DEATH|30_40_VS_LT20|UNADJUSTED_HR` |

## Prespecified SNP-subgroup curve annotations (eFigure 3A-O)

Every panel is a relapse/death cumulative-hazard comparison of vitamin D versus placebo in the named polymorphism subgroup. The panel prints a treatment HR, 95% CI, two-sidedness/test/model/adjustment not stated, P, and P interaction. Match base: `SNP|GENOTYPE|RELAPSE_DEATH|VITAMIND_VS_PLACEBO`.

| Provisional key | p. | Subgroup | HR (95% CI); P | P interaction |
|---|---:|---|---|---|
| AS023 | 7 | FokI CC | 0.65 (0.34 to 1.26); .20 | .65 |
| AS024 | 8 | FokI CT | 0.77 (0.42 to 1.43); .41 | .90 |
| AS025 | 9 | FokI TT | 0.97 (0.32 to 2.88); .95 | .67 |
| AS026 | 10 | BsmI AA | 0.44 (0.03 to 7.16); .56 | .66 |
| AS027 | 11 | BsmI AG | 0.60 (0.24 to 1.48); .27 | .50 |
| AS028 | 12 | BsmI GG | 0.86 (0.52 to 1.41); .55 | .38 |
| AS029 | 13 | CDK2 GG | 0.69 (0.34 to 1.38); .29 | .64 |
| AS030 | 14 | CDK2 GA | 0.72 (0.39 to 1.32); .28 | .63 |
| AS031 | 15 | CDK2 AA | 1.82 (0.48 to 6.88); .38 | .19 |
| AS032 | 16 | ApaI GG | 1.00 (0.49 to 2.05); .99 | .35 |
| AS033 | 17 | ApaI GT | 0.70 (0.38 to 1.27); .24 | .63 |
| AS034 | 18 | ApaI TT | 0.53 (0.15 to 1.84); .32 | .49 |
| AS035 | 19 | TaqI TT | 0.87 (0.52 to 1.46); .60 | .35 |
| AS036 | 20 | TaqI TC | 0.49 (0.22 to 1.10); .08 | .20 |
| AS037 | 21 | TaqI CC | HR/CI not estimable: printed `-` (`- to -`); P=1.00 | `-` |

## Source-linked duplicate match records

eFigure 1A annotation (AS021) and eTable 1 relapse/death 40-<50 unadjusted HR (AS009) print the identical HR, CI, and P. eFigure 1B annotation (AS022) and eTable 1 all-cause-death 30-<40 unadjusted HR (AS007) print the identical HR, CI, and P. They are matched repeated presentations of the same result and should be cross-referenced rather than treated as independent estimates in a merged inventory.
