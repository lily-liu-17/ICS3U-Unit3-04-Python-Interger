#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This lets user guess a number
# Program will say right or wrong and give answer

import random


def main():
    # This lets user guess a number

    # input
    interger = int(input("Enter a interger : "))

    # process and output
    if interger > 0:
        print("{0} is a positive number".format(interger))
    elif interger < 0:
        print("{0} is a negative number".format(interger))
    elif interger == 0:
        print("{0} is just zero!".format(interger))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
