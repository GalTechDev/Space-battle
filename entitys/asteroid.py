import GTLib as gt
import pygame as pg
import random
import numpy as np


random.seed(1)


class Asteroid(gt.Entity):
    def __init__(self, app: gt.Base, game, x: int = None, y: int = None, size: int = None):
        super().__init__()

        self.app = app

        x: int = x if x is not None else random.randint(0, app.size[1])
        y: int = y if y is not None else random.randint(0, app.size[0])

        self.size: int = size if size is not None else random.randint(5, 15)
        self.masse: int = self.size**2

        self.sprite = gt.Square(
            position=(x, y),
            size=(self.size, self.size),
            color="red"

        )

        self.add_sprite(self.sprite)

        self.velocity_x: int = random.uniform(-2, 2)
        self.velocity_y: int = random.uniform(-2, 2)

    
        @self.update()
        def update_pos():
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y


    def update_velocity(self, planet):
        # Coordonnées de l'astéroïde
        asteroid_mid_size = self.sprite.get_size()[0]//2
        asteroid_x, asteroid_y = self.sprite.get_pos()
        asteroid_x += asteroid_mid_size
        asteroid_y += asteroid_mid_size

        # Coordonnées de la planète
        planet_mid_size = planet.sprite.get_size()[0]//2
        planet_x, planet_y = planet.sprite.get_pos()
        planet_x += planet_mid_size
        planet_y += planet_mid_size

        # Calcul du vecteur directionnel de la planète vers l'astéroïde
        direction_x = planet_x - asteroid_x
        direction_y = planet_y - asteroid_y

        # Calcul de la distance entre la planète et l'astéroïde
        distance = np.sqrt(direction_x**2 + direction_y**2)

        if distance == 0:
            return  # Evite la division par zéro

        # Normalisation du vecteur directionnel
        direction_x /= distance
        direction_y /= distance

        # Force d'attraction gravitationnelle (simple modèle, sans constante G pour simplifier)
        force = planet.masse / distance

        # Mise à jour de la vitesse de l'astéroïde en fonction de la force gravitationnelle
        self.velocity_x += direction_x * force / self.masse
        self.velocity_y += direction_y * force / self.masse


    def calc_dist(self, object):
        a_x, a_y = object.sprite.get_pos()
        a_mid_size = object.sprite.get_size()[0]//2
        p_x, p_y = self.sprite.get_pos()
        p_mid_size = self.sprite.get_size()[0]//2

        return np.sqrt((a_x+a_mid_size - p_x+p_mid_size)**2 + (a_y + a_mid_size - p_y)**2)