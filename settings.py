import tkinter as tk
import customtkinter as ctk  
import pywinstyles

class Settings(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configure(width = 800,
                       height = 800)

        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a') # Vertical 
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = 'a') # Horizontal

        pywinstyles.set_opacity(self, value = 0.9, color="#000001") # Permet de gérer l'opacité du widget
    
    def create_widgets(self):
        pass

    def layout_widgets(self):
        pass