######################################################################
#                                                                    #
# Download and Unzip GitHub Repository                               #
# Author: Sandro Pereira https://blog.sandro-pereira.com/2020/09/01  #
#          /how-to-download-a-github-repository-using-powershell/    #
# Modified:                                                          #
# 8/4/2022 Andrew Lorenz Expanded for our needs   					 #
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

function date_time()
{
	# like 202210201936  yyyymmddhhmmss in 24 hr format
	return (Get-Date -UFormat "%Y%m%d%H%M%S").tostring() 
}

# get name of script being executed
$baseName = (Get-Item $PSCommandPath).BaseName 

# write parms to log file
Get-Date
echo ""
echo "Application Base Name: $baseName"
echo "Repository Name: $repoName"
echo "User Name: $($user)"
echo "Repository Branch: $($branch)"
echo "Destination Folder: $($destination)"

# prefix with user name to differentiate student's repos
$zipFile = "$destination/$user-$repoName.zip" 
echo "Desintation Zip File: $zipFile"

# Create the download URL
$repoZipURL = 
	"https://github.com/$user/$repoName/archive/refs/heads/$branch.zip"
echo "Repository Zip File URL: $repoZipURL"
echo ""

# Example of when using the API instead
# $repoZipURL = 
	# "https://api.github.com/repos/$user/$repoName/zipball/$branch"  

# download the zip 
echo "Downloading: $repoZipURL"
Try {
	# Sadly, these methods are too slow. We use Web Client instead 
	# even though no luck getting a progress bar to work.
	#Invoke-RestMethod -Uri $repoZipURL -OutFile $zipFile -ErrorAction stop 
	#Invoke-WebRequest -Uri $repoZipURL -OutFile $zipFile -UseBasicParsing
	$wc = New-Object net.webclient
	$wc.DownloadFile($repoZipURL, $zipFile)

# $webClient = [System.Net.WebClient]::new()
# # Download the file
# $webClient.DownloadFile($repoZipURL, $zipFile)

	$wc = New-Object net.webclient
	# trying to get around the "Too many automatic redirections were 
	# attempted" error
	#$wc.Headers.Add(Net.HttpRequestHeader.Cookie, "security=true") 
	# This method is very fast, but no progress bar
	$wc.DownloadFile($repoZipURL, $zipFile)  
	
	# Progress bar showing 100% complete
	Write-Progress -Activity "Downloading $repoName" `
		-Status "Downloaded $zipFile" -PercentComplete 100
}
#Catch [System.Net.WebException]{
Catch {
	echo "StatusCode: $($_.Exception.Response.StatusCode.value__)"
	echo "StatusDescription: $($_.Exception.Response.StatusDescription)"
	Write-Host $Error[0].Exception.GetType().FullName 
	Write-Host $_.Exception.Message
	Write-Host "Ensure Repo is public and URL contains valid Username, " `
			   "Repository, and Branch."
	echo $_.Exception.Message
	exit 0  # Stop execution of the script with exit command.
			# Can't exit with 1 to signal an error because none of the messages 
			# above are returned in stdout or stderr. 
			# We use stdout to capture specific messages written with 
			# Write-Host. We use echo to write to the log file for more details.
	#return $_.Exception.Message  # no can do.  Python can't deal with it.
}
echo "Download completed." ""

# $zipDest =  "$destination/$user-$repoName" 
# # remove any trailing periods from the path
# while ($zipDest.EndsWith('.')) {$zipDest = $zipDest.TrimEnd('.')}
# echo "Destination Folder: $zipDest"

$userRepo =  "$user-$repoName" # 
# remove any trailing periods from the path
while ($userRepo.EndsWith('.')) {$userRepo = $userRepo.TrimEnd('.')}
echo "Destination Folder: `"$destination`""

#Rename top level zip internal folder and then extract the zip file
Try {
	# Using 7zip instead of Expand-Archive. It's faster and doesn't choke
	# on archive subfolders that have trailing spaces.

	# Get the top level folder name in the zip file (this is the repo name 
	# with the branch appended)
	# 1) list the contents of the zip file w/o headers and save to a unique 
	# (for our purposes) file
	$archiveList = "DRU_Archive_List_" + (date_time) + ".tmp"
	echo "" "Zip file contents listed in this temp file: `"$archiveList`""
	& ${env:ProgramFiles}\7-Zip\7z.exe l -ba  $zipFile > $archiveList
	
	# 2) Get the first line in the file and parse the name of the top level 
	# folder. Like: JavaScript-Projects-main Since we don't know the branch 
	# name for sure (could be 'master', could be 'main'), we parse it. 
	# 7-zip rename folder cmd doesn't work with wildcards, otherwise we'd 
	# use something like JavaScript-Projects*
	$firstLine = Get-Content -Path $archiveList  -totalCount 1
	echo "First line in temp file: `"$firstLine`""
	
	# split line by space(s) to get the top folder name
	$topFolder = ($firstLine -split "\s+")[5] 
	echo "Zip file top folder name: `"$topFolder`""
	
	# Rename the top level folder in the zip file.
	echo "" "Renaming top level folder in archive: $zipFile"
	echo "From: `"$topFolder`""
	echo "To: `"$user-$topFolder`""
	& ${env:ProgramFiles}\7-Zip\7z.exe rn  $zipFile $topFolder $user-$topFolder
	echo "" "Unziping archive: `"$zipFile`""
	echo    "To folder: `"$destination`""
	& ${env:ProgramFiles}\7-Zip\7z.exe x $zipFile "-o$($destination)" -y 
}
Catch {
	echo "A problem occurred unzipping the file."
	Write-Host "An error occurred unzipping the file."
	Write-Host $Error[0].Exception.GetType().FullName
	Write-Host $_.Exception.Message
	exit 0
}
echo "Unzip completed." ""

# Delete the zip file
echo "Deleting zip file: $zipFile. . ."
Remove-Item -Path $zipFile -Force 
echo "Zip file deleted." ""

# Delete the tmp archive list file
echo "Deleting zip file content list: $destination/$archiveList. . ."
Remove-Item -Path $archiveList -Force 
echo "Zip file content list deleted." ""

# Open the unzipped top level repository folder in file explorer.  
# The top folder will be like: JavaScript-Projects-branch-main
echo "Opening unzipped top level repository. . ."
ii $destination\$user-$topFolder

echo "" "DRU done! :)"