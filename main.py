from direct.showbase.ShowBase import ShowBase

from hero import Hero
from mapmanager import MapManager


# Клас гри
class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.land = MapManager(self)
        self.land.loadMap("map/map_position.txt", "map/map_textures.txt")
        self.hero = Hero(self, (5, 5, 2), self.land)
        self.camLens.setFov(90)


my_game = Game()
my_game.run()