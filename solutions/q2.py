file = open("inputs/input2.txt","r")
passwords = file.readlines()
list_with_tuples = []
empty_tuple = ()
for i in range(0,len(passwords)):
    empty_tuple += (int(passwords[i][0:passwords[i].find("-")]),)
    empty_tuple += (int(passwords[i][passwords[i].find("-") + 1:passwords[i].find(" ")]),)
    empty_tuple += (passwords[i][passwords[i].find(" ") + 1:passwords[i].find(":")],)
    empty_tuple += (passwords[i][passwords[i].find(":") + 2:].strip("\n"),)
    list_with_tuples.append(empty_tuple)
    empty_tuple = ()
valid = 0
count = 0

for i in range(0,len(list_with_tuples)):
    for j in range(0,len(list_with_tuples[i][3])):
        if (list_with_tuples[i][3][j] == list_with_tuples[i][2]):
            count += 1
    if (count >= list_with_tuples[i][0] and count <= list_with_tuples[i][1]):
        valid += 1
    count = 0

print(valid)

#--------------------------PART2---------------------------
file = open("inputs/input2.txt","r")
passwords = file.readlines()
list_with_tuples = []
empty_tuple = ()
for i in range(0,len(passwords)):
    empty_tuple += (int(passwords[i][0:passwords[i].find("-")]),)
    empty_tuple += (int(passwords[i][passwords[i].find("-") + 1:passwords[i].find(" ")]),)
    empty_tuple += (passwords[i][passwords[i].find(" ") + 1:passwords[i].find(":")],)
    empty_tuple += (passwords[i][passwords[i].find(":") + 2:].strip("\n"),)
    list_with_tuples.append(empty_tuple)
    empty_tuple = ()
valid = 0
count = 0

for i in range(0,len(list_with_tuples)):
    if (list_with_tuples[i][0] - 1 < len(list_with_tuples[i][3])):
        if (list_with_tuples[i][3][list_with_tuples[i][0] - 1] == list_with_tuples[i][2]):
            count += 1
    if (list_with_tuples[i][1] - 1 < len(list_with_tuples[i][3])):
        if (list_with_tuples[i][3][list_with_tuples[i][1] - 1] == list_with_tuples[i][2]):
            count += 1
    if (count == 1):
        valid += 1
    count = 0

print(valid)