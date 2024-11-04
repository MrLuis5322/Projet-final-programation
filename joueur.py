import numpy as np  # Importation de NumPy pour les calculs mathématiques

class Joueur:  # Définition de la classe Joueur
    def __init__(self, accueil, obstacles):  
        self.accueil = accueil  # Référence à l'interface d'accueil
        self.obstacles = self.accueil.get_obstacles()
        # self.obstacles_instance = Obstcales() # Créer une instance de la classe Obstacles
        # self.obstacles = self.obstacles_instance.generer_obstacles()  # Génération des obstacles

        self.joueur_position = self.generer_position_valide_joueur()  # Position valide pour le joueur
        self.cible_position = self.generer_position_valide_cible()  # Position valide pour la cible

    def generer_position_valide_joueur(self):  # Méthode pour générer la position du joueur
        """ Retourne une position valide pour le joueur. """
        while True:  # Boucle infinie jusqu'à obtenir une position valide
            joueur = self.generer_point_aleatoire(negatif=True)  # Génération d'un point aléatoire dans le domaine négatif
            if not self.est_point_sur_obstacle(joueur):  # Vérification si le point n'est pas sur un obstacle
                return joueur  # Retourne la position valide

    def generer_position_valide_cible(self):  # Méthode pour générer la position de la cible
        """ Retourne une position valide pour la cible. """
        while True:  # Boucle infinie jusqu'à obtenir une position valide
            cible = self.generer_point_aleatoire(negatif=False)  # Génération d'un point aléatoire dans le domaine positif
            if not self.est_point_sur_obstacle(cible):  # Vérification si le point n'est pas sur un obstacle
                return cible  # Retourne la position valide

    def generer_point_aleatoire(self, negatif=True):  # Méthode pour générer un point aléatoire
        """ Génère un point aléatoire avec des coordonnées négatives ou positives. """
        if negatif:  # Si le point est pour le joueur
            return (np.random.uniform(-100, 0), np.random.uniform(-100, 0))  # Coordonnées négatives
        else:  # Si le point est pour la cible
            return (np.random.uniform(0, 100), np.random.uniform(0, 100))  # Coordonnées positives

    def est_point_sur_obstacle(self, point):  # Méthode pour vérifier si un point est sur un obstacle
        """ Vérifie si un point donné se trouve à l'intérieur d'un obstacle. """
        px, py = point  # Décomposition des coordonnées du point
        for (ox, oy, r) in self.obstacles:  # Itération sur les obstacles
            distance = np.sqrt((px - ox)**2 + (py - oy)**2)  # Calcul de la distance entre le point et l'obstacle
            if distance < r:  # Si le point est à l'intérieur de l'obstacle
                return True  # Retourne vrai
        return False  # Retourne faux si le point n'est pas sur un obstacle
