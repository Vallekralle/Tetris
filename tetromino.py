import pygame
pygame.init()


class Tetromino:    
    def move(block_list, tetromino_size):
        for block in block_list:
            block.y += tetromino_size
            
    
    def draw(win, block_list):
        for block in block_list:
            pygame.draw.rect(win, block.color, (block.x, block.y, block.width, block.height))
