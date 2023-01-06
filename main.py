import pygame
from win11toast import toast

from window import Window
from menu import Menu
from board import Board

pygame.init()


WIN = Window("Tetris", 1400, 800, 60)
main_menu = Menu(WIN.width, WIN.height)
game_board = object
joysticks = []


def main():
    initializeJoysticks()
    run = True
    
    while(run):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                match main_menu.chooseMode(pygame.mouse.get_pos()):
                    case 1:
                        if not toastNotification(1):
                            createBoard(10, 2, 1)
                    case 2:
                        if not toastNotification(2):
                            createBoard(10, 2, 2)
                        
            if event.type == pygame.JOYBUTTONDOWN:
                if not main_menu.active:
                    joyEventHandler()
        
        WIN.draw(main_menu, game_board)
        
        
def toastNotification(controllerCount:int):
    if len(joysticks) < controllerCount:
        msg = "You need " + str(controllerCount) + " controller/s connected!"
        toast("[Controller Error]",
               msg)
        return True
    return False


def createBoard(padY:int, rectSize:int, amount:int):
    global game_board
    
    game_board = Board(WIN.width, WIN.height, padY, rectSize, amount)
    main_menu.deactivate()


def initializeJoysticks():
    global joysticks
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
    
def joyEventHandler():
    global joysticks

    if joysticks[0].get_button(9): # left bumper
        game_board.tetromino_spawner[0].joyStickInput(9)
    if joysticks[0].get_button(10): # right bumper
        game_board.tetromino_spawner[0].joyStickInput(10)
    if joysticks[0].get_button(13): # left D-pad
        game_board.tetromino_spawner[0].joyStickInput(13)
    if joysticks[0].get_button(14): # right D-pad
        game_board.tetromino_spawner[0].joyStickInput(14)
    
    if len(joysticks) == 2:
        if joysticks[1].get_button(9): # left bumper
            game_board.tetromino_spawner[1].joyStickInput(9)
        if joysticks[1].get_button(10): # right bumper
            game_board.tetromino_spawner[1].joyStickInput(10)
        if joysticks[1].get_button(13): # left D-pad
            game_board.tetromino_spawner[1].joyStickInput(13)
        if joysticks[1].get_button(14): # right D-pad
            game_board.tetromino_spawner[1].joyStickInput(14)
    

if __name__ == "__main__":
    main()
