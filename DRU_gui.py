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

# Using the wildcard is bad practice  W/O it, you have to explicitly state which
# tool kit you are using (good practice) which makes for easier reading.
# W/O it, you have to prefix widgets with the toolkit like so:
# tk.Frame vs Frame
# from tkinter import *
import tkinter as tk, tkinter.ttk as ttk
from typing import Union


# from idlelib.tooltip import Hovertip # Tooltips!
from DRU_tooltip import Hovertip  # Tooltips!
from PIL import Image, ImageTk

# Import our other modules
import DRU_func

import pyglet
# The following works around the bug when pyglet imports a font and the
# filedialog.askdirectory() is called.  The bug manifests as the program
# freezing right before the filedialog window opens
from pyglet.libs.win32 import constants
constants.COINIT_MULTITHREADED = 0x2  # 0x2 = COINIT_APARTMENTTHREADED

# Add custom computer looking font
pyglet.font.add_file('./fonts/Venture13.ttf')

Widget = Union[tk.Widget, ttk.Widget] #

################
#    Colors    #
################

lt_grey = "#E3E3E3"
med_grey = "#C0C0C0"
white = "#FFF"
background = "#ebecee"  # light_grey
btn_fg = white
btn_bg = "#005faa"  # med-dark blue
lbl_color = btn_bg
logo_orng = "#fd750d"



