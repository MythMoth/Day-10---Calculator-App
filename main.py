from art import logo


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


on = True
answer = 0
num_1 = 0
num_2 = 0
operator_list = ["*", "/", "+", "-"]
selection = "2"

print(logo)

while on:
    print(logo)
    if selection == "2":
        num_1 = float(input("Enter the first number: "))
    elif selection == "1":
        num_1 = answer
    print("+\n-\n*\n/\n")
    operation = input("Select an operation: ")
    num_2 = float(input("Enter the second number: "))

    if operation in operator_list:
        if operation == "*":
            answer = multiply(num_1, num_2)
        elif operation == "/":
            answer = divide(num_1, num_2)
        elif operation == "+":
            answer = plus(num_1, num_2)
        else:
            answer = minus(num_1, num_2)
        print(f"{num_1} {operation} {num_2} = {answer}")
    else:
        print("Invalid operand selected")

    print(f"1 - Continue working with {answer}")
    print("2 - Start a new calculation")
    print("0 - Exit program")

    selection = input("Enter the corresponding number to select an option: ")
    while selection not in ["1", "2", "0"]:
        print("Invalid selection.\n")
        print(f"1 - Continue working with {answer}")
        print("2 - Start a new calculation")
        print("0 - Exit program")
        selection = input("Enter the corresponding number to select an option: ")
    if selection == "0":
        on = False

