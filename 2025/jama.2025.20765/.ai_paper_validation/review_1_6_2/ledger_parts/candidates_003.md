# Current stable candidate scope

Pending Human Adjudication. Canonical ledger: ../candidate_ledger.md.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C014 | statistical_results | S_W | S_W | REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows | reproduced | CONFIRMED | F-ST1-001 |
| C015 | plan_material | P_P | P_P | PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result | reproduced | CONFIRMED | F-XS-009, F-ST1-011 |
| C016 | plan_material | P_P | P_P | PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context | reproduced | CONFIRMED | F-XS-011, F-ST1-009 |
| C017 | statistical_results | S_W | S_W | REPORT DOC-003 p.6 affected cells vs same-table death total | reproduced | CONFIRMED | F-NUM-101 |
| C018 | statistical_results | S_W | S_W | REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator | reproduced | CONFIRMED | F-NUM-102 |
| C019 | statistical_results | S_W | S_W | REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference | reproduced | CONFIRMED | F-NUM-103 |

## C014 — Fourteen interval rows do not reproduce a rule fitting other display rows

Pending Human Adjudication.

**Candidate statement:** Fourteen interval rows do not reproduce a rule fitting other display rows.

**Source-order key:** DOC-001 PDF p. 6.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 p.6 Table2 within-display rows and REPORT DOC-003 pp.12,13 respective within-display rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** The exact recheck confirms all fourteen triples and the independent calculation reproduces all fourteen relative gaps above .05. Route A category 4 applies because the same diagnostic reproduces other rows of each display within the workflow tolerance. Unreported row-specific construction remains a human question, not a reason to suppress the observed pattern.

**Finding IDs:** F-ST1-001

**Qualifying route:** Route A, category 4

**Exact source locations:**

- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2CO10PPadjusted,CO6PPcrude/adjusted,self-reportadjusted; REPORT.
- [DOC-003 — PDF p. 12](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=12>), eTable8All,age≥40,primary,secondary,active,dependent,smoking<24,readingNo; REPORT.
- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9CO10crude/adjusted; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), population/adjustmentnotes; REPORT.

**Source evidence:** All 14 affected RR/lower/upper triples and their rounded-input reconstruction ranges are preserved in the detailed numeric list below. The Table 2 adjusted self-report upper endpoint is literally 42 in the supplied source, without a decimal point. Each source row was visually confirmed.

**Calculation:** Apply U*=E²/L, with range [(E−hE)²/(L+hL),(E+hE)²/(L−hL)] versus [U−hU,U+hU], using exact displayed half-units. Every listed gap/U exceeds .05. The rule reproduces other rows of each display; it is a reconstruction diagnostic rather than a claim about an unstated Wald method. No point is outside its printed CI and no CI/P conflict is inferred.

**Affected result or extracted value:** The 14 upper CI endpoints and corresponding primary/sensitivity/subgroup uncertainty.

**Why context does not resolve it:** Route A category 4 requires inclusion when a rule reproduces other display rows but fails these rows beyond precision; unknown row-specific construction is the human question.

**Alternative source-grounded interpretations:** Profile likelihood, bootstrap, marginal-risk or other nonsymmetric intervals may explain rows; procedures may differ by row. Fitted covariance/SE and construction definitions are absent.

**Exact remaining human question:** Which estimate/interval construction produced every listed row, and are the printed limits, including 42, intended for that construction?

**Classification rationale:** Every comparison is within its own REPORT display. Combining occurrences of one rule does not create S_C. No PLAN location is a conflicting comparator; S_W/statistical_results is retained.

**Classification ambiguity:** Row-specific interval procedures are unavailable. No universal Wald or log-symmetric interval requirement is asserted.

**Checker provenance:** F-ST1-001; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.

### Detailed interval reconstruction for C014

Each line gives display/row, printed E;L;U, independently recomputed U* interval, gap, and gap/|U|. Every displayed input/output receives its own half-unit; a literal42 receives±0.5, not±0.05.

