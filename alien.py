import sys
import random, pygame
from pygame.locals import *

class Alien:
    def __init__(self, screen, alien_image):
        self.x = random.randint(0, 570)
        self.y = 45
        self.screen = screen
        self.alien_image = alien_image
        
    def move(self):
        self. y += 5

    def draw(self):
        self.screen.blit(self.alien_image, (self.x, self.y))
        