import pygame

from tetromino import Tetromino
from block import Block

pygame.init()


class Otetromino(Tetromino):
    block_list = []
    
    def __init__(self, x, y, tetromino_size, xOffset, yOffset):
        super().__init__()
                
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.xOffset = xOffset // 2
        self.yOffset = yOffset // 2
        
        self.yellow = (255, 255, 0)
        
        self.createBlockList()
        
        
    def createBlockList(self):
        self.block_list = [
            Block(self.yellow, self.x + self.tetromino_size * 4 + self.xOffset + self.xOffset, self.y + self.yOffset, self.tetromino_size, self.tetromino_size),
            Block(self.yellow, self.x + self.tetromino_size * 5 + self.xOffset + self.xOffset, self.y + self.yOffset, self.tetromino_size, self.tetromino_size),
            Block(self.yellow, self.x + self.tetromino_size * 4 + self.xOffset + self.xOffset, self.y + self.tetromino_size + self.yOffset, self.tetromino_size, self.tetromino_size),
            Block(self.yellow, self.x + self.tetromino_size * 5 + self.xOffset + self.xOffset, self.y + self.tetromino_size + self.yOffset, self.tetromino_size, self.tetromino_size),
        ]
