"""Simple CLI Dice Rolling Game.
Roll two dice repeatedly until the user quits."""

import random

def game():
    roll_count = 0
    while True:
        choice = (input("\nRoll the dice?(yes/no): ")).lower()
        if choice in ("yes","y"):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            total = die1 + die2
            print(f"You rolled {die1} and {die2}")
            roll_count+=1
            if total == 12:
                print("Jackpot! Double six!!")

        elif choice in ("no","n"):
            print("\nThanks for playing this game..")
            print(f"You rolled the dice {roll_count} times.")
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    game()
                