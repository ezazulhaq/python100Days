# set all the alphabets as an Array
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_chiper(direction, text, shift):
    blank_word = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabets:
            index = alphabets.index(letter)

            new_index = index + shift
            if new_index > 25:
                new_index = new_index - 26
            if new_index < 0:
                new_index = new_index + 26

            new_letter = alphabets[new_index]
            blank_word += new_letter
        else:
            blank_word += letter

    print(f"The {direction}d message is {blank_word}")
