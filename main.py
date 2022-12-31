import pygame

from window import Window
from menu import Menu
from board import Board

pygame.init()


WIN = Window("Tetris", 1400, 800, 60)
main_menu = Menu(WIN.width, WIN.height)
game_board = object


def main(): 
    run = True
    
    while(run):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                match main_menu.chooseMode(pygame.mouse.get_pos()):
                    case 1:
                        createBoard(10, 2, 1)
                    case 2:
                        createBoard(10, 2, 2)
        
        WIN.draw(main_menu, game_board)
        

def createBoard(padY:int, rectSize:int, amount:int):
    global game_board
    game_board = Board(WIN.width, WIN.height, padY, rectSize, amount)
    main_menu.deactivate()
        

if __name__ == "__main__":
    main()
