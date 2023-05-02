import pygame, sys
from spritesheet import *

pygame.init()

screen = pygame.display.set_mode((400,200))

display_surface = pygame.display.get_surface()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    display_surface.fill('white')

    sprite = SpriteSheet.get_image('SpriteSheets/Tools.png',6,6,1,1)

    display_surface.blit(sprite[0], sprite[1])