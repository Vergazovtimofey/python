try:
     with open("sum.txt", 'w+') as my_file:
         text = input('введите цифры через пробел')
         my_file.writelines(text)
         my_text = text.split()

         print(sum(map(int, my_text)))
except IOError:
        print('Ошибка в файле')
except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')