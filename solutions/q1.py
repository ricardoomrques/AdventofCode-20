file = open("inputs/input1.txt","r")
numbers = file.readlines()
result = 0
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i])

for j in range(0,len(numbers) - 1):
    for k in range(j + 1, len(numbers)):
        if (numbers[j] + numbers[k] == 2020):
            result = numbers[j] * numbers[k]

#--------------------PART2----------------------

file = open("inputs/input1.txt","r")
numbers = file.readlines()
result = 0
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i])
    
for j in range(0,len(numbers) - 2):
    for k in range(j + 1, len(numbers) - 1):
        for m in range(k + 1, len(numbers)):
            if (numbers[j] + numbers[k] + numbers[m] == 2020):
                result = numbers[j] * numbers[k] * numbers[m]
    
print(result)