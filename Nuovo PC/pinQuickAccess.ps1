#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#cd "C:\Users\TL001023\OneDrive - TIM\Script"

<#
To Unpin
QuickAccess = New-Object -ComObject shell.application 
($QuickAccess.Namespace("shell:::{679f85cb-0220-4080-b29b-5540cc05aab6}").Items() | where {$_.Path -eq "C:\Temp"}).InvokeVerb("unpinfromhome")
#>


# creare prima Temp

$o = new-object -com shell.application
#$o.Namespace('c:\Temp').Self.InvokeVerb("pintohome")

Write-Host "Inizio Elaborazione"
$Topin = @("c:\Temp","c:\Applicazioni","c:\Laboratorio","c:\Oracle","c:\ZZ-SoftwareFactory-0-Sviluppo","c:\ZZ-SoftwareFactory-1-Esercizio","C:\Users\TL001023")
ForEach ($dir in $Topin) { 
	Write-Host "Pin: " $dir
	$o.Namespace($dir).Self.InvokeVerb("pintohome")
}
Write-Host "Fine Elaborazione"