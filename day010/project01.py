# Calculator
from calc import operator_dict, calculate


def calculator():
    # Enter the first number
    num1 = float(input("Enter the first number: "))
    for operator in operator_dict:
        print(operator)

    restart_flag = True

    while restart_flag:
        # Enter the operator
        operator = input("Pick an operator: ")

        # Enter the second number
        num2 = float(input("Enter the next number: "))

        answer = round(calculate(num1, num2, operator), 2)  # type: ignore
        print(f"{num1} {operator} {num2} = {answer}")

        # Ask if the user wants to continue
        user_input = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'q' to quit: ")
        if user_input == "y":
            num1 = answer
        elif user_input == "q":
            restart_flag = False
        else:
            restart_flag = False
            calculator()


calculator()
