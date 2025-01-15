import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    #Game loop starts here, the for loop is here to kill upon closing game window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #This fills the screen with a color, black in this case
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        #locks the game at 60 fps
        dt = clock.tick(60) / 1000

        #rotates the player around when keys defined in update method (player.py) are pressed
        player.update(dt)
        
    

    

if __name__ == "__main__":
    main()
