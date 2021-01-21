# def my_fuct():
#     a = int(input('введите число'))
#     b = int(input('введите отрицательную степень'))
#     c = a ** b
#     print(round(c, 5))
#
# my_fuct()
#
# def my_function():
#     a = int(input('введите число'))
#     b = int(input('введите отрицательную степень'))
#     c = pow(a, b)
#     print(c)
#
# my_function()

def my_function1():
    a = int(input('введите число'))
    b = int(input('введите отрицательную степень'))
    n = 1
    while n <= abs(b):
        n = n + 1
        g = 1 / (a * a)
        print(g)



my_function1()