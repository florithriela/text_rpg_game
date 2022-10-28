import random

class Mob:
    """Models each Menu Item."""
    def __init__(self):
        self.name = "goblin"

        self.health = 6
        self.hit = random.randint(1, 3)
        #self.create_ch() #if you want to initialize one of the functions when the class is called, such as creating an object on screen

    def spider_type(self, name):
        self.name = "spider"
        self.health = 5
        self.hit = random.randint(1, 3)


    def goblin_type(self):
        pass

    def bear_type(self):
        pass

    def dragon_type(self):
        pass


    def orc_type(self):
        pass