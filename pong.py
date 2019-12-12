import os, sys, pygame
from pygame.locals import *
from random import randint

class Pad(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 100)).convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.max_speed = 5
        self.speed = 0

    def move_up(self):
        self.speed = self.max_speed * -1

    def move_down(self):
        self.speed = self.max_speed * 1

    def stop(self):
        self.speed = 0

    def update(self):
        self.rect.move_ip(0, self.speed)

class Pelota(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pygame.image.load("icon.png")
        self.rect = self.image.get_rect(center=self.pos)
        self.speed_x = 0
        self.speed_y = 0
        #pelota = pygame.image.load("icon.png")
        #bola = pelota.get_rect()
        #speed = [1, 1]

    def change_y(self):
        self.speed_y *= -1

    def change_x(self):
        self.speed_x *= -1

    def movimiento(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
      self.rect.move_ip(self.speed_x, self.speed_y)

    def reset(self):
        self.rect = self.image.get_rect(center=self.pos)

class Score(pygame.sprite.Sprite):
    def __init__(self, font, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.font = font
        self.pos = pos
        self.score = 0
        self.image = self.font.render(str(self.score), 0, (255, 255, 255))
        self.rect = self.image.get_rect(center=self.pos)

    def score_up(self):
        self.score += 1

    def update(self):
        self.image = self.font.render(str(self.score), 0, (255, 255, 255))
        self.rect = self.image.get_rect(center=self.pos)

def main():
    pygame.init()

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')
    

    bola = Pelota((400, 200))

    pad_left = Pad((30, 300))
    pad_right = Pad((770, 300))

    sprites = pygame.sprite.Group(pad_left, pad_right, bola)

    clock = pygame.time.Clock()
    fps = 60

    pygame.key.set_repeat(1, 16)

    top = pygame.Rect(0, 0, width, 5)
    bottom = pygame.Rect(0, height-5, width, 5)


    if not pygame.font:
        raise SystemExit('Pygame does not support fonts')

    try:
        filename = os.path.join(
            os.path.dirname(__file__),
            'assets',
            'fonts',
            'wendy.ttf')
        font = pygame.font.Font(filename, 90)
    except pygame.error as e:
        print ('Cannot load font: ', filename)
        raise SystemExit(str(e))

    left_score = Score(font, (width/3, height/8))
    right_score = Score(font, (2*width/3, height/8)) 
        
    sprites = pygame.sprite.Group(
        pad_left, pad_right, bola, left_score, right_score)

    left = pygame.Rect(0, 0, 5, height)
    right = pygame.Rect(width-5, 0, 5, height)


    while 1:
        try:
            filename = os.path.join(
                os.path.dirname(__file__),
                'background.jpg')
            background = pygame.image.load(filename)
            background = background.convert()
        except pygame.error as e:
            print ('Cannot load image: ', filename)
            raise SystemExit(str(e))

        #screen.blit(background, (0, 0))
        #pygame.display.flip() 

        clock.tick(fps)
        pad_left.stop()
        pad_right.stop()

        screen_rect = screen.get_rect().inflate(0, -28)
        pad_left.rect.clamp_ip(screen_rect)
        pad_right.rect.clamp_ip(screen_rect)

        #pos = (400, 200)
        #pygame.time.delay(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                pad_left.move_up()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pad_left.move_down()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                pad_right.move_up()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                pad_right.move_down()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bola.movimiento(randint(1, 3), randint(1, 3))

        if bola.rect.colliderect(top) or bola.rect.colliderect(bottom):
            bola.change_y()
        elif (bola.rect.colliderect(pad_left.rect) or bola.rect.colliderect(pad_right.rect)):
            bola.change_x()
                   
        #bola = bola.move(speed)
        #if (bola.left < 0 or bola.right > width):
            #bola = pelota.get_rect(center = pos)
            

        #if (bola.top < 0 or bola.bottom > height):
            #speed[1] = -speed[1]
        if bola.rect.colliderect(left):
            right_score.score_up()
            bola.reset()
            bola.stop()
        elif bola.rect.colliderect(right):
            left_score.score_up()
            bola.reset()
            bola.stop()


        sprites.update()
        screen.blit(background, (0, 0))
        sprites.draw(screen)
        #screen.blit(pelota, bola)
        #pygame.draw.circle(screen, pelota, (400, 200), 15)
        pygame.display.flip()                

if __name__ == '__main__':
    main()
