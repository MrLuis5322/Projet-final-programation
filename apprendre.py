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
        self.fig, self.ax = plt.subplots(figsize=(5, 4))  # Taille réduite pour le graphique
        self.canvas = None
        
        # Appeler la fonction pour créer l'interface avec les sliders et le bouton
        self.create_function_interface()

    def create_function_interface(self):
        # Explication des fonctions disponibles
        explanation_text = "Choisissez une fonction et ajustez les paramètres.\n"
        explanation_text += "Fonctions disponibles: Quadratique, Sinus, Exponentielle"
        
        # Affichage du texte explicatif
        self.explanation_label = ctk.CTkLabel(self, text=explanation_text, font=("Arial", 12))
        self.explanation_label.pack(pady=10)
        
        # Variable pour la sélection de la fonction
        self.function_var = tk.StringVar(value="Quadratique")  # Valeur initiale
        
        # Menu déroulant pour sélectionner la fonction
        self.function_menu = ctk.CTkOptionMenu(self, values=["Quadratique", "Sinus", "Exponentielle"], variable=self.function_var, command=self.update_interface)
        self.function_menu.pack(pady=20)
        
        # Créer les sliders qui seront dynamiques selon la fonction sélectionnée
        self.a_var = tk.DoubleVar(value=1)  # Coefficient 'a' pour quadratique ou sinus
        self.h_var = tk.DoubleVar(value=0)  # Déplacement horizontal
        self.k_var = tk.DoubleVar(value=0)  # Déplacement vertical
        self.b_var = tk.DoubleVar(value=1)  # Coefficient 'b' pour sinus ou exponentielle
        
        # Créer un frame pour organiser les sliders horizontalement
        self.slider_frame = ctk.CTkFrame(self)
        self.slider_frame.pack(pady=10)

        # Créer les sliders pour les paramètres
        self.a_slider = self.create_slider("a", self.a_var, -3, 3, 0.1)
        self.h_slider = self.create_slider("h (Déplacement horizontal)", self.h_var, -5, 5, 1)
        self.k_slider = self.create_slider("k (Déplacement vertical)", self.k_var, -5, 5, 1)
        self.b_slider = self.create_slider("b (Amplitude pour Sinus/Exponentielle)", self.b_var, 0, 5, 0.1)
        
        # Créer un bouton pour afficher la courbe
        self.plot_button = ctk.CTkButton(self, text="Tracer la fonction", command=self.plot_function)
        self.plot_button.pack(pady=20)
        
        # Placer les sliders dans le frame
        self.a_slider.grid(row=0, column=0, padx=5)  # Grille pour aligner horizontalement
        self.h_slider.grid(row=0, column=1, padx=5)
        self.k_slider.grid(row=0, column=2, padx=5)
        self.b_slider.grid(row=0, column=3, padx=5)
        
        # Cacher le slider "b" au démarrage
        self.b_slider.grid_forget()
        
        # Placer un graphique vide au départ
        self.plot_function()

    def create_slider(self, label, variable, min_value, max_value, resolution):
        # Créer un slider avec un label
        frame = ctk.CTkFrame(self.slider_frame)  # Ajouter les sliders au même frame
        
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

    def update_interface(self, selected_function):
        # Fonction pour mettre à jour l'interface selon la fonction sélectionnée
        # Réinitialiser l'interface en fonction de la fonction choisie
        if selected_function == "Quadratique":
            self.b_slider.grid_forget()  # Cacher le slider b pour quadratique
        elif selected_function == "Sinus":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour sinus
        elif selected_function == "Exponentielle":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour exponentielle
        
        # Re-tracer la fonction avec la sélection mise à jour
        self.plot_function()

    def plot_function(self):
        # Fonction pour tracer la fonction en fonction des paramètres actuels
        # Récupérer les valeurs des sliders
        function = self.function_var.get()
        a = self.a_var.get()
        h = self.h_var.get()
        k = self.k_var.get()
        b = self.b_var.get()
        
        # Effacer le graphique précédent
        self.ax.clear()
        
        x = np.linspace(-10, 10, 400)  # Plage des x
        
        if function == "Quadratique":
            # Fonction quadratique : f(x) = a(x - h)^2 + k
            y = a * (x - h)**2 + k
            self.ax.set_title(f"Fonction Quadratique: f(x) = {a}(x - {h})^2 + {k}")
        elif function == "Sinus":
            # Fonction sinus : f(x) = a * sin(b * (x - h)) + k
            y = a * np.sin(b * (x - h)) + k
            self.ax.set_title(f"Fonction Sinus: f(x) = {a} * sin({b} * (x - {h})) + {k}")
        elif function == "Exponentielle":
            # Fonction exponentielle : f(x) = a * exp(b * (x - h)) + k
            y = a * np.exp(b * (x - h)) + k
            self.ax.set_title(f"Fonction Exponentielle: f(x) = {a} * exp({b} * (x - {h})) + {k}")
        
        # Tracer la fonction
        self.ax.plot(x, y)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('f(x)')
        
        # Fixer les limites des axes
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        
        self.ax.grid(True)
        
        # Afficher le graphique dans l'interface tkinter
        if self.canvas:
            self.canvas.draw()
        else:
            self.canvas = FigureCanvasTkAgg(self.fig, self)
            self.canvas.get_tk_widget().pack(pady=20)
            self.canvas.draw()

if __name__ == "__main__":  # Vérifier si ce fichier est exécuté en tant que programme principal
    root = ctk.CTk()  # Créer la fenêtre principale
    app = Apprendre(root)  # Créer l'application
    app.pack(expand=True, fill="both")  # Ajouter l'application dans la fenêtre
    root.mainloop()  # Lancer la boucle principale de tkinter
