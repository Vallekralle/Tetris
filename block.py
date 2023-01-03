import pygame
pygame.init()


class Block:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.rect = object
        
        
    def moveDirection(self, tetromino_size, direction):
        if direction == "down":
            self.y += tetromino_size
        elif direction == "left":
            self.x -= tetromino_size
        elif direction == "right":
            self.x += tetromino_size
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
