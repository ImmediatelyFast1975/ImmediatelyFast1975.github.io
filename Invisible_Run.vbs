Set WshShell = CreateObject("WScript.Shell")
' Kích nổ file .bat ngầm kịch trần, gán tham số 0 để giấu nhẹm cửa sổ đen CMD
WshShell.Run "cmd.exe /c C:\Auto Traffic Empire\run_autopilot.bat", 0, False