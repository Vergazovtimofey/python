def my_func():
    a = int(input('первое число'))
    b = int(input('второе число'))
    c = int(input('третье число'))
    d = min(a, b, c)
    if a == d:
        print(b + c)
        return
    elif b == d:
        print(a + c)
        return
    elif c == d:
        print(a + b)
        return

my_func()


