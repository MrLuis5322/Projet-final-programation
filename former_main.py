import tkinter as tk
from customtkinter import CTk
from game import Accueil
from login import Formulaire
import numpy as np
from menu_principal import Menu

class GraphWarGame(CTk):
    def __init__(self):
        super().__init__()

        self.title("Graphwar")

        # Taille de la fenêtre
        window_width = 1920
        window_height = 1080

        # Obtenir la taille de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculer les coordonnées pour centrer la fenêtre
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        # Appliquer la position calculée
        self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        self.accueil = None
        self.formulaire = None
        self.nom_joueur_connecte = None
        
        self.show_menu()  # Afficher le menu principal
        self.creation_menu()

    def show_accueil(self):
        print("Affichage de l'écran d'accueil")
        self.clear_main_frame()  # Efface les widgets précédents
    
        if self.accueil:
            self.accueil.destroy()  # Détruire l'écran précédent si nécessaire
    
    # Créer une nouvelle instance de Accueil
        self.accueil = Accueil(self, res=1)
    
    # Utiliser grid() pour afficher l'écran d'accueil dans une grille
        self.accueil.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    # Configurer la grille pour permettre à l'écran d'accueil de s'adapter à la taille de la fenêtre
        self.grid_rowconfigure(0, weight=1)  # Permet à la ligne 0 de se redimensionner
        self.grid_columnconfigure(0, weight=1)  # Permet à la colonne 0 de se redimensionner

        print("Ecran d'accueil affiché")

    def show_formulaire(self):
        print("Essayer d'afficher le formulaire...")
        self.clear_main_frame()  # Efface les widgets précédents

    # Créez une nouvelle instance de formulaire
        self.formulaire = Formulaire(self)  # Crée une nouvelle instance de Formulaire

    # Utiliser place pour centrer le formulaire dans la fenêtre
        self.formulaire.place(relx=0.5, rely=0.5, anchor="center")

    # Configurer la grille pour permettre au formulaire de s'adapter
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def clear_main_frame(self):
        for widget in self.winfo_children():  # Pour chaque widget enfant
            widget.place_forget()  # Utilise place_forget() pour masquer les widgets

    def ajouter_log(self, message_log):
        if self.nom_joueur_connecte:
            # Construire le nom du fichier du joueur
            nom_fichier_joueur = self.clean_filename(self.nom_joueur_connecte)  # vérification des caractères speciaux pour pas qu'il aie de ?&"$?"& dans le nom du fichier
            # Ajout log
            self.formulaire.ajouter_log(nom_fichier_joueur, message_log)
        else:
            print("Aucun joueur connecté. Impossible d'ajouter un log.")

    def clean_filename(self, filename):
    # Remplacer les caractères invalides dans le nom de fichier
        caracteres_invalides = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in caracteres_invalides:
            filename = filename.replace(char, '_')
        return f"{filename}.txt"