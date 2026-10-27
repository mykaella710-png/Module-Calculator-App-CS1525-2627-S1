def add(number_1, number_2):
    """Add together two numbers to find sum

    :param number_1: Number 1
    :param number_2: Number 2
    :return: Sum of two numbers
    """
    return number_1 + number_2

def subtract(number_1, number_2):
    """Subtract number 2 from number 1 to find difference

    :param number_1: Number 1
    :param number_2: Number 2
    :return:Difference of two numbers
    """
    return number_1 - number_2

def multiply(number_1, number_2):
    """Multiply two numbers to find the product

    :param number_1: Number 1
    :param number_2: Number 2
    :return: Product of the two numbers
    """
    return number_1 * number_2

def divide(number_1, number_2):
    """Divide number 1 by number 2 to find the quotient

    :param number_1: Number 1
    :param number_2: Number 2
    :return: Quotient of the two numbers
    """
    if number_2 == 0:
        return "Cannot divide by zero, undefined"
    else:
        return number_1 / number_2