import controller

profit = 0
resources = controller.resources


def coffee_machine():
    user_input = input(
        "What would you like? (espresso/latte/cappuccino) or 'exit': ")
    global profit
    global resources

    if user_input == "exit":
        print("Goodbye!")
        return

    if user_input == "espresso":
        make_espresso()
    elif user_input == "latte":
        make_latte()
    elif user_input == "cappuccino":
        make_cappuccino()
    else:
        # Print report of coffee machine
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")

    coffee_machine()


def make_espresso():
    global profit
    global resources

    # Check if there are enough resources to make the coffee
    if resources['water'] < 50:
        print("Sorry there is not enough water.")
    elif resources['coffee'] < 18:
        print("Sorry there is not enough coffee.")
    else:
        # Process the coffee
        resources['water'] -= 50
        resources['coffee'] -= 18
        profit += 15
        print("Here is your espresso ☕， Enjoy!")


def make_latte():
    global profit
    global resources

    # Check if there are enough resources to make the coffee
    if resources['water'] < 200:
        print("Sorry there is not enough water.")
    elif resources['milk'] < 150:
        print("Sorry there is not enough milk.")
    elif resources['coffee'] < 24:
        print("Sorry there is not enough coffee.")
    else:
        # Process the coffee
        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 24
        profit += 25
        print("Here is your latte ☕， Enjoy!")


def make_cappuccino():
    global profit
    global resources

    # Check if there are enough resources to make the coffee
    if resources['water'] < 250:
        print("Sorry there is not enough water.")
    elif resources['milk'] < 100:
        print("Sorry there is not enough milk.")
    elif resources['coffee'] < 24:
        print("Sorry there is not enough coffee.")
    else:
        # Process the coffee
        resources['water'] -= 250
        resources['milk'] -= 100
        resources['coffee'] -= 24
        profit += 30
        print("Here is your cappuccino ☕， Enjoy!")


coffee_machine()
