def odd_nums(num: int):
    return (x for x in range(1, num + 1, 2))

try:
    odd_to_15 = odd_nums(15)
    while True:
        print(next(odd_to_15))
except StopIteration:
    print('done')