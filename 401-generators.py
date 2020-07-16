def foo():
    print('foo')


def bar():
    while True:
        pass


def natural_numbers():
    i = 0
    while True:
        yield i
        i += 1


def some_numbers():
    result = []
    for i in range(100):
        result.append(i)
    return result


def some_numbers2():
    for i in range(100):
        yield i


def all_even_numbers():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1

    i = 0
    while True:
        yield i
        i += 2


def fibonacci():
    a = 1
    b = 1
    yield 1
    yield 1
    while True:
        c = a + b
        a = b
        b = c
        yield b


if __name__ == '__main__':
    print(some_numbers())
    print(some_numbers2())
    print(list(some_numbers2()))

    fib = fibonacci()

    for i in range(10):
        print(next(fib))

    # 1 1 2 3 5 8 13 21 34 ....
