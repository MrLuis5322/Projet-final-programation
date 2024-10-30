import tkinter as tk
from customtkinter import CTk, CTkButton, CTkEntry, CTkComboBox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#test
# Configuration de l'interface graphique
class GraphWarGame(CTk):
    def __init__(self):
        super().__init__()

        self.title("Graph War")
        self.geometry("800x600")
        #ajout  comme
        # Configuration de la figure Matplotlib
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Définir les obstacles
        self.obstacles = [(np.random.uniform(-100, 100), np.random.uniform(-100, 100), np.random.uniform(5, 15)) for _ in range(3)]
        self.player = self.generate_valid_player_position()  # Générer une position valide pour le joueur
        self.goal = self.generate_valid_goal()  # Générer une position valide pour la cible

        # Ajouter une boîte de sélection pour choisir le type de fonction
        self.function_types = {
            "Linéaire (x)": "x",
            "Quadratique (x^2)": "x**2",
            "Exponentielle (e^x)": "np.exp(x)",
            "Sinus (sin(x))": "np.sin(x)",
            "Cercle touchant l'origine": "circle"
        }



        self.func_selector = CTkComboBox(self, values=list(self.function_types.keys()), command=self.plot_selected_function)
        self.func_selector.pack(pady=10)

        # Ajouter des boutons pour les actions
        self.entry_func = CTkEntry(self, placeholder_text="Entrez une fonction en x (ex: np.sin(x))")
        self.entry_func.pack(pady=10)
        self.plot_button = CTkButton(self, text="Tracer la fonction", command=self.plot_function)
        self.plot_button.pack(pady=10)

        self.reset_button = CTkButton(self, text="Réinitialiser", command=self.reset_plot)
        self.reset_button.pack(pady=10)

        self.plot_obstacles_and_goal()

    def generate_valid_player_position(self):
        """ Génère une position valide pour le joueur (dans le domaine négatif, sans collision avec un obstacle). """
        while True:
            player = self.generate_random_point(negative=True)
            if not self.is_point_on_obstacle(player):
                return player

    def generate_valid_goal(self):
        """ Génère une position valide pour la cible (dans le domaine positif, sans collision avec un obstacle). """
        while True:
            goal = self.generate_random_point(negative=False)
            if not self.is_point_on_obstacle(goal):
                return goal

    def generate_random_point(self, negative=True):
        """ Génère un point aléatoire avec des coordonnées négatives (pour le joueur) ou positives (pour la cible). """
        if negative:
            return (np.random.uniform(-100, 0), np.random.uniform(-100, 0))
        else:
            return (np.random.uniform(0, 100), np.random.uniform(0, 100))

    def is_point_on_obstacle(self, point):
        """ Vérifie si un point est à l'intérieur d'un obstacle. """
        px, py = point
        for (ox, oy, r) in self.obstacles:
            distance = np.sqrt((px - ox)**2 + (py - oy)**2)
            if distance < r:
                return True
        return False

    def plot_obstacles_and_goal(self):
        # Tracer les obstacles
        for (ox, oy, r) in self.obstacles:
            circle = plt.Circle((ox, oy), r, color='red', fill=True)
            self.ax.add_patch(circle)

        # Tracer le point joueur
        self.ax.plot(self.player[0], self.player[1], 'bo', markersize=10, label='Joueur')
     
        # Tracer la cible
        self.ax.plot(self.goal[0], self.goal[1], 'go', markersize=10, label='Cible')

        # Configuration du graphe
        self.ax.set_xlim(-100, 100)  # Domaine de -100 à 100
        self.ax.set_ylim(-100, 100)  # Image de -100 à 100
        self.ax.set_aspect('equal', 'box')
        self.ax.legend()

    def plot_function(self):
    # Récupérer la fonction entrée par l'utilisateur
        func_text = self.entry_func.get()

        if not func_text:
            print("Veuillez entrer une fonction valide.")
            return

        try:
            # Générer les points x, en les décalant selon la position du joueur
            x_shift = self.player[0]  # Récupérer la position en x du joueur
            x = np.linspace(-100, 100, 1000)  # Valeurs x d'origine
            x_shifted = x + x_shift  # Décalage de x pour passer par le joueur

        # Vérifier si la fonction est une constante (pas de 'x' dans l'expression)
            if 'x' not in func_text:
            # Si c'est une constante, créer un tableau y constant
                y = np.full_like(x_shifted, eval(func_text))  # Evaluer la constante
            else:
            # Calculer les y en fonction de la fonction entrée
                y = eval(func_text, {"np": np, "x": x_shifted})

        # Tracer la fonction
            self.ax.plot(x_shifted, y, label=f'f(x)={func_text} (décalée par {x_shift})')

        # Vérifier et marquer les collisions avec les obstacles
            collision_points = self.check_collision(x_shifted, y)
            if collision_points:
                # Ajouter des points rouges là où il y a des collisions
                cx, cy = zip(*collision_points)
                self.ax.plot(cx, cy, 'ro', markersize=5, label='Collision')

            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            print(f"Erreur lors du traçage de la fonction : {e}")


        if not func_text:
            print("Veuillez entrer une fonction valide.")
            return

        try:
            # Générer les points x, en les décalant selon la position du joueur
            x_shift = self.player[0]  # Récupérer la position en x du joueur
            x = np.linspace(-100, 100, 1000)  # Valeurs x d'origine
            x_shifted = x + x_shift  # Décalage de x pour passer par le joueur

            # Calculer les y en fonction de la fonction entrée
            y = eval(func_text, {"np": np, "x": x_shifted})

            # Tracer la fonction
            self.ax.plot(x_shifted, y, label=f'f(x)={func_text} (décalée par {x_shift})')

            # Vérifier et marquer les collisions avec les obstacles
            collision_points = self.check_collision(x_shifted, y)
            if collision_points:
                # Ajouter des points rouges là où il y a des collisions
                cx, cy = zip(*collision_points)
                self.ax.plot(cx, cy, 'ro', markersize=5, label='Collision')

            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            print(f"Erreur lors du traçage de la fonction : {e}")

    def plot_selected_function(self, choice):
        # Récupérer la fonction associée au choix du menu
        func_text = self.function_types.get(choice)

        # Si le choix est un cercle, il faut tracer différemment
        if func_text == "circle":
            self.plot_circle()
        else:
            self.entry_func.delete(0, tk.END)  # Supprime l'ancien texte dans l'entrée
            self.entry_func.insert(0, func_text)  # Insère la nouvelle fonction dans l'entrée
            self.plot_function()  # Trace la fonction

    def plot_circle(self):
        # Effacer le graphe précédent
        self.reset_plot()

        # Tracer un cercle qui touche l'origine (0, 0)
        theta = np.linspace(0, 2 * np.pi, 100)
        r = 30  # Rayon du cercle
        # Placer le centre du cercle de manière à ce qu'il touche (0, 0)
        x = r * np.cos(theta) + r  # Décalage du centre de r pour toucher l'origine
        y = r * np.sin(theta)

        self.ax.plot(x, y, label="Cercle touchant l'origine")
        self.ax.legend()
        self.canvas.draw()

    def check_collision(self, x, y):
        # Vérifier si les points de la fonction passent à travers un obstacle
        collision_points = []
        for (ox, oy, r) in self.obstacles:
            distance = np.sqrt((x - ox)**2 + (y - oy)**2)
            # Ajouter les points qui se trouvent à l'intérieur d'un obstacle
            indices = np.where(distance < r)[0]
            for i in indices:
                collision_points.append((x[i], y[i]))
        return collision_points

    def reset_plot(self):
        # Réinitialiser le graphe
        self.ax.clear()
        self.plot_obstacles_and_goal()
        self.canvas.draw()

# Lancer le jeu
if __name__ == "__main__":
    app = GraphWarGame()
    app.mainloop()
