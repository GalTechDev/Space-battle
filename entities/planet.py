import GTLib as gt
import pygame as pg
import random
import os
from Mechanics import AffectedByGravity
from .asteroid import Asteroid
from .bullet import Bullet


class Planet(gt.Entites):
    def __init__(self, app: gt.Base, game, x: int = None, y: int = None, size: int = None) -> None:
        super().__init__()
        self.app = app
        self.game = game
        
        self.size: int = 165 #size if size is not None else random.randint(30, 60)

        x: int = x if x is not None else random.randint(0, game.map.sprite.get_size()[0]-self.size)
        y: int = y if y is not None else random.randint(0, game.map.sprite.get_size()[1]-self.size)

        self.masse = (self.size//3)**2

        self.attraction = self.size * 1

        self.sprite = gt.Image(
            position=(x, y),
            size=(self.size, self.size),
            path = os.path.join("sprite", "planet_1.png")
        )

        self.add_object(self.sprite)

        @self.update()
        def get_asteroid_in_champ_action():
            i=0
            while i < len(self.game.objects):
                object = self.game.objects[i]
                if isinstance(object, AffectedByGravity):
                    object.update_velocity(self)

                    if self.sprite.colliderect(object.sprite):
                        if isinstance(object, Asteroid):
                            try:
                                self.game.asteroids.remove(object)
                                self.game.remove_object(object)
                                continue
                            except Exception as error:
                                print(f"error on asteroid kill : {error} {i} {len(self.game.asteroids)}")
                                
                        elif isinstance(object, Bullet):
                            try:
                                self.game.asteroids.remove(object)
                                self.game.remove_object(object)
                                continue
                            except Exception as error:
                                print(f"error on bullet kill : {error} {i} {len(self.game.bullets)}")
                i+=1

        #@self.event()
        def follow_mouse(events: pg.event.Event):
            if events.type == pg.MOUSEMOTION:
                self.sprite.set_pos((pg.mouse.get_pos()[0]-self.size//2, pg.mouse.get_pos()[1]-self.size//2))

                