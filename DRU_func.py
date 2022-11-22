#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

'''
Module with functions to facilitate the download repository app

Functions:

    center_window(self, w, h)
    get_folder(entry_box)
    run(cmd)
    left_justify(entry_box)
    clr_branch(entry_box)
    trim_trailing(string, substr)
    print_file(file_path)
    validate_dest(unzip_dest, text_out)
    download(remote_url, unzip_dest)
    
'''

import subprocess, sys, os
import configparser # to write a .ini file for the app
from pathlib import Path

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import DRU_gui
#import DRU
import DRU_info_share as DRU_is # to share info between modules

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
    # calculate x and y coords to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def get_folder(entry_box):
    '''
    Browse for a file folder and store the folder path in an entry widget

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

def run(cmd):
    '''
    Run a subprocess to execute a Powershell script.

    Parameters
    ----------
    cmd : powershell command to run.  It can be a script with parms

    Returns
    -------
    An obj of type subprocess.CompletedProcess

    obj.returncode : status of 1 or 0.  Lets us know if the actual subproces
        was successfull.  We can't pass data back from the powershell script
        in the return code.  If we try to exit the script with anything other
        than 0, then nothing gets returned back to python.

    obj.stdout : We can return info back to python using Write-Host in PS
        We use this for short and sweet error/info messages that get output to
        the user in the DRU text widget.
                
    '''


    # temporary execution policy so PS script can run.
    # (local scripts don't have to be signed for this to run)
    completed = subprocess.run(["powershell.exe", "-ExecutionPolicy",
                                "RemoteSigned", "-Command", cmd],
                               capture_output=True, text=True, check=True)
    return completed

def left_justify(entry_box):
    '''
    Left justify the content of a given entry widget.
    This will ensure visibility of first characters of user entry

    Parameters
    ----------
    entry_box : tkinter Entry widget

    Returns
    -------
    True : Must return True to keep the call back turned on.
    '''
    
    entry_box.xview(0)  # Left justify content so we can see first chars
    return True         # Must return True to keep the callback turned on

def clr_branch(entry_box):
    '''
    Clear and disable the given entry widget. Used for the custom branch entry.

    Parameters
    ----------
    entry_box : tkinter Entry widget

    Returns
    -------
    None    
    '''
    
    entry_box.delete(0,'end')
    entry_box.config(state="disabled")


def trim_trailing(input_str, substr):
    '''
    Remove trailing substr from a string. Repeat until no more trailing
    substrings

    Parameters
    ----------
    input_str : string to trim
    substr: substring to trim from input_str

    Returns
    -------
    input_str trimmed of all traling occurrences of substr
    '''

    while (input_str.endswith(substr)):
        input_str = input_str[:-len(substr)] # slice off the trailing substr
    return input_str

def print_file(file_path):
    '''
    Print the contents of a file.
    
    Parameters
    ----------
    file_path : path to the file to print

    Returns
    -------
    None
    '''

    f = open(file_path, 'r')
    print(f.read())

def validate_dest(unzip_dest, text_out):
    '''
    Validate the destination folder provided by user. If it doesn't exist, then
    the default location of c:\temp is used.  This is created if needed.
    
    Parameters
    ----------
    unzip_dest : folder that will contain the unzipped repository
    text_out : text widget for displaying application info and error output

    Returns
    -------
    The unzip destination.  Updated to the default path if the one provided
    doesn't exist.
    '''
    # This var will be set to a message for the text output if we have to create
    # the destination folder
    dest_created = ""
    # If the unzip destination doesn't exist, set to the default, C:/temp
    if not os.path.exists(unzip_dest):
        text_out.insert('end', "Warning: Destination Path Not Found: ",
                        'err_bold', f"'{unzip_dest}'\n", 'info_bold',
                        "Using Default Path Instead.\n", 'err_bold')
        unzip_dest = 'C:/temp'
        dest_created = " <--Default path"
        # Try to create the default folder if it doesn't exist
        if not os.path.exists(unzip_dest):
            try:
                os.makedirs(unzip_dest)
                dest_created += " (Auto-created)\n"
            except OSError as e:
                text_out.insert('end', f"Fatal: {str(e)}\n", 'err_bold')
                text_out.insert('end',
                                f"Cannot create folder: '{unzip_dest}'\n",
                                'err')
                text_out.config(state='disabled')
                return
    # Message to user
    text_out.insert('end',"Destination: ",'bold', f"'{unzip_dest}'",'info_bold',
                    f"{dest_created}\n")                
    return unzip_dest


def download(self):
    '''
    Download the GitHub repository.
    
    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    # get the values needed by this method
    base_name = DRU_is.base_name # get base name from our info share module
    ini_file = base_name + '.ini'

    entry_repo = self.entry_repo
    btn_branch = self.rb_var.get() # get the id of the radio button selected

    entry_branch = self.entry_branch
    alt_branch = entry_branch.get() # get branch name entered by user

    text_out = self.txt_out 
    unzip_dest = self.entry_dest.get() # get the dest folder entered by user

    # prepare the text box for output
    text_out.config(state='normal')
    text_out.delete(1.0,'end')

    # reset the branch back to master/main after capturing it above
    self.rb_var.set('master')
    clr_branch(entry_branch)

    # parse the repo URL to get user name and repository name
    
    try:
        remote_url = entry_repo.get()
        parsed_url = remote_url.split("/")
        # assuming url in format like https://github.com/username/JavaScript-Projects/...
        user_name = parsed_url[3] 
        repo_name = parsed_url[4]
        # remove all leading and trailing white space, then all trailing '.git's
        # -- GitHub repo names can't end with ".git"
        # Try creating one on GitHub as a test.
        repo_name = trim_trailing(repo_name.strip(), '.git')
        print(f"Trimmed repo = '{repo_name}'")
