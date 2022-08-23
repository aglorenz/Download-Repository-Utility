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
from PIL import Image, ImageTk

# Import our other modules
import download_repo_func as dr_func

################
#    Colors    #
################
lt_grey = "#E3E3E3"
med_grey = "#C0C0C0"
orange = "#FF9600"
##dk_blue = "#004271"
txt_white = "#EAEBED"
white = "#FFF"
dk_blue = "#323232"


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

    self.master.config(bg=dk_blue)

    # images
    self.logo = ImageTk.PhotoImage(Image.open("TA_logo1.jpg"))
##    tk.Label(self.master, image = self.logo).place(x=0, y=0, relwidth=1, relheight=1)
    
    self.lbl_logo = tk.Label(self.master, image = self.logo)
    self.lbl_logo.grid(row=0, column=0)

    # Labels

        # Repo Source
    self.lbl_app = tk.Label(self.master, height=1, bg=dk_blue, fg=txt_white, font=("Verdana 24 bold underline"),
                                 text='Download Repository Utility')
    self.lbl_app.grid(row=0,column=1,padx=(20,0),pady=(25,18),sticky='w')

        # Repo URL
    self.lbl_repo_src = tk.Label(self.master, height=1, bg=dk_blue, fg=txt_white, font=("Verdana Bold", 12),
                                 text='Enter Repo URL:')
    self.lbl_repo_src.grid(row=1,column=0,padx=(20,0), pady=(0,5), sticky='w')

        # Select Repo Branch
    self.lbl_branch = tk.Label(self.master, height=1, bg=dk_blue, fg=txt_white, font=("Verdana Bold", 12),
                                 text='Repo Branch:')
    self.lbl_branch.grid(row=2, column=0, padx=(20,0), sticky='sw')

        # Execution Output
    self.lbl_output = tk.Label(self.master, height=1, bg=dk_blue, fg=txt_white, font=("Verdana Bold", 12),
                                 text='Program Output:')
    self.lbl_output.grid(row=4, column=0, padx=(20,0), pady=(20,0), sticky='w')

    ######################
    # Radio Button Frame #
    ######################
    
    self.br_frame=tk.Frame(self.master, relief="sunken", bd=1, bg=lt_grey)

    self.br_frame.grid(row=2,column=1,padx=(20,20),sticky='nswe')

    # Radio Buttons
    self.rb_var = tk.StringVar()  # all Radiobutton widgets will be set to this control variable
    
    self.rb_main = tk.Radiobutton(self.br_frame, anchor="w", font="Verdana 10", text="Main/Master", bg=lt_grey,
                                  command=lambda: dr_func.clr_branch(self.txt_branch),
                                  variable=self.rb_var, value="master", width=13)
    self.rb_main.grid(row=0, column=0)

##    self.rb_master = tk.Radiobutton(self.br_frame, anchor="w", text="Master", bg=lt_grey,
##                                    command=lambda: dr_func.clr_branch(self.txt_branch),
##                                    variable=self.rb_var, value="master", width=9)
##    self.rb_master.grid(row=0, column=1)

    self.rb_other = tk.Radiobutton(self.br_frame, anchor="w", text="Other:", bg=lt_grey,
                                   command=lambda: self.txt_branch.config(state="normal"),
                                   variable=self.rb_var, value="other", width=5)
    self.rb_other.grid(row=0, column=1)
    self.rb_var.set("master")  # set the default to Master.  Note: download works with master even if the 
                               # actual branch is main.  However, not vice versa.  So we use master


    # Radio Button Entry for custom branch name
    self.entry_branch = tk.Entry(self.br_frame, font="Verdana 12", validate="focusout",
                           state="disabled",
                           validatecommand=lambda:
                           dr_func.left_justify(self.entry_branch)) # left justify
    branch_tip = Hovertip(self.entry_branch,'Enter repo branch name',
                           hover_delay=500) # Tooltip
    self.entry_branch.grid(row=0, column=2)

    
    # Entry boxes

    # This is the function call to download the repo.  Since it needs to be called at least twice,
    # we assign the call to a string and then evalulate it when either download button pressed
    # or when the user hits the Enter key after pasting in the repo path.
    self.download = '''dr_func.download(self.entry_repo, self.entry_dest.get(),
                                        self.rb_var.get(), self.entry_branch.get(), self.txt_out)'''
        # Source URL
    self.entry_repo = tk.Entry(self.master, font="Verdana 12", validate="focusout",
                             validatecommand=lambda:
                             dr_func.left_justify(self.entry_repo)) # left justify
    entry_repo_tip = Hovertip(self.entry_repo,'Paste repository link, then press Enter',
                           hover_delay=500) # Tooltip
    self.entry_repo.grid(row=1, column=1, padx=(20,20), pady=(0,10), ipady=3, sticky='nswe')
        # download when enter key is pressed while cursor in Entry widget
    self.entry_repo.bind('<Return>', lambda event: eval(self.download))

        # Destination Path
    self.entry_dest = tk.Entry(self.master, font="Verdana 12")
    self.entry_dest.grid(row=3, column=1, padx=(20,20), pady=(10,0), sticky='nswe')

    # Buttons

        # Browse Destination Button
    self.btn_brws_dest = tk.Button(self.master, height=1, text='Browse Dest...', font=("Verdana", 12),
                                   bg=orange, command=lambda: dr_func.get_folder(self.entry_dest))
    btn_dest_tip = Hovertip(self.btn_brws_dest, 'Click to select Destination folder\n'
                            'Default is "C:\\temp"', hover_delay=500) # Tooltip
    self.btn_brws_dest.grid(row=3, column=0, padx=(24,0), pady=(10,0), sticky='we')

        # Download Repo Button
    self.btn_dwnld = tk.Button(self.master, height=2, text='Download Repo', font=("Verdana", 12),
                               bg=orange,
                               command=lambda: eval(self.download)) # download on button click
    btn_dwnld_tip = Hovertip(self.btn_dwnld,'Click to download and unzip\n'
                             'repo into desination folder.', hover_delay=500) # Tooltip
    self.btn_dwnld.grid(row=6, column=0, padx=(22,0), pady=(12,20), sticky='we')
    
        # Close application Button
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', font=("Verdana", 12),
                               bg=orange, fg=dk_blue, command=self.master.destroy)
    self.btn_close.grid(row=6, column=1, padx=(0,19), pady=(12,20), sticky='e')

    # set the Tab order so that download button immediately follows repository URL
    new_order = (self.entry_repo, self.btn_dwnld)
    for widget in new_order:
        widget.lift()

    # Text box

        # For capturing informational and error messages
    self.txt_out = tk.Text(self.master, font="Verdana 12", state="disabled", height=5)
    self.txt_out.grid(row=5, column=0, columnspan=2, padx=(22,20), pady=(0,0), sticky='nswe')

if __name__ == "__main__":
    pass
    

    
    
