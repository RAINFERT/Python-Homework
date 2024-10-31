import random

print('1 пункт')
def vector():
    v = [random.uniform(0, 1) for i in range(7)]
    lengthv = len(v)
    return v, lengthv


print(vector())
ve = vector()

print('2 пункт')
def matrix(lengthv):
    m = [[random.uniform(0, 1) for i in range(lengthv)] for j in range(6)]
    lengthm = len(m)
    return m, lengthm


ma = matrix(ve[1])

print()

print('3 пункт')
def matrix_multi(ma, ve, lengthv, lengthm):
    s = []

    for i in range(lengthm):
        t = 0
        for j in range(lengthv):
            t += ma[i][j] * ve[j]
        s.append(t)
    print(s)


matrix_multi(ma[0], ve[0], ve[1], ma[1])
print()

print('4 пункт')
def print_matrix(ma, lengthm, lengthv):
    for i in range(lengthm):
        for j in range(lengthv):
            print(ma[i][j], end=' ')
        print()


print_matrix(ma[0], ma[1], ve[1])
print()

print('5 пункт')
def print_vector(ve, lengthv):
    for i in range(lengthv):
        print(ve[i], end=' ')


print_vector(ve[0], ve[1])

print('6 пункт')
def matrix_diag(ma, lengthm):
    p = 0
    for i in range(lengthm):
        p += ma[i][i]
    print(p)


matrix_diag(ma[0], ma[1])

print()

print('7 пункт')
def svertka(ma, lengthv, lengthm):
    matrix_svertka = [[random.uniform(0, 1) for i in range(lengthv - 3)] for j in range(3)]
    b = []
    for i in range(lengthm - len(matrix_svertka) + 1):
        s = []
        for j in range(len(ma[0]) - len(matrix_svertka[0]) + 1):
            t=0
            for k in range(len(matrix_svertka)):
                for l in range(len(matrix_svertka[0])):
                    t += ma[k + i][l + j] * matrix_svertka[k][l]
            s.append(t)
        b.append(s)
    print(b)
    print('Ядро свертки:')
    print(matrix_svertka)


svertka(ma[0], ve[1], ma[1])
