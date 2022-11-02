row1 = ["☐", "☐", "☐"]
row2 = ["☐", "☐", "☐"]
row3 = ["☐", "☐", "☐"]
# row1 = ["1", "2", "3"]
# row2 = ["4", "5", "6"]
# row3 = ["7", "8", "9"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
treasure_pos = list((input("Where do you want to put the treasure (row,column)? ")))
if int(treasure_pos[0]) - 1 < len(treasure_map[int(treasure_pos[0]) - 1]) and \
        int(treasure_pos[1]) - 1 < len(treasure_map[int(treasure_pos[1]) - 1]):
    treasure_map[int(treasure_pos[0]) - 1][int(treasure_pos[1]) - 1] = "🗷"
    print("Your treasure has been placed!")
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("Unable to place treasure in desired location")
