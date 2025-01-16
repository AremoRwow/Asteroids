import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    #Initialise pygame
    pygame.init()
    #Initialise fonts to display text
    pygame.font.init()
    font = pygame.font.Font("expressway rg.otf", 20)

    #We define a background image we want to use instead of having a black window
    background_image = pygame.image.load("images/1-2.jpg")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #This scales the image to the screen resolution, because 1-2.jpg has a different resolution

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Defining the screen and the clock with pygame, and using variables for the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #Groups creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #adding classes to groups to iterate on them inside the game loop
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    #Player positionning on the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    score = 0


    #Game loop starts here, the for loop is here to kill upon closing game window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collision(player) == True:
                print("Game Over !")
                sys.exit()
            for bullet in shots:
                if bullet.collision(obj) == True:
                    bullet.kill()
                    obj.split()
                    score += ASTEROID_REWARD
        
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        #This fills the screen with a color, black in this case, NOT IN USE because we now have a background image
        #screen.fill("1-2.jpg")
        screen.blit(background_image, (0,0))

        for obj in drawable:
            obj.draw(screen)

        #This creates a text and reders it using a string and a color    
        text_score = font.render(f"SCORE: {score}", True, "white")    
        text_width = text_score.get_width()                         #Now we get the width of the text to make sure we place it in the center of the screen
        screen.blit(text_score, ((SCREEN_WIDTH - text_width) / 2, 10)) #And we use the width to center the text, as well as a y value to get it at the top of the screen

        #This line updates the game window
        pygame.display.flip()

        #locks the game at 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
