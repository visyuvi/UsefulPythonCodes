L1 = [2, 3, 4]
L2 = [5, 3, 7]

L1n = sorted(L1, reverse=True)

L2n = sorted(L2, reverse=True)


s = 0
for i in range(len(L1)):
    s += (max(L1n[i], L2n[i]))
print(s)


L2n = sorted(L2)

s = 0
for i in range(len(L1)):
    s += (max(L1n[i], L2n[i]))
print(s)
 