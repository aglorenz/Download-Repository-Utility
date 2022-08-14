import temp_func
import tkinter as tk

def load_gui(self):
    sv = tk.StringVar()
    self.e = tk.Entry(self.master, textvariable=sv, validate="focusout",
                      validatecommand=lambda:temp_func.callback(self.e))
    self.e.grid()

