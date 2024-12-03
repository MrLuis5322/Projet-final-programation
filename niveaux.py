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
from matplotlib.lines import Line2D  # Import pour ajouter des objets de légende personnalisés



class Niveaux(tk.Frame):  # Définition de la classe Accueil comme un frame tkinter
    def get_obstacles(self):  # Fonction qui retourne les obstacles
        return self.obstacles
    
    def __init__(self, master, res):  # Appel du constructeur
        super().__init__(master)  # Super permet d'appeler plusieurs inheritance
        self.type = "fixe"
        self.res = res  # Facteur de résolution
        

        self.fig, self.ax = plt.subplots()  # Création de la figure et des axes pour le tracé
        self.fig.set_facecolor('gray')
        self.ax.set_facecolor('white')
        self.numero_Niveau = 1

        self.obstacles = self.generer_obstacles_fixes(self.numero_Niveau)  # Liste des obstacles


        #ajouter obstacles ici self.obstacles = {[5,5,5], [1,1,1]}


        self.joueur = Joueur(self, self.obstacles, self.type, self.numero_Niveau)  # Instance de Joueur
        self.tir = Tir(self)

        # Création de l'interface utilisateur
        self.setup_ui()
        
        # Ajout du graphique
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.graph_widget = self.canvas.get_tk_widget()
        self.graph_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        self.cibles_touche = 0
        self.villes_touche = 0


    def generer_obstacles_fixes(self, niveau):
        """
        Cette méthode génère des obstacles fixes avec les coordonnées et tailles spécifiées.
        """
        obstacles = []
        taille_min, taille_max = 5, 25  # Plage de tailles des obstacles
        x_range = (0, 340)  # Plage pour les coordonnées x
        y_range = (0, 180)  # Plage pour les coordonnées y

        # Définir des positions fixes pour les obstacles (exemple)
        if niveau == 1:
            fixed_positions = [
                (50, 50, 10),
                (100, 75, 15),
                (150, 100, 20),
                (200, 50, 5),
                (250, 120, 25),
                (300, 150, 10),
                (75, 150, 20),
                (50, 180, 10),
                (200, 180, 15),
                (150, 50, 25),
            ]
        elif niveau == 2:
            fixed_positions = [
                (60, 55, 12),   # Changement des coordonnées pour le niveau 2
                (110, 85, 17),
                (160, 120, 22),
                (210, 55, 7),
                (260, 130, 27),
                (310, 160, 12),
                (85, 160, 22),
                (60, 190, 12),
                (210, 190, 17),
                (160, 55, 27),
            ]
        elif niveau == 3:
            fixed_positions = [
                (70, 60, 14),   # Changement des coordonnées pour le niveau 3
                (120, 95, 18),
                (170, 130, 23),
                (220, 60, 9),
                (270, 140, 29),
                (320, 170, 14),
                (95, 170, 24),
                (70, 200, 14),
                (220, 200, 19),
                (170, 60, 29),
            ]


        # Vérification si les obstacles sont dans les bornes spécifiées
        for (x, y, taille) in fixed_positions:
            if 0 <= x <= 340 and 0 <= y <= 180 and taille_min <= taille <= taille_max:
                obstacles.append((x, y, taille))
        
        # Retourner la liste des obstacles fixes
        return obstacles


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

        self.nextlvl = ctk.CTkButton(
            master=widget_frame,
            width=100,
            height=50,
            corner_radius=20,
            text="Niveau suivant",
            command=self.tir.reset_plot,
            fg_color='blue2',
        )
        self.nextlvl.pack(side=tk.LEFT, padx=10, pady=10)

        

        

        self.plot_obstacles_and_goal()

    def update_timer(self):  # Minuterie
        if self.temps > 0:
            self.temps -= 1
            self.timer_label.configure(text=f"Temps restant: {self.temps}s")
            self.after(1000, self.update_timer)
        else:
            self.end_game()

    

    def end_game(self):  # Fin de la partie
        self.timer_label.configure(text="Temps écoulé!")
        self.master.ajouter_log(f"Partie terminée avec {self.score} points")

    def plot_obstacles_and_goal(self):  # Tracé des obstacles et de la cible
        # Charger l'image pour l'arrière-plan
        background_image = mpimg.imread('landscapefromabove.jpg')  # Remplacez par le chemin de votre image d'arrière-plan

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

        # Charger l'image de la cible (avec ou sans transparence)
        cible_image = mpimg.imread('EnemyPlane.png')  # Remplacez par le chemin de l'image de la cible

        # Tracer la position de la cible en utilisant l'image
        self.ax.imshow(cible_image, 
                        extent=[self.joueur.cible_position[0] - 10, self.joueur.cible_position[0] + 10, 
                                self.joueur.cible_position[1] - 10, self.joueur.cible_position[1] + 10], 
                        aspect='auto')

        # Définir un titre dynamique basé sur la variable x (niveau)
        # Exemple de niveau, vous pouvez ajuster en fonction du niveau actuel du jeu
        self.ax.set_title(f"Niveau {self.numero_Niveau}")  # Ajouter le titre avec la variable x

        # Configurer les limites et l'aspect des axes
        self.ax.set_xlim(0, 360)
        self.ax.set_ylim(0, 200)
        self.ax.set_aspect('equal', 'box')

        # Légende avec les images : Ajouter des objets de légende personnalisés avec Line2D
        # Créez des légendes pour les images en utilisant des objets Line2D
        joueur_couleur = '#808080'  # Gris
        # Couleur de l'ennemi en vert armée
        ennemi_couleur = '#6B8E23'  # Vert armée
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor=joueur_couleur, markersize=15, label='Joueur'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor=ennemi_couleur, markersize=15, label='Ennemi')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.1, 1), title='Légende')

        # Ajouter des graduations manuelles sur l'axe x et y
        self.ax.set_xticks(np.arange(0, 361, 50))  # Axes X de 0 à 360 avec des intervalles de 50
        self.ax.set_yticks(np.arange(0, 201, 20))  # Axes Y de 0 à 200 avec des intervalles de 20

        # Ajouter des étiquettes personnalisées (facultatif)
        self.ax.set_xticklabels([f'{x}°' for x in np.arange(0, 361, 50)])  # Exemple d'étiquettes pour l'axe x
        self.ax.set_yticklabels([f'{y}m' for y in np.arange(0, 201, 20)])  # Exemple d'étiquettes pour l'axe y



    


    def niveauSuivant(self):
        self.numero_Niveau =+1
        print("")
        if (self.cibles_touche == 0):
            print("")
        elif(self.cibles_touche == 1):
            print("")

        elif(self.cibles_touche == 2):
            print("")