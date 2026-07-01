# ==========================================
# Question 11 - Sum of First N Natural Numbers
# ==========================================

# Take input from the user
n = int(input("Enter a number: "))

# Variable to store the sum
total = 0

# Calculate the sum of the first N natural numbers
for i in range(1, n + 1):
    total += i

# Display the result
print(f"Sum of the first {n} natural numbers is: {total}")