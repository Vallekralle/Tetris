import pygame
from random import choice
from threading import Thread

from otetromino import Otetromino
from ztetromino import Ztetromino
from stetromino import Stetromino
from ttetromino import Ttetromino
from itetromino import Itetromino
from ltetromino import Ltetromino
from jtetromino import Jtetromino

pygame.init()


class Spawner:
    def __init__(self, x, y, tetromino_size, offset, padY, frameHeight):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.offset = offset
        self.padY = padY
        self.frameHeight = frameHeight
        
        self.spawnList = []
        
        self.tetrominoes = [
            Otetromino(self.x, self.y, self.tetromino_size, offset),
            Ztetromino(self.x, self.y, self.tetromino_size, offset),
            Stetromino(self.x, self.y, self.tetromino_size, offset),
            Ttetromino(self.x, self.y, self.tetromino_size, offset),
            Itetromino(self.x, self.y, self.tetromino_size, offset),
            Ltetromino(self.x, self.y, self.tetromino_size, offset),
            Jtetromino(self.x, self.y, self.tetromino_size, offset),
        ]
        
        self.spawnTetromino()
        
        
    def spawnTetromino(self):
        self.spawnList.append(choice(self.tetrominoes))
        thread = Thread(target=self.spawnList[-1].fall,
                        args=[self.padY, self.tetromino_size * 20, 0.3, self.spawnTetromino, self.spawnList])
        thread.start()
        
    
    def dPadInput(self, button:int):
        thread = Thread(target=self.spawnList[-1].move,
                        args=[button, self.x, self.tetromino_size * 10, self.spawnList])
        thread.start()
    
    
    def xInput(self):
        pass
