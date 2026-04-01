import pygame as pg
import os
import sys

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
room_path = os.path.join(folder_path, 'Rooms')
sys.path.insert(0, room_path)

from TilemapClass import *
from Tilemap import *


placeholder_tile_colors = {
    0: (135, 206, 235),
    1: (100,0,100),
    2: (200,0,200)
}

placeholder_tilemap = TileMap(128, placeholder_tilemap_tilemap, placeholder_tile_colors)
