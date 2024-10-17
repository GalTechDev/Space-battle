import GTLib as gt
import pygame as pg

from entities import *
from .pause import Pause

import os

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
        
        self.map_1: Map = Map(app, self, "1")
        self.map_2: Map = Map(app, self, "2")
        
        self.screen_ply_1 = pg.Surface(app.size, pg.SRCALPHA, 32)
        self.screen_ply_2 = pg.Surface(app.size, pg.SRCALPHA, 32)
        
        self.canvas_ply_1 = pg.Surface(self.map_1.sprite.get_size(), pg.SRCALPHA, 32)
        self.canvas_ply_2 = pg.Surface(self.map_2.sprite.get_size(), pg.SRCALPHA, 32)
        
        self.rect_ply_1 = self.canvas_ply_1.get_rect()
        self.rect_ply_2 = self.canvas_ply_2.get_rect()
        
        self.add_object(self.map_1)
        self.add_object(self.map_2)
        self.add_object(self.camera_ply_1)
        self.add_object(self.player1)
        self.add_object(self.camera_ply_2)
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
                
            """for i, asteroid in enumerate(self.asteroids):
                if not all(
                    (asteroid.sprite.get_pos()[0]+asteroid.sprite.get_size()[0] > 0,
                    asteroid.sprite.get_pos()[1]+asteroid.sprite.get_size()[1] > 0,
                    asteroid.sprite.get_pos()[0] < self.map.sprite.base_surface.get_size()[0],
                    asteroid.sprite.get_pos()[1] < self.map.sprite.base_surface.get_size()[1])
                        ):
                    self.remove_object(self.asteroids.pop(i))"""

    def add_planet(self, x: int = None, y: int = None, size: int = None):
        self.plannets.append(Planet(self.app, self, x, y, size))
        self.add_object(self.plannets[-1])

    def add_asteroid(self, x: int = None, y: int = None, size: int = None):
        self.asteroids.append(Asteroid(self.app, self, x, y, size))
        self.add_object(self.asteroids[-1])

    def draw(self, screen: pg.Surface):
        self.screen_ply_1.fill((255,0,0,255))
        self.screen_ply_2.fill((0,0,0,0))
        
        self.canvas_ply_1.fill((0,255,0,255))
        self.canvas_ply_2.fill((0,0,0,0))
        
        for object in self.objects:
            object.draw(self.canvas_ply_1)
            object.draw(self.canvas_ply_2)

        self.rect_ply_1.x = -self.camera_ply_1.sprite.rect.x
        self.rect_ply_1.y = -self.camera_ply_1.sprite.rect.y
        #self.rect_ply_1.width = self.app.size[0]
        
        self.rect_ply_2.x = -self.camera_ply_2.sprite.rect.x #+ self.app.size[0]
        self.rect_ply_2.y = -self.camera_ply_2.sprite.rect.y
        #self.rect_ply_2.width = self.app.size[0]
        
        self.screen_ply_1.blit(self.canvas_ply_1, self.rect_ply_1) #self.rect_ply_1
        self.screen_ply_2.blit(self.canvas_ply_2, self.rect_ply_2) #self.rect_ply_2
        
        screen.blit(self.screen_ply_1, (0, 0))
        screen.blit(self.screen_ply_2, (self.app.size[0], 0))
