import alien
import sys
import random, pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Space Pirates!")
screen = pygame.display.set_mode((640, 650))

alien_image = pygame.image.load("alien.png")

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen.fill((0 , 0 , 0))
        alien.move()
        alien.draw()
        pygame.display.update()
