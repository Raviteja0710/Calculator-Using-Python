# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result:.2f}")  # formatted to 2 decimals
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result:.2f}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result:.2f}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result:.2f}")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            print("Thanks for using the calculator!")
            break
    else:
        print("Invalid Input")
