import pygame
pygame.init()


class Window:
    def __init__(self, name:str, width:int, height:int, fps:int):
        self.name = name
        self.width = width
        self.height = height
        self.fps = fps
        
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        
        
    def draw(self) -> None:
        pygame.display.update()
