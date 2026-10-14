#!/usr/bin/env python3
"""Render PDF pages and OCR them with RapidOCR on the GPU (CUDA).

Use when a page's text layer is missing, garbled, or a table/figure needs to be
read from the image. Writes <out>/<pdfstem>-p<N>.png and .txt (lines in reading
order, with confidence) and prints the text. Page numbers are 1-based PDF pages.

Usage (OCR venv): ~/venvs/stt/bin/python ocr_page.py FILE.pdf 7 [8 9 ...] --out DIR [--dpi 300] [--crop x0,y0,x1,y1]
--crop takes fractions of the page (0-1), e.g. 0,0.4,1,1 for the lower 60%.
"""
import argparse
from pathlib import Path

import fitz  # PyMuPDF
import onnxruntime as ort

ort.set_default_logger_severity(3)
ort.preload_dlls(directory="")  # CUDA 13/cuDNN libs bundled in the venv's nvidia/ packages
from rapidocr_onnxruntime import RapidOCR  # noqa: E402


def lines_in_order(result, tol=12):
    items = sorted(((min(p[1] for p in box), min(p[0] for p in box), txt, sc)
                    for box, txt, sc in (result or [])))
    rows, cur, y0 = [], [], None
    for y, x, t, s in items:
        if y0 is None or abs(y - y0) <= tol:
            cur.append((x, t, s)); y0 = y if y0 is None else y0
        else:
            rows.append(cur); cur, y0 = [(x, t, s)], y
    if cur:
        rows.append(cur)
    out = []
    for r in rows:
        r.sort()
        out.append("  ".join(t for _, t, _ in r) + f"    [min conf {min(s for *_, s in r):.2f}]")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("pages", nargs="+", type=int)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--crop")
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    eng = RapidOCR(det_use_cuda=True, cls_use_cuda=True, rec_use_cuda=True)
    prov = eng.text_det.infer.session.get_providers()[0]
    print(f"[ocr_page] provider: {prov}")
    doc = fitz.open(a.pdf)
    for n in a.pages:
        page = doc[n - 1]
        clip = None
        if a.crop:
            x0, y0, x1, y1 = map(float, a.crop.split(","))
            r = page.rect
            clip = fitz.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height, r.x0 + x1 * r.width, r.y0 + y1 * r.height)
        pix = page.get_pixmap(dpi=a.dpi, clip=clip, annots=False)  # never show reader annotations
        tag = f"{Path(a.pdf).stem}-p{n}" + ("-crop" if clip else "")
        png = out / f"{tag}.png"; pix.save(png)
        res, _ = eng(str(png))
        txt = "\n".join(lines_in_order(res))
        (out / f"{tag}.txt").write_text(txt, encoding="utf-8")
        print(f"===== {a.pdf} p{n} -> {png}\n{txt}")


if __name__ == "__main__":
    main()
