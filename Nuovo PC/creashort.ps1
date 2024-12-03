#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#cd "C:\Users\TL001023\OneDrive - TIM\Script"

$LNKFILE = "C:\Users\TL001023\Desktop\PorTableApps.lnk"

Write-Host "Inizio Elaborazione" $LNKFILE
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$LNKFILE")
$Shortcut.TargetPath = "C:\Applicazioni\Start.exe"
$Shortcut.IconLocation = "C:\Applicazioni\Start.exe,0"
$Shortcut.WorkingDirectory = "."
$Shortcut.Save()

Write-Host "Fine Elaborazione"

$LNKFILE = "C:\Users\TL001023\Desktop\Sviluppo.lnk"

Write-Host "Inizio Elaborazione" $LNKFILE
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$LNKFILE")
$Shortcut.TargetPath = "C:\Applicazioni\Lupo_PenSuite_v2016_Zero\Lupo_PenSuite.exe"
$Shortcut.IconLocation = "C:\Applicazioni\Lupo_PenSuite_v2016_Zero\Lupo_PenSuite.exe,0"
$Shortcut.WorkingDirectory = "."
$Shortcut.Save()

Write-Host "Fine Elaborazione"

$LNKFILE = "C:\Users\TL001023\Desktop\ClientMenu.lnk"

Write-Host "Inizio Elaborazione" $LNKFILE
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$LNKFILE")
$Shortcut.TargetPath = "C:\Applicazioni\DynamicMenu\psmenu.exe"
$Shortcut.IconLocation = "C:\Applicazioni\DynamicMenu\psmenu.exe,0"
$Shortcut.WorkingDirectory = "."
$Shortcut.Save()

Write-Host "Fine Elaborazione"

$LNKFILE = "C:\Users\TL001023\Desktop\Postman.lnk"

Write-Host "Inizio Elaborazione" $LNKFILE
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$LNKFILE")
$Shortcut.TargetPath = "C:\Applicazioni\Postman\Postman.exe"
$Shortcut.IconLocation = "C:\Applicazioni\Postman\Postman.exe,0"
$Shortcut.WorkingDirectory = "."
$Shortcut.Save()

Write-Host "Fine Elaborazione"