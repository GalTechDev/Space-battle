import GTLib as gt
import pygame as pg
import pygame.freetype as ft

class Pause(gt.Menu):
    def __init__(self, app: gt.Base, game: gt.Menu) -> None:
        super().__init__()

        self.text = gt.Text(
            position=(0, 0),
            text="PAUSE",
            font = ft.SysFont('Verdana', 30)
        )

        self.text.set_pos(
            (app.size[0]//2, app.size[1]//2),
            (self.text.get_size()[0]//2, self.text.get_size()[1]//2)
        )

        self.add_object(self.text)

        @self.event()
        def resume_game(events):
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_ESCAPE:
                    app.call_menu(game)                  
                    #app.call_menu(game.player1)
                    #app.call_menu(game.player2)
                    
                    app.drop_menu(self)