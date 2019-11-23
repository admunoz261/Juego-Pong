import os, sys, pygame

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    #----------Pelota----------
    #Código de la pelota
    #--------------------------

    pelota = (255, 255, 255)
    fondo = (128, 128, 128)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        screen.fill(fondo)
        pygame.draw.circle(screen, pelota, (400, 200), 15)
        pygame.display.update()
                

if __name__ == '__main__':
    main()
