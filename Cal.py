def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponentiate(x, y):
    return x ** y


def modulus(x, y):
    return x % y


def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y


def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate (x^y)")
    print("6. Modulus (x % y)")
    print("7. Floor Division (x // y)")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '7':
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")


if __name__ == "__main__":
    calculator()


