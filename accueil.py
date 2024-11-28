import tkinter as tk  
import customtkinter as ctk  
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importation pour intégrer Matplotlib avec tkinter
from joueur import Joueur  
from tir import Tir  
from traitementCSV import Obstacles
from matplotlib.patches import Circle
import matplotlib.image as mpimg


class Accueil(tk.Frame):  # Définition de la classe Accueil comme un frame tkinter
    def get_obstacles(self):  # Fonction qui retourne les obstacles
        return self.obstacles
    
    def __init__(self, master, res):  # Appel du constructeur
        super().__init__(master)  # Super permet d'appeler plusieurs inheritance
        self.type = "random"
        self.numero_Niveau = None
        self.res = res  # Facteur de résolution
        self.score = 0  # Score initial
        self.temps = 121  # Temps initial

        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        self.fig.set_facecolor('gray')
        self.ax.set_facecolor('white')

        self.obstacles_instance = Obstacles()  # Instance de la classe Obstacles
        self.obstacles = self.obstacles_instance.generer_obstacles()  # Liste des obstacles
        #ajouter obstacles ici self.obstacles = {[5,5,5], [1,1,1]}
        self.joueur = Joueur(self, self.obstacles, "random", None)  # Instance de Joueur
        self.tir = Tir(self)

        # Création de l'interface utilisateur
        self.setup_ui()
        
        # Ajout du graphique
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.graph_widget = self.canvas.get_tk_widget()
        self.graph_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.update_timer()

        self.cibles_touche = 0
        self.villes_touche = 0

    def setup_ui(self):  # Interface utilisateur
        # Conteneur pour les widgets
        widget_frame = ctk.CTkFrame(self, corner_radius=10)
        widget_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Menu déroulant
        self.function_types = {
            "Linéaire": "x",
            "Quadratique": "0.01*x**2",
            "Exponentielle": "np.exp(x)",
            "Sinus": "np.sin(x*0.1)*10",
            "Cosinus": "np.cos(x*0.1)*10",
        }
        self.func_selector = ctk.CTkComboBox(
            master=widget_frame,
            width=200,
            height=50,
            corner_radius=20,
            values=list(self.function_types.keys()),
            command=self.tir.plot_selected_function,
        )
        self.func_selector.pack(side=tk.LEFT, padx=10, pady=10)

        # Entrée utilisateur
        self.entry_func = ctk.CTkEntry(
            master=widget_frame,
            width=200,
            height=50,
            corner_radius=20,
            placeholder_text="Entrez une fonction",
        )
        self.entry_func.pack(side=tk.LEFT, padx=10, pady=10)

        # Boutons
        self.plot_button = ctk.CTkButton(
            master=widget_frame,
            width=100,
            height=50,
            corner_radius=20,
            text="Tirer",
            command=self.tir.plot_function,
            fg_color='blue',
        )
        self.plot_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_button = ctk.CTkButton(
            master=widget_frame,
            width=100,
            height=50,
            corner_radius=20,
            text="Réinitialiser",
            command=self.tir.reset_plot,
            fg_color='blue2',
        )
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Labels
        self.score_label = ctk.CTkLabel(
            master=widget_frame,
            width=150,
            height=50,
            corner_radius=20,
            fg_color='#363737',
            text_color='white',
            text=f"Score: {self.score}",
        )
        self.score_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.timer_label = ctk.CTkLabel(
            master=widget_frame,
            width=200,
            height=50,
            corner_radius=20,
            fg_color='#363737',
            text_color='white',
            text=f"Temps restant: {self.temps}s",
        )
        self.timer_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.plot_obstacles_and_goal()

    def update_timer(self):  # Minuterie
        if self.temps > 0:
            self.temps -= 1
            self.timer_label.configure(text=f"Temps restant: {self.temps}s")
            self.after(1000, self.update_timer)
        else:
            self.end_game()

    def update_score(self, points):  # Mise à jour du score
        self.score = max(0, self.score + points)
        self.score_label.configure(text=f"Score: {self.score}")

    def end_game(self):  # Fin de la partie
        self.timer_label.configure(text="Temps écoulé!")
        self.master.ajouter_log(f"Partie terminée avec {self.score} points")

    def plot_obstacles_and_goal(self):  # Tracé des obstacles et de la cible
        # Charger l'image pour l'arrière-plan
        background_image = mpimg.imread('landscapefromabove.jpg')  # Ariere plan

        # Afficher l'image en arrière-plan
        self.ax.imshow(background_image, extent=[0, 360, 0, 200], aspect='auto')

        # Tracer les obstacles
        for obstacle in self.joueur.obstacles:
            x, y, r = obstacle
            circle = Circle((x, y), r, color='red', alpha=0.5)
            self.ax.add_patch(circle)

        # Charger l'image de l'avion pour le joueur (avec fond transparent)
        joueur_image = mpimg.imread('PlayerPlane.png')  # Remplacez par le chemin de l'image de l'avion

        # Tracer la position du joueur en utilisant l'image de l'avion
        self.ax.imshow(joueur_image, 
                    extent=[self.joueur.joueur_position[0] - 10, self.joueur.joueur_position[0] + 10, 
                            self.joueur.joueur_position[1] - 10, self.joueur.joueur_position[1] + 10], 
                    aspect='auto', alpha=1.0)  # Garder la transparence du fond

        # Charger l'image de la cible
        cible_image = mpimg.imread('EnemyPlane.png')  # Remplacez par le chemin de l'image de la cible

        # Tracer la position de la cible en utilisant l'image
        self.ax.imshow(cible_image, 
                    extent=[self.joueur.cible_position[0] - 10, self.joueur.cible_position[0] + 10, 
                            self.joueur.cible_position[1] - 10, self.joueur.cible_position[1] + 10], 
                    aspect='auto')

        # Configurer les limites et l'aspect des axes
        self.ax.set_xlim(0, 360)
        self.ax.set_ylim(0, 200)
        self.ax.set_aspect('equal', 'box')

        # Ajouter une légende si nécessaire
        self.ax.legend(prop={"size": 15 * self.res}, markerscale=0.6 * self.res)





    def update_score_ville(self):
        self.villes_touche +=1

    def update_score_cible(self):
        self.cibles_touche +=1