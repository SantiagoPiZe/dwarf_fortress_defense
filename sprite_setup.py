import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT


def setup_sprites():
    dwarf_image = pygame.image.load("assets/dwarf.png").convert_alpha()
    goblin_image = pygame.image.load("assets/goblin.png").convert_alpha()
    wall_image = pygame.image.load("assets/wall.png").convert_alpha()
    catapult_image = pygame.image.load('assets/cannon.png').convert_alpha()
    background_image = pygame.image.load('assets/background.webp').convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    life_image = pygame.image.load('assets/life.png').convert_alpha()
    life_image = pygame.transform.scale(life_image, (50, 50))

    sprites = {
        'dwarf_image': dwarf_image,
        'goblin_image': goblin_image,
        'wall_image': wall_image,
        'catapult_image': catapult_image,
        'background_image': background_image,
        'life_image': life_image
    }

    return sprites
