# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:58:53 2024

@author: bunya2: Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total. (15 points)

"""

meal_charge = float(input( "How much the meal cost?"))
tax = meal_charge * 0.07
tip = meal_charge * 0.18
total = meal_charge + tax + tip

print("Your meal charge is",  meal_charge, "dollars.")
print("The mandatory sales tax amount is",tax, "dollars.")
print("The tip amount is", tip, "dollars.")
print("Total cost is:", total, "dollars.")