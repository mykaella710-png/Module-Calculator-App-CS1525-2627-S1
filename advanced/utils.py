from operations import add, subtract, multiply, divide

def get_user_number():
    while True:
        number = input("Please enter a number: ")
        try:
            number = int(number)
        except ValueError:
            number = input("Please enter a valid number\n")
            number = int(number)
        return number

def get_operation(number_1, number_2):
    while True:
        operation = input("Please enter one of the operations: add, subtract, multiply, divide\n")
        if operation == "+":
            return add(number_1, number_2)
        elif operation == "-":
            return subtract(number_1, number_2)
        elif operation == "*":
            return multiply(number_1, number_2)
        elif operation == "/":
            return divide(number_1, number_2)
        else:
            input("Invalid operation, please re-enter\n")