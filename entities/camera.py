import GTLib as gt
import numpy as np

class Camera(gt.Entites):
    def __init__(self, app: gt.Base, game, player: gt.Entites) -> None:
        super().__init__()
        
        self.object_mid_size = player.sprite.get_size()[0]//2

        self.sprite = gt.Square(
            position=(player.sprite.get_pos()[0]-app.size[0]//2+self.object_mid_size, player.sprite.get_pos()[1]-app.size[1]//2+self.object_mid_size),
            size=app.size,
            color="gray",
            alpha=0
        )
        
        
        self.mid_size_x = self.sprite.get_size()[0]//2
        self.mid_size_y = self.sprite.get_size()[1]//2

        self.add_object(self.sprite)

        @self.update()
        def follow_player():
            distance_to_border = 150
            
            object_x, object_y = player.sprite.get_pos()
            
            temp_x = (object_x+self.object_mid_size) - (self.sprite.rect.x+self.mid_size_x)
            temp_y = (object_y+self.object_mid_size) - (self.sprite.rect.y+self.mid_size_y)
            
            distance_x = abs(temp_x)
            distance_x_after = abs(temp_x + player.velocity_x)
            distance_y = abs(temp_y)
            distance_y_after = abs(temp_y + player.velocity_y)
            
            is_living_x = distance_x - distance_x_after < 0
            is_living_y = distance_y - distance_y_after < 0
            
            if distance_x > app.size[0]//2-distance_to_border and is_living_x:
                self.sprite.rect.x += player.velocity_x
                if self.sprite.rect.x < 0:
                    self.sprite.rect.x = 0
                elif self.sprite.rect.x+self.sprite.get_size()[0] > game.map_1.sprite.base_surface.get_size()[0]:
                    self.sprite.rect.x = game.map_1.sprite.base_surface.get_size()[0]-self.sprite.get_size()[0]
                    
            if distance_y > app.size[1]//2-distance_to_border and is_living_y:
                self.sprite.rect.y += player.velocity_y
                if self.sprite.rect.y < 0:
                    self.sprite.rect.y = 0
                elif self.sprite.rect.y+self.sprite.get_size()[1] > game.map_1.sprite.base_surface.get_size()[1]:
                    self.sprite.rect.y = game.map_1.sprite.base_surface.get_size()[1]-self.sprite.get_size()[1]