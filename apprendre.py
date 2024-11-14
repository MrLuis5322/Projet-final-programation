import tkinter as tk
import random
import customtkinter as ctk

class Apprendre(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Simuler un titre en ajoutant un Label dans le frame
        self.title_label = ctk.CTkLabel(self, text="Fenêtre d'Apprentissage", font=("Arial", 20))
        self.title_label.pack(pady=10)  # Positionner le titre en haut du frame

        # Fonction pour générer un test aléatoire
        def generate_random_test():
            print("test")

        # Créer un bouton pour générer un test aléatoire
        test_button = ctk.CTkButton(self, 
                                    text="Générer un test", 
                                    command=generate_random_test, 
                                    width=200,
                                    height=50,
                                    corner_radius=20,
                                    fg_color='blue')
        test_button.pack(pady=20)

       
