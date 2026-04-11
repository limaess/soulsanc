import pygame as pg
import random as r

from RoomInit import *

class Location:
    def __init__(self, rooms_in_loc, current_room, rooms_that_can_spawn, background_color):
        self.seed = r.randint(1,9999)

        self.rooms_inside = rooms_in_loc # list
        self.amount_of_rooms = len(rooms_in_loc)

        self.rooms_that_can_spawn = rooms_that_can_spawn

        self.current_room = current_room

        self.background_color = background_color

the_end = Location([], None, [the_end1], (0,0,3))