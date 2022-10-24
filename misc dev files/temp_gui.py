import temp_func
import tkinter as tk

def load_gui(self):
    sv = tk.StringVar()
    self.e = tk.Entry(self.master, validate="focusout",
                      validatecommand=lambda:temp_func.callback(self.e))
# this way is more elegant, however it only works once, not repeatedly
# Update:  this is because the callback command must return True to keep the
# validate command On
##    self.e = tk.Entry(self.master, validate="focusout",
##                      validatecommand=lambda:self.e.xview(0))
    self.e.grid()

