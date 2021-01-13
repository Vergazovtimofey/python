profit = int(input('выручка'))
cost = int(input('издержка'))
if profit > cost:
    print('прибыль')
    rent = ((profit - cost) / profit) * 100
    rent = round(rent)
    print(f'рентабильность фирмы в процентах {rent}')
    a = profit - cost
    men = int(input('количество человек в фирме'))
    z = a / men
    z = round(z, 2)
    print(f'выручка на одного сотрудника = {z}')
else:
    print('убыток')