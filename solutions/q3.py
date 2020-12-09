file = open("inputs/input3.txt","r")
maps = file.readlines()

for i in range(0,len(maps)):
    maps[i] = maps[i].strip("\n")

index_line = 0
index_map = 0
count_trees = 0

while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees += 1
    index_map += 3
    index_line += 1


print(count_trees)
#--------------------------------------PART2--------------------------------
file = open("inputs/input3.txt","r")
maps = file.readlines()

for i in range(0,len(maps)):
    maps[i] = maps[i].strip("\n")
    
index_line = 0
index_map = 0
count_trees1 = 0
while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees1 += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees1 += 1
    index_map += 3
    index_line += 1

index_line = 0
index_map = 0
count_trees2 = 0
while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees2 += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees2 += 1
    index_map += 1
    index_line += 1

index_line = 0
index_map = 0
count_trees3 = 0
while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees3 += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees3 += 1
    index_map += 5
    index_line += 1

index_line = 0
index_map = 0
count_trees4 = 0
while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees4 += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees4 += 1
    index_map += 7
    index_line += 1

index_line = 0
index_map = 0
count_trees5 = 0
while (index_line <= len(maps) - 1):
    if (index_map - len(maps[0]) >= 0 and index_line != len(maps) - 1): 
        index_map = index_map % len(maps[0])
        if (maps[index_line][index_map] == '#'):
            count_trees5 += 1
    else:
        if (maps[index_line][index_map] == '#'):
            count_trees5 += 1
    index_map += 1
    index_line += 2


print(count_trees1 * count_trees2 * count_trees3 * count_trees4 * count_trees5)

