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
                main_menu.chooseMode(pygame.mouse.get_pos())
        
        WIN.draw(main_menu)
        

if __name__ == "__main__":
    main()
