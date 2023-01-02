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
        
        
    def fall(self, padY, frameHeight, speed, spawnNewTetromino, spawnList):
        while(not self.grounded(padY, frameHeight) and not self.collided(spawnList)):
            sleep(speed)
            self.moveBlock("down")
        else:
            spawnNewTetromino()
    
                
    def grounded(self, padY, frameHeight):
        # Checks if this tetromino collided with the ground
        for block in self.block_list:
            if block.y + self.tetromino_size > padY + frameHeight:
                return True
        return False
    
    
    def collided(self, spawnList):
        # Checks if the tetromino collided with other tetrominoes
        for ind in range(0, len(spawnList) - 1):
            for other_block in spawnList[ind].block_list:
                if self.isColliding(other_block):
                    return True
        return False
                
            
    def isColliding(self, other_block):
        # Other part of the method collided()
        for this_block in self.block_list:
            if this_block.y + self.tetromino_size >= other_block.y and this_block.x == other_block.x:
                return True
        return False
    
    
    def move(self, button, xPos, frameWidth, spawnList):
        if button == 13 and not self.leftWall(xPos):
            self.moveBlock("left")
        if button == 14 and not self.rightWall(xPos, frameWidth):
            self.moveBlock("right")
            
            
    def leftWall(self, xPos):
        # Checks if the tetromino collides with the left wall
        for block in self.block_list:
            if block.x - self.tetromino_size < xPos:
                return True
        return False
    
    
    def rightWall(self, xPos, frameWidth):
        # Checks if the tetromino collides with the right wall
        for block in self.block_list:
            if block.x + self.tetromino_size > xPos + frameWidth:
                return True
        return False


    def moveBlock(self, direction):
        # Move all blocks in one direction
        for block in self.block_list:
            block.moveDirection(self.tetromino_size, direction)
        
    
    def draw(self, win):
        for block in self.block_list:
            pygame.draw.rect(win, block.color, (block.x, block.y, block.width, block.height))
