import pygame
import sys
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, FPS, CART_COOLDOWN_TIME
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
catapult = Catapult(all_sprites)
wall = Wall()
cart_entity = Cart(velocity=random.randint(15, 25))
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
            catapult.launch_projectile(mouse_held_duration)

    all_sprites.update()

    for projectile in projectiles:
        if wall.is_collided_with(projectile):
            projectile.kill()

    mouse_pos = pygame.mouse.get_pos()

    all_sprites.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), catapult.rect.center, mouse_pos, 2)

    catapult.aim(mouse_pos)

    for projectile in projectiles:
        if wall.has_collided_with(projectile.rect):
            projectile.kill()
        if ground.has_collided_with(projectile.rect):
            projectile.on_ground = True

    if(cart_spawn_cooldown == 0 ):
        new_cart = Cart(velocity=random.randint(15, 25), goblin_image=sprites["goblin_image"])
        all_sprites.add(new_cart)
        carts.add(new_cart)
        cart_spawn_cooldown = CART_COOLDOWN_TIME

    cart_dwarf_collision = pygame.sprite.groupcollide(carts, projectiles, False, False)
    for current_cart, collided_projectiles in cart_dwarf_collision.items():
        for current_projectile in collided_projectiles:
            current_cart.add_dwarf(current_projectile)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
