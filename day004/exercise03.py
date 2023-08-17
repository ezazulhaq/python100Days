# Treasure map exercise

# Take row1, row2 and row3 with values
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Take the position of the treasure
position = input("Where do you want to put the treasure? ")

# Convert the position to a number
column = int(position[0])
row = int(position[1])

map[row - 1][column - 1] = "X"

# Print the map
print(f"{row1}\n{row2}\n{row3}")
