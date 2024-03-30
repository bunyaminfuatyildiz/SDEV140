# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:13:33 2024

@author:Bunyamin Fuat Yildiz


Calculates the factorial of a given nonnegative integer.

Args:
    num (int): The nonnegative integer.

Returns:
    int: The factorial of the number, or an error message if invalid input
         is provided.
"""

def calculate_factorial(num):
    

    if num < 0:
        return "Error: There is no factorial for negative numbers."

    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Get user input
number = int(input("Enter a nonnegative integer: "))

# Calculate and display the factorial
print("The factorial of", number, "is", calculate_factorial(number))
