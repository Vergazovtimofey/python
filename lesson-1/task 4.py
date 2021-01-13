user = int(input('введите число'))
max = user % 10
user = user // 10
while user > 0:
    if user % 10 > max:
         max = user % 10
    user = user // 10
print(max)

