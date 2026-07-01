# ==========================================
# Question 09 - Reverse a String
# ==========================================

# Take input from the user
word = input("Enter any word: ")

# Print the string in reverse order
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")

print()  # Move the cursor to the next line