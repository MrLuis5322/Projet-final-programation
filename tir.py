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
            print("Veuillez entrer une fonction valide.")  # Affiche un message d'erreur
            return
        
        # Position du joueur et de la cible
        joueur_pos = self.accueil.joueur.joueur_position 
        cible_pos = self.accueil.joueur.cible_position  
        # Convertir en coordonnées
        x_joueur, y_joueur = joueur_pos 
        x_cible, y_cible = cible_pos

        #Déterminer les limites du tracé selon la position de la cible
        if x_cible > x_joueur:
            x_max = 400  # Tracé vers la droite
            x_min = x_joueur
        else:
            x_max = x_joueur  # Tracé vers la gauche
            x_min = 0

        # Générer des valeurs x entre les limites définies
        x_fct = np.linspace(x_min, x_max, 2000)

        # Inverser l'ordre des valeurs x et y si la cible est à gauche du joueur
        if x_cible < x_joueur:
            x_fct = x_fct[::-1]
        
        # Évaluer l'équation pour obtenir y
        try:
            y_fct = eval(equation, {"x": x_fct, "np": np})
        except Exception as e:
            print(f"Erreur dans l'équation : {e}")
            return
        
        # Appliquer la translation pour que le (0,0) de la fonction soit le joueur
        if y_joueur > y_fct[0]:
            y_fct = y_fct + (y_joueur - y_fct[0])
        else:
            y_fct = y_fct - (y_fct[0] - y_joueur)

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
        self.accueil.ax.plot(trajectoire_x, trajectoire_y, label=f'f(x)={equation}') 
        # Effe de collision
        if collision_x is not None and collision_y is not None:
            self.accueil.ax.plot(collision_x, collision_y, 'ro', markersize=2)  # 'ro' pour 'red dot'
    
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
        self.accueil.ax.legend(loc="upper left", prop={"size": 7}, markerscale=0.6, bbox_to_anchor=(1, 1))
        self.accueil.canvas.draw()