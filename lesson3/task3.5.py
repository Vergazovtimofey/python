def my_func():
    summa = 0
    exit = 1
    while exit == 1:
        number = input("введите числа через пробел или напишите Q для выхода")
        number = number.split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit = 0
                break
            else:
                result = result + int(number[el])
        summa = summa + result
        print(f'промежуточный результат{summa}')
    print(f'конечный результат{summa}')


my_func()