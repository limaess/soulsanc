import pygame as pg
import os,sys

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
player_class_path = os.path.join(folder_path, 'Player')
sys.path.insert(0, folder_path)
print(folder_path)

from TilemapClass import *
from Tilemap import *
from Player.EnemyInit import *

testinggrounds_enemies = {
    were_dead: {'position': (1800,500)},
    really_fast_guy: {'position': (500,900)}
}
testinggrounds = TileMap(128, testinggrounds_map, testinggrounds_colors, testinggrounds_enemies)

the_end1_enemies = {
    blind_lol: {'positions': [(1500, 0), (1500, 500)], 'count': 2},
    fly: {'count': 5, 'randomize_position': True, 'spawn_area': (1920, 1080)},
}

the_end1 = TileMap(128, the_end1_map, the_end_maincolors, the_end1_enemies)
