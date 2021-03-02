'''
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
'''

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# z = my_list.index('5')
# c = my_list.index('+5')
# my_list[z] = '05'
# my_list[c] = '+05'
i = 0
new_list = []

while i < len(my_list):
    if not my_list[i].isdigit() :
        new_list.append(my_list[i])
    elif my_list[i].isdigit() < 17:
        new_list.append('"')
        new_list.append(my_list[i].zfill(2))
        new_list.append('"')
    elif my_list[i] == '+-':
        new_list.append('"')
        new_list.append(my_list[i].zfill(3))
        new_list.append('"')

    else:
        new_list.append('"')
        new_list.append(my_list[i])
        new_list.append('"')

    i += 1
new_list.pop()
new_list.pop()
z = 0
while z < len(my_list):
    if my_list[z] == '+5':
        new_list.append('"')
        new_list.append(my_list[z].zfill(3))
        new_list.append('"')
        new_list.append(my_list[z+1])
    z += 1


print(new_list)
my_str = " ".join(new_list)
print(my_str)







