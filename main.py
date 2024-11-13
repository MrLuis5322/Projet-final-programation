import tkinter as tk
from customtkinter import CTk
from accueil import Accueil
from formulaire import Formulaire
import numpy as np
from menu import Menu

class GraphWarGame(CTk):
    def __init__(self):
        super().__init__()

        self.title("Graphwar")

        self.geometry("1920x1080")  # Ajuste la taille de la fenêtre si nécessaire

        
        self.accueil = None
        self.formulaire = None
        self.nom_joueur_connecte = None
        
        self.show_menu()  # Afficher le menu principal
        self.creation_menu()

    def show_menu(self):
        self.clear_main_frame()
        self.menu = Menu(self, self)
        self.menu.pack(fill=tk.BOTH, expand=True)

    def creation_menu(self):
        menu_bar = tk.Menu(self) # Création de la bar de menu 
        self.config(menu=menu_bar) # Configuration du menu

        # Créer un menu Fichier
        file_menu = tk.Menu(menu_bar, tearoff=0) # Création de l'onglet fichier
        menu_bar.add_cascade(label="Fichier", menu=file_menu) # Ajout de l'onglet fichier
        file_menu.add_command(label="Jouer", command=self.show_accueil) # Ajout de la commande acceuil
        file_menu.add_command(label="Se connecter", command=self.show_formulaire) # Ajout de la commande formulaire
        file_menu.add_separator() # Ajout d'un séparateur après enrigistrer et avant quitter
        file_menu.add_command(label="Quitter", command=self.quit_game) # Ajout de la commande quitter
        
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
        print("Essayer d'afficher le formulaire...")
        self.clear_main_frame()  # Efface les widgets précédents

    # Créez une nouvelle instance de formulaire
        self.formulaire = Formulaire(self)  # Crée une nouvelle instance de Formulaire

    # Utiliser grid pour centrer le formulaire dans la fenêtre
        self.formulaire.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Configurer la grille pour centrer le formulaire
        self.grid_rowconfigure(0, weight=1)  # Permet à la ligne 0 de se redimensionner
        self.grid_columnconfigure(0, weight=1)  # Permet à la colonne 0 de se redimensionner


    # Créez une nouvelle instance de formulaire et centrez-la dans la fenêtre principale
        self.formulaire = Formulaire(self)  # Crée une nouvelle instance de Formulaire
    
    # Utiliser grid pour centrer le formulaire dans la fenêtre
        self.formulaire.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Configurer la grille pour centrer le formulaire
        self.grid_rowconfigure(0, weight=1)  # Permet à la ligne 0 de se redimensionner
        self.grid_columnconfigure(0, weight=1)  # Permet à la colonne 0 de se redimensionner




    def clear_main_frame(self):
        print("Effacement des widgets...")
        for widget in self.winfo_children():  # Pour chaque widget enfant
            print(f"Effacement du widget: {widget}")
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