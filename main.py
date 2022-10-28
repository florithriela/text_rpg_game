import random
import pickle
import json
import sys
from colorama import Fore, Back, Style
from charcter import Character
from mob import Mob
from combat import Combat
from story import Story
from loot import Loot



def death(self):
     print(f"{Fore.RED}You died!")
     sel = input(f"{Fore.BLUE}type 1 to return to the menu,  2 exit.\n")
     if sel == "1":
         run_menu()
     if sel == "2":
         sys.exit()


def game_start(char_name, class_name):
    #char_name = player_one.name
    combat = Combat()
    loot = Loot()
    print(f"{Fore.BLUE}The hero {char_name} sets off on a journey to find fame and adventure.")
    #print(Style.RESET_ALL)
    print(f"{Fore.BLUE}{char_name} sets off on a path towards the dark forest.")
    print(f"{Fore.BLUE}{char_name} finds a troll blocking the path.")
    op = input(f"{Fore.BLUE}type 1 to fight the troll, 2 to sneak around it.\n")
    while op != "1" or "2":
        print(f"{Fore.BLUE} Please make a valid selection")
        op = input(f"{Fore.BLUE}type 1 to fight the troll, 2 to sneak around it.\n")

        if op == "2":
            print(f"{Fore.BLUE}You attempt to sneak past the troll but you are not stealthy enough")
            print(f"{Fore.BLUE}He sees you and hits you with his might fists for {combat.damage_to_char()[0]}")



        if op == "1":

           while combat.m_health_pool >= 1 and combat.player_health_pool >= 1:

                select = input(f"{Fore.RED}Press '1' to swing your sword at the troll, press '2' to use a health potion\n")
                if select == '1':
                    print(
                        f"{Fore.BLUE}{char_name} swings their sword at the troll and hits it for {Fore.RED}{combat.attack()[0]} damage.")
                    print(
                        f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {Fore.RED}{combat.damage_to_char()[0]} damage")
                    print(f"{Fore.BLUE}Your health is now {Fore.GREEN}{combat.player_h()}.")
                    print(f"{Fore.BLUE}The trolls health is now {Fore.RED}{combat.mob_h()}")
                if select == '2':
                    print(
                        f"{Fore.BLUE}{char_name} uses a health potion and heals for {Fore.GREEN}{combat.recover_health()[0]}.")
                    print(f"{Fore.BLUE}{char_name} health is now at {Fore.GREEN}{combat.player_h()}.")
                    print(
                        f"{Fore.BLUE}The troll swings back at you with its mighty fists and hits you for {combat.damage_to_char()[0]}")

            # print(f"The troll is now at {self.combat.attack()[1]} health.")
            # print(f"Your health is now {self.combat.damage_to_char()[1]}.")

        if combat.player_health_pool <= 1:

            print(f"{Fore.RED}You died!")
            sel = input(f"{Fore.BLUE}type 1 to return to the menu,  2 exit.\n")
            if sel == "1":
                run_menu()
            if sel == "2":
                sys.exit()
        elif combat.m_health_pool <= 1:
            print(f"{Fore.RED}You have slain the troll!")

            print(f"{Fore.BLUE}You search the dead troll and find {loot.gold()} gold")


def create_new_char():
    print("Welcome to RPG world")
    class_name = input(f"Enter your class, choose mage or warrior")
    char_name = input(f"Enter your name")

    player_one = Character(char_name, class_name)
    #player_info = {'Name: "f{player_one.name}", Class:"f{player_one.cla}"'}
    print(f"Your have made a {player_one.cla} named {player_one.name}")
    pickled_player = pickle.dump(player_one, open('player_file.pickle', 'wb'))
    #player_file.close()
    un_pickled_player = pickle.load(open('player_file.pickle', 'rb'))
    player_one = un_pickled_player
    print(f"This is the unpickled player {player_one}")
    # my_class = str(player_one.cla)
    # my_name = str(player_one.name)
    # my_string = my_class, my_name
    # print(my_string)

    #with open('player_info.txt', 'w') as f:
    #    f.write(str(my_string))

    #with open('player_info.txt', 'w') as player_info_file:
    #    player_info_file.write(json.dumps(player_game_one))
    #
    game_start(player_one.name, player_one.cla)
    return player_one.name, player_one.cla

def run_menu():
    print(f"{Fore.BLUE}Welcome to text world\n")
    print(f"C{Fore.BLUE}choose from the following options\n")
    print(f"""{Fore.BLUE}Menu:\n
    {Fore.CYAN}1: Start a new game\n
    {Fore.CYAN}2: Quit\n
    {Fore.CYAN}3: Load game\n
    """)

    opt = input(f"{Fore.BLUE}what would you like to do? -->\n")

    if opt == "1":
        print(f"{Fore.BLUE}ok starting game")
        print(f"{Fore.YELLOW} :) :) :)")
        create_new_char()
    if opt == "2":
        sys.exit()

    if opt == "3":
        un_pickled_player = pickle.load(open('player_file.pickle', 'rb'))
        player_one = un_pickled_player
        #with open('player_info.txt', 'r') as f:
            # player_data = f.read()
            # char_name = player_data[0]
            # class_name = player_data[1]
            # player_one = Character(char_name, class_name)



        print(f"Your saved character is a {player_one.cla} named {player_one.name}")

        game_start(player_one.name, player_one.cla)

run_menu()



