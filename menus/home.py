import GTLib as gt
import pygame as pg
import pygame.freetype as ft

class Home(gt.Menu):
    def __init__(self, app: gt.Base) -> None:
        super().__init__()

        # addition

        def add_image(position: list = (0, 0), path: str = "") -> gt.Image:
            gt_image = gt.Image(
                position=position,
                path = path        
            )
            
            gt_image.set_pos(
                (app.size[0]//2, app.size[1]//2),
                (gt_image.get_size()[0]//2, (gt_image.get_size()[1]//2) - position[1])
            )
            
            self.add_object(gt_image)
            
            return gt_image

        self.menu: gt.Image = add_image(position=(0, 0), path="sprite/menu_sprite.png")
        self.menu.mask(
            (0, 0), 
            (100, 20),
            (0, 0), 
            (100, 20)
        )
        self.option1 = add_image(position=(0, self.menu.get_size()[1]+30), path="sprite/menu_sprite.png")
        self.option1.mask(
            (0, 0), 
            (100, 20),
            (0, 0), 
            (100, 20)
        )
        self.option2 = add_image(position=(0, self.menu.get_size()[1]+self.option1.get_size()[1]+30*2), path="sprite/menu_sprite.png")       
        self.option2.mask(
            (0, 0), 
            (100, 20),
            (0, 0), 
            (100, 20)
        )

        @self.event()
        def start_game(events):
            pass
