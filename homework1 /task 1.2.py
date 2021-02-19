my_list = list(range(1, 1000, 2))
user_list = []
for i in my_list:
    i = i ** 3

    if i % 7 == 0:
        user_list.append(i)

    elif (i + 17) % 7 == 0:
        user_list.append(i)
        print(sum(user_list))

print(sum(user_list))
print(sum(user_list))
'''
# вторая версия решения задачи
 '''
# my_list = [el ** 3 for el in range(1, 1000, 2) if el % 7 == 0 or (el + 17) % 7 == 0]
# print(sum(my_list))
