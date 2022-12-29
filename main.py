import pygame

from window import Window

pygame.init()


WIN = Window("Tetris", 800, 600, 60)


def main():
    run = True
    
    while(run):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        WIN.draw()
        

if __name__ == "__main__":
    main()
