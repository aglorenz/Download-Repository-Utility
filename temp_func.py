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
    print(sv.get())
    sv.delete(0,'end')
    sv.insert(0,"aaaaaaaa sldfj sldfj sdlfj sldfkj ")
##    sv.set("aaaaaaaa sldfj sldfj sdlfj sldfkj ")
    print(type(sv))
#    sv.xview_moveto(0)
##    sv.xview_moveto(.1)
    return True
##
##def left_justify(my_text):
##    my_text.xview_moveto(0)
##    return True
