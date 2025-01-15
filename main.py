import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Defining the screen and the clock with pygame, and using variables for the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #Groups creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #adding player CLASS to both groups
    Player.containers = (updatable, drawable)

    #Player positionning on the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0    


    #Game loop starts here, the for loop is here to kill upon closing game window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        #This fills the screen with a color, black in this case
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)


        #This line updates the game window
        pygame.display.flip()

        #locks the game at 60 fps
        dt = clock.tick(60) / 1000

        
        
    

    

if __name__ == "__main__":
    main()
