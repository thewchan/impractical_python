"""
Pseudo-code:
ask for number of length of key
initiate defaultdict
for count in length of key
    ask for column number store as temp1
    ask for direction store as temp2
    defaultdict[temp1] = temp2
"""
from collections import defaultdict

while True:
    key_len = input("Enter length of key: ")
    try:
        key_len = int(key_len)
    except ValueError:
        print("Please enter a number.")
        continue
    break

key_stored = defaultdict(int)

for column in range(key_len):
    while True:
        column_num = input(f"Enter column number for position {column + 1}: ")
        try:
            column_num = int(column_num)
        except ValueError:
            print("Please enter a number.")
            continue
        if (column_num > 0 and column_num <= key_len):
            break
        else:
            print("Please enter a valid column number.")
            continue
    while True:
        direction = input(
            f"Enter direction of position {column + 1} (up/down): "
            )
        if direction.lower() == 'up':
            direction = -1
            break
        elif direction.lower() == 'down':
            direction = 1
            break
        else:
            print("Please enter a valid direction (up/down).")
            continue
    key_stored[column_num] = direction

print("The key you have entered is:\n ", key_stored)
