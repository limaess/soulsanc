# import pygame as pg
# import os,sys
# import random as r

# folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# player_class_path = os.path.join(folder_path, 'Player')
# room_path = os.path.join(folder_path, 'Rooms')

# sys.path.insert(1, player_class_path)
# sys.path.insert(0, room_path)

# from Player.PlayerClass import *

# from Player.EnemyClass import *
# from Player.EnemyInit import *

# from Rooms.RoomInit import *

# pg.init()

# class DevTools:
#     def __init__(self):
#         self.cheats_enabled = False

#         self.enemy_choice_cfg = 0
#         self.enemy_cfg = None

#         self.enemies_frozen = False
#         self.friendly_enemies = False

#         self.draw_enemy_sight = False

        # self.stats_for_nerds = False
#         self.show_all_enemies = False

#     def enemy_choice(self, enemy_len, keys):
#         if keys[pg.K_q]:
#             self.enemy_choice_cfg = (self.enemy_choice_cfg - 1) % enemy_len
#             print(f'chosen enemy: {enemy_choice_list[self.enemy_choice_cfg].name}')
#         if keys[pg.K_e]:
#             self.enemy_choice_cfg = (self.enemy_choice_cfg + 1) % enemy_len
#             print(f'chosen enemy: {enemy_choice_list[self.enemy_choice_cfg].name}')

#     def spawn_enemy(self, keys, mouse_pos):
#         if keys[pg.K_w]:
#             print("spawning enemy...")
#             self.enemy_cfg = enemy_choice_list[self.enemy_choice_cfg]
#             if self.enemy_cfg:
#                 print("enemy config is valid..\n")

#                 print("adding color...")
#                 enemy_color = (
#                         ((r.randint(self.enemy_cfg.color[0][0], self.enemy_cfg.color[0][1]), 
#                          r.randint(self.enemy_cfg.color[1][0], self.enemy_cfg.color[1][1]), 
#                          r.randint(self.enemy_cfg.color[2][0], self.enemy_cfg.color[2][1])))
#                 )
#                 print(f"color: {enemy_color}\n")

#                 enemy_class = self.enemy_cfg.self_class

#                 if enemy_class is None:
#                     print(f"unknown enemy config class '{self.enemy_cfg.self_class}'")
#                 else:
#                     print(f"enemy class: {enemy_class.__name__}\n")

#                     enemy = enemy_class(self.enemy_cfg.name, (enemy_color), 0,0, self.enemy_cfg.width, self.enemy_cfg.height, 0,0, self.enemy_cfg.accel, self.enemy_cfg.max_vel, 
#                                 self.enemy_cfg.lineofsight_size, self.enemy_cfg.target_change_cooldown,self.enemy_cfg.reaction_time,self.enemy_cfg.hearing, self.enemy_cfg.abilities, 
#                                 self.enemy_cfg.self_class)
#                     enemy.x, enemy.y = mouse_pos
#                     print(f"adding enemy to enemies group: {enemy.name} at {enemy.x, enemy.y}\nenemies: {len(enemies) + 1}\n")
#                     enemies.add(enemy)
#             else:
#                 print('choose an enemy')

#     def clear_enemies(self, keys):
#         if keys[pg.K_z]:
#             print("removed all enemies")
#             enemies.empty()

#     def onclick_tp(self, mouse_pos, event):
#         if event.button == 1:
#             player.x, player.y = mouse_pos
#             print(f"teleported to: {mouse_pos}")
#         if event.button == 3:
#             for enemy in enemies:
#                 print(f"changed enemy targets to: {mouse_pos}")
#                 enemy.target_x,enemy.target_y = mouse_pos 
#                 enemy.target_change_cooldown = 10000

#     def other_settings(self, keys):
#         if keys[pg.K_ESCAPE]:
#             self.enemies_frozen = not self.enemies_frozen
#             print(f"frozen enemies: {self.enemies_frozen}")
#         if keys[pg.K_1]:
#             self.draw_enemy_sight = not self.draw_enemy_sight
#             print(f"drawing enemy sight: {self.draw_enemy_sight}")
#         if keys[pg.K_2]:
#             self.stats_for_nerds = not self.stats_for_nerds
#             print(f"drawing stats for nerds: {self.stats_for_nerds}")
#         if keys[pg.K_3]:
#             self.show_all_enemies = not self.show_all_enemies
#             print(f"showing enemies: {self.show_all_enemies}")
#         if keys[pg.K_4]:
#             self.friendly_enemies = not self.friendly_enemies
#             print(f"friendly enemies: {self.friendly_enemies}")

#     def enable_cheats(self, keys):
#         if keys[pg.K_F2]:
#             self.cheats_enabled = not self.cheats_enabled
#             print(f"cheats: {self.cheats_enabled}")

#     def main(self, mouse_pos, enemy_len, keys):
#         if self.cheats_enabled:
#             self.enemy_choice(enemy_len, keys)
#             self.spawn_enemy(keys, mouse_pos)
#             self.clear_enemies(keys)
#             self.other_settings(keys)
#         else:
#             self.enemies_frozen = False
#             self.draw_enemy_sight = False
#             self.stats_for_nerds = False
#             self.show_all_enemies = False
#             self.friendly_enemies = False

#         self.enable_cheats(keys)

    # def draw_stats_for_nerds(self, draw_text,font, enemy):
    #     if self.stats_for_nerds:
    #         draw_text(f'x:{round(enemy.x_vel, ndigits=2)}\ny:{round(enemy.y_vel, ndigits=2)}', font, (255,255,255), enemy.x, enemy.y) # x velocities
    #         draw_text(f' chs:{enemy.max_vel}\n wnd:{enemy.max_vel - (enemy.max_vel / 2.5)}', font, (255,255,255), enemy.x + 60, enemy.y) # chase max vel and wander max vel

    #         draw_text(f'{round(enemy.reaction_time)}\n{round(enemy.lineofsight_size)}', font, (255,255,255), enemy.x + 110, enemy.y + 50)

    #         draw_text(f'{enemy.target_change_cooldown}\n{enemy.last_target_change}', font, (255,255,255), enemy.x, enemy.y + 50) # target change cooldown and last target change

    #         draw_text(f'{round(enemy.accel, 2)}\n{round((0.01 + enemy.accel / 2), ndigits=2)}', font, (255,255,255), enemy.x + 60, enemy.y + 50) # chase accel and wander accel

    #         draw_text(f'{enemy.nerdy_message}', font, (255,255,255), enemy.x, enemy.y + 90)
    #         draw_text(f'friend: {self.friendly_enemies}', font, (255,255,255), enemy.x, enemy.y + 110)

# dev_tools = DevTools()
 