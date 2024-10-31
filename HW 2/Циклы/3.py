import random
def guess(a,b):
    c = random.randint(a,b)
    print('Ожидаются ответы: "да" и "нет"')
    while True:
        print(f'Число равно {c} ?')
        an = input().lower()
        if an =='да':
            print('Я Угадал!')
            break
        else:
            print(f'Это число меньше {c} ?')
            ann = input().lower()
            if ann == 'да':
                b=c-1
            else:
                a=c+1
            c = random.randint(a, b)
a,b=map(int,input('Введите интервал через пробел:' ).split())
guess(a,b)
