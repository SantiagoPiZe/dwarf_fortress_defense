import pygame
import math
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, initial_speed, dwarf_image):
        super().__init__()
        self.image = pygame.transform.scale(dwarf_image, (40, 40))
        self.rect = self.image.get_rect()

        #Convert pixels to meters
        self.initial_x = x / 50 # 1 mt = 50 px
        self.initial_y = y / 50 # 1 mt = 50 px

        self.rect.center = (x, y)
        self.angle = math.radians(180 - angle)
        self.speed = initial_speed 
        self.gravity = 9.8
        self.vx = -self.speed * math.cos(self.angle)
        self.vy = -self.speed * math.sin(self.angle)
        self.weight = random.uniform(1, 3)
        self.on_ground = False
        self.start_time_in_sec = pygame.time.get_ticks() / 1000

    def update(self):
        current_time = pygame.time.get_ticks() / 1000
        t = current_time - self.start_time_in_sec  

        # Calculate the new position
        dx = self.vx * t + self.initial_x
        dy = (0.5 * self.gravity * t ** 2) + (self.vy * t) + self.initial_y

        # Reverse conversion from meters to pixels
        self.rect.x = dx * 50
        if(self.on_ground is False):
            self.rect.y = dy * 50

        if not pygame.Rect(0, 0, SCREEN_WIDTH + self.rect.width, SCREEN_HEIGHT + self.rect.height).contains(self.rect):
            self.kill()