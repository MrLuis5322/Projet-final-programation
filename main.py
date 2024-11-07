import tkinter as tk
from customtkinter import CTk
#NON
#import accueil as Accueil
#OUI
from accueil import Accueil
from formulaire import Formulaire


class GraphWarGame(CTk):  # Définition de la classe principale pour le jeu
    def __init__(self):  # Constructeur de la classe
        super().__init__()  

        self.title("Graphwar")  # Définition du titre de la fenêtre
        self.geometry("800x600")  # Définition de la taille de la fenêtre

        #Dimentions de l'ecran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width =1024/screen_width
        res_height = 800/screen_height


        self.accueil = Accueil(self,res_width,res_height)  # Création d'une classe Accueil
        self.accueil.pack(fill=tk.BOTH, expand=True)  # Ajout de l'interface Accueil à la fenêtre
     

        

        def show_accueil():
            self.accueil = Accueil(self, res_height, res_width)  # Création d'une classe Accueil
            self.accueil.pack(fill=tk.BOTH, expand=True)  # Ajout de l'interface Accueil à la fenêtre

        # Appeler la fonction pour afficher l'Accueil
        self.creation_menu()

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
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        res_width =1024/screen_width
        res_height = 800/screen_height
        print("Accueil affiché")
        self.clear_main_frame()
        self.accueil = Accueil(self, res_height, res_width)  # Création d'une classe Accueil
        self.accueil.pack(fill=tk.BOTH, expand=True)

    def show_formulaire(self):
        self.clear_main_frame()
        self.formulaire = Formulaire(self)
        self.formulaire.pack(fill=tk.BOTH, expand=True)

    def clear_main_frame(self):
        #Efface tous les widgets enfants avant d'en ajouter de nouveaux
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":  # Vérification si ce fichier est exécuté en tant que programme principal
    app = GraphWarGame()  # Création d'une instance de GraphWarGame
    app.update()  # Ajout de l'appel update() pour forcer le rendu de la fenêtre
    app.mainloop()  # Démarrage de la boucle principale de l'application