- Table2 CO10 PP adjusted: 3.1;2.1;5.2; reconstructed [4.326744,4.840244]; gap 0.309756; relative 0.059568.
- Table2 CO6 PP crude: 3.6;2.14;6.87; reconstructed [5.875291,6.240047]; gap 0.624953; relative 0.090968.
- Table2 CO6 PP adjusted: 3.8;2.3;7.7; reconstructed [5.984043,6.587778]; gap 1.062222; relative 0.137951.
- Table2 self-report adjusted: 2.8;1.9;42; reconstructed [3.878205,4.390541]; gap 37.109459; relative 0.883559.
- eTable8 All: 2.890;1.983;4.709; reconstructed [4.209332,4.214371]; gap 0.494129; relative 0.104933.
- eTable8 Age≥40: 2.953;2.048;5.092; reconstructed [4.255434,4.260397]; gap 0.831103; relative 0.163217.
- eTable8 Primary: 2.638;1.849;4.07; reconstructed [3.761236,3.766125]; gap 0.298875; relative 0.073434.
- eTable8 Secondary: 2.719;1.348;4.83; reconstructed [5.480343,5.488445]; gap 0.645343; relative 0.133611.
- eTable8 Active: 2.989;1.933;4.885; reconstructed [4.619153,4.624637]; gap 0.259863; relative 0.053196.
- eTable8 Dependent: 2.587;1.329;3.986; reconstructed [5.031954,5.039636]; gap 1.045454; relative 0.262281.
- eTable8 Smoke<24: 3.511;1.884;7.127; reconstructed [6.539459,6.546659]; gap 0.579841; relative 0.081358.
- eTable8 Reading No: 2.198;1.288;3.299; reconstructed [3.747774,3.754099]; gap 0.448274; relative 0.135882.
- eTable9 CO10 crude: 2.9;1.8;6.4; reconstructed [4.390541,4.972857]; gap 1.377143; relative 0.215179.
- eTable9 CO10 adjusted: 3.1;1.9;6.5; reconstructed [4.770513,5.363514]; gap 1.086486; relative 0.167152.

Reproducing comparators: Table 2 self-report crude 2.7 [1.8,4.1], week 9 crude 2.6 [1.8,3.9]/adjusted 2.7 [1.8,4.3], month 6 crude 2.7 [2.0,3.8]/adjusted 2.7 [1.9,4.0], and success 1.2 [.9,1.6]/1.2 [.9,1.5] have overlapping reconstruction/printed intervals. In eTable 8, age <40 gives [4.846799,4.853725] versus [4.8565,4.8575], relative gap .000571; smoking ≥24 gives [3.857124,3.862770] versus [3.9105,3.9115], relative gap .012204; no formal education and reading Yes also pass the .05 rule. In eTable 9, CO<6 3.6 [2.4,5.4]/3.8 [2.4,6.2], week 9 2.5 [1.7,3.6]/2.6 [1.7,3.8], month 6 2.58 [1.8,3.6]/2.7 [1.8,4.0], and success 1.1 [.7,1.6]/1.1 [.7,1.5] have overlapping intervals. These source-confirmed comparators establish the observed reproducing rule without asserting a universal inferential construction.



## C015 — Latest protocol and SAP prescribe different failure windows

Pending Human Adjudication.

**Candidate statement:** Latest protocol and SAP prescribe different failure windows.

**Source-order key:** DOC-002 PDF p. 9 (V6.0 header; current conflicting definition).

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.9,47,77,85; REPORT DOC-001 pp.1,3,6 identifies affected result

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route B is reproduced and meets B1 through a planned key-secondary endpoint definition, B2 because retained protocol/SAP definitions and the report do not specify their governing hierarchy, and B3 because the definition attached to the reported failure result remains unresolved.

**Finding IDs:** F-XS-009, F-ST1-011

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 9](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=9>), lines179–180 month-5 definition, explicitly headed V6.0; PLAN.
- [DOC-002 — PDF p. 47](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=47>), lines1319–1320month6definition; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2413–2415 explicit5→6amendment; PLAN.
- [DOC-002 — PDF p. 85](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=85>), lines2685–2686SAPmonth5; PLAN.
- [DOC-001 — PDF p. 1](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1>), key-secondaryfailureproportions; REPORT.
- [DOC-001 — PDF p. 3](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3>), outcomedetailpointer; REPORT.
- [DOC-001 — PDF p. 6](<../../../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6>), Table2failure1/720versus2/360; REPORT.

