import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FPS
from catapult import Catapult
from projectile import Projectile
from wall import Wall

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()  
projectiles = pygame.sprite.Group()


# Create instances
catapult = Catapult(all_sprites)
wall = Wall()
all_sprites.add(catapult)
all_sprites.add(wall)

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed_time = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_held_duration = pygame.time.get_ticks() - mouse_pressed_time
            catapult.launch_projectile(mouse_held_duration)

    all_sprites.update()

    for projectile in projectiles:
        if wall.is_collided_with(projectile):
            projectile.kill()

    mouse_pos = pygame.mouse.get_pos()

    all_sprites.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), catapult.rect.center, mouse_pos, 2)

    catapult.aim(mouse_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
