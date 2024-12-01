from customtkinter import CTk
import customtkinter as ctk
import tkinter as tk
from menu_principal import Main_menu
from login import Login
from game import Game
from settings import Settings

class GraphWarGame(CTk):
    def __init__(self):
        super().__init__()
        self.title("Graphwar") # Nom de la fenêtre
        self.windowList = [tk.Frame(self), tk.Frame(self), tk.Frame(self)] # On crée des placeholders pour pouvoir créer nos autres windows par la suite (pas optimal)

        self.rowconfigure(0, weight = 1, uniform = 'a') # Vertical
        self.columnconfigure(0, weight = 1, uniform = 'a') # Horizontal
        
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}") # Taille de la fenêtre selon la resolution de l'utilisateur

    def setupWindow(self):
        m = Main_menu(self)
        l = Login(self)
        s = Settings(self)
        g = Game(self)
        self.windowList = [m, l, s, g] # Liste avec tout les menus
        m.grid(row = 0, column = 0, sticky = 'nsew')

    def changeWindow(self, sindex, findex):
        if self.windowList[findex].winfo_ismapped():
            self.windowList[findex].grid_forget()
        self.windowList[sindex].grid(row = 0, column = 0, sticky = 'nsew')
        self.windowList[sindex].layout_widgets()
    
    def showWindow(self, sindex):
        self.windowList[sindex].layout_widgets
        self.windowList[sindex].grid(row = 0, column = 0)

    def quit_game(self): # Permet d'éviter le bug de ne pas pouvoir relancer 
        self.withdraw()
        self.quit()

if __name__ == "__main__":
    app = GraphWarGame()
    app.setupWindow()
    app.update
    app.protocol("WM_DELETE_WINDOW", app.quit_game)
    app.mainloop()