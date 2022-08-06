# -*- coding: iso-8859-1 -*-
import subprocess, sys, os
from pathlib import Path

##p = subprocess.Popen(["powershell.exe", 
##              "C:\\Users\\Andy\\Documents\\_Student Repos\\download1.ps1"], 
##              stdout=sys.stdout)
##p.communicate()

##p = subprocess.Popen(["powershell.exe", 
##              "C:\\Users\\Andy\\Documents\\_Student Repos\\download1.ps1"], 
##              stdout=subprocess.PIPE)
##p_out, p_err = p.communicate()

def run(cmd):

    completed = subprocess.run(["powershell.exe", "-ExecutionPolicy", "RemoteSigned", "-Command", cmd], capture_output=True)
    return completed

def print_file(file_path):
    f = open(file_path, 'r')
    print(f.read())


if __name__ == '__main__':
    full_script_name = os.path.basename(__file__)  # like "download_repo.py"
    base_name = Path(full_script_name).stem # basename with no stem. like "download_repo"
    repo_name = 'JavaScript-Projects'
    user_name = 'jefflicano82'
    
    ps_command = f"./{base_name}.ps1 -repoName {repo_name} -user {user_name} | Out-File -Encoding ASCII {base_name}.log"
    result = run(ps_command)
    if result.returncode != 0:
        print(f"An error occured: {result.stderr}")
    else:
        print("Download executed successfully!")
        print_file(f"{base_name}.log")

    

