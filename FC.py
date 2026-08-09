def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))

    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1-4)")

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result 2:", subtract(num1, num2))
    elif choice == "3":
        print("Result 3:", multiply(num1*num2))
    else:
        print("Result 4:", divide(num1 / num2))

except ValueError:
    print("Error: Please enter valid numbers. ")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

    

