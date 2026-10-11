#!/usr/bin/env python3
"""Restore jama.2019.0556 to 2019/ and archive its workflow 1.4.1 results (one-off; see README.md).

Uses archive_1_5_results.classify plus 1.4.1-specific rules. The unpacked tesseract install in
.ai_paper_validation/local_ocr/ (binaries) goes to archived/local_only/, which git ignores.
Usage: python3 archive_0556_workflow_1_4_1.py [--execute]
"""
import argparse, csv, hashlib, re, shutil, sys
from pathlib import Path

ARCH = Path(__file__).resolve().parent
REPO = ARCH.parents[1]
sys.path.insert(0, str(ARCH))
from archive_1_5_results import classify as classify_15  # noqa: E402

SRC_PKG = REPO / "archived/local_only/2019/jama.2019.0556"
DST_PKG = REPO / "2019/jama.2019.0556"
OCR_DEST = REPO / "archived/local_only/2019/jama.2019.0556_workflow_1_4_1_local_ocr"
MANIFEST = ARCH / "archive_manifest_jama.2019.0556.csv"


def classify(rel: Path) -> str:
    parts = rel.parts
    if parts[0] in {"workflow1.4.1", "workflow_1_4_1"}:
        return "archive"
    if parts[0] == ".ai_paper_validation" and len(parts) > 1:
        if parts[1] == "local_ocr":
            return "local_ocr"
        if re.match(r"^review_1_4_\d", parts[1]):
            return "keep" if len(parts) > 3 and parts[2] == "preprocessing" else "archive"
        if len(parts) == 2 and parts[1] == "validation_trace.md":
            return "archive"
    return classify_15(rel)


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--execute", action="store_true"); a = ap.parse_args()
    base = DST_PKG if DST_PKG.exists() and not SRC_PKG.exists() else SRC_PKG
    files = sorted(x for x in base.rglob("*") if x.is_file())
    plan = [(f.relative_to(base), classify(f.relative_to(base))) for f in files]
    rx = re.compile(r"^#{1,4}\s*C\d{3}\b|Pending Human Adjudication", re.M)
    flagged = [str(r) for r, act in plan if act == "keep" and r.parts[0] == ".ai_paper_validation"
               and r.suffix in {".md", ".txt", ".json", ".yaml", ".html"}
               and rx.search((base / r).read_text(encoding="utf-8", errors="ignore"))]
    counts = {k: sum(1 for _, x in plan if x == k) for k in ("keep", "archive", "local_ocr")}
    print(f"files={len(plan)} {counts} flagged={flagged}")
    for r, act in plan:
        if act == "archive":
            print("  ARCHIVE", r)
    if not a.execute:
        return
    if flagged:
        sys.exit("refusing: kept files look like results")
    if MANIFEST.exists() or OCR_DEST.exists():
        sys.exit("refusing: an earlier run exists")
    if base == SRC_PKG:
        if DST_PKG.exists():
            sys.exit(f"{DST_PKG} already exists")
        for empty in (".git", ".agents"):
            d = SRC_PKG / empty
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
        shutil.move(str(SRC_PKG), str(DST_PKG))
    with MANIFEST.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["year", "paper", "package_relative_path", "archive_path", "bytes", "sha256"])
        for rel, act in plan:
            if act == "keep":
                continue
            src = DST_PKG / rel
            dst = (ARCH / "2019/jama.2019.0556" / rel) if act == "archive" else OCR_DEST / Path(*rel.parts[2:])
            digest, size = sha(src), src.stat().st_size
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            if sha(dst) != digest:
                sys.exit(f"hash mismatch {dst}")
            w.writerow(["2019", "jama.2019.0556", rel.as_posix(), dst.relative_to(REPO).as_posix(), size, digest])
    for d in sorted((x for x in DST_PKG.rglob("*") if x.is_dir()), key=lambda x: len(x.parts), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()
    print("restored to", DST_PKG.relative_to(REPO), "| manifest", MANIFEST.relative_to(REPO))


if __name__ == "__main__":
    main()
