#!/usr/bin/env bash
# Invoke the mandated one-page OCR wrapper for an explicit rendered-page range.
set -euo pipefail

interpreter="$1"
document_dir="$2"
first_page="$3"
last_page="$4"
workers="${5:-4}"

export interpreter document_dir
seq "$first_page" "$last_page" | xargs -r -P "$workers" -I '{}' bash -c '
  page="$1"
  image="$document_dir/ocr_page_images/page-$(printf "%03d" "$page").png"
  output="$document_dir/ocr_text_pages/page-$(printf "%03d" "$page").txt"
  metadata="$document_dir/page_ocr_metadata/page-$(printf "%03d" "$page").json"
  if [ ! -s "$output" ] || [ ! -s "$metadata" ]; then
    "$interpreter" scripts/ocr_page.py "$image" "$output" --mode gpu --metadata "$metadata"
  fi
' _ '{}'
