import GTLib as gt
import numpy as np


class Camera(gt.Entites):
    def __init__(self, player: gt.Entites) -> None:
        super().__init__()

        self.sprite = gt.Square(
            position=(0,0),
            size=(900, 700),
            color="gray",
            alpha=0
        )

        self.add_object(self.sprite)

        @self.update()
        def follow_player():
            object_x, object_y = player.sprite.get_pos()
            object_mid_size = player.sprite.get_size()[0]//2
            self_mid_size_x = self.sprite.get_size()[0]//2
            self_mid_size_y = self.sprite.get_size()[1]//2

            distance_x = abs((object_x+object_mid_size) - (self.sprite.rect.x+self_mid_size_x))
            distance_y = abs((object_y+object_mid_size) - (self.sprite.rect.y+self_mid_size_y))
            #print(distance)
            if distance_x > 250 and True:
                self.sprite.rect.x += player.velocity_x
            if distance_y > 250 and True:
                self.sprite.rect.y += player.velocity_y
                
                """self.sprite.rect.x = (object_x-self_mid_size_x+object_mid_size) 
                self.sprite.rect.y = (object_y-self_mid_size_y+object_mid_size)"""