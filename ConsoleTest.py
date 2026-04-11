import pygame as pg
import random as r

import json

import os,sys
folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
room_path = os.path.join(folder_path, 'Rooms')

sys.path.insert(1, player_class_path)
sys.path.insert(0, room_path)

# from Player.PlayerClass import *

# from Player.EnemyClass import *
from Player.EnemyInit import *

from Rooms.RoomInit import *

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
UNFOCUSED_CONSOLE_COLOR = (200, 200, 200)

GRAY = (100, 100, 100)
DARKGRAY = (80, 80, 80)

BLACK = (0, 0, 0)

pg.init()

FONT = pg.font.SysFont('Tahoma', 12)

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pg.Rect(x, y, width, height)
        self.background_rect = pg.Rect((x - 35, y - 310, width * 1.2, height * 14))     

        self.text = text
        self.text_history = []

        self.active = False
        self.box_color = WHITE

        self.dragging = False

        self.scroll_pos = 0
        self.scroll_speed = 10

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            if self.background_rect.collidepoint(event.pos):               
                if event.button == 5:  
                    self.scroll_pos = max(0, self.scroll_pos - self.scroll_speed)
                elif event.button == 4:  
                    self.scroll_pos = min(len(self.text_history) - self.scroll_speed, self.scroll_pos + self.scroll_speed)
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    with open('text data', 'w', encoding='utf-8') as f:
                        json.dump(self.text, f, indent=2)
                    
                    self.text_history.insert(0, self.text)

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_DELETE:
                    self.text = ''

                else:
                    self.text += event.unicode
        return None

    def draw(self, screen):
        if self.active:
            self.box_color = WHITE
        else:
            self.box_color = UNFOCUSED_CONSOLE_COLOR

        pg.draw.rect(screen, GRAY, self.background_rect)     
        pg.draw.rect(screen, WHITE, self.background_rect, 3)      

        # input box
        pg.draw.rect(screen, DARKGRAY, self.rect)
        pg.draw.rect(screen, self.box_color, self.rect, 2)

        text_surface = FONT.render(self.text, True, self.box_color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        visible_logs = self.text_history[self.scroll_pos:self.scroll_pos + 18]
        text_y = self.rect.y - 40
        for text in visible_logs:
            text_thing = FONT.render(text, True, WHITE)
            screen.blit(text_thing, (self.rect.x - 20, text_y))
            text_y -= 15

screen = pg.display.set_mode((1920, 1080))
clock = pg.time.Clock()

drag_start = False

class DevConsole:
    def __init__(self, x, y, width, height, text=''):
        self.cheats_on = False
        self.input_box = InputBox(x, y, width, height, text)

        self.commands = {
            'ent_spawn': self.ent_spawn,
            'ent_clear': self.clearenemies,
            'ent_viewstat': self.viewstat,
            'ent_viewsight': self.viewsight,

            'self_goto': self.goto,

            'print': self.returninput,

            'scrollspeed': self.change_scroll_speed
        }

        self.stats_for_nerds = False
        self.view_sight = False

    def handle_event(self, event):
        return self.input_box.handle_event(event)

    def draw(self, screen):
        self.input_box.draw(screen)

    def execute_command(self, command):
        parts = command.split()
        if parts:
            command_name = parts[0].lower()
            args = parts[1:]
            parsed_args = []
            for arg in args:
                try:
                    parsed_args.append(int(arg))
                except ValueError:
                    try:
                        parsed_args.append(float(arg))
                    except ValueError:
                        parsed_args.append(arg)
            if command_name in self.commands:
                self.commands[command_name](*parsed_args)
            else:
                self.input_box.text_history.insert(0,f'{command_name} not defined!')

    def ent_spawn(self, enemy_name, x,y):
        enemy_names = {
            'bad': default_enemy,
            'quick': quick_enemy,
            'colorful': colorful_enemy,
            'fast': really_fast_guy,
            'big': big_enemy,
            'devil': OH_MY_GOD,
            'jevil': WHAT_THE_FUCK,
            'fly': fly,
            'butterfly': oo_a_butterfly,
            'blind': blind_lol,
            'ash': were_dead
        }

        if enemy_name in enemy_names:
            enemy_cfg = enemy_names.get(enemy_name)
        else:
            self.input_box.text_history.insert(0,"enemies:")
            for enemy in enemy_names:
                self.input_box.text_history.insert(0,f" {enemy}")
            return

        self.input_box.text_history.insert(0,"enemy config is valid..")
        self.input_box.text_history.insert(0,"")
        self.input_box.text_history.insert(0,"adding color..")

        enemy_color = (
                ((r.randint(enemy_cfg.color[0][0], enemy_cfg.color[0][1]), 
                 r.randint(enemy_cfg.color[1][0], enemy_cfg.color[1][1]), 
                 r.randint(enemy_cfg.color[2][0], enemy_cfg.color[2][1])))
        )

        self.input_box.text_history.insert(0,f"color: {enemy_color}")
        self.input_box.text_history.insert(0,"")

        enemy_class = enemy_cfg.self_class

        if enemy_class is None:
            self.input_box.text_history.insert(0,f"unknown enemy class: {enemy_class}")

        else:
            self.input_box.text_history.insert(0,f"enemy class: {enemy_class.__name__}")
            enemy = enemy_class(enemy_cfg.name, (enemy_color), 0,0, enemy_cfg.width, enemy_cfg.height, 0,0, enemy_cfg.accel, enemy_cfg.max_vel, 
                        enemy_cfg.lineofsight_size, enemy_cfg.target_change_cooldown,enemy_cfg.reaction_time,enemy_cfg.hearing, enemy_cfg.abilities, 
                        enemy_cfg.self_class)
            if not x == 'mx' and not y == 'my':
                enemy.x, enemy.y = x,y
            else:
                enemy.x, enemy.y = pg.mouse.get_pos()

            self.input_box.text_history.insert(0,f"adding {enemy.name} to enemies group at {enemy.x, enemy.y}\nenemies in room: {len(enemies) + 1}")
            self.input_box.text_history.insert(0,"")

            enemies.add(enemy)

    def clearenemies(self):
        if enemies:
            for enemy in enemies:
                self.input_box.text_history.insert(0,f'{enemy.name} removed')
        enemies.empty()                

    def viewstat(self):
        self.stats_for_nerds = not self.stats_for_nerds
        self.input_box.text_history.insert(0,f'view enemy stats: {self.stats_for_nerds}')
        self.input_box.text_history.insert(0,"")

    def viewsight(self):
        self.view_sight = not self.view_sight
        self.input_box.text_history.insert(0,f'view enemy sight: {self.view_sight}')
        self.input_box.text_history.insert(0,"")

    def goto(self, x,y):
        if not x == 'mx' and not y == 'my':
            player.x, player.y = x,y
        else:
            player.x,player.y = pg.mouse.get_pos()

    def returninput(self, *args):
        if args:
            user_input = ' '.join(map(str, args))
            self.input_box.text_history.insert(0,user_input)
        else:
            self.input_box.text_history.insert(0,'input smth')

    def change_scroll_speed(self, scroll_speed):
        if scroll_speed:
            self.input_box.scroll_speed = scroll_speed
        else:
            self.input_box.text_history.insert(0,f'scrollspeed: {self.input_box.scroll_speed}')

    def main(self, screen):
        self.draw(screen)

        self.input_box.background_rect.topleft = self.input_box.rect.x - 35, self.input_box.rect.y - 310,

        if pg.mouse.get_pressed()[0] and not self.input_box.dragging:
            mouse_pos = pg.mouse.get_pos()
            if self.input_box.background_rect.collidepoint(mouse_pos):
                self.input_box.dragging = True
                self.input_box.mouse_offset_x = mouse_pos[0] - dev_console.input_box.rect.x
                self.input_box.mouse_offset_y = mouse_pos[1] - dev_console.input_box.rect.y

        if self.input_box.dragging:
            mouse_pos = pg.mouse.get_pos()
            self.input_box.rect.x = mouse_pos[0] - self.input_box.mouse_offset_x
            self.input_box.rect.y = mouse_pos[1] - self.input_box.mouse_offset_y
            self.input_box.background_rect.topleft = self.input_box.rect.x - 35, self.input_box.rect.y - 310

            if not pg.mouse.get_pressed()[0]:
                self.input_box.dragging = False

    def in_event_main(self, event):
        dev_console.handle_event(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            dev_console.execute_command(self.input_box.text)
            dev_console.input_box.text = ''

dev_console = DevConsole(75, 450, 350, 25)
