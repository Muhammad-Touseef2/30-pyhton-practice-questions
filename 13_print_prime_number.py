# ==========================================
# Question 13 - Print Prime Numbers from 1 to 100
# ==========================================

print("Prime numbers between 1 and 100 are:")

# Check each number from 2 to 100
for number in range(2, 101):
    is_prime = True

    # Check if the number is divisible by any number other than 1 and itself
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    # Print the number if it is prime
    if is_prime:
        print(number, end=" ")

print()  # Move the cursor to the next line