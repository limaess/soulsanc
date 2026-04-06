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

running = True
while running: 
    clock.tick(75)
    fps = round(clock.get_fps())

    screen.fill((20,20,50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    player.main(screen)

    testinggrounds.main(screen)

    enemies.update(player)
    enemies.draw(screen)

    y = 0
    for enemy in enemies:
        enemy.draw_sight(screen)

        if enemy.player_in_sight(player):
            draw_text(f'chased by {enemy.name}', font, (255,255,255), 0,y)
            y += 30

    draw_text('player ->', font, (255,255,255), player.x - 120, player.y + 15)
    draw_text(f'{fps}', font, (255,255,255), 0,900)

    pg.display.flip()
pg.quit 