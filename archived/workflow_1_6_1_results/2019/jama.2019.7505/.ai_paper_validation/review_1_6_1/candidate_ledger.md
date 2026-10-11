# Stable candidate ledger

**Pending Human Adjudication**

Two stable IDs were assigned only after the fresh independent initial inclusion screen, in source order. C001 starts at the main abstract p.1; C002 concerns the respiratory-component definition accompanying Table 3 pp.9–10. All five included finding records are retained. No count target or prior review conclusion guided registration. An assigned ID remains in every later artifact. Direct-source recheck has confirmed roles, relationships and domains and assigned evidence states; independent inclusion audit confirms both candidates. IDs are preserved.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_C | S_C, S_W | REPORT main article binary methods/results vs REPORT results supplement eFigure 12 collapsed-composite label; REPORT main article method/ratio/count comparisons | reproduced | CONFIRMED | F-NUM-001, F-XS-001, F-ST1-001, F-ST1-002 |
| C002 | protocol_report | P_R | P_R | PLAN protocol Appendix iii respiratory definitions vs REPORT main article Table 3 footnote d and REPORT results supplement eMethods 2.8 | reproduced_after_transcription_correction | CONFIRMED | F-XS-002 |

## C001 — Binary effect-quantity identity remains unclear across the reported vectors

**Candidate statement:** The main article labels binary intervention effects as risk ratios, but its displayed counts and denominators do not reconcile with that incidence contrast beyond display precision. The identical primary collapsed-composite vector is additionally labeled an odds ratio in the results supplement. These occurrences form one repeated effect-quantity issue; no specific implementation or replacement result is asserted.

**Review domain:** statistical_results
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main article binary methods/results vs REPORT results supplement eFigure 12 collapsed-composite label; REPORT main article method/ratio/count comparisons
**Evidence state:** reproduced
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-NUM-001, F-XS-001, F-ST1-001, F-ST1-002
**Classification rationale:** Main internal method/count/ratio comparisons are S_W; the explicit RR-versus-OR primary-vector label conflict between the main article and results supplement is S_C, which has precedence. The final SAP corroborates incidence RR wording and is not a conflicting comparator. The issue concerns quantitative estimate/method identity.
**Classification ambiguity:** The report does not identify an alternative primary estimator or the row-specific model behind the supplement's collapsed-composite OR label. The generic per-protocol effect column is corroboration, not independently a definite RR label.

**Exact source locations:** All pages are physical PDF pages. Evidence links are relative to this ledger.

