import pygame
from time import sleep
pygame.init()


class Tetromino:
    color = ()
    block_list = []
    
    
    def __init__(self, x, y, tetromino_size, offset):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.offset = offset // 2
        
        
    def move(self, padY, frameHeight, speed, spawnNewTetromino):
        while(self.grounded(padY, frameHeight)):
            sleep(speed)
            
            for block in self.block_list:
                block.move(self.tetromino_size)  
        else:
            spawnNewTetromino()
                
                
    def grounded(self, padY, frameHeight):
        for block in self.block_list:
            if block.y + self.tetromino_size > padY + frameHeight:
                return False
        return True
    
    
    def draw(self, win):
        for block in self.block_list:
            pygame.draw.rect(win, block.color, (block.x, block.y, block.width, block.height))
