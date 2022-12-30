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
                break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                match main_menu.chooseMode(pygame.mouse.get_pos()):
                    case 1:
                        createBoard(800, 10, 1)
                    case 2:
                        createBoard(10, 10, 2)
        
        WIN.draw(main_menu, game_board)
        

def createBoard(padX:int, padY:int, amount:int):
    global game_board
    game_board = Board(WIN.width, WIN.height, padX, padY, amount)
    main_menu.deactivate()
        

if __name__ == "__main__":
    main()
