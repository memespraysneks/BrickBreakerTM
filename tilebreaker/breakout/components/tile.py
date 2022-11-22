import pygame
from .sprite import MySprite
import random


class Tile(MySprite):
    """Tile - meant to be hit with the ball"""

    def __init__(self, *args, color=random.randint(100,200), width=100, height=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
