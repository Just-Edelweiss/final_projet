from sys import exit
from os import system

def title_screen_selections():
    option = None
    while option is None or option.lower() not in ['play', 'quit']:
        if option is not None:
            print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ('play'):
            start_game()
        elif option.lower() == ('quit'):
            exit()
    
def title_screen():
    system('clear')
    print('##########################')
    print('#   Welcome adventurer   #')
    print('##########################')
    print('         - Play -         ')
    print('         - Quit -         ')
    title_screen_selections()

if __name__ == "__main__":
    title_screen()
    
