import random

class Loot:
    """loot table"""
    def __init__(self):
        """loot"""
        drop_list = ["sword", "coat", "shoes", "hat", "cape", "ring",
                     "coat", "junk", "earring"]

        golds = ["1 gold", "1 gold", "1 gold", "1 gold", "2 gold", "2 gold",
                 "3 gold"]
        self.inventory = []

    def loot_drops(self):
        drop_list = ["sword", "coat", "shoes", "hat", "cape", "ring",
                     "coat", "junk", "earring"]
        drops = (random.choices(drop_list, weights=[8, 8, 8, 3, 3, 3, 1, 1, 1], k=2))
        return (drops)

    def gold_drops(self):
        golds = ["1 gold", "1 gold", "1 gold", "1 gold", "2 gold", "2 gold",
                     "3 gold"]
        drops = (random.choices(drop_list, weights=[3, 3, 1, 1, 1, 1, 1], k=1))
        return (drops)


    def gold(self):
        golds = random.randint(1,4)
        self.inventory.append(golds)
        return (golds)
    #print(f"you walk further and find a chest, you open and inside you find {loot()}")

    def list_inventory(self):
        for item in inventory:
            print(item)