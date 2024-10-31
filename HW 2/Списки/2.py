import random
l = [random.randint(0, 100) for i in range(20)]
a = [0] * 11
for u in l:
    a[u // 10] += 1
for i,j in enumerate(a):
    print(i,'-й бин содержит ',j,' элементов.')
for i, j in enumerate(a):
    print(i, '-й бин имеет вероятность - ', j/20)
