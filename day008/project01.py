# Program a Ceaser Chiper
from chiper import ceaser_chiper


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if (direction != "encode" and direction != "decode"):
        print("Invalid input")
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser_chiper(direction, text, shift)

    flag = input("Do you want to continue? Type 'yes' or 'no'\n")
    if (flag == "no"):
        break
