# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:32:21 2024

@author: bunya
"""
from typing import Dict, List, Tuple

def get_top_three_prices(shop_prices: Dict[str, float]) -> List[str]:
    """
    This function takes a dictionary of shop prices as input and returns the top three most expensive items and their prices.

    Args:
        shop_prices: A dictionary where keys are item names and values are their prices.

    Returns:
        A list of strings, where each string represents an item and its price in the format "ITEM PRICE".
    """
    if len(shop_prices) < 3:
        return ["Not enough items in the shop to determine top three prices."]

    # Sort the shop prices dictionary by price in descending order.
    sorted_prices = sorted(shop_prices.items(), key=lambda item: item[1], reverse=True)

    # Get the top 3 most expensive items.
    top_three_items = sorted_prices[:3]

    # Format the output as "ITEM PRICE" for each item.
    output = [f"{item[0]} {item[1]}" for item in top_three_items]

    return output

# Sample shop prices
shop_prices = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# Get the top three most expensive items and their prices
top_three_prices_list = get_top_three_prices(shop_prices)

# Print the output
for item_price in top_three_prices_list:
    print(item_price)
