# Secret Auction Program
from bid import store_bider, find_highest_bider

biders = []
biding_finished = False

while not biding_finished:
    # Enter input for bid amount
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # Store bid in a dictionary
    biders.append(store_bider(name, bid))  # type: ignore

    add_more = input("Are there any other biders? Type 'yes' or 'no'.\n")

    if add_more == "no":
        biding_finished = True

        # Get the higest bider
        find_highest_bider(biders=biders)
