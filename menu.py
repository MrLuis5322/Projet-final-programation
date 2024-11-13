import tkinter as tk
import customtkinter as ctk

class Menu(tk.Frame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.game = game
        self.place(relwidth=1, relheight=1)  # Utilisation de place ici pour occuper tout l'espace

        # Bouton pour accéder à l'accueil (Jouer)
        btn_play = ctk.CTkButton(self, 
                            width = 200,
                            height = 50,
                            corner_radius = 20,
                            text="Jouer", 
                            command=self.game.show_accueil,  # Appeler la méthode show_accueil de GraphWarGame
                            fg_color = 'blue')
        btn_play.place(x = 750, y = 250)  # Positionnement avec place

        # Bouton pour se connecter
        btn_login = ctk.CTkButton(self, 
                                  text="Se connecter", 
                                  command=self.game.show_formulaire,
                                  width = 200,
                                  height = 50,
                                  corner_radius = 20,
                                  fg_color = 'blue')
        btn_login.place(x = 750, y = 310)

        # Bouton pour quitter le jeu
        btn_quit = ctk.CTkButton(self, 
                                 width = 200,
                                 height = 50,
                                 corner_radius = 20,
                                 text="Quitter", 
                                 command=self.game.quit_game,
                                 fg_color = 'blue')
        btn_quit.place(x = 750, y = 370)

