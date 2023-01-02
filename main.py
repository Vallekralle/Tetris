import pygame

from window import Window
from menu import Menu
from board import Board

pygame.init()


WIN = Window("Tetris", 1400, 800, 60)
main_menu = Menu(WIN.width, WIN.height)
game_board = object
joysticks = []


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
                        
            if event.type == pygame.JOYBUTTONDOWN:
                joyEventHandler()
        
        WIN.draw(main_menu, game_board)
        

def createBoard(padY:int, rectSize:int, amount:int):
    global game_board

    initializeJoysticks()
    
    game_board = Board(WIN.width, WIN.height, padY, rectSize, amount)
    main_menu.deactivate()


def initializeJoysticks():
    global joysticks
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
    
def joyEventHandler():
    global joysticks
    global game_board

    if joysticks[0].get_button(0):
        print("[Controller 1]: Pressed cross button!")
    if joysticks[0].get_button(13):
        game_board.tetromino_spawner[0].dPadInput(13)
    if joysticks[0].get_button(14):
        game_board.tetromino_spawner[0].dPadInput(14)
    
    if len(game_board.tetromino_spawner) == 2:
        if joysticks[1].get_button(0):
            print("[Controller 2]: Pressed cross button!")
        if joysticks[1].get_button(13):
            game_board.tetromino_spawner[1].dPadInput(13)
        if joysticks[1].get_button(14):
            game_board.tetromino_spawner[1].dPadInput(14)
    

if __name__ == "__main__":
    main()
