import pygame
from random import randint

from otetromino import Otetromino
from ztetromino import Ztetromino
from stetromino import Stetromino
from ttetromino import Ttetromino
from itetromino import Itetromino
from ltetromino import Ltetromino
from jtetromino import Jtetromino

pygame.init()


class Spawner:
    def __init__(self, x, y, tetromino_size, offset):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.offset = offset
        
        self.spawnList = []
        
        self.tetrominoes = [
            Otetromino(self.x, self.y, self.tetromino_size, offset),
            Ztetromino(self.x, self.y, self.tetromino_size, offset),
            Stetromino(self.x, self.y, self.tetromino_size, offset),
            Ttetromino(self.x, self.y, self.tetromino_size, offset),
            Itetromino(self.x, self.y, self.tetromino_size, offset),
            Ltetromino(self.x, self.y, self.tetromino_size, offset),
            Jtetromino(self.x, self.y, self.tetromino_size, offset)
        ]
        
        self.spawnTetromino()
        
        
    def spawnTetromino(self):
        self.spawnList.append(self.tetrominoes[randint(0, len(self.tetrominoes) - 1)])
