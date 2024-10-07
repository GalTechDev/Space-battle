import GTLib as gt
import random
import os

class Map(gt.Entites):
    def __init__(self, app: gt.Base, game, camera_index: str,bg_image_path="") -> None:
        super().__init__()
        self.app = app
        self.game = game
        self.camera_index = camera_index
        self.camera = game.camera_ply_1 if camera_index == "1" else game.camera_ply_2
        
        self.sprite = SpaceMap(
            size = (5000, 5000),
            nb_stars = 6000
        )
        
        self.sprite.mask(
            position=(0 if camera_index == "1" else self.app.size[1],0),
            size=self.app.size,
            focus_pos=(-self.camera.sprite.get_pos()[0], -self.camera.sprite.get_pos()[1]),
            focus_size=self.app.size
        )
        
       #self.add_object(self.sprite)
            
            
    def draw(self, false_screen):
        self.sprite.mask(
            position=(0 if self.camera_index == "1" else self.app.size[1],0),
            size=self.app.size,
            focus_pos=(-self.camera.sprite.get_pos()[0], -self.camera.sprite.get_pos()[1]),
            focus_size=self.app.size
        )
        self.sprite.draw(self.app.screen)
            
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
        
        

                