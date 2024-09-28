import GTLib as gt
import pygame as pg
import random
import numpy as np

class Planet(gt.Entity):
    def __init__(self, app: gt.Base, game, x: int = None, y: int = None, size: int = 30) -> None:
        super().__init__()
        self.app = app
        self.game = game

        x: int = x if x is not None else random.randint(0, app.size[1])
        y: int = y if y is not None else random.randint(0, app.size[0])

        self.size: int = random.randint(30, 60)
        self.masse = self.size**2

        self.attraction = self.size * 3

        self.sprite = gt.Square(
            position=(x, y),
            size=(self.size, self.size),
            color="green"

        )

        self.add_sprite(self.sprite)

        @self.update()
        def get_asteroid_in_champ_action():
            for asteroid in self.game.asteroids:
                distance: float = self.calc_dist(asteroid)

                if distance <= self.attraction or True:
                    asteroid.update_velocity(self)

                if self.sprite.colliderect(asteroid.sprite):
                    try:
                        self.app.drop_menu(asteroid)
                    except Exception:
                        pass

        @self.event()
        def follow_mouse(events):
            if events.type == pg.MOUSEMOTION:
                self.sprite.set_pos((pg.mouse.get_pos()[0]-self.size//2, pg.mouse.get_pos()[1]-self.size//2))

    def calc_dist(self, object):
        a_x, a_y = object.sprite.get_pos()
        a_mid_size = object.sprite.get_size()[0]//2
        p_x, p_y = self.sprite.get_pos()
        p_mid_size = self.sprite.get_size()[0]//2

        return np.sqrt((a_x+a_mid_size - p_x+p_mid_size)**2 + (a_y + a_mid_size - p_y)**2)

                