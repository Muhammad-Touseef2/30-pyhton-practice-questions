# =======================================================
# Create a program that find the largest of three numbers
# =======================================================

num1 = int(input("Enter the value of num1 :"))
num2 = int(input("Enter the value of num2 :"))
num3 = int(input("Enter the value of num3 :"))

if num1 > num2 and num1 > num3:
    print("Largest number is :" , num1)
elif num2>num3 :
    print("Largest number is: " , num2) 
else:
    print("Largest number is :" , num3)       