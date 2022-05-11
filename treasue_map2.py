# Don't change the code below
row1 = ["😈", "😃", "😢"]
row2 = ["😢", "😃", "🤥"]
row3 = ["🤥", "😢", "😈"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Write your code below this row

# row first, column next
horizontal = int(position[0])
vertical = int(position[1])

# print(map[horizontal -1])
# print(map[vertical - 1])

map[vertical - 1][horizontal - 1] = "X"

# Don't change the code below
print(f"{row1}\n{row2}\n{row3}")