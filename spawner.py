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
        
        if len(self.spawnList) > 1:
            thread2 = Thread(target=self.spawnList[-2].gameOver,
                            args=[self.padY])
            thread2.start()
            
            thread3 = Thread(target=self.checkingLines,
                             args=[])
            thread3.start()
            
            
    """Deleting lines"""
    def checkingLines(self):
        yPos, positions = self.y + self.frameHeight, []
        
        for i in range(0, 21):
            yPos -= self.tetromino_size
            if self.positionTaken(yPos):
                self.deleteLines(yPos)
                positions.append(yPos)
        
        self.deleteStep(positions)
            
            
    def positionTaken(self, yPos):
        taken = 0
        
        for ind in range(0, len(self.spawnList) - 1):
            for block in self.spawnList[ind].block_list:
                if block.y - self.offset // 2 == yPos:
                    taken += 1

        if taken == 10:
            return True
        return False
    
    
    def deleteLines(self, yPos):
        for tetroInd in range(0, len(self.spawnList) - 1):
            for blockInd in range(len(self.spawnList[tetroInd].block_list) - 1, -1, -1):
                if self.spawnList[tetroInd].block_list[blockInd].y - self.offset // 2 == yPos:
                    self.spawnList[tetroInd].block_list.pop(blockInd)
        
    
    def deleteStep(self, positions):
        for pos in range(0, len(positions)):
            for ind in range(0, len(self.spawnList) - 1):
                for block in self.spawnList[ind].block_list:
                    if block.y < positions[pos]:
                        block.moveDirection(self.tetromino_size, "down")
        
    
    """Threads for joystick inputs"""
    def joyStickInput(self, button:int):
        if button == 9 or button == 10:
            # Rotate the current tetromino clockwise or counterclockwise
            thread1 = Thread(target=self.spawnList[-1].rotate,
                             args=[button, self.spawnList, self.x, self.padY])
            thread1.start()
            
        elif button == 13 or button == 14:
            # Move the current tetromino to the right or left
            thread2 = Thread(target=self.spawnList[-1].move,
                            args=[button, self.x, self.tetromino_size * 10, self.spawnList])
            thread2.start()
