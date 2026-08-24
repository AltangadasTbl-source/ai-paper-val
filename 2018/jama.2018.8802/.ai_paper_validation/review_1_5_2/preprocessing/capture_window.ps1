param(
    [Parameter(Mandatory = $true)][long]$WindowHandle,
    [Parameter(Mandatory = $true)][string]$OutputPath
)

$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public static class Qc15WindowCapture {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left; public int Top; public int Right; public int Bottom; }
    [DllImport("user32.dll")]
    public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
    [DllImport("user32.dll")]
    public static extern bool PrintWindow(IntPtr hWnd, IntPtr hdcBlt, uint flags);
}
"@

$handle = [IntPtr]$WindowHandle
$rect = New-Object Qc15WindowCapture+RECT
if (-not [Qc15WindowCapture]::GetWindowRect($handle, [ref]$rect)) {
    throw "GetWindowRect failed for handle $WindowHandle"
}
$width = $rect.Right - $rect.Left
$height = $rect.Bottom - $rect.Top
if ($width -lt 100 -or $height -lt 100) {
    throw "Window dimensions are invalid: ${width}x${height}"
}
$bitmap = New-Object System.Drawing.Bitmap($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$hdc = $graphics.GetHdc()
try {
    if (-not [Qc15WindowCapture]::PrintWindow($handle, $hdc, 2)) {
        throw "PrintWindow failed for handle $WindowHandle"
    }
} finally {
    $graphics.ReleaseHdc($hdc)
    $graphics.Dispose()
}
$bitmap.Save($OutputPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bitmap.Dispose()
Write-Output "Captured ${width}x${height} to $OutputPath"
