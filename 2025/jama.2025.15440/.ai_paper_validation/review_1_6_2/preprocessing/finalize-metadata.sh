#!/usr/bin/env bash
set -euo pipefail
review_dir=.ai_paper_validation/review_1_6_2
report_path=.ai_paper_validation/final_report_1_6_2.md
test -s "$report_path"
export QC_FINISHED_UTC
QC_FINISHED_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
started_utc=$(sed -n 's/^- \*\*Started UTC:\*\* //p' "$review_dir/run_state.md")
started_epoch=$(date -u -d "$started_utc" +%s)
finished_epoch=$(date -u -d "$QC_FINISHED_UTC" +%s)
export QC_OBSERVED_MINUTES QC_TARGET_STATUS QC_EXCEEDANCE_CAUSES
QC_OBSERVED_MINUTES=$(awk -v elapsed="$((finished_epoch-started_epoch))" 'BEGIN {printf "%.2f", elapsed/60}')
if awk -v observed="$QC_OBSERVED_MINUTES" 'BEGIN {exit !(observed <= 55)}'; then
  QC_TARGET_STATUS=MET_TARGET
  QC_EXCEEDANCE_CAUSES=None
else
  QC_TARGET_STATUS=EXCEEDED_TARGET
  QC_EXCEEDANCE_CAUSES='Twenty-six fresh GPU OCR pages and CUDA startup; complete same-table power and sample-size reconstruction with display-precision enclosures; sequential independent screening, source recheck, second statistical pass and quality audit; audit documentation and transcription repair; complete report assembly.'
fi
perl -i -pe 's/^(\- \*\*Finished UTC:\*\* ).*/$1$ENV{QC_FINISHED_UTC}/; s/^(\- \*\*Observed elapsed minutes:\*\* ).*/$1$ENV{QC_OBSERVED_MINUTES}/; s/^(\- \*\*Target status:\*\* ).*/$1$ENV{QC_TARGET_STATUS}/; s/^(\- \*\*Exceedance causes:\*\* ).*/$1$ENV{QC_EXCEEDANCE_CAUSES}/; s/^(\- \*\*Run status:\*\* ).*/${1}FINAL_VALIDATION_PENDING/;' "$review_dir/run_state.md"
perl -i -pe 'BEGIN {open my $state, "<", ".ai_paper_validation/review_1_6_2/run_state.md" or die $!; while (<$state>) {if (/^- \*\*(Target basis|Total source units|Fresh-source units|Target elapsed minutes|Started UTC|Finished UTC|Observed elapsed minutes|Target status|Exceedance causes):\*\*/) {$fields{$1}=$_}}} if (/^- \*\*(Target basis|Total source units|Fresh-source units|Target elapsed minutes|Started UTC|Finished UTC|Observed elapsed minutes|Target status|Exceedance causes):\*\*/) {$_=$fields{$1}}' "$report_path"
printf 'Metadata finalized: %s; %s minutes; %s\n' "$QC_FINISHED_UTC" "$QC_OBSERVED_MINUTES" "$QC_TARGET_STATUS"
