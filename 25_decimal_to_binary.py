"""
Decimal to Binary Converter

This program converts a decimal number into its binary representation
without using Python's built-in bin() function.
"""

number = int(input("Enter a decimal number: "))

if number == 0:
    print("Binary representation: 0")
else:
    binary = ""

    while number > 0:
        binary = str(number % 2) + binary
        number //= 2

    print(f"Binary representation: {binary}")