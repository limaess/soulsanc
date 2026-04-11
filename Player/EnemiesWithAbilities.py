import pygame as pg
import random as r

from PlayerClass import player
from EnemyClass import Enemy


class DashEnemy(Enemy):
    def __init__(self, name, color, x, y, width, height, x_vel, y_vel, accel, max_vel, lineofsight_size, attention_span, reaction_time, hearing, abilities, self_class):
        super().__init__(name, color, x, y, width, height, x_vel, y_vel, accel, max_vel, lineofsight_size, attention_span, reaction_time, hearing, abilities, self_class)
        self.pounce_pos_x = 0
        self.pounce_pos_y = 0   
        self.pounce_cooldown = r.randint(300, 500)

        self.def_max_vel = max_vel
    
    def countdown_pouncecd(self):
        self.pounce_cooldown -= 1
    
    def pounce_cd_thingie(self):
        if self.pounce_cooldown <= 0:
            return True
        return False
    
    def change_vel_based_on_pouncepos(self):
        if self.pounce_pos_x >= self.x:
            self.x_vel = min(self.x_vel - self.accel * 2, self.max_vel)
        else:
            self.x_vel = max(self.x_vel + self.accel * 2, -self.max_vel)
        if self.pounce_pos_y >= self.y:
            self.y_vel = min(self.y_vel - self.accel * 2, self.max_vel)
        else:
            self.y_vel = max(self.y_vel + self.accel * 2, -self.max_vel)
    
    def change_pounce_pos(self, player):
        print(f"change_pounce_pos() called - {self.pounce_cooldown}\n")
        self.pounce_pos_x = player.x
        self.pounce_pos_y = player.y
    
        # target_rect = pg.Rect(self.pounce_pos_x, self.pounce_pos_y, 200,200)
    
        print(f"pounce pos: {self.pounce_pos_x,self.pounce_pos_y}")
        print(f"self pos: {self.x, self.y}\n")
        
        # if player.chaserect.colliderect(target_rect):
        #     self.pounce_pos_x = player.x
        #     self.pounce_pos_y = player.y
        #     target_rect = pg.Rect(self.pounce_pos_x, self.pounce_pos_y, 200, 200)
    
    def pounce(self, player):

        if self.pounce_cooldown == 70:
            self.max_vel = self.def_max_vel * 2
            self.negative_max_vel = -self.max_vel

            if self.pounce_pos_x >= self.x:
                self.x_vel = -self.max_vel
            else:
                self.x_vel = self.max_vel
            if self.pounce_pos_y >= self.y:
                self.y_vel = -self.max_vel
            else:
                self.y_vel = self.max_vel

        if self.max_vel >= self.def_max_vel:
            self.change_vel_based_on_pouncepos()


        if self.pounce_cd_thingie():
            self.pounce_cooldown = r.randint(300, 500)
            self.max_vel = self.def_max_vel

    def update(self, player, surface):
        pg.draw.rect(surface, (255,255,255), (self.pounce_pos_x, self.pounce_pos_y, 25,25))

        super().update(player, surface)
        self.countdown_pouncecd()
        if self.needs_to_chase():
            # logic
            if self.pounce_cooldown <= 80:
                self.pounce(player)
            if self.pounce_cooldown == 120:
                self.change_pounce_pos(player)

            # nerdy messages
            if self.pounce_cooldown <= 120 and self.pounce_cooldown >= 90:
                self.nerdy_message = 'changing pounce pos'
            if self.pounce_cooldown <= 90 and self.pounce_cooldown >= 80:
                self.nerdy_message = 'preparing pounce'
            if self.pounce_cooldown <= 80 and self.pounce_cooldown >= 50:
                self.nerdy_message = 'pouncing'
            if self.pounce_cooldown <= 50 and self.pounce_cooldown >= 1:
                self.nerdy_message = 'ending pounce'