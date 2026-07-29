'''# Simple Calculator

print("===== Simple Calculator =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operator!")'''


'''def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print("Simple Calculator")

num1 = float(input("Enter first number: "))
op = input("Choose (+ - * /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(add(num1, num2))

elif op == "-":
    print(subtract(num1, num2))

elif op == "*":
    print(multiply(num1, num2))

elif op == "/":
    print(divide(num1, num2))

else:
    print("Invalid Choice")'''
