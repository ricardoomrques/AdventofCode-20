file = open("inputs/input5.txt","r")
seats = file.readlines()
for i in range(0,len(seats)):
    seats[i] = seats[i].strip("\n")

max_id = 0
current_id = 0
min_row = 0
max_row = 127
min_col = 0
max_col = 7
col = 0
row = 0
id_list = []
potential_ids = []

for i in range(0,len(seats)):
    for j in range(0,len(seats[i])):
        if (min_row + 1 == max_row and seats[i][j] == "F"):
            row = min_row
        elif (min_row + 1 == max_row and seats[i][j] == "B"):
            row = max_row
        elif (min_col + 1 == max_col and seats[i][j] == "R"):
            col = max_col
        elif (min_col + 1 == max_col and seats[i][j] == "L"):
            col = min_col
        elif (seats[i][j] == "F"):
            max_row = int((max_row - min_row) / 2) + min_row
        elif (seats[i][j] == "B"):
            min_row = int((max_row - min_row) / 2) + min_row + 1
        elif (seats[i][j] == "L"):
            max_col = int((max_col - min_col) / 2) + min_col
        elif (seats[i][j] == "R"):
            min_col = int((max_col - min_col) / 2) + min_col + 1
    current_id = row * 8 + col
    if (current_id > max_id):
        max_id = current_id
    current_id = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    col = 0
    row = 0

#----------------------------------PART2--------------------------------------
file = open("inputs/input5.txt","r")
seats = file.readlines()
for i in range(0,len(seats)):
    seats[i] = seats[i].strip("\n")

max_id = 0
current_id = 0
min_row = 0
max_row = 127
min_col = 0
max_col = 7
col = 0
row = 0
id_list = []

for i in range(0,len(seats)):
    for j in range(0,len(seats[i])):
        if (min_row + 1 == max_row and seats[i][j] == "F"):
            row = min_row
        elif (min_row + 1 == max_row and seats[i][j] == "B"):
            row = max_row
        elif (min_col + 1 == max_col and seats[i][j] == "R"):
            col = max_col
        elif (min_col + 1 == max_col and seats[i][j] == "L"):
            col = min_col
        elif (seats[i][j] == "F"):
            max_row = int((max_row - min_row) / 2) + min_row
        elif (seats[i][j] == "B"):
            min_row = int((max_row - min_row) / 2) + min_row + 1
        elif (seats[i][j] == "L"):
            max_col = int((max_col - min_col) / 2) + min_col
        elif (seats[i][j] == "R"):
            min_col = int((max_col - min_col) / 2) + min_col + 1
    current_id = row * 8 + col
    if (current_id > max_id):
        max_id = current_id
    current_id = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    col = 0
    row = 0

for i in range(0,len(seats)):
    for j in range(0,len(seats[i])):
        if (min_row + 1 == max_row and seats[i][j] == "F"):
            row = min_row
        elif (min_row + 1 == max_row and seats[i][j] == "B"):
            row = max_row
        elif (min_col + 1 == max_col and seats[i][j] == "R"):
            col = max_col
        elif (min_col + 1 == max_col and seats[i][j] == "L"):
            col = min_col
        elif (seats[i][j] == "F"):
            max_row = int((max_row - min_row) / 2) + min_row
        elif (seats[i][j] == "B"):
            min_row = int((max_row - min_row) / 2) + min_row + 1
        elif (seats[i][j] == "L"):
            max_col = int((max_col - min_col) / 2) + min_col
        elif (seats[i][j] == "R"):
            min_col = int((max_col - min_col) / 2) + min_col + 1
    current_id = row * 8 + col
    id_list.append(current_id)
    current_id = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    col = 0
    row = 0

id_list.sort()

for i in range(0,len(id_list) - 1):
    if (id_list[i + 1] - id_list[i] != 1):
        print(id_list[i] + 1)
