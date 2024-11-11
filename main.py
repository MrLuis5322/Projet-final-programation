import tkinter as tk
from customtkinter import CTk
from accueil import Accueil
from formulaire import Formulaire

class GraphWarGame(CTk):  # Définition de la classe principale pour le jeu
    def __init__(self):  # Constructeur de la classe
        super().__init__() # Super permet d'appeler plusieurs inheritance

        self.title("Graphwar")  # Définition du titre de la fenêtre

        screen_width = self.winfo_screenwidth() # Est egal a la largeur de lecran de lutilisateur
        screen_height = self.winfo_screenheight() # Est egal a la hauteur de lecran de lutilisateur
        res_width = 2560 / screen_width # Le facteur de resolution voulue base sur la largeur
        res_height = 1600 / screen_height # Le facteur de resolution voulue base sur la hauteur

        self.geometry(f"{screen_width}x{screen_height}")  # Définition de la taille de la fenêtre avec la resolution de lutilisateur

        self.accueil = Accueil(self, res_width, res_height) # Cree une instance accueil (notre main window)
        self.accueil.pack(fill=tk.BOTH, expand=True) # Place le layout de accueil

        self.creation_menu() # Appeler la fonction pour afficher le menu

        # Ajouter une zone de logs NE FONCTIONNE PAS POSISION A CHANGER ET DISPARAIT LORSQUON LOG IN ***********************************************************
        self.zone_logs = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.zone_logs.pack(padx=20, pady=20)

        self.formulaire = None # Aucun formulaire remplis
        self.nom_joueur_connecte = None # Aucun joueur connecte

    def creation_menu(self):
        menu_bar = tk.Menu(self) # Creation de la bar de menu 
        self.config(menu=menu_bar) # Configuration du menu

        # Créer un menu Fichier
        file_menu = tk.Menu(menu_bar, tearoff=0) # Creation de longlet fichier
        menu_bar.add_cascade(label="Fichier", menu=file_menu) # Ajout de longelt fichier
        file_menu.add_command(label="Ouvrir", command=self.open_file) # Ajout de la commande ouvrir
        file_menu.add_command(label="Enregistrer", command=self.save_file) # Ajout de la commande enregistrer
        file_menu.add_separator() # Ajout dun separateur apres enrigistrer et avant quitter
        file_menu.add_command(label="Quitter", command=self.quit_game) # Ajout de la commande quitter

        # Créer un menu Affichage
        view_menu = tk.Menu(menu_bar, tearoff=0) # Creation de longlet affichage
        menu_bar.add_cascade(label="Affichage", menu=view_menu) # Ajout de longlet affichage
        view_menu.add_command(label="Accueil", command=self.show_accueil) # Ajout de la commande acceuil
        view_menu.add_command(label="Formulaire", command=self.show_formulaire) # Ajout de la commande formulaire
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit_game

    def quit_game(self): # Permet deviter le bug de ne pas pouvoir relancer
        self.withdraw()
        self.quit()

# GROS PROBLEMES A PARTIR DICI ********************************************************************************************************************************
    def open_file(self): #INCOMPLET ***************************************************************************************************************************
        print("fichier ouvert")

    def save_file(self): #INCOMPLET ***************************************************************************************************************************
        print("fichier enregistré")

    def show_accueil(self): # Je ne comprend pas a quoi ca sert ni pourquoi on en aurait de besoin. Tres mal fait si je comprend ce que c supposer faier ******
        self.clear_main_frame()  # Efface les widgets précédents
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width = 1024 / screen_width
        res_height = 800 / screen_height
        print("Accueil affiché")
        if self.accueil:
            self.accueil.destroy()
        self.accueil = Accueil(self, res_height, res_width)
        self.accueil.pack(fill=tk.BOTH, expand=True)

    def show_formulaire(self): # Same que plus haut mais je crois que elle elle est bien
        self.clear_main_frame() 
        print("Formulaire affiché")
        self.formulaire = Formulaire(self)
        self.formulaire.pack(fill=tk.BOTH, expand=True)  # Afficher fomulaire

    def clear_main_frame(self): # Efface tous les widgets enfants avant d'en ajouter de nouveaux
        for widget in self.winfo_children(): # Pour chaque widget
            widget.pack_forget()  # Utilise pack_forget() pour masquer les widgets ### ON PEUT PAS LE DELETE **************************************************

    def ajouter_log(self, message_log): # LES LOGS NE FONCTIONNENT PAS ****************************************************************************************
        if self.nom_joueur_connecte:
            # Construire le nom du fichier du joueur
            nom_fichier_joueur = self.clean_filename(self.nom_joueur_connecte)  #verification des caracteres speciaux pour pas qu,il aie de ?&"$?"& dans le nom du fichier
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
    app.protocol("WM_DELETE_WINDOW", app.quit_game) # Permet deviter le bug lorsque on ferme la fenetre avec x
    app.mainloop()  # Démarrage de la boucle principale de l'application
