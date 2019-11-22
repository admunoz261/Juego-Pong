import os, sys, pygame

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()
