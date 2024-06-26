import pygame

from tetromino import Tetromino
from block import Block

pygame.init()


class Otetromino(Tetromino):
    def __init__(self, x, y, tetromino_size, offset):
        super().__init__(x, y, tetromino_size, offset)
                
        self.color = (255, 255, 0)
        
        self.createBlockList()
        
        
    def createBlockList(self):
        self.block_list = [
            Block(self.color, self.x + self.tetromino_size * 4 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 5 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 4 + self.offset, self.y + self.tetromino_size + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 5 + self.offset, self.y + self.tetromino_size + self.offset, self.tetromino_size, self.tetromino_size),
        ]
