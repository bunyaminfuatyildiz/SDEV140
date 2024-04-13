# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# LargeSmall.py - This program calculates the largest and smallest of three integer values.

def find_largest(num1, num2, num3):
    """Finds the largest of three numbers."""
    return max(num1, num2, num3)

def find_smallest(num1, num2, num3):
    """Finds the smallest of three numbers."""
    return min(num1, num2, num3)




# Prompt the user to enter 3 integer values
print("Enter the first number ")
firstNumber = int(input())
print("Enter the second number ")
secondNumber = int(input())
print("Enter the third number ")
thirdNumber = int(input())

# Find the largest and smallest numbers
largest = find_largest(firstNumber, secondNumber, thirdNumber)
smallest = find_smallest(firstNumber, secondNumber, thirdNumber)

# Output largest and smallest numbers
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))


