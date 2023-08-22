# Add function
def add(n1, n2):
    return n1 + n2

# Subtract function


def subtract(n1, n2):
    return n1 - n2

# Multiply function


def multiply(n1, n2):
    return n1 * n2

# Divide function


def divide(n1, n2):
    return n1 / n2


operator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(num1, num2, operator):
    # Check if the operator is in the dictionary
    if operator in operator_dict:
        # Call the function from the dictionary
        calculation_func = operator_dict[operator]
        return calculation_func(num1, num2)
    else:
        print("Invalid operator")
