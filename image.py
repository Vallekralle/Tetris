import pygame
pygame.init()


class Image:
    def __init__(self, x:int, y:int, width:int, height:int, path:str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = path
        
        self.loadImg()
        
    
    def loadImg(self):
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        
    def pressed(self, mouse_pos):
        if(self.x <= mouse_pos[0] <= self.x + self.width and
           self.y <= mouse_pos[1] <= self.y + self.height):
            return True
        return False
