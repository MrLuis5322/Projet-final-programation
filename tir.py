import numpy as np  
from joueur import Joueur
import tkinter as tk

# Fonction pour vérifier si un point est dans un cercle
def touche_au_cercle(x, y, cercle_x, cercle_y, rayon):
    return (x - cercle_x)**2 + (y - cercle_y)**2 <= rayon**2

class Tir: 
    def __init__(self, accueil):  # Constructeur qui prend en paramètre notre interface graphique
        self.accueil = accueil 
        self.obstacles = accueil.obstacles  # Initialiser les obstacles

    def plot_function(self):  
        equation = self.accueil.entry_func.get()  # Récupère la fonction entrée par l'utilisateur
        
        if not equation:  # Vérifie si la fonction est vide
            print("Veuillez entrer une fonction valide.")  # Affiche un message d'erreur A AJOUTER AU LOG *****************************************************
            return
        
        # Sécurité pour éviter les transaltion verticale (pour eviter une fonction qui ne partirait pas du joueur)
        nb_plus, nb_moins, nb_x, no = 0, 0, 0, 0 
        if '+' or '-' in equation:
            for i in equation:
                if i == '+' : nb_plus += 1
                if i == 'x' : nb_x += 1
                if i == '-' and equation[no+1] != 'x': nb_moins += 1
                no += 1
            if nb_plus >= nb_x or nb_moins >= nb_x:
                print("La fonction ne peut pas être translatée verticalement.")
                return
        
        # Position du joueur et de la cible
        joueur_pos = self.accueil.joueur.joueur_position 
        cible_pos = self.accueil.joueur.cible_position  
        # Convertir en coordonnées
        x_joueur, y_joueur = joueur_pos 
        x_cible, y_cible = cible_pos

        # Générer des valeurs x entre les limites du plan (x = [0, 360], y = [0, 200])
        x_fct = np.linspace(0, 360, 2000)
        
        # Évaluer l'équation pour obtenir y
        try:
            y_fct = eval(equation, {"x": x_fct, "np": np})
        except Exception as e:
            print(f"Erreur dans l'équation : {e}")
            return
        
        # Faire une translation horizontale et vertical de la fonction afin de la faire commencer (0,0) au joueur (x_joueur, y_joueur)
        x_fct = x_fct + x_joueur
        y_fct = y_fct + y_joueur

        # Appliquer une réflexion si le joueur est à droite de la cible
        if x_joueur > x_cible:
            # Calcul de la réflexion : inversion des valeurs x autour de x_joueur
            x_fct = 2 * x_joueur - x_fct

        # Initialiser les listes pour le tracé limité
        trajectoire_x = []
        trajectoire_y = []
        # Stocker les coordonnées des collisons
        collision_x = None 
        collision_y = None
        cible_touchee = False

        # Vérification des collisions
        for i in range(len(x_fct)):
            # Vérifier la collision avec les obsatcles 
            collision = False
            for obstacle in self.obstacles:  # Itération sur les obstacles
                x, y, r = obstacle  # Décomposition de l'obsatcles
                if touche_au_cercle(x_fct[i], y_fct[i], x, y, r):
                    print(f"Obstacle touché en : ({x_fct[i]:.2f}, {y_fct[i]:.2f})")
                    collision_x = x_fct[i]
                    collision_y = y_fct[i]
                    collision = True
                    break 
                else:
                    trajectoire_x.append(x_fct[i])
                    trajectoire_y.append(y_fct[i])

            # Vérifier la collision avec la cible
            if touche_au_cercle(x_fct[i], y_fct[i], x_cible, y_cible, 5):
                print(f"Cible touchée en : ({x_fct[i]:.2f}, {y_fct[i]:.2f})")
                cible_touchee = True
                collision = True
                break
            else:
                trajectoire_x.append(x_fct[i])
                trajectoire_y.append(y_fct[i])

            if collision:
                self.accueil.update_score(-1)#-1 point pour le joueur
                self.accueil.update_score_ville()
                self.accueil.master.ajouter_log(f"Perte d'un point") #log
                break  # Quitte la boucle

        # Trajectoire
        self.accueil.ax.plot(trajectoire_x, trajectoire_y) #label=f'f(x)={equation}
        # Effe de collision
        if collision_x is not None and collision_y is not None:
            self.accueil.ax.plot(collision_x, collision_y, 'x', markersize=15*self.accueil.res)

        # Arranger le visuel
        self._finalize_plot()

        # Si la cible est touchée, ajoutez un délai, puis réinitialisez la scène
        if cible_touchee:
            self.cible_atteinte()  # Appelle la méthode pour gérer la réinitialisation après la cible atteinte
            
    def cible_atteinte(self):
        self.accueil.after(800, self.reset_plot)  # Attente de 1 secondes avant réinitialisation
        self.accueil.update_score(1)#Ajouter 1 point
        self.accueil.update_score_cible()
        self.accueil.master.ajouter_log(f"Ajout d'un point")#log

    def reset_plot(self):
        self.accueil.ax.clear()
        # Générer de nouveaux obstacles et mettre à jour les obstacles dans l'instance Tir
        self.accueil.obstacles = self.accueil.obstacles_instance.generer_obstacles()
        self.obstacles = self.accueil.obstacles
        # Générer un nouveau joueur avec les nouveaux obstacles
        self.accueil.joueur = Joueur(self.accueil, self.accueil.obstacles)
        self.accueil.plot_obstacles_and_goal()
        # Tracer les obstacles et la cible
        self._finalize_plot()

        if self.accueil.timer_label.cget("text") == "Temps écoulé!": #https://stackoverflow.com/questions/6112482/how-to-get-the-tkinter-label-text
            self.accueil.temps = 61
            self.accueil.timer_label.configure(text=f"Temps restant: {self.accueil.temps}s")  # Remettre à jour l'affichage du timer
            self.accueil.update_timer()
            self.accueil.score = 0
            self.accueil.update_score(0)

    def plot_selected_function(self, choice): # Méthode pour tracer une fonction sélectionnée
        func_text = self.accueil.function_types.get(choice) # Récupère la fonction associée au choix
        self.accueil.entry_func.delete(0, tk.END) # Efface le champ de saisie
        self.accueil.entry_func.insert(0, func_text) # Insère la fonction sélectionnée dans le champ
        self.plot_function() # Appelle la méthode pour tracer la fonction

    def _finalize_plot(self):
        self.accueil.ax.set_xticks([])
        self.accueil.ax.set_yticks([])
        self.accueil.ax.legend(loc="upper left", prop={"size": 15*self.accueil.res}, markerscale=0.6*self.accueil.res, bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()
