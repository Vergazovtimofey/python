
# duration = int(input('введите время в секундах'))
# day = duration // 86400
# hour = (duration % 86400) // 3600
# minutes = ((duration % 86400) % 3600) // 60
# seconds = ((duration % 86400) % 3600) % 60
# print(f'{day} дней, {hour} часов, {minutes} минут, {seconds} секунд')

def my_func(duration):
    day = duration // 86400
    hour = (duration % 86400) // 3600
    minutes = ((duration % 86400) % 3600) // 60
    seconds = ((duration % 86400) % 3600) % 60
    print(f'{day} дней, {hour} часов, {minutes} минут, {seconds} секунд')


my_func(3400)
