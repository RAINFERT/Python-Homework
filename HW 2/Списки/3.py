import random
import math

l = [random.randint(-100, 100) for i in range(random.randint(100, 100))]
r = [random.randint(-100, 100) for i in range(len(l))]
summa = [random.randint(-100, 100) for i in range(len(l))]
multi = [random.randint(-100, 100) for i in range(len(l))]
scal = [random.randint(-100, 100) for i in range(len(l))]
number = int(input())

for i in range(len(summa)):
    summa[i] = l[i] + r[i]
for i in range(len(multi)):
    multi[i] = l[i] * r[i]
s = 0
for i in range(len(l)):
    s += l[i] ** 2
s = math.sqrt(s)
f = 0
for i in range(len(r)):
    f += r[i] ** 2
f = math.sqrt(f)
if f > s:
    for i in range(len(r)):
        scal[i] = number * r[i]
else:
    for i in range(len(l)):
        scal[i] = number * l[i]
print('Первый вектор =',l)
print('Второй вектор =',r)
print('Сумма =',summa)
print('Произведение =',multi)
print('Скалярное произведение =',scal)
