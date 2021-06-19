import pygame

import pygame, sys
from code.setting import settings


pygame.init()


surface = pygame.display.set_mode([settings.width, settings.height])

name = pygame.display.set_caption(settings.name)

icon = pygame.image.load(settings.icon)
pygame.display.set_icon(icon)


run = True
while run:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

pygame.quit()
# sys.exit