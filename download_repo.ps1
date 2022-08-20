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
$baseName
$repoName
$user
$branch
$destination

# $repoName = 'JavaScript-Projects'
# $user = 'jefflicano82'
# $branch = 'main'
# $destination = 'C:\Users\Andy\Documents\_Student Repos'

# Force to create a zip file 
$zipFile = "$destination/$user-$repoName.zip" # prepend user name to differentiate other student's repos
$zipFile

#New-Item $zipFile -ItemType File -Force  # | Out-Null # supress output with Out-Null

# this is the same way as when you click on the green download button
$repositoryZipUrl = "https://github.com/$user/$repoName/archive/$branch.zip"
#$repositoryZipUrl = "https://github.com/sandroasp/Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio/archive/master.zip"

# using the API instead
#$repositoryZipUrl = "https://api.github.com/repos/$user/$repoName/zipball/$branch"  

# download the zip 
Write-Host 'Starting downloading the GitHub Repository'
Invoke-RestMethod -Uri $repositoryZipUrl -OutFile $zipFile
Write-Host 'Download finished'

#Extract Zip File
Write-Host 'Starting unziping the GitHub Repository locally'
#Expand-Archive -Path $zipFile -Force -DestinationPath $destination
Expand-Archive -Path $zipFile -Force 
Write-Host 'Unzip finished'

# move zip file to the destination - Expand-Archive has a bug:  when using -DestinationPath, it uses the name of the first folder in
# the zip file instead of the name of the zip file root.  Example:  if I have username-repo.zip and the first folder in the zip
# is repo, then the folder name is repo instead of username-repo.zip
#
Move-Item $user-$repoName $destination

# remove zip file
Remove-Item -Path $zipFile -Force 
# open unzipped folder for instructor use 
ii $destination\$user-$repoName


#[String]$destination = Split-Path -Parent $PSCommandPath
#DownloadGithubRepository -Name 'Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio' -Author 'sandroasp' -Location $destination