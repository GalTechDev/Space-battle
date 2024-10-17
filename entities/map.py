import GTLib as gt
import random
import pygame as pg

class Map(gt.Entites):
    def __init__(self, app: gt.Base, game) -> None:
        super().__init__()
        self.app = app
        self.game = game
        
        self.sprite = SpaceMap(
            size = (5000, 5000),
            nb_stars = 6000
        )
        
        self.add_object(self.sprite)
        
    def draw(self, screen: pg.Surface, camera):
        self.sprite.mask(
            position=(0, 0),
            size=self.app.size,
            focus_pos=(-camera.sprite.get_pos()[0], -camera.sprite.get_pos()[1]),
            focus_size=self.app.size
        )
        
        screen.blit(self.sprite.surface, camera.sprite.get_pos())
            
            
class SpaceMap(gt.Square):
    def __init__(self, size: tuple[int, int], nb_stars):
        super().__init__((0,0), size)
        for _ in range(nb_stars):
            x = random.randint(0, size[0])
            y = random.randint(0, size [1])
            
            star = gt.Square(
                position=(x, y),
                size = [random.randint(1, 3)]*2,
                rotation = random.choice([0, 45]),
                alpha = random.randint(50, 255),
                color ="white"
            )
            star.blit(self.surface, star.surface)
        
        

                