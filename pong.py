import os, sys, pygame

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    #----------Pelota----------
    #Código de la pelota
    #--------------------------

    #pelota = (255, 255, 255)
    pelota = pygame.image.load("icon.png")
    bola = pelota.get_rect()
    fondo = (128, 128, 128)
    speed = [1, 1]

    
    while 1:
        pos = (400, 200)
        pygame.time.delay(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                   
        bola = bola.move(speed)

        if (bola.left < 0 or bola.right > width):
            bola = pelota.get_rect(center = pos)
            

        if (bola.top < 0 or bola.bottom > height):
            speed[1] = -speed[1]

        screen.fill(fondo)
        screen.blit(pelota, bola)
        #pygame.draw.circle(screen, pelota, (400, 200), 15)
        pygame.display.flip()                

if __name__ == '__main__':
    main()
