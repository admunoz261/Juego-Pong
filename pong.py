import os, sys, pygame

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    blanco = (120,216,235)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        pygame.draw.rect(screen, blanco, (0, 0,15,100))
        pygame.draw.rect(screen, blanco, (0, 300,15,100))
        pygame.draw.rect(screen, blanco, (0,385,800,15))
        pygame.draw.rect(screen, blanco, (0,0,800,15))
        pygame.draw.rect(screen, blanco, (785, 0,15,100))
        pygame.draw.rect(screen, blanco, (785, 300,15,100))
        pygame.display.update()

if __name__ == '__main__':
    main()
