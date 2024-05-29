from os import system
from super_print import sprint
from Player import *



def lv1_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('You are an adventurer thirsty')
    sprint('for adventure, starting your')
    sprint('journey in a small village')
    sprint('that has a remnant of a great')
    sprint('intriguing monolith in the')
    sprint('central square, whose secret')
    sprint('no one has yet unraveled.')
    sprint('To move forward and start')
    sprint('exploring, you first need to')
    sprint('know the commands to move,')
    sprint("which are 'move' or 'go'.")
    sprint('Test them !')
    sprint('#----------------------------#')
   
def lv2_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('You are now much closer to')
    sprint('the intriguing monolith. There')
    sprint('are five of them in a cercle')
    sprint("and you don't really know why.")
    sprint('To learn more about your')
    sprint('environment, you can use the')
    sprint("commands 'look' or 'inspect'.")
    sprint('These will be useful if you')
    sprint('wish to loot a chest, for')
    sprint('example. Go try them !')
    sprint('#----------------------------#')

def lv3_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('In an old wooden chest, you')
    sprint('find an rusty sword that will')
    sprint('deal damage to your ennemies.')
    sprint('You can use command mutiple')
    sprint('time.')
    sprint('#----------------------------#')

def lv4_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('In your carefull researche you')
    sprint('find a healing potion... ')
    sprint("I don't think I need to")
    sprint('explain this one for you.')
    sprint('Maybe you can use the command')
    sprint('again.')
    sprint('#----------------------------#')

def lv5_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('Your researche leed you to...')
    sprint('OH MY GOD... A HELMET... which')
    sprint('will be of no use to you...')
    sprint('but at least it looks stylish.')
    sprint('#----------------------------#')

def lv6_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('Haha, to greedy there is')
    sprint('nothing left in the chest, you')
    sprint('took everything from it.')
    sprint('#----------------------------#')


def lv7_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('Bro, I told you there is')
    sprint('nothing left.')
    sprint('#----------------------------#')

def lv8_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('Stop it, there is no more for')
    sprint('you.')
    sprint('#----------------------------#')

def lv9_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('WHAT DO YOU NOT UNDERSTAND IN')
    sprint("' NOTHING LEFT ' ?")
    sprint('#----------------------------#')

def lv10_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('You win. I give up.')
    sprint('#----------------------------#')

def lv11_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('You now enter in the forest')
    sprint('near the monolith. The little')
    sprint('light that can come thrue all')
    sprint("the branches don't help that")
    sprint('much.')
    sprint('#----------------------------#')

def lv12_screen():
    system('clear')
    sprint('#----------------------------#')
    sprint('Oh no. you uncounter a goblin.')
    sprint('He look menacing, is gonna')
    sprint('attack you. You can try the')
    sprint("command 'Use' to help you.")
    sprint('#----------------------------#')

def use_table():
    system('clear')
    sprint('#----------------------------#')
    sprint('    What do you want to use   ')
    sprint('#----------------------------#')
    sprint('           - sword -          ')
    sprint('           - heal  -          ')
    sprint('#----------------------------#')

def combat_scene(player, enemie):
    while player.alive or enemie.alive:
        option = None
        use_table()
        while option is None or option.lower() not in ['Sword', 'Heal']:
            if option is not None:
                sprint("Please enter a valid command")
            option = input("> ")
            if option.lower() == ('Sword'):
                player.attack(enemie)
                enemie.attack(player)
            elif option.lower() == ('Heal'):
                player.heal()
    end()

def end():
    system('clear')
    sprint('#----------------------------#')
    sprint('Congratulation, you won the')
    sprint('game.')
    sprint('#----------------------------#')