import pygame
import sys
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, RED, FPS, CART_COOLDOWN_TIME
import config
from sprite_setup import setup_sprites
from catapult import Catapult
from projectile import Projectile
from wall import Wall
from cart import Cart
from ground import Ground

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

sprites = setup_sprites()

all_sprites = pygame.sprite.Group()  
projectiles = pygame.sprite.Group()
carts = pygame.sprite.Group()

# Create instances
catapult = Catapult(sprites["catapult_image"], sprites["dwarf_image"])
wall = Wall(sprites["wall_image"])
cart_spawn_cooldown = 0
ground = Ground()

all_sprites.add(catapult)
all_sprites.add(wall)
all_sprites.add(ground)

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    if(cart_spawn_cooldown > 0):
        cart_spawn_cooldown -=1

    screen.blit(sprites["background_image"], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed_time = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_held_duration = pygame.time.get_ticks() - mouse_pressed_time
            catapult.launch_projectile(all_sprites, projectiles, mouse_held_duration)

    all_sprites.update()
    catapult.draw_cooldown(screen)
    mouse_pos = pygame.mouse.get_pos()

    all_sprites.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), catapult.rect.center, mouse_pos, 2)

    for cart in carts:
        cart.draw_speed(screen)
        cart.draw_ttl(screen)

    catapult.aim(mouse_pos)
    for projectile in projectiles:
        if wall.has_collided_with(projectile.rect):
            projectile.kill()
        if ground.has_collided_with(projectile.rect):
            projectile.on_ground = True

    if(cart_spawn_cooldown == 0 ):
        new_cart = Cart(velocity=random.uniform(1.0, 2.5), goblin_image=sprites["goblin_image"],
                        goblin_slow_image=sprites['goblin_slow_image'], explosion_image=sprites['explosion_image'],
                        wall_instance=wall)
        all_sprites.add(new_cart)
        carts.add(new_cart)
        cart_spawn_cooldown = CART_COOLDOWN_TIME

    cart_dwarf_collision = pygame.sprite.groupcollide(carts, projectiles, False, False)
    for current_cart, collided_projectiles in cart_dwarf_collision.items():
        for current_projectile in collided_projectiles:
            current_cart.add_dwarf(current_projectile)

    for i in range(config.lives):
        screen.blit(sprites['life_image'], (10 + i * sprites['life_image'].get_width(), 10))

    #  game over screen
    if config.lives <= 0:
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 36)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(3000)  # Pause for 3 seconds 
        running = False

    pygame.display.flip()
    clock.tick(FPS)
