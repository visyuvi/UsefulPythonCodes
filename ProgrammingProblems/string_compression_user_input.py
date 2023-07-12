# code to take input

n = int(input("Enter number of items"))
print("Enter input one line at a time")
L = []
A = []

for _ in range(n):
    L.append(input())

for i in range(n):
    x = L[i]
    c = 1
    j = 0
    a = ""
    while j < len(x) - 1:
        if x[j] != x[j + 1]:
            a += str(c) + " "
            a += x[j] + " "
            j += 1
            c = 1
        else:
            c += 1
            j += 1
    a += str(c) + " "
    a += x[j] + " "
    A.append(a)

print(A)
