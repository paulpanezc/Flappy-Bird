from random import randint
import os
import pygame


logo_width, punctuation_width, restart_width, pipe_width, window_width = 200, 100, 150, 48, 384
background_height, pipe_height, min_pipe_height, window_height = 425, 300, 50, 525
WHITE_COLOR, BLACK_COLOR = (255, 255, 255), (0, 0, 0)
pipe_distanceX, pipe_distanceY = (window_width - pipe_width)/2, 100
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
speed = 3
window = pygame.display.set_mode((window_width, window_height))
NUMBERS = [[[(187, 50), (177, 50), (177, 100), (207, 100), (207, 50), (187, 50), (187, 90), (197, 90), (197, 60), (187, 60)], # white points of 0
            [(190, 47), (174, 47), (174, 103), (210, 103), (210, 47), (190, 47), (190, 87), (194, 87), (194, 63), (190, 63)]], # black points of 0
            [[(184.5, 50), (184.5, 65), (189.5, 65), (189.5, 100), (199.5, 100), (199.5, 50)], # white points of 1
            [(181.5, 47), (181.5, 68), (186.5, 68), (186.5, 103), (202.5, 103), (202.5, 47)]], # black points of 1
            [[(177, 50), (177, 60), (191, 60), (191, 70), (177, 70), (177, 100), (201, 100), (201, 90), (187, 90), (187, 80), (201, 80), (201, 50)], # white points of 2
            [(174, 47), (174, 63), (188, 63), (188, 67), (174, 67), (174, 103), (204, 103), (204, 87), (190, 87), (190, 83), (204, 83), (204, 47)]], # black points of 2
            [[(201, 50), (177, 50), (177, 60), (191, 60), (191, 70), (177, 70), (177, 80), (191, 80), (191, 90), (177, 90), (177, 100), (201, 100)], # white points of 3
            [(204, 47), (174, 47), (174, 63), (188, 63), (188, 67), (174, 67), (174, 83), (188, 83), (188, 87), (174, 87), (174, 103), (204, 103)]], # black points of 3
            [[(177, 50), (187, 50), (187, 70), (197, 70), (197, 50), (207, 50), (207, 100), (197, 100), (197, 85), (177, 85)], # white points of 4
            [(174, 47), (190, 47), (190, 67), (194, 67), (194, 47), (210, 47), (210, 103), (194, 103), (194, 88), (174, 88)]], # black points of 4
            [[(177, 50), (177, 80), (197, 80), (197, 90), (177, 90), (177, 100), (207, 100), (207, 70), (187, 70), (187, 60), (207, 60), (207, 50)], # white points of 5
            [(174, 47), (174, 83), (194, 83), (194, 87), (174, 87), (174, 103), (210, 103), (210, 67), (190, 67), (190, 63), (210, 63), (210, 47)]], # black points of 5
            [[(187, 70), (187, 60), (207, 60), (207, 50), (177, 50), (177, 100), (207, 100), (207, 70), (187, 70), (187, 80), (187, 90), (197, 90), (197, 80), (187, 80)], # white points of 6
            [(190, 67), (190, 63), (210, 63), (210, 47), (174, 47), (174, 103), (210, 103), (210, 67), (190, 67), (190, 83), (190, 87), (194, 87), (194, 83), (190, 83)]], # black points of 6
            [[(177, 50), (177, 70), (187, 70), (187, 60), (197, 60), (197, 100), (207, 100), (207, 50), (177, 50)], # white points of 7
            [(174, 47), (174, 73), (190, 73), (190, 63), (194, 63), (194, 103), (210, 103), (210, 47), (174, 47)]], # black points of 7
            [[(187, 70), (187, 60), (197, 60), (197, 70), (177, 70), (177, 50), (207, 50), (207, 100), (177, 100), (177, 70), (187, 70), (187, 80), (187, 90), (197, 90), (197, 80), (187, 80)], # white points of 8
            [(190, 67), (190, 63), (194, 63), (194, 67), (174, 67), (174, 47), (210, 47), (210, 103), (174, 103), (174, 67), (190, 67), (190, 83), (190, 87), (194, 87), (194, 83), (190, 83)]], # black points of 8
            [[(197, 80), (197, 90), (177, 90), (177, 100), (207, 100), (207, 50), (177, 50), (177, 80), (197, 80), (197, 70), (197, 60), (187, 60), (187, 70), (197, 70)], # white points of 9
            [(194, 83), (194, 87), (174, 87), (174, 103), (210, 103), (210, 47), (174, 47), (174, 83), (194, 83), (194, 67), (194, 63), (190, 63), (190, 67), (194, 67)]]] # black points of 9


