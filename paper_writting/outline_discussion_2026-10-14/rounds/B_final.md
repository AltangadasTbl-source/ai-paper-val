# Drafter B, final: sign-off on v4

## 1. What I accept

I sign off on: the workflow as the core contribution, labeled "development and exploratory application"; outcome sets A–D with dated prespecified-versus-added status; the abstract leading with verification yield; the intended-use statement, failure-mode table, Box 1 and the auditable screening log; describing but not crediting the architecture; the untested "skill" port; dual verification of all 221 non-protocol flags with the pipeline-assigned denominator; C's gap sentence pending a search; Practice of Epidemiology; and no submission without human verification.

## 2. Remaining dissents

1. **Period contrast.**
   - *Argument:* a risk difference across 19 vs 25 papers is confounded by period-specific inputs. These include the annotations, the reused assets from year-specific versions, and the tuning history. A modeled number invites the very reading we disclaim.
   - *Resolution:* I accept A's Newcombe risk difference in the supplement under two conditions. First, the 5 clean reruns must be complete; if they are not, the contrast is dropped. Second, the same table must list the three confounders. The label stays "hypothesis-generating".
2. **Stability rerun.**
   - *Correction:* v4 §5.4 still says "B: optional". Since round 3 my position has been **strongly recommended**, and essential if "replicable" is used.
   - *Resolution:* adopt v4's plan (2 extra runs on 8 packages) with two additions:
     - Run on *copies* of the packages. A rerun in place would collide with the existing `review_1_6_2/` artifacts, which the workflow promises never to overwrite.
     - Make at least one run per stratum a cold start with no reused derivatives, because only 605 of 5,560 source units were extracted fresh.

     At a median of 66 minutes per run, the 16 runs cost about 18 machine-hours.
3. **Conditions for "replicable".**
   - *Argument:* procedure and output are different claims.
   - *Resolution:* "procedurally replicable" requires the second-operator run (Shiyin, README only) plus published hashes of the control files.
   - "Output agreement" may be stated only as the measured overlap on k packages under one model ID and one Codex version. The paper must not say "replicable results" in general.
   - Tokens and the Codex version must be recovered or declared missing.
4. **Article type.** No dissent: Practice of Epidemiology.
5. **Release wording (minor).**
   - The workflow uses the current Codex session's provider and stores no credentials, so say "runs under the user's own Codex authentication".

## 3. Factual errors in v4

1. **"CPU-only operation" is wrong.** Rendering and OCR use the CPU by default, but GPU OCR is permitted on request. Of the 44 `tooling_record.md` files, 14 record `Compute device: GPU_USER_REQUESTED`, although the notes say no GPU inference ran in at least one of them. Write "CPU by default; GPU OCR on user request, recorded per run".
2. **"Workflow 1.6.2 is frozen with hashes" overstates what the runs recorded.**
   - The workflow hashes sources and reused assets, not its own control files. The validator checks only that control files are present and written in English.
   - My post hoc check found AGENTS.md, QUALITY_CONTROL_SCOPE.md, review_contract.md, settings.toml, validate_review.py and a sample preset byte-identical across all 44 packages and identical to `method_design/workflow1.6.2/`.
   - Report this as a post hoc verification, and publish those hashes with the release.
3. **The execution environment was not uniform.** Pandoc versions differ across runs (for example 3.7.0.2 and 3.1.11.1), so more than one machine or environment was used. Table 1 should list the tool versions per run, taken from `tooling_record.md`.
4. **The stage list is incomplete.** It omits the reuse-asset curator and the second inclusion screener, which runs whenever statistical pass 2 emits findings.
5. **Confirmed correct:** run dates (11–14 October 2026), the single model, the funnel (789/215/440), the counts 184 + 37 = 221 and 219, and the runtimes.
