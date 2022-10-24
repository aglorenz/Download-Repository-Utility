#from tkinter import *
import tkinter as tk
#from tkinter import Frame
import temp_gui
import temp_func

class ParentWindow(tk.Frame):
    
    def __init__(self, master, *args, **kwargs):
        
        tk.Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master

        # This CenterWindow method will center our app on the user's screen
        temp_func.center_window(self,760,170) # initial width and height
        
        self.master.title('Download GitHub Repo')
        self.master.config(bg="#C0C0C0")

        ##self.master.columnconfigure(0,weight=1) # if I uncomment this, then column 0 stretches with the size of the frame.
        self.master.columnconfigure(1,weight=2)

        # load in the GUI widgets from a separate module
        # keeping code compartmentalized and clutter free
        temp_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
