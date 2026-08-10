#!/usr/bin/env bash
# Page-scoped preprocessing for the approved audit scope.  Source PDFs are read-only inputs.
set -euo pipefail

root_dir="$(cd "$(dirname "$0")/../.." && pwd)"
out_dir="$root_dir/.ai_paper_validation/preprocessing"
main_pdf="$root_dir/jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf"
supp_pdf="$root_dir/joi250116supp2_prod_1771885794.27755.pdf"

mkdir -p "$out_dir/DOC-001"/{native_pages,ocr_pages,images} "$out_dir/DOC-003"/{native_pages,ocr_pages,images}

normalise_page() {
  local document_id="$1" source_name="$2" page="$3" raw="$4" normalized="$5"
  {
    printf '[[source_document_id: %s]]\n[[source_pdf: %s]]\n[[source_pdf_page: %s]]\n\n' "$document_id" "$source_name" "$page"
    perl -CSDA -pe 's/\r\n?/\n/g; s/\f/\n/g; s/[ \t]+\n/\n/g; s/\n{3,}/\n\n/g' "$raw"
  } > "$normalized"
}

extract_native() {
  local document_id="$1" pdf="$2" source_name="$3" page="$4"
  local base="$out_dir/$document_id/native_pages/page_$(printf '%03d' "$page")"
  pdftotext -f "$page" -l "$page" -layout "$pdf" "$base.raw.txt"
  normalise_page "$document_id" "$source_name" "$page" "$base.raw.txt" "$base.txt"
  rm "$base.raw.txt"
}

render_page() {
  local document_id="$1" pdf="$2" page="$3"
  local prefix="$out_dir/$document_id/images/page_$(printf '%03d' "$page")"
  pdftocairo -f "$page" -l "$page" -singlefile -png -r 200 "$pdf" "$prefix"
}

for page in $(seq 1 12); do
  extract_native 'DOC-001' "$main_pdf" 'jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf' "$page"
done
# Only the article's Figure 1-2 and Tables 1-3 require visual review; page 11 is prose/references.
for page in 3 4 5 6 7 8; do
  render_page 'DOC-001' "$main_pdf" "$page"
done

for page in 1 $(seq 6 53); do
  extract_native 'DOC-003' "$supp_pdf" 'joi250116supp2_prod_1771885794.27755.pdf' "$page"
done
for page in $(seq 6 53); do
  render_page 'DOC-003' "$supp_pdf" "$page"
done

# The runtime contains no OCR executable or trained data.  Preserve a page-linked fallback
# record for pages rendered because they contain result tables, figures, or flow diagrams.
for document_id in DOC-001 DOC-003; do
  for image in "$out_dir/$document_id/images"/*.png; do
    page="$(basename "$image" .png | sed 's/page_//; s/^0*//')"
    native="$out_dir/$document_id/native_pages/page_$(printf '%03d' "$page").txt"
    ocr="$out_dir/$document_id/ocr_pages/page_$(printf '%03d' "$page").txt"
    {
      printf '[[source_document_id: %s]]\n[[source_pdf_page: %s]]\n[[rendered_image: %s]]\n\n' "$document_id" "$page" "${image#$root_dir/}"
      printf 'OCR status: Not run — no installed OCR executable or trained OCR data were available.\n'
      printf 'Native extraction is retained at: %s\n' "${native#$root_dir/}"
    } > "$ocr"
  done
done

for document_id in DOC-001 DOC-003; do
  bundle="$out_dir/$document_id/normalized_text.txt"
  : > "$bundle"
  for page_file in "$out_dir/$document_id/native_pages"/*.txt; do
    cat "$page_file" >> "$bundle"
    printf '\n\n===== END SOURCE PAGE =====\n\n' >> "$bundle"
  done
done
