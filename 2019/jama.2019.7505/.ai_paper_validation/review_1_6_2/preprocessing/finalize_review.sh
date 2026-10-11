#!/usr/bin/env bash
set -euo pipefail
run_dir=.ai_paper_validation/review_1_6_2
report_md=.ai_paper_validation/final_report_1_6_2.md
started_utc=$(sed -n 's/^- \*\*Started UTC:\*\* //p' "$run_dir/run_state.md")
finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
started_epoch=$(date -u -d "$started_utc" +%s)
finished_epoch=$(date -u -d "$finished_utc" +%s)
observed_minutes=$(awk -v seconds="$((finished_epoch-started_epoch))" 'BEGIN {printf "%.2f", seconds/60}')
target_range=$(sed -n 's/^- \*\*Target elapsed minutes:\*\* //p' "$run_dir/run_state.md")
target_upper=${target_range#*-}
target_status=$(awk -v observed="$observed_minutes" -v upper="$target_upper" 'BEGIN {print (observed > upper ? "EXCEEDED_TARGET" : "MET_TARGET")}')
awk -v finish="$finished_utc" -v elapsed="$observed_minutes" -v status="$target_status" '
/^\- \*\*Finished UTC:\*\*/ {$0="- **Finished UTC:** " finish}
/^\- \*\*Observed elapsed minutes:\*\*/ {$0="- **Observed elapsed minutes:** " elapsed}
/^\- \*\*Target status:\*\*/ {$0="- **Target status:** " status}
{print}' "$run_dir/run_state.md" > "$run_dir/preprocessing/run_state_final.tmp"
mv "$run_dir/preprocessing/run_state_final.tmp" "$run_dir/run_state.md"
awk 'NR==FNR {if ($0 ~ /^- \*\*(Target basis|Total source units|Fresh-source units|Target elapsed minutes|Started UTC|Finished UTC|Observed elapsed minutes|Target status|Exceedance causes):\*\*/) {split($0,a,/\*\*/);fields[a[2]]=$0}; next}
{line=$0; if (line ~ /^(- )?\*\*(Target basis|Total source units|Fresh-source units|Target elapsed minutes|Started UTC|Finished UTC|Observed elapsed minutes|Target status|Exceedance causes):\*\*/) {split(line,a,/\*\*/);if(a[2] in fields) line=fields[a[2]]}; print line}' "$run_dir/run_state.md" "$report_md" > "$run_dir/preprocessing/report_final.tmp"
mv "$run_dir/preprocessing/report_final.tmp" "$report_md"
while read -r prior_hash source_path; do sha256sum -- "$source_path"; done < "$run_dir/source_hashes_before.sha256" > "$run_dir/source_hashes_after.sha256"
while read -r prior_hash asset_path; do sha256sum -- "$asset_path"; done < "$run_dir/reused_artifact_hashes_before.sha256" > "$run_dir/reused_artifact_hashes_after.sha256"
cmp "$run_dir/source_hashes_before.sha256" "$run_dir/source_hashes_after.sha256"
cmp "$run_dir/reused_artifact_hashes_before.sha256" "$run_dir/reused_artifact_hashes_after.sha256"
python3 workflow_1_6_2/scripts/render_report.py "$report_md" .ai_paper_validation/final_report_1_6_2.html --profile 1.6.2
python3 workflow_1_6_2/scripts/bootstrap_tooling.py remove
printf "\nFinal tooling check: bootstrap_tooling.py remove completed after HTML rendering; no fallback environment was created. Removal state remains NOT_CREATED. All current derivatives used the recorded direct tools on CPU.\n" >> "$run_dir/tooling_record.md"
python3 workflow_1_6_2/scripts/validate_review.py --profile 1.6.2 --package .
