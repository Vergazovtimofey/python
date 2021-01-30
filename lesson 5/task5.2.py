with open("text.txt") as f_obj:
    num1 = 0
    num2 = 0
    for num, line in enumerate(f_obj, start=1):
        num1 = 1
        num2 = num2 + num1
        print(f'номер строки {num}, количество знаков в строке {len(line)}')
    print(f'сумарное количесво строк {num2}')
with open("text.txt") as f_obj:
    content = f_obj.read()
    content = content.split()
    print(f'Общее количество слов {len(content)}')

