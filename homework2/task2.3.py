my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# z = my_list.index('5')
# c = my_list.index('+5')
# my_list[z] = '05'
# my_list[c] = '+05'
i = 0


while i < 10:
    if not my_list[i].isdigit() :
        my_list.append(my_list[i])
    elif my_list[i].isdigit() < 17:
        my_list.append('"')
        my_list.append(my_list[i].zfill(2))
        my_list.append('"')
    elif my_list[i] == '+-':
        my_list.append('"')
        my_list.append(my_list[i].zfill(3))
        my_list.append('"')

    else:
        my_list.append('"')
        my_list.append(my_list[i])
        my_list.append('"')

    i += 1

z = 0
while z < len(my_list):
    if my_list[z] == '+5':
        my_list.append('"')
        my_list.append(my_list[z].zfill(3))
        my_list.append('"')
        my_list.append(my_list[z+1])
    z += 1

my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(13)
my_list.pop(12)
my_list.pop(-1)
my_list.pop(-1)
my_list.pop(-1)
my_list.pop(-1)
print(my_list)
my_str = " ".join(my_list)
print(my_str)

