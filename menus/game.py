import GTLib as gt
import pygame as pg

from entitys import *
from .map import Map
from .pause import Pause

class Game(gt.Menu):
    def __init__(self, app: gt.Advanced) -> None:
        super().__init__()
        self.app: gt.Advanced = app
        
        self.map: Map = Map()

        self.plannets: list = []
        self.asteroids: list = []
        self.bullets: list = []
        
        self.player1: Player = Player(profile="PROFILE_1", position=(10,10), size=(10,10))
        self.player2: Player = Player(profile="PROFILE_2", position=(30,30), size=(10,10))

        self.groupe_sprit: gt.UI.Group = gt.UI.Group()       
        self.add_sprite(self.groupe_sprit)
        
        app.call_menu(self.player1)
        app.call_menu(self.player2)
        
        @self.event()
        def pause_game(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_ESCAPE:
                    app.call_menu(Pause(app, self))

                    app.drop_menu(self)
                    app.drop_menu(self.player1)
                    app.drop_menu(self.player2)
                  
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
        self.app.call_menu(self.plannets[-1])

    def add_asteroid(self, x, y, size):
        self.asteroids.append(Asteroid(self.app, self, x, y, size))
        self.app.call_menu(self.asteroids[-1])