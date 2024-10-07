import GTLib as gt
import pygame as pg
import random
import os
from Mechanics import AffectedByGravity, ShowStats

random.seed(1)


class Asteroid(ShowStats, gt.Entites, AffectedByGravity):
    def __init__(self, app: gt.Base, game, x: int = None, y: int = None, size: int = None):
        super().__init__()
        self.app = app
        
        self.size: int = size if size is not None else random.randint(40, 50)

        zone = random.choice(range(4))
        if zone == 0: #zone en haut
            x: int = x if x is not None else random.uniform(-self.size, game.map_1.sprite.base_surface.get_size()[0])
            y: int = -self.size
        elif zone == 0: #zone en bas
            x: int = x if x is not None else random.uniform(-self.size, game.map_1.sprite.base_surface.get_size()[0])
            y: int = game.map_1.sprite.base_surface.get_size()[1]
        elif zone == 0: #zone a gauche
            x: int = -self.size
            y: int = y if y is not None else random.uniform(-self.size, game.map_1.sprite.base_surface.get_size()[1])
        else: #zone a droite
            x: int = game.map_1.sprite.base_surface.get_size()[0]
            y: int = y if y is not None else random.uniform(-self.size, game.map_1.sprite.base_surface.get_size()[1])
        
            
        self.masse: int = (self.size//3)**2

        self.sprite = gt.Square(
            position=(x, y),
            size=(self.size, self.size),
            color="red"
        )

        
        self.sprite = gt.Image(
            position=(x, y),
            path = os.path.join("sprite", "asteroid.png")
        )
        
        self.sprite.set_size((self.size, self.size))

        self.add_object(self.sprite)

        self.velocity_x: int = 0
        self.velocity_y: int = 0
    
        @self.update()
        def update_pos():
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y