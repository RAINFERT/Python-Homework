def sum():
    for a in range(1,10,1):
        for b in range(1,10,1):
            print(a+b, end=' ')
        print()
def minus():
    for a in range(1,10,1):
        for b in range(1,10,1):
            print(a-b, end=' ')
        print()
def multi():
    for a in range(1,10,1):
        for b in range(1,10,1):
            print(a*b, end=' ')
        print()
def div():
    for a in range(1,10,1):
        for b in range(1,10,1):
            print('{:.3}'.format(a/b), end=' ')
        print()
x = input()
def choice(x):
    if x == '+':
        return sum()
    if x == '-':
        return minus()
    if x == '*':
        return multi()
    if x == '/':
        return div()
v = choice(x)
