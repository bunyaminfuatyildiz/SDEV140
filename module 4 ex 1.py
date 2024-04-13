# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:28:10 2024

@author: bunya
"""

# Write your program here
def unique_words(file_path):
    unique_words_set = set()

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into words
            words = line.strip().split()
            # Add each word to the set to keep only unique words
            unique_words_set.update(words)

    # Convert the set to a list and sort it alphabetically
    unique_words_list = sorted(list(unique_words_set))

    # Print the unique words
    for word in unique_words_list:
        print(word)

# Test the function with a file
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    unique_words(file_path)
