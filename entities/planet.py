import GTLib as gt
import pygame as pg
import random
import numpy as np
from .asteroid import Asteroid


class Planet(gt.Entites):
    def __init__(self, app: gt.Base, game, x: int = None, y: int = None, size: int = None) -> None:
        super().__init__()
        self.app = app
        self.game = game
        
        self.size: int = size if size is not None else random.randint(30, 60)

        x: int = x if x is not None else random.randint(0, game.map.sprite.get_size()[1]-self.size)
        y: int = y if y is not None else random.randint(0, game.map.sprite.get_size()[0]-self.size)

        self.masse = (self.size//2)**2

        self.attraction = self.size * 3

        self.sprite = gt.Square(
            position=(x, y),
            size=(self.size, self.size),
            color="green"
        )

        self.add_object(self.sprite)

        @self.update()
        def get_asteroid_in_champ_action():
            for asteroid in self.game.asteroids:
                asteroid: Asteroid
                asteroid.update_velocity(self)

                if self.sprite.colliderect(asteroid.sprite):
                    try:
                        self.game.remove_object(asteroid)
                    except Exception:
                        pass

        #@self.event()
        def follow_mouse(events: pg.event.Event):
            if events.type == pg.MOUSEMOTION:
                self.sprite.set_pos((pg.mouse.get_pos()[0]-self.size//2, pg.mouse.get_pos()[1]-self.size//2))

                