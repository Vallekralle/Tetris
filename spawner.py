import pygame
from random import randint

from otetromino import Otetromino

pygame.init()


class Spawner:
    def __init__(self, x, y, tetromino_size, xOffset, yOffset):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.xOffset = xOffset
        self.yOffset = yOffset
        
        self.spawnList = []
        
        self.tetrominoes = [
            Otetromino(self.x, self.y, self.tetromino_size, xOffset, yOffset),
        ]
        
        self.spawnTetromino()
        
        
    def spawnTetromino(self):
        self.spawnList.append(self.tetrominoes[randint(0, len(self.tetrominoes) - 1)])
