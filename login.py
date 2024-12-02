import customtkinter as ctk  
import tkinter as tk  
import os
import pywinstyles

class Login(tk.Frame):  
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(width = 800, 
                       height = 800,
                       bg = 'gray14')
        
        self.nom = ""
        
        self.rowconfigure(0, weight = 1, uniform = 'a') # Vertical 
        self.columnconfigure(0, weight = 1, uniform = 'a') # Horizontal

        self.DOSSIER_COMPTES = os.path.join(os.path.dirname(__file__), "accounts")  # Code pour accéder aux fichiers dans "accounts"  
        pywinstyles.set_opacity(self, value = 0.95, color="#000001") # Permet de gérer l'opacité du widget
        
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
        
        self.connect = self.tab.add("Se connecter")
        self.create = self.tab.add("Créer un compte")

        self.tab._segmented_button.configure(width = 100,
                                         height = 50,
                                         corner_radius = 75,
                                         text_color = 'gray14',
                                         font = ('Helvetica', 20))
        
        self.warning1 = ctk.CTkLabel(self.connect, 
                                               text="",
                                               width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))
        self.label_nom_creation = ctk.CTkLabel(self.create, 
                                               text="Username:",
                                               width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))
        self.champ_nom_creation = ctk.CTkEntry(self.create, 
                                               placeholder_text="Entrez votre nom",
                                               width = 200,
                                                height = 50,
                                                corner_radius = 75,
                                                font = ('Helvetica', 20),) 
        self.label_password_creation = ctk.CTkLabel(self.create, 
                                                 text="Password:",
                                                 width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))  
        self.champ_password_creation = ctk.CTkEntry(self.create, 
                                                 placeholder_text="Entrez votre password",
                                                 width = 200,
                                                height = 50,
                                                corner_radius = 75,
                                                font = ('Helvetica', 20)) 
        self.bouton_creation_joueur = ctk.CTkButton(self.create, 
                                                    width = 200, 
                                                    height = 50, 
                                                    border_width = 0, 
                                                    corner_radius = 75, 
                                                    text="Créer mon compte", 
                                                    font = ('Helvetica', 20),
                                                    command=self.create_account, 
                                                    text_color='gray14',
                                                    hover_color = 'gold3',
                                                    fg_color = 'gold')
        self.bouton_retour1 = ctk.CTkButton(self.create,
                                            text="Retour", 
                                            command = lambda:self.parent.changeWindow(0, 1),
                                            width = 200, 
                                            height = 50, 
                                            border_width = 0, 
                                            corner_radius = 75,
                                            font = ('Helvetica', 20),
                                            text_color='gray14',
                                            hover_color = 'gold3',
                                            fg_color = 'gold')

        self.warning2 = ctk.CTkLabel(self.create, 
                                               text="",
                                               width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))
        self.label_nom_connexion = ctk.CTkLabel(self.connect, 
                                                text="Username:",
                                                width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))  
        self.champ_nom_connexion = ctk.CTkEntry(self.connect, 
                                                placeholder_text="Entrez votre username",
                                                width = 200,
                                                height = 50,
                                                corner_radius = 75,
                                                font = ('Helvetica', 20)) 
        self.label_password_connexion = ctk.CTkLabel(self.connect, 
                                                     text="Password:",
                                                     width = 200,
                                                height = 50,
                                                fg_color= 'transparent',
                                                text_color = 'gold',
                                                font = ('Helvetica', 30))  
        self.champ_password_connexion = ctk.CTkEntry(self.connect, 
                                                  placeholder_text="Entrez votre password",
                                                  width = 200,
                                                    height = 50,
                                                    corner_radius = 75,
                                                    font = ('Helvetica', 20)) 
        self.bouton_connexion_joueur = ctk.CTkButton(self.connect, 
                                                     text="Se connecter", 
                                                     command=self.connect_account,
                                                     width = 200, 
                                                    height = 50, 
                                                    border_width = 0, 
                                                    corner_radius = 75,
                                                    font = ('Helvetica', 20),
                                                    text_color='gray14',
                                                    hover_color = 'gold3',
                                                    fg_color = 'gold') 
        self.bouton_retour2 = ctk.CTkButton(self.connect,
                                            text="Retour", 
                                            command = lambda:self.parent.changeWindow(0, 1),
                                            width = 200, 
                                            height = 50, 
                                            border_width = 0, 
                                            corner_radius = 75,
                                            font = ('Helvetica', 20),
                                            text_color='gray14',
                                            hover_color = 'gold3',
                                            fg_color = 'gold')


    def layout_widgets(self):
        self.tab.grid(row = 0, column = 0)

        self.create.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
        self.create.columnconfigure(0, weight = 1, uniform = 'a')

        self.bouton_creation_joueur.grid(row=5, column=0)
        self.champ_password_creation.grid(row=4, column=0) 
        self.label_password_creation.grid(row=3, column=0)
        self.champ_nom_creation.grid(row=2, column=0)  
        self.label_nom_creation.grid(row=1, column=0) 
        self.bouton_retour1.grid(row = 6, column = 0)
        self.warning1.grid(row = 0, column = 0)

        self.connect.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
        self.connect.columnconfigure(0, weight = 1, uniform = 'a')

        self.bouton_connexion_joueur.grid(row=5, column=0)
        self.champ_password_connexion.grid(row=4, column=0)
        self.label_password_connexion.grid(row=3, column=0)
        self.champ_nom_connexion.grid(row=2, column=0)
        self.label_nom_connexion.grid(row=1, column=0)
        self.bouton_retour2.grid(row = 6, column = 0)
        self.warning2.grid(row = 0, column = 0)

    def create_account(self): 
        # Récupérer les noms et email
        nom = self.champ_nom_creation.get()  
        password = self.champ_password_creation.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_COMPTES, self.nettoyer_nom_fichier(nom))

        # Fichier existe déjà?
        if os.path.exists(nom_fichier_joueur): 
            self.warning2.configure(text = 'Ce nom existe déja!')
        else:
        # Création fichier
            with open(nom_fichier_joueur, "w") as fichierE:  # Ouvrir fichier en écriture w pour write
                fichierE.write(f"Nom: {nom}\n")  # Écrire nom
                fichierE.write(f"Password: {password}\n")  # Écrire email
                fichierE.write("Logs:\n")  # Ajouter de logs:
            self.warning2.configure(text = 'Compte créé, veuillez vous connecter')

    # Partie de connexion
    def connect_account(self): 
        self.nom = self.champ_nom_connexion.get()  
        self.password = self.champ_password_connexion.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_COMPTES, self.nettoyer_nom_fichier(self.nom)) 

        # Vérifier si le joueur existe
        # Si il n'existe pas alors erreur
        if not os.path.exists(nom_fichier_joueur):  
            self.warning1.configure(text = "Ce compte n'existe pas!")
            return
        
        # Lecture (j'utilise le with pour que le fichier soit fermé après)
        with open(nom_fichier_joueur, "r") as fichierL:  # Ouvrir fichier en lecture (r pour read)
            lignes = fichierL.readlines()  # Lire lignes
            email_fichier = lignes[1].strip().split(": ")[1]  # Extraire le password du fichier (1 pour ligne 2)

        # Vérification de l'email
        if email_fichier != self.password:  # Email incorrect
            self.warning1.configure(text = "Ce compte n'existe pas!")
            return  

        self.warning1.configure(text = f'Connexion réussie pour le joueur {self.nom}')

        self.master.nom_joueur_connecte = self.nom  # Sauvegarder le joueur connecté

    def nettoyer_nom_fichier(self, nom_fichier):  # Supprimer mauvais caractères
        return self.master.clean_filename(nom_fichier)
