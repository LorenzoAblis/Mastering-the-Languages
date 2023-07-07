# A simple number guessing game

import random 

while True:
    difficulty = int(input("Difficulty (1=easy, 2=normal, 3=hard): "))
    choice = int(input("What is your number?: "))
    number = random.randint(1, (difficulty * 10))
    play_again = False

    if choice == number:
        print("Correct!")
    elif choice != number:
        print("Wrong!")
    play_again = input("Play again? (y/n): ")
    if play_again == "n":
        break