def load_gui(self):
    ''' Define the tkinter widgets and their initial
        configuration and place them using the grid geometry.

    Parameters
    ----------
    self : Frame
        The tkinter Frame in which this function will place widgets

    Returns
    -------
        None
        
    '''

    self.master.config(bg=background)

    # Dictionary to save space when passing parms to widget_fn
    # Hover in and out colors for buttons
    dict_btn_hvr_in = {'bg_color': logo_orng, 'fg_color': btn_fg}
    dict_btn_hvr_out = {'bg_color': btn_bg, 'fg_color': btn_fg}
    ##########
    # Images #
    ##########

    # Even though the image had transparency, it wasn't transparent when
    # used in the app. Had to manually set the background color to the same
    # as that of the app. 
    img_logo=Image.open('./images/DRU-Logo.png')
    # this one has transparency needed for the favicon
    img_icon=Image.open('./images/DRU-Favicon-Thick.ico') # Thicker circle
    #img_icon=Image.open('./images/DRU-Favicon.png')

    # Resize the image in the given (width, height)
    logo=img_logo.resize((100,100))

    # Convert the images in TkImage
    self.logo=ImageTk.PhotoImage(logo)
    self.icon=ImageTk.PhotoImage(img_icon)

    # set the icon in the title bar
    self.master.iconphoto(False, self.icon) # 
        
    # must get rid of border or it shows
    self.lbl_logo = tk.Label(self.master, image=self.logo, borderwidth=0)
    lbl_logo_tip = Hovertip(self.lbl_logo,
                            'Designed and developed by:\n'
                            'Andrew Lorenz',
                            hover_delay=500) # Tooltip

    self.lbl_logo.grid(row=0, column=0, padx=(20,0), pady=(10,0))    

    ##########
    # Labels #
    ##########
    
        # Repo Source
    self.lbl_app = tk.Label(self.master, height=1, bg=background, fg=lbl_color,
                            font=("Venture13", 18, "underline"),
                            text='DOWNLOAD REPOSITORY UTILITY')
    self.lbl_app.grid(row=0,column=1,padx=(18,0),pady=(25,18),sticky='w')

        # Repo URL
    self.lbl_repo_src = tk.Label(self.master, height=1, bg=background,
                                 fg=lbl_color, font=("Venture13", 13),
                                 text='Enter Repo URL:')
    self.lbl_repo_src.grid(row=1,column=0,padx=(20,0), pady=(0,5), sticky='w')

        # Select Repo Branch
    self.lbl_branch = tk.Label(self.master, height=1, bg=background,
                               fg=lbl_color, font=("Venture13", 13),
                               text='Repo Branch:')
    self.lbl_branch.grid(row=2, column=0, padx=(20,0), sticky='sw')

        # Execution Output
    self.lbl_output = tk.Label(self.master, height=1, bg=background,
                               fg=lbl_color, font=("Venture13", 13),
                               text='Output:')
    self.lbl_output.grid(row=4, column=0, padx=(20,0), pady=(20,0), sticky='w')

    ######################
    # Radio Button Frame #
    ######################
    
        # subframe for the repo branch selection (radio buttons 'n entry widget)
    self.br_frame=tk.Frame(self.master, relief="sunken", bd=1, bg=lt_grey)

    self.br_frame.grid(row=2,column=1,padx=(20,20),sticky='nswe')

    # Radio Buttons
        # All Radiobutton widgets will be set to this control variable
    self.rb_var = tk.StringVar()
    
    self.rb_main = tk.Radiobutton(self.br_frame, anchor="w", font="Verdana 10",
                                  text="Main/Master", bg=lt_grey,
                                  command=lambda:
                                  DRU_func.clr_branch(self.entry_branch),
                                  variable=self.rb_var, value="master",
                                  width=13)
    rb_main_tip = Hovertip(self.rb_main,
                           'If repo contains either master or main but not\n'
                           'both, leave this selected.\n'
                           'If the repo contains both branches and you need\n'
                           'content from main, select "Other" and enter "main".',
                            hover_delay=500) # Tooltip
    
    self.rb_main.grid(row=0, column=0)

    self.rb_other = tk.Radiobutton(self.br_frame, anchor="w", font="Verdana 10",
                                   text="Other:", bg=lt_grey,
                                   command=lambda:
                                   self.entry_branch.config(state="normal"),
                                   variable=self.rb_var, value="other", width=5)
    rb_other_tip = Hovertip(self.rb_other,
                        'If the desired repo branch is other than main or\n'
                        'master, select this and enter the branch name.\n'
                        'If the repo contains master and main and you need\n'
                        'content from main, select this and enter "main".',
                        hover_delay=500) # Tooltip
    self.rb_other.grid(row=0, column=1)

        # Set the default to Master.  Note: download works with master even
        # if the actual branch is main.  However, not vice versa.  So we
        # use master.  Caveat:  If the repo has both branches and master/main
        # is selected, then only the master branch files will be downloaded.
        # User will need to select other and enter 'main' in that case.
    self.rb_var.set("master")

        # Radio Button Entry for custom branch name
    self.entry_branch = tk.Entry(self.br_frame, font="Verdana 12",
                        validate="focusout", state="disabled",
                        validatecommand=lambda:
                        DRU_func.left_justify(self.entry_branch)) # left justify
    branch_tip = Hovertip(self.entry_branch,'Enter repo branch name',
                          hover_delay=500) # Tooltip
    self.entry_branch.grid(row=0, column=2)

    ###############
    # Entry Boxes #
    ###############

        # This is the function call to download the repo.  Since it needs to
        # be called at least twice, we assign the call to a string and then
        # evalulate it when either download button pressed or when the user
        # hits the Enter key after pasting in the repo path.
        # New way to call w/o the parm clutter.  Self has access to everything.
    self.download = '''DRU_func.download(self)'''  
