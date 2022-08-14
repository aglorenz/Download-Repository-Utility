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
import configparser # to write a .ini file
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
    # temporary execution policy so PS script can run.  (local scripts don't have to be signed for this to run)
    completed = subprocess.run(["powershell.exe", "-ExecutionPolicy", "RemoteSigned", "-Command", cmd], capture_output=True)
    return completed

def print_file(file_path):
    f = open(file_path, 'r')
    print(f.read())

def download(remote_url, unzip_dest):
    # save the dest folder path to an .ini file
    ini_config = configparser.ConfigParser()
    ini_config['zipfile.dest'] = {}
    ini_config['zipfile.dest']['destination'] = unzip_dest
    with open('download_repo.ini', 'w') as configfile:
              ini_config.write(configfile)

    base_name = config.base_name # get base name from our config module
    print(f"base_name = {base_name}")
    #remote_url = "https://github.com/Alisak1/JavaScript-Projects/blob/main/Basic%20JavaScript%20Projects/Movie%20Website/bootstrap4_project/academy_cinemas.html"
    parsed_url = remote_url.split("/")
    user_name = parsed_url[3] # assuming url in format like https://github.com/Alisak1/JavaScript-Projects/...
    repo_name = parsed_url[4]
    
    #repo_name = os.path.splitext(remote_url)[0]  # 'MyRepo'
    print(f"Username {user_name}, RepoName {repo_name}")
##    repo_name = 'JavaScript-Projects'
##    user_name = 'jefflicano82'
##    
##    ps_command = (f"./{base_name}.ps1 -repoName {repo_name} -user {user_name} -destination {unzip_dest}"
##                  f" | Out-File -Encoding ASCII {base_name}.log")
    ps_command = (f"./{base_name}.ps1 -repoName {repo_name} -user {user_name}"
                  f" | Out-File -Encoding ASCII {base_name}.log")
    print(ps_command)
    result = run(ps_command)
    if result.returncode != 0:
        print(f"An error occured: {result.stderr}")
    else:
        print("Download executed successfully!")
        print_file(f"{base_name}.log")






    
