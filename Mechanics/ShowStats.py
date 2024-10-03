import GTLib as gt
import pygame as pg

class ShowStats:
    
    masse: int = 1
    sprite: gt.Sprite = None

    velocity_x: int = 0
    velocity_y: int = 0
    
    def draw(self, screen: pg.Surface):
        for object in self.objects:
            object.draw(screen)
        print("h")
        pg.draw.line(
            screen, 
            "pink", 
            (self.sprite.get_size()[0]+self.sprite.get_size()[0], self.sprite.get_size()[1]+self.sprite.get_size()[1]),
            (self.sprite.get_size()[0]+self.sprite.get_size()[0]+self.velocity_x, self.sprite.get_size()[1]+self.sprite.get_size()[1]+self.velocity_y)
        )