# ==========================================
# Question 08 - Count Vowels in a String
# ==========================================

# Take input from the user
word = input("Enter any word: ")

# Variable to store the number of vowels
count = 0

# Check each character in the string
for char in word:
    if char in "aeiouAEIOU":
        count += 1

# Display the result
print("Number of vowels:", count)