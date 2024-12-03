#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
import-module microsoftteams
#$User = "corrado.pollio@telecomitalia.it"
#$PassWord = ConvertTo-SecureString -String "1hundert_wasser" -AsPlainText -Force

#Write-Output $User

#$UserCredential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $PassWord
#Connect-MicrosoftTeams -Credential $UserCredential -AccountId $User

#$credential = Get-Credential
#Write-Output $credential
#Connect-MicrosoftTeams -Credential $credential

<#
file utenti.csv

UserId
francesco.tassone@telecomitalia.it

#>

$Accountid = "tl001023@telecomitalia.it"

Connect-MicrosoftTeams -AccountId $Accountid

<#

$teams = Get-Team -User $User

Foreach($team in $teams)
{
Write-Output ($team.GroupId + " - " + $team.DisplayName)
}

#>

$GroupId = "f3e7ebf3-7154-461b-9313-68d79ba3f67c"
$Role= "member"
#Add-TeamUser -GroupId $GroupId -User massimo.lanzetta@telecomitalia.it

$users = import-csv c:\Temp\utenti.csv

Foreach($user in $users)
{
 Write-Output ("Inserisco:  " + $user.UserId) 
 Add-TeamUser -GroupId $GroupId -User $user.UserId -Role $Role
}

