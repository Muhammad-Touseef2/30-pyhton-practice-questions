# Day 06 - Find the Second Largest Number in a List

numbers = [1, 2, 3, 4, 5]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print(f"The second largest number in the list is: {second_largest}")