import pygame
from pygame.locals import *
rows = 6
cols = 6
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
##! Definir les couleurs des bricks
red = (120,5,2)
blue = (5,12,200)
green = (5,200,5)

class Mur():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 60
    def create_wall(self):
        self.block = []
        # Block list for each block
        block_individual = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                blockX = col * self.width
                blockY = row* self.height
                rect = pygame.Rect(blockX, blockY, self.width, self.height)
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                block_individual = [rect, strength]
                block_row.append(block_individual)
            # Ajouter le blcok vers la liste
            self.block.append(block_row)
    
    def draw_wall(self):
        for row in self.block:
            for block in row:
                #assign a colour based on block strength
                if block[1] == 3:
                    block_col = blue
                elif block[1] == 2:
                    block_col = green
                elif block[1] == 1:
                    block_col = red
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, (250,208,105), (block[0]), 2)