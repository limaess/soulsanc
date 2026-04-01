import pygame as pg
import sys
import os

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
sys.path.insert(0, player_class_path)

from Player.PlayerClass import *

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.rect = pg.Rect(x, y, width, height)
        self.image = pg.Surface((width, height))
        self.image.fill(color)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pg.draw.rect(surface, (0,0,0), (self.rect), 3)

class TileMap:
    def __init__(self, tile_size, tile_map, tile_colors):
        self.tile_size = tile_size
        self.tile_map = tile_map

        self.tiles = pg.sprite.Group()

        self.tile_colors = tile_colors

    def draw(self, surface):
        for row in range(len(self.tile_map)):
            for col in range(len(self.tile_map[row])):
                tile_type = self.tile_map[row][col]

                if tile_type != 0:
                    x = col * self.tile_size
                    y = row * self.tile_size
                    color = self.tile_colors[tile_type]
                    tile = Tile(x, y, self.tile_size, self.tile_size, color)
                    tile.draw(surface)
                    self.tiles.add(tile)

    def collideright(self, tile):
        return player.collide_rectLEFT.colliderect(tile.rect)
    def collideleft(self, tile):
        return player.collide_rectRIGHT.colliderect(tile.rect)
    def collidebottom(self, tile):
        return player.collide_rectUP.colliderect(tile.rect)
    def collidetop(self, tile):
        return player.collide_rectDOWN.colliderect(tile.rect)
    
    def collideplayer(self, tile):
        return player.rect.colliderect(tile.rect)

    def collisions(self):
       for tile in self.tiles.sprites():
        if self.collideplayer(tile):
            if self.collideright(tile):
                player.x = tile.rect.right
            if self.collideleft(tile):
                player.x = tile.rect.left - player.width
            if self.collidebottom(tile):
                player.y = tile.rect.bottom
            if self.collidetop(tile):
                player.y = tile.rect.top - player.height
    def main(self, surface):
        self.draw(surface)
        self.collisions()