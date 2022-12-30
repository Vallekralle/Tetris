import pygame
pygame.init()


class Window:
    clock = pygame.time.Clock()
    drawing_list = []
    
    
    def __init__(self, name:str, width:int, height:int, fps:int):
        self.name = name
        self.width = width
        self.height = height
        self.fps = fps
        
        self.createWindow()
        
        
    def createWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        
        
    def draw(self, menu:object, board:object):
        self.clock.tick(self.fps)
        
        self.window.fill((255, 255, 255))
        
        if menu.active:
            menu.draw(self.window)
        else:
            board.draw(self.window)    
        
        pygame.display.update()
        
        
    def addToList(self, newList:list):
        self.drawing_list.extend(newList)
    
    
    def resetList(self):
        self.drawing_list.clear()
