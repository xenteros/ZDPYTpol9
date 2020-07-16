def foo(i, fun):
    print(fun(i))


if __name__ == '__main__':
    for i in range(20):
        doubler = lambda x: 2 * x
        foo(i, doubler)

    for i in range(10):
        foo(i, lambda x: x ** 2)
