import pygame
pygame.init()


class Board():
    frame_list = []
    
    
    def __init__(self, win_width, win_height, padX, padY, amount):
        self.win_width = win_width
        self.win_height = win_height
        self.padX = padX
        self.padY = padY
        self.amount = amount
        
        self.tetromino_height = (self.win_height - self.padY) // 20
        
        self.frameWidth = self.tetromino_height * 10
        self.frameHeight = self.tetromino_height * 20
        self.rectSize = 2
        
        self.createFrame()
        

    def createFrame(self):
        rect_list = []
        x = self.win_width // 2 // self.amount - self.frameWidth // 2
        y = self.padY // 2
        
        for i in range(1, self.amount + 1):
            for horizontal in range(21):
                rect_list.append(pygame.Rect(x, y, self.frameWidth, self.rectSize))
                y += self.tetromino_height
            y = self.padY // 2
            
            for vertical in range(11):
                rect_list.append(pygame.Rect(x, y, self.rectSize, self.frameHeight))
                x += self.tetromino_height
            x = self.win_width // 2 - self.frameWidth // 2
            
            x += self.win_width // 4
            
        self.frame_list.append(rect_list)
                
        
    def draw(self, win):
        for frame in self.frame_list:
            for rect in frame:
                pygame.draw.rect(win, (0, 0, 0), rect)
