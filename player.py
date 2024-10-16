from constants import *
from circleshape import *
from shot import Shot

# Child class of CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    # Draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        
    # Player shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_ROTATION_SPEED * dt
        
    def update(self, dt):
        
        keys= pygame.key.get_pressed()

        if self.timer == 0:
            pass
        else:
            self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
            
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
            
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
            
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                pass
            else:
                self.timer = PLAYER_SHOOT_COOLDOWN
                self.shoot()
                
            
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED