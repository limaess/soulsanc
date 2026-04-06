import pygame as pg

from TilemapClass import *
from Tilemap import *


placeholder_tile_colors = {
    0: (135, 206, 235),
    1: (100,0,100),
    2: (200,0,200)
}

placeholder_tilemap = TileMap(128, placeholder_tilemap_tilemap, placeholder_tile_colors)
