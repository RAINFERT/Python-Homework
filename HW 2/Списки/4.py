import random

r = [[random.randint(-100, 100) for i in range(100)] for j in range(100)]
v = [random.randint(-100, 100) for i in range(100)]
s = []
for i in range(len(r)):
    t = 0
    for j in range(len(v)):
        t += r[i][j] * v[j]
    s.append(t)
print(s)
