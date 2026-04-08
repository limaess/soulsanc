import pygame as pg
import os,sys

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
room_path = os.path.join(folder_path, 'Rooms')

sys.path.insert(1, player_class_path)
sys.path.insert(0, room_path)

from Player.PlayerClass import *
from Player.EnemyClass import *
from Player.EnemyInit import *

from Rooms.RoomInit import *

enemy_choice_cfg = 0
enemy_cfg = None

def enemy_choice(keys, enemy_len):
    global enemy_choice_cfg
    global enemy_cfg
    if keys[pg.K_q]:
        enemy_choice_cfg = (enemy_choice_cfg - 1) % enemy_len
    if keys[pg.K_e]:
        enemy_choice_cfg = (enemy_choice_cfg + 1) % enemy_len
    enemy_cfg = enemy_choice_list[enemy_choice_cfg]

    return enemy_cfg

def spawn_enemy(mouse_pos, keys):
    if keys[pg.K_w]:
        cfg = enemy_choice_list[enemy_choice_cfg]
        if cfg:
            enemy = Enemy(cfg.name, (cfg.color), 0,0, cfg.width, cfg.height, 0,0, cfg.accel, cfg.max_vel, cfg.lineofsight_size, cfg.target_change_cooldown)
            enemy.x, enemy.y = mouse_pos
            enemies.add(enemy)
        else:
            print('choose an enemy')

def clear_enemies(keys):
    if keys[pg.K_z]:
        enemies.empty()

def onclick_tp(mouse_pos, event):
    if event.button == 1:
        player.x, player.y = mouse_pos
    if event.button == 3:
        for enemy in enemies:
            enemy.target_x,enemy.target_y = mouse_pos 
            enemy.target_change_cooldown = 10000

def stop_chasing(keys):
    chasing = False
    if keys[pg.K_2]:
        chasing = not chasing
    
    if not chasing:
        for enemy in enemies:
            enemy.lineofsight_size = 0 

freeze_enemies = False
drawsight = False

 