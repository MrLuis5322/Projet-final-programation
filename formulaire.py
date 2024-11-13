import customtkinter as ctk  
import tkinter as tk  
import os  # os pour manipuler fichier sur windows https://www.geeksforgeeks.org/os-module-python-examples/

class Formulaire(ctk.CTkFrame):  
    def __init__(self, maitre=None):  
        self.DOSSIER_JOUEURS = os.path.join(os.path.dirname(__file__), "accounts") # code trouvé sur internet pour faire instence aux fichiers dans accounts
        super().__init__(maitre)  
        self.creer_widgets()

    def creer_widgets(self):
        self.onglets = ctk.CTkTabview(master = self)  
        self.onglets.place(x=750, 
                           y=750,
                           relheight = 1,
                           relwidth = 1)

        # Partie créer joueur
        self.onglets.add("Créer un Joueur")
        self.formulaire_creation_joueur = ctk.CTkFrame(self.onglets.tab("Créer un Joueur"))  
        self.formulaire_creation_joueur.place(x = 0,
                                              y = 0,)

        self.label_nom_creation = ctk.CTkLabel(self.formulaire_creation_joueur, text="Nom:")
        self.label_nom_creation.place(x = 10,
                                      y = 10)
        
        self.champ_nom_creation = ctk.CTkEntry(self.formulaire_creation_joueur, placeholder_text="Entrez votre nom")  
        self.champ_nom_creation.place(x = 10,
                                      y = 10)

        self.label_email_creation = ctk.CTkLabel(self.formulaire_creation_joueur, text="Email:")  
        self.label_email_creation.place(x = 10,
                                        y = 10)  
        
        self.champ_email_creation = ctk.CTkEntry(self.formulaire_creation_joueur, placeholder_text="Entrez votre email")  
        self.champ_email_creation.place(x = 10,
                                        y = 10)  

        self.bouton_creation_joueur = ctk.CTkButton(self.formulaire_creation_joueur, text="Créer Joueur", command=self.soumettre_creation_joueur) #bouton soumettre
        self.bouton_creation_joueur.place(x = 10,
                                          y = 10)  

        # Partie conection
        self.onglets.add("Se connecter")  
        self.formulaire_connexion_joueur = ctk.CTkFrame(self.onglets.tab("Se connecter"))  
        self.formulaire_connexion_joueur.place(fill="both", 
                                               expand=True)  

        self.label_nom_connexion = ctk.CTkLabel(self.formulaire_connexion_joueur, text="Nom:")  
        self.label_nom_connexion.place(x = 10,
                                       y = 10)  
        
        self.champ_nom_connexion = ctk.CTkEntry(self.formulaire_connexion_joueur, placeholder_text="Entrez votre nom")  
        self.champ_nom_connexion.place(x = 10,
                                       y = 10)  

     
        self.label_email_connexion = ctk.CTkLabel(self.formulaire_connexion_joueur, text="Email:")  # Créer un label pour l'email
        self.label_email_connexion.place(x = 10,
                                         y = 10)  # Ajouter le label pour l'email
        
        self.champ_email_connexion = ctk.CTkEntry(self.formulaire_connexion_joueur, placeholder_text="Entrez votre email")  # Champ de saisie pour l'email
        self.champ_email_connexion.place(x = 10,
                                         y = 10)  # Ajouter le champ de texte pour l'email

        # Bouton soumettre partie conection
        self.bouton_connexion_joueur = ctk.CTkButton(self.formulaire_connexion_joueur, text="Se connecter", command=self.soumettre_connexion_joueur) 
        self.bouton_connexion_joueur.place(x = 10,
                                           y = 10) 

    def soumettre_creation_joueur(self): 
        # Récupérer les noms et email
        nom = self.champ_nom_creation.get()  
        email = self.champ_email_creation.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_JOUEURS, self.nettoyer_nom_fichier(nom))

        # Fichier existe déjà?
        if os.path.exists(nom_fichier_joueur): 
            print(f"Le joueur {nom} a deja ete cree.")  
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

    # Partie de conexion
    def soumettre_connexion_joueur(self): 
        nom = self.champ_nom_connexion.get()  
        email = self.champ_email_connexion.get() 

        nom_fichier_joueur = os.path.join(self.DOSSIER_JOUEURS, self.nettoyer_nom_fichier(nom)) 

        # Vérifier si le joueur existe
        # si il existe pas alors erreur
        if not os.path.exists(nom_fichier_joueur):  
            print(f"Joueur {nom} non trouvé.")  
            return  

        # Lecture (j'utilise le with pour que le fichier soit fermé après)
        with open(nom_fichier_joueur, "r") as fichierL:  # Ouvrir fichie lecture (r pour read)
            lignes = fichierL.readlines()  # Lire lignes
            email_fichier = lignes[1].strip().split(": ")[1]  # Extraire l'email du fichier (1 pour ligne 2)

        # Email
        if email_fichier != email:  # Email mauvais
            print(f"Email incorrect pour le joueur {nom}.") 
            return  

        print(f"Connexion réussie pour le joueur {nom}")  
        print(f"Email: {email}") 

        self.master.nom_joueur_connecte = nom  # Sauvegarder joueur conecté
        # log joueur conecté
        self.ajouter_log(nom_fichier_joueur, "Le joueur s'est connecte.")  # Ajouter un log dans le fichier du joueur

    def ajouter_log(self, fichier_joueur, message_log):  # Ajouter log dans joueur
        # Ouvrir fichier et ajouter (a pour append)
        with open(fichier_joueur, "a") as fichier: 
            fichier.write(f"{message_log}\n")  

        print(f"Log ajouté: {message_log}")  # Afficher un message dans la console pour confirmer l'ajout du log

    def nettoyer_nom_fichier(self, nom_fichier):  # Supprimer mauvais caractères
       
       return self.master.clean_filename(nom_fichier)

