import GTLib as gt
import pygame as pg
from Mechanics import AffectedByGravity
from .asteroid import Asteroid

class Bullet(gt.Entites, AffectedByGravity):
    def __init__(self, game, player, damage: int = 0) -> None:
        super().__init__()

        self.damage: int = damage

        self.velocity_y: int = 0
        self.velocity_x: int = 0

        self.sprite = gt.Square(
            position=(),
            size=(),
        )
        
        @self.update()
        def bullet_collide():
            for object in game.object:
                if self.sprite.colliderect(object):
                    if isinstance(object, Asteroid):
                        pass
                    elif isinstance(object, type(player)):
                        pass
                    
        @self.update()
        def update_pos():
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y