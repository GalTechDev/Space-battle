import GTLib as gt
import pygame as pg
import random
import numpy as np
from Mechanics import AffectedByGravity

random.seed(1)


class Asteroid(gt.Entites, AffectedByGravity):
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

        self.add_object(self.sprite)

        self.velocity_x: int = random.uniform(-2, 2)
        self.velocity_y: int = random.uniform(-2, 2)

    
        @self.update()
        def update_pos():
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y