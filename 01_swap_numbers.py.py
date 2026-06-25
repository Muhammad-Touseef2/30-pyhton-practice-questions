#Write a python program to swap two variables

num1 = int(input("Enter the value of number 1 : "))
num2 = int(input("Enter the value of number 2 : "))

print("The value of number 1 before swapping" , num1)
print("The value of number 2 before swapping" , num2)

temp = num1
num1 = num2
num2 = temp

print()
print("The value of number 1 after swapping" , num1)
print("The value of number 2 after swapping" , num2)
