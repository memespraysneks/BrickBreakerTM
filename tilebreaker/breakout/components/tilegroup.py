import pygame
from .tile import Tile
from random import randint

class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30, level=1):
        super().__init__()
        tile_color = randint(100,200)
        level_dictionary = {1:[[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[0,1,1,1,1,1,0],[0,0,1,1,1,0,0],[0,0,0,1,0,0,0]]}
        tile_layout = level_dictionary[level]
        for y in range(len(tile_layout)):
            for x in range(len(tile_layout[y])):
                if tile_layout[y][x] == 1:    
                    tile = Tile(color=tile_color,width=tile_width, height=tile_height)
                    tile.move_to(x*105+25, y*50)
                    self.add(tile)
