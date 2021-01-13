user_answer = int(input('введите время в секундах'))
hours = user_answer // 3600
minutes = user_answer // 60
seconds = user_answer
print(f'часы: {hours} минуты: {minutes} секунды:{seconds}')


#вторая версия программы если не правильно понял задание
user_answer1 = int(input('введите время в секундах'))
hours1 = user_answer1 // 3600
ost = user_answer1 % 3600
minutes1 = ost // 60
ost2 = ost % 60
seconds1 =  ost2
print(f'часы: {hours1}   минуты: {minutes1} секунды:{seconds1} ')
