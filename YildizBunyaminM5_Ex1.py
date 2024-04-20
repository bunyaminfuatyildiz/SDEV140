# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 22:17:05 2024

@author: bunya
"""
def calculate_sales_tax():
    """
    This function asks the user to enter the total sales for the month and calculates
    the county, state, and total sales tax.

    Returns:
        A dictionary containing the county sales tax, state sales tax, and total sales tax.
    """
    # Ask the user to enter the total sales amount
    total_sales = float(input("Enter the total sales for the month: "))

    # Define tax rates as constants
    STATE_TAX_RATE = 0.05
    COUNTY_TAX_RATE = 0.025

    # Calculate the county sales tax
    county_sales_tax = total_sales * COUNTY_TAX_RATE

    # Calculate the state sales tax
    state_sales_tax = total_sales * STATE_TAX_RATE

    # Calculate the total sales tax
    total_sales_tax = county_sales_tax + state_sales_tax

    # Return the results as a dictionary
    return {
        "county_sales_tax": county_sales_tax,
        "state_sales_tax": state_sales_tax,
        "total_sales_tax": total_sales_tax
    }

# Calculate sales tax based on user input
sales_tax_info = calculate_sales_tax()

# Print the results
print(f"County Sales Tax: ${sales_tax_info['county_sales_tax']:.2f}")
print(f"State Sales Tax: ${sales_tax_info['state_sales_tax']:.2f}")
print(f"Total Sales Tax: ${sales_tax_info['total_sales_tax']:.2f}")

