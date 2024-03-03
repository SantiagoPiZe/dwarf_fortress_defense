import pygame
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, initial_speed):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)  
        self.speed = initial_speed
        self.gravity = 0.5 
        self.vx = self.speed * math.cos(self.angle)  
        self.vy = -self.speed * math.sin(self.angle)

    def update(self):
        self.rect.x += self.vx
        self.vy += self.gravity
        self.rect.y += self.vy

        if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).contains(self.rect):
            self.kill()