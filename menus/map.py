import GTLib as gt
import pygame as pg
import os

class Map(gt.Menu):
    def __init__(self, app: gt.Base, game, bg_image_path="") -> None:
        super().__init__()
        self.app = app
        
        self.sprite2 = gt.Image(
            position=(0,0),
            path= os.path.join("sprite", "map_bg.png"),
            alpha=255
        )
        
        self.sprite = gt.Square(
            position=(0,0),
            size = app.size,
            color="pink",
            alpha=255
        )
        self.sprite.base_surface = self.sprite2.base_surface
        
        self.add_object(self.sprite)
        
        @self.update()
        def update_bg():
            self.sprite.mask(
                size=app.size,
                focus_pos=(-game.camera.sprite.get_pos()[0], -game.camera.sprite.get_pos()[1]),
                focus_size=app.size
            )
            self.sprite.set_pos((0, 0))
            
    def draw(self, false_screen):
        self.sprite.draw(self.app.screen)
            

                