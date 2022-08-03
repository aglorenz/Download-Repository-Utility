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

if __name__ == '__main__':
    ps_command = "./download1.ps1"
    result = run(ps_command)
    if result.returncode != 0:
        print("An error occured: %s", result.stderr)
    else:
        print("Download executed successfully!")

    

