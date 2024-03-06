import pygame
import sys
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FPS
from catapult import Catapult
from projectile import Projectile
from wall import Wall
from cart import Cart
from ground import Ground

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

dwarf_image = pygame.image.load("assets/dwarf.png").convert_alpha()
goblin_image = pygame.image.load("assets/goblin.png").convert_alpha()
wall_image = pygame.image.load("assets/wall.png").convert_alpha()
catapult_image = pygame.image.load('assets/cannon.png').convert_alpha()
background_image = pygame.image.load('assets/background.webp').convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


all_sprites = pygame.sprite.Group()  
projectiles = pygame.sprite.Group()


# Create instances
catapult = Catapult(catapult_image, dwarf_image)
wall = Wall(wall_image)
cart_entity = Cart(velocity=random.randint(15, 25), goblin_image=goblin_image)
ground = Ground()

all_sprites.add(cart_entity)
all_sprites.add(catapult)
all_sprites.add(wall)
all_sprites.add(ground)

# Main game loop
running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed_time = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_held_duration = pygame.time.get_ticks() - mouse_pressed_time
            catapult.launch_projectile(all_sprites, projectiles, mouse_held_duration)

    all_sprites.update()

    mouse_pos = pygame.mouse.get_pos()

    all_sprites.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), catapult.rect.center, mouse_pos, 2)

    catapult.aim(mouse_pos)

    for projectile in projectiles:
        if wall.has_collided_with(projectile.rect):
            projectile.kill()
        if ground.has_collided_with(projectile.rect):
            projectile.on_ground = True
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.quit()
sys.exit()
