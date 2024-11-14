import tkinter as tk
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Apprendre(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Créer un titre pour la fenêtre d'apprentissage
        self.title_label = ctk.CTkLabel(self, text="Fenêtre d'Apprentissage", font=("Arial", 20))
        self.title_label.pack(pady=10)  # Afficher le titre
        
        # Créer une figure et un axe pour le graphique
        self.fig, self.ax = plt.subplots()
        self.canvas = None
        
        # Appeler la fonction pour créer l'interface avec les sliders et le bouton
        self.create_quadratic_interface()

    def create_quadratic_interface(self):
        # Explication de la fonction quadratique
        explanation_text = "Fonction Quadratique: f(x) = a(x - h)^2 + k\n"
        explanation_text += "Ajustez les sliders pour voir l'impact sur la fonction."
        
        # Affichage du texte explicatif
        self.explanation_label = ctk.CTkLabel(self, text=explanation_text, font=("Arial", 12))
        self.explanation_label.pack(pady=10)
        
        # Variables pour les paramètres de la fonction quadratique
        self.a_var = tk.DoubleVar(value=1)  # Coefficient 'a'
        self.h_var = tk.DoubleVar(value=0)  # Déplacement horizontal 'h'
        self.k_var = tk.DoubleVar(value=0)  # Déplacement vertical 'k'
        
        # Créer les sliders pour chaque paramètre
        self.a_slider = self.create_slider("a (Coefficient de la parabole)", self.a_var, -3, 3, 0.1)
        self.h_slider = self.create_slider("h (Déplacement horizontal)", self.h_var, -5, 5, 1)
        self.k_slider = self.create_slider("k (Déplacement vertical)", self.k_var, -5, 5, 1)
        
        # Créer un bouton pour afficher la courbe
        self.plot_button = ctk.CTkButton(self, text="Tracer la fonction", command=self.plot_function)
        self.plot_button.pack(pady=20)
        
        # Placer les sliders dans l'interface
        self.a_slider.pack(pady=10)
        self.h_slider.pack(pady=10)
        self.k_slider.pack(pady=10)
        
        # Mettre à jour le graphique initialement avec les valeurs des sliders
        self.plot_function()

    def create_slider(self, label, variable, min_value, max_value, resolution):
        # Créer un slider avec un label
        frame = ctk.CTkFrame(self)
        
        # Ajouter un label pour chaque slider
        slider_label = ctk.CTkLabel(frame, text=label)
        slider_label.pack(pady=5)
        
        # Créer un slider
        slider = ctk.CTkSlider(
            frame, 
            from_=min_value,  # Valeur minimale
            to=max_value,     # Valeur maximale (utiliser 'to' au lieu de 'to_')
            number_of_steps=int((max_value - min_value) / resolution),
            variable=variable
        )
        slider.pack(padx=20, pady=5)
        
        return frame

    def plot_function(self):
        # Fonction pour tracer la fonction quadratique avec les valeurs des sliders
        # Récupérer les valeurs des sliders
        a = self.a_var.get()
        h = self.h_var.get()
        k = self.k_var.get()
        
        # Fonction quadratique : f(x) = a(x - h)^2 + k
        x = np.linspace(-10, 10, 400)
        y = a * (x - h)**2 + k
        
        # Effacer le graphique précédent
        self.ax.clear()
        
        # Tracer la nouvelle fonction
        self.ax.plot(x, y, label=f'f(x) = {a}(x - {h})^2 + {k}')
        self.ax.set_title('Fonction Quadratique')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('f(x)')
        
        # Fixer les limites des axes
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        
        self.ax.grid(True)
        self.ax.legend()

        # Afficher le graphique dans l'interface tkinter
        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvasTkAgg(self.fig, self)
            self.canvas.get_tk_widget().pack(pady=20)
            self.canvas.draw()


