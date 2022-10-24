######################################################################
#                                                                    #
# Download and Unzip GitHub Repository                               #
# Author: Sandro Pereira https://blog.sandro-pereira.com/2020/09/01  #
#          /how-to-download-a-github-repository-using-powershell/    #
# Modified:                                                          #
# 8/4/2022 Andrew Lorenz Tweaked for our needs   					 #
#                        Prerequisites: Powershell v5.1				 #
#                                                                    #
######################################################################
using assembly System.Net.Http
using namespace System.Net.Http
param( 
   [Parameter(Mandatory=$True)] 
   [string] $repoName, 
	
   [Parameter(Mandatory=$True)] 
   [string] $user, 
	
   [Parameter(Mandatory=$False)] 
   [string] $branch = "main", 
	
   [Parameter(Mandatory=$False)] 
   [string] $destination = "c:\temp" 
) 
$baseName = (Get-Item $PSCommandPath).BaseName # get name of script being executed
# write parms to log file
Get-Date
echo ""
echo "Application Base Name: $baseName"
echo "Repository Name: $repoName"
echo "User Name: $($user)"
echo "Repository Branch: $($branch)"
echo "Destination Folder: $($destination)"


# example
# $repoName = 'JavaScript-Projects'
# $user = 'jefflicano82'
# $branch = 'main'
# $destination = 'C:\Users\Andy\Documents\_Student Repos'

# Force to create a zip file 
$zipFile = "$destination/$user-$repoName.zip" # prepend user name to differentiate other student's repos
echo "Desintation Zip File: $zipFile"

#New-Item $zipFile -ItemType File -Force  # | Out-Null # supress output with Out-Null

# this is the same way as when you click on the green download button (supposedly)
$repositoryZipUrl = "https://github.com/$user/$repoName/archive/refs/heads/$branch.zip"
#$repositoryZipUrl = "https://github.com/$user/$repoName/archive/$branch.zip"
echo "Repository Zip File URL: $repositoryZipUrl"
echo ""

#$repositoryZipUrl = "https://github.com/sandroasp/Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio/archive/master.zip"

# using the API instead
#$repositoryZipUrl = "https://api.github.com/repos/$user/$repoName/zipball/$branch"  

# download the zip 
echo "Downloading: $repositoryZipUrl"
Try {
	#Invoke-RestMethod -Uri $repositoryZipUrl -OutFile $zipFile -ErrorAction stop 
	#Invoke-WebRequest -Uri $repositoryZipUrl -OutFile $zipFile -UseBasicParsing

# $webClient = [System.Net.WebClient]::new()
# # Download the file
# $webClient.DownloadFile($repositoryZipUrl, $zipFile)

	$wc = New-Object net.webclient
	#$wc.Headers.Add(Net.HttpRequestHeader.Cookie, "security=true") # trying to get around the "Too many automatic redirections were attempted" error
	#Write-Progress -Activity "Downloading $repoName" -Status "Downloaded $zipFile" -PercentComplete 10  # this is lame.  need a better way
	$wc.DownloadFile($repositoryZipUrl, $zipFile)


	# Create the HTTP client download request
	# $httpClient = New-Object System.Net.Http.HttpClient
	# $response = $httpClient.GetAsync($repositoryZipUrl)
	# $response.Wait()
	 
	# # Create a file stream pointed to the output file destination
	# $outputFileStream = [System.IO.FileStream]::new($zipFile, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write)
	 
	# # Stream the download to the destination file stream
	# $downloadTask = $response.Result.Content.CopyToAsync($outputFileStream)
	# $downloadTask.Wait()
	 
	# # Close the file stream
	# $outputFileStream.Close()	
	
	Write-Progress -Activity "Downloading $repoName" -Status "Downloaded $zipFile" -PercentComplete 100
}
#Catch [System.Net.WebException]{
Catch {
	echo "StatusCode: $($_.Exception.Response.StatusCode.value__)"
	echo "StatusDescription: $($_.Exception.Response.StatusDescription)"
	Write-Host $Error[0].Exception.GetType().FullName # gets name of error so you can catch it
	Write-Host $_.Exception.Message
	Write-Host "Ensure Repo is public and URL contains valid Username, Repository, and Branch."
	echo $_.Exception.Message
	exit 0  # Stop execution of the script with exit command.
			# Can't exit with 1 to signal an error because none of the messages above are returned in stdout or stderr 
			# stderr returns too much. I only want a little bit of text returned.  So I use stdout instead.
			# which captures messages written with Write-Host.  Using echo writes to the log file for more details.
	#return $_.Exception.Message 
}
echo "Download completed." ""

