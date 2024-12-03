Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process

# Creazione del connettore LDAP
$ldap = New-Object DirectoryServices.DirectoryEntry("LDAP://ldap.telecomitalia.local/O=Telecom Italia Group")

# Creazione del cercatore LDAP
$searcher = New-Object DirectoryServices.DirectorySearcher($ldap)

$users = import-csv c:\Temp\utentipotno.csv

$File   = 'C:\Temp\destinazioni.csv'
$Stream = [System.IO.StreamWriter]::new($File)
Foreach($user in $users)
{
	$emailAziendale = $user.User	
	Write-Output ("Cerco:  " + $emailAziendale) 
	$filter = "(&(objectClass=user)(mail=$emailAziendale))"
	$searcher.Filter = $filter
	$searcher.PropertiesToLoad.AddRange(@("displayName", "descrizStruttura", "manager", "*"))
	$results = $searcher.FindAll()
	$destinazione = ""
	$nome=""
	$department=""
	$company=""
	$trovato=$results.length
	Write-Host "Trovato: $trovato"
	if ($trovato -ne 1) {
		Write-Host "$emailAziendale NON TROVATO"
		$destinazione="NON TROVATO"
		$Stream.WriteLine($emailAziendale + ";" + $destinazione + ";" + $department + ";" + $company )
	} else {	
		foreach ($result in $results) {
			foreach ($propertyName in $result.Properties.PropertyNames) {
				if ($propertyName -eq "extensionattribute13"){
					$destinazione =$($result.Properties[$propertyName][0])
				}
				if ($propertyName -eq "displayname"){
					$nome =$($result.Properties[$propertyName][0])
				}
				if ($propertyName -eq "department"){
					$department =$($result.Properties[$propertyName][0])
				}
				if ($propertyName -eq "company"){
					$company =$($result.Properties[$propertyName][0])
				}
			 }
			 
			Write-Host "$nome - $destinazione"
			$Stream.WriteLine($nome + ";" + $destinazione + ";" + $department + ";" + $company )
		} 
	}	
}
$Stream.Close()	
