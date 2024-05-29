from sys import exit, stdout
from os import system
from super_print import *
from level import *
from Object import *
from Player import *

acceptable_actions = ['move', 'go', 'inspect', 'look', 'Use']

def title_screen_selections():
    option = None
    while option is None or option.lower() not in ['play', 'quit']:
        if option is not None:
            sprint("Please enter a valid command")
        option = input("> ")
        if option.lower() == ('play'):
            sprint('What is your name, adventurer ?')
        elif option.lower() == ('quit'):
            exit()



def title_screen():
    system('clear')
    sprint('##########################')
    sprint('#   Welcome adventurer   #')
    sprint('##########################')
    sprint('         - Play -         ')
    sprint('         - Quit -         ')
    sprint('--------------------------')
    title_screen_selections()


def choose_name():
    name = input("> ")
    system('clear')
    sprint("My dear friend " + name + ", that's a lovely name.")
    return name
        

def adventur():
    lv1_screen()
    option = None
    while True:
        if option is not None and option.lower() not in ['move', 'go']:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv2_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv3_screen()
            sword = Object('sword','weapon',1)
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv4_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv5_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv6_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv7_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv8_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv9_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv11_screen()
            break
        if option.lower() in ['inspect', 'look']:
            lv10_screen()
            lv11_screen()
            break
    option = None
    while True:
        if option is not None and option.lower() not in acceptable_actions:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() in ['move', 'go']:
            lv12_screen()
            Goblin = Player('Goblin', 10)
            combat_scene(P1, Goblin)
            break
        if option.lower() in ['inspect', 'look']:
            sprint('There is nothing to inspect')
        option = input("> ")


if __name__ == "__main__":
    title_screen()
    P1 = Player(choose_name(), 10)
    adventur()
    