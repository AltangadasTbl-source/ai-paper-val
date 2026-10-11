# Workflow 1.6 Tooling Record

- **Probe UTC:** 2026-10-11T01:09:26Z
- **Platform:** linux
- **Direct tools available:** pdfinfo=yes; pdftotext=yes; pdftoppm=yes; pdftocairo=yes; tesseract=yes; libreoffice=yes; pandoc=yes
- **Fallback environment:** NOT_NEEDED
- **Fallback packages:** None
- **Fallback capabilities used:** None
- **Fallback environment removed:** NOT_CREATED
- **Tooling limitations:** None

Probe command: python3 workflow_1_6/scripts/pdf_tools.py probe. Python 3.14.4; direct tools under /usr/bin. Native and layout extraction use Poppler; rendered pages use Poppler; targeted OCR if needed uses Tesseract CPU; hashes use sha256sum. No global packages installed.

Direct engine versions: Poppler pdfinfo 26.01.0; Tesseract 5.5.0; Pandoc 3.7.0.2. Tool probe JSON: preprocessing/tool_probe.json.

Provider validation compatibility: the supplied auxiliary validator hard-codes openrouter. The explicit current-provider instruction authorizes openai. A preserved copy at tooling/current_provider/validate_review.py changes only that expected provider value; provider_override.diff and validator_hashes.sha256 document the exact change. Original template validation and current-provider validation will both be preserved. This does not change any scientific or integrity checks.
