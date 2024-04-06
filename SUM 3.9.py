# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:35:07 2024

@author: bunya
"""

# Write your program here
def calculate_and_display_stats():
    numbers = []
    while True:
        input_str = input("Enter a number or press Enter to quit: ")
        if not input_str:  # User pressed Enter
            break

        try:
            number = float(input_str)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")

    if numbers:  # Check if any numbers were entered
        total = sum(numbers)
        average = total / len(numbers)
        print("The sum is", total)
        print("The average is", average)
    else:
        print("No numbers were entered.")


if __name__ == "__main__":
    calculate_and_display_stats()
