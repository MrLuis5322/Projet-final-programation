import numpy as np  
from joueur import Joueur
import tkinter as tk
import time

# Fonction pour vérifier si un point est dans un cercle
def touche_au_cercle(x, y, cercle_x, cercle_y, rayon):
    return (x - cercle_x)**2 + (y - cercle_y)**2 <= rayon**2

class Tir: 
    def __init__(self, accueil):  # Constructeur qui prend en paramètre notre interface graphique
        self.accueil = accueil 
        self.obstacles = accueil.obstacles  # Initialiser les obstacles

    # Méthode pour tracer une fonction
    def plot_function(self):  
        equation = self.accueil.entry_func.get()  # Récupère la fonction entrée par l'utilisateur
        if not equation:  # Vérifie si la fonction est vide
            print("Veuillez entrer une fonction valide.")  # Affiche un message d'erreur
            return
        
        # Position du joueur et de la cible
        joueur_pos = self.accueil.joueur.joueur_position 
        cible_pos = self.accueil.joueur.cible_position  
        # Convertir en coordonnées
        x_joueur, y_joueur = joueur_pos 
        x_cible, y_cible = cible_pos

        # Génère un tableau de valeurs x allant de x_joueur à 200 (-100 à 100)
        x_fct = np.linspace(x_joueur, 400, 2000)
        
        # Évaluer l'équation pour obtenir y
        try:
            y_fct = eval(equation, {"x": x_fct, "np": np})
        except Exception as e:
            print(f"Erreur dans l'équation : {e}")
            return
        
        # Appliquer la translation pour que le (0,0) de la fonction soit le joueur
        x_translated = x_fct + x_joueur
        y_translated = y_fct + y_joueur

        # Initialiser les listes pour le tracé limité
        trajectoire_x = []
        trajectoire_y = []
        # Stocker les coordonnées des collisons
        collision_x = None 
        collision_y = None
        cible_touchee = False

        # Vérification des collisions
        for i in range(len(x_translated)):
            # Ajouter les points à la trajectoire si on n'est pas encore à la position du joueur ou atteint un obsatcle
            if x_translated[i] >= x_joueur: # x_joueur + ... afin de commencer a l'extrémité du cercle

                # Vérifier la collision avec les obsatcles 
                collision = False
                for obstacle in self.obstacles:  # Itération sur les obstacles
                    x, y, r = obstacle  # Décomposition de l'obsatcles
                    if touche_au_cercle(x_translated[i], y_translated[i], x, y, r):
                        print(f"Obstacle touché en : ({x_translated[i]:.2f}, {y_translated[i]:.2f})")
                        collision_x = x_translated[i]
                        collision_y = y_translated[i]
                        collision = True
                        break 

                # Vérifier la collision avec la cible
                if touche_au_cercle(x_translated[i], y_translated[i], x_cible, y_cible, 5):
                    print(f"Cible touchée en : ({x_translated[i]:.2f}, {y_translated[i]:.2f})")
                    cible_touchee = True
                    collision = True
                    break 

                if collision:
                    break  # Quitte la boucle

                # Ajouter les points à la trajectoire
                trajectoire_x.append(x_translated[i])
                trajectoire_y.append(y_translated[i])

        # Trajectoire
        self.accueil.ax.plot(trajectoire_x, trajectoire_y, label=f'f(x)={equation}') 
        # Effe de collision
        if collision_x is not None and collision_y is not None:
            self.accueil.ax.plot(collision_x, collision_y, 'ro', markersize=2)  # 'ro' pour 'red dot'
    
        # Supprimer les graduations
        self.accueil.ax.set_xticks([])
        self.accueil.ax.set_yticks([])
        # Placer la légende en dehors de la zone de tracé
        self.accueil.ax.legend(loc="upper left", prop = { "size": 7 }, markerscale=0.6, bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()  

        # Si la cible est touchée, ajoutez un délai, puis réinitialisez la scène
        if cible_touchee:
            self.cible_atteinte()  # Appelle la méthode pour gérer la réinitialisation après la cible atteinte
            
    def cible_atteinte(self):
        self.accueil.after(800, self.reset_plot)  # Attente de 1 secondes avant réinitialisation

    def reset_plot(self):
        self.accueil.ax.clear()
        
        # Générer de nouveaux obstacles et mettre à jour les obstacles dans l'instance Tir
        self.accueil.obstacles = self.accueil.obstacles_instance.generer_obstacles()
        self.obstacles = self.accueil.obstacles  # Mettre à jour les obstacles dans Tir
        
        # Générer un nouveau joueur avec les nouveaux obstacles
        self.accueil.joueur = Joueur(self.accueil, self.accueil.obstacles)
        
        # Tracer les obstacles et la cible
        self.accueil.plot_obstacles_and_goal()
        self.accueil.ax.set_xticks([])
        self.accueil.ax.set_yticks([])
        self.accueil.ax.legend(loc="upper left", prop={"size": 7}, markerscale=0.6, bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()

    def plot_selected_function(self, choice):  # Méthode pour tracer une fonction sélectionnée
        func_text = self.accueil.function_types.get(choice)  # Récupère la fonction associée au choix
        self.accueil.entry_func.delete(0, tk.END)  # Efface le champ de saisie
        self.accueil.entry_func.insert(0, func_text)  # Insère la fonction sélectionnée dans le champ
        self.plot_function()  # Appelle la méthode pour tracer la fonction