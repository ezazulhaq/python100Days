# Treasure Island program

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input(
    "Where do you want to go? Type 'left' or 'right'. : ").lower()

if direction == "left":
    swim = input(
        "Do you want to swim or wait? Type 'swim' or 'wait'. : ").lower()
    if swim == "wait":
        door = input("Which door? Type 'red', 'blue' or 'yellow'. : ").lower()
        if door == "red":
            print("Burned by fire. Game over.")
        elif door == "blue":
            print("Eaten by beasts. Game over.")
        elif door == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")

else:
    print("Fall into a hole. Game over.")
