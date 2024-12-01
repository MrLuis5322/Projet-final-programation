import customtkinter as ctk  
import tkinter as tk  
import os
import pywinstyles

class Login(tk.Frame):  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a') # Vertical 
        self.columnconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a') # Horizontal

        self.configure(width = 800, 
                       height = 800)

        self.DOSSIER_COMPTES = os.path.join(os.path.dirname(__file__), "accounts")  # Code pour accéder aux fichiers dans "accounts"  
        pywinstyles.set_opacity(self, value = 0.9, color="#000001") # Permet de gérer l'opacité du widget
        
        self.create_widgets()
        

    def create_widgets(self):
        self.tab = ctk.CTkTabview(master = self,
                                  width = 800, 
                                  height = 800,
                                  segmented_button_fg_color = 'gold',
                                  segmented_button_selected_color = 'gold3',
                                  segmented_button_unselected_color = 'gold',
                                  segmented_button_unselected_hover_color = 'gold3',
                                  segmented_button_selected_hover_color = 'gold3')
        
        self.create = self.tab.add("Créer un compte")  # On ajoute un onglet de connexion et un onglet de céation de compte
        self.connect = self.tab.add("Se connecter")

        self.tab._segmented_button.configure(width = 100,
                                         height = 50,
                                         corner_radius = 75,
                                         text_color = 'gray14',
                                         font = ('Helvetica', 20))
        
        self.label_nom_creation = ctk.CTkLabel(self.create, 
                                               text="Nom:")
        self.champ_nom_creation = ctk.CTkEntry(self.create, 
                                               placeholder_text="Entrez votre nom") 
        self.label_password_creation = ctk.CTkLabel(self.create, 
                                                 text="Password:")  
        self.champ_password_creation = ctk.CTkEntry(self.create, 
                                                 placeholder_text="Entrez votre password") 
        self.bouton_creation_joueur = ctk.CTkButton(self.create, 
                                                    text="Créer compte", 
                                                    command = self.create_account)
                                                    #command=self.soumettre_creation_joueur)

        self.label_nom_connexion = ctk.CTkLabel(self.connect, 
                                                text="Nom:")  
        self.champ_nom_connexion = ctk.CTkEntry(self.connect, 
                                                placeholder_text="Entrez votre nom") 
        self.label_password_connexion = ctk.CTkLabel(self.connect, text="Password:")  
        self.champ_password_connexion = ctk.CTkEntry(self.connect, 
                                                  placeholder_text="Entrez votre password") 
        self.bouton_connexion_joueur = ctk.CTkButton(self.connect, 
                                                     text="Se connecter", 
                                                     command=self.connect_account) 

    def layout_widgets(self):
        self.tab.grid(row = 0, column = 0, rowspan = 5, columnspan = 5)

        self.bouton_creation_joueur.grid(row=0, column=0)
        self.champ_password_creation.grid(row=3, column=0) 
        self.label_password_creation.grid(row=2, column=0)
        self.champ_nom_creation.grid(row=1, column=0)  
        self.label_nom_creation.grid(row=0, column=0) 

        self.bouton_connexion_joueur.grid(row=4, column=0)
        self.champ_password_connexion.grid(row=3, column=0)
        self.label_password_connexion.grid(row=2, column=0)
        self.champ_nom_connexion.grid(row=1, column=0)
        self.label_nom_connexion.grid(row=0, column=0)

    def create_account(self): 
        # Récupérer les noms et email
        nom = self.champ_nom_creation.get()  
        password = self.champ_password_creation.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_COMPTES, self.nettoyer_nom_fichier(nom))

        # Fichier existe déjà?
        if os.path.exists(nom_fichier_joueur): 
            print(f"Cette identifiant existe déja!")  
        else:
        # Création fichier
            with open(nom_fichier_joueur, "w") as fichierE:  # Ouvrir fichier en écriture w pour write
                fichierE.write(f"Nom: {nom}\n")  # Écrire nom
                fichierE.write(f"Password: {password}\n")  # Écrire email
                fichierE.write("Logs:\n")  # Ajouter de logs:
                print("----------------Joueur créé----------------")  
                print(f"Nom: {nom}")  
                print(f"Email: {password}") 

    # Partie de connexion
    def connect_account(self): 
        nom = self.champ_nom_connexion.get()  
        password = self.champ_password_connexion.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_COMPTES, self.nettoyer_nom_fichier(nom)) 

        # Vérifier si le joueur existe
        # Si il n'existe pas alors erreur
        if not os.path.exists(nom_fichier_joueur):  
            print(f"Joueur {nom} non trouvé.")  
            return  

        # Lecture (j'utilise le with pour que le fichier soit fermé après)
        with open(nom_fichier_joueur, "r") as fichierL:  # Ouvrir fichier en lecture (r pour read)
            lignes = fichierL.readlines()  # Lire lignes
            email_fichier = lignes[1].strip().split(": ")[1]  # Extraire l'email du fichier (1 pour ligne 2)

        # Vérification de l'email
        if email_fichier != password:  # Email incorrect
            print(f"Email incorrect pour le joueur {nom}.") 
            return  

        print(f"Connexion réussie pour le joueur {nom}")  
        print(f"Email: {password}") 

        self.master.nom_joueur_connecte = nom  # Sauvegarder le joueur connecté
        # Log du joueur connecté
        self.ajouter_log(nom_fichier_joueur, "Le joueur s'est connecté.")  # Ajouter un log dans le fichier du joueur

    def nettoyer_nom_fichier(self, nom_fichier):  # Supprimer mauvais caractères
        return self.master.clean_filename(nom_fichier)
