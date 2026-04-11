import pygame as pg
import sys
import os

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = os.path.join(folder_path, 'Player')
sys.path.insert(0, player_class_path)

from Player.PlayerClass import *
from Player.EnemyInit import *

from ConsoleTest import *

class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.rect = pg.Rect(x, y, width, height)
        self.image = pg.Surface((width, height)).convert()
        self.image.fill(color)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collideright(self):
        return player.collide_rectLEFT.colliderect(self.rect)
    def collideleft(self):
        return player.collide_rectRIGHT.colliderect(self.rect)
    def collidebottom(self):
        return player.collide_rectUP.colliderect(self.rect)
    def collidetop(self):
        return player.collide_rectDOWN.colliderect(self.rect)
    
    def collideplayer(self):
        return player.collrect.colliderect(self.rect)

    def collisions(self):
        if self.collideplayer():
            if self.collideright():
                player.x = self.rect.right
            if self.collideleft():
                player.x = self.rect.left - player.width
            if self.collidebottom():
                player.y = self.rect.bottom
            if self.collidetop():
               player.y = self.rect.top - player.height

class TileMap:
    def __init__(self, tile_size, tile_map, tile_colors, enemies_in_room):
        self.tile_size = tile_size
        self.tile_map = tile_map

        self.tiles = pg.sprite.Group()

        self.tile_colors = tile_colors

        self.enemies_in_room = enemies_in_room # 

        self.created_tiles = False

    def create_tiles(self):
        dev_console.input_box.text_history.insert(0, "creating tiles..")
        dev_console.input_box.text_history.insert(0,"--------------------------")
        for row in range(len(self.tile_map)):
            for col in range(len(self.tile_map[row])):
                tile_type = self.tile_map[row][col]

                if tile_type != 0:
                    x = col * self.tile_size
                    y = row * self.tile_size
                    color = self.tile_colors[tile_type]
                    tile = Tile(x, y, self.tile_size, self.tile_size, color)
                    self.tiles.add(tile)
                    dev_console.input_box.text_history.insert(0,f"added tile '{tile_type}' at: {x, y} with color: {color} -- {row, col}")
        self.created_tiles = True
        dev_console.input_box.text_history.insert(0,"--------------------------")
        dev_console.input_box.text_history.insert(0, "created tiles")

    def spawn_enemies(self):
        dev_console.input_box.text_history.insert(0, "spawning enemies... \n")
        if self.enemies_in_room:
            for enemy in self.enemies_in_room:
                enemy_data = self.enemies_in_room[enemy]
                for count in range(enemy_data['count']):
                    dev_console.input_box.text_history.insert(0, f"new enemy: {enemy.name}")
                    dev_console.input_box.text_history.insert(0, "--------------------------")

                    # re-randomize enemy color
                    dev_console.input_box.text_history.insert(0, "adding enemy color")
                    enemy_color = (
                            ((r.randint(enemy.color[0][0], enemy.color[0][1]), # rerandomizing enemy color
                             r.randint(enemy.color[1][0], enemy.color[1][1]), 
                             r.randint(enemy.color[2][0], enemy.color[2][1])))
                    )
                    dev_console.input_box.text_history.insert(0, f"new enemy color: {enemy_color}")

                    # create new instance of enemy
                    spawned_enemy = enemy.self_class(enemy.name, (enemy_color), 0,0, enemy.width, enemy.height, 0,0, enemy.accel, enemy.max_vel, 
                                enemy.lineofsight_size, enemy.target_change_cooldown,enemy.reaction_time,enemy.hearing, enemy.abilities, 
                                enemy.self_class) 

                    # set its position to the set position in enemies_in_room 
                    position_index = count % len(enemy_data['position'])
                    spawned_enemy.x, spawned_enemy.y = enemy_data['position'][position_index][0], enemy_data['position'][position_index][1]

                    dev_console.input_box.text_history.insert(0, f"adding enemy to enemies group : {enemy.name} at {spawned_enemy.x, spawned_enemy.y} - {count}")
                    dev_console.input_box.text_history.insert(0, "--------------------------")

                    # add to group
                    enemies.add(spawned_enemy)
        else:
            dev_console.input_box.text_history.insert(0, "no enemies to add")
            return
        dev_console.input_box.text_history.insert(0, "spawned enemies \n")
        for enemy in enemies:
            dev_console.input_box.text_history.insert(0, f"{enemy.name} - {enemy.x, enemy.y}")
        
            
    def draw(self, surface):
        self.tiles.draw(surface)

    def update(self):
        if not self.created_tiles:
            self.create_tiles()
            self.spawn_enemies()
            dev_console.input_box.text_history.insert(0, '')


        for tile in self.tiles:
            if player.collision_rect.colliderect(tile.rect):
                tile.collisions()