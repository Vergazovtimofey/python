my_list = [23, 1, 3, 5, 12, 16, 36, 67, 75]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(new_list)
