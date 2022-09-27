#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

import subprocess, sys, os
from pathlib import Path
import tkinter as tk
import configparser

# Import our application modules
import download_repo_gui as dr_gui
import download_repo_func as dr_func
import download_repo_info_share as dr_is # This module allows us to create "global" values for access in other modules in this app

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(tk.Frame):
    
    def __init__(self, master, *args, **kwargs):
        
        tk.Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master

        # This CenterWindow method will center our app on the user's screen
        dr_func.center_window(self,760,458) # initial width and height
        
        self.master.title('D  R  U') # Download Repository Utility = D R U

        ##self.master.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches
        # with the size of the frame.  We don't want that.
        self.master.columnconfigure(1,weight=1)
        self.master.rowconfigure(5,weight=1)

        # Load in the GUI widgets from a separate module
        # keeping code compartmentalized and clutter free
        dr_gui.load_gui(self)

        ################################
        # Read the initialization file #
        ################################
        
        # Get the saved Zip file destination folder (from last run) and display it in the GUI
        # First create an object
        ini_config = configparser.ConfigParser()
        # Get the name of the .ini file from the base_name in our config module (avoids hardcoding)
        ini_file = dr_is.base_name + '.ini'  # value is set below in the if __name__ == "__main__":
        ini_config.read(ini_file)
        #print(ini_config.sections()) # Debug - to see contents of the ini file
        dest_folder = ini_config['zipfile.dest']['destination']
        
        self.entry_dest.insert(0,dest_folder)  # show the destination folder path in the GUI


if __name__ == "__main__":
    # Set base_name in the config module so it can be accessed by other modules like a global var
    full_script_name = os.path.basename(__file__)  # like "download_repo.py"
    dr_is.base_name = Path(full_script_name).stem # basename with no stem. like "download_repo"

    root = tk.Tk() # root = main window of the application
    App = ParentWindow(root)
    root.mainloop()


    

