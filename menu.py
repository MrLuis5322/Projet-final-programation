import tkinter as tk
import customtkinter as ctk
import webbrowser  # Import pour ouvrir des liens dans le navigateur
from apprendre import Apprendre


class Menu(tk.Frame):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.place(relwidth=1, relheight=1)  # Utilisation de place ici pour occuper tout l'espace

        # Conteneur central pour aligner les boutons verticalement au centre
        container = tk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")  # Centrer le conteneur au milieu de la fenêtre

        # Bouton pour accéder à l'accueil (Jouer)
        btn_play = ctk.CTkButton(container, 
                                 width=200,
                                 height=50,
                                 corner_radius=20,
                                 text="Jouer", 
                                 command=self.game.show_accueil, 
                                 fg_color='blue')
        btn_play.pack(pady=10)  # Espacement vertical entre les boutons

        # Bouton pour se connecter
        btn_login = ctk.CTkButton(container, 
                                  text="Se connecter", 
                                  command=self.game.show_formulaire,
                                  width=200,
                                  height=50,
                                  corner_radius=20,
                                  fg_color='blue')
        btn_login.pack(pady=10)

        # Bouton pour le tutoriel
        btn_tutorial = ctk.CTkButton(container, 
                                     text="Tutoriel",
                                     command=self.open_tutorial,
                                     width=200,
                                     height=50,
                                     corner_radius=20,
                                     fg_color='blue')
        btn_tutorial.pack(pady=10)

        # Bouton pour l'apprentissage
        btn_learning = ctk.CTkButton(container, 
                                     text="Apprentissage",
                                     command=self.game.afficher_apprendre,  # Assurez-vous que cela appelle la bonne fonction
                                     width=200,
                                     height=50,
                                     corner_radius=20,
                                     fg_color='blue')
        btn_learning.pack(pady=10)

        # Bouton pour quitter le jeu
        btn_quit = ctk.CTkButton(container, 
                                 width=200,
                                 height=50,
                                 corner_radius=20,
                                 text="Quitter", 
                                 command=self.game.quit_game,
                                 fg_color='blue')
        btn_quit.pack(pady=10)

    def open_tutorial(self):
        # Ouvre la vidéo YouTube dans un navigateur web
        webbrowser.open("https://www.youtube.com/watch?v=EHuQe7SKwkA")  # Remplace par l'URL de la vidéo tutoriel 

    def open_learning_window(self):
        # Ouvre la fenêtre d'apprentissage
        apprendre_window = Apprendre(self)  # Crée une nouvelle instance de la fenêtre Apprendre
        apprendre_window.grab_set()  # Empêche de revenir à la fenêtre principale tant que celle-ci est ouverte
