import pygame
import os

#set up asset folders
folder = os.path.dirname(os.path.realpath(__file__))
img_folder = os.path.join(folder, 'assets')
player_img = pygame.image.load("IMG-20180922-WA0001.jpg")

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#templates
WIDTH = 899
HEIGHT = 1599
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 3
        #self.rect.y -= 3
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top= HEIGHT