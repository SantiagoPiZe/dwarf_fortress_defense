import pygame
import math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN, CATAPULT_COOLDOWN_TIME
from projectile import Projectile

class Catapult(pygame.sprite.Sprite):
    def __init__(self, catapult_image, dwarf_image):
        super().__init__()
        self.original_image = catapult_image
        self.dwarf_image = dwarf_image
        self.image = pygame.transform.rotate(pygame.transform.scale(self.original_image, (50, 50)), -90)
        self.rect = self.image.get_rect()
        self.rect.right = SCREEN_WIDTH - 10
        self.rect.bottom = SCREEN_HEIGHT - 75
        self.cooldown = 0
        self.min_angle = 90
        self.max_angle = 180
        self.angle = 90
        self.font = pygame.font.Font(None, 24)

    def update(self):
        self.current_sprite = 1
        if self.cooldown > 0:
            self.cooldown -= 1

    def draw_cooldown(self, screen):
        cooldown_percentage = self.cooldown / CATAPULT_COOLDOWN_TIME
        pygame.draw.rect(screen, GREEN, (self.rect.x, self.rect.y - 20, self.rect.width * cooldown_percentage, 10))
        cooldown_text = self.font.render(str(self.cooldown), True, (255, 255, 255))
        screen.blit(cooldown_text, (self.rect.x, self.rect.y - 40))

    def launch_projectile(self, all_sprites, projectiles, mouse_held_duration):
        if self.cooldown == 0:
            initial_speed = 5 + mouse_held_duration // 100
            projectile = Projectile(self.rect.centerx, self.rect.centery, self.angle, initial_speed, self.dwarf_image)
            all_sprites.add(projectile)
            projectiles.add(projectile)
            self.cooldown = CATAPULT_COOLDOWN_TIME

    def aim(self, mouse_pos):
        dx = mouse_pos[0] - self.rect.centerx
        dy = mouse_pos[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        self.angle = max(self.min_angle, min(self.max_angle, angle))
        if(angle > 0 and angle < 90):
            self.image = pygame.transform.rotate(pygame.transform.scale(self.original_image, (50, 50)), -70)
        else:
            if(angle < 0):
                self.image = pygame.transform.rotate(pygame.transform.scale(self.original_image, (50, 50)), 20)
            else:
                self.image = pygame.transform.rotate(pygame.transform.scale(self.original_image, (50, 50)), 200 + self.angle)