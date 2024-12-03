@echo on
rem set TARGET='C:\Users\TL001023\OneDrive - TIM\Work Folders\Desktop\Notiziario_Tecnico_TIM_3_2022_Metaverso.pdf'
rem set SHORTCUT='C:\Users\TL001023\Desktop\Notiziario_Tecnico_TIM_3_2022_Metaverso.pdf.lnk'

set DIR_TARGET="C:\Users\TL001023\OneDrive - TIM\Work Folders\Desktop"
set DIR_SHORTCUT=C:\Users\TL001023\Desktop

set PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile

rem %PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(%SHORTCUT%); $S.TargetPath = %TARGET%; $S.Save()"

rem for /f "delims=" %%f in ('dir /b %DIR_TARGET%') do echo %%f 

for /f "delims=" %%f in ('dir /b %DIR_TARGET%') do (
 	%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('"%DIR_SHORTCUT%\%%f.lnk"'); $S.TargetPath = '"C:\Users\TL001023\OneDrive - TIM\Work Folders\Desktop\%%f"'; $S.Save()"
)

