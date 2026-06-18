def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

def floor_division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b

def calculator():
    print("===== Python Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("0. Exit")

    while True:
        choice = input("\nEnter choice (0-7): ")
        if choice == "0":
            print("Exiting calculator.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", addition(a, b))
        elif choice == "2":
            print("Result:", subtraction(a, b))
        elif choice == "3":
            print("Result:", multiplication(a, b))
        elif choice == "4":
            print("Result:", division(a, b))
        elif choice == "5":
            print("Result:", power(a, b))
        elif choice == "6":
            print("Result:", modulus(a, b))
        elif choice == "7":
            print("Result:", floor_division(a, b))

if __name__ == "__main__":
    calculator()
