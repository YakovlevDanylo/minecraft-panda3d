from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
# Клас гри
class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.land = MapManager(self)
        self.camLens.setFov(90)


my_game = Game()
my_game.run()