#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Finding the magic number game


import constants


def main():
    # This function finds the sum of 2 numbers

    print("Guess the magic number (0-9)!")
    
    # Input
    magic_number = int(input("Please enter your guess: "))

    # Process
    if magic_number == constants.MAGIC_NUMBER:
        win = 0

    elif magic_number != constants.MAGIC_NUMBER:
        win = 1
    # Output
    if win == 0:
        print("Nice! Your answer is right!")

    elif win == 1:
        print("Oops! Your answer is wrong!")


if __name__ == "__main__":
    main()
