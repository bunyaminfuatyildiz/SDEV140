# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 15:44:58 2024

@author: bunya
"""
def is_prime(num):
    """
    Determine if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(upper_limit):
    """
    Generate a list of prime numbers less than or equal to the upper limit.

    Args:
        upper_limit (int): The upper limit for the prime search.

    Returns:
        list: A list of prime numbers.
    """
    primes = []
    for num in range(2, upper_limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    """
    Main function to get user input and print prime numbers.
    """
    while True:
        try:
            upper_limit = int(input("Enter a positive integer greater than 1: "))
            if upper_limit > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a valid integer.")

    print("Prime numbers less than or equal to", upper_limit, "are:")
    primes = get_primes(upper_limit)
    for prime in primes:
        print(prime)

if __name__ == "__main__":
    main()

