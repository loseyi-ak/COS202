# COS202 Assignment
# Mathematical Calculator

print("===== MATHEMATICAL CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose an operation (+, -, *, /, %): ")

if operation == "+":
    print("Answer =", num1 + num2)

elif operation == "-":
    print("Answer =", num1 - num2)

elif operation == "*":
    print("Answer =", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Answer =", num1 / num2)

elif operation == "%":
    print("Answer =", num1 % num2)

else:
    print("Invalid operation.")