import numpy as np  
import tkinter as tk  

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
        x_fct = np.linspace(x_joueur, 200, 1000)
        
        # Évaluer l'équation pour obtenir y
        try:
            # Passer x_local comme "x" dans le contexte d'évaluation
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

        # Vérification des collisions
        collision_detected = False
        for i in range(len(x_translated)):
            # Ajouter les points à la trajectoire si on n'est pas encore à la position du joueur
            if x_translated[i] >= x_joueur: # x_joueur + ... afin de commencer a l'extrémité du cercle
                # Vérifier la collision avec la cible
                if touche_au_cercle(x_translated[i], y_translated[i], x_cible, y_cible, 5):
                    collision_detected = True
                    print(f"Cible touchée en : ({x_translated[i]:.2f}, {y_translated[i]:.2f})")
                    break

                 # Ajouter les points à la trajectoire
                trajectoire_x.append(x_translated[i])
                trajectoire_y.append(y_translated[i])

        # Trajectoire
        self.accueil.ax.plot(trajectoire_x, trajectoire_y, label=f'f(x)={equation}') 
        # Supprimer les graduations
        self.accueil.ax.set_xticks([])
        self.accueil.ax.set_yticks([])
        # Placer la légende en dehors de la zone de tracé
        self.accueil.ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()  

    def reset_plot(self):  # Méthode pour réinitialiser le graphique
        self.accueil.ax.clear()  # Efface l'axe du graphique
        self.accueil.plot_obstacles_and_goal()  # Rétrace les obstacles et la cible
        # Supprimer les graduations
        self.accueil.ax.set_xticks([])
        self.accueil.ax.set_yticks([])
        self.accueil.ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()  # Met à jour le graphique(cnvas)

    def plot_selected_function(self, choice):  # Méthode pour tracer une fonction sélectionnée
        func_text = self.accueil.function_types.get(choice)  # Récupère la fonction associée au choix
        if func_text == "circle":  # Vérifie si la fonction sélectionnée est un cercle
            self.plot_circle()  # Appelle une méthode pour tracer un cercle
        else:
            self.accueil.entry_func.delete(0, tk.END)  # Efface le champ de saisie
            self.accueil.entry_func.insert(0, func_text)  # Insère la fonction sélectionnée dans le champ
            self.plot_function()  # Appelle la méthode pour tracer la fonction

    def plot_circle(self):  # Méthode pour tracer un cercle (à implémenter)
        # Logique pour tracer un cercle touchant l'origine si on veut prendre en charge cela
        pass  # À implémenter
