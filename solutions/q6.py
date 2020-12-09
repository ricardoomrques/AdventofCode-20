file = open("inputs/input6.txt","r")
answers = file.readlines()
for i in range(0,len(answers)):
    answers[i] = answers[i].strip("\n")

letters_seen = []
temp_letters_seen = []
result = 0
count = 0

for i in range(0,len(answers)):
    if (len(answers[i]) == 0):
        result += len(letters_seen)
        letters_seen = []
    else:
        for j in range(0,len(answers[i])):
            if (answers[i][j] not in letters_seen):
                letters_seen.append(answers[i][j])


print(result)
#--------------------PART2---------------------------------
file = open("inputs/input6.txt","r")
answers = file.readlines()
for i in range(0,len(answers)):
    answers[i] = answers[i].strip("\n")

letters_seen = []
temp_letters_seen = []
result = 0
count = 0

for i in range(0,len(answers)):
    if (len(answers[i]) == 0):
        for k in range(0,len(letters_seen)):
            if (letters_seen.count(letters_seen[k]) == count and letters_seen[k] not in temp_letters_seen):
                result += 1
                temp_letters_seen.append(letters_seen[k])
        letters_seen = []
        temp_letters_seen = []
        count = 0
    else:
        count += 1
        for j in range(0,len(answers[i])):
            letters_seen.append(answers[i][j])

temp_letters_seen = []

for k in range(0,len(letters_seen)):
            if (letters_seen.count(letters_seen[k]) == count and letters_seen[k] not in temp_letters_seen):
                result += 1
                temp_letters_seen.append(letters_seen[k])

print(result)
