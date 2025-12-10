import os
import time
import random
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

while user_score >= PLAY_COST:
    print(f"Current Score: {user_score}")
    if user_score > 0:
        play_again = input(f"Would you like to play? (y/n): ").lower()
        if play_again in QUIT_COMMANDS:
            print("Thanks for playing! Cashing out.")
            break
        elif play_again not in ['yes', 'y']:
            print("Invalid input. Assuming 'no'. Cashing out.")
            break
    user_score -= PLAY_COST
    print(f"Deducting {PLAY_COST} points. Rolling...")
    time.sleep(1)
    
    final_reels = []

    for roll_iteration in range(10):
        clear()
        reels = [random.randint(0, 9) for _ in range(9)]
        print("\n  --- SPINNING ---")
        print(f" |{reels[0]}|{reels[1]}|{reels[2]}| ")
        print(f" |{reels[3]}|{reels[4]}|{reels[5]}| ")
        print(f" |{reels[6]}|{reels[7]}|{reels[8]}| ")
        print("  ----------------")