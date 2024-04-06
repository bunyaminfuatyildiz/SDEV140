# Ask the user to enter a series of single-digit numbers
number_series = input("Enter a series of single-digit numbers without  any separator: ")

# Calculate the sum of the single-digit numbers
sum_of_digits = sum(int(digit) for digit in number_series)

# Display the sum
print(f"The sum of the digits is: {sum_of_digits}")
