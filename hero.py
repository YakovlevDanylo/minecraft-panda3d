# напиши свій код тут

key_switch_camera = 'c'  # камера прив’язана до героя чи ні
key_switch_mode = 'z'  # можна проходити крізь перешкоди чи ні

key_forward = 'w'  # крок уперед (туди, куди дивиться камера)
key_back = 's'  # крок назад
key_left = 'a'  # крок ліворуч (убік від камери)
key_right = 'd'  # крок праворуч
key_up = 'e'  # крок угору
key_down = 'q'  # крок униз

key_turn_left = 'n'  # поворот камери праворуч (а світу — ліворуч)
key_turn_right = 'm'  # поворот камери ліворуч (а світу — праворуч)


class Hero:
    def __init__(self, game, pos, land):
        self.game = game
        self.land = land
        self.mode = True  # режим проходження крізь усе
        self.hero = self.game.loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(self.game.render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        self.game.disableMouse()
        self.game.camera.setH(180)
        self.game.camera.setP(0)
        self.game.camera.setR(0)
        self.game.camera.reparentTo(self.hero)
        self.game.camera.setPos(0, 10, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        self.game.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        self.game.camera.reparentTo(self.game.render)
        self.game.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        '''повертає координати, куди переміститься персонаж, що стоїть у точці (x, y),
        якщо він зробить крок у напрямку angle'''

        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        '''переміщується в потрібні координати у будь-якому випадку'''
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def check_dir(self, angle):
        '''повертає округлені зміни координат X, Y,
        що відповідають руху у напрямку кута angle.
        Координата Y зменшується, якщо персонаж дивиться на кут 0,
        і збільшується, якщо дивиться на кут 180.
        Координата X збільшується, якщо персонаж дивиться на кут 90,
        і зменшується, якщо дивиться на кут 270.
            кут 0 (від 0 до 20)        ->        Y - 1
            кут 45 (від 25 до 65)      -> X + 1, Y - 1
            кут 90 (від 70 до 110)     -> X + 1
            від 115 до 155             -> X + 1, Y + 1
            від 160 до 200             ->        Y + 1
            від 205 до 245             -> X - 1, Y + 1
            від 250 до 290             -> X - 1
            від 290 до 335             -> X - 1, Y - 1
            від 340                    ->        Y - 1'''
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def accept_events(self):
        self.game.accept(key_turn_left, self.turn_left)
        self.game.accept(key_turn_left + '-repeat', self.turn_left)
        self.game.accept(key_turn_right, self.turn_right)
        self.game.accept(key_turn_right + '-repeat', self.turn_right)

        self.game.accept(key_forward, self.forward)
        self.game.accept(key_forward + '-repeat', self.forward)
        self.game.accept(key_back, self.back)
        self.game.accept(key_back + '-repeat', self.back)
        self.game.accept(key_left, self.left)
        self.game.accept(key_left + '-repeat', self.left)
        self.game.accept(key_right, self.right)
        self.game.accept(key_right + '-repeat', self.right)

        self.game.accept(key_switch_camera, self.changeView)
