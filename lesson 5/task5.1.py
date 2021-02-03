with open ('my_file.txt', 'w') as my_file:
    line = input("введите текст \n")
    while my_file:
        my_file.writelines(line)
        line = input('введите текст \n')
        if not line:
            break

