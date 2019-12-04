import os, sys, pygame
from pygame.locals import *

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    purple = (192,122,209)
    white = (0, 0, 0)

    velocidad = 2

    while 1:

        screen.fill(white)
        posx1 = 30
        posy1 = 140

        posx2 = 755
        posy2 = 140

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys(exit)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        posx1 = posx1 - 4
                    elif event.key == pygame.K_RIGHT:
                        posx1 = posx1 + 4
                    elif event.key == pygame.K_UP:
                        posy1 = posy1 - 4
                    elif event.key == pygame.K_DOWN:
                        posy1 = posy1 + 4
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        posx2 = posx2 - 4
                    elif event.key == pygame.K_RIGHT:
                        posx2 = posx2 + 4
                    elif event.key == pygame.K_UP:
                        posy2 = posy2 - 4
                    elif event.key == pygame.K_DOWN:
                        posy2 = posy2 + 4

        pygame.draw.rect(screen, purple , (posx1, posy1, 15, 100))
        pygame.draw.rect(screen, purple, (posx2, posy2, 15, 100))

        pygame.display.update()

if __name__ == '__main__':
    main()
