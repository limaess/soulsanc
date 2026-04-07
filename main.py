import pygame as pg
import random as r

import os,sys

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
room_path = os.path.join(folder_path, 'Rooms')

sys.path.insert(1, player_class_path)
sys.path.insert(0, room_path)

from Player.PlayerClass import *
from Player.EnemyClass import *

from Rooms.RoomInit import *

pg.init()

screen = pg.display.set_mode((1920, 1080))
clock = pg.time.Clock()

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
    
font = pg.font.SysFont('Arial', 30)
biggerfont = pg.font.SysFont('Arial', 50)

cfg = None
cfg_yourchoice = 0

running = True
while running: 
    clock.tick(75)
    fps = round(clock.get_fps())
    mouse_pos = pg.mouse.get_pos()

    screen.fill((20,20,50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            player.x, player.y = mouse_pos

    this = len(enemies)
    thiserthis = len(enemy_choice_list)

    keys = pg.key.get_just_pressed()

    if keys[pg.K_q]:
        cfg_yourchoice = (cfg_yourchoice - 1) % thiserthis
    if keys[pg.K_e]:
        cfg_yourchoice = (cfg_yourchoice + 1) % thiserthis

    if keys[pg.K_w]:
        cfg = enemy_choice_list[cfg_yourchoice]
        if cfg:
            enemy = Enemy(cfg.name, (cfg.color), 0,0, cfg.width, cfg.height, 0,0, cfg.accel, cfg.max_vel, cfg.lineofsight_size, cfg.target_change_cooldown)
            enemy.x, enemy.y = mouse_pos 
            enemies.add(enemy)
        else:
            print('choose an enemy')
    
    if keys[pg.K_z]:
        enemies.empty()

    if enemy_choice_list[cfg_yourchoice] == colorful_enemy:
        colorful_enemy.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    player.main(screen)

    testinggrounds.main(screen)

    enemies.update(player)
    enemies.draw(screen)

    thisy = 0
    othery = 40
    draw_text(f'on screen: {this}', biggerfont, (255,255,255), 1630, -10)

    for enemy in enemies:
        enemy.draw_sight(screen)
        if enemy.player_in_sight(player):
            draw_text(f'chased by {enemy.name}', font, (255,255,255), 0,thisy)
            thisy += 30
        pg.draw.rect(screen, (50,50,50), (1695, othery, 150, 40))
        draw_text(f'{enemy.name}', font, (enemy.color), 1700, othery)
        othery += 40    

        draw_text(f'x:{round(enemy.x_vel, ndigits=2)}\ny:{round(enemy.y_vel, ndigits=2)}', font, (255,255,255), enemy.x, enemy.y)
        draw_text(f' chs:{enemy.max_vel}\n wnd:{enemy.max_vel - (enemy.max_vel / 2.5)}', font, (255,255,255), enemy.x + 90, enemy.y)
        draw_text(f'{enemy.target_change_cooldown}\n{enemy.last_target_change}', font, (255,255,255), enemy.x, enemy.y + 80)

    draw_text('player ->', font, (255,255,255), player.x - 120, player.y + 15)
    draw_text(f'fps: {fps}', biggerfont, (255,255,255), 0,900)
    draw_text(f'currently chosen enemy:\n{enemy_choice_list[cfg_yourchoice].name} -- {cfg_yourchoice + 1}', biggerfont, (enemy_choice_list[cfg_yourchoice].color), 0, 940)

    pg.display.flip()
pg.quit 