import pygame

from image import Image

pygame.init()


class Menu():    
    def __init__(self, win_width:int, win_height:int):
        self.win_width = win_width
        self.win_height = win_height
        
        self.active = True
        
        self.createImg()
        
        
    def createImg(self):
        self.images = {
            "background": Image(0, 0, self.win_width, self.win_height, "img\\menuBackground.png"),
            "onePlayerButton": Image(self.win_width // 2 - 210, self.win_height // 2 - 30, 200, 60, "img\\onePlayerButton.png"),
            "twoPlayerButton": Image(self.win_width // 2 + 10, self.win_height // 2 - 30, 200, 60, "img\\twoPlayerButton.png")
        }
        
    
    def draw(self, win:object):
        for str, img in self.images.items():
            win.blit(img.image, (img.x, img.y))


    def chooseMode(self, mouse_pos:tuple):
        if self.active:
            if self.images["onePlayerButton"].pressed(mouse_pos):
                return 1
            elif self.images["twoPlayerButton"].pressed(mouse_pos):
                return 2
        return 0
            
    
    def deactivate(self):
        self.active = False
    