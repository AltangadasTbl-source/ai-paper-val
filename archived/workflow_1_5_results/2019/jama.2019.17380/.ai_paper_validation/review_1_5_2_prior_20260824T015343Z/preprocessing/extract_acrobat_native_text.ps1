param(
    [Parameter(Mandatory = $true)][string]$PdfPath,
    [Parameter(Mandatory = $true)][string]$OutputPath,
    [int]$DeclaredPageCount = 0
)

$ErrorActionPreference = 'Stop'
$pddoc = New-Object -ComObject AcroExch.PDDoc
if (-not $pddoc.Open($PdfPath)) {
    throw "AcroExch.PDDoc could not open the direct PDF source: $PdfPath"
}

try {
    $acrobatPageCount = $pddoc.GetNumPages()
    $pageCount = if ($DeclaredPageCount -gt 0) { $DeclaredPageCount } else { $acrobatPageCount }
    $builder = New-Object System.Text.StringBuilder
    [void]$builder.AppendLine("# Fresh Acrobat native-text extraction")
    [void]$builder.AppendLine("# Source: $PdfPath")
    [void]$builder.AppendLine("# Acrobat PDDoc page count: $acrobatPageCount")
    [void]$builder.AppendLine("# Declared source-unit page count: $pageCount")
    for ($pageIndex = 0; $pageIndex -lt $pageCount; $pageIndex++) {
        $pageNumber = $pageIndex + 1
        [void]$builder.AppendLine()
        [void]$builder.AppendLine("===== PDF PAGE $pageNumber OF $pageCount =====")
        $page = $pddoc.AcquirePage($pageIndex)
        if ($null -eq $page) {
            [void]$builder.AppendLine("# No Acrobat page object was accessible for this declared source unit.")
            continue
        }
        $hilites = New-Object -ComObject AcroExch.HiliteList
        [void]$hilites.Add(0, 32767)
        $pageHilite = $page.CreatePageHilite($hilites)
        $segmentCount = $pageHilite.GetNumText()
        [void]$builder.AppendLine("# Acrobat text segments: $segmentCount")
        for ($segmentIndex = 0; $segmentIndex -lt $segmentCount; $segmentIndex++) {
            $segmentText = $pageHilite.GetText($segmentIndex)
            if ($null -ne $segmentText) {
                [void]$builder.AppendLine($segmentText)
            }
        }
    }
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($OutputPath, $builder.ToString(), $utf8NoBom)
    Write-Output ("PAGES={0};CHARS={1};OUTPUT={2}" -f $pageCount, $builder.Length, $OutputPath)
}
finally {
    $pddoc.Close()
    [void][System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($pddoc)
}
