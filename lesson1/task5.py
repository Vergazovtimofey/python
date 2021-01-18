profit = int(input('выручка'))
cost = int(input('издержка'))
if profit > cost:
    print('прибыль')
    rent = profit / cost
    print(f'рентабильность фирмы {rent}')
    a = profit - cost
    men = int(input('количество человек в фирме'))
    z = a / men
    print(f'выручка на одного сотрудника = {z}')
else:
    print('убыток')