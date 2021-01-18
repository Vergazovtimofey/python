my_list = [7,5,3,3,2]
print(f'рейтинг {my_list}')
number = int(input('введите любое число которое мы поместим в рейтинг'))
for el in range(len(my_list)):
    if number >= 7:
        my_list.insert(0, number)
        print(my_list)
        break
    elif number == 7 or number >= 5:
        my_list.insert(1, number)
        print(my_list)
        break
    elif number >= 5 or number >= 3:
        my_list.insert(2, number)
        print(my_list)
        break
    elif number == 3 or number >= 2:
        my_list.insert(4, number)
        print(my_list)
        break
    elif number < 2:
        my_list.insert(5, number)
        print(my_list)
        break
