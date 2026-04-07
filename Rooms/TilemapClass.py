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
        self.image = pg.Surface((width, height)).convert()
        self.image.fill(color)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collideright(self):
        return player.collide_rectLEFT.colliderect(self.rect)
    def collideleft(self):
        return player.collide_rectRIGHT.colliderect(self.rect)
    def collidebottom(self):
        return player.collide_rectUP.colliderect(self.rect)
    def collidetop(self):
        return player.collide_rectDOWN.colliderect(self.rect)
    
    def collideplayer(self):
        return player.rect.colliderect(self.rect)

    def collisions(self):
        if self.collideplayer():
            if self.collideright():
                player.x = self.rect.right
            if self.collideleft():
                player.x = self.rect.left - player.width
            if self.collidebottom():
                player.y = self.rect.bottom
            if self.collidetop():
               player.y = self.rect.top - player.height

class TileMap:
    def __init__(self, tile_size, tile_map, tile_colors):
        self.tile_size = tile_size
        self.tile_map = tile_map

        self.tiles = pg.sprite.Group()

        self.tile_colors = tile_colors

        self.created_tiles = False

    def create_tiles(self):
        for row in range(len(self.tile_map)):
            for col in range(len(self.tile_map[row])):
                tile_type = self.tile_map[row][col]

                if tile_type != 0:
                    x = col * self.tile_size
                    y = row * self.tile_size
                    color = self.tile_colors[tile_type]
                    tile = Tile(x, y, self.tile_size, self.tile_size, color)
                    self.tiles.add(tile)
        self.created_tiles = True

    def draw(self, surface):
        self.tiles.draw(surface)

    def update(self):
        if not self.created_tiles:
            self.create_tiles()

        for tile in self.tiles:
            if player.collision_rect.colliderect(tile.rect):
                tile.collisions()