**Source evidence:** Protocol p.9, explicitly headed V6.0, and SAP p.85 define failure as remaining smear-positive at month 5 or later; protocol p.47 uses month 6 or later. The amendment explicitly replaces month 5 with month 6 in v6. Report prints failure 1/720 versus 2/360 without an explicit competing window.

**Calculation:** These are exact categorical endpoint windows, not rounded month measurements. The amendment reconciles historical protocol changes but not the SAP's retained month-5 rule. No patient reclassification or event-count discrepancy is inferred.

**Affected result or extracted value:** Definition attached to abstract key-secondary failure proportions0.1% and0.5%, Table2 counts1/720 and2/360, and TB programme outcome classification.

**Why context does not resolve it:** SAP and amended protocol prescribe different windows for a reported key-secondary endpoint; the report does not identify which classified its three events.

**Alternative source-grounded interpretations:** The amended month-6 rule, SAP month-5 rule or programme-register rule may govern. A finalized endpoint dictionary is absent.

**Exact remaining human question:** Were failures classified using month 5 or later or month 6 or later, and which supplied plan rule governed the three reported events?

**Classification rationale:** All conflicting thresholds are prospective PLAN content in one bundle. The report supplies no competing month threshold and therefore adds no P_R. P_P/plan_material is retained.

**Classification ambiguity:** Final endpoint dictionary and governing amendment/SAP hierarchy are absent. PDF p.9 is explicitly headed V6.0; its earlier position does not establish an earlier version.

**Checker provenance:** F-XS-009, F-ST1-011; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C016 — Current Phase3 power statements retain different cluster allocations

Pending Human Adjudication.

**Candidate statement:** Current Phase3 power statements retain different cluster allocations.

**Source-order key:** DOC-002 PDF p. 48.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN DOC-002 pp.48,63,65,77,83; PLAN p.64 peripheral Phase4context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route B is reproduced and satisfies B1 for primary trial power/allocation inputs, B2 because the current repeated paragraph is not explicitly historical or a distinct calculation, and B3 for allocation assumptions attached to the1080-participant/27-cluster primary design. The qualifying relative gap is .0625 for the intervention-arm input.

**Finding IDs:** F-XS-011, F-ST1-009

**Qualifying route:** Route B

**Exact source locations:**

