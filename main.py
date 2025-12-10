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
        
        if roll_iteration == 9:
            final_reels = reels
            print("\n  --- RESULTS ---")
        
        time.sleep(0.25)

  r1, r2, r3, r4, r5, r6, r7, r8, r9 = final_reels
  winnings = 0
    win_lines_count = 0

    # Define all possible win conditions (5 ways)
    win_conditions = [
        ("Top Row: 1=2=3", r1, r2, r3),
        ("Mid Row: 4=5=6", r4, r5, r6),
        ("Bot Row: 7=8=9", r7, r8, r9),
        ("Diag \\: 1=5=9", r1, r5, r9),
        ("Diag /: 7=5=3", r7, r5, r3),
    ]

  print("\nChecking results...")
    for description, a, b, c in win_conditions:
        # Use simple `if` statements so multiple lines can award payouts
        if a == b == c:
            print(f" 🎉 WINNER! {description} matched! Awarding {PAYOUT_WIN_LINE} points.")
            winnings += PAYOUT_WIN_LINE
            win_lines_count += 1
    
    if winnings > 0:
        user_score += winnings
        print(f"\nTotal Winnings this round: {winnings}")
        print(f"New Score: {user_score}")
    else:
        print("\nNo matching lines this round. Better luck next time!")
     input("\nPress Enter to continue to the next round...")
    clear()
print("\n")
print("===========================")
print(f"GAME OVER. Your final score is: {user_score}")
print("===========================")