#!/usr/bin/env bash
set -eu
cd /home/juliz/ai-paper-val/2025/jama.2025.15440
link_failures=0
while IFS= read -r review_doc; do
  while IFS= read -r review_link; do
    case "$review_link" in http:*|https:*|mailto:*|\#*) continue ;; esac
    review_target=${review_link%%#*}
    [ -n "$review_target" ] || continue
    if [ ! -f "$(dirname "$review_doc")/$review_target" ]; then
      printf 'UNRESOLVED %s -> %s\n' "$review_doc" "$review_link"
      link_failures=$((link_failures+1))
    fi
  done < <(perl -ne 'while (/\]\((?:<([^>]+)>|([^\s\)]+))\)/g) { print((defined $1 ? $1 : $2), "\n"); }' "$review_doc")
done < <(rg --files .ai_paper_validation/review_1_6_2 -g '*.md' -g '!tooling/**'; if [ -f .ai_paper_validation/final_report_1_6_2.md ]; then printf '%s\n' .ai_paper_validation/final_report_1_6_2.md; fi)
printf 'Unresolved local links: %s\n' "$link_failures"
[ "$link_failures" -eq 0 ]
