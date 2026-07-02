"""
Day 03 - Fibonacci Sequence

This program prints the Fibonacci sequence up to the
number of terms entered by the user.
"""

# Take input from the user
number_of_terms = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
first = 0
second = 1

# Check different cases
if number_of_terms <= 0:
    print("Please enter a positive integer.")

elif number_of_terms == 1:
    print("Fibonacci sequence:")
    print(first)

elif number_of_terms == 2:
    print("Fibonacci sequence:")
    print(first, second)

else:
    print("Fibonacci sequence:")
    print(first, second, end=" ")

    # Generate the remaining terms
    for _ in range(number_of_terms - 2):
        next_number = first + second
        print(next_number, end=" ")
        first = second
        second = next_number