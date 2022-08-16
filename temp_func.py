import tkinter as tk

import temp

def center_window(self, w, h):
    
    # get User's screen width and height
    screen_width = self.master.winfo_screenwidth() # get user's screen width
    screen_height = self.master.winfo_screenheight() # and height
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

def callback(sv):
    repo = sv.get()
    print(repo)
    sv.xview(0) # left justify the text to view the first character in window.

    print(type(sv))
    return True # must return True to keep this function turned On