class Number:
    def __init__(self, value):
        self.value = value

    def draw(self, ratio):
        black_points = []
        for x in NUMBERS[self.value][1]:
            black_points.append((x[0] + ratio * 30, x[1]))
        pygame.draw.polygon(window, BLACK_COLOR, tuple(black_points))
        white_points = []
        for x in NUMBERS[self.value][0]:
            white_points.append((x[0] + ratio * 30, x[1]))
        pygame.draw.polygon(window, WHITE_COLOR, tuple(white_points))


class Game:
    def __init__(self):
        self.accumulator = 0
        self.collision = False
        self.punctuation = 0
        self.best = 0
        self.starting = False
        self.bird = Bird()
        self.ground = Ground()
        self.column1 = PipeGroup(0)
        self.column2 = PipeGroup(self.column1.posX)
        self.pipe1 = Pipe(False)
        self.pipe2 = Pipe(True)
        self.pipe3 = Pipe(False)
        self.pipe4 = Pipe(True)
        self.column1.add(self.pipe1, self.pipe2)
        self.column2.add(self.pipe3, self.pipe4)
    
    def show_punctuation(self):
        pos = 0
        score = str(self.punctuation)
        digits = len(score)
        for d in score:
            digit = Number(int(d))
            digit.draw((((pos * 2) - digits) + 1) / 2)
            pos += 1


class PipeGroup(pygame.sprite.Group):
    def __init__(self, separation):
        pygame.sprite.Group.__init__(self)
        if separation > 0:
            self.posX = pipe_width + pipe_distanceX + separation
        else:
            self.posX = 2 * window_width
        self.posY = randint(min_pipe_height + pipe_distanceY, background_height - min_pipe_height)

    def move(self, separation):
        self.posX -= speed
        if self.posX < -1 * pipe_width:
            if separation > 0:
                self.posX = pipe_width + pipe_distanceX + separation
            else:
                self.posX = window_width
            self.posY = randint(min_pipe_height + pipe_distanceY, background_height - min_pipe_height)


class Item(pygame.sprite.Sprite):
    def __init__(self, width, height, image_name):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        image_path = os.path.join(PROJECT_PATH, 'img/' + image_name + '.png')
        self.image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.posX = 0
        self.posY = 0

    def show(self):
        window.blit(self.image, self.rect)

    def update(self, position):
        self.posX = position[0]
        self.posY = position[1]
        self.rect.left = self.posX
        self.rect.top = self.posY


class Bird(Item):
    def __init__(self):
        Item.__init__(self, 45, 33, 'bird2')
        self.initial_angle = 22.5
        self.final_angle = 270
        self.up = True
        self.flying = False
        self.state = 1
        self.posX = 177
        self.posY = 225
        self.initial_posY = self.posY
        self.rotated = False
        self.down_time = 0
        self.flying_time = 6
        self.speed = 0.5
        self._state = self.flying_time
        self.images = {}
        self.rotate_images = {}
        for i in range(1, 4):
            image_path = os.path.join(PROJECT_PATH, 'img/bird' + str(i) + '.png')
            image = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (self.width, self.height))
            self.images[self.flying_time * i] = image
            self.rotate_images[self.flying_time * i] = pygame.transform.rotate(image, self.initial_angle)

    def fly(self, start):
        if self.rotated:
            self.images = self.rotate_images
            rotate_bird = self.images[self.flying_time]
            self.rect.width = rotate_bird.get_rect().width
            self.rect.height = rotate_bird.get_rect().height
        if not start:
            if self.up:
                if self.posY < self.initial_posY + 6:
                    self.posY += self.speed
                else:
                    self.up = False
            else:
                if self.posY > self.initial_posY - 3:
                    self.posY -= self.speed
                else:
                    self.up = True
        else:
            if self.flying:
                self.posY -= 35
                self.flying = False
            else:
                self.down_time += 0.75
                self.posY += 0.25 * self.down_time
        self.update((self.posX, self.posY))
        if self.state % self.flying_time == 0:
            window.blit(self.images[self.state], self.rect)
            self._state = self.state
        else:
            window.blit(self.images[self._state], self.rect)
        if self.state != self.flying_time * len(self.images):
            self.state += 1
        else:
            self.state = 1

    def stop(self):
        rotate_bird = pygame.transform.rotate(self.image, self.final_angle)
        self.rect.top = background_height - self.width
        window.blit(rotate_bird, self.rect)


class Ground(Item):
    def __init__(self):
        Item.__init__(self, 25, window_height - background_height, 'ground')
        self.posX = 2 * window_width

    def show(self):
        for i in range(1, self.posX // self.width + 2):
            self.rect.left, self.rect.top = self.posX - self.width * i, background_height
            window.blit(self.image, self.rect)

    def move(self):
        self.posX -= speed
        if self.posX < window_height:
            self.posX = 2 * window_height


class Pipe(Item):
    def __init__(self, invested):
        Item.__init__(self, pipe_width, pipe_height, 'pipe')
        if invested:
            self.image = pygame.transform.flip(self.image, False, True)
