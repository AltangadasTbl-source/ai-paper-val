"""Select and initialize the local OCR backend used by the workflow.

The preferred path is RapidOCR on ONNX Runtime's CUDA provider.  It is used
only after creating the detector, classifier, and recognizer sessions and
confirming that each one reports ``CUDAExecutionProvider``.  That prevents
ONNX Runtime's silent CPU fallback from being recorded as GPU OCR.

Run this module through the environment intended for OCR.  In this project
that is normally ``~/venvs/stt/bin/python``.  On Linux, the module discovers
CUDA libraries installed as Python packages, adjusts ``LD_LIBRARY_PATH``, and
re-execs before importing ONNX Runtime when necessary.
"""

from __future__ import annotations

import importlib.util
import os
import platform
import re
import shutil
import site
import subprocess
import sys
from pathlib import Path
from typing import Any


CUDA_REEXEC_FLAG = "AI_PAPER_VALIDATION_CUDA_REEXEC"
RTX_5070_LAPTOP_PATTERN = re.compile(r"rtx\s*5070\s+laptop", re.IGNORECASE)


def _site_package_roots() -> list[Path]:
    roots: list[Path] = []
    for candidate in [*site.getsitepackages(), site.getusersitepackages()]:
        path = Path(candidate)
        if path not in roots and path.exists():
            roots.append(path)
    return roots


def cuda_runtime_library_dirs() -> list[str]:
    """Return CUDA runtime library directories shipped in the active venv."""
    directories: list[str] = []
    for root in _site_package_roots():
        nvidia = root / "nvidia"
        if not nvidia.is_dir():
            continue
        for directory in sorted(nvidia.glob("*/lib")):
            if directory.is_dir() and str(directory) not in directories:
                directories.append(str(directory))
    return directories


def ensure_cuda_loader_path() -> list[str]:
    """Re-exec on Linux so ONNX Runtime can load venv-provided CUDA libraries."""
    directories = cuda_runtime_library_dirs()
    if not directories or platform.system() != "Linux":
        return directories

    current = os.environ.get("LD_LIBRARY_PATH", "")
    current_entries = [entry for entry in current.split(os.pathsep) if entry]
    missing = [directory for directory in directories if directory not in current_entries]
    if missing and os.environ.get(CUDA_REEXEC_FLAG) != "1":
        environment = os.environ.copy()
        environment["LD_LIBRARY_PATH"] = os.pathsep.join([*directories, *current_entries])
        environment[CUDA_REEXEC_FLAG] = "1"
        os.execvpe(sys.executable, [sys.executable, *sys.argv], environment)
    return directories


