print('Введите счёт: ')
t_1, t_2 = input().split(sep=':')
if t_1 > t_2:
    print(1)
elif t_1 < t_2:
    print(2)
else:
    print(0)