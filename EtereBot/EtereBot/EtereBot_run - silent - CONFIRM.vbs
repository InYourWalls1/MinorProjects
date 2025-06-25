response = MsgBox("Do you want to run the Bot?", vbYesNo, "EtereBot: running on start")

If response = vbYes Then
    Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run "cmd /c .\EtereBot_run.bat", 0, False
End If