- REPORT [main abstract p.1](../../jama_bluth_2019_oi_190055_16092.pdf#page=1): primary counts, RR and CI; key secondary hypoxemia result.
- REPORT [main methods p.4](../../jama_bluth_2019_oi_190055_16092.pdf#page=4): binary intervention RR/interval/chi-square specification, separate center-adjusted sensitivity, subgroup interaction model.
- REPORT [main narrative p.8](../../jama_bluth_2019_oi_190055_16092.pdf#page=8): primary, mild respiratory failure and pleural-effusion vectors.
- REPORT [main Table 3 p.9](../../jama_bluth_2019_oi_190055_16092.pdf#page=9): 31 binary rows sharing the RR computation block: primary PPC; mild, moderate and severe respiratory failure; atelectasis; pleural effusion; new pulmonary infiltrates; cardiopulmonary edema; bronchospasm; pulmonary infection; aspiration pneumonitis; ARDS; pneumothorax; severe PPC; extrapulmonary composite; systemic inflammatory response syndrome; sepsis; severe sepsis; septic shock; gastrointestinal failure; acute kidney failure; extrapulmonary infection; hepatic failure; coma; disseminated intravascular coagulation; impaired wound healing; unexpected ICU admission/readmission; hypoxemia; hypotension; bradycardia; in-hospital mortality.
- REPORT [main Table 3 continuation/footnote b and Figure 2 p.10](../../jama_bluth_2019_oi_190055_16092.pdf#page=10): binary rescue and vasoactive-drug rows; all eleven forest rows (nonlaparoscopic/laparoscopic, BMI below/at least 40, SpO2 below/at least 96%, peripheral/upper abdominal incision, waist-to-hip below/at least 1, all patients).
- REPORT [results supplement eTable 8 p.29](../../joi190055supp4_prod_16092.pdf#page=29): thirteen per-protocol generic effect-estimate rows, with 917/912 reference populations: primary PPC; mild, moderate, severe respiratory failure; ARDS; bronchospasm; new infiltrates; pulmonary infection; aspiration; pleural effusion; atelectasis; cardiopulmonary edema; pneumothorax. These corroborate the recurring pattern without assigning a definite RR meaning to the generic column.
- REPORT [results supplement eFigure 12 p.42](../../joi190055supp4_prod_16092.pdf#page=42): Global Tests / Collapsed Composite 0.93 [0.83, 1.04] under Odds Ratio (95% CI). Separately specified GEE/count/component models are not compared with crude ratios.
- PLAN [final SAP p.2](../../joi190055supp3_prod_16092.pdf#page=2): corroborating primary/secondary incidence RR specification only.

**Source evidence:** Primary 211/989 vs 233/987, printed RR 0.93 (0.83–1.04), P=.23; hypoxemia 49/989 vs 134/987, RR 0.51 (0.40–0.65); hypotension 313/989 vs 170/987, RR 1.43 (1.31–1.56); bradycardia 98/989 vs 59/987, RR 1.27 (1.11–1.45); pleural effusion 43/989 vs 21/987, RR 1.35 (1.14–1.62). The main method identifies intervention risk ratios and describes site-adjusted sensitivity separately. eFigure 12 repeats the full primary estimate/interval triple under an OR header. The full 33 binary main vectors, all 11 forest vectors, and all 13 PP corroborating vectors remain in the complete numeric checker and new source maps, with each affected page listed above.

**Reported-versus-comparator:** The reported primary vector 0.93 (0.83–1.04) is compared with its stated incidence-risk quantity and with its matched supplementary quantity label. Its stated counts give an incidence ratio 0.903748, while the supplement calls the displayed vector an OR. Other rows provide recurring corroboration; equal-event rows do not independently demonstrate a discrepancy.

**Reasoning procedure:** Match population, contrast, window, outcome and confidence level; preserve stated analysis exceptions; reproduce the declared incidence contrast from exact counts; apply display-precision intervals; inspect the two explicit quantity headers; distinguish direct observations from diagnostic explanation; consolidate the repeated pattern. No specified adjusted/model-based result is required to equal a crude ratio.

**Calculation:** Primary (211/989)/(233/987)=0.903748. Exact counts are primary authority; even conservative half-unit input bounds give 0.898766–0.908757, disjoint from the displayed estimate's half-unit interval 0.925–0.935. Incidence ratios for hypoxemia, hypotension, bradycardia and pleural effusion are 0.364932, 1.837453, 1.657658 and 2.043478, outside the corresponding printed intervals. The diagnostic alternative allocation contrast [H events/(H events+L events)]/[H non-events/(H non-events+L non-events)] gives 0.935791, 0.510737, 1.431233, 1.274329 and 1.357955 for these five rows. It closely tracks the pattern but does not establish the authors' computation; some values do not match conventional final rounding. The source-grounded issue is the target quantity/interval identity, not a claim of exact algorithm reconstruction. The primary crude OR=0.877644 is another diagnostic, not an assigned replacement.

**Affected result or extracted value:** Primary five-day PPC effect magnitude and interval; hypoxemia and other binary treatment-effect quantities; effect-scale encoding of the supplement's primary collapsed composite. The reported primary P=.23 and null primary conclusion are kept separate from magnitude/scale extraction.

**Why context does not resolve it:** The report distinguishes binary incidence analysis, Cox time-to-event analysis, and adjusted sensitivity, but gives no primary contrast or row-specific OR model mapping that resolves the recurring ratios. Replacing a label or choosing a different denominator/estimand changes the quantitative effect an extractor would use; it is not a single obvious glyph repair.

**Alternative source-grounded interpretations:** The advertised incidence contrast could use an unreported estimator; a different two-by-two orientation could underlie the values; the supplement could repeat the main ratio under the shared OR heading or present a distinct OR model. No alternative is selected. The PP generic header alone cannot settle the meaning.

**Mechanical evidence recheck:** Complete: all affected source locations and full vectors matched; calculations and conservative display bounds reproduced; roles and S_C plus S_W classification confirmed. Diagnostic orientation remains an inference. Evidence state reproduced.

**Potential downstream evidence impact:** An extractor could copy a quantity on an unresolved effect scale or magnitude for the primary or hypoxemia result. No actual propagation or conclusion change is claimed.

**Human verification steps:** Inspect main methods, all shared binary rows, forest labels, PP generic column and eFigure 12 global header; identify the probability contrast, denominator orientation, estimator and interval algorithm producing each repeated binary vector; establish whether the supplement's collapsed composite is the main RR or a distinct OR. Preserve separate HR/mean-difference/model-based analyses.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned and reported respiratory-severity criteria differ

**Candidate statement:** The protocol distinguishes mild respiratory failure by response to supplemental oxygen and moderate failure by hypoxemia persisting despite oxygen, whereas the report classifies by response at ≤2 L versus response only at >2 L. The operational criterion accompanying named primary-component and severe-composite counts remains unclear.

**Review domain:** protocol_report
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** PLAN protocol Appendix iii respiratory definitions vs REPORT main article Table 3 footnote d and REPORT results supplement eMethods 2.8
**Evidence state:** reproduced_after_transcription_correction
**Inclusion audit:** CONFIRMED
**Finding IDs:** F-XS-002
**Classification rationale:** A prospective protocol definition conflicts with reported endpoint definitions, so the relationship is P_R and the domain protocol_report. The two REPORT descriptions corroborate each other; the final SAP and amendment list do not add a separate contradictory relationship.
**Classification ambiguity:** An unprovided operational refinement or amendment could explain the difference; none is established by the supplied package.

**Exact source locations:**

- PLAN [protocol Appendix iii p.31](../../joi190055supp1_prod_16092.pdf#page=31): mild room-air hypoxemia responding to supplemental oxygen with no flow boundary; moderate hypoxemia despite supplemental oxygen.
- REPORT [eMethods 2.8 p.20](../../joi190055supp4_prod_16092.pdf#page=20): response-based oxygen-flow severity classification; supplementary mild '=2 L/min' is read with the main explicit ≤2 boundary and complementary >2 category.
- REPORT [main Table 3 p.9](../../jama_bluth_2019_oi_190055_16092.pdf#page=9): mild counts 135/154, moderate 42/58, severe PPC 116/134; reference totals 989/987.
- REPORT [main Table 3 footnote d p.10](../../jama_bluth_2019_oi_190055_16092.pdf#page=10): mild response to ≤2 L and moderate response only to >2 L after room-air hypoxemia criteria.
- REPORT [severe-composite definition p.21](../../joi190055supp4_prod_16092.pdf#page=21): mild respiratory failure excluded.
- PLAN [final SAP p.1](../../joi190055supp3_prod_16092.pdf#page=1): retains primary respiratory components and severe-PPC exclusion of mild; no replacement flow criterion.
- PLAN [amendments p.1](../../joi190055supp2_prod_16092.pdf#page=1), [p.2](../../joi190055supp2_prod_16092.pdf#page=2), [p.3](../../joi190055supp2_prod_16092.pdf#page=3): complete supplied amendment list contains no respiratory-severity definition replacement.

**Source evidence:** Protocol mild uses room-air PaO2 below 60 mmHg or SpO2 below 90% for at least ten minutes and responds to supplemental oxygen. Protocol moderate instead states PaO2 below 60 mmHg or SpO2 below 90% despite supplemental oxygen, without repeating the room-air or ten-minute qualifiers. This source-transcription qualification was made during mechanical recheck. Main/report moderate instead responds only to more than 2 L oxygen, while mild responds at no more than 2 L. The severe composite excludes mild respiratory failure.

**Reported-versus-comparator:** Oxygen required for response and hypoxemia persisting during oxygen are different operational criteria. The protocol mild category also has no stated 2 L boundary. The updated SAP and disclosed amendments do not establish a superseding respiratory-flow definition.

**Reasoning procedure:** Compare exact endpoint definitions in their first-five-day window; read final SAP and complete amendments; distinguish the locally resolved supplementary glyph from the remaining plan/report criterion; link the criterion to the named component and severe-composite counts without inferring patient reclassification.

**Calculation:** Logical boundary comparison rather than reanalysis: an oxygen-responsive event requiring >2 L is compatible with the protocol's unrestricted responsive mild category and the report's moderate category. No actual patient membership is inferred. Mild counts 135/154 and moderate counts 42/58 are the affected reported components; severe-PPC 116/134 excludes mild. Both mild and moderate are in overall primary PPC, so the overall incidence 211/233 is not asserted to change.

**Affected result or extracted value:** The operational respiratory-component definition accompanying mild and moderate counts and severe-composite membership. No changed overall primary incidence is claimed.

**Why context does not resolve it:** Both criteria are understandable, but immediate source context does not identify which governed data classification or whether a later definition amendment occurred. Their difference can change severity-category and severe-composite membership, rather than merely naming the same category.

**Alternative source-grounded interpretations:** A later oxygen-flow refinement could have been implemented; the original protocol could have governed collection with a later summary convention. The supplied evidence does not determine implementation or numerical consequences.

**Mechanical evidence recheck:** Complete: all source definitions, counts, severe-composite exclusion, final SAP and amendments matched. The protocol moderate comparator was qualified to omit unprinted room-air/ten-minute wording; the severity-criterion discrepancy remains. P_R classification confirmed; evidence state reproduced_after_transcription_correction.

**Potential downstream evidence impact:** A review could encode the respiratory severity or severe-composite definition differently while extracting the same published counts. No actual reclassification or downstream propagation is asserted.

**Human verification steps:** Compare protocol Appendix iii, main footnote d, eMethods, severe-composite exclusion and final SAP; human reviewers can inspect the case-report form/data dictionary and any further available approved amendment to establish the implemented response criterion.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
