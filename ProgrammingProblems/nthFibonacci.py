fibDict = {1: 0, 2: 1, 3: 1}


def getNthFib(n):
    # Write your code here
    if n in fibDict:
        return fibDict[n]
    else:
        fibDict[n] = getNthFib(n - 1) + getNthFib(n - 2)
        return fibDict[n]


print(getNthFib(4))
