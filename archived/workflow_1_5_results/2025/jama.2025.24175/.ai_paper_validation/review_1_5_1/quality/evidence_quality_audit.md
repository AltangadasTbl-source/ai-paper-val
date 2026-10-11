# Evidence-Quality Audit

## Audit outcome

- **Candidate coverage:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, and C014 audited (14/14). Every ID remains **Pending Human Adjudication**.
- **Direct-source coverage:** The five direct PDFs contain 167 pages. The source ledger closes every row: 61 reusable pages plus 106 fresh-required pages equals 167 total pages, and 167 pages are mapped. DOC-001 is 12+0=12, DOC-002 is 0+72=72, DOC-003 is 49+5=54, DOC-004 is 0+28=28, and DOC-005 is 0+1=1.
- **Integrity:** `sha256sum -c` reproduced all five hashes in `source_hashes_before.sha256` and all 232 hashes in `reused_artifact_hashes_before.sha256`; no direct source or reused evidence asset changed during the review window checked by this audit.
- **Relationship coverage:** N001-N125 and S001-S051 are present. Numeric review reports 125/125; cross-source review reports 125/125 numeric and 51/51 statistical relationships; each statistical relationship has a `PASS_1_COMPLETE` and `PASS_2_COMPLETE` record. Statistical pass 2 reports no appended proposal.
- **Discovery boundary:** The current artifacts document fresh discovery from source-linked mappings, not an old candidate set. The inventory expressly omits old checker/candidate/report material as scientific input; the 125 numeric relationships, 51 statistical relationships, and 14 stable candidates demonstrate that discovery did not stop at 10. This audit found no top-N, queue, or early-stop mechanism in the current 1.5.1 artifacts.
- **Stable-ID parity:** The candidate ledger and mechanical recheck each contain exactly C001-C014. This quality artifact contains the same 14 IDs. No ID is removed, renumbered, combined, ranked, or suppressed.
- **Statistical-agent requirement:** `/root/statistics_pass_1` and `/root/statistics_pass_2` are distinct runtime IDs. Both are recorded as fresh `gpt-5.6-terra` agents at high reasoning effort with one primary artifact each.
- **Display-zero rule:** No stable card is based on `P = 0`, `p = 0.000`, or equivalent notation. Threshold displays such as `P<.0001` and `P=<.001` were treated as finite-precision notation. None requires the conditional independent-contradiction field reserved for a card that actually mentions a display zero.
- **Neutrality and impact boundary:** The supported records are reporting-consistency observations. No supplied evidence establishes a paper-level conclusion change. Any downstream statement must be conditional and limited to the particular count, denominator, effect measure, interval, site descriptor, or subgroup output a data extractor could copy if the observation is substantiated.
- **Human fields:** Every final-report card must retain the five required human-adjudication subfields with the exact blank value `__`. The final report did not yet exist at this audit point, so this is a required report-assembly check.

## Coverage- and artifact-level repair requirements

1. `coverage_manifest.md` still marks the checker, registration, recheck, second statistical pass, evidence-quality, and report rows `PENDING`. Completed rows must be closed. Candidate-stage scopes must spell out C001 through C014 individually, and each statistical-pass scope must spell out S001 through S051 individually; ranges are not sufficient. Each current row contains one plain relative artifact path. The quality path now resolves; the report path awaits report assembly.
2. `candidate_ledger.md` uses `### Cxxx` headings. The contract requires `## Cxxx` for every stable card.
3. Source links in `candidate_ledger.md` use `../../../<source>.pdf#page=N`. From the ledger's directory these resolve one level above the package and are broken. They must be `../../<source>.pdf#page=N`. The same `../../../` form is correct in `verification/evidence_recheck.md` and this quality file because both are one directory deeper. All recheck source paths resolve, and all cited page numbers fall within the source PDF page counts.
4. The source recheck supersedes incorrect direct-source transcriptions still present in `parts/mapping/doc002_pp001_032.md`, `checkers/numeric_consistency.md`, and `checkers/cross_source_consistency.md`: the supplied PDF prints 100 micrograms rather than 20, a 1.4-point cutoff rather than 1.5 for the matched responder definition, 5000 rather than 8000 for entry classification, 117 rather than 112 participants per arm, and 24 rather than 28 ImmunoSep sites. The 8000 threshold belongs to reversal. The historical mortality sentence is on p. 41 and is arithmetically coherent; the alleged p. 42 pairing is absent. Dependent relationship and checker narratives must be repaired without changing any C ID.
5. The evidence manifest records every spawned agent known at this audit point exactly once, including the coordinator and two statistical agents. Any later report or repair agent must be added once with its primary artifact, and the token ledger must mirror the completed execution manifest.

