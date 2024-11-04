import numpy as np  # Importation de NumPy pour les calculs mathématiques

class Joueur:  # Définition de la classe Joueur
    def __init__(self, accueil, obstacles):  
        self.accueil = accueil  # Référence à l'interface d'accueil
        self.obstacles = self.accueil.get_obstacles()
        # self.obstacles_instance = Obstcales() # Créer une instance de la classe Obstacles
        # self.obstacles = self.obstacles_instance.generer_obstacles()  # Génération des obstacles

        self.joueur_position = self.generer_position_valide_point()  # Position valide pour le joueur
        self.cible_position = self.generer_position_valide_point()  # Position valide pour la cible

    def generer_position_valide_point(self):  # Méthode pour générer la position du joueur, retourne un position valide
        while True:  # Boucle infinie jusqu'à obtenir une position valide
            xpoint = np.random.randint(-170, 170)  # Génération d'un x aléatoire
            ypoint = np.random.randint(-90, 90) # Génération d'un y aléatoire
            is_valide = True
            for (xobstacle, yobstacle, robstacle) in self.obstacles: # Pour chaque obstacle
                distance = np.sqrt((xpoint-xobstacle)**2 + (ypoint - yobstacle)**2) # On calcul la distance entre le point et l'obstacle
                if distance < (robstacle + 10):
                    is_valide = False
            if is_valide : return (xpoint, ypoint)
            