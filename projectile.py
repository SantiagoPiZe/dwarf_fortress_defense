import pygame
import math
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, initial_speed, dwarf_image):
        super().__init__()
        self.image = pygame.transform.scale(dwarf_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)  
        self.speed = initial_speed
        self.gravity = 0.5 
        self.vx = self.speed * math.cos(self.angle)  
        self.vy = -self.speed * math.sin(self.angle)
        self.weight = random.uniform(0.1, 0.5)
        self.on_ground = False

    def update(self):
        self.rect.x += self.vx
        if(not self.on_ground):
            self.vy += self.gravity
            self.rect.y += self.vy
        else:
            self.vy = 0
            self.vx = -1
            if( -1 < self.vx < 1):
                self.vx = -1

        if not pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT).contains(self.rect):
            self.kill()