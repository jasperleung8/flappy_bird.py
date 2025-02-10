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

    def __init__(self,groups):
        pygame.sprite.Sprite.__init__(self)
        
