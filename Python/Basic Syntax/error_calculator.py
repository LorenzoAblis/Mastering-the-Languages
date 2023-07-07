# A calculator that is able to handle errors

first_number = 0
second_number = 0
operator = ""

try:
    try:
        first_number = int(input("First Number: "))
        second_number = int(input("Second Number: "))
        operator = input("Operation: ")
    except ValueError:
        print("Invalid Input, please enter an integer")

    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("Cannot divide by zero")
    else:
        print("Unsupported operator")
except Exception as e:
    print("An unexpected error occurred")
    print(e)
    