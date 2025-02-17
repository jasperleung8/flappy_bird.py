import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 864
height = 936

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy bird")

font = pygame.font.SysFont('Bauhaus 93',60)

white = (255,255,255)

ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

bg = pygame.images.load("background2.png")
ground = pygame.images.load("ground.png")
button = pygame.images.load("restart.png")

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(height/2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for  num in range(1,4):
            img = pygame.image.load(f"bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False

    def update (self):

        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            flap_cooldown = 5
            self.counter += 1

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2)

        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y - int(pipe_gap / 2)] 
        elif position == -1:
            self.rect.topleft = [x,y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0 :
            self.kill()

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action
