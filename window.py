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
        
        self.window.fill((5, 175, 237))
        
        if menu.active:
            menu.draw(self.window)
        else:
            board.drawBackground(self.window)
            self.drawTetrominoes(board)
            board.drawGrid(self.window)
            
        pygame.display.update()
        
    
    def drawTetrominoes(self, board):
        for spawner in board.tetromino_spawner:
            for tetromino in spawner.spawnList: 
                for block in tetromino.block_list:
                    block.draw(self.window)
