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
        if game_over==False:
            #jump
            pygame.mouse.get_pressed()[0]==1 and self.clicked==False
            self.clicked=True
            self.vel=-10
            if pygame.mouse.get_pressed()[0]==1:
                self.clicked=False


            #handle the animation
            flap_cooldown=5
            self.counter+=1

            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images)                                                                                                                            :
                    self.index=0
                self.image=self.images[self.index                                                                                                                          ]

            #rotate the bird
            self.image=pygame.transform.rotate(self.images[self.index])    (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

        else:
        #point the bird at the ground
            self.image=pygame.transform.rotate(self.images[self.index],-90)

class Pipe(pygame.sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        self.image=pygame.image.load('flappy bird/assets/pipe.png')
        self.rect=self.image.get_rect()
        #position variables determins whether pipe comes from top or bottom
        #if position is 1 then pipe comes from top and if -1 then comes from bottom
        if position==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomLeft=[x,y-int(pip_gap/2)]
        else:
            self.rect.topleft[x,y+int(pip_gap/2)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    def update (self):
        self.rect.x -=scroll_speed
        if self.rect.right<0:
            self.kill()#

class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topLeft=(x,y)

    def draw(self):
        action=False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #get mouseover and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True

        #draw button
        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action


pipe_group=pygame.sprite.Group()
bird_group=pygame.sprite.Group()

flappy=Bird(100,int(HEIGHT/2))

bird_group.add(flappy)


#restart button
button=Button(WIDTH//2-50,HEIGHT//2-100,button_img)

run==True
while run:
    clock.tick(fps)

    #draw background
    screen.blit(bg,(0,0))

    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()

    #draw and scroll the ground
    screen.blit(ground_img,(ground_Scroll,768))

    #check the score
    if len(pipe_group)>0:
        if bird_group.sprites()[0].rect.left>pipe_group.sprites()[0].rect.left\
        and bird_group.sprites()[0].rect.right<pipe_group.sprites()[0].rect.right\
        and pass_pipe==False:
            pass_pipe=True
