#!/usr/bin/env python3
"""Render selected PDF pages and OCR them with RapidOCR's CUDA backend."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

import fitz
from rapidocr_onnxruntime import RapidOCR


def parse_page_spec(spec: str) -> list[int]:
    pages: set[int] = set()
    for item in spec.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" in item:
            start_text, end_text = item.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start < 1 or end < start:
                raise ValueError(f"Invalid page range: {item}")
            pages.update(range(start, end + 1))
        else:
            page = int(item)
            if page < 1:
                raise ValueError(f"Invalid page number: {item}")
            pages.add(page)
    if not pages:
        raise ValueError("At least one page is required")
    return sorted(pages)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gpu_identity() -> str:
    command = [
        "nvidia-smi",
        "--query-gpu=name,memory.total,driver_version",
        "--format=csv,noheader",
    ]
    return subprocess.check_output(command, text=True).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--pages", required=True, help="1-based pages, e.g. 3-16,22")
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--render-scale", type=float, default=2.25)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = args.pdf.resolve()
    output_root = args.output_root.resolve()
    selected_pages = parse_page_spec(args.pages)
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)
    if args.render_scale <= 0:
        raise ValueError("--render-scale must be positive")

    document = fitz.open(pdf_path)
    invalid_pages = [page for page in selected_pages if page > document.page_count]
    if invalid_pages:
        raise ValueError(
            f"Pages exceed PDF page count ({document.page_count}): {invalid_pages}"
        )

    image_dir = output_root / "images"
    text_dir = output_root / "ocr_pages"
    metadata_dir = output_root / "ocr_metadata"
    image_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    engine = RapidOCR(
        det_use_cuda=True,
        cls_use_cuda=True,
        rec_use_cuda=True,
        print_verbose=False,
    )
    sessions = [engine.text_det.infer, engine.text_cls.infer, engine.text_rec.session]
    providers = [session.session.get_providers() for session in sessions]
    if any(
        not provider_list or provider_list[0] != "CUDAExecutionProvider"
        for provider_list in providers
    ):
        raise RuntimeError(f"CUDA is not the primary OCR provider: {providers}")

    backend = {
        "engine": "rapidocr_onnxruntime",
        "requested_backend": "gpu",
        "selected_backend": "rapidocr-cuda",
        "gpu": gpu_identity(),
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", "not set"),
        "stage_providers": {
            "detector": providers[0],
            "classifier": providers[1],
            "recognizer": providers[2],
        },
    }
    source = {
        "pdf": pdf_path.as_posix(),
        "filename": pdf_path.name,
        "sha256": sha256(pdf_path),
        "total_pages": document.page_count,
        "selected_pages": selected_pages,
        "render_scale": args.render_scale,
    }
    (output_root / "gpu_ocr_backend_report.json").write_text(
        json.dumps(backend, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (output_root / "ocr_scope.json").write_text(
        json.dumps(source, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    page_records: list[dict[str, object]] = []
    matrix = fitz.Matrix(args.render_scale, args.render_scale)
    for page_number in selected_pages:
        page_started = time.perf_counter()
        page = document.load_page(page_number - 1)
        image_path = image_dir / f"page_{page_number:03d}.png"
        page.get_pixmap(matrix=matrix, alpha=False).save(image_path)
        result, engine_elapsed = engine(str(image_path))
        rows = result or []
        recognized_text = "\n".join(str(row[1]) for row in rows)
        scores = [float(row[2]) for row in rows]
        output_path = text_dir / f"page_{page_number:03d}.txt"
        metadata_path = metadata_dir / f"page_{page_number:03d}.json"
        header = (
            f"[[source_pdf: {pdf_path.name}]]\n"
            f"[[source_pdf_sha256: {source['sha256']}]]\n"
            f"[[source_pdf_page: {page_number}]]\n"
            f"[[rendered_image: {image_path.relative_to(output_root).as_posix()}]]\n"
            "[[ocr_backend: rapidocr-cuda]]\n\n"
        )
        output_path.write_text(header + recognized_text + "\n", encoding="utf-8")
        record = {
            "status": "completed",
            "source_pdf": pdf_path.name,
            "source_pdf_sha256": source["sha256"],
            "source_pdf_page": page_number,
            "input_image": image_path.relative_to(output_root).as_posix(),
            "output_text": output_path.relative_to(output_root).as_posix(),
            "characters": len(recognized_text),
            "line_count": len(rows),
            "mean_confidence": sum(scores) / len(scores) if scores else None,
            "engine_elapsed_seconds": engine_elapsed,
            "wall_elapsed_seconds": time.perf_counter() - page_started,
        }
        metadata_path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        page_records.append(record)
        print(
            f"completed {pdf_path.name} p{page_number:03d}: "
            f"{len(rows)} lines, {len(recognized_text)} characters",
            flush=True,
        )

    manifest = {
        "source": source,
        "backend": backend,
        "completed_pages": len(page_records),
        "pages": page_records,
    }
    (output_root / "ocr_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"GPU OCR complete: {len(page_records)} pages -> {output_root}")


if __name__ == "__main__":
    main()
