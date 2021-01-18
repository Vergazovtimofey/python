a = int(input('пробежал в первый день'))
b = int(input('должен пробежать'))
c = 1
while b >= a:
    a = a + a * 0.1
    c +=1
    a = round(a, 2)
    print(f'номер дня{c} количесво км в этот день {a}')
