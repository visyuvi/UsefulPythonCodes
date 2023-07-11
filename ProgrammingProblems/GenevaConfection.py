testCases = int(input())
List = []

# take input for each of the test cases
for x in range(testCases):
    List.append([])
    f = input()  # Number of elements
    for y in range(int(f)):
        List[x].append(int(input()))  # List of elements

# for each of the test case do the following

for x in range(testCases):
    carList = List[x]
    branch = []
    current = 1

    while True:

        if len(carList):
            if carList[-1] == current:
                carList.pop()
                current += 1
            elif len(branch):
                if branch[-1] == current:
                    branch.pop()
                    current += 1
                else:
                    branch.append(carList.pop())
            else:
                branch.append(carList.pop())

        elif len(branch):
            if branch[-1] == current:
                branch.pop()
                current += 1
            else:
                print('N')
                break
        else:
            print('Y')
            break

