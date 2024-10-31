a = []
for i in range(12):
    a.extend(['*', i + 1])

a.append('*')

s = 0
s_max = 5

for elem in a:
    print(elem, ' ', end='')
    s += 1
    if s == s_max:
        s = 0
        print()
