import tkinter as tk
from customtkinter import CTk
#NON
#import accueil as Accueil
#OUI
from accueil import Accueil


class GraphWarGame(CTk):  # Définition de la classe principale pour le jeu
    def __init__(self):  # Constructeur de la classe
        super().__init__()  

        self.title("Graphwar")  # Définition du titre de la fenêtre
        self.geometry("800x600")  # Définition de la taille de la fenêtre

        self.accueil = Accueil(self)  # Création d'une classe Accueil
        self.accueil.pack(fill=tk.BOTH, expand=True)  # Ajout de l'interface Accueil à la fenêtre

if __name__ == "__main__":  # Vérification si ce fichier est exécuté en tant que programme principal
    app = GraphWarGame()  # Création d'une instance de GraphWarGame
    app.mainloop()  # Démarrage de la boucle principale de l'application


#executez et fermet un programme, il va apparaitre un message d'erreur. JSP comment fix ca. invalid command name "1143198609344update"...
