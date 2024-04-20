# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 9:25:13 2024

@author: bunya
"""

import random

def guess_the_number(track_guesses=False):
  """
  This function generates a random number between 1 and 100 and plays a guessing game with the user.

  Args:
      track_guesses: Optional boolean value (default: False). If True, tracks the number of guesses the user makes.
  """
  # Generate random number
  random_number = random.randint(1, 100)

  # Keep track of guesses (if enabled)
  num_guesses = 0 if not track_guesses else 1

  # Game loop
  while True:
    try:
      # Get user guess
      guess = int(input("Guess a number between 1 and 100: "))
      num_guesses += 1

      # Check guess
      if guess > random_number:
        print("Too high, try again.")
      elif guess < random_number:
        print("Too low, try again.")
      else:
        print(f"Congratulations! You guessed the number in {num_guesses} tries.")
        break

    except ValueError:
      print("Invalid input. Please enter a number.")

  # Restart game prompt
  play_again = input("Would you like to play again? (y/n): ").lower()
  if play_again == "y":
    guess_the_number(track_guesses)

# Run the game with optional guess tracking
guess_the_number(track_guesses=True)
