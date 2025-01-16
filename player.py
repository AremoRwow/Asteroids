import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.timer = 0

        #Selecting an image for our player
        self.image = pygame.image.load("images/Goliath.png")
        self.image = pygame.transform.scale(self.image, (40, 56))

        #Creating a rectangle for our image
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)



    #This is old now, we're using an image instead of a triangle for the Player
    '''def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]'''
    
    def rotate_image(self):
        adjusted_angle = -self.rotation - 180
        rotated_image = pygame.transform.rotate(self.image, adjusted_angle)
        self.rect = rotated_image.get_rect(center = self.position)
        return rotated_image

    def draw (self, screen):
        # pygame.draw.polygon(screen, "white", self.triangle(), width = 2) This is the draw method that goes with the triangle method
        rotated_image = self.rotate_image()
        screen.blit(rotated_image, self.rect)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = (self.position.x, self.position.y)

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        #Updating rectangle coordinates to make it move with the player
        self.rect.center = (self.position.x, self.position.y)
    
    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        keys = pygame.key.get_pressed()

        new_shot = Shot(self.position, SHOT_RADIUS)
  
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED

        return new_shot