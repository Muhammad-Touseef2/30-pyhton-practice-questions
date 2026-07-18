# Question: Write a Python program to find the square root of a perfect square 
# number using a while loop (without using the math module).

number = int(input("Enter a number: "))

found = False

for i in range(1, number + 1):
    if i * i == number:
        print(f"The square root of {number} is {i}")
        found = True
        break

if not found:
    print(f"{number} is not a perfect square.")