import random as r

class Item:
    def __init__(self, amount, uses_left, value, value_type, function):
        self.amount = amount
        self.uses_left = uses_left

        self.value = value
        self.value_type = value_type

        self.function = function