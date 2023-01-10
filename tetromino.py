import pygame
from time import sleep
pygame.init()


class Tetromino:
    color = ()
    block_list = []
    rotation_list = []
    rotInd = 0
    
    
    def __init__(self, x, y, tetromino_size, offset):
        self.x = x
        self.y = y
        self.tetromino_size = tetromino_size
        self.offset = offset // 2
        

    """Movement"""
    def fall(self, padY, frameHeight, speed, spawnNewTetromino, spawnList):
        while(not self.grounded(padY, frameHeight) and not self.collided(spawnList, self.bottomSideCollsion)):
            self.moveBlock("down")
            sleep(speed)
        else:
            spawnNewTetromino()
            

    def move(self, button, xPos, frameWidth, spawnList):
        if button == 13 and not self.leftWall(xPos) and not self.collided(spawnList, self.leftSideCollsion):
            self.moveBlock("left")
        if button == 14 and not self.rightWall(xPos, frameWidth) and not self.collided(spawnList, self.rightSideCollsion):
            self.moveBlock("right")
            
            
    def moveBlock(self, direction):
        for block in self.block_list:
            block.moveDirection(self.tetromino_size, direction)
    
    
    """Rotation"""
    def rotate(self, button, spawnList, xPos, padY):
        if button == 9:
            self.canRotate(-1, spawnList, xPos, padY)
        if button == 10:
            self.canRotate(1, spawnList, xPos, padY)
            
    
    def canRotate(self, newInd, spawnList, xPos, padY):
        self.rotInd = self.rotInd + (newInd)
        self.changeRotInd()
        if(not self.rotationCollision(spawnList, self.rotateBlocks(newInd))
           and not self.wallCollision(xPos, padY)):
            self.block_list = self.rotateBlocks(newInd)
        else:
            self.rotInd = self.rotInd + (-(newInd))
            self.changeRotInd()
            
            
    def wallCollision(self, xPos, padY):
        for this_block in self.rotation_list[self.rotInd]:
            if (this_block.x < xPos or this_block.x + self.tetromino_size > xPos + self.tetromino_size * 11 or
                this_block.y < padY or this_block.y + self.tetromino_size > padY + self.tetromino_size * 20):
                    return True
        return False
            
            
    def rotationCollision(self, spawnList, rotation_list):
        for ind in range(0, len(spawnList) - 1):
            for other_block in spawnList[ind].block_list:
                for this_block in rotation_list:
                    if (this_block.x == other_block.x and this_block.y == other_block.y):
                        return True
        return False
            
            
    def changeRotInd(self):
        if self.rotInd == -1:
            self.rotInd = 3
        elif self.rotInd == 4:
            self.rotInd = 0


    def rotateBlocks(self, dirNum):
        pass
    
    
    """Collsion with the game board""" 
    def grounded(self, padY, frameHeight):
        for block in self.block_list:
            if block.y + self.tetromino_size > padY + frameHeight:
                return True
        return False
    
    
    def leftWall(self, xPos):
        for block in self.block_list:
            if block.x - self.tetromino_size < xPos:
                return True
        return False
    
    
    def rightWall(self, xPos, frameWidth):
        for block in self.block_list:
            if block.x + self.tetromino_size > xPos + frameWidth:
                return True
        return False
    
    
    """Collsion with other tetrominoes"""
    def collided(self, spawnList, site):
        for ind in range(0, len(spawnList) - 1):
            for other_block in spawnList[ind].block_list:
                for this_block in self.block_list:
                    if site(this_block, other_block):
                        return True
        return False
                
            
    def bottomSideCollsion(self, this_block, other_block):
        if this_block.y + self.tetromino_size >= other_block.y and this_block.x == other_block.x and not this_block.y >= other_block.y + self.tetromino_size:
            return True
        return False
    
    
    def leftSideCollsion(self, this_block, other_block):
        if this_block.x == other_block.x + self.tetromino_size and this_block.y == other_block.y:
            return True
        return False


    def rightSideCollsion(self, this_block, other_block):
        if this_block.x + self.tetromino_size == other_block.x and this_block.y == other_block.y:
            return True
        return False
    
    
    """Game over"""    
    def gameOver(self, padY):
        for block in self.block_list:
            if block.y - self.offset == padY:
                return True
        return False
    
    
    """Drawing the tetromino"""
    def draw(self, win):
        for block in self.block_list:
            pygame.draw.rect(win, block.color, block.rect)
