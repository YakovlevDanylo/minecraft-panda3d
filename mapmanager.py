from random import random

class MapManager:
    def __init__(self, game):
        self.game = game # Зберігання посилання на нашу гру

        # Збереження посилання на модель та текстурку
        self.model = "assets/models/block"
        self.texture = "assets/textures/sand1.png"

        self.startNew()

        self.createSome()


    def startNew(self):
        self.land = self.game.render.attachNewNode("land")

    def addBlock(self, position, color):
        # Завантаження моделі блока і тектури та накладання на неї текстури
        self.block = self.game.loader.loadModel(self.model)
        self.block_texture = self.game.loader.loadTexture(self.texture)
        self.block.setTexture(self.block_texture)

        # Встановлення кольору та позиції
        #self.block.setColor(color)
        self.block.setPos(position)

        # Прив'язка до сцени
        self.block.reparentTo(self.land)

    def createSome(self):
        for j in range(10):
            for i in range(10):
                self.addBlock(position=(0+i, 10+j, 0), color=(random(), random(), random(), 1))

        for i in range(4):
            self.addBlock(position=(0, 10, 1+i), color=(random(), random(), random(), 1))

        for i in range(4):
            self.addBlock(position=(9, 10, 1+i), color=(random(), random(), random(), 1))

        for i in range(4):
            self.addBlock(position=(0, 19, 1+i), color=(random(), random(), random(), 1))

        for i in range(4):
            self.addBlock(position=(9, 19, 1+i), color=(random(), random(), random(), 1))