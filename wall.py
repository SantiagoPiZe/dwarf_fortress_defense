import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE


class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_image):
        super().__init__()
        self.image = pygame.transform.scale(wall_image, (30, SCREEN_HEIGHT - 450))
        self.rect = self.image.get_rect()
        self.rect.left = SCREEN_WIDTH - 110
        self.rect.bottom = SCREEN_HEIGHT

    def has_collided_with(self, sprite):
        return self.rect.colliderect(sprite)
