# Prime Number Checker
# This program checks whether a given number is prime or not.

number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a prime number.")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")