##    self.download = '''DRU_func.download(self, self.entry_repo,
##                       self.entry_dest.get(), self.rb_var.get(),
##                       self.entry_branch.get(), self.txt_out)'''
        # Source URL
        # Left justify it when the user moves out of the field.
        # Makes it easier to verify they got the whole URL
    self.entry_repo = tk.Entry(self.master, font="Verdana 12",
                               validate="focusout", validatecommand=lambda:
                               DRU_func.left_justify(self.entry_repo))
    entry_repo_tip = Hovertip(self.entry_repo,
                              'Paste   repository   link,   then\n'
                              'press  Enter  to begin  download. ',
                              hover_delay=500) # Tooltip
    self.entry_repo.grid(row=1, column=1, padx=(20,20), pady=(0,10),
                         ipady=3, sticky='nswe')
    self.entry_repo.focus() # set focus on startup for easy user entry
        # download when enter key is pressed while cursor in Entry widget
    self.entry_repo.bind('<Return>', lambda event: eval(self.download))

        # Destination Path
    self.entry_dest = tk.Entry(self.master, font="Verdana 12")
    self.entry_dest.grid(row=3, column=1, padx=(20,20),
                         pady=(10,0), sticky='nswe')

    ###########
    # Buttons #
    ###########

    '''fn() passed to hovertip class.  Enables us to change widget colors'''
    def widget_fn(target:Widget, bg_color:str, fg_color:str):
        #Widget.config(bg=color)
        target.config(bg=bg_color, fg=fg_color)

        # Browse Destination Button
    self.btn_brws_dest = tk.Button(self.master, height=1, text='Browse Dest...',
                                   font=("Venture13", 12), bg=btn_bg, fg=btn_fg,
                                   command=lambda:
                                   DRU_func.get_folder(self.entry_dest))

    Hovertip(self.btn_brws_dest,
             'Click to select Destination folder.\n'
             'Default is "C:/temp".', hover_delay=500,
             # unpack dict as parms by using **
             widget_fn_in=lambda: widget_fn(self.btn_brws_dest,
                                            **dict_btn_hvr_in),
             widget_fn_out=lambda: widget_fn(self.btn_brws_dest,
                                             **dict_btn_hvr_out))
    self.btn_brws_dest.grid(row=3, column=0, padx=(22,0), ipady=1,
                            pady=(12,0), sticky='we')

        # Download Repo Button
    self.btn_dwnld = tk.Button(self.master, height=2, text='Download Repo',
                               font=("Venture13", 13), bg=btn_bg, fg=btn_fg,
                               command=lambda: eval(self.download))
    Hovertip(self.btn_dwnld,
             'Click to download and unzip\n'
             'repo into destination folder.', hover_delay=500,
             widget_fn_in=lambda: widget_fn(self.btn_dwnld, **dict_btn_hvr_in),
             widget_fn_out=lambda: widget_fn(self.btn_dwnld,
                                             **dict_btn_hvr_out))
    self.btn_dwnld.grid(row=6, column=0, padx=(22,0), pady=(12,20),
                        sticky='we')
    
        # Close application Button
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close',
                               font=("Venture13", 13), bg=btn_bg, fg=btn_fg,
                               command=self.master.destroy)
    Hovertip(self.btn_close,
             None, hover_delay=None,
             widget_fn_in=lambda: widget_fn(self.btn_close, **dict_btn_hvr_in),
             widget_fn_out=lambda: widget_fn(self.btn_close, **dict_btn_hvr_out))
    self.btn_close.grid(row=6, column=1, padx=(0,19), pady=(12,20), sticky='e')

        # Set the Tab order so that download button immediately follows
        # repository URL
    new_order = (self.entry_repo, self.btn_dwnld)
    for widget in new_order:
        widget.lift()

    ##############
    # Text Boxes #
    ##############

        # For reporting informational and error messages
    self.txt_out = tk.Text(self.master, font="Verdana 12",
                           state="disabled", height=5)
    self.txt_out.grid(row=5, column=0, columnspan=2, padx=(22,20),
                      pady=(0,0), sticky='nswe')
        # tag for red error messages    
    self.txt_out.tag_configure('err', foreground="red")
        # tag for bold red error messages
    self.txt_out.tag_configure('err_bold', foreground="red",
                               font="Verdana 12 bold") 
        # tag for bold messages
    self.txt_out.tag_configure('bold', font="Verdana 12 bold") 
        # tag for blue bold info messages
    self.txt_out.tag_configure('info_bold', foreground="blue",
                                font="Verdana 12 bold") 

if __name__ == "__main__":
    pass
