my_list = []

rows = 2
columns = 3

for row in range(rows):
    my_list.append([])
    for column in range(columns):
        value = float(input("enter a number for row " + str(row) + ", column " + str(column) + ": "))
        my_list[row].append(value)

print(my_list)

# Sum each column
for column in range(columns):
    total = 0
    for row in range(rows):
        total += my_list[row][column]
    print("Sum for column", column, "=", total)

# Sum each row
for row in range(rows):
    total = 0
    for column in range(columns):
        total += my_list[row][column]
    print("Sum for row", row, "=", total)
