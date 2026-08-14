#!/usr/bin/env python3
"""Convert direct DOC/DOCX package supplements to derived PDFs without modifying sources."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import tempfile
import tomllib
from pathlib import Path


def _windows_path(path: Path) -> str:
    if platform.system() == "Windows":
        return str(path.resolve())
    completed = subprocess.run(
        ["wslpath", "-w", str(path.resolve())], check=True, capture_output=True, text=True
    )
    return completed.stdout.strip()


def _convert_linux(source: Path, destination_dir: Path, executable: str) -> Path:
    with tempfile.TemporaryDirectory(prefix="office-convert-", dir=destination_dir) as staging_raw:
        staging = Path(staging_raw)
        subprocess.run(
            [executable, "--headless", "--convert-to", "pdf", "--outdir", str(staging), str(source)],
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        generated = staging / f"{source.stem}.pdf"
        if not generated.is_file():
            raise RuntimeError(f"Office converter did not create {generated.name}")
        destination = destination_dir / f"{source.name}.pdf"
        shutil.copy2(generated, destination)
        return destination


def _convert_windows(source: Path, destination_dir: Path, wrapper: Path) -> Path:
    powershell = os.environ.get("AI_VALIDATION_POWERSHELL", "powershell.exe")
    subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-File",
            str(wrapper),
            "convert-doc",
            _windows_path(source),
            _windows_path(destination_dir),
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=240,
    )
    generated = destination_dir / f"{source.stem}.pdf"
    if not generated.is_file():
        raise RuntimeError(f"Windows Office converter did not create {generated.name}")
    destination = destination_dir / f"{source.name}.pdf"
    generated.replace(destination)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    package = args.package.resolve()
    config_path = (
        args.config or Path(__file__).resolve().parents[4] / "ai-validation.toml"
    ).expanduser().resolve()
    with config_path.open("rb") as handle:
        settings = tomllib.load(handle)
    tools = settings.get("tools", {})
    output_dir = (args.output_dir or package / "audit/preprocessing/converted_pdf").resolve()
    manifest_path = (args.manifest or package / "audit/preprocessing/conversion_manifest.json").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    sources = sorted(
        (path for path in package.iterdir() if path.is_file() and path.suffix.lower() in {".doc", ".docx"}),
        key=lambda path: path.name.casefold(),
    )
    configured_office = os.environ.get(
        "AI_VALIDATION_LIBREOFFICE", str(tools.get("libreoffice", ""))
    )
    executable = (
        (shutil.which(configured_office) or configured_office if configured_office else None)
        or shutil.which("libreoffice")
        or shutil.which("soffice")
    )
    wrapper = Path(
        os.environ.get(
            "AI_VALIDATION_POWERSHELL_WRAPPER",
            str(Path(__file__).resolve().parent / "windows_tools.ps1"),
        )
    ).resolve()
    powershell = str(tools.get("powershell", "powershell.exe"))
    os.environ.setdefault("AI_VALIDATION_POWERSHELL", powershell)
    records: list[dict[str, str]] = []
    failed = False
    for source in sources:
        record = {"source": source.name, "status": "FAILED", "engine": "", "pdf": ""}
        try:
            if executable:
                pdf = _convert_linux(source, output_dir, executable)
                record.update(status="COMPLETED", engine=executable, pdf=str(pdf.relative_to(package)))
            elif shutil.which(os.environ.get("AI_VALIDATION_POWERSHELL", "powershell.exe")) and wrapper.is_file():
                pdf = _convert_windows(source, output_dir, wrapper)
                record.update(status="COMPLETED", engine="windows-libreoffice", pdf=str(pdf.relative_to(package)))
            else:
                raise RuntimeError("No WSL or Windows LibreOffice converter is available.")
        except Exception as error:  # Preserve all records before failing preflight.
            failed = True
            record["error"] = str(error)
        records.append(record)
    manifest = {"schema_version": 1, "package": package.name, "documents": records}
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
