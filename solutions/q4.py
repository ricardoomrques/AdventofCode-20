file = open("inputs/input4.txt","r")
passport_inputs = file.readlines()
final_passwords = []
temp = []
count = 0
valid = 0
for i in range(0,len(passport_inputs)):
    if (passport_inputs[i] == "\n"):
        final_passwords.append(temp)
        temp = []
    else:
        passport_inputs[i] = passport_inputs[i].strip("\n")
        temp.append(passport_inputs[i])

for i in range(0,len(final_passwords)):
    for j in range(0,len(final_passwords[i])):
        if (final_passwords[i][j].count("ecl") > 0):
            count += 1
        if (final_passwords[i][j].count("pid") > 0):
            count += 1
        if (final_passwords[i][j].count("eyr") > 0):
            count += 1
        if (final_passwords[i][j].count("hcl") > 0):
            count += 1
        if (final_passwords[i][j].count("byr") > 0):
            count += 1
        if (final_passwords[i][j].count("iyr") > 0):
            count += 1
        if (final_passwords[i][j].count("hgt") > 0):
            count += 1
    if (count == 7):
        valid += 1
    count = 0


print(valid)
#---------------------------------PART2--------------------------
file = open("inputs/input4.txt","r")
passport_inputs = file.readlines()

final_passwords = []
temp = []
valid = 0
count = 0

for i in range(0,len(passport_inputs)):
    if (passport_inputs[i] == "\n"):
        final_passwords.append(temp)
        temp = []
    else:
        passport_inputs[i] = passport_inputs[i].strip("\n")
        temp += passport_inputs[i].split(" ")

for i in range(0,len(final_passwords)):
    for j in range(0,len(final_passwords[i])):
        if (final_passwords[i][j].count("ecl") > 0):
            if (final_passwords[i][j][4:] == 'amb' or final_passwords[i][j][4:] == 'blu' or final_passwords[i][j][4:] == 'brn' or
            final_passwords[i][j][4:] == 'gry' or final_passwords[i][j][4:] == 'grn' or final_passwords[i][j][4:] == 'hzl' or
            final_passwords[i][j][4:] == 'oth'):
                count += 1
        if (final_passwords[i][j].count("pid") > 0):
            if (len(final_passwords[i][j][4:]) == 9):
                count += 1
        if (final_passwords[i][j].count("eyr") > 0):
            if (int(final_passwords[i][j][4:]) >= 2020 and int(final_passwords[i][j][4:]) <= 2030):
                count += 1
        if (final_passwords[i][j].count("hcl") > 0):
            if (len(final_passwords[i][j][5:]) == 6 and final_passwords[i][j][5:].isalnum()):
                count += 1
        if (final_passwords[i][j].count("byr") > 0):
            if (int(final_passwords[i][j][4:]) >= 1920 and int(final_passwords[i][j][4:]) <= 2002):
                count += 1
        if (final_passwords[i][j].count("iyr") > 0):
            if (int(final_passwords[i][j][4:]) >= 2010 and int(final_passwords[i][j][4:]) <= 2020):
                count += 1
        if (final_passwords[i][j].count("hgt") > 0):
            if (final_passwords[i][j][::-1][0:2] == "mc" and int(final_passwords[i][j][4:len(final_passwords[i][j]) - 2]) >= 150 and int(final_passwords[i][j][4:len(final_passwords[i][j]) - 2]) <= 193):
                count += 1
            elif (final_passwords[i][j][::-1][0:2] == "ni" and int(final_passwords[i][j][4:len(final_passwords[i][j]) - 2]) >= 59 and int(final_passwords[i][j][4:len(final_passwords[i][j]) - 2]) <= 76):
                count += 1
    if (count == 7):
        valid += 1
    count = 0

print(valid)
