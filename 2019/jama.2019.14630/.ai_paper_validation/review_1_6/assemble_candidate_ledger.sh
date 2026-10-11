#!/bin/bash
set -euo pipefail
review_dir=.ai_paper_validation/review_1_6
ledger_path="$review_dir/candidate_ledger.md"
append_section() {
  awk -v key="$1" '
    /^#{1,3} / {
      if (active) exit;
      if (index($0,key)>0) {active=1; next}
    }
    active {print}
  ' "$review_dir/$2" | sed -E 's@(\.\./){2,}([^()<> ]+\.pdf#page=[0-9]+)@../../\2@g'
}
while IFS=$'\t' read -r cid source_path local_key card_title category relationship roles domain duplicate_keys; do
  printf '\n## %s — %s\n\n' "$cid" "$card_title" >> "$ledger_path"
  printf '**Status:** Pending Human Adjudication\n\n**Category:** %s\n\n**Relationship type:** %s\n\n**All relationships:** %s\n\n**Compared document roles:** %s\n\n**Review domain:** %s\n\n**Checker provenance:** %s in %s; additional exact-duplicate provenance: %s.\n\n' "$category" "$relationship" "$relationship" "$roles" "$domain" "$local_key" "$source_path" "$duplicate_keys" >> "$ledger_path"
  if [[ "$cid" == C042 ]]; then
    printf '**Registered comparison:** Intervention arm only: eTable2 baseline33(0,29) versus eTable7 baseline0(0,29). The shared two-arm numeric record below is context; the control comparison is separately registered as C043.\n\n' >> "$ledger_path"
  elif [[ "$cid" == C043 ]]; then
    printf '**Registered comparison:** Control arm only: eTable2 baseline4(0,29) versus eTable7 baseline0(0,29). The shared two-arm numeric record below is context; the intervention comparison is separately registered as C042.\n\n' >> "$ledger_path"
  fi
  append_section "$local_key" "$source_path" >> "$ledger_path"
  if [[ "$duplicate_keys" != None ]]; then
    IFS=',' read -ra duplicate_array <<< "$duplicate_keys"
    for duplicate_key in "${duplicate_array[@]}"; do
      duplicate_key="${duplicate_key// /}"
      if [[ "$duplicate_key" == X-* ]]; then duplicate_source=checkers/cross_source_consistency.md; else duplicate_source=checkers/statistical_pass_1.md; fi
      printf '\n### Exact-duplicate provenance %s\n\n' "$duplicate_key" >> "$ledger_path"
      append_section "$duplicate_key" "$duplicate_source" >> "$ledger_path"
    done
  fi
  if [[ "$cid" == C004 ]]; then
    printf '\n**Coordinator arithmetic correction:** Intervention largest-remainder allocation is47,31,22, not48,31,21. The displayed48,31,21 totals100 but requires a different undisclosed total-preserving rule; ordinary individual rounding gives48,31,22. This correction changes the alternative explanation only.\n' >> "$ledger_path"
  fi
done < "$review_dir/candidate_registration_map.tsv"
