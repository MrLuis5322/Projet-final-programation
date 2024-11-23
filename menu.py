import tkinter as tk
import customtkinter as ctk
import webbrowser  # Import pour ouvrir des liens dans le navigateur
from PIL import Image, ImageTk  # Import pour gérer les images
from apprendre import Apprendre

class Menu(tk.Frame):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.place(relwidth=1, relheight=1)  # Utilisation de place ici pour occuper tout l'espace

        # Initialiser l'image de fond (sans l'afficher immédiatement)
        self.bg_image = Image.open("background.jpg")  # Remplacez par le chemin de votre image
        self.bg_label = tk.Label(self)  # Créer un Label sans image pour le moment

        self.bg_label.place(relwidth=1, relheight=1)  # Placer le label dans toute la fenêtre
        
        # Utiliser `after` pour appeler la mise à jour de l'image après l'initialisation complète de la fenêtre
        self.after(100, self.update_background)  # Appeler la mise à jour après 100ms

         # Positionnement des boutons au centre de l'écran
        btn_width, btn_height = 200, 50
        spacing = 70  # Espacement vertical entre les boutons
        center_x, center_y = 960, 540  # Centre de la fenêtre (1920x1080)

        # Calcul des positions Y des boutons
        positions_y = [
            center_y - 2 * spacing,  # Bouton "Jouer"
            center_y - spacing,      # Bouton "Se connecter"
            center_y,                # Bouton "Tutoriel"
            center_y + spacing,      # Bouton "Apprentissage"
            center_y + 2 * spacing   # Bouton "Quitter"
        ]

        # Bouton pour accéder à l'accueil (Jouer)
        btn_play = ctk.CTkButton(self, 
                                 width=btn_width,
                                 height=btn_height,
                                 corner_radius=20,
                                 text="Jouer", 
                                 command=self.game.show_accueil, 
                                 fg_color='blue')
        btn_play.place(x=center_x - btn_width // 2, y=positions_y[0])

        # Bouton pour se connecter
        btn_login = ctk.CTkButton(self, 
                                  text="Se connecter", 
                                  command=self.game.show_formulaire,
                                  width=btn_width,
                                  height=btn_height,
                                  corner_radius=20,
                                  fg_color='blue')
        btn_login.place(x=center_x - btn_width // 2, y=positions_y[1])

        # Bouton pour le tutoriel
        btn_tutorial = ctk.CTkButton(self, 
                                     text="Tutoriel",
                                     command=self.open_tutorial,
                                     width=btn_width,
                                     height=btn_height,
                                     corner_radius=20,
                                     fg_color='green')
        btn_tutorial.place(x=center_x - btn_width // 2, y=positions_y[2])

        # Bouton pour l'apprentissage
        btn_learning = ctk.CTkButton(self, 
                                     text="Apprentissage",
                                     command=self.game.afficher_apprendre,
                                     width=btn_width,
                                     height=btn_height,
                                     corner_radius=20,
                                     fg_color='green')
        btn_learning.place(x=center_x - btn_width // 2, y=positions_y[3])

        # Bouton pour quitter le jeu
        btn_quit = ctk.CTkButton(self, 
                                 width=btn_width,
                                 height=btn_height,
                                 corner_radius=20,
                                 text="Quitter", 
                                 command=self.game.quit_game,
                                 fg_color='red')
        btn_quit.place(x=center_x - btn_width // 2, y=positions_y[4])

    def update_background(self):
        """Mise à jour de l'image de fond pour qu'elle remplisse la fenêtre"""
        # Redimensionner l'image de fond pour s'adapter à la taille actuelle de la fenêtre
        self.bg_image_resized = self.bg_image.resize((self.game.winfo_width(), self.game.winfo_height()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)  # Convertir en format compatible Tkinter

        self.bg_label.config(image=self.bg_photo)  # Assigner l'image redimensionnée au label
        self.bg_label.image = self.bg_photo  # Garder une référence à l'image pour éviter qu'elle ne soit supprimée

    def open_tutorial(self):
        """Ouvre le tutoriel dans le navigateur"""
        webbrowser.open("https://www.youtube.com/watch?v=EHuQe7SKwkA")  # Remplace par l'URL de la vidéo tutoriel 

    def open_learning_window(self):
        """Ouvre la fenêtre d'apprentissage"""
        apprendre_window = Apprendre(self)  # Crée une nouvelle instance de la fenêtre Apprendre
        apprendre_window.grab_set()  # Empêche de revenir à la fenêtre principale tant que celle-ci est ouverte
