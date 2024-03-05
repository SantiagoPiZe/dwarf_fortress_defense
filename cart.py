import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Cart(pygame.sprite.Sprite):
    def __init__(self, velocity):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = SCREEN_HEIGHT - 50
        self.speed = velocity
        self.start_time = pygame.time.get_ticks() / 1000

    def update(self):
        t = pygame.time.get_ticks() / 1000 - self.start_time
        # MRU: x = x0 + v * t
        self.rect.x = self.speed * t