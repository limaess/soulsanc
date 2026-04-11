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
from Player.EnemyInit import *

from Rooms.RoomInit import *
from Rooms.LocationClass import *

from DevTools import *

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((1920, 1080))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
    
smallerfont = pg.font.SysFont('Arial', 20)
font = pg.font.SysFont('Arial', 30)
biggerfont = pg.font.SysFont('Arial', 50)

THE_END_SCREEN_EFFECT = pg.surface.Surface((1920,1080)).convert_alpha()
THE_END_SCREEN_EFFECT.fill((10,10,15, 150))

running = True
while running: 
    clock.tick(75)
    mouse_pos = pg.mouse.get_pos()
    
    screen.fill(the_end.background_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            dev_tools.onclick_tp(mouse_pos,event)

    enemies_len = len(enemies)
    enemychoice_len = len(enemy_choice_list)

    keys = pg.key.get_just_pressed()

    dev_tools.main(mouse_pos,enemychoice_len, keys)

    enemy_cfg = dev_tools.enemy_cfg

    player.main(screen)

    the_end1.update()
    the_end1.draw(screen)

    if enemies:
        if not dev_tools.enemies_frozen:
            enemies.update(player, screen)  
        enemies.draw(screen)

        if dev_tools.friendly_enemies:
            player.chaserect.x = 1000000
        else:
            player.chaserect.x = player.x


    thisy = 0   
    othery = 0

    screen.blit(THE_END_SCREEN_EFFECT, (0,0))

    for enemy in enemies:   
        if dev_tools.draw_enemy_sight:
            enemy.draw_sight(screen)    
            if enemy.player_in_sight(player):
              pg.draw.line(screen, (150,150,150), player.chaserect.center, enemy.rect.center, 5)
            else:
                pg.draw.line(screen, (150,150,150), (enemy.target_x + 25, enemy.target_y + 25), enemy.rect.center, 3)

        try:
            if dev_tools.show_all_enemies:
                pg.draw.rect(screen, (0,0,0), (1690, othery, 250, 40))
                draw_text(f'{enemy.name} - {enemy.nerdy_message}', smallerfont, (enemy.color), 1690, othery)
            othery += 40    
        except ValueError:
            pass

        dev_tools.draw_stats_for_nerds(draw_text,smallerfont,enemy)

    enemy_color = (
        (r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[0][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[0][1]), 
         r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[1][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[1][1]), 
         r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[2][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[2][1]))
        )   

    if dev_tools.cheats_enabled:
        draw_text('player ->', font, (255,255,255), player.x - 120, player.y + 15)
        draw_text(f'left vel: {round(player.left_vel, ndigits=2)}\nright vel: {round(player.right_vel, ndigits=2)}\ndown vel: {round(player.down_vel, ndigits=2)}\nup vel: {round(player.up_vel, ndigits=2)}',
                font, (255,255,255), 0,0)
        draw_text(f'x vel: {round(player.x_vel, 2)}\ny vel: {round(player.y_vel, 2)}', font, (255,255,255), 0,150)

        draw_text(f'fps: {round(clock.get_fps())} ticks:{pg.time.get_ticks()} time:{clock.get_time()}', biggerfont, (255,255,255), 0,900)

        draw_text(f'currently chosen enemy:\n{enemy_choice_list[dev_tools.enemy_choice_cfg].name} -- {dev_tools.enemy_choice_cfg + 1}', biggerfont, (enemy_color), 0, 940)

    pg.display.flip()
pg.quit()