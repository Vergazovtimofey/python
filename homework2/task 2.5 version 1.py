my_list = [46.02, 23.7, 22.4, 98.89, 45.22, 34.09, 15.44, 76.05, 98.22,
           76.32, 33.03, 55.05, 66.66, 77.07, 88.08, 99.09, 23.09, 66.02, 34.54, 20.20]
new_list = []
print('цены')
for i in my_list:
    if i > 0:
        z = i // 1
        z = z.__round__()
        a = i % (i // 1)
        a = a.__round__(2)
        a = int(a * 100)
        if a < 10:
            a = f'0{a}'
        q = (f'{z} руб {a} коп')
        new_list.append(q)
        # new_list.insert(el+1, a)

# print(new_list)
my_str =", ".join(new_list)
print(my_str)

'''
список отсортированый по возрастанию
'''


new_list.clear()
my_list.sort()
print("цены по возрастанию")
for i in my_list:
    if i > 0:
        z = i // 1
        z = z.__round__()
        a = i % (i // 1)
        a = a.__round__(2)
        a = int(a * 100)
        if a < 10:
            a = f'0{a}'
        q = (f'{z} руб {a} коп')
        new_list.append(q)
        # new_list.insert(el+1, a)

# print(new_list)
my_str =", ".join(new_list)
print(my_str)

'''
список отсортированый по убыванию
'''
new_list.clear()
my_list.sort(reverse = True)
print("цены по убыванию")
for i in my_list:
    if i > 0:
        z = i // 1
        z = z.__round__()
        a = i % (i // 1)
        a = a.__round__(2)
        a = int(a * 100)
        if a < 10:
            a = f'0{a}'
        q = (f'{z} руб {a} коп')
        new_list.append(q)
        # new_list.insert(el+1, a)

# print(new_list)
my_str =", ".join(new_list)
print(my_str)

"""
первые 5 самых дорогих товаров
"""
print('первые 5 самых дорогих товаров')
new_list.clear()
my_list.sort(reverse=True)
p = 0
while p < 5:
    new_list.append(my_list[p])
    p += 1
my_list.clear()
for i in new_list:
    if i > 1:
        z = i // 1
        z = z.__round__()
        a = i % (i // 1)
        a = a.__round__(2)
        a = int(a * 100)
        if a < 10:
            a = f'0{a}'
        q = (f'{z} руб {a} коп')
        my_list.append(q)

my_str =", ".join(my_list)
print(my_str)
