import tkinter as tk
from customtkinter import CTk
from accueil import Accueil
from formulaire import Formulaire

class GraphWarGame(CTk):  # Définition de la classe principale pour le jeu
    def __init__(self):  # Constructeur de la classe
        super().__init__()

        self.title("Graphwar")  # Définition du titre de la fenêtre
        self.geometry("800x600")  # Définition de la taille de la fenêtre

        # Dimensions de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width = 1024 / screen_width
        res_height = 800 / screen_height

        # Accueil par défaut
        self.accueil = Accueil(self, res_width, res_height)
        self.accueil.pack(fill=tk.BOTH, expand=True)

        # Appeler la fonction pour afficher le menu
        self.creation_menu()


        # Ajouter une zone de logs
        self.zone_logs = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.zone_logs.pack(padx=20, pady=20)

        # Initialisation du nom du formulaire
        self.formulaire = None
        self.nom_joueur_connecte = None

    def creation_menu(self):
        # Crée le menu principal
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Créer un menu Fichier
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Ouvrir", command=self.open_file)
        file_menu.add_command(label="Enregistrer", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

        # Créer un menu Affichage
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Affichage", menu=view_menu)
        view_menu.add_command(label="Accueil", command=self.show_accueil)
        view_menu.add_command(label="Formulaire", command=self.show_formulaire)

    def open_file(self):
        print("fichier ouvert")

    def save_file(self):
        print("fichier enregistré")

    def show_accueil(self):
        self.clear_main_frame()  # Efface les widgets précédents
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width = 1024 / screen_width
        res_height = 800 / screen_height
        print("Accueil affiché")

        self.accueil = Accueil(self, res_height, res_width)
        self.accueil.pack(fill=tk.BOTH, expand=True)

    def show_formulaire(self):
        
        self.clear_main_frame() 
        print("Formulaire affiché")
        
        self.formulaire = Formulaire(self)
        self.formulaire.pack(fill=tk.BOTH, expand=True)  # Afficher fomulaire



    def clear_main_frame(self):
        # Efface tous les widgets enfants avant d'en ajouter de nouveaux
        for widget in self.winfo_children():
            widget.pack_forget()  # Utilise pack_forget() pour masquer les widgets


    def ajouter_log(self, message_log):
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
    app.mainloop()  # Démarrage de la boucle principale de l'application
