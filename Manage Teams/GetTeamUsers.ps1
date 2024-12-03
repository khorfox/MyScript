#Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
#Install-Module -Name MicrosoftTeams -Scope CurrentUserOwner

import-module microsoftteams

#Get-TeamUser -GroupId 2f162b0e-36d2-4e15-8ba3-ba229cecdccf -Role 
$Accountid = "tl001023@telecomitalia.it"

Connect-MicrosoftTeams -AccountId $Accountid

$GroupId = "f3e7ebf3-7154-461b-9313-68d79ba3f67c"

$users = Get-TeamUser -GroupId $GroupId

Foreach($user in $users)
{
 Write-Output ("Utente:  " + $user.name + " Ruolo:  " + $user.role) 

}

$users | Export-Csv -Path utenti.csv