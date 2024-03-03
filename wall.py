import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, SCREEN_HEIGHT - 500)) 
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_WIDTH - 100
        self.rect.bottom = SCREEN_HEIGHT - 50

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
