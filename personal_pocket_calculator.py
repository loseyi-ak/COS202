# COS202 Assignment
# Personal Pocket Calculator (PPC)

print("===== PERSONAL POCKET CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Choose an option (1-5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Answer =", num1 + num2)

elif choice == 2:
    print("Answer =", num1 - num2)

elif choice == 3:
    print("Answer =", num1 * num2)

elif choice == 4:
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Answer =", num1 / num2)

elif choice == 5:
    print("Answer =", num1 % num2)

else:
    print("Invalid option.")