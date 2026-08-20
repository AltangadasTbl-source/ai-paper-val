param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("gpu", "convert-doc")]
    [string]$Action,
    [Parameter(Position = 1)]
    [string]$InputPath,
    [Parameter(Position = 2)]
    [string]$OutputDirectory
)

$ErrorActionPreference = "Stop"

if ($Action -eq "gpu") {
    $gpuTool = Get-Command nvidia-smi.exe -ErrorAction SilentlyContinue
    if (-not $gpuTool) {
        $gpuTool = Get-Command nvidia-smi -ErrorAction SilentlyContinue
    }
    if (-not $gpuTool) {
        throw "nvidia-smi is not available on Windows."
    }
    & $gpuTool.Source --query-gpu=name,memory.total,driver_version --format=csv,noheader
    exit $LASTEXITCODE
}

if (-not (Test-Path -LiteralPath $InputPath -PathType Leaf)) {
    throw "Input document does not exist: $InputPath"
}
New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null

$officeCandidates = @(
    "C:\Program Files\LibreOffice\program\soffice.exe",
    "C:\Program Files (x86)\LibreOffice\program\soffice.exe"
)
$office = $officeCandidates | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
if (-not $office) {
    $command = Get-Command soffice.exe -ErrorAction SilentlyContinue
    if ($command) {
        $office = $command.Source
    }
}
if (-not $office) {
    throw "LibreOffice was not found on Windows."
}

$process = Start-Process -FilePath $office -ArgumentList @(
    "--headless",
    "--convert-to", "pdf",
    "--outdir", $OutputDirectory,
    $InputPath
) -NoNewWindow -Wait -PassThru
if ($process.ExitCode -ne 0) {
    throw "LibreOffice conversion failed with exit code $($process.ExitCode)."
}
