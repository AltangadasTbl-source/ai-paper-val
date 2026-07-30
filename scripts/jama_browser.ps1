param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('eval', 'eval-file', 'navigate')]
    [string]$Command,
    [Parameter(Mandatory = $true)]
    [string]$Value,
    [int]$Port = 9222,
    [string]$DateRange
)

$ErrorActionPreference = 'Stop'
$utf8 = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8
$pages = Invoke-RestMethod -Uri ("http://127.0.0.1:{0}/json/list" -f $Port)
$matchingPages = @($pages | Where-Object { $_.type -eq 'page' -and $_.url -like '*jamanetwork.com*' })
$page = $matchingPages[0]
if (-not $page) { $page = @($pages | Where-Object { $_.type -eq 'page' })[0] }
if (-not $page) { throw 'No browser page is open in the local Chrome session.' }
$webSocketUrl = [string]$page.webSocketDebuggerUrl

$socket = [System.Net.WebSockets.ClientWebSocket]::new()
$tokenSource = [System.Threading.CancellationTokenSource]::new()
$token = $tokenSource.Token
$null = $socket.ConnectAsync([Uri]$webSocketUrl, $token).GetAwaiter().GetResult()

if ($Command -eq 'navigate') {
    $request = @{ id = 1; method = 'Page.navigate'; params = @{ url = $Value } }
} else {
    if ($Command -eq 'eval-file') {
        $Value = Get-Content -Raw -Path $Value
        if ($DateRange) { $Value = $Value.Replace('__DATE_RANGE__', $DateRange) }
    }
    $request = @{
        id = 1
        method = 'Runtime.evaluate'
        params = @{ expression = $Value; returnByValue = $true; awaitPromise = $true }
    }
}
$json = $request | ConvertTo-Json -Compress -Depth 8
$bytes = [Text.Encoding]::UTF8.GetBytes($json)
$segment = [ArraySegment[byte]]::new($bytes)
$null = $socket.SendAsync($segment, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, $token).GetAwaiter().GetResult()

while ($true) {
    $stream = [System.IO.MemoryStream]::new()
    do {
        $buffer = New-Object byte[] 65536
        $segment = [ArraySegment[byte]]::new($buffer)
        $result = $socket.ReceiveAsync($segment, $token).GetAwaiter().GetResult()
        $stream.Write($buffer, 0, $result.Count)
    } while (-not $result.EndOfMessage)
    $response = [Text.Encoding]::UTF8.GetString($stream.ToArray()) | ConvertFrom-Json
    $stream.Dispose()
    if ($response.id -eq 1) {
        $response | ConvertTo-Json -Depth 32
        break
    }
}
$socket.Dispose()
$tokenSource.Dispose()
