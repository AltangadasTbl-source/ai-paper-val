#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "$0")/../.." && pwd)"
base="$root_dir/.ai_paper_validation/preprocessing"
manifest="$base/page_level_manifest.tsv"
printf 'document_id\tsource_pdf\tpdf_page\tscope\tnative_text_path\tnative_character_count\textraction_quality\tvisual_content\trendered_image_path\tocr_status\tocr_record_path\n' > "$manifest"

append_page() {
  local id="$1" source="$2" page="$3" scope="$4" visual="$5"
  local page3 chars quality image ocr ocr_status
  page3="$(printf '%03d' "$page")"
  chars="$(wc -m < "$base/$id/native_pages/page_$page3.txt")"
  quality='good_native_text'
  if [ "$chars" -lt 1000 ]; then quality='sparse_native_text'; fi
  image=''
  ocr='not_applicable'
  ocr_status='not_required'
  if [ "$visual" != 'none' ]; then
    image=".ai_paper_validation/preprocessing/$id/images/page_$page3.png"
    ocr=".ai_paper_validation/preprocessing/$id/ocr_pages/page_$page3.txt"
    ocr_status='not_run_ocr_runtime_unavailable; rendered_image_and_native_text_retained'
  fi
  printf '%s\t%s\t%s\t%s\t.ai_paper_validation/preprocessing/%s/native_pages/page_%s.txt\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$id" "$source" "$page" "$scope" "$id" "$page3" "$chars" "$quality" "$visual" "$image" "$ocr_status" "$ocr" >> "$manifest"
}

main_source='jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf'
for page in $(seq 1 12); do
  visual='none'
  case "$page" in
    3) visual='Figure 1: participant flow diagram' ;;
    4|5) visual='Table 1' ;;
    6) visual='Table 2' ;;
    7) visual='Figure 2' ;;
    8) visual='Table 3' ;;
  esac
  append_page 'DOC-001' "$main_source" "$page" 'Approved main article' "$visual"
done

supp_source='joi250116supp2_prod_1771885794.27755.pdf'
for page in 1 $(seq 6 53); do
  visual='none'
  if [ "$page" -ge 6 ] && [ "$page" -le 44 ]; then visual='eTable content (including continuation where applicable)'; fi
  if [ "$page" -ge 45 ]; then visual='eFigure content'; fi
  append_page 'DOC-003' "$supp_source" "$page" 'Approved result-relevant supplement' "$visual"
done

mkdir -p "$root_dir/.ai_paper_validation/document_outputs/DOC-001" "$root_dir/.ai_paper_validation/document_outputs/DOC-002" "$root_dir/.ai_paper_validation/document_outputs/DOC-003" "$root_dir/.ai_paper_validation/document_outputs/DOC-004" "$root_dir/.ai_paper_validation/document_outputs/DOC-005"
jq -n --arg source "$main_source" --arg manifest '. + {document_id:"DOC-001",source_pdf:$source,processing_status:"Preprocessed",selected_pdf_pages:"1-12",native_extraction:"completed all selected pages",rendered_pages:"3-8",ocr_status:"OCR runtime unavailable; native text and visual renders retained",page_manifest:$manifest}' > "$root_dir/.ai_paper_validation/document_outputs/DOC-001/preprocessing_record.json"
jq -n --arg source "$supp_source" --arg manifest '. + {document_id:"DOC-003",source_pdf:$source,processing_status:"Preprocessed",selected_pdf_pages:"1,6-53",native_extraction:"completed all selected pages",rendered_pages:"6-53",ocr_status:"OCR runtime unavailable; native text and visual renders retained",page_manifest:$manifest}' > "$root_dir/.ai_paper_validation/document_outputs/DOC-003/preprocessing_record.json"
jq -n --arg source 'joi250116supp1_prod_1771885794.26255.pdf' '. + {document_id:"DOC-002",source_pdf:$source,processing_status:"Not Audited by Design",extraction_scope:"Excluded protocol/SAP content; no broad native extraction, rendering, or OCR performed by preprocessor."}' > "$root_dir/.ai_paper_validation/document_outputs/DOC-002/preprocessing_record.json"
jq -n --arg source 'joi250116supp3_prod_1771885794.28255.pdf' '. + {document_id:"DOC-004",source_pdf:$source,processing_status:"Not Audited by Design",extraction_scope:"Excluded administrative collaborator content; no broad native extraction, rendering, or OCR performed by preprocessor."}' > "$root_dir/.ai_paper_validation/document_outputs/DOC-004/preprocessing_record.json"
jq -n --arg source 'joi250116supp4_prod_1771885794.28755.pdf' '. + {document_id:"DOC-005",source_pdf:$source,processing_status:"Not Audited by Design",extraction_scope:"Excluded administrative data-sharing content; no broad native extraction, rendering, or OCR performed by preprocessor."}' > "$root_dir/.ai_paper_validation/document_outputs/DOC-005/preprocessing_record.json"
