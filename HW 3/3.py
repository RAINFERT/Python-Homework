import random


def matrix():
    m = [[[random.randint(0, 255) for i in range(50)] for i in range(60)] for j in range(3)]
    lengthm = len(m[0])
    return m, lengthm


ma = matrix()


def decorator(func):
    def wrapper(mm, lubov, kernel):
        for i in range(3):
            func(mm[i], lubov, kernel)

    return wrapper


matrix_svertka = [[random.randint(-1, 1) for i in range(4)] for j in range(3)]


@decorator
def svertka(ma, lengthm, kernel):
    b = []
    for i in range(lengthm - len(kernel) + 1):
        s = []
        for j in range(len(ma[0]) - len(kernel[0]) + 1):
            t = 0
            for k in range(len(kernel)):
                for l in range(len(kernel[0])):
                    t += ma[k + i][l + j] * kernel[k][l]
            s.append(t)
        b.append(s)
    print(b)


svertka(ma[0], ma[1], matrix_svertka)
