import numpy as np  # Importation de NumPy pour les calculs mathématiques

class Joueur:  # Définition de la classe Joueur
    def __init__(self, accueil, obstacles):
        self.accueil = accueil  # Référence à l'interface d'accueil
        self.obstacles = self.accueil.get_obstacles() # Reference aux obstacles
        self.reference = (0, 0) # Reference au dernier point etant ete cree, sert a ne pas cree un point sur le dernier point cree
        self.joueur_position = self.generer_position_valide_point()  # Position valide pour le joueur
        self.cible_position = self.generer_position_valide_point()  # Position valide pour la cible

    def generer_position_valide_point(self):  # Méthode pour générer la position du joueur, retourne un position valide
        while True:  # Boucle infinie jusqu'à obtenir une position valide
            xpoint = np.random.randint(0, 340)  # Génération d'un x aléatoire
            ypoint = np.random.randint(0, 180) # Génération d'un y aléatoire
            is_valide = True # Création d'une variable pour vérifier si le point est valide
            for (xobstacle, yobstacle, robstacle) in self.obstacles: # Pour chaque obstacle
                odistance = np.sqrt((xpoint-xobstacle)**2 + (ypoint - yobstacle)**2) # On calcul la distance entre le point et l'obstacle
                if odistance < (robstacle + 10): # Si la distance est plus petit que le rayon de l'obstacle et que le rayon du point
                    is_valide = False # Le point n'est pas valide
                pdistance = np.sqrt((xpoint-self.reference[0])**2 + (ypoint - self.reference[1])**2) # On calcul la distance entre le point et le point de reference
                if pdistance < 10: # Si le point n'est pas asse eloigne du point de reference
                    is_valide = False # Le point n'est pas valide
            if is_valide : # Si le point est valide
                self.reference = (xpoint, ypoint) # Le point de reference devient le point
                return (xpoint, ypoint) # On le retourne
            