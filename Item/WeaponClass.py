import pygame as pg
import random as r
import sys
import os

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
sys.path.insert(0, player_class_path)

from Player.PlayerClass import player

class Weapon():
    def __init__(self, cooldown):
        # super().__init__()
        self.cooldown = cooldown
        self.weapons = {
            'scythe': {'cooldown': 0, 'func': self.scythe_otherfunc},
            'placeholder': {'cooldown': 0, 'func': None}
        }

    def applyEffect(self,weapon):
        self.weapons[weapon]['cooldown'] = weapon.cooldown
        self.weapons[weapon]['func']()

    def scythe_dash(self):
        velocities = [player.left_vel,player.right_vel,player.up_vel,player.down_vel]
        for vel in velocities:
            vel += 4     
        
    def scythe_otherfunc(self):
        self.cooldown = self.weapons['scythe']['cooldown'] 
        velocities = [player.left_vel,player.right_vel,player.up_vel,player.down_vel]

        if self.cooldown <= 4.9:
            self.scythe_dash()
        if self.cooldown <= 1:
            for vel in velocities:
                vel -= 0.1

scythe = Weapon(5)
velocities = [player.left_vel,player.right_vel,player.up_vel,player.down_vel]

pg.init()

while True:
    keys = pg.key.get_just_pressed()

    if keys[pg.K_q]:
        break

    if keys[pg.K_z]:
        scythe.applyEffect('scythe')

    print(scythe.cooldown)
    print(* velocities)