def _nvidia_smi() -> dict[str, Any]:
    executable = shutil.which("nvidia-smi")
    result: dict[str, Any] = {"available": bool(executable), "path": executable, "gpus": []}
    if not executable:
        return result
    try:
        completed = subprocess.run(
            [executable, "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        for line in completed.stdout.splitlines():
            fields = [field.strip() for field in line.split(",")]
            if fields:
                result["gpus"].append(
                    {
                        "name": fields[0],
                        "memory_total": fields[1] if len(fields) > 1 else None,
                        "driver_version": fields[2] if len(fields) > 2 else None,
                    }
                )
    except (OSError, subprocess.SubprocessError) as error:
        result["error"] = str(error)
    return result


def _rapidocr_session_providers(ocr: Any) -> dict[str, list[str]]:
    """Read providers from the public RapidOCR object layout defensively."""
    candidates = {
        "detector": ("text_det", "infer", "session"),
        "classifier": ("text_cls", "infer", "session"),
        "recognizer": ("text_rec", "session", "session"),
    }
    providers: dict[str, list[str]] = {}
    for name, attributes in candidates.items():
        current = ocr
        try:
            for attribute in attributes:
                current = getattr(current, attribute)
            providers[name] = list(current.get_providers())
        except (AttributeError, TypeError):
            providers[name] = []
    return providers


def _initialize_rapidocr(use_cuda: bool) -> tuple[Any, dict[str, list[str]]]:
    from rapidocr_onnxruntime import RapidOCR

    options: dict[str, Any] = {"print_verbose": False}
    if use_cuda:
        options.update(det_use_cuda=True, cls_use_cuda=True, rec_use_cuda=True)
    ocr = RapidOCR(**options)
    return ocr, _rapidocr_session_providers(ocr)


def _cpu_backend(report: dict[str, Any], requested_mode: str) -> dict[str, Any]:
    if importlib.util.find_spec("rapidocr_onnxruntime"):
        try:
            _, providers = _initialize_rapidocr(use_cuda=False)
            report.update(
                selected_backend="rapidocr-cpu",
                engine="rapidocr_onnxruntime",
                use_cuda=False,
                actual_providers=providers,
                reason="RapidOCR is available; selecting its CPU execution path.",
            )
            return report
        except Exception as error:  # The Tesseract fallback may still be usable.
            report["warnings"].append(f"RapidOCR CPU initialization failed: {error}")

    tesseract = shutil.which("tesseract")
    if tesseract:
        report.update(
            selected_backend="tesseract-cpu",
            engine="tesseract",
            use_cuda=False,
            tesseract_path=tesseract,
            reason="RapidOCR is unavailable; selecting the installed Tesseract CPU fallback.",
        )
        return report

    report.update(
        selected_backend="unavailable",
        engine=None,
        use_cuda=False,
        reason=(
            "No usable OCR engine was found. Install rapidocr_onnxruntime in the OCR Python "
            "environment or install Tesseract for CPU OCR."
        ),
    )
    if requested_mode == "gpu":
        report["warnings"].append("GPU OCR was required but could not be initialized.")
    return report


def select_ocr_backend(requested_mode: str = "auto") -> dict[str, Any]:
    """Return a validated OCR backend report.

    ``auto`` prefers CUDA, then RapidOCR CPU, then Tesseract CPU. ``gpu``
    requests CUDA but still reports the safe fallback instead of pretending it
    succeeded. Callers that require acceleration must reject non-CUDA reports.
    """
    if requested_mode not in {"auto", "gpu", "cpu"}:
        raise ValueError("requested_mode must be one of: auto, gpu, cpu")

    if requested_mode != "cpu":
        ensure_cuda_loader_path()

    nvidia = _nvidia_smi()
    gpu_names = [gpu["name"] for gpu in nvidia["gpus"]]
    report: dict[str, Any] = {
        "schema_version": 1,
        "python": sys.executable,
        "platform": platform.platform(),
        "requested_mode": requested_mode,
        "nvidia_smi": nvidia,
        "rtx_5070_laptop_detected": any(RTX_5070_LAPTOP_PATTERN.search(name) for name in gpu_names),
        "cuda_runtime_library_dirs": cuda_runtime_library_dirs(),
        "packages": {
            "rapidocr_onnxruntime": bool(importlib.util.find_spec("rapidocr_onnxruntime")),
            "onnxruntime": bool(importlib.util.find_spec("onnxruntime")),
            "tesseract": bool(shutil.which("tesseract")),
        },
        "warnings": [],
    }

    if report["packages"]["onnxruntime"]:
        try:
            import onnxruntime

            report["onnxruntime_version"] = onnxruntime.__version__
            report["onnxruntime_available_providers"] = onnxruntime.get_available_providers()
        except Exception as error:
            report["warnings"].append(f"Unable to inspect ONNX Runtime providers: {error}")
            report["onnxruntime_available_providers"] = []
    else:
        report["onnxruntime_available_providers"] = []

    gpu_preconditions = (
        bool(gpu_names)
        and report["packages"]["rapidocr_onnxruntime"]
        and "CUDAExecutionProvider" in report["onnxruntime_available_providers"]
    )
    if requested_mode != "cpu" and gpu_preconditions:
        try:
            _, providers = _initialize_rapidocr(use_cuda=True)
            all_cuda = bool(providers) and all(providers.values()) and all(
                "CUDAExecutionProvider" in stage for stage in providers.values()
            )
            if all_cuda:
                profile = "RTX 5070 Laptop" if report["rtx_5070_laptop_detected"] else "NVIDIA CUDA GPU"
                report.update(
                    selected_backend="rapidocr-cuda",
                    engine="rapidocr_onnxruntime",
                    use_cuda=True,
                    actual_providers=providers,
                    reason=f"{profile} detected and all RapidOCR stages initialized with CUDA.",
                )
                return report
            report["warnings"].append(
                "RapidOCR initialized without CUDA for every stage; falling back to CPU. "
                f"Actual providers: {providers}"
            )
        except Exception as error:
            report["warnings"].append(f"RapidOCR CUDA initialization failed: {error}")
    elif requested_mode == "gpu":
        report["warnings"].append(
            "GPU preconditions were not met (NVIDIA GPU, CUDAExecutionProvider, and RapidOCR are required)."
        )

    return _cpu_backend(report, requested_mode)


def initialize_selected_rapidocr(report: dict[str, Any]) -> Any:
    """Create RapidOCR for a backend report and verify it did not change backend."""
    backend = report.get("selected_backend")
    if backend not in {"rapidocr-cuda", "rapidocr-cpu"}:
        raise RuntimeError(f"RapidOCR was not selected: {backend}")
    ocr, providers = _initialize_rapidocr(use_cuda=backend == "rapidocr-cuda")
    if backend == "rapidocr-cuda" and not (
        providers and all(providers.values()) and all("CUDAExecutionProvider" in stage for stage in providers.values())
    ):
        raise RuntimeError(f"RapidOCR CUDA provider changed after selection: {providers}")
    return ocr
