import pygame
pygame.init()


class Tetromino:
    color = ()
    block_list = []
    
    
    def __init__(self, x, y, tetromino_size, offset):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.offset = offset // 2
    
      
    def move(self):
        pass
        
    
    def draw(self, win):
        for block in self.block_list:
            pygame.draw.rect(win, block.color, (block.x, block.y, block.width, block.height))
