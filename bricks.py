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

ball = Ball()

while run:
    # Definer fps
    QUANTAM.tick(60)
    # Definir une couleur de Background
    screen.fill((250,208,105))
    
    # Dessiner 
    mur.draw_wall()
    ball.draw()
    paddle.draw()
    paddle.move()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
        

pygame.quit()
