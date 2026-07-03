"""
Python Program to Find the Greatest Common Divisor (GCD)

Methods Covered:
1. Using the math module
2. Using the Brute Force approach
"""

# ==========================
# Method 1: Using math.gcd()
# ==========================

import math

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

gcd = math.gcd(first_number, second_number)

print("The GCD of", first_number, "and", second_number, "is:", gcd)


# ==============================
# Method 2: Brute Force Approach
# ==============================

first_number = int(input("\nEnter first number: "))
second_number = int(input("Enter second number: "))

for i in range(1, min(first_number, second_number) + 1):
    if first_number % i == 0 and second_number % i == 0:
        gcd = i

print("The GCD of", first_number, "and", second_number, "is:", gcd)