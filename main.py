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

from ConsoleTest import *

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

def draw_stats_for_nerds(draw_text,font, enemy):
    if dev_console.stats_for_nerds:
        draw_text(f'x:{round(enemy.x_vel, ndigits=2)}\ny:{round(enemy.y_vel, ndigits=2)}', font, (255,255,255), enemy.x, enemy.y) # x velocities
        draw_text(f' chs:{enemy.max_vel}\n wnd:{enemy.max_vel - (enemy.max_vel / 2.5)}', font, (255,255,255), enemy.x + 60, enemy.y) # chase max vel and wander max vel

        draw_text(f'{round(enemy.reaction_time)}\n{round(enemy.lineofsight_size)}', font, (255,255,255), enemy.x + 110, enemy.y + 50)

        draw_text(f'{enemy.target_change_cooldown}\n{enemy.last_target_change}', font, (255,255,255), enemy.x, enemy.y + 50) # target change cooldown and last target change
        draw_text(f'{round(enemy.accel, 2)}\n{round((0.01 + enemy.accel / 2), ndigits=2)}', font, (255,255,255), enemy.x + 60, enemy.y + 50) # chase accel and wander accel

        draw_text(f'{enemy.nerdy_message}', font, (255,255,255), enemy.x, enemy.y + 90)


running = True
while running: 
    clock.tick(75)
    mouse_pos = pg.mouse.get_pos()
    
    screen.fill(the_end.background_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if dev_console.cheats_on:
            dev_console.in_event_main(event)

    enemies_len = len(enemies)
    enemychoice_len = len(enemy_choice_list)

    keys = pg.key.get_just_pressed()

    # dev_tools.main(mouse_pos,enemychoice_len, keys)

    if keys[pg.K_F2]:
        dev_console.cheats_on = not dev_console.cheats_on

    # enemy_cfg = dev_tools.enemy_cfg

    player.main(screen)

    the_end3.update()
    the_end3.draw(screen)


    if enemies:
        # if not dev_tools.enemies_frozen:
        enemies.update(player, screen)  
        enemies.draw(screen)

        # if dev_tools.friendly_enemies:
        #     player.chaserect.x = 1000000
        # else:
        #     player.chaserect.x = player.x


    thisy = 0   
    othery = 0

    screen.blit(THE_END_SCREEN_EFFECT, (0,0))

    for enemy in enemies:   
        if dev_console.view_sight:
            enemy.draw_sight(screen)    
            if enemy.player_in_sight(player):
              pg.draw.line(screen, (150,150,150), player.chaserect.center, enemy.rect.center, 5)
            else:
                pg.draw.line(screen, (150,150,150), (enemy.target_x + 25, enemy.target_y + 25), enemy.rect.center, 3)

    #     try:
    #         if dev_tools.show_all_enemies:
    #             pg.draw.rect(screen, (0,0,0), (1690, othery, 250, 40))
    #             draw_text(f'{enemy.name} - {enemy.nerdy_message}', smallerfont, (enemy.color), 1690, othery)
    #         othery += 40    
    #     except ValueError:
    #         pass

        draw_stats_for_nerds(draw_text, smallerfont, enemy)

    # enemy_color = (
    #     (r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[0][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[0][1]), 
    #      r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[1][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[1][1]), 
    #      r.randint(enemy_choice_list[dev_tools.enemy_choice_cfg].color[2][0], enemy_choice_list[dev_tools.enemy_choice_cfg].color[2][1]))
    #     )   

    # if dev_tools.cheats_enabled:
    #     draw_text('player ->', font, (255,255,255), player.x - 120, player.y + 15)
    #     draw_text(f'left vel: {round(player.left_vel, ndigits=2)}\nright vel: {round(player.right_vel, ndigits=2)}\ndown vel: {round(player.down_vel, ndigits=2)}\nup vel: {round(player.up_vel, ndigits=2)}',
    #             font, (255,255,255), 0,0)
    #     draw_text(f'x vel: {round(player.x_vel, 2)}\ny vel: {round(player.y_vel, 2)}', font, (255,255,255), 0,150)

    #     draw_text(f'fps: {round(clock.get_fps())} ticks:{pg.time.get_ticks()} time:{clock.get_time()}', biggerfont, (255,255,255), 0,900)

    #     draw_text(f'currently chosen enemy:\n{enemy_choice_list[dev_tools.enemy_choice_cfg].name} -- {dev_tools.enemy_choice_cfg + 1}', biggerfont, (enemy_color), 0, 940)

    if dev_console.cheats_on:
        dev_console.main(screen)

    pg.display.flip()
pg.quit()