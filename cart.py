import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import config

class Cart(pygame.sprite.Sprite):
    def __init__(self, velocity, goblin_image, wall_instance):
        super().__init__()
        self.image =  pygame.transform.scale(goblin_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = SCREEN_HEIGHT - 55
        self.speed = velocity
        self.start_time = pygame.time.get_ticks() / 1000
        self.weight = 5
        self.wall_instance = wall_instance

    def update(self):
        t = pygame.time.get_ticks() / 1000 - self.start_time
        # MRU: x = x0 + v * t
        self.has_collided_with_wall()
        self.rect.x = self.speed * t

    
    def add_dwarf(self, dwarf):
        #wtot * stot = m1 * s1 + m2* s2
        prev_weight = self.weight
        self.weight += dwarf.weight
        self.speed = (prev_weight * self.speed + dwarf.vx * dwarf.weight) / self.weight
        dwarf.kill()
    
    def has_collided_with_wall(self):
        if self.rect.colliderect(self.wall_instance):
            config.lives -= 1
            self.kill()
