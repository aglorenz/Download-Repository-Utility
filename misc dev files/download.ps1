$user = 'aglorenz'
$author = 'minifid'
$repo = 'Tech_academy_C_sharp_projects'
$pwdFilePath = '.\SecurePassword.txt'
#$uri = "https://api.github.com/repos/$user/$repo/zipball/"
$uri = "https://api.github.com/repos/$author/$repo/zipball"

# if password file exists (saved from previous execution of this script)

if (Test-Path -Path $pwdFilePath -PathType Leaf ) {
	# get secure string pwd from file, convert it to back to encrypted object and create a credential object
	if($pwdText = Get-Content $pwdFilePath) { #-ErrorAction Ignore
		"printing secure string" # for testing
#		$pwdText
		$securePwd = $pwdText | ConvertTo-SecureString
		# create cedential object
		$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $user, $securePwd
#		$cred
	} else {  # password is null
		"password is null"
		# create credential object
#		if(!$cred){$cred = Get-Credential -Message 'Provide GitHub credentials' -UserName $user}
		#$cred.GetNetworkCredential().Password # print out the password for testing
#		$cred

		# convert the encrypted "secure string"  password into a text-readable string (does not look like the original pwd)
#		$secureStringText = $cred.Password | ConvertFrom-SecureString
		# save password in local file for next use
#		Set-Content $pwdFilePath $secureStringText
	}
}
#exit
if(!$cred){$cred = Get-Credential -Message 'Provide GitHub credentials' -UserName $user}
$secureStringText = $cred.Password | ConvertFrom-SecureString
# save password in local file for next use
Set-Content $pwdFilePath $secureStringText

# Set up headers for the WebRequest to download the zip file
$headers = @{
  "Authorization" = "Basic " + [convert]::ToBase64String([char[]] ($cred.GetNetworkCredential().UserName + ':' + $cred.GetNetworkCredential().Password)) 
  "Accept" = "application/vnd.github.v3+json"
}
$response = Invoke-WebRequest -Method Get -Headers $headers -Uri $uri
$filename = $response.headers['content-disposition'].Split('=')[1]

# save the zip file to destination
Set-Content -Path (join-path "$HOME\Documents" $filename) -Encoding byte -Value $response.Content 