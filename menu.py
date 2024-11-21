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
                                     fg_color='green')
        btn_tutorial.pack(pady=10)

        # Bouton pour l'apprentissage
        btn_learning = ctk.CTkButton(container, 
                                     text="Apprentissage",
                                     command=self.game.afficher_apprendre,  # Assurez-vous que cela appelle la bonne fonction
                                     width=200,
                                     height=50,
                                     corner_radius=20,
                                     fg_color='green')
        btn_learning.pack(pady=10)

        # Bouton pour quitter le jeu
        btn_quit = ctk.CTkButton(container, 
                                 width=200,
                                 height=50,
                                 corner_radius=20,
                                 text="Quitter", 
                                 command=self.game.quit_game,
                                 fg_color='red')
        btn_quit.pack(pady=10)

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
