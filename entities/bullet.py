import GTLib as gt
import pygame as pg
from Mechanics import FollowCam

class Bullet(gt.Entites):
    def __init__(self, damage: int = 0) -> None:
        super().__init__()

        self.damage: int = damage

        self.velocity_y: int = 0
        self.velocity_x: int = 0

        self.sprite = gt.Sprite()