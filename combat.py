import random

class Combat:
    """combat"""

    def __init__(self):
        """combat"""
        #self.damage = [1, 1, 1]
        self.player_health_pool = 20
        #self.health = self.health_max
        #self.attack = random.randint(damage, weights = [])
        self.m_health_pool = 10

    def player_h(self):
        """returns current player health???"""
        current_health = self.player_health_pool
        return current_health

    def mob_h(self):
        """returns current mob health???"""
        current_heal = self.m_health_pool
        return current_heal


    def recover_health(self):
        heal = random.randint(2,4)
        player_health = self.player_health_pool + heal
        if player_health >= 20:
            player_health = 20
        self.player_health_pool = player_health
        return heal, player_health

    def damage_to_char(self):
        """picks from list of numbers to do random damage to player
        from the mob, returns damage to player and player health"""
        list3 = [10, 2, 3, 3, 4, 6, 8]
        damages = random.choice(list3)
        player_health = self.player_health_pool - damages
        if player_health <= 0:
            player_health = 0
        self.player_health_pool = player_health
        return damages, player_health

    def attack(self):
        """in this function the player attacks the mob, hits are taken from a random number list, and  then returns
         the attacks as damage to mob and returns the mob health after taking damage"""
        #hits = [1, 2, 3, 4, 5, 1, 0]
        #damages = random.choice(hits)
        damages = random.randint(1,4)
        c_mob_health = self.m_health_pool - damages
        if c_mob_health <= 0:
            c_mob_health = 0
        self.m_health_pool =  c_mob_health
        #if self.m_health_pool <= 0:
            #return (print("the troll is dead"))
        #else:
        print(f"{damages, c_mob_health, self.m_health_pool}, damage dealt by player, mob health after damage, current mob health")
        return damages, c_mob_health


    def m_take_damage(self):
        c_mob_health = self.m_health_pool - self.attack
        return c_mob_health