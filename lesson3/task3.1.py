def dell():
    a = int(input('введите первое число'))
    b = int(input('введите второе чило'))
    if b == 0:
        print('делить на ноль нельзя')
        return
    c = a / b

    print(f'деление ваших чисел {round(c, 3)}')

dell()