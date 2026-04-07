import pygame as pg
import random

from PlayerClass import player

class Enemy(pg.sprite.Sprite):
    def __init__(self, name, color, x, y, width, height, x_vel, y_vel, accel, max_vel, lineofsight_size, attention_span):
        super().__init__()
        self.name = name
        self.lineofsight_size = lineofsight_size

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color

        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.sight_rect = pg.Rect(x, y, lineofsight_size, lineofsight_size)

        self.x_vel = x_vel
        self.y_vel = y_vel
        self.accel = accel
        self.max_vel = max_vel
        self.negative_max_vel = self.max_vel * -1

        self.target_x = x
        self.target_y = y
        self.last_target_change = pg.time.get_ticks()

        self.target_change_cooldown = attention_span
        self.default_target_changecd = attention_span

    def update(self, player):
        if self.player_in_sight(player):
            self.chase(player)
        else:
            self.wander()

        self.limits()

        self.rect.topleft = (self.x, self.y)
        self.sight_rect.center = (self.x + self.rect.width // 2, self.y + self.rect.height // 2)

    def player_in_sight(self, player):
        return self.sight_rect.colliderect(player.rect)

    def target_change(self):
        self.target_x = random.randint(round(self.x - 300), round(self.x + 300))
        self.target_y = random.randint(round(self.y - 300), round(self.y + 300))

    def target_gen(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_target_change > self.target_change_cooldown:
            if round((abs(self.x - self.target_x)) < 10 and round(abs(self.y - self.target_y)) < 10):
                self.target_change()
                self.last_target_change = current_time # reset it pretty please

            self.target_change()
            self.last_target_change = current_time
            self.target_change_cooldown = random.randint(self.default_target_changecd - 100, self.default_target_changecd + 100)

        if self.target_x <= 0 or self.target_x >= 1800 or self.target_y <= 0 or self.target_y >= 1000:
            self.target_change()
            self.last_target_change = current_time

    def randomness(self):
        # makes so the enemies are somewhat random?
        self.x_vel += random.uniform(-0.005, 0.005) # so they feel more like
        self.y_vel += random.uniform(-0.005, 0.005) # actual animals

        if random.random() < 0.1:
            self.x_vel += random.uniform(-0.1, 0.1)
        if random.random() < 0.1:
            self.y_vel += random.uniform(-0.1, 0.1)
    
    def chase(self, player):
        self.x -= self.x_vel
        self.y -= self.y_vel

        self.x_vel = max(self.negative_max_vel, min(self.x_vel, self.max_vel))
        self.y_vel = max(self.negative_max_vel, min(self.y_vel, self.max_vel))

        self.randomness()

        if self.x > player.rect.x:
            self.x_vel += self.accel
        if self.x < player.rect.x:
            self.x_vel -= self.accel
        if self.y > player.rect.y:
            self.y_vel += self.accel
        if self.y < player.rect.y:
            self.y_vel -= self.accel

    def wander(self):
        self.x -= self.x_vel
        self.y -= self.y_vel

        self.randomness()

        if self.x > self.target_x:
            self.x_vel += 0.03
        if self.x < self.target_x:
            self.x_vel -= 0.03
        if self.y > self.target_y:
            self.y_vel += 0.03
        if self.y < self.target_y:
            self.y_vel -= 0.03

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
        pg.draw.rect(surface, (0,200,50), self.sight_rect, 3)
        pg.draw.rect(surface, (0,255,0), (self.target_x, self.target_y, 50, 50))

enemies = pg.sprite.Group()

default_enemy = Enemy('bad guy', (255,0,10), 500, 100, 200, 250, 0, 0, 0.04, 3, 850, 1000)
quick_enemy = Enemy('gay guy', (0,100,255), 500, 400, 150, 200, 0, 0, 0.05, 3.3, 700, 800)

colorful_enemy = Enemy('this guy', (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 900,900, 190,210, 0,0, 0.06, 3.4, 700, 900)

really_fast_guy = Enemy('fast guy', (200, 50, 50), 0,0, 100, 130, 0,0, 0.07, 4, 500, 750)

big_enemy = Enemy('big fat guy', (200,100,30), 0,0, 300,370, 0,0, 0.03, 2.7, 1000, 1200)

OH_MY_GOD = Enemy('THE DEVIL', (255,0,0), 0,0, 300, 400, 0,0, 0.1, 6.66, 900, 200)
WHAT_THE_FUCK = Enemy('THE JEVIL', (70,20,170), 0,0, 100,150, 0,0, 0.3, 7.77, 600, 100)

enemy_choice_list = [default_enemy, quick_enemy, colorful_enemy, really_fast_guy, big_enemy, OH_MY_GOD, WHAT_THE_FUCK]

# enemies.add(default_enemy, quick_enemy)