# Simple Calculator Program

# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (+, -, *, /): ")

if choice == '+':
    print("Result =", a + b)
elif choice == '-':
    print("Result =", a - b)
elif choice == '*':
    print("Result =", a * b)
elif choice == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice!")