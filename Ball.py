import pygame
from pygame.locals import *
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
class Ball():
    def __init__(self):
        self.size = 10
    def draw(self):
        pygame.draw.circle(screen, (200,0,0),[screen_width // 2, screen_height - 80], self.size, 0)
