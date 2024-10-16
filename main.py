import pygame
from constants import *
from player import Player

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
    
    # Player Object Spawn
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    
    # Infinite loop, keeps the game running until event has been triggered.
    while True:
        
        
        # Listen for event, such as QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black and draw the player
        screen.fill("black")
        player.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # limit frame rate to 60 FPS
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()