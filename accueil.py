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
from matplotlib.lines import Line2D
from matplotlib.transforms import Affine2D #transformer image joueur



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

    from matplotlib.transforms import Affine2D

    def plot_obstacles_and_goal(self):  
        # Charger l'image pour l'arrière-plan
        background_image = mpimg.imread('landscapefromabove.jpg')  # Arrière-plan
        self.ax.imshow(background_image, extent=[0, 360, 0, 200], aspect='auto')

        # Tracer les obstacles
        for obstacle in self.joueur.obstacles:
            x, y, r = obstacle
            circle = Circle((x, y), r, color='red', alpha=0.5)
            self.ax.add_patch(circle)

        # Charger l'image de l'avion pour le joueur
        joueur_image = mpimg.imread('PlayerPlane.png')

        # Vérifier la position du joueur par rapport à la cible
        joueur_x, joueur_y = self.joueur.joueur_position
        cible_x, cible_y = self.joueur.cible_position

        # Appliquer une rotation si nécessaire
        if joueur_x < cible_x:  # Si le joueur est à gauche de la cible
            rotation_transform = Affine2D().rotate_deg_around(joueur_x, joueur_y, 180) + self.ax.transData
        else:  # Si le joueur est à droite de la cible, pas de rotation
            rotation_transform = self.ax.transData

        # Tracer l'image de l'avion avec la rotation appliquée
        self.ax.imshow(
            joueur_image,
            extent=[joueur_x - 10, joueur_x + 10, joueur_y - 10, joueur_y + 10],
            aspect='auto',
            transform=rotation_transform,
            alpha=1.0,
        )

        # Charger et tracer l'image de la cible
        cible_image = mpimg.imread('EnemyPlane.png')
        self.ax.imshow(
            cible_image,
            extent=[cible_x - 10, cible_x + 10, cible_y - 10, cible_y + 10],
            aspect='auto',
        )

        # Configurer les limites et l'aspect des axes
        self.ax.set_xlim(0, 360)
        self.ax.set_ylim(0, 200)
        self.ax.set_aspect('equal', 'box')

        # Ajouter une légende
        joueur_couleur = '#808080'
        ennemi_couleur = '#6B8E23'
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor=joueur_couleur, markersize=15, label='Joueur'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor=ennemi_couleur, markersize=15, label='Ennemi')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.1, 1), title='Légende')

        # Ajouter des graduations manuelles
        self.ax.set_xticks(np.arange(0, 361, 50))
        self.ax.set_yticks(np.arange(0, 201, 20))
        self.ax.set_xticklabels([f'{x}°' for x in np.arange(0, 361, 50)])
        self.ax.set_yticklabels([f'{y}m' for y in np.arange(0, 201, 20)])






    def update_score_ville(self):
        self.villes_touche +=1

    def update_score_cible(self):
        self.cibles_touche +=1