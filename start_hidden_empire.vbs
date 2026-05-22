Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Auto_Traffic_Empire\run_all_modules.bat" & Chr(34), 0
Set WshShell = Nothing