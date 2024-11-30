import numpy as np

class Joueur:
    def __init__(self, parent, obstacles):
        self.parent = parent  # Référence à l'interface la classe Game pour avoir accès aux obstacles
        self.obstacles = self.parent.obstacles # Sert à éviter une génération du joueur sur l'obstacle
        self.reference = (0, 0) # Sert à ne pas créer un point sur le dernier point créé
        self.joueur_position = self.generer_position_valide_point()  # Sert à générer un point valide pour le joueur
        self.cible_position = self.generer_position_valide_point()  # Sert à générer un point valide pour la cible

    def generer_position_valide_point(self):  # Trouve un point valide
        while True:  # Tant que le point est sur une position invalide, on refais les opérations
            xpoint = np.random.randint(0, 340) 
            ypoint = np.random.randint(0, 180)
            is_valide = True
            for (xobstacle, yobstacle, robstacle) in self.obstacles:
                odistance = np.sqrt((xpoint-xobstacle)**2 + (ypoint - yobstacle)**2) # Sert à trouver la distance entre le point et l'obstacle
                if odistance < (robstacle + 10): # Sert à vérifier que le point est plus loin que le rayon de l'obstacle
                    is_valide = False
                pdistance = np.sqrt((xpoint-self.reference[0])**2 + (ypoint - self.reference[1])**2)
                if pdistance < 10: # Sert à vérifier si le point est assez loin du point de référence
                    is_valide = False
            if is_valide :
                self.reference = (xpoint, ypoint) # On change le pont de référence si le nouveau point est valide
                return (xpoint, ypoint)