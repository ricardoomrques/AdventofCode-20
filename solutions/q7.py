file = open("inputs/input7.txt","r")
sentences = file.readlines()

for i in range(0,len(sentences)):
    sentences[i] = sentences[i].strip("\n")

to_check = ["shiny gold bag"]
temp = []
temp2 = []  
matches = 1
result = 0

while (matches != 0):
    matches = 0
    for i in range(0,len(to_check)):
        for j in range(0,len(sentences)):
            if (sentences[j].count(to_check[i]) > 0 and sentences[j][0:sentences[j].index("contain") - 2] != to_check[i] and sentences[j][0:sentences[j].index("contain") - 2] not in temp2):
                matches += 1
                temp.append(sentences[j][0:sentences[j].index("contain") - 2])
                temp2.append(sentences[j][0:sentences[j].index("contain") - 2])
    to_check = temp
    temp = []
    result += matches


print(result)

#--------------------------------PART2----------------------------- 

#TO BE DONE