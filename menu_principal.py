import tkinter as tk
import customtkinter as ctk
import webbrowser  # Import pour ouvrir des liens dans le navigateur

class Main_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg = 'gray14')

        self.columnconfigure(0, weight = 1, uniform = 'a') # Vertical 
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight = 2, uniform = 'a') # Horizontal
        self.create_widgets()
        self.layout_widgets()
    
    def create_widgets(self):   
        # Création des boutons
        self.game_title = ctk.CTkLabel(master = self,
                                  text = 'GraphWar',
                                  width = 400,
                                  height = 100,
                                  fg_color= 'transparent',
                                  text_color = 'dark orange',
                                  font = ('Helvetica', 100))
        self.btn_play = ctk.CTkButton(master = self,
                                 width=300,
                                 height=75,
                                 corner_radius=50,
                                 text="Jouer", 
                                 font = ('Helvetica', 30),
                                 command=lambda:self.parent.changeWindow(3, 0), # Change la fenêtre pour jouer
                                 text_color='gray14',
                                 hover_color = 'orange',
                                 fg_color='dark orange')
        self.btn_login = ctk.CTkButton(master = self,
                                  text="Se connecter", 
                                  command=lambda:self.parent.showWindow(1), # Change la fenêtre pour login
                                  width=300,
                                  height=75,
                                  corner_radius=75,
                                  font = ('Helvetica', 30),
                                  text_color='gray14',
                                 hover_color = 'orange',
                                 fg_color='dark orange')
        self.btn_settings = ctk.CTkButton(master = self,
                                 width=300,
                                 height=75,
                                 corner_radius=75,
                                 text="Réglages", 
                                 font = ('Helvetica', 30),
                                 command=lambda:self.parent.showWindow(2), # Change le fenêtre pour les réglages
                                 text_color='gray14',
                                 hover_color = 'orange',
                                 fg_color='dark orange')
        self.btn_tutorial = ctk.CTkButton(master = self,
                                     text="Tutoriel",
                                     command=self.open_tutorial, # Ouvre le tutoriel
                                     width=300,
                                     height=75,
                                     corner_radius=75,
                                     font = ('Helvetica', 30),
                                     text_color='gray14',
                                 hover_color = 'orange',
                                 fg_color='dark orange')
        self.btn_quit = ctk.CTkButton(master = self,
                                 width=300,
                                 height=75,
                                 corner_radius=75,
                                 text="Quitter", 
                                 font = ('Helvetica', 30),
                                 command=self.parent.quit_game, # Quitte le jeux
                                 text_color='gray14',
                                 hover_color = 'orange',
                                 fg_color='dark orange')

    def layout_widgets(self):
        #Placement des boutons
        self.game_title.grid(row = 3, column = 0, rowspan = 2)
        self.btn_play.grid(row = 5, column = 0)
        self.btn_login.grid(row = 6, column = 0)
        self.btn_settings.grid(row = 7, column = 0)
        self.btn_tutorial.grid(row = 8, column = 0)
        self.btn_quit.grid(row = 9, column = 0)

    def open_tutorial(self):
        webbrowser.open("https://www.youtube.com/watch?v=EHuQe7SKwkA")  # Remplace par l'URL de la vidéo tutoriel
