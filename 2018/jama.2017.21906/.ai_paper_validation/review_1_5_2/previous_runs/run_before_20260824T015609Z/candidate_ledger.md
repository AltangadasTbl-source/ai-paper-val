# Stable Candidate Ledger

All five distinct source-grounded consistency candidates remain **Pending Human Adjudication**. Duplicate proposals were merged only when they concerned the same printed values, comparator, and rule. Stable IDs will not be deleted, merged, or renumbered.

## Duplicate-merge record

- Numeric NCP-001, cross-source CP-01, and statistical P1-S008-01 were merged as C001.
- Cross-source CP-02 and statistical P1-S021-01 were merged as C002.
- Numeric NCP-002, cross-source CP-03, and statistical P1-S507-01 were merged as C003.
- Cross-source CP-04 remained distinct as C004.
- Cross-source CP-05 and statistical P1-S505-01 were merged as C005.

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint mismatch

- **Category:** Cross-document numeric inconsistency
- **Relationships/provenance:** N024; S008; numeric, cross-source, and statistical-pass-1 proposals.
- **Exact source locations:** [Main article Table 2 — PDF p. 6](../../jama_huffman_2018_oi_170166.pdf#page=6); [main article Results narrative — PDF p. 7](../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Direct source evidence:** Table 2 prints adjusted risk difference `6.25 (4.10 to 8.40)`; the matched narrative prints `6.25% [95% CI, 4.10%-8.10%]`. OR `1.46 (1.29-1.65)` matches in both locations.
- **Comparator and rule:** Same eligible population, intervention-control contrast, adjusted measure, point estimate, lower endpoint, and OR imply a matched result. The upper endpoints differ by `8.40 - 8.10 = 0.30` percentage points, exceeding two-decimal rounding tolerance.
- **Alternative source-grounded interpretations:** Either occurrence may be a transcription/typesetting error, or an unstated distinct analysis may exist; supplied locations identify no different population, adjustment set, time point, or estimand.
- **Remaining human question:** Which upper 95% CI endpoint is authoritative for this result?
- **Status:** Pending Human Adjudication.

## C002 — Discharge beta-blocker adjusted point estimates mismatch

- **Category:** Cross-document numeric inconsistency
- **Relationships/provenance:** S021; cross-source and statistical-pass-1 proposals.
- **Exact source locations:** [Main article Table 2 — PDF p. 6](../../jama_huffman_2018_oi_170166.pdf#page=6); [main article Results narrative — PDF p. 7](../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Direct source evidence:** Table 2 prints adjusted risk difference `6.69 (4.43 to 8.95)` and OR `1.48 (1.30-1.68)`; the matched narrative prints `6.63% [4.43%-8.95%]` and OR `1.47 [1.30-1.68]`.
- **Comparator and rule:** The named population, contrast, adjusted analysis, and interval endpoints match, while RD differs by `0.06` percentage points and OR by `0.01` at the printed precision.
- **Alternative source-grounded interpretations:** One occurrence may be a transcription/rounding issue or each may derive from a different analysis run, but no different model or population is printed.
- **Remaining human question:** Which RD and OR point estimates belong to the finalized discharge beta-blocker analysis?
- **Status:** Pending Human Adjudication.

## C003 — eTable 1 difference footnote conflicts with the displayed comparison groups

- **Category:** Measure, label, or scale inconsistency
- **Relationships/provenance:** N517; S507; numeric, cross-source, and statistical-pass-1 proposals.
- **Exact source locations:** [Supplement 3 eTable 1 — PDF p. 17](../../joi170166supp3_prod.pdf#page=17); [main article missing-follow-up narrative — PDF p. 6](../../jama_huffman_2018_oi_170166.pdf#page=6).
- **Direct source evidence:** Columns are `Complete Follow Up n=21,079` and `Missing Follow Up n=295`, but footnote a says `Difference = intervention minus control`. Printed examples follow missing minus complete: age `60.0-60.6=-0.6`, male `71.2%-75.8%=-4.6%`, tobacco `42.4%-30.8%=11.6%`.
- **Comparator and rule:** A difference footnote must name the displayed comparator populations. Complete/missing follow-up and intervention/control are distinct package-defined partitions.
- **Alternative source-grounded interpretations:** The footnote may be copied from eTable 2; alternatively the table heading could be wrong, but the printed arithmetic supports missing-minus-complete.
- **Remaining human question:** Should footnote a identify `missing follow-up minus complete follow-up`, or was another comparison intended?
- **Status:** Pending Human Adjudication.

## C004 — SAP and article use different component sets under the same outcome name

- **Category:** Measure, label, or scale inconsistency
- **Relationships/provenance:** N026, N027, S032, and cross-source CP-04; planned/reported measure-definition relationship.
- **Exact source locations:** [SAP secondary endpoint — PDF p. 5](../../joi170166supp2_prod.pdf#page=5); [main article outcome definition — PDF p. 3](../../jama_huffman_2018_oi_170166.pdf#page=3); [main article Table 3 footnote — PDF p. 7](../../jama_huffman_2018_oi_170166.pdf#page=7).
- **Direct source evidence:** The SAP defines `optimal in-hospital medication use` as aspirin, ADP-receptor antagonist, heparin, statin, and beta blocker. The article uses the same outcome label for aspirin, ADP-receptor antagonist, anticoagulant, and beta blocker; it states in-hospital statin use was predefined but not collected. Table 3 reports 31.7% control and 35.8% intervention under the four-component definition.
- **Comparator and rule:** The supplied SAP and article use the same outcome name for different printed component sets. The article directly defines its four-component measure and explains why statin is absent; the package supplies no amendment or change-control record linking that definition to the five-component SAP measure.
- **Alternative source-grounded interpretations:** This may be an operational deviation transparently explained by absent statin data, and a nonsupplied amendment may authorize the modified composite.
- **Remaining human question:** Was the component-set change formally prespecified or amended, and when did the four-component definition replace the SAP definition?
- **Status:** Pending Human Adjudication.

## C005 — Published prespecified age strata do not match the supplied SAP

- **Category:** Measure, label, or scale inconsistency
- **Relationships/provenance:** S505 with S037-S039; cross-source and statistical-pass-1 proposals.
- **Exact source locations:** [SAP subgroup analyses — PDF p. 7](../../joi170166supp2_prod.pdf#page=7); [main article Methods — PDF p. 3](../../jama_huffman_2018_oi_170166.pdf#page=3); [main article Figure 3 — PDF p. 9](../../jama_huffman_2018_oi_170166.pdf#page=9).
- **Direct source evidence:** The SAP specifies age `<65 years and >65 years`. Figure 3 is titled as `Prespecified Subgroups` but displays `<50`, `50-69`, and `≥70` years; the article narrative also calls the subgroups prespecified.
- **Comparator and rule:** An exact subgroup display labelled prespecified should map to the supplied prespecified categories. A two-category 65-year split does not map to the three displayed 50/70-year strata.
- **Alternative source-grounded interpretations:** A later amendment or separate prespecification may exist, or the article may use “prespecified” at a broader category level; no supplied source documents that mapping.
- **Remaining human question:** Were the 50/70-year categories prespecified in an amendment or other supplied-to-authors analysis record?
- **Status:** Pending Human Adjudication.
