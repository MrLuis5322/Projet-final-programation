import tkinter as tk
from customtkinter import CTk

class Settings(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.rowconfigure() # Vertical 
        self.columnconfigure() # Horizontal
        self.grid(row = 0, column = 1, columnspan = 2, sticky = 'nsew')