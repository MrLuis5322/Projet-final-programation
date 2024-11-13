import customtkinter as ctk  
import tkinter as tk  
import os

class Formulaire(ctk.CTkFrame):  
    def __init__(self, maitre=None):  
        self.DOSSIER_JOUEURS = os.path.join(os.path.dirname(__file__), "accounts")  # Code pour accéder aux fichiers dans "accounts"
        super().__init__(maitre)  
        self.grid(row=0, column=0, sticky="nsew")  # Le formulaire occupe tout l'espace disponible
        self.master.grid_rowconfigure(0, weight=1)  # Configure la première ligne de la fenêtre principale pour pouvoir redimensionner
        self.master.grid_columnconfigure(0, weight=1)  # Configure la première colonne de la fenêtre principale pour pouvoir redimensionner
        self.creer_widgets()

    def creer_widgets(self):
        # Créer un cadre qui contiendra le formulaire et le centrer
        cadre = ctk.CTkFrame(self) 
        cadre.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        cadre.grid_rowconfigure(0, weight=1)  # Permet au formulaire de prendre tout l'espace vertical
        cadre.grid_columnconfigure(0, weight=1)  # Permet au formulaire de prendre tout l'espace horizontal

        # Partie onglets
        self.onglets = ctk.CTkTabview(master=cadre)  
        self.onglets.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)  # Le formulaire occupera tout l'espace disponible dans le cadre

        # Partie créer joueur
        self.onglets.add("Créer un Joueur")  # Ajout de l'onglet "Créer un Joueur"
        self.formulaire_creation_joueur = ctk.CTkFrame(self.onglets.tab("Créer un Joueur"))  
        self.formulaire_creation_joueur.grid(row=0, column=0, padx=20, pady=20)

        self.label_nom_creation = ctk.CTkLabel(self.formulaire_creation_joueur, text="Nom:")
        self.label_nom_creation.grid(row=0, column=0, pady=5)
        
        self.champ_nom_creation = ctk.CTkEntry(self.formulaire_creation_joueur, placeholder_text="Entrez votre nom")  
        self.champ_nom_creation.grid(row=1, column=0, pady=5)

        self.label_email_creation = ctk.CTkLabel(self.formulaire_creation_joueur, text="Email:")  
        self.label_email_creation.grid(row=2, column=0, pady=5)  
        
        self.champ_email_creation = ctk.CTkEntry(self.formulaire_creation_joueur, placeholder_text="Entrez votre email")  
        self.champ_email_creation.grid(row=3, column=0, pady=5)  

        self.bouton_creation_joueur = ctk.CTkButton(self.formulaire_creation_joueur, text="Créer Joueur", command=self.soumettre_creation_joueur)
        self.bouton_creation_joueur.grid(row=4, column=0, pady=10)

        # Partie connexion
        self.onglets.add("Se connecter")  # Ajout de l'onglet "Se connecter"
        self.formulaire_connexion_joueur = ctk.CTkFrame(self.onglets.tab("Se connecter"))  
        self.formulaire_connexion_joueur.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)  # Utilisation de grid ici

        # Configuration du grid
        self.formulaire_connexion_joueur.grid_columnconfigure(0, weight=1)  # Pour que les widgets prennent tout l'espace

        self.label_nom_connexion = ctk.CTkLabel(self.formulaire_connexion_joueur, text="Nom:")  
        self.label_nom_connexion.grid(row=0, column=0, pady=5)
        
        self.champ_nom_connexion = ctk.CTkEntry(self.formulaire_connexion_joueur, placeholder_text="Entrez votre nom")  
        self.champ_nom_connexion.grid(row=1, column=0, pady=5)

        self.label_email_connexion = ctk.CTkLabel(self.formulaire_connexion_joueur, text="Email:")  
        self.label_email_connexion.grid(row=2, column=0, pady=5)
        
        self.champ_email_connexion = ctk.CTkEntry(self.formulaire_connexion_joueur, placeholder_text="Entrez votre email")  
        self.champ_email_connexion.grid(row=3, column=0, pady=5)

        self.bouton_connexion_joueur = ctk.CTkButton(self.formulaire_connexion_joueur, text="Se connecter", command=self.soumettre_connexion_joueur) 
        self.bouton_connexion_joueur.grid(row=4, column=0, pady=10)

    def soumettre_creation_joueur(self): 
        # Récupérer les noms et email
        nom = self.champ_nom_creation.get()  
        email = self.champ_email_creation.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_JOUEURS, self.nettoyer_nom_fichier(nom))

        # Fichier existe déjà?
        if os.path.exists(nom_fichier_joueur): 
            print(f"Le joueur {nom} a déjà été créé.")  
            return 

        # Création fichier
        with open(nom_fichier_joueur, "w") as fichierE:  # Ouvrir fichier en écriture w pour write
            fichierE.write(f"Nom: {nom}\n")  # Écrire nom
            fichierE.write(f"Email: {email}\n")  # Écrire email
            fichierE.write("Logs:\n")  # Ajouter de logs:

        # Message dans la console
        print("----------------Joueur créé----------------")  
        print(f"Nom: {nom}")  
        print(f"Email: {email}") 

    # Partie de connexion
    def soumettre_connexion_joueur(self): 
        nom = self.champ_nom_connexion.get()  
        email = self.champ_email_connexion.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_JOUEURS, self.nettoyer_nom_fichier(nom)) 

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
        if email_fichier != email:  # Email incorrect
            print(f"Email incorrect pour le joueur {nom}.") 
            return  

        print(f"Connexion réussie pour le joueur {nom}")  
        print(f"Email: {email}") 

        self.master.nom_joueur_connecte = nom  # Sauvegarder le joueur connecté
        # Log du joueur connecté
        self.ajouter_log(nom_fichier_joueur, "Le joueur s'est connecté.")  # Ajouter un log dans le fichier du joueur

    def ajouter_log(self, fichier_joueur, message_log):  # Ajouter log dans le fichier du joueur
        # Ouvrir fichier et ajouter (a pour append)
        with open(fichier_joueur, "a") as fichier: 
            fichier.write(f"{message_log}\n")  

        print(f"Log ajouté: {message_log}")  # Afficher un message dans la console pour confirmer l'ajout du log

    def nettoyer_nom_fichier(self, nom_fichier):  # Supprimer mauvais caractères
        return self.master.clean_filename(nom_fichier)
