import random

r = [random.randint(-100, 100) for i in range(random.randint(100, 100))]
f = [random.randint(-100, 100) for i in range(random.randint(1, len(r)-1))]
s = []
for i in range(len(r) - (len(f) - 1)):
    t = 0
    for j in range(len(f)):
        t += r[i + j] * f[j]
    s.append(t)
print(s)
