import os
import time
import random

def clear():
    """Clears the terminal screen cross-platform."""
    # os.system('cls') works on Windows.
    # os.system('clear') works on macOS/Linux.
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Setting up variables
user_score = 100
PLAY_COST = 5
PAYOUT_WIN_LINE = 20
QUIT_COMMANDS = ['no', 'n', 'quit', 'exit']

# 2. Welcome Message
print("===========================")
print("Loops Machine")
print("===========================")
print(f"Starting score: {user_score}")
print(f"Cost per play: {PLAY_COST}")
print(f"Payout per win line: {PAYOUT_WIN_LINE}")
print("===========================\n")

# 3. Paying for the game (Main Game Loop)
while user_score >= PLAY_COST:
    print(f"Current Score: {user_score}")

    # Ask the user if they want to play again (only if they have funds)
    if user_score > 0:
        play_again = input(f"Would you like to play? (y/n): ").lower()
        if play_again in QUIT_COMMANDS:
            print("Thanks for playing! Cashing out.")
            break
        elif play_again not in ['yes', 'y']:
            print("Invalid input. Assuming 'no'. Cashing out.")
            break
            
    # Deduct play cost
    user_score -= PLAY_COST
    print(f"Deducting {PLAY_COST} points. Rolling...")
    time.sleep(1)
    
    final_reels = []

    # 4. Slot Roll Simulation Loop
    for roll_iteration in range(10):
        clear()
        # Generate 9 random numbers for this specific animation frame
        reels = [random.randint(0, 9) for _ in range(9)]
        
        print("\n  --- SPINNING ---")
        print(f" |{reels[0]}|{reels[1]}|{reels[2]}| ")
        print(f" |{reels[3]}|{reels[4]}|{reels[5]}| ")
        print(f" |{reels[6]}|{reels[7]}|{reels[8]}| ")
        print("  ----------------")
        
        if roll_iteration == 9:
            # Save the numbers from the final roll
            final_reels = reels
            print("\n  --- RESULTS ---")
        
        time.sleep(0.25)

    # The code below this line must be indented within the `while` loop, 
    # but *outside* the `for` loop.

    # 5. Check for Payout

    # Map the final reels to variables for easier checking (r1, r2, ..., r9)
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
    
    # Check each condition using a loop
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
        
    # 6. Cash out or play again
    input("\nPress Enter to continue to the next round...")
    clear()

# Code outside the while loop runs when the game ends (user runs out of money or quits)
print("\n")
print("===========================")
print(f"GAME OVER. Your final score is: {user_score}")
print("===========================")