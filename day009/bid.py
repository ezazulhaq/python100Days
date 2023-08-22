
def store_bider(name, bid):
    return {
        "name": name,
        "bid": bid
    }


def find_highest_bider(biders):
    # Print out the highest bid
    highest_bid = 0
    winner = ""
    for bidder in biders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            winner = bidder["name"]

    print(f"The winner is {winner} with a bid of ${highest_bid}.")
