#
# Python Ver:   3.9.5
#
# Author:       Andrew Lorenz
#
# Tested OS:  This code was written and tested to work with Windows 10.

'''
Module to set up the GUI for the file transfer application.

More Detailed description goes here (if necessary)

Functions:

    load_gui(self)
    
'''

# Using the wildcard is bad practice  W/O it, you have to explicitly state which tool kit you are using
# which makes for easier reading.  W/O it, you have to prefix widgets with the toolkit like so:  tk.Frame vs Frame
# from tkinter import *
import tkinter as tk
from idlelib.tooltip import Hovertip # Tooltips!

# Import our other modules
import download_repo_func

def load_gui(self, base_name):
    ''' Define the tkinter widgets and their initial
        configuration and place them using the grid geometry.

    Parameters
    ----------
    self : Frame
        The tkinter Frame in which this function will place widgets
    base_name : string
        The base_name of the main python file without extention ex: "download_repo"
        Retrieved after initialization from config.py module

    Returns
    -------
        None
        
    '''


    # Labels
    self.lbl_repo_src = tk.Label(self.master,height=1,bg="#C0C0C0",font=("Verdana", 12),
                                 text='Enter Repo URL:')
    self.lbl_repo_src.grid(row=0,column=1,padx=(20,0),pady=(20,0),sticky='w')

    self.sv = tk.StringVar()

    # Entry boxes
    self.txt_source = tk.Entry(self.master, font="Verdana 12", validate="focusout",
                               validatecommand=lambda:download_repo_func.left_justify(self.txt_source)) # left justify
    txt_source_tip = Hovertip(self.txt_source,'Enter repository link provided by student',
                           hover_delay=500) # Tooltip
    self.txt_source.grid(row=1,column=1,rowspan=1,padx=(20,20),pady=(0,0),ipady=1,sticky='nswe')
    self.txt_dest = tk.Entry(self.master, font="Verdana 12")
    self.txt_dest.grid(row=2,column=1,rowspan=1,padx=(20,20),pady=(10,0),sticky='nswe')

    # Buttons

    # Browse Dest 
    self.btn_brws_dest = tk.Button(self.master,width=12,height=1,text='Browse Dest...',
                                   command=lambda: download_repo_func.get_folder(self.txt_dest))
    btn_dest_tip = Hovertip(self.btn_brws_dest,'Click to select Destination folder\n'
                            'Default is "C:\\temp"', hover_delay=500) # Tooltip
    self.btn_brws_dest.grid(row=2,column=0,padx=(24,0),pady=(10,0),sticky='we')

    # Download Repo 
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Download Repo',
                               command=lambda: download_repo_func.download(self.txt_source.get(), self.txt_dest.get()))
    btn_check_tip = Hovertip(self.btn_check,'Click to download and unzip\n'
                             'repo into desination folder.', hover_delay=500) # Tooltip
    self.btn_check.grid(row=3,column=0, padx=(24,0),pady=(10,0),sticky='we')
    
    # Close application 
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=self.master.destroy)
    self.btn_close.grid(row=3,column=1, padx=(0,19),pady=(10,0),sticky='e')

if __name__ == "__main__":
    pass
    

    
    
