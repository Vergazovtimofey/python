rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []

with open("play.txt") as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('play_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)


