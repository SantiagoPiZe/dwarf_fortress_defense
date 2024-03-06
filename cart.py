import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Cart(pygame.sprite.Sprite):
    def __init__(self, velocity, goblin_image):
        super().__init__()
        self.image =  pygame.transform.scale(goblin_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = SCREEN_HEIGHT - 55
        self.speed = velocity
        self.start_time = pygame.time.get_ticks() / 1000

    def update(self):
        t = pygame.time.get_ticks() / 1000 - self.start_time
        # MRU: x = x0 + v * t
        self.rect.x = self.speed * t