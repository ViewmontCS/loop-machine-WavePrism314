import os
from random import randint
from time import sleep

def clear():
  os.system('cls')

user_score = 100
PLAY_COST = 5
PAYOUT_WIN_LINE = 20
QUIT_COMMANDS = ['no', 'n', 'quit', 'exit']

print("===========================")
print("Loops Machine")
print("===========================")
print(f"Starting score: {user_score}")
print(f"Cost per play: {PLAY_COST}")
print(f"Payout per win line: {PAYOUT_WIN_LINE}")
print("===========================\n")

