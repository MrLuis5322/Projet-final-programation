import tkinter as tk
from customtkinter import CTk
from accueil import Accueil
from formulaire import Formulaire
import numpy as np
from menu import Menu
from apprendre import Apprendre
from niveaux import Niveaux

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
        self.niveaux = None
        self.formulaire = None
        self.nom_joueur_connecte = None
        
        self.show_menu()  # Afficher le menu principal
        self.creation_menu()


    def show_menu(self):
        print("Retour au menu")  # Affichage dans le terminal pour déboguer
        self.clear_main_frame()  # Efface les widgets précédents
        self.menu = Menu(self)  # Créer une nouvelle instance de Menu

    # Forcer la mise à jour du fond d'écran
        self.menu.update_idletasks()  # Met à jour la fenêtre après avoir ajouté l'image de fond

    # Placer le menu et les autres widgets
        self.menu.place(relwidth=1, relheight=1)  # Utiliser place pour occuper toute la fenêtre

    # Forcer une mise à jour de la fenêtre après ajout du menu et de l'image de fond
        self.update()  # Met à jour la fenêtre (force le redessinage)



    def creation_menu(self):
        menu_bar = tk.Menu(self)  # Création de la barre de menu
        self.config(menu=menu_bar)  # Configuration du menu

        file_menu = tk.Menu(menu_bar, tearoff=0)  # Création de l'onglet fichier
        menu_bar.add_cascade(label="Fichier", menu=file_menu)  # Ajout de l'onglet fichier
        file_menu.add_command(label="Jouer", command=self.show_accueil)  # Commande pour afficher l'accueil
        file_menu.add_command(label="Niveaux", command=self.show_niveaux)
        file_menu.add_command(label="Se connecter", command=self.show_formulaire)  # Commande pour afficher le formulaire
        file_menu.add_command(label="Apprendre", command=self.afficher_apprendre)  # Nouveau bouton pour Apprendre
        file_menu.add_separator()  # Ajout d'un séparateur
        file_menu.add_command(label="Retour au menu", command=self.show_menu)  # Commande retour au menu
        file_menu.add_separator()  # Ajout d'un séparateur avant quitter
        file_menu.add_command(label="Quitter", command=self.quit_game)  # Commande pour quitter l'application
       


    def afficher_apprendre(self):
        print("Affichage de la fenêtre d'apprentissage")
        self.clear_main_frame()  # Efface les widgets précédents
        self.apprendre = Apprendre(self)  # Créer une nouvelle instance de Apprendre
        self.apprendre.place(relwidth=1, relheight=1)  # Afficher la fenêtre d'apprentissage dans la fenêtre principale


    def show_formulaire(self):
        print("Essayer d'afficher le formulaire...")
        self.clear_main_frame()  # Efface les widgets précédents

    # Créez une nouvelle instance de formulaire
        self.formulaire = Formulaire(self)  # Crée une nouvelle instance de Formulaire
    
        self.formulaire.place(relwidth=1, relheight=1)  # Afficher la fenêtre d'apprentissage dans la fenêtre principale
    
        print("Formulaire centré affiché")

        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit_game

    def quit_game(self): # Permet d'éviter le bug de ne pas pouvoir relancer
        self.withdraw()
        self.quit()

    

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

    def show_niveaux(self):
        print("Affichage de l'écran des niveaux")

        self.clear_main_frame()

        if self.niveaux:
            self.niveaux.destroy()
        
        self.niveaux = Niveaux(self,res = 1)

        self.niveaux.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Configurer la grille pour permettre à l'écran d'accueil de s'adapter à la taille de la fenêtre
        self.grid_rowconfigure(0, weight=1)  # Permet à la ligne 0 de se redimensionner
        self.grid_columnconfigure(0, weight=1)  # Permet à la colonne 0 de se redimensionner

        print("Ecran des niveaux affiché")








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

    def centrer_fenetre(self, largeur, hauteur):
        ecran_largeur = self.winfo_screenwidth()
        ecran_hauteur = self.winfo_screenheight()
        position_x = int((ecran_largeur - largeur) / 2)
        position_y = int((ecran_hauteur - hauteur) / 2)
        self.geometry(f"{largeur}x{hauteur}+{position_x}+{position_y}")



if __name__ == "__main__":  # Vérification si ce fichier est exécuté en tant que programme principal
    app = GraphWarGame()  # Création d'une instance de GraphWarGame 
    app.update()  # Ajout de l'appel update() pour forcer le rendu de la fenêtre
    app.protocol("WM_DELETE_WINDOW", app.quit_game) # Permet d'éviter le bug lorsqu'on ferme la fenetre avec x
    app.mainloop()  # Démarrage de la boucle principale de l'application