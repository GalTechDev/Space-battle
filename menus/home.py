import GTLib as gt

class Home(gt.Menu):
    def __init__(self) -> None:
        super().__init__()

        self.groupe_square = gt.UI.Group()
        self.add_object(self.groupe_square)
        self.update()
