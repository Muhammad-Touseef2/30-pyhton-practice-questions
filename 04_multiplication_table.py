# =======================================================================
# Create a program that prints the multiplication table of a given number
# =======================================================================

number = int(input("Enter the number: "))

for i in range(1 , 11):
    print(number , "X" , i , "=" , number * i)