#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Finding the magic number game


import constants


def main():
    # This function sees if the user inputed the magic number

    print("Guess the magic number (0-9)!")

    # Input
    magic_number = int(input("Please enter your guess: "))

    # Process
    if magic_number == constants.MAGIC_NUMBER:
        # Output
        print("Nice! Your answer is right!")

    elif magic_number != constants.MAGIC_NUMBER:
        # Output
        print("Oops! Your answer is wrong!")


if __name__ == "__main__":
    main()
