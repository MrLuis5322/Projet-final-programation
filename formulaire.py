import customtkinter as ctk
import tkinter as tk

class Formulaire(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Nom
        self.name_label = ctk.CTkLabel(self, text="Nom:")
        self.name_label.pack(padx=20, pady=(20, 10), anchor="w")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Entrez votre nom")
        self.name_entry.pack(padx=20, pady=(20, 10), fill="x")

        # Email
        self.email_label = ctk.CTkLabel(self, text="Email:")
        self.email_label.pack(padx=20, pady=(10, 10), anchor="w")
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Entrez votre email")
        self.email_entry.pack(padx=20, pady=(10, 10), fill="x")

    

        # Message
        self.message_label = ctk.CTkLabel(self, text="Message:")
        self.message_label.pack(padx=20, pady=(10, 10), anchor="nw")
        self.message_text = tk.Text(self, height=5, width=30)
        self.message_text.pack(padx=20, pady=(10, 10), fill="x")

        # Bouton de soumission
        self.submit_button = ctk.CTkButton(self, text="Soumettre", command=self.submit_form)
        self.submit_button.pack(padx=20, pady=20)

    def submit_form(self):
        print("----------------Joueur cree----------------")
        print("Nom:", self.name_entry.get())
        print("Email:", self.email_entry.get())
        print("Message:", self.message_text.get("1.0", tk.END))