## C001 — Day-15 SOFA numerator across Table 2 and narrative

- **State:** Pending Human Adjudication.
- **Category alignment:** Cross-document numeric inconsistency.
- **Evidence and links:** [DOC-001 Table 2, PDF p. 6](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=6>) and [DOC-001 narrative, PDF p. 7](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=7>) resolve to the direct source.
- **Support quality:** Directly reproduced. Table 2 prints 52/131 (39.7%); narrative prints 51/131 (39.7%) for the same named endpoint and denominator. `52/131=39.6947%` rounds to 39.7%, while `51/131=38.9313%` rounds to 38.9%. The Table-2 counts reproduce the displayed crude OR at approximately 2.15.
- **Direct versus inferred:** The two numerators and shared percentage are direct. A transcription error or an unstated analysis-set distinction is inferred; the package does not select the authoritative numerator.
- **Recheck consistency and overlap:** The recheck reproduces the source facts and calculation. Multiple checker proposals concerned the same comparator/rule and were properly consolidated before stable IDs; no remaining duplicate card was identified.
- **Required report wording:** State that the two printed occurrences do not reconcile and ask which numerator is authoritative. Do not state that 52 is necessarily the correct numerator. Limit possible downstream copying to this day-15 binary-outcome count, percentage, and dependent effect outputs.

## C002 — IFN-gamma dose registration

- **State:** Pending Human Adjudication.
- **Category alignment:** The ledger retains Measure, label, or scale inconsistency for traceability, but the supplied PDFs do not establish a dose inconsistency.
- **Evidence and links:** [DOC-002 protocol dose, PDF p. 6](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=6>) and [DOC-001 regimen, PDF p. 2](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>) resolve to the direct sources.
- **Support quality:** Direct-source-repaired/nonreproduced registration. Both matched locations print 100 micrograms; the earlier 20-microgram premise is absent. The direct ratio is 100/100=1.
- **Direct versus inferred:** Agreement at 100 micrograms is direct. Font-encoding error or an unsupplied protocol version is inferred.
- **Recheck consistency and overlap:** The ledger now reflects the recheck, but its source mappings and numeric checker still contain the stale 20-microgram transcription and require repair. No separate supported dose relationship remains to combine with another stable ID.
- **Required report wording:** Explicitly say that the supplied direct sources agree at 100 micrograms and that the original registration premise was not reproduced. Do not describe an observed fivefold paper discrepancy. Limit downstream language to the risk of copying a stale workflow transcription if it were left uncorrected.

## C003 — Primary responder-cutoff registration

- **State:** Pending Human Adjudication.
- **Category alignment:** The ledger retains Measure, label, or scale inconsistency for traceability, but no matched cutoff inconsistency is established by the supplied PDFs.
- **Evidence and links:** [DOC-002 protocol, PDF p. 7](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=7>), [DOC-002 protocol endpoint material, PDF p. 24](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=24>), [DOC-001, PDF p. 1](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=1>), and [DOC-002 SAP, PDF p. 66](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=66>) resolve.
- **Support quality:** Direct-source-repaired/nonreproduced registration. The matched supplied occurrences use 1.4 points; `1.4-1.4=0`. A planning mean difference must not be substituted for a binary responder threshold.
- **Direct versus inferred:** Agreement at 1.4 is direct. Character recognition error or an unsupplied version is inferred.
- **Recheck consistency and overlap:** The ledger reflects the recheck; stale mapping/checker entries that say 1.5 for the matched cutoff require repair. This registration is not a second formulation of the sample-size issue in C005 because its intended rule concerns a cutoff, not target-total arithmetic.
- **Required report wording:** Say that the supplied package does not reproduce a 1.5-versus-1.4 responder-cutoff discrepancy. Keep any question about an outside version explicitly outside supplied evidence and avoid implying that participant classification changed.

## C004 — Entry-classification threshold registration

