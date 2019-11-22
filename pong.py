import os, sys, pygame
from pygame.locals import *

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    purple = (192,122,209)
    white = (0,0,0)

    velocidad = 2

    while 1:

        screen.fill(white)
        posx = 30
        posy = 180
        pygame.draw.rect(screen, purple , (posx, posy, 15, 100))
        pygame.draw.rect(screen, purple, (755, 100, 15, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys(exit)

        pygame.display.update()

if __name__ == '__main__':
    main()
