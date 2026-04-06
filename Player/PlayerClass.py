import pygame as pg

class PlayerCurrency:
    def __init__(self, chip,scrap,pearl):
        self.currencies = {
            'chip': chip,
            'scrap': scrap,
            'pearl': pearl
        }

    def has_enough(self, item):
        return self.currency[item.price_curr] >= item.value
    
    # def buy_item(self, item):
    #     if self.has_enough(item.price, item.price_curr):
    #         self.currency[item.price_curr] -= item.value
    #     else:
    #         print("youre poor lol")

    def exchange_chips(self):
        if self.chip >= 100:
            self.chip -= 100
            self.scrap += 5

    def exchange_scrap(self):
        if self.scrap >= 25:
            self.scrap -= 25
            self.pearl += 1

class Player:
    def __init__(self, x,y,width,height):
        self.x,self.y = x,y
        self.width,self.height = width,height

        self.rect = pg.Rect(x,y,width,height)

        self.collide_rectUP = pg.Rect(x + width, (y - height), width / 1.3, height)
        self.collide_rectDOWN = pg.Rect(x + width, (y + height), width / 1.3, height) 
        self.collide_rectRIGHT = pg.Rect((x + width * 2), y + height // 3, height , height // 1.2)
        self.collide_rectLEFT = pg.Rect((x - width * 2), y + height // 3, height, height // 1.2)

        self.left_colors = (255,0,0)
        self.right_colors = (255,0,0)
        self.down_colors = (255,0,0)
        self.up_colors = (255,0,0)

        self.health = 2

        self.left_vel = 0
        self.right_vel = 0

        self.up_vel = 0
        self.down_vel = 0

        self.def_yvel = 0

    def movement(self):
        self.x -= self.left_vel
        self.x += self.right_vel

        self.y -= self.up_vel
        self.y += self.down_vel

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.left_vel = min(self.left_vel + 0.4, 3.2)
        else:
            self.left_vel = max(self.left_vel - 0.20, 0)

        if keys[pg.K_RIGHT]:
            self.right_vel = min(self.right_vel + 0.4, 3.2)
        else:
            self.right_vel = max(self.right_vel - 0.20, 0)

        if keys[pg.K_UP]:
            self.up_vel = min(self.up_vel + 0.4, 3.2)
        else:
            self.up_vel = max(self.up_vel - 0.20, 0)

        if keys[pg.K_DOWN]:
            self.down_vel = min(self.down_vel + 0.4, 3.2)
        else:
            self.down_vel = max(self.down_vel - 0.2, 0)


    def draw(self,surface):
        self.rect.topleft = self.x,self.y
        
        self.collide_rectUP.topleft = (self.x + 6.25), (self.y - self.height + 30)
        self.collide_rectDOWN.topleft = (self.x + 6.25), (self.y + self.height - 30)

        self.collide_rectRIGHT.center = (self.x + self.width * 1.5), self.y + self.height // 2
        self.collide_rectLEFT.center = (self.x - self.width // 2), self.y + self.height // 2

        pg.draw.rect(surface, (200,100,255), (self.rect))
        pg.draw.rect(surface, (0,0,0), (self.rect), 3)


        # pg.draw.rect(surface, (self.up_colors), (self.collide_rectUP))
        # pg.draw.rect(surface, (self.down_colors), (self.collide_rectDOWN))
        # pg.draw.rect(surface, (self.left_colors), (self.collide_rectLEFT))
        # pg.draw.rect(surface, (self.right_colors), (self.collide_rectRIGHT))

    def limits(self):
        self.rect.x = max(0, min(self.x, 1920 - self.rect.width))
        self.rect.y = max(0, min(self.y, 1080 - self.rect.height))

    def main(self, surface):
        self.movement()
        self.limits()

        self.draw(surface)
        
player = Player(100, 100, 50,70)
player_currencies = PlayerCurrency(-1, -5, -1)
