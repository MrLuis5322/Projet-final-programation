import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, parent, game):
        super().__init__(parent)
        self.game = game
        self.pack(fill=tk.BOTH, expand=True)

        # Bouton pour accéder à l'accueil (Jouer)
        btn_play = tk.Button(self, text="Jouer", command=self.game.show_accueil)
        btn_play.pack(pady=10)

        # Bouton pour se connecter
        btn_login = tk.Button(self, text="Se connecter", command=self.game.show_formulaire)
        btn_login.pack(pady=10)

        # Bouton pour quitter le jeu
        btn_quit = tk.Button(self, text="Quitter", command=self.game.quit_game)
        btn_quit.pack(pady=10)
