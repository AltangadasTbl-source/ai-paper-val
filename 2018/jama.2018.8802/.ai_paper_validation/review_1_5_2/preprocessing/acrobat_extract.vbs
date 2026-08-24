Option Explicit

If WScript.Arguments.Count <> 2 Then
  WScript.Echo "Usage: cscript acrobat_extract.vbs SOURCE_PDF OUTPUT_TEXT"
  WScript.Quit 2
End If

Dim sourcePath, outputPath
sourcePath = WScript.Arguments(0)
outputPath = WScript.Arguments(1)

Dim app, avDoc, pdDoc, jsObj, fso, output, pageIndex, wordIndex, pageCount, wordCount, token
Set app = CreateObject("AcroExch.App")
Set avDoc = CreateObject("AcroExch.AVDoc")
If Not avDoc.Open(sourcePath, "QC15 fresh native-text extraction") Then
  WScript.Echo "ERROR: Acrobat could not open " & sourcePath
  app.Exit
  WScript.Quit 3
End If

Set pdDoc = avDoc.GetPDDoc
pageCount = pdDoc.GetNumPages
Set jsObj = pdDoc.GetJSObject
Set fso = CreateObject("Scripting.FileSystemObject")
Set output = fso.CreateTextFile(outputPath, True, True)

For pageIndex = 0 To pageCount - 1
  wordCount = jsObj.getPageNumWords(pageIndex)
  output.WriteLine "=== PDF PAGE " & (pageIndex + 1) & " | NATIVE WORDS " & wordCount & " ==="
  For wordIndex = 0 To wordCount - 1
    token = jsObj.getPageNthWord(pageIndex, wordIndex, False)
    If wordIndex > 0 Then output.Write " "
    output.Write token
  Next
  output.WriteLine
  output.WriteLine
  WScript.Echo "PAGE " & (pageIndex + 1) & " WORDS " & wordCount
Next

output.Close
avDoc.Close True
app.Exit
WScript.Echo "COMPLETE PAGES " & pageCount & " OUTPUT " & outputPath
