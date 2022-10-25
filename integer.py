#!/usr/bin/env python3
# Created By: Nolan Shami
# Date: Oct 24th, 2022
# This program tells you if your integer
# is positive, negative or just zero.


def main():

    print()
    user_integer = int(input("Enter your integer: "))

    # Check if integer is positive, negative or just zero

    if user_integer > 0:

        print("{} is a positive integer!".format(user_integer))

    elif user_integer < 0:

        print("{} is a negative integer!".format(user_integer))

    else:

        print("{} is just 0!".format(user_integer))


if __name__ == "__main__":

    main()
