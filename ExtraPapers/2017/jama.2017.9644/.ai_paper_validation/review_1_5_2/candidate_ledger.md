# Stable Candidate Ledger

All genuine duplicate signals were merged before assignment. Similar Table 3 rows remain separate because each has different printed values and a distinct within-row numerator/denominator/percentage identity. Every entry remains **Pending Human Adjudication**; no AI validity, importance, action, acceptance, rejection, correction, or severity decision is assigned.

## C001 — Figure 2 combines a percentage axis with count-like embedded labels without stating the embedded unit

- **Candidate statement:** Figure 2A-B uses an axis labelled `Patients, %`, while the integers inside each bar sum to the group sample size and reproduce count numerators rather than percentages.
- **Category:** Rate-versus-count inconsistency
- **Exact source locations:** [Main article — PDF p. 7](<../../jama_lapergue_2017_oi_170084.pdf#page=7>), Figure 2A-B.
- **Source evidence:** A contact values `8, 2, 18, 92, 72` sum to 192; stent values `5, 5, 22, 84, 73` sum to 189. B values likewise sum to 192 and 189. Both axes run 0-100 and state `Patients, %`.
- **Reported-versus-comparator:** Percentage-axis label versus count-like embedded values and group `n` labels.
- **Consistency rule:** A mixed count/percentage display should make the unit of internal annotations distinguishable from the percentage scale.
- **Direct observation:** Axis text, group totals, and all embedded integers are printed in the figure.
- **Derived diagnostic:** Exact sums show the embedded values are counts; 2b+3 values reproduce Table 2 numerators.
- **Alternative source-grounded interpretation:** This may be an intentional 100%-stacked chart with count annotations; the numeric content itself reconciles.
- **Exact human question:** Was the mixed convention intentional, and should the embedded numbers be explicitly labelled as counts?
- **Provenance:** MAIN-N051; SIG-N051; CS-01.
- **Status:** Pending Human Adjudication.

## C002 — eTable frontline stent header does not identify how n=175 relates to the main flow totals

- **Candidate statement:** The supplement eTable labels the assigned-group column `Stent Retriever First (n=175)`, while the main flow diagram reports 189 assigned to stent retriever and 170 receiving a stent retriever as randomized.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Supplement 2 — PDF p. 4](<../../joi170084supp2_prod.pdf#page=4>), eTable; [main article — PDF p. 4](<../../jama_lapergue_2017_oi_170084.pdf#page=4>), Figure 1.
- **Source evidence:** eTable header `n=175`; flow totals 189 randomized and 170 received assigned stent. Device rows in that eTable column sum to 186, so they are not a mutually exclusive participant partition.
- **Reported-versus-comparator:** Undefined eTable header total 175 versus the two relevant main-flow totals 170 and 189.
- **Consistency rule:** A displayed `n` for a treatment-labelled column should identify its population or reconcile to the matched assigned/treated population.
- **Direct observation:** The three totals and table/flow labels are printed.
- **Derived diagnostic:** 175 is neither 170 nor 189; row sums do not define the header because multiple devices can be used.
- **Alternative source-grounded interpretation:** Excluding 12 spontaneous lyses, one groin failure, and one extracranial-only procedure from 189 leaves 175 participants with a frontline thrombectomy device, including five assigned-stent participants who received aspiration; the eTable may intend that exposure population despite its `Stent Retriever First` label.
- **Exact human question:** What exactly does `Stent Retriever First (n=175)` count, and how should it be labelled relative to the 170 assigned-treatment recipients and 189 randomized participants?
- **Provenance:** SUP-N011; N074; SIG-N074.
- **Status:** Pending Human Adjudication.

## C003 — Protocol and publication report different design sample sizes

- **Candidate statement:** Protocol V1.1 reports 161 participants per arm (322 total), whereas the article reports 190 per arm (380 total) for the same trial design.
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Protocol — PDF p. 7](<../../joi170084supp1_prod.pdf#page=7>), sample-size section; [main article — PDF p. 3](<../../jama_lapergue_2017_oi_170084.pdf#page=3>), Statistical Analysis.
- **Source evidence:** Both use 70% and 85% expected rates, two-sided alpha .05, and 90% power; the article additionally states a 15% failure assumption and reports 380/190, while protocol V1.1 reports 322/161.
- **Reported-versus-comparator:** 322 total/161 per arm versus 380 total/190 per arm.
- **Consistency rule:** Different design totals for the same trial should be linked to a supplied amendment or clearly distinguished calculation assumptions.
- **Direct observation:** Both sample sizes and premises are printed.
- **Derived diagnostic:** The totals differ by 58 participants; the supplied package does not include controlling amendment provenance.
- **Alternative source-grounded interpretation:** A later approved amendment may have added the article's 15% failure allowance or otherwise revised the design before enrollment.
- **Exact human question:** Which design calculation governed the trial, and does an approved amendment explain the change from 322 to 380?
- **Provenance:** S001; S022; SIG-STAT-001; PP-01.
- **Status:** Pending Human Adjudication.

## C004 — Protocol and publication report different primary analysis methods

- **Candidate statement:** Protocol V1.1 specifies a chi-square primary comparison with rate differences and center-stratified/Breslow-Day analysis, whereas the publication specifies mixed logistic regression with center random and IV-thrombolysis fixed effects.
- **Category:** Statistical reporting inconsistency
- **Exact source locations:** [Protocol — PDF p. 6](<../../joi170084supp1_prod.pdf#page=6>) and [p. 7](<../../joi170084supp1_prod.pdf#page=7>), Data Analysis; [main article — PDF p. 3](<../../jama_lapergue_2017_oi_170084.pdf#page=3>) and [Supplement 2 — PDF p. 2](<../../joi170084supp2_prod.pdf#page=2>), published statistical methods.
- **Source evidence:** The supplied documents describe different primary test/model families and adjustment/center handling for the same endpoint.
- **Reported-versus-comparator:** Planned chi-square/stratified approach versus published mixed logistic approach.
- **Consistency rule:** A changed prespecified primary analysis requires supplied version/amendment provenance to establish which method controlled the final analysis.
- **Direct observation:** Both methods are explicitly printed.
- **Derived diagnostic:** No amendment/final SAP in the supplied package connects the methods.
- **Alternative source-grounded interpretation:** The published method may reflect an authorized pre-analysis amendment or final SAP not supplied in the package.
- **Exact human question:** Was the mixed-logistic analysis prespecified in an approved controlling document before analysis, and how does it supersede protocol V1.1?
- **Provenance:** S003; S021; S023; SIG-STAT-001; PP-01.
- **Status:** Pending Human Adjudication.

## C005 — Stent intracranial-hemorrhage percentage does not match 85/188

- **Candidate statement:** Table 3 prints `85/188 (46.2)` for stent-retriever intracranial hemorrhage, but the fraction rounds to 45.2%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 85, denominator 188, percentage 46.2.
- **Reported-versus-comparator:** 46.2% versus `85/188 × 100 = 45.2128%`, one-decimal 45.2%.
- **Consistency rule:** A printed percentage should reproduce from its printed fraction under ordinary one-decimal rounding.
- **Direct observation:** The fraction and percentage are printed in the same row.
- **Derived diagnostic:** Difference is 1.0 percentage point after one-decimal rounding.
- **Alternative source-grounded interpretation:** `85/184=46.2%`, and nearby stent rows explicitly use 184; either the denominator or percentage may derive from another analysis total.
- **Exact human question:** What denominator produced 46.2%, and which displayed element is intended?
- **Provenance:** MAIN-N053/N055; N053/N055; SIG-N053A.
- **Status:** Pending Human Adjudication.

## C006 — Stent hemorrhagic-infarction percentage does not match 49/188

- **Candidate statement:** Table 3 prints `49/188 (26.6)`, but the fraction rounds to 26.1%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 49, denominator 188, percentage 26.6.
- **Reported-versus-comparator:** 26.6% versus `49/188 × 100 = 26.0638%`, one-decimal 26.1%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The three printed values are in one row.
- **Derived diagnostic:** Difference is 0.5 percentage point after rounding.
- **Alternative source-grounded interpretation:** `49/184=26.6%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N055; N055; SIG-N055A.
- **Status:** Pending Human Adjudication.

## C007 — Stent hemorrhagic-infarction type 1 percentage does not match 24/188

- **Candidate statement:** Table 3 prints `24/188 (13.0)`, but the fraction rounds to 12.8%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 24, denominator 188, percentage 13.0.
- **Reported-versus-comparator:** 13.0% versus `24/188 × 100 = 12.7660%`, one-decimal 12.8%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The three values are printed in one row.
- **Derived diagnostic:** Difference is 0.2 percentage point after rounding.
- **Alternative source-grounded interpretation:** `24/184=13.0%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N055; N055; SIG-N055B.
- **Status:** Pending Human Adjudication.

## C008 — Stent hemorrhagic-infarction type 2 percentage does not match 25/188

- **Candidate statement:** Table 3 prints `25/188 (13.6)`, but the fraction rounds to 13.3%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 25, denominator 188, percentage 13.6.
- **Reported-versus-comparator:** 13.6% versus `25/188 × 100 = 13.2979%`, one-decimal 13.3%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The three values are printed in one row.
- **Derived diagnostic:** Difference is 0.3 percentage point after rounding.
- **Alternative source-grounded interpretation:** `25/184=13.6%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N055; N055; SIG-N055C.
- **Status:** Pending Human Adjudication.

## C009 — Stent parenchymal-hematoma percentage does not match 33/188

- **Candidate statement:** Table 3 prints `33/188 (17.4)`, but the fraction rounds to 17.6%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 33, denominator 188, percentage 17.4.
- **Reported-versus-comparator:** 17.4% versus `33/188 × 100 = 17.5532%`, one-decimal 17.6%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The values are printed together.
- **Derived diagnostic:** Difference is 0.2 percentage point after rounding.
- **Alternative source-grounded interpretation:** A row-specific unprinted denominator may have produced 17.4%; neither printed 188 nor nearby 184 yields that result at one decimal.
- **Exact human question:** What denominator produced 17.4%, and which displayed element is intended?
- **Provenance:** MAIN-N056; N056; SIG-N056A.
- **Status:** Pending Human Adjudication.

## C010 — Stent parenchymal-hematoma type 1 percentage does not match 19/188

- **Candidate statement:** Table 3 prints `19/188 (10.3)`, but the fraction rounds to 10.1%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 19, denominator 188, percentage 10.3.
- **Reported-versus-comparator:** 10.3% versus `19/188 × 100 = 10.1064%`, one-decimal 10.1%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The values are printed together.
- **Derived diagnostic:** Difference is 0.2 percentage point after rounding.
- **Alternative source-grounded interpretation:** `19/184=10.3%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N056; N056; SIG-N056B.
- **Status:** Pending Human Adjudication.

## C011 — Stent parenchymal-hematoma type 2 percentage does not match 14/188

- **Candidate statement:** Table 3 prints `14/188 (7.6)`, but the fraction rounds to 7.4%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 14, denominator 188, percentage 7.6.
- **Reported-versus-comparator:** 7.6% versus `14/188 × 100 = 7.4468%`, one-decimal 7.4%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The values are printed together.
- **Derived diagnostic:** Difference is 0.2 percentage point after rounding.
- **Alternative source-grounded interpretation:** `14/184=7.6%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N056; N056; SIG-N056C.
- **Status:** Pending Human Adjudication.

## C012 — Stent symptomatic-intracranial-hemorrhage percentage does not match 12/188

- **Candidate statement:** Table 3 prints `12/188 (6.5)`, but the fraction rounds to 6.4%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 12, denominator 188, percentage 6.5.
- **Reported-versus-comparator:** 6.5% versus `12/188 × 100 = 6.3830%`, one-decimal 6.4%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The values are printed together.
- **Derived diagnostic:** Difference is 0.1 percentage point after rounding.
- **Alternative source-grounded interpretation:** `12/184=6.5%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N053/N057; N053/N057; SIG-N053B.
- **Status:** Pending Human Adjudication.

## C013 — Stent subarachnoid-hemorrhage percentage does not match 13/188

- **Candidate statement:** Table 3 prints `13/188 (7.1)`, but the fraction rounds to 6.9%.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Main article — PDF p. 8](<../../jama_lapergue_2017_oi_170084.pdf#page=8>), Table 3.
- **Source evidence:** Printed numerator 13, denominator 188, percentage 7.1.
- **Reported-versus-comparator:** 7.1% versus `13/188 × 100 = 6.9149%`, one-decimal 6.9%.
- **Consistency rule:** Within-row fraction-to-percentage identity.
- **Direct observation:** The values are printed together.
- **Derived diagnostic:** Difference is 0.2 percentage point after rounding.
- **Alternative source-grounded interpretation:** `13/184=7.1%`; the intended denominator may be 184.
- **Exact human question:** Which denominator and percentage are intended for this row?
- **Provenance:** MAIN-N057; N057; SIG-N057A.
- **Status:** Pending Human Adjudication.

## Registration completeness

Stable candidate set: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013. No candidate was registered solely for a display-zero P value; none occurred.
