file = open("inputs/input9.txt","r")
numbers = file.readlines()
valid = False
result = 0
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i].strip("\n"))

jump_index = 1

for i in range(25,len(numbers)):
    for j in range(i - 25, i - 1):
        for k in range(i - 24,i):
            if (numbers[j] + numbers[k] == numbers[i]):
                valid = True
    if (valid == False):
        result = numbers[i]
    valid = False

valid = True

print(result)
#---------------------------------PART2------------------------------
file = open("inputs/input9.txt","r")
numbers = file.readlines()
valid = False
result = 0
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i].strip("\n"))

jump_index = 1

for i in range(25,len(numbers)):
    for j in range(i - 25, i - 1):
        for k in range(i - 24,i):
            if (numbers[j] + numbers[k] == numbers[i]):
                valid = True
    if (valid == False):
        result = numbers[i]
    valid = False

valid = True

while (valid == True):
    for i in range(0,len(numbers)):
        if (sum(numbers[i : jump_index]) == result):
            valid = False
            result = max(numbers[i : jump_index]) + min(numbers[i : jump_index])
    jump_index += 1

print(result)

