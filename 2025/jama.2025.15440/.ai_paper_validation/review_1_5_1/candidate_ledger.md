# Stable Candidate Ledger

All entries are quality-control candidates and remain **Pending Human Adjudication**. Checker-local XC001 and SP1001 were merged before stable assignment because they concern the same printed values, comparator, and consistency rule. NC001 is distinct and was retained separately. No candidate was suppressed or capped.

## C001 — Conflicting confidence intervals for the matched any-stroke rate ratio

- **Candidate statement:** The abstract and detailed results/Figure 4B report the same any-stroke arm counts and rate-ratio point estimate but different 95% confidence-interval endpoints.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** DOC-001, `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF p. 1 abstract; PDF p. 5 results narrative; PDF p. 7 Figure 4B.
- **Source evidence:** Page 1 prints patch 69 (2.7%) versus usual care 64 (2.5%), rate ratio 1.08 (95% CI 0.76-1.53). Pages 5 and 7 print the same 69 versus 64 and rate ratio 1.08 but 95% CI 0.77-1.51 for the 2.5-year any-stroke comparison.
- **Reported-versus-comparator:** Abstract CI 0.76-1.53 versus detailed-results/Figure 4B CI 0.77-1.51 for the same displayed counts and point estimate.
- **Reasoning procedure:** Match population, contrast, outcome, follow-up, effect measure, counts, and point estimate, then compare the two-decimal CI endpoints. No distinct estimand or interval method is labeled.
- **Calculation:** Lower endpoints differ by 0.01; upper endpoints differ by 0.02. This is a direct printed-value comparison and does not select either interval as correct.
- **Alternative source-grounded interpretations:** One location may contain a transcription or production-rounding difference; separate interval calculations may have been used but not labeled; or one display may not have received the same update. O-E, V, and the exact CI procedure are not supplied.
- **Checker provenance:** XC001 from cross-source review and SP1001 from statistical pass 1; relationship S003, with supporting N006 and S013.
- **Quality-control relevance:** A reader or evidence extractor could treat the two interval pairs as separate or choose one without knowing which is intended.
- **Potential downstream evidence impact:** If confirmed, an extractor, systematic review, or meta-analysis could copy a nonauthoritative CI endpoint pair for this outcome; no effect on the paper's conclusion is inferred.
- **Human verification steps:** Inspect the analysis output for the 69-versus-64 any-stroke comparison, confirm the CI method and estimand, and compare the intended rounded endpoints with all three printed locations.
- **Exact remaining human question:** Which 95% CI pair is intended for the matched 2.5-year any-stroke rate ratio of 1.08, and was any difference in estimand or interval method intended?
- **Status:** Pending Human Adjudication.

## C002 — Stroke subtype counts do not partition the displayed any-stroke count in the patch group

- **Candidate statement:** Figure 4B prints patch-group presumed ischemic and hemorrhagic stroke counts whose sum exceeds the patch-group `Any stroke` count, while the usual-care counts reconcile.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-001, `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF p. 7 Figure 4B, rows `Presumed ischemic stroke`, `Hemorrhagic stroke`, and `Any stroke`, including caption/footnote.
- **Source evidence:** Patch/usual care respectively: presumed ischemic stroke 60 (2.4%)/58 (2.3%); hemorrhagic stroke 12 (0.5%)/6 (0.2%); any stroke 69 (2.7%)/64 (2.5%). The figure describes events from randomization through 2.5 years and defines presumed ischemic stroke as including unspecified stroke.
- **Reported-versus-comparator:** If subtype rows are mutually exclusive participant-level components, patch subtypes total 72 versus `Any stroke` 69, while usual-care subtypes total 64 versus `Any stroke` 64.
- **Reasoning procedure:** Compare the displayed integer component counts with the displayed total under the conditional partition identity; separate direct arithmetic from the unresolved overlap/counting convention.
- **Calculation:** Patch: 60 + 12 = 72, three above 69. Usual care: 58 + 6 = 64, equal to 64. Counts have zero rounding tolerance. Displayed patch percentages also give 2.4% + 0.5% = 2.9% versus 2.7%, but the integer counts establish the observation.
- **Alternative source-grounded interpretations:** Stroke types may overlap; one participant may contribute multiple stroke records/types; `Any stroke` may count unique participants while subtype rows count events; or record-source/classification rules may create overlap. The supplied figure does not specify the necessary counting convention.
- **Checker provenance:** NC001 from numeric review; relationship N035, with related S013.
- **Quality-control relevance:** Without the counting rule, a reader may incorrectly treat the subtype rows as a mutually exclusive partition of all stroke outcomes.
- **Potential downstream evidence impact:** If confirmed, an evidence extractor could sum nonexclusive subtype counts or misstate the all-stroke composition in a systematic review or evidence table; no conclusion change is inferred.
- **Human verification steps:** Inspect participant-level derivation and event-classification rules; determine whether subtype rows count unique participants or events and whether overlap is permitted; then verify the three patch counts and corresponding footnote.
- **Exact remaining human question:** Were the two Figure 4B stroke subtypes intended as mutually exclusive participant-level outcomes? If yes, which count requires correction; if no, what overlap and counting rule explains 60 + 12 versus 69?
- **Status:** Pending Human Adjudication.

Stable candidate count: 2 (C001, C002). No display-zero-only candidate was registered.
