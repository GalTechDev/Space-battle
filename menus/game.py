import GTLib as gt
import pygame as pg

from entities import *
from .pause import Pause

class Game(gt.Menu):
    def __init__(self, app: gt.Advanced) -> None:
        super().__init__()
        self.app: gt.Advanced = app

        self.plannets: list = []
        self.asteroids: list = []
        self.bullets: list = []
        
        self.nb_asteroids = 20
        
        self.player1: Player = Player(self, profile="PROFILE_1", position=(self.app.size[0]//2-5, self.app.size[1]//2-5), size=(10,10))
        self.camera_ply_1 = Camera(app, self, self.player1)
        
        self.player2: Player = Player(self, profile="PROFILE_2", position=(self.app.size[0]//2-5, self.app.size[1]//2-5), size=(10,10))
        self.camera_ply_2 = Camera(app, self, self.player2)
        
        self.map: Map = Map(app, self)
        
        self.screen_ply_1 = pg.Surface(app.size, pg.SRCALPHA, 32)
        self.screen_ply_2 = pg.Surface(app.size, pg.SRCALPHA, 32)
        
        self.canvas_ply = pg.Surface(self.map.sprite.get_size())
        print(self.canvas_ply.get_size())
        self.rect_ply_1 = self.canvas_ply.get_rect()
        self.rect_ply_2 = self.canvas_ply.get_rect()
        

        self.add_object(self.player1)
        self.add_object(self.player2)
        
        
        @self.event()
        def pause_game(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_ESCAPE:
                    app.call_menu(Pause(app, self))

                    app.drop_menu(self)
                  
        @self.event()
        def k_add_planet(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_p:
                    self.add_planet()

        @self.event()
        def k_add_asteroid(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_a:
                    self.add_asteroid()
                    
        
        @self.update()
        def manage_asteroid():
            while len(self.asteroids) < self.nb_asteroids:
                self.add_asteroid()
                
        @self.update()
        def update_cam():
            self.camera_ply_1.update()
            self.camera_ply_2.update()

    def add_planet(self, x: int = None, y: int = None, size: int = None):
        self.plannets.append(Planet(self.app, self, x, y, size))
        self.add_object(self.plannets[-1])

    def add_asteroid(self, x: int = None, y: int = None, size: int = None):
        self.asteroids.append(Asteroid(self.app, self, x, y, size))
        self.add_object(self.asteroids[-1])

    def draw(self, screen: pg.Surface):      
        
        canvas_ply_1 = canvas_ply_2 = self.canvas_ply.copy()
        
        self.map.draw(canvas_ply_1, self.camera_ply_1)
        self.map.draw(canvas_ply_2, self.camera_ply_2)
        
        for object in self.objects:
            object.draw(canvas_ply_1)
            object.draw(canvas_ply_2)
            
        self.camera_ply_1.draw(canvas_ply_1)
        self.camera_ply_2.draw(canvas_ply_2)

        self.rect_ply_1.x = -self.camera_ply_1.sprite.rect.x
        self.rect_ply_1.y = -self.camera_ply_1.sprite.rect.y
        
        self.rect_ply_2.x = -self.camera_ply_2.sprite.rect.x 
        self.rect_ply_2.y = -self.camera_ply_2.sprite.rect.y
        
        
        self.screen_ply_1.blit(canvas_ply_1, self.rect_ply_1)
        self.screen_ply_2.blit(canvas_ply_2, self.rect_ply_2)
        
        screen.blit(self.screen_ply_1, (0, 0))
        screen.blit(self.screen_ply_2, (self.app.size[0], 0))
