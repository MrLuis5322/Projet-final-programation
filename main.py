import tkinter as tk
from customtkinter import CTk
from accueil import Accueil
from formulaire import Formulaire
import numpy as np

class GraphWarGame(CTk):  # Définition de la classe principale pour le jeu
    def __init__(self):  # Constructeur de la classe
        super().__init__() # Super permet d'appeler plusieurs inheritance

        self.title("Graphwar")  # Définition du titre de la fenêtre

        screen_width = self.winfo_screenwidth() # Est égal à la largeur de l'écran de l'utilisateur
        screen_height = self.winfo_screenheight() # Est égal a la hauteur de l'écran de l'utilisateur
        res_width = screen_width / 1707 # Le facteur de résolution voulue basée sur la largeur
        res_height = screen_height / 1067 # Le facteur de résolution voulue basée sur la hauteur
        res = np.sqrt((res_height**2) + (res_width**2)) # Le facteur de résolution utilisé

        self.geometry(f"{screen_width}x{screen_height}")  # Définition de la taille de la fenêtre avec la resolution de lutilisateur

        self.accueil = Accueil(self, res) # Crée une instance accueil (notre main window)
        self.accueil.pack(fill=tk.BOTH, expand=True) # Place le layout de accueil

        self.creation_menu() # Appeler la fonction pour afficher le menu

        # Ajouter une zone de logs, ajout si on a le temps (problème en lien avec la réénitialisation)
        # self.zone_logs = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        # self.zone_logs.pack(padx=20, pady=20)

        self.formulaire = None # Aucun formulaire remplis
        self.nom_joueur_connecte = None # Aucun joueur connecté

    def creation_menu(self):
        menu_bar = tk.Menu(self) # Création de la bar de menu 
        self.config(menu=menu_bar) # Configuration du menu

        # Créer un menu Fichier
        file_menu = tk.Menu(menu_bar, tearoff=0) # Création de l'onglet fichier
        menu_bar.add_cascade(label="Fichier", menu=file_menu) # Ajout de l'onglet fichier
        file_menu.add_command(label="Ouvrir", command=self.open_file) # Ajout de la commande ouvrir
        file_menu.add_command(label="Enregistrer", command=self.save_file) # Ajout de la commande enregistrer
        file_menu.add_separator() # Ajout d'un séparateur après enrigistrer et avant quitter
        file_menu.add_command(label="Quitter", command=self.quit_game) # Ajout de la commande quitter

        # Créer un menu Affichage
        view_menu = tk.Menu(menu_bar, tearoff=0) # Création de l'onglet affichage
        menu_bar.add_cascade(label="Affichage", menu=view_menu) # Ajout de l'onglet affichage
        view_menu.add_command(label="Accueil", command=self.show_accueil) # Ajout de la commande acceuil
        view_menu.add_command(label="Formulaire", command=self.show_formulaire) # Ajout de la commande formulaire
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit_game

    def quit_game(self): # Permet d'éviter le bug de ne pas pouvoir relancer
        self.withdraw()
        self.quit()

    def open_file(self): # INCOMPLET: Nous pouvons compléter si nous avons le temps
        print("fichier ouvert")

    def save_file(self): # INCOMPLET: Nous pouvons compléter si nous avons le temps
        print("fichier enregistré")

    def show_accueil(self):
        self.clear_main_frame()  # Éfface les widgets précédents
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width = screen_width / 1707 # Le facteur de résolution voulue basée sur la largeur
        res_height = screen_height / 1067 # Le facteur de résolution voulue basée sur la hauteur
        res = (res_height + res_width) / 2 # Le facteur de résolution utilisé
        print("Accueil affiché")
        if self.accueil:
            self.accueil.destroy()
        self.accueil = Accueil(self, res)
        self.accueil.pack(fill=tk.BOTH, expand=True)

    def show_formulaire(self):
        self.clear_main_frame() 
        print("Formulaire affiché")
        self.formulaire = Formulaire(self)
        self.formulaire.pack(fill=tk.BOTH, expand=True)  # Afficher fomulaire

    def clear_main_frame(self): # Éfface tous les widgets enfants avant d'en ajouter de nouveaux
        for widget in self.winfo_children(): # Pour chaque widget
            widget.pack_forget()  # Utilise pack_forget() pour masquer les widgets

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

if __name__ == "__main__":  # Vérification si ce fichier est exécuté en tant que programme principal
    app = GraphWarGame()  # Création d'une instance de GraphWarGame
    app.update()  # Ajout de l'appel update() pour forcer le rendu de la fenêtre
    app.protocol("WM_DELETE_WINDOW", app.quit_game) # Permet d'éviter le bug lorsqu'on ferme la fenetre avec x
    app.mainloop()  # Démarrage de la boucle principale de l'application