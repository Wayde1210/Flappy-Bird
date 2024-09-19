import pygame
import random
from pygame.locals import *

pygame.init()

clock= pygame.time.Clock()
fps=60

WIDTH=864
HEIGHT=936

screen=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Flappy Bird Game')

#define font
font= pygame.font.SysFont('Bauhaus 93', 60)

#define colours
white=(255,255,255)

#define game variabeles
ground_Scroll =0
scroll_speed=100
flying=False

game_over=False
pip_gap=150
pipe_frequency=1500 #milliseconds

last_pipe=pygame.time.get_ticks()-pipe_frequency

score=0

pass_pipe=False

#load images

bg=pygame.image.load('Flappy bird/assets/bg.png')
ground_img=pygame.image.load('Flappy bird/assets/ground.png')
button_img=pygame.image.load('Flappy Bird/assets/restart.png')

#function for showing the text on the screen
def draw_text(text,font, text_col, x. y):
    img=font.render(text,True,text_col)
    screen.blit(img,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x=100
    flappy.rect.y=int(screen_height/2)
    score=0
    return score

class Bird(pygame.sprite.sprite):
    def __init__(self,x,y):
        pygame.sprite.sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,4):
            img=pygame.image.load(f'Flappy Bird/assets/bird{num}.png')
            self.images.append(img)
            self.image=self.images[self.index] #list_name[index_num]
            self.rect=self.image.get_rect()
            self.rect.center= [x,y]
            self.vel=0  #velocity  -  speed
            self.clicked=False#when click on birdn -it will turn to be true


    def update(self):
        if flying==True:
            #apply gravity
            self.vel+= 0.5 #speed
            if self.vel > 8:
                self.vel=8
            if self.rect.bottom <768:
                self.rect.y += int(self.vel)

            
