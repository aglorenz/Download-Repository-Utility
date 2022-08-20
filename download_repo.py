# -*- coding: iso-8859-1 -*-
import subprocess, sys, os
from pathlib import Path
import tkinter as tk
import configparser

# Import our other modules
import download_repo_gui as dr_gui
import download_repo_func as dr_func
import config # This module allows us to create "global" values for access in other modules in this app

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(tk.Frame):
    
    def __init__(self, master, *args, **kwargs):
        
        tk.Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master

        # This CenterWindow method will center our app on the user's screen
        dr_func.center_window(self,760,360) # initial width and height
        
        self.master.title('Download GitHub Repo')
        self.master.config(bg="#C0C0C0")

        ##self.master.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
        self.master.columnconfigure(1,weight=1)
        self.master.rowconfigure(5,weight=1)

        # load in the GUI widgets from a separate module
        # keeping code compartmentalized and clutter free
        dr_gui.load_gui(self, config.base_name)

        # read the .ini file and display the saved destination folder in GUI
        ini_config = configparser.ConfigParser()
        # get the name of the .ini file from base_name in our config module
        ini_file = config.base_name + '.ini'
        ini_config.read(ini_file)
        #print(ini_config.sections())
        dest_folder = ini_config['zipfile.dest']['destination']
        
        self.txt_dest.insert(0,dest_folder)


if __name__ == "__main__":
    # set base_name in the config module so it can be accessed by other modules like a global var
    full_script_name = os.path.basename(__file__)  # like "download_repo.py"
    config.base_name = Path(full_script_name).stem # basename with no stem. like "download_repo"

    root = tk.Tk() # root = main window of the application
    App = ParentWindow(root)
    root.mainloop()


    

