def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


func = add(4, 5, 6)

print(func)


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)

print(calculate)

