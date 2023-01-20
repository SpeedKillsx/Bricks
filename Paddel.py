import pygame
from pygame.locals import *

screen_width = 600
screen_height = 600
cols = 6
rows = 6
paddle_color = (250,128,125)
screen = pygame.display.set_mode((screen_width, screen_height))
class Paddle():
    def __init__(self):
        self.height = 20
        self.width = screen_width // cols
        self.x = int((screen_width/2) - (self.width/2))
        self.y = screen_height - self.height * 3
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 10
        self.direction = 0
    def move(self):
        # Definier la direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x = self.rect.x + self.speed
            self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, paddle_color, self.rect)
       

            