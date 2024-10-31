import random
l = [random.randint(-100,100)for i in range(random.randint(10,100))]

print(min(l))
print(max(l))
l.sort()
mediana=l[len(l)//2]
print(mediana)
