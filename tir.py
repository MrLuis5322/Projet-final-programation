import numpy as np  
import matplotlib.pyplot as plt 
import tkinter as tk  

class Tir: 
    def __init__(self, accueil):  # Constructeur qui prend en paramètre notre interface graphique
        self.accueil = accueil 
# Méthode pour tracer une fonction
    def plot_function(self):  
        func_text = self.accueil.entry_func.get()  # Récupère la fonction entrée par l'utilisateur
        if not func_text:  # Vérifie si la fonction est vide
            print("Veuillez entrer une fonction valide.")  # Affiche un message d'erreur
            return  

        x = np.linspace(-100, 100, 1000)  # Crée un tableau de 1000 valeurs de x entre -100 et 100

        try:
            # Évalue la fonction entrée en utilisant NumPy et les valeurs de x (vient de cgatgpt fac jsp si vous voulez le modifier)
            y = eval(func_text, {"np": np, "x": x})  
            self.accueil.ax.plot(x, y, label=f'f(x)={func_text}') 
            self.accueil.ax.legend() 
            self.accueil.canvas.draw()  
        except Exception as e:  
            print(f"Erreur lors du traçage de la fonction : {e}")  

    def reset_plot(self):  # Méthode pour réinitialiser le graphique
        self.accueil.ax.clear()  # Efface l'axe du graphique
        self.accueil.plot_obstacles_and_goal()  # Rétrace les obstacles et la cible
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
