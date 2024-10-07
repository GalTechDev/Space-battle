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
        
        pg.draw.line(
            screen, 
            "pink", 
            (self.sprite.get_pos()[0]+self.sprite.get_size()[0]//2, self.sprite.get_pos()[1]+self.sprite.get_size()[1]//2),
            (self.sprite.get_pos()[0]+self.sprite.get_size()[0]//2+self.velocity_x*10, self.sprite.get_pos()[1]+self.sprite.get_size()[1]//2+self.velocity_y*10),
            2
        )