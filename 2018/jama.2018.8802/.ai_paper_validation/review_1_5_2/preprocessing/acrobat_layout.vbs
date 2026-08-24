Option Explicit

If WScript.Arguments.Count <> 2 Then
  WScript.Echo "Usage: cscript acrobat_layout.vbs SOURCE_PDF OUTPUT_TSV"
  WScript.Quit 2
End If

Dim sourcePath, outputPath
sourcePath = WScript.Arguments(0)
outputPath = WScript.Arguments(1)

Dim app, avDoc, pdDoc, jsObj, fso, output, pageIndex, wordIndex, pageCount, wordCount
Dim token, quads, quad, xCoord, yCoord
Set app = CreateObject("AcroExch.App")
Set avDoc = CreateObject("AcroExch.AVDoc")
If Not avDoc.Open(sourcePath, "QC15 fresh coordinate-layout extraction") Then
  WScript.Echo "ERROR: Acrobat could not open " & sourcePath
  app.Exit
  WScript.Quit 3
End If

Set pdDoc = avDoc.GetPDDoc
pageCount = pdDoc.GetNumPages
Set jsObj = pdDoc.GetJSObject
Set fso = CreateObject("Scripting.FileSystemObject")
Set output = fso.CreateTextFile(outputPath, True, True)
output.WriteLine "PAGE" & vbTab & "WORD_INDEX" & vbTab & "X" & vbTab & "Y" & vbTab & "TOKEN"

For pageIndex = 0 To pageCount - 1
  wordCount = jsObj.getPageNumWords(pageIndex)
  For wordIndex = 0 To wordCount - 1
    token = jsObj.getPageNthWord(pageIndex, wordIndex, False)
    token = Replace(token, vbTab, " ")
    token = Replace(token, vbCr, " ")
    token = Replace(token, vbLf, " ")
    quads = jsObj.getPageNthWordQuads(pageIndex, wordIndex)
    xCoord = ""
    yCoord = ""
    If IsArray(quads) Then
      If UBound(quads) >= 0 Then
        quad = quads(0)
        If IsArray(quad) Then
          If UBound(quad) >= 7 Then
            xCoord = quad(0)
            yCoord = quad(1)
          End If
        End If
      End If
    End If
    output.WriteLine (pageIndex + 1) & vbTab & wordIndex & vbTab & xCoord & vbTab & yCoord & vbTab & token
  Next
  WScript.Echo "PAGE " & (pageIndex + 1) & " LAYOUT_WORDS " & wordCount
Next

output.Close
avDoc.Close True
app.Exit
WScript.Echo "COMPLETE PAGES " & pageCount & " OUTPUT " & outputPath
