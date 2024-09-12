num1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid Number or operator. Please enter one of +, -, *, /.")
