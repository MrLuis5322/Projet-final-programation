import tkinter as tk
import customtkinter as ctk  
import pywinstyles

class Settings(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.pres = 1
        self.cres = 1
        self.lres = 1

        self.configure(width = 1000,
                       height = 1000,
                       bg = 'gray14')

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight = 1, minsize = 150, uniform = 'a') # Vertical 
        self.columnconfigure(0, weight = 1, minsize = 700, uniform = 'a') # Horizontal

        pywinstyles.set_opacity(self, value = 0.95, color="#000001") # Permet de gérer l'opacité du widget

        self.create_widgets()
    
    def create_widgets(self):
        self.warning = ctk.CTkLabel(master = self, 
                                      text="",
                                      width = 200,
                                      height = 50,
                                      fg_color= 'transparent',
                                      text_color = 'gold',
                                      font = ('Helvetica', 30))
        self.pres_label = ctk.CTkLabel(master = self, 
                                      text="Player resolution: ",
                                      width = 200,
                                      height = 50,
                                      fg_color= 'transparent',
                                      text_color = 'gold',
                                      font = ('Helvetica', 30))
        self.pres_champ = ctk.CTkEntry(master = self, 
                                       placeholder_text="Player resolution",
                                       width = 200,
                                       height = 50,
                                       corner_radius = 75,
                                       font = ('Helvetica', 20))
        self.cres_label = ctk.CTkLabel(master = self, 
                                      text="Target resolution: ",
                                      width = 200,
                                      height = 50,
                                      fg_color= 'transparent',
                                      text_color = 'gold',
                                      font = ('Helvetica', 30))
        self.cres_champ = ctk.CTkEntry(master = self, 
                                       placeholder_text="Target resolution",
                                       width = 200,
                                       height = 50,
                                       corner_radius = 75,
                                       font = ('Helvetica', 20))
        self.lres_label = ctk.CTkLabel(master = self, 
                                       text="Legend resolution: ",
                                       width = 200,
                                       height = 50,
                                       fg_color= 'transparent',
                                       text_color = 'gold',
                                       font = ('Helvetica', 30))
        self.lres_champ = ctk.CTkEntry(master = self, 
                                       placeholder_text="Legend resolution",
                                       width = 200,
                                       height = 50,
                                       corner_radius = 75,
                                       font = ('Helvetica', 20))
        self.bouton_retour = ctk.CTkButton(master = self,
                                           text="Retour", 
                                           command = lambda:self.parent.changeWindow(0, 2),
                                           width = 200, 
                                           height = 50, 
                                           border_width = 0, 
                                           corner_radius = 75,
                                           font = ('Helvetica', 20),
                                           text_color='gray14',
                                           hover_color = 'gold3',
                                           fg_color = 'gold')
        self.bouton_update = ctk.CTkButton(master = self,
                                           text="Update", 
                                           command = self.update,
                                           width = 200, 
                                           height = 50, 
                                           border_width = 0, 
                                           corner_radius = 75,
                                           font = ('Helvetica', 20),
                                           text_color='gray14',
                                           hover_color = 'gold3',
                                           fg_color = 'gold')

    def layout_widgets(self):
        self.warning.grid(row = 0, column = 0)
        self.pres_label.grid(row = 1, column = 0)
        self.cres_label.grid(row = 3, column = 0)
        self.lres_label.grid(row = 5, column = 0)
        self.pres_champ.grid(row = 2, column = 0)
        self.cres_champ.grid(row = 4, column = 0)
        self.lres_champ.grid(row = 6, column = 0)
        self.bouton_update.grid(row = 7, column = 0)
        self.bouton_retour.grid(row = 8, column = 0)
    
    def update(self):
        #if self.pres_champ.get() is not 0 and self.cres_champ.get() is not 0 and self.lres_champ.get() is not 0:
        if self.pres_champ.get() == '' or self.cres_champ.get() == '' or self.lres_champ.get() == '' or self.pres_champ.get() == '0' or self.cres_champ.get() == '0' or self.lres_champ.get() == '0':
            self.warning.configure(text = "La valeur 0 n'est pas permise")
        elif self.pres_champ.get() > '5' or self.cres_champ.get() > '5' or self.lres_champ.get() > '5':
            self.warning.configure(text = "La valeur ne peut pas dépasser 5")
        else:
            p = float(self.pres_champ.get())
            c = float(self.cres_champ.get())
            l = float(self.lres_champ.get())
            self.pres = p 
            self.cres = c
            self.lres = l
            self.warning.configure(text = 'Les réglages sont mis à jour')