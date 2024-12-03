powershell Unblock-File -Path %~dp0Get-LargestTopFolders.ps1
powershell -ExecutionPolicy Unrestricted -Command %~dp0Get-LargestTopFolders.ps1 -Path "C:\Users\TL001023\AppData" -TopFolders 10

pause