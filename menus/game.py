import GTLib as gt
from entitys import *

class Game(gt.Menu):
    def __init__(self, app: gt.Advanced) -> None:
        super().__init__()
        
        self.map = Map()
        
        self.player1 = Player(profile="PROFILE_1", position=(10,10), size=(10,10))
        self.player2 = Player(profile="PROFILE_2", position=(30,30), size=(10,10))

        self.groupe_square = gt.UI.Group()       
        self.add_sprite(self.groupe_square)
        
        app.call_menu(self.player1)
        app.call_menu(self.player2)
        
        self.update()
        
        @self.event()
        def pause_game(events):
            pass

class Map():
    def __init__(self) -> None:
        pass