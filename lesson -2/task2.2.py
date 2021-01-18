user_list = list(input('введите произвольное количесво чисел'))
symbols = user_list
el = 0
for element in range(len(user_list) // 2):
    user_list[el], user_list[el + 1] = user_list[el + 1], user_list[el]
    el +=2
print(user_list)





