- **State:** Pending Human Adjudication.
- **Category alignment:** The ledger retains Measure, label, or scale inconsistency for traceability, but the supplied entry-classification definitions agree.
- **Evidence and links:** [DOC-002 protocol entry rule, PDF p. 9](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=9>), [DOC-003 eMethods, PDF p. 13](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=13>), and [DOC-002 reversal rule, PDF p. 69](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=69>) resolve.
- **Support quality:** Direct-source-repaired/nonreproduced registration. Entry sources print below 5000 molecules/monocyte. The value above 8000 is a separately named day-15 reversal rule, not an entry criterion.
- **Direct versus inferred:** The 5000 entry and 8000 reversal definitions are direct. Transfer of the reversal threshold into the entry rule is inferred.
- **Recheck consistency and overlap:** The ledger reflects the recheck; the stale entry-threshold transcription in the mapping/numeric checker requires repair. This is definitionally distinct from C003 and from any dose comparison.
- **Required report wording:** State that the supplied sources distinguish 5000 for entry from 8000 for reversal and do not reproduce the registered entry-threshold conflict. Do not claim treatment allocation was affected.

## C005 — Sample-size, dropout, and target registration

- **State:** Pending Human Adjudication.
- **Category alignment:** Denominator, proportion, or total inconsistency remains the ledger category, but the word “about” and an unstated rounding rule prevent a strict contradiction from being established.
- **Evidence and links:** [DOC-002 protocol, PDF pp. 25-26](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=25>) resolves; the per-arm and total values are on p. 26.
- **Support quality:** Direct-source-repaired/nonreproduced registration. The source prints 117 per arm, about 15% dropout, and target 280, not 112 per arm. `2*117=234`; exact 15% inflation gives `234/0.85=275.29`, conventionally at least 276; 280 corresponds to a 16.43% allowance relative to 234. Four additional participants can be consistent with conservative rounding of “about 15%.”
- **Direct versus inferred:** The three printed planning values are direct. A block-size, site, or conservative-rounding rationale is inferred because it is not stated.
- **Recheck consistency and overlap:** The ledger reflects the repaired source value, but N057/S013 and dependent checker text still say 112 and require repair. The corrected relationship is separate from C003's cutoff-tracing question.
- **Required report wording:** Present the calculation as a diagnostic and say that the package omits the rule leading from 276 to 280. Do not characterize 280 as impossible or assert that 15% was applied exactly. Limit downstream impact to extraction of planning assumptions.

## C006 — Historical-trial narrative and flow death counts

- **State:** Pending Human Adjudication.
- **Category alignment:** Cross-document numeric inconsistency.
- **Evidence and links:** [DOC-002 narrative, PDF p. 41](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=41>) and [DOC-002 Figure 1, PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>) resolve.
- **Support quality:** Directly reproduced, conditional on time-window identity. The narrative prints 14/15 deaths (93.3%) in the personalized arm; the flow figure prints 11 early terminations because of death. The difference is three people. The placebo count is 18 in both locations.
- **Direct versus inferred:** The counts and narrative 28-day label are direct. Treating the flow count as the same 28-day outcome is conditional because the figure does not state its time window.
- **Recheck consistency and overlap:** The recheck preserves the missing time-window definition. C014 arose from unsupported assembled pairs and must not be used as corroboration; C006 remains the sole directly observed narrative-versus-flow comparison.
- **Required report wording:** Use a conditional comparison: the values require reconciliation only if the flow's early-termination count covers the narrative's 28-day window. Do not assert a mortality error without that definition. Limit downstream impact to extraction of the historical arm-specific death count and follow-up window.

## C007 — APACHE II P value and displayed t-test inputs

- **State:** Pending Human Adjudication.
- **Category alignment:** Statistical reporting inconsistency.
- **Evidence and links:** [DOC-002 Table 2, PDF p. 48](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=48>) resolves.
- **Support quality:** Directly reproduced. The source prints n=21, 18.2 plus or minus 8.7 versus n=15, 30.5 plus or minus 9.4, `P=.376`, and a Student t-test footnote. Pooled and Welch diagnostics give t near 4 and two-sided P near .0003-.0004, far from .376.
- **Direct versus inferred:** The row and test label are direct. The t/P calculations are diagnostics from displayed summaries; transposition, a different dataset, or a transformed analysis is inferred.
- **Recheck consistency and overlap:** Numeric and statistical pass 1 proposals address the same row/rule and were properly consolidated. The recheck reproduces the diagnostic and names the missing raw observations and implementation details.
- **Required report wording:** Say the displayed inputs are not compatible with `.376` under conventional two-group calculations using the named test. Do not identify which printed component should change. Limit downstream impact to reuse of this baseline comparison.

