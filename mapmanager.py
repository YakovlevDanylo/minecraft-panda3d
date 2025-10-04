from random import random

class MapManager:
    def __init__(self, game):
        self.game = game # Зберігання посилання на нашу гру

        # Збереження посилання на модель та текстурку
        self.model = "assets/models/block"
        self.texture = "assets/textures/block.png"

        self.startNew()



    def startNew(self):
        self.land = self.game.render.attachNewNode("land")

    def addBlock(self, position):
        # Завантаження моделі блока і тектури та накладання на неї текстури
        self.block = self.game.loader.loadModel(self.model)
        self.block_texture = self.game.loader.loadTexture(self.texture)
        self.block.setTexture(self.block_texture)

        # Встановлення кольору та позиції

        self.block.setPos(position)

        # Прив'язка до сцени
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadMap(self, map_file, texture_file):
        self.clear()

        pos_lines = open(map_file).read().strip().split("\n")
        texture_lines = open(texture_file).read().strip().split("\n")

        y = 0
        while y < len(pos_lines):
            row_line = pos_lines[y].split()
            texture_line = texture_lines[y].split()
            x = 0

            while x < len(row_line):
                height = int(row_line[x])
                texture_num = texture_line[x]

                if texture_num == "0":
                    self.texture = "assets/textures/block_wood.png"
                elif texture_num == "1":
                    self.texture = "assets/textures/sand1.png"
                elif texture_num == "2":
                    self.texture = "assets/textures/wood.png"

                z = 0
                while z <= height:
                    self.addBlock((x,y,z))
                    z+=1
                x+=1
            y+=1