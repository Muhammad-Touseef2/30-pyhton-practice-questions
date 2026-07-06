# Sum of Digits in a Number

number = int(input("Enter a number: "))

sum_of_digits = 0
temp_number = number

while temp_number > 0:
    digit = temp_number % 10
    sum_of_digits += digit
    temp_number //= 10

print(f"The sum of digits of {number} is: {sum_of_digits}")