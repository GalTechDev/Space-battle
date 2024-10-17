import GTLib as gt
import pygame as pg
import os
from Mechanics import ShowStats, AffectedByGravity

class Player(ShowStats, gt.Entites, AffectedByGravity):
    controls = {
        "PROFILE_1": {
            "UP":   {"key":pg.K_UP,     "active": False},
            "DOWN": {"key":pg.K_DOWN,   "active": False},
            "LEFT": {"key":pg.K_LEFT,   "active": False},
            "RIGHT":{"key":pg.K_RIGHT,  "active": False},
            "FIRE": {"key":pg.K_RCTRL,  "active": False}
        },
        
        "PROFILE_2": {
            "UP":   {"key":pg.K_z,      "active": False},
            "DOWN": {"key":pg.K_s,      "active": False},
            "LEFT": {"key":pg.K_q,      "active": False},
            "RIGHT":{"key":pg.K_d,      "active": False},
            "FIRE": {"key":pg.K_SPACE,  "active": False}
        }
    }
    
    def __init__(self, game, profile, position: tuple[int, int], size: tuple[int, int]):   
        super().__init__()  
        self.sprite = gt.Image(
            position=position,
            path = os.path.join("sprite", "ship.png")
        )
        self.sprite.mask((0, 0), (95, 95), (0,0), (95, 95))
        
        self.move_set = self.controls.get(profile)
        
        self.max_velocity: int = 6
        self.velocity_x: int = 0
        self.velocity_y: int = 0
        self.accel: float = 0.3
        
        self.friction: float = 1-0.1
        
        self.add_object(self.sprite)
        
        
        @self.event()
        def player_move(event):
            if event.type == pg.KEYDOWN:
                for info in self.move_set.values():
                    if event.key == info.get("key"):
                        info["active"] = True
            elif event.type == pg.KEYUP:
                for info in self.move_set.values():
                    if event.key == info.get("key"):
                        info["active"] = False
            
        @self.update()
        def update_position():
            friction = self.friction
            for move, info in self.move_set.items():
                if info.get("active"):
                    friction = 1
                    if move == "UP":
                        self.velocity_y -= self.accel
                    elif move == "DOWN":
                        self.velocity_y += self.accel
                    elif move == "LEFT":
                        self.velocity_x -= self.accel
                    elif move == "RIGHT":
                        self.velocity_x += self.accel
            
            if friction != 1:
                self.velocity_x *= friction if abs(self.velocity_x) > 0.1 else 0
                self.velocity_y *= friction if abs(self.velocity_y) > 0.1 else 0
            else:
                self.velocity_x = -self.max_velocity if self.velocity_x < -self.max_velocity else self.max_velocity if self.velocity_x > self.max_velocity else self.velocity_x
                self.velocity_y = -self.max_velocity if self.velocity_y < -self.max_velocity else self.max_velocity if self.velocity_y > self.max_velocity else self.velocity_y
                
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y
            
            if self.sprite.rect.x < 0:
                self.sprite.rect.x = 0
                self.velocity_x = 0
            elif self.sprite.rect.x+self.sprite.get_size()[0] > game.map_1.sprite.get_size()[0]:
                self.sprite.rect.x = game.map_1.sprite.get_size()[0]-self.sprite.get_size()[0]
                self.velocity_x = 0
                    
            if self.sprite.rect.y < 0:
                self.sprite.rect.y = 0
                self.velocity_y = 0
            elif self.sprite.rect.y+self.sprite.get_size()[1] > game.map_1.sprite.get_size()[1]:
                self.sprite.rect.y = game.map_1.sprite.get_size()[1]-self.sprite.get_size()[1]
                self.velocity_y = 0
