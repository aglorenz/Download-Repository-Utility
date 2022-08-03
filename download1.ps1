######################################################################
#                                                                    #
# Download and Unzip GitHub Repository                               #
# Author: Sandro Pereira                                             #
#                                                                    #
######################################################################

# function DownloadGitHubRepository 
# { 
    # param( 
       # [Parameter(Mandatory=$True)] 
       # [string] $repoName, 
        
       # [Parameter(Mandatory=$True)] 
       # [string] $author, 
        
       # [Parameter(Mandatory=$False)] 
       # [string] $branch = "master", 
        
       # [Parameter(Mandatory=$False)] 
       # [string] $destination = "c:\temp" 
    # ) 
	
$repoName = 'JavaScript-Projects'
$author = 'Eli-gav'
$branch = 'main'
$destination = 'C:\Users\Andy\Documents\_Student Repos'


# Force to create a zip file 
$zipFile = "$destination\$author-$repoName.zip" # prepend author name to differntiate other student's repos
$zipFile

New-Item $zipFile -ItemType File -Force  # | Out-Null # supress output with Out-Null

# this is the same way as when you click on the green download button
$repositoryZipUrl = "https://github.com/$author/$repoName/archive/$branch.zip"
#$repositoryZipUrl = "https://github.com/sandroasp/Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio/archive/master.zip"

# using the API instead
#$repositoryZipUrl = "https://api.github.com/repos/$author/$repoName/zipball/$branch"  
# download the zip 
Write-Host 'Starting downloading the GitHub Repository'
Invoke-RestMethod -Uri $repositoryZipUrl -OutFile $zipFile
Write-Host 'Download finished'

#Extract Zip File
Write-Host 'Starting unziping the GitHub Repository locally'
Expand-Archive -Path $zipFile -Force 
Write-Host 'Unzip finished'

# remove zip file
Remove-Item -Path $zipFile -Force 


#[String]$destination = Split-Path -Parent $PSCommandPath
#DownloadGithubRepository -Name 'Microsoft-Integration-and-Azure-Stencils-Pack-for-Visio' -Author 'sandroasp' -Location $destination