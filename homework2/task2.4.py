s = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
     'токарь высшего разряда нИКОЛАй', 'директор аэлита']

s.append(s[0][20:40])
s.append(s[1][18:40])
s.append((s[2][23:40]))
s.append(s[3][9:30])

s.pop(0)
s.pop(0)
s.pop(0)
s.pop(0)
print(s)
my_str = "".join(s[0]).capitalize()
my_str1 = "".join(s[1]).capitalize()
my_str2 = "".join(s[2]).capitalize()
my_str3 = "".join(s[3]).capitalize()
print(my_str, my_str1, my_str2,my_str3)
print(f'Привет {my_str}')
print(f'Привет {my_str1}')
print(f'Привет {my_str2}')
print(f'Привет {my_str3}')



