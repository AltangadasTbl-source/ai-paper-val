# Stable Candidate Ledger

All records below are quality-control candidates and remain **Pending Human Adjudication**. Genuine duplicate discoveries from the numeric, cross-source, and statistical lanes were merged before these stable IDs were assigned. No candidate was deleted, capped, ranked, or adjudicated.

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint differs between Table 2 and narrative

- **Category:** Statistical reporting inconsistency
- **Provenance:** S009; SP1-001.
- **Exact source locations:** DOC-001, `jama_huffman_2018_oi_170166.pdf`, PDF p. 6, Table 2 and adjacent Results narrative.
- **Printed evidence:** Table 2 reports adjusted risk difference 6.25% (95% CI, 4.10% to 8.40%) and OR 1.46 (1.29 to 1.65). The narrative reports the same named in-hospital beta-blocker comparison as 6.25% (95% CI, 4.10% to 8.10%) and OR 1.46 (1.29 to 1.65).
- **Consistency rule and calculation:** A same-model, same-contrast repetition should preserve the same CI endpoints. The printed upper endpoints differ by 0.30 percentage point (8.40 minus 8.10).
- **Direct observation versus inference:** The differing printed endpoints are direct observations. Treating the two occurrences as the same adjusted result is supported by the identical outcome, point estimate, lower endpoint, OR, and OR interval; the source does not identify a second model.
- **Alternative source-grounded interpretation:** One occurrence may be a transcription error or may use an unlabelled distinct output; the package does not establish which value is supported by the analysis output.
- **Exact human question:** Which upper confidence-limit endpoint is supported for the adjusted in-hospital beta-blocker risk difference?
- **Status:** Pending Human Adjudication

## C002 — Discharge beta-blocker adjusted point estimates differ between Table 2 and narrative

- **Category:** Cross-document numeric inconsistency
- **Provenance:** N036; S052; NC-001; XC-001; SP1-002.
- **Exact source locations:** DOC-001, `jama_huffman_2018_oi_170166.pdf`, PDF p. 6, Table 2; PDF p. 7, Results narrative.
- **Printed evidence:** Table 2 reports adjusted risk difference 6.69% (95% CI, 4.43% to 8.95%) and OR 1.48 (1.30 to 1.68). The narrative reports 6.63% with the same risk-difference interval and OR 1.47 with the same OR interval.
- **Consistency rule and calculation:** A same-outcome, same-contrast, same-model repetition should preserve point estimates at displayed precision unless a different analysis is named. The risk differences differ by 0.06 percentage point and the ORs by 0.01, while both printed intervals are identical.
- **Direct observation versus inference:** The two printed estimate pairs and identical intervals are direct observations. Their identity as the same adjusted result is inferred from the named discharge outcome, intervention-versus-control contrast, and unchanged intervals.
- **Alternative source-grounded interpretation:** Unreported higher-precision or distinct model output could explain the values; no such distinction is supplied.
- **Exact human question:** Do both locations report the same adjusted analysis and, if so, which risk difference and OR should be retained?
- **Status:** Pending Human Adjudication

## C003 — eTable 1 difference footnote names groups not displayed in the table

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** N308; S305; NC-002; XC-002; SP1-003.
- **Exact source locations:** DOC-004, `joi170166supp3_prod.pdf`, PDF p. 17, eTable 1 title, headers, values, and footnote a.
- **Printed evidence:** eTable 1 is titled for complete versus missing follow-up and displays columns `Complete Follow Up` (n=21,079) and `Missing Follow Up` (n=295), followed by `Difference (95% CI)`. Footnote a states `Difference = intervention minus control.` For age, the printed difference -0.6 equals 60.0 minus 60.6, the displayed missing-minus-complete contrast.
- **Consistency rule and calculation:** A difference footnote should name the groups actually compared. The displayed columns contain follow-up-status groups, not intervention/control groups; 60.0 - 60.6 = -0.6.
- **Direct observation versus inference:** The headers, footnote, and age arithmetic are direct. A carried-over footnote is a possible explanation, not an established cause.
- **Alternative source-grounded interpretation:** The footnote may have been copied from eTable 2, but the supplied package does not explicitly define the eTable 1 sign convention for every row.
- **Exact human question:** What comparator order and sign convention were used for the eTable 1 differences?
- **Status:** Pending Human Adjudication

## C004 — Reported prespecified age-subgroup boundaries differ from the supplied SAP

