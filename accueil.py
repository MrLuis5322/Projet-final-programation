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
    #master c'est la convention pour désigner la fenêtre principale
    def get_obstacles(self):
        return self.obstacles
    
    def __init__(self, master):# Appel du constructeur de la classe parente
        super().__init__(master)
        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        
        self.obstacles_instance = Obstacles() # Créer une instance de la classe Obstacles
        self.obstacles = self.obstacles_instance.generer_obstacles()  # Génération des obstacles
        self.joueur = Joueur(self, self.obstacles)  # Création d'une instance de Joueur
        self.tir = Tir(self)

        self.setup_ui()  # Appel de la méthode pour configurer l'interface utilisateur
        self.ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # Création d'un canvas pour afficher la figure
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Ajout du canvas à la fenêtre. Ce code je l'ai crecherche je le comprend pas trop mais ca marche

    def setup_ui(self):  # Méthode pour configurer l'interface utilisateur

        # Définition des types de fonctions disponibles dans le menu déroulant(a ajouter)
        self.function_types = {
            "Linéaire (x)": "x",
            "Quadratique (x^2)": "x**2",
            "Exponentielle (e^x)": "np.exp(x)",
            "Sinus (sin(x))": "np.sin(x)",
            "Cercle touchant l'origine": "circle" #???? on le garde tu?
        }

        # Création d'une combo box pour sélectionner le type de fonction
        self.func_selector = ctk.CTkComboBox(self, values=list(self.function_types.keys()), command=self.tir.plot_selected_function)
        self.func_selector.pack(pady=10)  # Ajout de la combo box à la fenêtre

        # Création d'une entrée pour que l'utilisateur saisisse une fonction
        self.entry_func = ctk.CTkEntry(self, placeholder_text="Entrez une fonction en x (ex: np.sin(x))")
        self.entry_func.pack(pady=10)  # Ajout de l'entrée à la fenêtre
        
        # Création d'un bouton pour tracer la fonction saisie
        self.plot_button = ctk.CTkButton(self, text="Tracer la fonction", command=self.tir.plot_function)
        self.plot_button.pack(pady=10)  # Ajout du bouton à la fenêtre

        # Création d'un bouton pour réinitialiser le tracé
        self.reset_button = ctk.CTkButton(self, text="Réinitialiser", command=self.tir.reset_plot)
        self.reset_button.pack(pady=10)  # Ajout du bouton à la fenêtre

        # Supprimer les graduations
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

        self.plot_obstacles_and_goal() # Appel de la méthode pour tracer les obstacles et la cible

    def plot_obstacles_and_goal(self):  # Méthode pour tracer les obstacles et la cible
        for obstacle in self.joueur.obstacles:  # Itération sur les obstacles
            x, y, r = obstacle  # Décomposition du tuple
            circle = Circle((x, y), r, color='red', alpha=0.5)  # Crée un cercle avec les coordonnées et le rayon
            self.ax.add_patch(circle)  # Ajout du cercle au tracé

    # Tracé du joueur
        self.ax.plot(self.joueur.joueur_position[0], self.joueur.joueur_position[1], 'bo', markersize=10, label='Joueur')
    # Tracé de la cible
        self.ax.plot(self.joueur.cible_position[0], self.joueur.cible_position[1], 'go', markersize=10, label='Cible')

    # Définition des limites des axes
        self.ax.set_xlim(-100, 100)  
        self.ax.set_ylim(-100, 100)  
        self.ax.set_aspect('equal', 'box')  # Assurer un aspect égal pour le tracé
        self.ax.legend()  # Affichage de la légende
