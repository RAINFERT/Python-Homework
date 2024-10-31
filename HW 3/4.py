import random


def vector():
    v = [random.randint(0, 255) for i in range(3)]
    v.append(random.randint(0, 1))
    lengthv = len(v)
    return v


ve = vector()


def matrix_multi(ve):
    s = []
    matrix_rgb = [[0.299, 0.587, 0.114], [0.5959, -0.2746, -0.3213], [0.2115, -0.5227, 0.3112]]
    matrix_yiq = [[1, 0.956, 0.619], [1, -0.272, -0.647], [1, -1.106, 1.703]]
    if ve[3] == 0:
        ma = matrix_rgb
    else:
        ma = matrix_yiq
    for i in range(3):
        t = 0
        for j in range(3):
            t += ma[i][j] * ve[j]
        s.append(t)
    print(s)


matrix_multi(ve)
