from sys import stdout
from time import sleep

def sprint(msg):
    for lettre in msg:
        stdout.write(lettre)
        stdout.flush()
        sleep(0.02)
    print()