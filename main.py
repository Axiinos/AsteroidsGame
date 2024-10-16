import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    
    # Initialize pygame
    pygame.init()
    
    # Get time object
    clock = pygame.time.Clock()
    
    # Delta time
    dt = 0
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH,
                                      SCREEN_HEIGHT))
    

    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Player membership
    Player.containers = (updatable, drawable)
    
    # Asteroid Membership
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Asteroid Field Membership
    AsteroidField.containers = (updatable)
    
    # Player Object Spawn
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    
    # Asteroid Field Object Spawn
    asteroid_field = AsteroidField()
    
    # Infinite loop, keeps the game running until event has been triggered.
    while True:
        
        # Listen for event, such as QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black and draw the player
        screen.fill("black")
        
        # Update members of the updatable group
        for obj in updatable:
            obj.update(dt)
        
        # Update members of the drawable group
        for obj in drawable:
            obj.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()