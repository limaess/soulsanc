import pygame as pg
import random

from EnemyClass import Enemy
from EnemiesWithAbilities import *

enemies = pg.sprite.Group()

default_enemy = Enemy('bad guy', ((50, 130),(0,10), (10,50)),
                       500, 100, 200, 250, 0, 0, 0.07       , 4.3, 850, 850, 500, 2.5, [], Enemy)
quick_enemy = Enemy('gay guy', (((0,50)),((100,200)),((150,255))),
                     500, 400, 150, 200, 0, 0, 0.08, 5, 700, 600, 300, 2, [], Enemy)

colorful_enemy = Enemy('this guy', (((0,255)),((0,255)),((0,255))), 900,900, 190,210, 0,0, 0.06, 4, 700, 700, 600, 1.7, [], Enemy)

really_fast_guy = DashEnemy('fast guy', (((140,255)), ((25,60)), ((50,75))), 0,0, 100, 120, 0,0, 0.15, 6, 700, 500, 300, 4.5, [], DashEnemy)

big_enemy = Enemy('big fat guy', (((170,255)),((50,200)),((20,60))), 0,0, 300,370, 0,0, 0.06, 3.1, 1000, 1000, 700, 2, [], Enemy)

OH_MY_GOD = Enemy('THE DEVIL guy', (((254, 255)), ((0,1)), ((0, 1))), 0,0, 300, 400, 0,0, 0.1, 6.66, 900, 200, 0, 50, [], Enemy)
WHAT_THE_FUCK = DashEnemy('THE JEVIL guy', (((70, 71)), ((20,21)), ((170,171))), 0,0, 100,150, 0,0, 0.2, 7.77, 600, 100, 0, 50, [], DashEnemy)

fly = Enemy('fly guy', (((25,30)), ((25,30)), ((25,35))), 0,0, 75,100, 0,0, 0.2, 7, 300, 1, 10000000000, 1.5, [], Enemy)
oo_a_butterfly = Enemy('butterfly guy', (((200, 250)), ((40,140)), ((100,200))), 0,0, 150,200, 0,0, 0.3, 20, 900, 1, 1000000, 0, [], Enemy)

blind_lol = Enemy('blind guy', (((20,40)), ((30,60)), ((10,20))), 0,0, 300,320, 0,0, 0.07, 7, 300, 1500, 1000, 20, [], Enemy)

were_dead = DashEnemy('John TEiN', (((100, 140)), ((60,80)), ((150,200))), 0,0, 200,230, 0,0, 0.08, 3.5, 1000, 900, 500, 2.5, [], DashEnemy)

enemy_choice_list = [default_enemy, quick_enemy, colorful_enemy, really_fast_guy, big_enemy, OH_MY_GOD, WHAT_THE_FUCK, fly, oo_a_butterfly, blind_lol, were_dead]
