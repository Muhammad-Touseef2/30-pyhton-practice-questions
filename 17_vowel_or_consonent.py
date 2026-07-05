# Vowel or Consonant Checker
# This program checks whether the entered character is a vowel or a consonant.

ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")
elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")