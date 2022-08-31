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
import download_repo_gui as dr_gui
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
    # temporary execution policy so PS script can run.  (local scripts don't have to be signed for this to run)
    completed = subprocess.run(["powershell.exe", "-ExecutionPolicy", "RemoteSigned", "-Command", cmd], capture_output=True)
    return completed

def left_justify(entry_box):
    entry_box.xview(0)  # left justify contents to ensure view of first character
    return True         # must return true to keep the callback turned on

def clr_branch(entry_box):
    entry_box.delete(0,'end')
    entry_box.config(state="disabled")

def enable_branch_field(entry_box):
    entry_box.config(state="normal")

def disable_branch_field(entry_box):
    entry_box.config(state="disabled")

def print_file(file_path):
    f = open(file_path, 'r')
    print(f.read())

def download(entry_repo, unzip_dest, btn_branch, alt_branch, text_out):
    # save the dest folder path to an .ini file
    ini_config = configparser.ConfigParser()
    ini_config['zipfile.dest'] = {}
    ini_config['zipfile.dest']['destination'] = unzip_dest
    with open('download_repo.ini', 'w') as configfile:
              ini_config.write(configfile)

    base_name = config.base_name # get base name from our config module
    print(f"base_name = {base_name}")

    #remote_url = "https://github.com/Alisak1/JavaScript-Projects/blob/main/Basic%20JavaScript%20Projects/Movie%20Website/bootstrap4_project/academy_cinemas.html"
    remote_url = entry_repo.get()

    # If the remote url is empty, or is not a valid github url
    if remote_url == '' or remote_url.find('github.com') == -1:
        messagebox.showinfo("Error", "Please enter a valid link!")
        return

    parsed_url = remote_url.split("/")
    user_name = parsed_url[3] # assuming url in format like https://github.com/Alisak1/JavaScript-Projects/...
    repo_name = parsed_url[4]
    if (btn_branch == "other"):
        branch = alt_branch
        #Check to see if the branch exists in the repo
        cmd = f"git ls-remote --heads {user_name}/{repo_name} {branch}"
        print(f"cmd = {cmd}")
        completed = run(cmd)
        if completed.returncode != 0:
            messagebox.showinfo("Error", "Branch does not exist!")
            return
        else:
            print("Branch exists")
    else:
        branch = btn_branch
    
    # test write URL to text widget
    text_out.config(state='normal')
    text_out.delete(1.0,'end')
    text_out.insert('end', remote_url + '\n')
    text_out.insert('end','Hi Andy'+'\n')
    text_out.insert('end','Hi Andy')
    text_out.config(state='disabled')
    print(f"remote url = {remote_url}")

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
    ps_command = (f"./{base_name}.ps1 -repoName {repo_name} -user {user_name}"
                  f" -branch '{branch}' -destination '{unzip_dest}'"
                  f" | Out-File -Encoding ASCII {base_name}.log")
    print(ps_command)
    result = run(ps_command)
    if result.returncode != 0:
        print(f"An error occured: {result.stderr}")
    else:
        print("Download executed successfully!")
        print_file(f"{base_name}.log")
