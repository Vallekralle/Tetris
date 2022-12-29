import pygame

from window import Window
from menu import Menu

pygame.init()


WIN = Window("Tetris", 1400, 800, 60)
main_menu = Menu(WIN.width, WIN.height)


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
                        onePlayerMode()
                    case 2:
                        twoPlayerMode()
        
        WIN.draw(main_menu)
        
        
def onePlayerMode():
    main_menu.deactivate()
    

def twoPlayerMode():
    main_menu.deactivate()
        

if __name__ == "__main__":
    main()
