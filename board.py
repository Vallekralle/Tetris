import pygame
pygame.init()


class Board():
    frame_list = []
    
    
    def __init__(self, win_width, win_height, padY, rectSize, amount):
        self.win_width = win_width
        self.win_height = win_height
        self.padY = padY
        self.amount = amount
        self.rectSize = rectSize
        
        self.tetromino_height = (self.win_height - self.padY) // 20
        
        self.frameWidth = self.tetromino_height * 10
        self.frameHeight = self.tetromino_height * 20
        
        self.createFrame()
        

    def createFrame(self):
        rect_list = []
        x = ((self.win_width // 2) // self.amount) - (self.frameWidth // 2)
        y = self.padY
        
        for i in range(1, self.amount + 1):
            # Background for the grid
            self.frame_list.insert(0, [pygame.Rect(x, y, self.frameWidth, self.frameHeight)])
            
            # Creating the grid    
            for horizontal in range(21):
                rect_list.append(pygame.Rect(x, y, self.frameWidth, self.rectSize))
                y += self.tetromino_height
            y = self.padY
            
            for vertical in range(11):
                rect_list.append(pygame.Rect(x, y, self.rectSize, self.frameHeight))
                x += self.tetromino_height            
            
            x = (self.win_width // 2 - self.frameWidth // 2) + self.win_width // 4
            
        self.frame_list.append(rect_list)
                
        
    def draw(self, win):
        for ind, frame in enumerate(self.frame_list):
            for rect in frame:
                if ind <= self.amount - 1:
                    pygame.draw.rect(win, (255, 255, 255), rect)
                else:
                    pygame.draw.rect(win, (0, 0, 0), rect)
