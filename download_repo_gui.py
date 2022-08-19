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
import download_repo_func as dr_func

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

        # Repo Source
    self.lbl_repo_src = tk.Label(self.master,height=1,bg="#C0C0C0",font=("Verdana", 12),
                                 text='Enter Repo URL:')
    self.lbl_repo_src.grid(row=0,column=1,padx=(20,0),pady=(20,0),sticky='w')

        # Choose Repo Branch
    self.lbl_branch = tk.Label(self.master, height=1, bg="#C0C0C0", font=("Verdana", 12),
                                 text='Select Branch:')
    self.lbl_branch.grid(row=2, column=0, padx=(20,0), pady=(0), sticky='w')

    #self.sv = tk.StringVar()

    ######################
    # Radio Button Frame #
    ######################
    med_grey = "#E3E3E3"
    
    self.br_frame=tk.Frame(self.master, relief="sunken", bd=1, bg=med_grey)

    self.br_frame.grid(row=2,column=1,padx=(20,20),sticky='nswe')

    # Radio Buttons
    self.rb_var = tk.StringVar()  # all Radiobutton widgets will be set to this control variable
    
    self.rb_main = tk.Radiobutton(self.br_frame, anchor="w", font="Verdana 10", text="Main", bg=med_grey,
                                  command=lambda: dr_func.clr_branch(self.txt_branch),
                                  variable=self.rb_var, value="main", width=7)
    self.rb_main.grid(row=0, column=0)

    self.rb_master = tk.Radiobutton(self.br_frame, anchor="w", text="Master", bg=med_grey,
                                    command=lambda: dr_func.clr_branch(self.txt_branch),
                                    variable=self.rb_var, value="master", width=9)
    self.rb_master.grid(row=0, column=1)

    self.rb_other = tk.Radiobutton(self.br_frame, anchor="w", text="Other:", bg=med_grey,
                                   command=lambda: self.txt_branch.config(state="normal"),
                                   variable=self.rb_var, value="other", width=5)
    self.rb_other.grid(row=0, column=2)
    self.rb_var.set("main")  # set the default to Main


    # Radio Button Entry for branch name
    self.txt_branch = tk.Entry(self.br_frame, font="Verdana 12", validate="focusout",
                           state="disabled",
                           validatecommand=lambda:
                           dr_func.left_justify(self.txt_branch)) # left justify
    branch_tip = Hovertip(self.txt_branch,'Enter repo branch name',
                           hover_delay=500) # Tooltip
    self.txt_branch.grid(row=0, column=3)

    
    # Entry boxes

    # This is the function call to download the repo.  Since it needs to be called at least twice,
    # assigning the call to a string and then evalulating it when download button pressed
    # or when the user hits the Enter key after pasting in the repo path.
    self.download = '''dr_func.download(self.txt_repo.get(), self.txt_dest.get(),
                                        self.rb_var.get(), self.txt_branch.get())'''
        # Source URL
    self.txt_repo = tk.Entry(self.master, font="Verdana 12", validate="focusout",
                             validatecommand=lambda:
                             dr_func.left_justify(self.txt_repo)) # left justify
    txt_repo_tip = Hovertip(self.txt_repo,'Enter repository link',
                           hover_delay=500) # Tooltip
    self.txt_repo.grid(row=1, column=1, rowspan=1, padx=(20,20), pady=(0,10), ipady=1, sticky='nswe')
    self.txt_repo.bind('<Return>', lambda event: eval(self.download))

        # Destination Path
    self.txt_dest = tk.Entry(self.master, font="Verdana 12")
    self.txt_dest.grid(row=3, column=1, rowspan=1, padx=(20,20), pady=(10,0), sticky='nswe')

    # Buttons

        # Browse Destination Button
    self.btn_brws_dest = tk.Button(self.master, width=12, height=1, text='Browse Dest...',
                                   command=lambda: dr_func.get_folder(self.txt_dest))
    btn_dest_tip = Hovertip(self.btn_brws_dest, 'Click to select Destination folder\n'
                            'Default is "C:\\temp"', hover_delay=500) # Tooltip
    self.btn_brws_dest.grid(row=3, column=0, padx=(24,0), pady=(10,0), sticky='we')

        # Download Repo Button
    self.btn_dwnld = tk.Button(self.master, width=12, height=2, text='Download Repo',
                               command=lambda: eval(self.download))
##                                                                self.rb_var.get(), self.txt_branch.get()))
    btn_dwnld_tip = Hovertip(self.btn_dwnld,'Click to download and unzip\n'
                             'repo into desination folder.', hover_delay=500) # Tooltip
    self.btn_dwnld.grid(row=4,column=0, padx=(24,0), pady=(12,0), sticky='we')
    
        # Close application Button
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program',
                               command=self.master.destroy)
    self.btn_close.grid(row=4,column=1, padx=(0,19), pady=(12,0), sticky='e')

    # set the Tab order so that download button immediately follows repository URL
    new_order = (self.txt_repo, self.btn_dwnld)
    for widget in new_order:
        widget.lift()


if __name__ == "__main__":
    pass
    

    
    