- [DOC-002 — PDF p. 48](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=48>), lines1348–1353poweroverview; PLAN.
- [DOC-002 — PDF p. 63](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=63>), lines1886–1907Phase3power/allocation; PLAN.
- [DOC-002 — PDF p. 64](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=64>), Phase4allocationcontext; PLAN.
- [DOC-002 — PDF p. 65](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=65>), lines1958–1963repeatedpowerparagraph; PLAN.
- [DOC-002 — PDF p. 77](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=77>), lines2416–2424allocationamendment; PLAN.
- [DOC-002 — PDF p. 83](<../../../joi250093supp1_prod_1768590553.08963.pdf#page=83>), lines2629–2642SAPallocation; PLAN.

**Source evidence:** Current overview/detail/SAP give Phase 3 18 intervention and 9 control clusters, total 27, 90% power at 5%, 18%/8% abstinence. The repeated current protocol paragraph gives 16 and 8 with the same power/rates. The amendment changes 16/8 to 18/9. Its Phase 4 20/20 versus other 18/18 is unreported-phase peripheral context.

**Calculation:** 18±.5 versus 16±.5 yields gap 1/16=.0625. Independently rounded arm sums give [26,28] versus [23,25], gap 1/24=.041667, which does not independently qualify; 9-versus-8 intervals touch. The intervention-arm power input supplies the reproduced basis.

**Affected result or extracted value:** Phase 3 allocation and power inputs underlying the 1080-participant,27-cluster primary trial.

**Why context does not resolve it:** The repeated current paragraph attaches the same power/rates to 16/8 without labeling it historical; this changes a primary analysis-population/power input rather than an administrative site copy.

**Alternative source-grounded interpretations:** The repeated paragraph may carry forward earlier text, or both allocations may have been evaluated without being distinguished. The governing final power calculation is absent.

**Exact remaining human question:** Which Phase 3 allocation and power calculation governs, and should the current 16/8 paragraph be read as historical?

**Classification rationale:** Conflicting power inputs are solely PLAN content. The observed27-cluster trial corroborates one specification without adding P_R. P_P/plan_material is retained.

**Classification ambiguity:** The amendment discloses the change; p.65 may retain historical text without naming it. Separate unreported Phase4 inputs remain peripheral context.

**Checker provenance:** F-XS-011, F-ST1-009; checkers/cross_source_consistency.md; checkers/statistical_pass_1.md; independent decision in screening/inclusion_screen.md.



## C017 — Two cause-of-death percentages do not reconcile within eTable4

Pending Human Adjudication.

**Candidate statement:** Two cause-of-death percentages do not reconcile within eTable4.

**Source-order key:** DOC-003 PDF p. 6.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.6 affected cells vs same-table death total

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category3 applies to each source-confirmed count/denominator/percentage cell. Both half-unit reconstructions leave relative gap .228327>.05. Recovering a likely percentage does not remove the printed reading; both occurrences belong to one pattern.

**Finding IDs:** F-NUM-101

**Qualifying route:** Route A, category 3

**Exact source locations:**

- [DOC-003 — PDF p. 6](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=6>), eTable4usual-careDruguser,Severepneumonia,Totaldeaths; REPORT.

**Source evidence:** eTable 4 usual-care Drug user and Severe pneumonia each print 1(7.4%), with Total deaths 27. Overall affected counts are 1 and mHealth 0. Stroke 2(7.4%) and fall 1(3.7%) support the common denominator; all cause counts sum 27.

**Calculation:** 100×1/27=3.703704%. Required rounded range 100×[.5/27.5,1.5/26.5]=[1.818182,5.660377]% versus [7.35,7.45]% gives gap 1.689623/7.4=.228327. Both cells fail the same within-display rule and form one issue.

**Affected result or extracted value:** Usual-care death-cause percentages associated with drug use and severe pneumonia.

**Why context does not resolve it:** Route A category 3 applies to co-located count/denominator/percentage inconsistency; recoverable percentage values do not remove the printed 7.4% readings.

**Alternative source-grounded interpretations:** 7.4% could represent two deaths or another denominator; sums corroborate one death but do not assign a correction. No cause-specific denominator is given.

**Exact remaining human question:** What counts, denominators and percentages should be used for the two affected usual-care cause rows?

**Classification rationale:** Counts, percentages and death total are REPORT results in one table; S_W/statistical_results is retained.

**Classification ambiguity:** None.

**Checker provenance:** F-NUM-101; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.



## C018 — Site2008 death count and percentage do not reproduce the table denominator

Pending Human Adjudication.

**Candidate statement:** Site2008 death count and percentage do not reproduce the table denominator.

**Source-order key:** DOC-003 PDF p. 9.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.9 site2008 vs same-table count/percentage pattern; REPORT DOC-003 p.8 corroborates denominator

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category4 independently supports inclusion: the same-display N40 rule reproduces the other death cells and leaves relative gap .474815 for this cell. N40 is supported inference, not an explicit eTable6 denominator column. Category3 describes the related count/percentage framing, but category4 is the clearest primary qualifying route.

**Finding IDs:** F-NUM-102

**Qualifying route:** Route A, category 4

**Exact source locations:**

- [DOC-003 — PDF p. 9](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=9>), eTable6Controlsite2008cell5(7.5),otherdeathrows; REPORT.
- [DOC-003 — PDF p. 8](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=8>), eTable5site2008recruitmentandITT40,observed35; REPORT.

**Source evidence:** eTable 6 Control site 2008 prints 5(7.5). All other death rows use N=40, including 3(7.5),4(10.0),site2012 5(12.5). eTable 5 prints recruitment/ITT population 40 and observed contributors 35 for site 2008.

**Calculation:** 100×5/40=12.5%. Rounded range 100×[4.5/40.5,5.5/39.5]=[11.111111,13.924051]% versus [7.45,7.55]% gives gap 3.561111/7.5=.474815. N40 rule reproduces other death cells.

**Affected result or extracted value:** Site 2008 cluster mortality count/percentage.

**Why context does not resolve it:** Route A category 4 applies because the same-display denominator rule reproduces the other rows and fails this row beyond0.05. The N40 rule is inferred from the display and corroborated onp8; eTable6 has no explicit denominator column. Co-located counts also support category3 framing, rather than a peripheral copy comparison.

**Alternative source-grounded interpretations:** 7.5% represents three of40, while five of40 is12.5%; another denominator would require definition. Counts sum overall52/usual-care27/mHealth25, corroborating counts without assigning a correction.

**Exact remaining human question:** What death count, denominator and percentage governs site 2008 in eTable 6?

**Classification rationale:** The affected cell and reproducing row pattern are in one REPORT table. The site population corroborator is in the same REPORT document; S_W/statistical_results is retained.

**Classification ambiguity:** eTable6 has no separate N column. N40 is inferred from the complete same-display pattern and corroborated by eTable5 recruitment/ITT population; a distinct mortality denominator is undefined.

**Checker provenance:** F-NUM-102; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.



## C019 — Treatment-failure absolute difference has the opposite signed contrast

Pending Human Adjudication.

**Candidate statement:** Treatment-failure absolute difference has the opposite signed contrast.

**Source-order key:** DOC-003 PDF p. 13.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-003 p.13 treatment-failure cell vs same-display arm risks and common contrast; p.14 defines difference

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Inclusion audit reason:** Route A category2 applies to the source-confirmed sign comparison under the common display contrast, whose relative gap is1.367585. The unsigned-magnitude or row-specific reference alternative remains explicit; it is not assumed away.

**Finding IDs:** F-NUM-103

**Qualifying route:** Route A, category 2

**Exact source locations:**

- [DOC-003 — PDF p. 13](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=13>), eTable9TreatmentFailuresabsolute-difference0.5andarmrisks; REPORT.
- [DOC-003 — PDF p. 14](<../../../joi250093supp2_prod_1768590553.09463.pdf#page=14>), notebAbsolute difference; REPORT.

**Source evidence:** eTable 9 failure risks are mHealth 1/695,0.1%[0.01,0.8], versus usual-care 2/333,0.6%[0.1,2.2]. Absolute difference prints +0.5[-0.4,1.3]. Other rows use mHealth-minus-usual-care:43.2−16.5=26.7;38.0−11.4=26.6;50.8−22.5=28.3;57.5−24.6=32.9;3.2−2.1=1.1; success difference0.

**Calculation:** 100×(1/695−2/333)=−.456716 percentage points. Rounded count/denominator range [−.679989,−.233792] versus [.45,.55] gives gap .683792/.5=1.367585. Printed arm risks independently allow [−.60,−.40], remaining negative.

**Affected result or extracted value:** Signed failure risk difference in the excluding-deaths sensitivity.

**Why context does not resolve it:** Route A category 2 applies to a sign reversing the common displayed contrast; the word Absolute is an alternative interpretation rather than removal of the direction mismatch.

**Alternative source-grounded interpretations:** This row may use unsigned magnitude, reversed reference group or another model-based contrast; no row-specific switch is named. The signed interval and other rows remain printed. No CI construction is inferred.

**Exact remaining human question:** Does Treatment Failures use mHealth-minus-usual-care, and what signed difference and matching interval should be extracted?

**Classification rationale:** Arm risks, point difference, comparator rows and note are within one REPORT document; S_W/statistical_results is retained.

**Classification ambiguity:** “Absolute difference” could denote an unsigned magnitude, a row-specific reverse reference or another contrast. No explicit signed reference or row-specific switch is printed.

**Checker provenance:** F-NUM-103; checkers/numeric_consistency.md; independent decision in screening/inclusion_screen.md.

