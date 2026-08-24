param(
  [Parameter(Mandatory = $true)][string]$Title,
  [Parameter(Mandatory = $true)][string]$DocumentId,
  [Parameter(Mandatory = $true)][int]$PageCount,
  [Parameter(Mandatory = $true)][int]$Port
)

$ErrorActionPreference = "Stop"
$outputDirectory = "\\wsl.localhost\Ubuntu\home\juliz\ai-paper-val\2018\jama.2018.6496\.ai_paper_validation\review_1_5_2\preprocessing\rendered_pages"

function Invoke-Cdp {
  param($Socket, [int]$Id, [string]$Method, $Parameters)
  $payload = @{id = $Id; method = $Method; params = $Parameters} | ConvertTo-Json -Compress -Depth 8
  $bytes = [Text.Encoding]::UTF8.GetBytes($payload)
  $Socket.SendAsync(
    [ArraySegment[byte]]::new($bytes),
    [Net.WebSockets.WebSocketMessageType]::Text,
    $true,
    [Threading.CancellationToken]::None
  ).Wait()
  do {
    $stream = [IO.MemoryStream]::new()
    do {
      $buffer = New-Object byte[] 8388608
      $result = $Socket.ReceiveAsync(
        [ArraySegment[byte]]::new($buffer),
        [Threading.CancellationToken]::None
      ).Result
      $stream.Write($buffer, 0, $result.Count)
    } while (-not $result.EndOfMessage)
    $response = [Text.Encoding]::UTF8.GetString($stream.ToArray()) | ConvertFrom-Json
  } while ($response.id -ne $Id)
  return $response
}

for ($pageIndex = 0; $pageIndex -lt $PageCount; $pageIndex++) {
  $targets = (Invoke-WebRequest -UseBasicParsing "http://127.0.0.1:$Port/json/list").Content | ConvertFrom-Json
  $target = $targets | Where-Object { $_.type -eq "webview" -and $_.title -eq $Title } | Select-Object -First 1
  if (-not $target) { throw "PDF webview not found for $Title" }
  $socket = [Net.WebSockets.ClientWebSocket]::new()
  $socket.ConnectAsync([Uri]$target.webSocketDebuggerUrl, [Threading.CancellationToken]::None).Wait()
  $baseId = 1000 + ($pageIndex * 3)
  $expression = "(()=>{let p=document.querySelector(`"pdf-viewer`"),r=p.shadowRoot;r.querySelector(`"#sidenav`").style.display=`"none`";r.querySelector(`"#toolbar`").style.display=`"none`";r.querySelector(`"#sidenav-container`").style.width=`"0px`";r.querySelector(`"#main`").style.left=`"0px`";r.querySelector(`"#main`").style.width=`"100%`";window.dispatchEvent(new Event(`"resize`"));p.viewport_.fitToPage();p.viewport_.goToPage($pageIndex);return true})()"
  Invoke-Cdp $socket $baseId "Runtime.evaluate" @{expression = $expression; returnByValue = $true} | Out-Null
  Start-Sleep -Milliseconds 750
  $rectExpression = "JSON.stringify(document.querySelector(`"pdf-viewer`").viewport_.getPageScreenRect($pageIndex))"
  $rectResponse = Invoke-Cdp $socket ($baseId + 1) "Runtime.evaluate" @{expression = $rectExpression; returnByValue = $true}
  $rect = $rectResponse.result.result.value | ConvertFrom-Json
  $shot = Invoke-Cdp $socket ($baseId + 2) "Page.captureScreenshot" @{
    format = "png"
    captureBeyondViewport = $false
    clip = @{
      x = [double]$rect.x
      y = [double]$rect.y
      width = [double]$rect.width
      height = [double]$rect.height
      scale = 1
    }
  }
  $name = "{0}-page-{1:D3}.png" -f $DocumentId, ($pageIndex + 1)
  [IO.File]::WriteAllBytes((Join-Path $outputDirectory $name), [Convert]::FromBase64String($shot.result.data))
  $socket.Dispose()
  Write-Output $name
}
