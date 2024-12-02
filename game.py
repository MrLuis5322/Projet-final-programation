import tkinter as tk  
import customtkinter as ctk  
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importation pour intégrer Matplotlib avec tkinter
from joueur import Joueur  
from tir import Tir  
from traitementCSV import Obstacles
from matplotlib.patches import Circle

class Game(tk.Frame):  # Définition de la classe Accueil comme un frame tkinter
    
    def __init__(self, parent): # Appel du constructeur
        super().__init__(parent) # Super permet d'appeler plusieurs inheritance
        self.parent = parent

        # Création des classes utiles pour la partie
        self.obstacles_instance = Obstacles()
        self.obstacles = self.obstacles_instance.generer_obstacles()
        self.joueur = Joueur(self, self.obstacles)
        self.tir = Tir(self)

        self.index = 0.0
        self.score = 0 # Score du joueur
        self.temps = 121 # Temps pour que le joueur tire le plus de cibles possible

        self.config(bg = 'gray14')

        self.rowconfigure((0, 1), weight = 1, uniform = 'a') # Vertical 
        self.rowconfigure(2, weight = 8, uniform = 'a')
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = 'a') # Horizontal
        self.columnconfigure(4, weight = 2, uniform = 'a')

        self.create_widgets()
        self.update_timer()

    def create_figure(self):
        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        self.ax.legend(loc="upper left", prop = { "size": 15}, 
                       markerscale=0.6, 
                       bbox_to_anchor=(1, 1)) # Place la légende et définit sa taille selon la resolution de l'utilisateur
        self.canvas = FigureCanvasTkAgg(self.fig, 
                                        master=self)  # Création d'un canvas pour afficher la figure
        self.canvas.get_tk_widget().grid(row = 2, column = 0, sticky = 'nswe', columnspan = 10, rowspan = 8)  # Ajout du canvas à la fenêtre
        self.ax.set_facecolor('#242424')
        self.fig.set_facecolor('#242424')

    def create_widgets(self): # Méthode pour configurer l'interface utilisateur
        self.create_figure()
        self.function_types = {
            "Linéaire": "x",
            "Quadratique": "0.01*x**2",
            "Exponentielle": "np.exp(x)",
            "Sinus": "np.sin(x*0.1)*10",
            "Cosinus": "np.cos(x*0.1)*10",
        }
        self.func_selector = ctk.CTkComboBox(master = self, 
                                             width = 200,
                                             height = 50,
                                             corner_radius = 75,
                                             font = ('Helvetica', 20),
                                             values=list(self.function_types.keys()), 
                                             justify = 'left',
                                             state = 'readonly',
                                             command=self.tir.plot_selected_function)
        self.entry_func = ctk.CTkEntry(master = self, 
                                       width = 200,
                                       height = 50,
                                       corner_radius = 75,
                                       font = ('Helvetica', 20),
                                       placeholder_text="Entrez une fonction")
        self.plot_button = ctk.CTkButton(master = self, 
                                         width = 200, 
                                         height = 50, 
                                         border_width = 0, 
                                         corner_radius = 75, 
                                         text="Tirer", 
                                         font = ('Helvetica', 20),
                                         command=self.tir.plot_function, 
                                         text_color='gray14',
                                         hover_color = 'red4',
                                         fg_color = 'red3')
        self.reset_button = ctk.CTkButton(master = self, 
                                          width = 200, 
                                          height = 50, 
                                          border_width = 0, 
                                          corner_radius = 75, 
                                          text="Réinitialiser", 
                                          font = ('Helvetica', 20),
                                          command=self.tir.reset_plot, 
                                          text_color='gray14',
                                          hover_color = 'red4',
                                          fg_color = 'red3')
        self.main_menu = ctk.CTkButton(master = self, 
                                          width = 200, 
                                          height = 50, 
                                          border_width = 0, 
                                          corner_radius = 75, 
                                          text="Retour au menu", 
                                          font = ('Helvetica', 20),
                                          command=lambda:self.parent.changeWindow(0, 3), 
                                          text_color='gray14',
                                          hover_color = 'red4',
                                          fg_color = 'red3')
        self.score_label = ctk.CTkLabel(master = self, 
                                        width = 200, 
                                        height = 50, 
                                        corner_radius = 75, 
                                        fg_color = '#363737',
                                        text_color = 'white',
                                        font = ('Helvetica', 20),
                                        text=f"Score: {self.score}")
        self.user_label = ctk.CTkLabel(master = self, 
                                        width = 200, 
                                        height = 50, 
                                        corner_radius = 75, 
                                        fg_color = '#363737',
                                        text_color = 'white',
                                        font = ('Helvetica', 20),
                                        text=f"Joueur: {self.score}")
        self.timer_label = ctk.CTkLabel( master = self, 
                                        width = 200, 
                                        height = 50, 
                                        corner_radius = 75, 
                                        text_color = 'white',
                                        fg_color = '#363737',
                                        font = ('Helvetica', 20),
                                        text=f"Décompte: {self.temps}s")
        self.logs = ctk.CTkTextbox(master = self,
                                   fg_color = 'gray14',
                                   text_color = 'white',
                                   font = ('Helvetica', 15),
                                   state = 'disable')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.plot_obstacles_and_goal() # Appel de la méthode pour tracer les obstacles et la cible

    def layout_widgets(self):
        self.func_selector.grid(row = 0, column = 2)
        self.entry_func.grid(row = 0, column = 1)
        self.plot_button.grid(row = 1, column = 1)
        self.reset_button.grid(row = 1, column = 0)
        self.score_label.grid(row = 1, column = 2)
        self.timer_label.grid(row = 1, column = 3)
        self.user_label.grid(row = 0, column = 3)
        self.main_menu.grid(row = 0, column = 0)
        self.logs.grid(row = 0, column = 4, rowspan = 2, sticky = 'nswe')
        if self.parent.windowList[1].nom == "":
            self.user_label.configure(text=f"Joueur: guest")
        else:
            self.user_label.configure(text=f"Joueur: {self.parent.windowList[1].nom}")

    def update_timer(self):
        if self.temps > 0:
            self.temps -= 1
            self.timer_label.configure(text=f"Temps restant: {self.temps}s")
            self.after(1000, self.update_timer)  # Récursivite pour après 1 sec update le temps
        else:
            self.end_game()

    def update_score(self, points):
        if points == 0 or points < 0:
            self.score == 0
        else:
            self.score += points
            self.score_label.configure(text=f"Score: {self.score}")

    def end_game(self):
        self.timer_label.configure(text="Temps écoulé!")
        self.plot_button.configure(state = 'disable')
        self.logs.insert(f"Partie termine avec {self.score} points")

    def plot_obstacles_and_goal(self):  # Méthode pour tracer les obstacles et la cible
        for obstacle in self.joueur.obstacles:  # Itération sur les obstacles
            x, y, r = obstacle  # Décomposition du tuple
            circle = Circle((x, y), r, color='red', alpha=0.5)  # Crée un cercle avec les coordonnées et le rayon
            self.ax.add_patch(circle)  # Ajout du cercle au tracé

        # Tracé du joueur
        self.ax.plot(self.joueur.joueur_position[0], self.joueur.joueur_position[1], 'v', markersize=15*self.parent.windowList[2].pres, label='Joueur')
        # Tracé de la cible
        self.ax.plot(self.joueur.cible_position[0], self.joueur.cible_position[1], 'o', markersize=15*self.parent.windowList[2].cres, label='Cible')

        # Définition des limites des axes
        self.ax.set_xlim(0, 360)  
        self.ax.set_ylim(0, 200)  
        self.ax.set_aspect('equal', 'box')  # Assurer un aspect égal pour le tracé
        self.ax.legend(prop = { "size": 15*self.parent.windowList[2].lres}, markerscale=0.6*self.parent.windowList[2].lres) # Affichage de la légende

    def write_log(self, string):
        self.logs.configure(state = 'normal') 
        self.logs.insert(index = f'{self.index} linestart', text = f'{string}\n')
        self.index += 1.0
        self.logs.configure(state = 'disable')
