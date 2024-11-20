import tkinter as tk
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinterweb import HtmlFrame  # Importer HtmlFrame de tkinterweb
import socket
from tkinter import messagebox

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
        explanation_text += "Fonctions disponibles: Quadratique, Sinus, Exponentielle, Cosinus, Racine carrée, Linéaire"
        
        # Affichage du texte explicatif
        self.explanation_label = ctk.CTkLabel(self, text=explanation_text, font=("Arial", 12))
        self.explanation_label.pack(pady=10)
        
        # Variable pour la sélection de la fonction (défaut: Linéaire)
        self.function_var = tk.StringVar(value="Linéaire")  # Valeur initiale = Linéaire
        
        # Menu déroulant pour sélectionner la fonction
        self.function_menu = ctk.CTkOptionMenu(self, values=["Linéaire", "Quadratique", "Sinus", "Cosinus", "Exponentielle", "Racine carrée"], variable=self.function_var, command=self.update_interface)
        self.function_menu.pack(pady=20)
        
        # Ajouter un menu déroulant pour choisir le type de plan
        self.plan_var = tk.StringVar(value="Plan complet")  # Valeur initiale = Plan complet
        self.plan_menu = ctk.CTkOptionMenu(self, values=["Plan complet", "Quadrant positif"], variable=self.plan_var, command=self.update_interface)
        self.plan_menu.pack(pady=20)
        
        # Créer les sliders qui seront dynamiques selon la fonction sélectionnée
        self.a_var = tk.DoubleVar(value=1)  # Coefficient 'a' pour quadratique ou linéaire
        self.h_var = tk.DoubleVar(value=0)  # Déplacement horizontal
        self.k_var = tk.DoubleVar(value=0)  # Déplacement vertical
        self.b_var = tk.DoubleVar(value=1)  # Coefficient 'b' pour sinus, cosinus, exponentielle, linéaire (défaut 1)
        
        # Créer un frame pour organiser les sliders horizontalement
        self.slider_frame = ctk.CTkFrame(self)
        self.slider_frame.pack(pady=10)

        # Créer les sliders et les paramètres (label, variable, min, max, indentation)
        self.a_slider = self.create_slider("a", self.a_var, -3, 3, 0.1)
        self.h_slider = self.create_slider("h (Déplacement horizontal)", self.h_var, -5, 5, 1)
        self.k_slider = self.create_slider("k (Déplacement vertical)", self.k_var, -5, 5, 1)
        self.b_slider = self.create_slider("b", self.b_var, -5, 5, 0.1)
        
        # Créer un bouton pour afficher la courbe
        self.plot_button = ctk.CTkButton(self, text="Tracer la fonction", command=self.plot_function)
        self.plot_button.pack(pady=20)
        
        #ouvrir lien internet
        self.link = ctk.CTkButton(self, text="En apprendre plus", command=self.ouvrir_lien)
        self.link.pack(pady = 25)

        # Placer les sliders dans le frame
        self.a_slider.grid(row=0, column=0, padx=5)  # Grille pour aligner horizontalement
        self.h_slider.grid(row=0, column=1, padx=5)
        self.k_slider.grid(row=0, column=2, padx=5)
        self.b_slider.grid(row=0, column=3, padx=5)
        
        # Cacher les sliders non pertinents au démarrage
        self.h_slider.grid_forget()
        self.k_slider.grid_forget()
        
        # Placer un graphique linéaire vide au départ
        self.plot_function()
        

    def ouvrir_lien(self):
        # Vérifier la connexion
        if not self.est_online():
        # Afficher un message d'erreur si l'application est hors ligne
            messagebox.showerror("Erreur de connexion", "Aucune connexion Internet. Impossible d'afficher la page.")
            return  # Sortir de la fonction si pas de connexion
    
    # Création de la fenêtre secondaire
        nouvelle_fenetre = tk.Toplevel()
        nouvelle_fenetre.title("Fenêtre avec page Web")
        nouvelle_fenetre.geometry("800x600")  # Taille de la fenêtre

    # Créer un cadre HTML (widget) dans la fenêtre pour afficher la page Web
        html_frame = HtmlFrame(nouvelle_fenetre, horizontal_scrollbar="auto")
        html_frame.place(relwidth=1, relheight=1)

    # Charger la page Web dans le HtmlFrame
        function = self.function_var.get()  # Récupérer la fonction sélectionnée

        if function == "Quadratique":
           url = "https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-fonction-polynomiale-de-degre-2-m1124"
        elif function == "Sinus":
            url = "https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-fonction-sinus-m1171"
        elif function == "Exponentielle":
            url = "https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-fonction-exponentielle-m1143"
        elif function == "Cosinus":
            url = "https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-fonction-cosinus-m1177"
        elif function == "Racine carrée":
            url = "https://www.alloprof.qc.ca/fr/eleves/bv/mathematiques/la-fonction-racine-carree-m1131"
        elif function == "Linéaire":
            url = "https://www.example.com"

        #url = "https://www.example.com"  # Remplacer par l'URL que vous voulez afficher
        html_frame.load_url(url)

    def est_online(self):
        try:
        # On tente de se connecter à un serveur public (par exemple, Google) port 80 pour HTTP, 5 secondes pour se conecter sinon echec
        #Cette méthode tente d'établir une connexion réseau à un hôte et un port spécifiés.
            socket.create_connection(("www.google.com", 80), timeout=5)
            return True  # Connexion réussie
        #Cette exception est levée si une erreur se produit lors de la résolution du nom de domaine (par exemple, si www.google.com ne peut pas être trouvé) ou si le temps de 5 sec est fini
        except (socket.timeout, socket.gaierror):
            return False  # Pas de connexion

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

    def update_interface(self, selected_function=None):
        # Fonction pour mettre à jour l'interface selon la fonction sélectionnée
        # Réinitialiser l'interface en fonction de la fonction choisie
        if selected_function is None:
            selected_function = self.function_var.get()

        if selected_function == "Quadratique":
            self.b_slider.grid_forget()  # Cacher le slider b pour quadratique
            self.h_slider.grid(row=0, column=1, padx=5)  # Afficher le slider h pour quadratique
            self.k_slider.grid(row=0, column=2, padx=5)  # Afficher le slider k pour quadratique
        elif selected_function == "Sinus":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour sinus
            self.h_slider.grid(row=0, column=1, padx=5)  # Afficher le slider h pour sinus
            self.k_slider.grid(row=0, column=2, padx=5)  # Afficher le slider k pour sinus
        elif selected_function == "Exponentielle":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour exponentielle
            self.h_slider.grid(row=0, column=1, padx=5)  # Afficher le slider h pour exponentielle
            self.k_slider.grid(row=0, column=2, padx=5)  # Afficher le slider k pour exponentielle
        elif selected_function == "Cosinus":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour cosinus
            self.h_slider.grid(row=0, column=1, padx=5)  # Afficher le slider h pour cosinus
            self.k_slider.grid(row=0, column=2, padx=5)  # Afficher le slider k pour cosinus
        elif selected_function == "Racine carrée":
            self.b_slider.grid_forget()  # Cacher le slider b pour racine carrée
            self.h_slider.grid(row=0, column=1, padx=5)  # Afficher le slider h pour racine carrée
            self.k_slider.grid(row=0, column=2, padx=5)  # Afficher le slider k pour racine carrée
        elif selected_function == "Linéaire":
            self.b_slider.grid(row=0, column=3, padx=5)  # Afficher le slider b pour linéaire
            self.h_slider.grid_forget()  # Cacher le slider h pour linéaire
            self.k_slider.grid_forget()  # Cacher le slider k pour linéaire
        
        # Re-tracer la fonction avec la sélection mise à jour
        self.plot_function()

    def plot_function(self):
        # Fonction pour tracer la fonction en fonction des paramètres actuels
        function = self.function_var.get()  # Récupérer la fonction sélectionnée
        plan_type = self.plan_var.get()  # Récupérer l'option de plan sélectionnée
        
        # Effacer le graphique précédent
        self.ax.clear()

        # Tracer la fonction en fonction du type choisi
        x = np.linspace(0, 10, 400) if plan_type == "Quadrant positif" else np.linspace(-10, 10, 400)
        a = self.a_var.get()
        b = self.b_var.get()
        h = self.h_var.get()
        k = self.k_var.get()

        if function == "Quadratique":
            y = a * (x - h) ** 2 + k
            self.ax.plot(x, y, label=f"f(x) = {a} * (x - {h})^2 + {k}")
            self.ax.set_title(f"Fonction Quadratique: f(x) = {a} * (x - {h})^2 + {k}")
        elif function == "Sinus":
            y = a * np.sin(b * (x - h)) + k
            self.ax.plot(x, y, label=f"f(x) = {a} * sin({b} * (x - {h})) + {k}")
            self.ax.set_title(f"Fonction Sinus: f(x) = {a} * sin({b} * (x - {h})) + {k}")
        elif function == "Exponentielle":
            y = a * np.exp(b * (x - h)) + k
            self.ax.plot(x, y, label=f"f(x) = {a} * exp({b} * (x - {h})) + {k}")
            self.ax.set_title(f"Fonction Exponentielle: f(x) = {a} * exp({b} * (x - {h})) + {k}")
        elif function == "Cosinus":
            y = a * np.cos(b * (x - h)) + k
            self.ax.plot(x, y, label=f"f(x) = {a} * cos({b} * (x - {h})) + {k}")
            self.ax.set_title(f"Fonction Cosinus: f(x) = {a} * cos({b} * (x - {h})) + {k}")
        elif function == "Racine carrée":
            x = x[x >= h]  # Limiter x pour éviter les valeurs négatives dans la racine carrée
            y = a * np.sqrt(x - h) + k
            self.ax.plot(x, y, label=f"f(x) = {a} * sqrt(x - {h}) + {k}")
            self.ax.set_title(f"Fonction Racine Carrée: f(x) = {a} * sqrt(x - {h}) + {k}")
        elif function == "Linéaire":
            y = a * x + b
            self.ax.plot(x, y, label=f"f(x) = {a} * x + {b}")
            self.ax.set_title(f"Fonction Linéaire: f(x) = {a} * x + {b}")

        # Limiter les axes de -10 à 10 pour x et y, ou juste pour le quadrant positif
        if plan_type == "Quadrant positif":
            self.ax.set_xlim(0, 10)
            self.ax.set_ylim(0, 10)
        else:
            self.ax.set_xlim(-10, 10)
            self.ax.set_ylim(-10, 10)

        # Ajouter une grille et légende
        self.ax.grid(True)
        self.ax.legend()

        # Redessiner le graphique sur le canvas
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(pady=20)
        self.canvas.draw()


# Lancer l'application pour test uniquementt
if __name__ == "__main__":
    root = ctk.CTk()  # Créer la fenêtre principale
    app = Apprendre(root)  # Créer l'application
    app.pack(expand=True, fill="both")  # Ajouter l'application dans la fenêtre
    root.mainloop()  # Lancer la boucle principale de tkinter
