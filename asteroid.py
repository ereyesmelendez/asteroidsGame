import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color, velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = velocity
        
    def draw(self, surface):
        # Draw the asteroid (represented as a circle here)
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[0] * dt
        