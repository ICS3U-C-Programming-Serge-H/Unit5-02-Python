#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: May 10, 2025
# This program will ask the user to enter a base then height
# And calculate the area of the triangle


def calc_area(base, height):
    # Code formula for the area of triangle

    area = base * height / 2
    print(f"The area of the triangle is {area:.2f}")


def main():
    # Get the base from user
    while True:
        try:
            base = float(input("Enter a base(cm): "))
            if base <= 0:
                print("Please enter a positive base number: ")
                continue
            break
        except ValueError:
            print("Please enter a whole number")
    # Get height from user
    while True:
        try:
            height = float(input("Enter a height(cm): "))
            if height <= 0:
                print("Please enter a positive height number: ")
                continue
            break
        except ValueError:
            print("Enter a whole number.")

    calc_area(base, height)


if __name__ == "__main__":
    main()
