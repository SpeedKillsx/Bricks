import pygame
from pygame.locals import *
screen_width = 600
screen_height = 600
ball_color = (250,128,125)
screen = pygame.display.set_mode((screen_width, screen_height))
class Ball():
    def __init__(self, x, y):
        self.reset(x, y)
    def draw(self):
        pygame.draw.circle(screen, ball_color,[self.rect.x + self.ball_rad, self.rect.y + self.ball_rad] , self.ball_rad)
        pygame.draw.circle(screen, ball_color,[self.rect.x + self.ball_rad, self.rect.y + self.ball_rad] , self.ball_rad, 3)
    def move(self, paddle, wall):
        # Check the direction
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        if  self.rect.bottom < 0:
            self.speed_y *=-1
        
        
        # Collision with the paddle
        if self.rect.colliderect(paddle):
            # ! Check if there is a collision withe the top of the paddle
            if abs(self.rect.bottom - paddle.rect.top) < 5 and self.speed_y >0:
                self.speed_y *=-1
                self.speed_x += paddle.direction
                # check if the X speed is higher than the max
                if self.speed_x>self.speed_max:
                    self.speed_x = self.speed_max
                # Check if the speed is under 0 or under - 5 
                elif self.speed_x < 0 or self.speed_x<-self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *=-1
        wall.destroyed = 1
        # Collision with the wall
        row_count = 0 
        for row in wall.block:
            # Check the collision for each rect in a row
            rectangle_count = 0
            for rectangle in row:
                if self.rect.colliderect(rectangle[0]):
                    # Check if the collision if in the bottom of the rect
                    if abs(self.rect.top - rectangle[0].bottom) < 5 and self.speed_y <0:
                        self.speed_y *=-1
                    # Check if the collision is from the top 
                    if abs(self.rect.bottom - rectangle[0].top) < 5 and self.speed_y >0:
                        self.speed_y *=-1
                    # Check if the collision is from behind 
                    if abs(self.rect.left - rectangle[0].right) < 5 and self.speed_x <0:
                        self.speed_x *=-1
                    if abs(self.rect.right - rectangle[0].left) < 5 and self.speed_x >0:
                        self.speed_x *=-1
                    # get the rectnagle position
                    save_position = [rectangle[0].x, rectangle[0].y]
                    if wall.block[row_count][rectangle_count][1] > 1:
                        #Decrase the strength
                        wall.block[row_count][rectangle_count][1] -= 1
                    elif wall.block[row_count][rectangle_count][1] == 1:
                        wall.block[row_count][rectangle_count][0] = (0,0,0,0)
                if wall.block[row_count][rectangle_count][0]!=(0,0,0,0):
                    wall.destroyed =0
                rectangle_count+=1
            row_count+=1
        
        if wall.destroyed == 1:
            self.game_over = 2
                                
        if self.rect.top > screen_height :
            self.game_over = -1
        #  Move the ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        return self.game_over
    def reset(self, x, y):
        self.ball_rad = 10
        # Center the ball
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0
