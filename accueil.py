import tkinter as tk  
import customtkinter as ctk  
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importation pour intégrer Matplotlib avec tkinter
from joueur import Joueur  
from tir import Tir  
from traitementCSV import Obstacles
from matplotlib.patches import Circle

class Accueil(tk.Frame):  # Définition de la classe Accueil comme un frame tkinter
    def get_obstacles(self): # Fonction qui retourne les obstacles
        return self.obstacles
    
    def __init__(self, master, res): # Appel du constructeur
        super().__init__(master) # Super permet d'appeler plusieurs inheritance

        # On passe en parametre le facteur de resolution de lutilisateur et on le stock dans une variable
        self.res = res

        self.score = 0 # On set le score a 0
        self.temps = 121 # On set le temps a 120 secondes

        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        
        self.obstacles_instance = Obstacles() # Créer une instance de la classe Obstacles
        self.obstacles = self.obstacles_instance.generer_obstacles()  # Génération de la liste des obstacles
        self.joueur = Joueur(self, self.obstacles)  # Création d'une instance de Joueur
        self.tir = Tir(self)

        self.setup_ui()  # Appel de la méthode pour configurer l'interface utilisateur
        self.ax.legend(loc="upper left", prop = { "size": 15*res }, markerscale=0.6*res, bbox_to_anchor=(1, 1)) # Place la legend et definit sa taille selon la resolution de lutilisateur
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # Création d'un canvas pour afficher la figure
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Ajout du canvas à la fenêtre

        self.update_timer()

        self.cibles_touche = 0
        self.viles_touche = 0

    def setup_ui(self): # Méthode pour configurer l'interface utilisateur

        # Définition des types de fonctions disponibles dans le menu déroulant(a ajouter)
        self.function_types = {
            "Linéaire": "x",
            "Quadratique": "0.01*x**2",
            "Exponentielle": "np.exp(x)",
            "Sinus": "np.sin(x*0.1)*10",
            "Cosinus": "np.cos(x)",
        }

        # Création d'une combo box pour sélectionner le type de fonction
        self.func_selector = ctk.CTkComboBox(self, values=list(self.function_types.keys()), command=self.tir.plot_selected_function)
        self.func_selector.pack(pady=10)  # Ajout de la combo box à la fenêtre

        # Création d'une entrée pour que l'utilisateur saisisse une fonction
        self.entry_func = ctk.CTkEntry(self, placeholder_text="Entrez une fonction")
        self.entry_func.pack(pady=10)  # Ajout de l'entrée à la fenêtre
        
        # Création d'un bouton pour tracer la fonction saisie
        self.plot_button = ctk.CTkButton(self, text="Tracer la fonction", command=self.tir.plot_function)
        self.plot_button.pack(pady=10)  # Ajout du bouton à la fenêtre

        # Création d'un bouton pour réinitialiser le tracé
        self.reset_button = ctk.CTkButton(self, text="Réinitialiser", command=self.tir.reset_plot)
        self.reset_button.pack(pady=10)  # Ajout du bouton à la fenêtre

        #Affichage minuterie et score
        self.score_label = ctk.CTkLabel(self, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)
        self.timer_label = ctk.CTkLabel(self, text=f"Temps restant: {self.temps}s")
        self.timer_label.pack(pady=10)

        # N'afficher que le millieu des graduations (sinon le jeu est trop facile)
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.plot_obstacles_and_goal() # Appel de la méthode pour tracer les obstacles et la cible

    def update_timer(self):
        #Diminue la minuterie et met à jour l'affichage
        if self.temps > 0:
            self.temps -= 1
            self.timer_label.configure(text=f"Temps restant: {self.temps}s")
            self.after(1000, self.update_timer)  # Recursivite pour apres 1 sec update le temps
        else:
            self.end_game()

    def update_score(self, points):
        #Met à jour le score et update affichage
        if points == 0:
            self.score ==0
        else:
            self.score += points
            self.score_label.configure(text=f"Score: {self.score}")

    def end_game(self):
        self.timer_label.configure(text="Temps écoulé!")
        self.master.ajouter_log(f"Partie termine avec {self.score} points")
        #Ajouter une sauvgarde des log

    def plot_obstacles_and_goal(self):  # Méthode pour tracer les obstacles et la cible
        for obstacle in self.joueur.obstacles:  # Itération sur les obstacles
            x, y, r = obstacle  # Décomposition du tuple
            circle = Circle((x, y), r, color='red', alpha=0.5)  # Crée un cercle avec les coordonnées et le rayon
            self.ax.add_patch(circle)  # Ajout du cercle au tracé

        # Tracé du joueur
        self.ax.plot(self.joueur.joueur_position[0], self.joueur.joueur_position[1], 'v', markersize=15*self.res, label='Joueur') #FIX LE PROBLEME *******
        # Tracé de la cible
        self.ax.plot(self.joueur.cible_position[0], self.joueur.cible_position[1], 'o', markersize=15*self.res, label='Cible') # DE TOUCHER AVANT DE TOUCHER

        # Définition des limites des axes
        self.ax.set_xlim(0, 360)  
        self.ax.set_ylim(0, 200)  
        self.ax.set_aspect('equal', 'box')  # Assurer un aspect égal pour le tracé
        self.ax.legend(prop = { "size": 7*self.res}, markerscale=0.6*self.res,) # Affichage de la légende

    def update_score_ville(self): # QUAND EST CE QUE LA METHODE DE UPDATE LES POINTS DE LUIS EST OPTIMALE??? **************************************************
        self.viles_touche +=1

    def update_score_cible(self):
        self.cibles_touche +=1
