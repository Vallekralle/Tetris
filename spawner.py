import pygame
from random import choice
from threading import Thread
import copy

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
        # Create new random tetromino and let it fall
        newTetromino = copy.deepcopy(choice(self.tetrominoes))
        self.spawnList.append(newTetromino)
        thread = Thread(target=self.spawnList[-1].fall,
                        args=[self.padY, self.tetromino_size * 20, 0.3, self.spawnTetromino, self.spawnList])
        thread.start()
        
    
    def joyStickInput(self, button:int):
        if button == 9 or button == 10:
            # Rotate the current tetromino clockwise or counterclockwise
            thread1 = Thread(target=self.spawnList[-1].rotate,
                             args=[button])
            thread1.start()
            
        elif button == 13 or button == 14:
            # Move the current tetromino to the right or left
            thread2 = Thread(target=self.spawnList[-1].move,
                            args=[button, self.x, self.tetromino_size * 10, self.spawnList])
            thread2.start()
