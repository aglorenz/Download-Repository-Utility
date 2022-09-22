#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

'''
Module with functions to facilitate the file transfer application

Functions:

    center_window(self, w, h)
    get_folder(entry_box)
    run(cmd)
    print_file(file_path)
    download(remote_url, unzip_dest)
    
'''


import subprocess, sys, os
import configparser # to write a .ini file for the app
from pathlib import Path

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


import download_repo
import config  # to share info between modules

def center_window(self, w, h):
    '''Center the application window on the user's screen

    Parameters
    ----------
    self : Frame
        The tkinter Frame to center in the user's window
    w : int
        The width of the tkinter Frame
    h : int
        The height of the tkinter Frame

    Returns
    -------
        None
    '''
    
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's screen width
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def get_folder(entry_box):
    '''Browse for a file folder and store the folder path in an entry_box

    Parameters
    ----------
    entry_box : tkinter Entry widget
        Resulting folder path is stored in .ini file for next use

    Returns
    -------
        None    
    '''

    entry_box.delete(0,'end')
    folder_path = filedialog.askdirectory()
    entry_box.insert(0,folder_path)

##p = subprocess.Popen(["powershell.exe", 
##              "C:\\Users\\Andy\\Documents\\_Student Repos\\download1.ps1"], 
##              stdout=sys.stdout)
##p.communicate()

##p = subprocess.Popen(["powershell.exe", 
##              "C:\\Users\\Andy\\Documents\\_Student Repos\\download1.ps1"], 
##              stdout=subprocess.PIPE)
##p_out, p_err = p.communicate()

def run(cmd):
    # temporary execution policy so PS script can run.
    # (local scripts don't have to be signed for this to run)
    completed = subprocess.run(["powershell.exe", "-ExecutionPolicy", "RemoteSigned",
                                "-Command", cmd], capture_output=True,
                               text=True, check=True)
    print("Start")
    print(completed.returncode)
    print("End")
    return completed

def left_justify(entry_box):
    entry_box.xview(0)  # left justify contents to ensure view of first character
    return True         # must return true to keep the callback turned on

def clr_branch(entry_box):
    entry_box.delete(0,'end')
    entry_box.config(state="disabled")

# Remove trailing substr from a string. Repeat until no more trailing substrings
def trim_trailing(string, substr):
    while (string.endswith(substr)):
        string = string[:-len(substr)] # slice off the trailing substr
    return string

def print_file(file_path):
    f = open(file_path, 'r')
    print(f.read())

def validate_dest(unzip_dest, text_out):
    # set to a message for the text output if destination folder is auto-created
    dest_created = ""
    if not os.path.exists(unzip_dest):
        # create default directory if not exists
        unzip_dest = 'C:/temp'
        dest_created = " --Default folder"
        if not os.path.exists(unzip_dest):
            try:
                os.makedirs(unzip_dest) # , exist_ok=True)
                dest_created += " (Auto-created)\n"
            except OSError as e:
                text_out.insert('end', f"Fatal: {str(e)}\n", 'err_bold')
                text_out.insert('end', f"Cannot create folder: '{unzip_dest}'\n", 'err')
                text_out.config(state='disabled')
                sys.exit(1)
    text_out.insert('end',"Destination: ",'bold', f"'{unzip_dest}'",'info_bold',
                    f"{dest_created}\n")                
    return unzip_dest

def download(entry_repo, unzip_dest, btn_branch, alt_branch, text_out):
    # save the dest folder path to an .ini file
    ini_config = configparser.ConfigParser()
    ini_config['zipfile.dest'] = {}
    ini_config['zipfile.dest']['destination'] = unzip_dest
    with open('download_repo.ini', 'w') as configfile:
              ini_config.write(configfile)

    base_name = config.base_name # get base name from our config module

    # prepare the text box for output
    text_out.config(state='normal')
    text_out.delete(1.0,'end')

    # parse the repo URL to get user name and repository name
    
    try:
        remote_url = entry_repo.get()
        parsed_url = remote_url.split("/")
        # assuming url in format like https://github.com/Alisak1/JavaScript-Projects/...
        user_name = parsed_url[3] 
        repo_name = parsed_url[4]
        # remove all leading and trailing white space, then all trailing '.git's
        # -- GitHub repo names can't end with ".git"  Try creating one on GitHub, you'll see   
        repo_name = trim_trailing(repo_name.strip(), '.git')
        print(f"Trimmed repo = '{repo_name}'")
##        if len(repo_name) == 0:
##            raise IndexError


    except IndexError as e:
        text_out.insert('end', f"Fatal: {str(e)}\n", 'err_bold')
        text_out.insert('end', "Missing or bad formatting in Repo URL.\n", 'err')
        text_out.insert('end',
                        "Ensure URL contains valid Username and Repository like so:\n", 'err')
        text_out.insert('end',
                        "https://github.com/JoeSchmo/JavaScript-Projects/...", 'err_bold')
        text_out.config(state='disabled')
        sys.exit(1)
##        raise Exception("woops")  # this will end the program when not caught with except

    # Get the branch name            
    if (btn_branch == "other"):
        branch = alt_branch
    else:
        branch = btn_branch

    # output the important parameters to the text widget
    text_out.insert('end', f"{remote_url}\n")
    text_out.tag_add('info','end')
    text_out.insert('end',"User: ",'bold', f"'{user_name}'",'info_bold',
                          " | Repo: ",'bold', f"'{repo_name}'",'info_bold',
                          " | Branch: ",'bold', f"'{branch}'\n",'info_bold' )

    # Get the destination folder.  Default to C:\temp if empty or path doesn't exist
    # Create folder if needed.
    unzip_dest = validate_dest(unzip_dest, text_out)

##    text_out.insert('end',"Destination: ",'bold', f"\"{unzip_dest}\"" +
##                    dest_created, 'info_bold')
    
    # clear the repo entry field for next use
    entry_repo.delete(0,'end')

    print(f"Username={user_name}, RepoName={repo_name}, Branch={branch}")
    
    # Note: using "-Encoding ASCII" because Powershell 5.1 doesn't support
    # UTF-8 (without BOM) When usig UTF-8, the beginning of the output looks funky
    # However, using ASCII eliminates any special characters like ñ and results in
    # a ? instead.  Small risk considering what we are using this for.
    # Could possible start using Powershell Core, which allows UTF-8 (no BOM)
    # but testing will need to be done.
    # https://4sysops.com/wiki/differences-between-powershell-versions/
    ps_command = (f"./{base_name}.ps1 -repoName '{repo_name}' -user '{user_name}'"
                  f" -branch '{branch}' -destination '{unzip_dest}'"
                  f" | Out-File -Encoding ASCII {base_name}.log")
    print(ps_command)
    result = run(ps_command) 
    print(type(result))
    print(result.stdout)  # how do I capture the return code?
    text_out.insert('end', f"{result.stdout}", 'err_bold')
    text_out.config(state='disabled')
##        # If I manually set return code to 1 in powershell script to show an error,
          # then result never gets assigned and I can't examine anything else returned :(
##        print(f"An error occured: {e}")  # this fails with
          # "local variable 'result' referenced before assignment"
##        
##    if result.returncode != 0:
##        print(f"We have an error!  yay!!")
##    else:
##
##        print("Download executed successfully!")
##        #print_file(f"{base_name}.log")






    
