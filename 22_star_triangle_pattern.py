"""
Program: Right Triangle Star Pattern
Description: Prints a right-angled triangle pattern using asterisks (*).
"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()