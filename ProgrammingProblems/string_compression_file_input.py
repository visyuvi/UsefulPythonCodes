# Take input from file
with open("input.txt", "r") as f:
    L = f.readlines()

for line in L:  # for each input
    line = line.strip()

    newStr = ""
    last = line[0]
    count = 1

    for char in line[1:]:  # For every character except the first

        if char == last:
            count += 1
        else:
            newStr += str(count) + " " + last + " "
            count = 1
            last = char

    newStr += str(count) + " " + last

    print(newStr)
     