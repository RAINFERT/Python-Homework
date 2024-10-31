import random

l = [random.randint(-100, 100) for i in range(random.randint(10, 100))]

for i in range(len(l)):
    if l[i] < 0:
        u = i-1
        while l[u] < 0:
            u -= 1

        y = i+1
        if y == len(l):
            y = 0
        while l[y] < 0:
            if y == len(l)-1:
                y=0
            y += 1
        l[i] = (l[y]+l[u])/2
for i in range(len(l)):
    print(l[i], end=' ')
