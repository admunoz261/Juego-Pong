import os, sys, pygame

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    purple = (192,122,209)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        screen.fill(purple)

        pygame.display.update()

if __name__ == '__main__':
    main()
