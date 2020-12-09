file = open("inputs/input8.txt","r")
commands = file.readlines()

for i in range(0,len(commands)):
    commands[i] = commands[i].strip("\n")

index_seen = []
temp = []
result = 0
index = 0

while (index not in index_seen and index < len(commands)):
    index_seen.append(index)
    if (commands[index][0:3] == "nop"):
        index += 1 
    elif (commands[index][0:3] == "acc"):
        if (commands[index][4] == "+"):
            result += int(commands[index][5:])
        elif (commands[index][4] == "-"):
            result -= int(commands[index][5:])
        index += 1
    else:
        if (commands[index][4] == "+"):
            index += int(commands[index][5:])
        elif (commands[index][4] == "-"):
            index -= int(commands[index][5:])

print(result)

#------------------------------PART2------------------------------



    