## C008 — Septic-shock parent and child counts

- **State:** Pending Human Adjudication.
- **Category alignment:** Denominator, proportion, or total inconsistency.
- **Evidence and links:** [DOC-002 Figure 1, PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>) resolves.
- **Support quality:** Directly reproduced. The parent is 177 and the three displayed child counts are 44, 2, and 132; `44+2+132=178`. Percentage rounding cannot explain an integer sum above the parent.
- **Direct versus inferred:** Counts and branch layout are direct. Mutual exclusivity is supported by the displayed flow but any overlap or exception mechanism is inferred because it is not stated.
- **Recheck consistency and overlap:** The recheck reproduces the arithmetic. Although C006 uses the same figure, it compares mortality counts under a different rule; the two are not duplicates.
- **Required report wording:** Say that the displayed child counts exceed the parent by one unless an unstated overlap or different denominator applies. Do not select a count to change. Limit downstream impact to the copied classification total and proportions.

## C009 — ImmunoSep study-site totals

- **State:** Pending Human Adjudication.
- **Category alignment:** Cross-document numeric inconsistency.
- **Evidence and links:** [DOC-001 final report, PDF p. 2](<../../../jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf#page=2>), [DOC-002 protocol, PDF p. 10](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=10>), [DOC-002 SAP design, PDF p. 65](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=65>), and [DOC-002 SAP model text, PDF p. 67](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=67>) resolve.
- **Support quality:** Direct-source-repaired/nonreproduced registration. The original four-value premise and p. 1 citation were wrong. Direct sources print 24 in protocol/SAP design, 31 participating sites in SAP model text, and 33 sites in the final report.
- **Direct versus inferred:** Values and nearby wording are direct. Mapping them to planned, activated, participating, enrolling, or final milestones is inferred because a site chronology is absent.
- **Recheck consistency and overlap:** The ledger reflects repaired values. N047 and the numeric/cross-source checker still say 28, and the cross-source proposal still cites final-report p. 1; these require repair. The protocol and SAP-design 24 are duplicate occurrences of one value, not separate discrepancies.
- **Required report wording:** State the repaired three distinct values and the missing operational definitions. Do not call them incompatible as the same quantity unless milestone identity is established. Limit downstream impact to trial-scale/site-count extraction.

## C010 — Relative-risk label and displayed association

- **State:** Pending Human Adjudication.
- **Category alignment:** Measure, label, or scale inconsistency.
- **Evidence and links:** [DOC-002 Figure 2C, PDF p. 51](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=51>) and [DOC-002 Figure 3, PDF p. 52](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=52>) resolve.
- **Support quality:** Directly reproduced. Figure 2C labels 2.82 (1.58-5.14) as RR; displayed counts give crude RR `(69/103)/(37/89)=1.61` and crude OR `(69*52)/(34*37)=2.85`. Figure 3 prints HR 2.82 (1.58-5.14).
- **Direct versus inferred:** Counts, labels, values, and exact repetition are direct. Whether the 2.82 is copied, an HR, an OR, or another model output is inferred because Figure 2C does not state a model.
- **Recheck consistency and overlap:** Statistical passes and recheck reproduce the same measure-label issue. This is distinct from C007's test/P relationship.
- **Required report wording:** Say that 2.82 does not reproduce as a crude risk ratio from the displayed counts and exactly matches a nearby HR. Ask what effect measure generated it; do not prescribe HR or OR. `P<.0001` is threshold notation and is not the basis of this card. Limit downstream impact to effect-measure extraction.

## C011 — SII day-15 OR, counts, and interval

- **State:** Pending Human Adjudication.
- **Category alignment:** Statistical reporting inconsistency.
- **Evidence and links:** [DOC-003 eTable 10, PDF p. 22](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=22>) resolves.
- **Support quality:** Directly reproduced. The row prints 40/106 versus 29/122, OR 1.194, CI 1.09-3.45, and P=.030. The counts give crude OR `(40*93)/(66*29)=1.9436`; the CI geometric midpoint is `sqrt(1.09*3.45)=1.939`.
- **Direct versus inferred:** Printed row values are direct. The crude OR and midpoint are diagnostics. A decimal/transcription error or cross-analysis pairing is inferred; exact P reconstruction is not supported because the test method is absent.
- **Recheck consistency and overlap:** Statistical passes and recheck reproduce the same relationship. No duplicate stable ID was found.
- **Required report wording:** State that the printed point estimate does not reconcile with the count-derived crude OR and the interval's log midpoint under the displayed unadjusted label. Do not claim that P=.030 independently proves the intended point estimate. Limit downstream impact to this stratum-specific effect estimate and interval.

## C012 — Repeated interaction rows under different outcomes

- **State:** Pending Human Adjudication.
- **Category alignment:** Cross-document numeric inconsistency.
- **Evidence and links:** [DOC-003 eFigure 7B, PDF p. 51](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=51>) and [DOC-003 eFigure 8B, PDF p. 52](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=52>) resolve.
- **Support quality:** Directly reproduced. All six point estimates, intervals, and P values repeat exactly, while captions and A-panel event counts identify different outcomes.
- **Direct versus inferred:** Complete row identity and outcome labels are direct. Copying or a caption error is inferred; exact equality by chance or intentional shared output is not ruled out by source-production files because they are absent.
- **Recheck consistency and overlap:** S047 and S049 intentionally retain the two outcome occurrences. Pass-1 and cross-source proposals concern the same comparison and were properly consolidated into C012.
- **Required report wording:** Describe exact six-row duplication under distinct outcome captions and ask whether the table or caption is the mismatched element. Do not claim a specific production error. Limit downstream impact to outcome-specific subgroup extraction.

## C013 — APACHE interaction point estimate and interval

- **State:** Pending Human Adjudication.
- **Category alignment:** Statistical reporting inconsistency.
- **Evidence and links:** [DOC-003 eFigure 9B, PDF p. 53](<../../../joi250116supp2_prod_1771885794.27755.pdf#page=53>) resolves.
- **Support quality:** Directly reproduced. The row prints OR 0.11 and CI 0.36-3.42; `0.11<0.36`, so the estimate is outside the stated interval. Display rounding cannot span the difference.
- **Direct versus inferred:** The row and noncontainment are direct logical facts. A missing leading digit, wrong endpoint, or row shift is inferred.
- **Recheck consistency and overlap:** Statistical pass 1 and cross-source proposals concern the same row/rule and were properly consolidated. Pass 2 and recheck reproduce it.
- **Required report wording:** State only that the point estimate is not contained in its printed interval and ask which component matches the original model output. Do not propose 1.11 as established. Limit downstream impact to reuse of this interaction estimate and interval.

## C014 — Historical mortality-pair registration

- **State:** Pending Human Adjudication.
- **Category alignment:** The ledger retains Numeric or arithmetic inconsistency for traceability, but the alleged paired values are not present in the supplied source.
- **Evidence and links:** [DOC-002 actual mortality sentence, PDF p. 41](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=41>), [Discussion page, PDF p. 42](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=42>), [Table 2, PDF p. 48](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=48>), and [Figure 1, PDF p. 50](<../../../joi250116supp1_prod_1771885794.26255.pdf#page=50>) resolve.
- **Support quality:** Direct-source-repaired/nonreproduced registration. The alleged p. 42 pairs are absent. The actual p. 41 mortality sentence is coherent: `18/21=85.7%` and `14/15=93.3%`. Values 10 (47.6%) and 12 (80.0%) on p. 48 refer to unrelated rows. Figure 1's death count 11 belongs to the separate C006 comparison.
- **Direct versus inferred:** The coherent mortality sentence and absence of the alleged pairing are direct recheck facts. Assembly from unrelated rows and a shifted page citation is inferred.
- **Recheck consistency and overlap:** The ledger now reflects the recheck, but the cross-source checker's Proposal 5 and matched-result narrative retain the unsupported pairing and require repair. C014 is adjacent to C006, but it cannot be treated as corroboration or silently combined with C006; preserving both IDs requires stating that C014's original evidence basis was not reproduced.
- **Required report wording:** Explicitly state that no direct source location in the supplied package prints the registered count/percentage pairs and that the actual p. 41 pairs reconcile. Do not present C014 as a reproduced paper inconsistency. Limit downstream language to preventing reuse of an unsupported assembled pair in this workflow record.

## Completion statement

Every stable ID has a complete quality card above. Eight observations are directly reproduced from supplied-source comparisons: C001, C006, C007, C008, C010, C011, C012, and C013. Six registrations carry direct-source repairs or nonreproduced original premises: C002, C003, C004, C005, C009, and C014. The latter six must remain visible under their stable IDs, with the source-repair facts prominent and without converting absent or differently defined evidence into an asserted paper inconsistency.
