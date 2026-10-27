from utils import get_user_number, get_operation
while True:
    number_1 = get_user_number()
    number_2 = get_user_number()
    operation_result = get_operation(number_1, number_2)
    print(operation_result)