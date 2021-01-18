season_list = ['witer', 'spring', 'summer', 'autumn']
season_dict = {1: 'winer', 2: 'spring', 3: 'summer',4: 'autumn'}
n = int(input("введите порядковый номер месяц"))
if n == 12 or n == 1 or n == 2:
    print(season_list[0])
    print(season_dict.get(1))
elif n == 3 or n == 4 or n == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif n == 6 or n == 7 or n == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif n == 9 or n == 10 or n == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print('такого месяца не сущесвует')

