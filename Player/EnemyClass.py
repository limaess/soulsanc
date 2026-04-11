import pygame as pg
import random as r

from PlayerClass import player

pg.init()
class Enemy(pg.sprite.Sprite):
    def __init__(self, name, color, x, y, width, height, x_vel, y_vel, accel, max_vel, lineofsight_size, attention_span,reaction_time, hearing, abilities, self_class):
        super().__init__()
        self.name = name
        self.lineofsight_size = lineofsight_size
        self.def_lineofsight_size = lineofsight_size

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color

        self.image = pg.Surface((width, height))
        if isinstance(self.color[0], tuple):  # Check if self.color is a tuple of tuples
            color = (r.randint(self.color[0][0], self.color[0][1]), 
                     r.randint(self.color[1][0], self.color[1][1]), 
                     r.randint(self.color[2][0], self.color[2][1]))
        else:
            color = self.color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.sight_rect = pg.Rect(x, y, lineofsight_size, lineofsight_size)

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.accel = accel
        self.def_accel = accel

        self.max_vel = max_vel
        self.negative_max_vel = self.max_vel * -1

        self.target_x = x
        self.target_y = y
        self.last_target_change = pg.time.get_ticks()

        self.target_change_cooldown = attention_span
        self.default_target_changecd = attention_span

        self.notice_time = 0
        self.reaction_time = reaction_time 
        self.def_reaction_time = reaction_time

        self.hearing = hearing
        self.def_hearing = hearing

        self.abilities = abilities

        self.nerdy_message = ''

        self.self_class = self_class

    def update(self, player, surface):
        self.reaction_time = self.def_reaction_time - (player.noise + 0.01) * self.hearing

        if self.player_in_sight(player):
            if self.needs_to_chase():
                self.chase(player)
                self.reaction_time = 5000
                self.hearing = self.def_hearing / 1.5
                self.nerdy_message = 'chasing' 
            else:
                self.nerdy_message = 'noticing'
                self.wander()
        else: #
            self.notice_time = 0
            self.wander()
            self.hearing = self.def_hearing
            self.nerdy_message = 'wandering'
            
        self.limits()
        self.listen(player)

        self.rect.topleft = (self.x, self.y)
        self.sight_rect.center = (self.x + self.rect.width // 2, self.y + self.rect.height // 2)

    def player_in_sight(self, player):
        return self.sight_rect.colliderect(player.chaserect)
    
    def needs_to_chase(self):
        current_time = pg.time.get_ticks()
        if self.notice_time == 0: # noticing
            self.notice_time = current_time 
        if current_time - self.notice_time > self.reaction_time: # noticed
            return True

    # targets
    def target_change(self):
        self.target_x = r.randint(round(self.x - (self.lineofsight_size / 2)), round(self.x + (self.lineofsight_size / 2)))
        self.target_y = r.randint(round(self.y - (self.lineofsight_size / 2)), round(self.y + (self.lineofsight_size / 2)))

        if self.target_x <= 0 or self.target_x >= 1900:
            self.target_x = self.target_x = r.randint(round(self.x - (self.lineofsight_size / 2)), round(self.x + (self.lineofsight_size / 2)))
        if self.target_y <= 0 or self.target_y >= 1060:
            self.target_y = r.randint(round(self.y - (self.lineofsight_size / 2)), round(self.y + (self.lineofsight_size / 2)))

    def target_gen(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_target_change > self.target_change_cooldown: # if targetchange cd is over:
            if round(abs(self.x - self.target_x)) < 10 and round(abs(self.y - self.target_y)) < 10:  
                self.target_change() # change targets before actually changing targets
                self.last_target_change = current_time # reset it pretty please
                return

            self.target_change()
            self.last_target_change = current_time
            self.target_change_cooldown = r.randint(self.default_target_changecd - (self.default_target_changecd // 5), self.default_target_changecd + (self.default_target_changecd // 5))

        # if self.target_x <= 0 or self.target_x >= 1800 or self.target_y <= 0 or self.target_y >= 1000:
        #     self.target_change()
        #     self.last_target_change = current_time
        self.target_x = max(0, min(self.target_x, 1900))
        self.target_y = max(0, min(self.target_y, 1080))

    def randomness(self):
        # makes so the enemies are somewhat random?
        self.x_vel += r.uniform(-0.1, 0.1) # so they feel more like
        self.y_vel += r.uniform(-0.1, 0.1) # actual animals

        if r.random() < 0.1:
            self.x_vel += r.uniform(-0.2, 0.2)
        if r.random() < 0.1:
            self.y_vel += r.uniform(-0.2, 0.2)
    
    def chase(self, player):
        self.x -= self.x_vel
        self.y -= self.y_vel

        self.x_vel = max(self.negative_max_vel, min(self.x_vel, self.max_vel))
        self.y_vel = max(self.negative_max_vel, min(self.y_vel, self.max_vel))

        self.target_x = player.chaserect.x
        self.target_y = player.chaserect.y

        self.randomness()

        if self.rect.centerx - 25 > self.target_x:
            self.x_vel += self.accel
        if self.rect.centerx - 25 < self.target_x:
            self.x_vel -= self.accel
        if self.rect.centery - 25 > self.target_y:
            self.y_vel += self.accel
        if self.rect.centery - 25 < self.target_y:
            self.y_vel -= self.accel

    def wander(self):
        self.x -= self.x_vel
        self.y -= self.y_vel

        wanderaccel = 0.01 + self.accel / 2 

        self.randomness()

        if self.x > self.target_x:
            self.x_vel += wanderaccel
        if self.x < self.target_x:
            self.x_vel -= wanderaccel
        if self.y > self.target_y:
            self.y_vel += wanderaccel
        if self.y < self.target_y:
            self.y_vel -= wanderaccel

        self.target_gen()

        self.x_vel = max(self.negative_max_vel, min(self.x_vel, self.max_vel - (self.max_vel / 2)))
        self.y_vel = max(self.negative_max_vel, min(self.y_vel, self.max_vel - (self.max_vel / 2.5)))

    def limits(self):
        self.x = max(0, min(self.x, 1920 - self.rect.width))
        self.y = max(0, min(self.y, 1080 - self.rect.height))

        if self.y >= 1080 - self.rect.height:
            self.y_vel = 0
            self.y -= 1
        if self.y <= 0:
            self.y_vel = 0
            self.y += 1

        if self.x >= 1920 - self.rect.width:
            self.x_vel = 0
            self.x -= 1
        if self.x <= 0:
            self.x += 1
            self.x_vel = 0

    def draw_sight(self, surface):
        pg.draw.rect(surface, (200,200,200), (self.sight_rect), 3)
        pg.draw.rect(surface, (150,150,155), (self.target_x, self.target_y, 50, 50))

    def listen(self, player):
        self.lineofsight_size = self.def_lineofsight_size + (player.noise * self.hearing)
        self.sight_rect.size = (self.lineofsight_size, self.lineofsight_size)