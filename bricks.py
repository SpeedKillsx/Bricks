import pygame
from pygame.locals import *
from Mur import *
from Paddel import *
from Ball import *
# Initialiser la fenetre de jeu
pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bricks')
# Commencer la programmation des evenements du jeu

run = True
mur = Mur()
mur.create_wall()
QUANTAM = pygame.time.Clock()
paddle = Paddle()

ball = Ball(paddle.x +(paddle.width// 2),paddle.y-(paddle.height))

while run:
    # Definer fps
    QUANTAM.tick(60)
    # Definir une couleur de Background
    screen.fill((250,208,105))
    
    # Dessiner 
    mur.draw_wall()
    paddle.draw()
    paddle.move()
    ball.draw()
    if ball.move(paddle=paddle, wall=mur) == 0:
        pass
    elif ball.move(paddle=paddle, wall=mur) == -1:
        ball.reset(paddle.x +(paddle.width// 2),paddle.y-(paddle.height))
    else:
        print("YOU WIN")
        run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()
        

pygame.quit()
