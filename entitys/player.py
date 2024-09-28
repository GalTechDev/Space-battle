import GTLib as gt
import pygame as pg

class Player(gt.Entity):
    controls = {
        "PROFILE_1": {
            "UP":   {"key":pg.K_UP,     "active": False},
            "DOWN": {"key":pg.K_DOWN,   "active": False},
            "LEFT": {"key":pg.K_LEFT,   "active": False},
            "RIGHT":{"key":pg.K_RIGHT,  "active": False}
        },
        
        "PROFILE_2": {
            "UP":   {"key":pg.K_z,      "active": False},
            "DOWN": {"key":pg.K_s,      "active": False},
            "LEFT": {"key":pg.K_q,      "active": False},
            "RIGHT":{"key":pg.K_d,      "active": False}
        }
    }
    
    def __init__(self, profile, position: tuple[int, int], size: tuple[int, int]):   
        super().__init__()  
        self.sprite = gt.UI.Square(position=position, size=size, color="blue")
        self.move_set = self.controls.get(profile)
        
        self.max_velocity: int = 3
        self.velocity_x: int = 0
        self.velocity_y: int = 0
        self.accel: float = 0.1
        
        self.friction: float = 1-0.1
        
        self.add_sprite(self.sprite)
        
        
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
                        self.velocity_y -=self.accel
                    elif move == "DOWN":
                        self.velocity_y +=self.accel
                    elif move == "LEFT":
                        self.velocity_x -=self.accel
                    elif move == "RIGHT":
                        self.velocity_x +=self.accel
            
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y
            
            if friction != 1:
                self.velocity_x *= friction if abs(self.velocity_x) > 0.1 else 0
                self.velocity_y *= friction if abs(self.velocity_y) > 0.1 else 0
            else:
                self.velocity_x = -self.max_velocity if self.velocity_x < -self.max_velocity else self.max_velocity if self.velocity_x > self.max_velocity else self.velocity_x
                self.velocity_y = -self.max_velocity if self.velocity_y < -self.max_velocity else self.max_velocity if self.velocity_y > self.max_velocity else self.velocity_y
                
            self.sprite.rect.x += self.velocity_x
            self.sprite.rect.y += self.velocity_y