- **Category:** Cross-document numeric inconsistency
- **Provenance:** S303; S038; S039; S040; XC-003; SP1-004.
- **Exact source locations:** DOC-003, `joi170166supp2_prod.pdf`, PDF p. 7, section 7.5.2; DOC-001, `jama_huffman_2018_oi_170166.pdf`, PDF p. 3, statistical-analysis description, and PDF p. 9, Figure 3.
- **Printed evidence:** The supplied SAP lists the a priori participant-level age subgroup as younger than 65 years versus older than 65 years. The article states that results were reported by prespecified subgroups, while Figure 3 displays age groups younger than 50, 50-69, and 70 years or older.
- **Consistency rule and calculation:** A numeric subgroup definition described as prespecified should match the supplied prespecification or identify a documented amendment. The supplied boundaries change from a two-group boundary at 65 years to three groups bounded at 50 and 70 years.
- **Direct observation versus inference:** The two printed sets of cut points and the article's prespecified label are direct observations. Whether an unprovided amendment exists is unknown.
- **Alternative source-grounded interpretation:** A separate or amended analysis plan could have authorized the displayed categories, but none is included in the package.
- **Exact human question:** Were the Figure 3 age categories prespecified in a supplied or unsupplied amendment, and what definition should the prespecified label reference?
- **Status:** Pending Human Adjudication

## C005 — The named optimal in-hospital medication composite uses different component labels across final-result tables

- **Category:** Measure, label, or scale inconsistency
- **Provenance:** S033; S307; S308; SP1-005.
- **Exact source locations:** DOC-001, `jama_huffman_2018_oi_170166.pdf`, PDF p. 3 and PDF p. 7, Table 3 footnote c; DOC-004, `joi170166supp3_prod.pdf`, PDF p. 21, eTable 5 footnote c, and PDF p. 22, eTable 6 footnote b.
- **Printed evidence:** The main article and eTable 5 define optimal in-hospital medication with aspirin, an ADP-receptor antagonist, an anticoagulant, and a beta-blocker. eTable 6 uses the same composite name but lists aspirin, an ADP-receptor antagonist, heparin, and a beta-blocker.
- **Consistency rule and calculation:** A repeated named composite should retain the same component definition or explicitly distinguish a narrower construct. The printed component substitution is `anticoagulant` versus `heparin`.
- **Direct observation versus inference:** The component wording is directly printed. Whether heparin was the only anticoagulant in the analyzed data is not supplied.
- **Alternative source-grounded interpretation:** If heparin was the only qualifying anticoagulant, the terms could be extensionally equivalent; the package does not establish that fact.
- **Exact human question:** Did eTable 6 analyze the same medication composite as Table 3 and eTable 5, and what exact anticoagulant component definition was used?
- **Status:** Pending Human Adjudication

## C006 — Hospital-type subgroup is reported as prespecified but is absent from the supplied SAP subgroup list

- **Category:** Cross-document numeric inconsistency
- **Provenance:** S049; S050; S051; S303; SP2-001.
- **Exact source locations:** DOC-001, `jama_huffman_2018_oi_170166.pdf`, PDF p. 3, Statistical Analysis, and PDF p. 9, Figure 3 and adjacent Results narrative; DOC-003, `joi170166supp2_prod.pdf`, PDF p. 7, section 7.5.2.
- **Printed evidence:** The article says results are reported by prespecified subgroups including hospital type, and Figure 3 displays government (9 hospitals), nonprofit (12), and private (42). The supplied SAP lists site-level subgroups as hospital size and use of quality-improvement toolkit components; it does not list hospital type.
- **Consistency rule and calculation:** A final subgroup labelled prespecified should appear in the supplied prespecification or a supplied amendment. The article's list includes the three-category hospital-type subgroup, whereas the supplied SAP list includes toolkit-component use and does not name hospital type; this is a categorical definition comparison rather than rounding arithmetic.
- **Direct observation versus inference:** The article's prespecified label, its three hospital-type categories, and the SAP list are direct observations. Whether a later unprovided amendment added hospital type is unknown.
- **Alternative source-grounded interpretation:** A separate or amended plan could have authorized hospital type, but no such document is included in the package.
- **Exact human question:** Was hospital type prespecified in an amendment or separate plan, and how should the article's prespecified label relate to the subgroup list supplied here?
- **Status:** Pending Human Adjudication
