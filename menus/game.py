import GTLib as gt
import pygame as pg

from entities import *
from .pause import Pause

class Game(gt.Menu):
    def __init__(self, app: gt.Advanced) -> None:
        super().__init__()
        self.app: gt.Advanced = app
        
        self.map: Map = Map(app, self)

        self.plannets: list = []
        self.asteroids: list = []
        self.bullets: list = []
        
        self.player1: Player = Player(self, profile="PROFILE_1", position=(self.app.size[0]//2-5, self.app.size[1]//2-5), size=(10,10))
        self.camera = Camera(app, self, self.player1)
        
        self.canvas = pg.Surface(self.map.sprite.base_surface.get_size(), pg.SRCALPHA, 32)
        self.rect = self.canvas.get_rect()
        
        #self.player2: Player = Player(profile="PROFILE_2", position=(30,30), size=(10,10))

        #self.groupe_sprit: gt.UI.Group = gt.UI.Group()       
        #self.add_object(self.groupe_sprit)
        
        self.add_object(self.map)
        self.add_object(self.camera)
        self.add_object(self.player1)
        
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
                    self.add_planet(None, None, None)

        @self.event()
        def k_add_asteroid(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_a:
                    self.add_asteroid(None, None, None)

    def add_planet(self, x, y, size):
        self.plannets.append(Planet(self.app, self, x, y, size))
        self.add_object(self.plannets[-1])

    def add_asteroid(self, x, y, size):
        self.asteroids.append(Asteroid(self.app, self, x, y, size))
        self.add_object(self.asteroids[-1])

    def draw(self, screen: pg.Surface):
        self.canvas.fill((0,0,0,0))
        
        for object in self.objects:
            object.draw(self.canvas)

        self.rect.x = -self.camera.sprite.rect.x
        self.rect.y = -self.camera.sprite.rect.y
        
        screen.blit(self.canvas, self.rect)
