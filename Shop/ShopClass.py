import sys
import os

folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

player_class_path = sys.path.join(folder_path, 'Player')

from Player.PlayerClass import player_currencies

class Shop:
    def __init__(self):
        self.items_inshop = []

    def buy_item(self, item):
        if player_currencies.has_enough(item.value, item.value_type):
            player_currencies.currency[item.value_type] -= item.value
        else:
            print("youre poor lol")

    def sell_item(self, item):
        player_currencies.currency[item.value_type] += item.value
