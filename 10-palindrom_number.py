# ==========================================
# Question 10 - Check Palindrome Number
# ==========================================

# Take input from the user
number = int(input("Enter a number: "))

# Store the original number
original_number = number

# Variable to store the reversed number
reverse = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

# Check if the number is a palindrome
if reverse == original_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")