##        if len(repo_name) == 0:
##            raise IndexError


    except IndexError as e:
        text_out.insert('end', f"Fatal: {str(e)}\n", 'err_bold')
        text_out.insert('end', "Missing or bad formatting in Repo URL.\n",
                        'err')
        text_out.insert('end',
                        "Ensure URL contains valid Username and Repository",
                        'err')
        text_out.insert('end',
                        "like so:\n", 'err')
        text_out.insert('end',
                        "https://github.com/JoeSchmo/JavaScript-Projects/...",
                        'err_bold')
        text_out.config(state='disabled')
        return

        # Using sys.exit causes DRU to exit when run from shortcut in task bar.
        # sys.exit(1)  
        # raise exception will end the program when not caught with except
        # raise Exception("woops")  

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

    # Get the destination folder.  Default to C:\temp if empty or path doesn't
    # exist. Create folder if needed.
    unzip_dest = validate_dest(unzip_dest, text_out)
    # save updated dest to entry box
    self.entry_dest.delete(0,'end')
    self.entry_dest.insert(0,unzip_dest) 

    # save the dest folder path to an .ini file for next App start up
    ini_config = configparser.ConfigParser()
    ini_config['zipfile.dest'] = {}
    ini_config['zipfile.dest']['destination'] = unzip_dest
    with open(ini_file, 'w') as configfile:
              ini_config.write(configfile)

##    text_out.insert('end',"Destination: ",'bold', f"\"{unzip_dest}\"" +
##                    dest_created, 'info_bold')
    
    # clear the repo entry field for next use
    entry_repo.delete(0,'end')

    print(f"Username={user_name}, RepoName={repo_name}, Branch={branch}")
    
    # Note: using "-Encoding ASCII" because Powershell 5.1 doesn't support
    # UTF-8 without BOM. When usig UTF-8, the beginning of the output looks
    # funky
    # However, using ASCII eliminates any special characters like ñ and results
    # in a ? instead.  Small risk considering what we are using this for.
    # Could possibly start using Powershell Core, which allows UTF-8 (no BOM)
    # but testing will need to be done.
    # https://4sysops.com/wiki/differences-between-powershell-versions/
    ps_command = (f"./{base_name}.ps1 -repoName '{repo_name}'"
                  f" -user '{user_name}'"
                  f" -branch '{branch}' -destination '{unzip_dest}'"
                  f" | Out-File -Encoding ASCII {base_name}.log")
    print(ps_command)
    result = run(ps_command)
    print(type(result))
    print(result.stdout)  # how do I capture the return code?
    text_out.insert('end', f"{result.stdout}", 'err_bold')
    text_out.config(state='disabled')

# If I manually set return code to 1 in powershell script to show an error,
# then result never gets assigned and I can't examine anything else returned :(
#        print(f"An error occured: {e}")  # this fails with
# "local variable 'result' referenced before assignment"
##        
##    if result.returncode != 0:
##        print(f"We have an error!  yay!!")
##    else:
##
##        print("Download executed successfully!")
##        #print_file(f"{base_name}.log")

