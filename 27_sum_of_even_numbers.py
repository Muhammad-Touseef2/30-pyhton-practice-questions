# Sum of Even Numbers in a List

numbers = [1, 2, 3, 4, 5, 6]

even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print(f"Sum of even numbers: {even_sum}")