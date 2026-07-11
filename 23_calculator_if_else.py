print("=== Simple Calculator ===")

operation = input("Enter an operator (+, -, *, /, %): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "+":
    print(f"Result: {num1 + num2}")

elif operation == "-":
    print(f"Result: {num1 - num2}")

elif operation == "*":
    print(f"Result: {num1 * num2}")

elif operation == "/":
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")

elif operation == "%":
    if num2 != 0:
        print(f"Result: {num1 % num2}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator. Please use one of these: +, -, *, /, %.")