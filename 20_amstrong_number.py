"""
Program: Armstrong Numbers from 1 to 100
Author: Muhammad Touseef
Description:
    This program prints all Armstrong numbers between 1 and 100.

An Armstrong number is a number that is equal to the sum of its
digits, where each digit is raised to the power of the total
number of digits.

Example:
    153 = 1³ + 5³ + 3³ = 153
"""

print("Armstrong Numbers from 1 to 100:\n")

for number in range(1, 101):
    temp = number
    digits = len(str(number))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == number:
        print(number)