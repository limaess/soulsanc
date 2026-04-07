import pygame as pg
import random

from EnemyClass import Enemy

enemies = pg.sprite.Group()

default_enemy = Enemy('bad guy', (255,0,10), 500, 100, 200, 250, 0, 0, 0.04, 3, 850, 1000)
quick_enemy = Enemy('gay guy', (0,100,255), 500, 400, 150, 200, 0, 0, 0.05, 3.3, 700, 800)

colorful_enemy = Enemy('this guy', (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 900,900, 190,210, 0,0, 0.06, 3.4, 700, 900)

really_fast_guy = Enemy('fast guy', (200, 50, 50), 0,0, 100, 130, 0,0, 0.07, 4, 700, 500)

big_enemy = Enemy('big fat guy', (200,100,30), 0,0, 300,370, 0,0, 0.03, 2.7, 1000, 1200)

OH_MY_GOD = Enemy('THE DEVIL', (255,0,0), 0,0, 300, 400, 0,0, 0.1, 6.66, 900, 200)
WHAT_THE_FUCK = Enemy('THE JEVIL', (70,20,170), 0,0, 100,150, 0,0, 0.2, 7.77, 600, 100)

fly = Enemy('ew a fly', (50,50,50), 0,0, 75,100, 0,0, 0.2, 7, 300, 10)
oo_a_butterfly = Enemy('oo a butterfly', (150, 100, 200), 0,0, 150,200, 0,0, 0.3, 20, 0, 1)

enemy_choice_list = [default_enemy, quick_enemy, colorful_enemy, really_fast_guy, big_enemy, OH_MY_GOD, WHAT_THE_FUCK, fly, oo_a_butterfly]