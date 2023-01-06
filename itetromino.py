import pygame

from tetromino import Tetromino
from block import Block

pygame.init()


class Itetromino(Tetromino):
    def __init__(self, x, y, tetromino_size, offset):
        super().__init__(x, y, tetromino_size, offset)
                
        self.color = (0, 255, 255)
        
        self.createBlockList()
        
        
    def rotateBlocks(self, dirNum):
        self.rotation_list = [
            [
                Block(self.color, self.block_list[0].x - self.tetromino_size * 2 if dirNum == -1 else self.block_list[0].x - self.tetromino_size, self.block_list[0].y - self.tetromino_size * 2 if dirNum == 1 else self.block_list[0].y + self.tetromino_size, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[1].x - self.tetromino_size if dirNum == -1 else self.block_list[1].x, self.block_list[1].y - self.tetromino_size if dirNum == 1 else self.block_list[1].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[2].x + self.tetromino_size if dirNum == 1 else self.block_list[2].x, self.block_list[2].y - self.tetromino_size if dirNum == -1 else self.block_list[2].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[3].x + self.tetromino_size * 2 if dirNum == 1 else self.block_list[3].x + self.tetromino_size, self.block_list[3].y - self.tetromino_size * 2 if dirNum == -1 else self.block_list[3].y + self.tetromino_size, self.tetromino_size, self.tetromino_size),
            ],
            [
                Block(self.color, self.block_list[0].x + self.tetromino_size * 2 if dirNum == 1 else self.block_list[0].x - self.tetromino_size, self.block_list[0].y - self.tetromino_size * 2 if dirNum == -1 else self.block_list[0].y - self.tetromino_size, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[1].x + self.tetromino_size if dirNum == 1 else self.block_list[1].x, self.block_list[1].y - self.tetromino_size if dirNum == -1 else self.block_list[1].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[2].x + self.tetromino_size if dirNum == -1 else self.block_list[2].x, self.block_list[2].y + self.tetromino_size if dirNum == 1 else self.block_list[2].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[3].x + self.tetromino_size * 2 if dirNum == -1 else self.block_list[3].x - self.tetromino_size, self.block_list[3].y + self.tetromino_size * 2 if dirNum == 1 else self.block_list[3].y + self.tetromino_size, self.tetromino_size, self.tetromino_size),
            ],
            [
                Block(self.color, self.block_list[0].x + self.tetromino_size * 2 if dirNum == -1 else self.block_list[0].x + self.tetromino_size, self.block_list[0].y + self.tetromino_size * 2 if dirNum == 1 else self.block_list[0].y - self.tetromino_size, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[1].x + self.tetromino_size if dirNum == -1 else self.block_list[1].x, self.block_list[1].y + self.tetromino_size if dirNum == 1 else self.block_list[1].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[2].x - self.tetromino_size if dirNum == 1 else self.block_list[2].x, self.block_list[2].y + self.tetromino_size if dirNum == -1 else self.block_list[2].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[3].x - self.tetromino_size * 2 if dirNum == 1 else self.block_list[3].x - self.tetromino_size, self.block_list[3].y + self.tetromino_size * 2 if dirNum == -1 else self.block_list[3].y - self.tetromino_size, self.tetromino_size, self.tetromino_size),
            ],
            [
                Block(self.color, self.block_list[0].x - self.tetromino_size * 2 if dirNum == 1 else self.block_list[0].x + self.tetromino_size, self.block_list[0].y + self.tetromino_size * 2 if dirNum == -1 else self.block_list[0].y + self.tetromino_size, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[1].x - self.tetromino_size if dirNum == 1 else self.block_list[1].x, self.block_list[1].y + self.tetromino_size if dirNum == -1 else self.block_list[1].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[2].x - self.tetromino_size if dirNum == -1 else self.block_list[2].x, self.block_list[2].y - self.tetromino_size if dirNum == 1 else self.block_list[2].y, self.tetromino_size, self.tetromino_size),
                Block(self.color, self.block_list[3].x - self.tetromino_size * 2 if dirNum == -1 else self.block_list[3].x + self.tetromino_size, self.block_list[3].y - self.tetromino_size * 2 if dirNum == 1 else self.block_list[3].y - self.tetromino_size, self.tetromino_size, self.tetromino_size),
            ],
        ]
        
        self.block_list = self.rotation_list[self.rotInd]
        
        
    def createBlockList(self):
        self.block_list = [
            Block(self.color, self.x + self.tetromino_size * 3 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 4 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 5 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
            Block(self.color, self.x + self.tetromino_size * 6 + self.offset, self.y + self.offset, self.tetromino_size, self.tetromino_size),
        ]