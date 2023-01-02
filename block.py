import pygame
pygame.init()


class Block:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
    def move(self, tetromino_size):
        self.y += tetromino_size
