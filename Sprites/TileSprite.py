import pygame.sprite
from Sprites.SpriteMapper import TileMapper


class TileSprite(pygame.sprite.Sprite):
    def __init__(self, image_key, coordinate=(0,0)):
        super().__init__()
        self.image = TileMapper.get(image_key)
        self.image = pygame.transform.scale(self.image, (100,100)).convert_alpha()
        self.rect = self.image.get_rect(center=coordinate)