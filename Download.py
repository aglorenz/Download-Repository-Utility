# -*- coding: iso-8859-1 -*-
import subprocess, sys

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
    print_file('temp.txt')
##    ps_command = "./download_repo.ps1 -repoName 'JavaScript-Projects' -user 'jefflicano82' | Out-File -Encoding ASCII temp.txt"
##    result = run(ps_command)
##    if result.returncode != 0:
##        print("An error occured: %s", result.stderr)
##    else:
##        print("Download executed successfully!")
##        print_file('temp.txt')

    

