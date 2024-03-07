import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, 80), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT

    def has_collided_with(self, sprite):
        return self.rect.colliderect(sprite)