# $zipDest =  "$destination/$user-$repoName" # 
# # remove any trailing periods from the path
# while ($zipDest.EndsWith('.')) {$zipDest = $zipDest.TrimEnd('.')}
# echo "Destination Folder: $zipDest"

$userRepo =  "$destination/$user-$repoName" # 
# remove any trailing periods from the path
while ($userRepo.EndsWith('.')) {$userRepo = $userRepo.TrimEnd('.')}
echo "Destination Folder: $zipDest"


# #Create the destination folder if it doesn't exist ### may not need this section if the new rename below works
# if (Get-Item -Path $zipDest -ErrorAction Ignore) {
	# echo "" "Destination Folder Already Exists: $zipDest"
# }
# else {
	# echo "" "Destination Folder Does Not Exist."
	# echo "Creating Folder: $zipDest"
	# New-Item $zipDest -ItemType Directory
# }

#Extract Zip File
echo "" "Unziping File:  $zipFile"
echo    "To Folder:      $zipDest"
Try {
	#Expand-Archive -Path $zipFile -Force -DestinationPath $destination
	#Expand-Archive -Path $zipFile -Force 
	# using 7zip because it's faster and doesn't choke on archive subfolders with trailing spaces

	# Rename the top level folder in the zip file.
	#& ${env:ProgramFiles}\7-Zip\7z.exe rn  alejlo2594-JavaScript-Projects.zip JavaScript-Projects-main Andy
	& ${env:ProgramFiles}\7-Zip\7z.exe rn  $zipFile $repoName $userRepo
	& ${env:ProgramFiles}\7-Zip\7z.exe x $zipFile "-o$($destination)" -y # change $zipDest to $destination

#	& ${env:ProgramFiles}\7-Zip\7z.exe x $zipFile "-o$($zipDest)" -y # change $zipDest to $destination
}
Catch {
	echo "A problem occurred unzipping the file."
	Write-Host "An error occurred unzipping the file."
	Write-Host $Error[0].Exception.GetType().FullName
	Write-Host $_.Exception.Message
	exit 0
}
echo "Unzip completed." ""

	

#Rename-Item "D:\temp\Test Test1"
# Move zip file to the destination - Note: Expand-Archive has a bug:  when using -DestinationPath option, 
# it uses the name of the first folder in the zip file instead of the name of the zip file root.  
# Example:  if I have username-repo.zip and the first folder in the zip
# is repo, then the folder name is repo instead of username-repo.zip
#
# echo "Moving unzipped folder: $user-$repoName"
# echo "To: $destination"
#Move-Item $user-$repoName $destination
# echo "Move completed." ""

# Delete the zip file
echo "Deleting:  $zipFile"
#Remove-Item -Path $zipFile -Force 
echo "Zip file deleted." ""

# Open the unzipped top level repository folder in file explorer.  
# The top folder will be like, JavaScript-Projects-branch where branch is 'main', 'master' or other git branch
# The * in $repoName* is a wilcard that will match any branch.  Since a repository will only
# unzip into a single top level folder, we will normally only get one File Explorer window opened.  
# If for some reason there are are two repositories unzipped into the destination (perhaps you downloaded
# the master branch previously and now the main branch), then File explorer will open both in separate windows.  
echo "Opening Top Level Archive Folder"
#ii $destination\$user-$repoName\$repoName*
ii $destination\$user-$repoName\*    # current


#[String]$destination = Split-Path -Parent $PSCommandPath
#DownloadGithubRepository -Name 'Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio' -Author 'sandroasp' -Location $destination