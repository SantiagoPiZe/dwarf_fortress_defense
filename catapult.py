import pygame
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN, CATAPULT_COOLDOWN_TIME
from projectile import Projectile

class Catapult(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH - 10
        self.rect.bottom = SCREEN_HEIGHT - 50
        self.cooldown = 0
        self.min_angle = 90
        self.max_angle = 180 
        self.angle = 90 

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def launch_projectile(self, all_sprites, projectiles, mouse_held_duration):
        if self.cooldown == 0:
            initial_speed = 5 + mouse_held_duration // 100
            projectile = Projectile(self.rect.centerx, self.rect.centery, self.angle, initial_speed)
            all_sprites.add(projectile)
            projectiles.add(projectile)
            self.cooldown = CATAPULT_COOLDOWN_TIME

    def aim(self, mouse_pos):
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        self.angle = max(self.min_angle, min(self.max_angle, angle))
