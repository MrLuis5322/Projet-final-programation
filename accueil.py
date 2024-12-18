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

        # On passe en paramètre le facteur de résolution de l'utilisateur et on le stock dans une variable
        self.res = res

        self.score = 0 # On set le score à 0
        self.temps = 121 # On set le temps à 120 secondes

        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        
        self.obstacles_instance = Obstacles() # Créer une instance de la classe Obstacles
        self.obstacles = self.obstacles_instance.generer_obstacles()  # Génération de la liste des obstacles
        self.joueur = Joueur(self, self.obstacles)  # Création d'une instance de Joueur
        self.tir = Tir(self)

        self.setup_ui()  # Appel de la méthode pour configurer l'interface utilisateur
        self.ax.legend(loc="upper left", prop = { "size": 15*res }, 
                       markerscale=0.6*res, 
                       bbox_to_anchor=(1, 1)) # Place la légende et définit sa taille selon la resolution de l'utilisateur
        
        self.ax.set_facecolor('#363737')
        self.canvas = FigureCanvasTkAgg(self.fig, 
                                        master=self)  # Création d'un canvas pour afficher la figure
        self.canvas.get_tk_widget().place(x = 0, 
                                          y = 300, 
                                          relheight = 0.8, 
                                          relwidth = 1)  # Ajout du canvas à la fenêtre
        self.fig.set_facecolor('#363737')

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
            "Cosinus": "np.cos(x*0.1)*10",
        }

        # Création d'une combo box pour sélectionner le type de fonction
        self.func_selector = ctk.CTkComboBox(master = self, 
                                             width = 200,
                                             height = 50,
                                             corner_radius = 20,
                                             values=list(self.function_types.keys()), 
                                             command=self.tir.plot_selected_function)
        self.func_selector.place(x = 750, y = 20)  # Ajout de la combo box à la fenêtre

        # Création d'une entrée pour que l'utilisateur saisisse une fonction
        self.entry_func = ctk.CTkEntry(master = self, 
                                       width = 200,
                                       height = 50,
                                       corner_radius = 20,
                                       placeholder_text="Entrez une fonction")
        self.entry_func.place(x = 750, y = 110)  # Ajout de l'entrée à la fenêtre
        
        # Création d'un bouton pour tracer la fonction saisie
        self.plot_button = ctk.CTkButton(master = self, 
                                         width = 100, 
                                         height = 50, 
                                         border_width = 0, 
                                         corner_radius = 20, 
                                         text="Tirer", 
                                         command=self.tir.plot_function, 
                                         fg_color = 'blue')
        self.plot_button.place(x=500, y = 110)  # Ajout du bouton à la fenêtre

        # Création d'un bouton pour réinitialiser le tracé
        self.reset_button = ctk.CTkButton(master = self, 
                                          width = 100, 
                                          height = 50, 
                                          border_width = 0, 
                                          corner_radius = 20, 
                                          text="Réinitialiser", 
                                          command=self.tir.reset_plot, 
                                          fg_color = 'blue2')
        self.reset_button.place(x=500, y = 20)  # Ajout du bouton à la fenêtre

        #Affichage minuterie et score
        self.score_label = ctk.CTkLabel(master = self, 
                                        width = 100, 
                                        height = 50, 
                                        corner_radius = 20, 
                                        fg_color = '#363737',
                                        text_color = 'white',
                                        text=f"Score: {self.score}")
        self.score_label.place(x = 1000, y = 110)

        self.timer_label = ctk.CTkLabel( master = self, 
                                        width = 100, 
                                        height = 50, 
                                        corner_radius = 20, 
                                        text_color = 'white',
                                        fg_color = '#363737',

                                        text=f"Temps restant: {self.temps}s")
        self.timer_label.place(x = 1000, y = 20)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.plot_obstacles_and_goal() # Appel de la méthode pour tracer les obstacles et la cible

    def update_timer(self):
        # Diminue la minuterie et met à jour l'affichage
        if self.temps > 0:
            self.temps -= 1
            self.timer_label.configure(text=f"Temps restant: {self.temps}s")
            self.after(1000, self.update_timer)  # Récursivite pour après 1 sec update le temps
        else:
            self.end_game()

    def update_score(self, points):
        # Met à jour le score et update affichage
        if points == 0:
            self.score == 0
        elif points < 0:
            self.score = 0
        else:
            self.score += points
            self.score_label.configure(text=f"Score: {self.score}")

    def end_game(self):
        self.timer_label.configure(text="Temps écoulé!")
        self.master.ajouter_log(f"Partie termine avec {self.score} points")
        # Ajouter une sauvgarde des log

    def plot_obstacles_and_goal(self):  # Méthode pour tracer les obstacles et la cible
        for obstacle in self.joueur.obstacles:  # Itération sur les obstacles
            x, y, r = obstacle  # Décomposition du tuple
            circle = Circle((x, y), r, color='red', alpha=0.5)  # Crée un cercle avec les coordonnées et le rayon
            self.ax.add_patch(circle)  # Ajout du cercle au tracé

        # Tracé du joueur
        self.ax.plot(self.joueur.joueur_position[0], self.joueur.joueur_position[1], 'v', markersize=15*self.res, label='Joueur')
        # Tracé de la cible
        self.ax.plot(self.joueur.cible_position[0], self.joueur.cible_position[1], 'o', markersize=15*self.res, label='Cible')

        # Définition des limites des axes
        self.ax.set_xlim(0, 360)  
        self.ax.set_ylim(0, 200)  
        self.ax.set_aspect('equal', 'box')  # Assurer un aspect égal pour le tracé
        self.ax.legend(prop = { "size": 15*self.res}, markerscale=0.6*self.res,) # Affichage de la légende

    def update_score_ville(self):
        self.viles_touche +=1

    def update_score_cible(self):
        self.cibles_touche +=1
