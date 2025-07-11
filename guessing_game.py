#!/usr/bin/env python3

# Assignment 5 - Extra Credit

import random

def display_title():
    print("Guess the number!")
    print()

def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}.\n")
    count = 0
    while True:
        guess = int(input("Your guess: "))
        count += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You guessed it in {count} tries.\n")
            return

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = get_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
