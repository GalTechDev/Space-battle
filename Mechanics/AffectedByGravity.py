import numpy as np
import GTLib as gt

class AffectedByGravity:
    
    masse: int = 1
    sprite: gt.Sprite = None

    velocity_x: int = 0
    velocity_y: int = 0

    def update_velocity(self, object):
        # Coordonnées de l'astéroïde
        self_mid_size = self.sprite.get_size()[0]//2
        self_x, self_y = self.sprite.get_pos()
        self_x += self_mid_size
        self_y += self_mid_size

        # Coordonnées de la planète
        object_mid_size = object.sprite.get_size()[0]//2
        object_x, object_y = object.sprite.get_pos()
        object_x += object_mid_size
        object_y += object_mid_size

        # Calcul du vecteur directionnel de la planète vers l'astéroïde
        direction_x = object_x - self_x
        direction_y = object_y - self_y

        # Calcul de la distance entre la planète et l'astéroïde
        distance = np.sqrt(direction_x**2 + direction_y**2)

        if distance == 0:
            return  # Evite la division par zéro

        # Normalisation du vecteur directionnel
        direction_x /= distance
        direction_y /= distance

        # Force d'attraction gravitationnelle (simple modèle, sans constante G pour simplifier)
        force = object.masse / distance

        # Mise à jour de la vitesse de l'astéroïde en fonction de la force gravitationnelle
        vx: float = direction_x * force / self.masse
        vy: float = direction_y * force / self.masse

        self.velocity_x += vx
        self.velocity_y += vy

        return vx, vy
    
    def calc_dist(self, object):
        object_x, object_y = object.sprite.get_pos()
        object_mid_size = object.sprite.get_size()[0]//2
        self_x, self_y = self.sprite.get_pos()
        self_mid_size = self.sprite.get_size()[0]//2

        return np.sqrt((object_x+object_mid_size - self_x+self_mid_size)**2 + (object_y + object_mid_size - self_y)**2)