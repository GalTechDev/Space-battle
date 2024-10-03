import GTLib as gt
import pygame as pg
import os

class Map(gt.Entites):
    def __init__(self, app: gt.Base, game, bg_image_path="") -> None:
        super().__init__()
        self.app = app
        self.game =game
        
        self.sprite = gt.Image(
            position=(0,0),
            path= os.path.join("sprite", "map_bg.png"),
            alpha=255
        )
        
       #self.add_object(self.sprite)
            
            
    def draw(self, false_screen):
        self.sprite.mask(
            size=self.app.size,
            focus_pos=(-self.game.camera.sprite.get_pos()[0], -self.game.camera.sprite.get_pos()[1]),
            focus_size=self.app.size
        )
        self.sprite.draw(self.app.screen)
            

                