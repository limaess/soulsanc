import pygame as pg

from TilemapClass import *
from Tilemap import *


testinggrounds_colors = {
    0: (135, 206, 235),
    1: (100,0,100),
    2: (200,0,200)
}

testinggrounds = TileMap(128, testinggrounds_map, testinggrounds_colors)
