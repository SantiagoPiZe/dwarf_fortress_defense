import pygame

import config
from config import SCREEN_HEIGHT, RED, BLACK


class Cart(pygame.sprite.Sprite):
    def __init__(self, velocity, goblin_image, wall_instance):
        super().__init__()
        self.image = pygame.transform.scale(goblin_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = SCREEN_HEIGHT - 55
        self.speed = velocity
        self.start_time_in_sec = pygame.time.get_ticks() / 1000
        self.weight = 5
        self.wall_instance = wall_instance
        self.ttl = 2500
        self.x0 = 0
        self.font = pygame.font.Font(None, 24)


    def update(self):
        t = pygame.time.get_ticks() / 1000 - self.start_time_in_sec
        # MRU: x = x0 + v * t
        self.has_collided_with_wall()
        self.rect.x = self.x0 + self.speed * t
        self.ttl -= 1
        if self.ttl <= 0:
            self.kill()

    def draw_speed(self, screen):
        speed_text = self.font.render(str( "%.2f" % self.speed), True, (255, 255, 255))
        screen.blit(speed_text, (self.rect.x, self.rect.y - 20))

    def draw_ttl(self, screen):
        ttl_percentage = self.ttl / 2500
        black_surface = pygame.Surface((self.rect.width, 10))
        black_surface.fill(BLACK)
        black_surface.set_alpha(128)
        screen.blit(black_surface, (self.rect.x, self.rect.y))
        
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y, self.rect.width * ttl_percentage, 10))


    def add_dwarf(self, dwarf):
        # Conservación del momento lineal: p_before = p_after
        # p_before = m1 * v1 + m2 * v2
        # p_after = (m1 + m2) * v_after
        # v_after = (m1 * v1 + m2 * v2) / (m1 + m2)
        total_momentum_before = self.weight * self.speed + dwarf.weight * dwarf.vx
        total_weight_after = self.weight + dwarf.weight
        self.speed = total_momentum_before / total_weight_after
        self.weight = total_weight_after
        self.x0 = self.rect.x
        self.start_time_in_sec = pygame.time.get_ticks() / 1000
        dwarf.kill()

    def has_collided_with_wall(self):
        if self.rect.colliderect(self.wall_instance):
            config.lives -= 1
            self.kill()
