# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:59:06 2024

@author: bunya
"""

import random

def write_random_numbers(file_name, number_count):
    with open(file_name, 'w') as file:
        for _ in range(number_count):
            number = random.randint(1, 500)
            file.write(f"{number}\n")
            print(number)

# User specifies the number of random numbers
num_numbers = int(input("How many random numbers would you like to generate? "))
file_name = "random_numbers.txt"

write_random_numbers(file_name, num_numbers)