import time
import functools

def parent():
    print("I'm a parent.")

    def child1():
        print("I'm the first child.")

    def child2():
        print("I'm the second child.")

    child1()
    child2()


def upper_case(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper()


def stoper(func):
    def wrapper():
        start = time.time()  # current time in seconds
        result = func()
        end = time.time()  # current time in seconds
        print(f'{func.__name__} took {(end - start)//1} seconds')
        return result

    return wrapper


def slow(_func=None, *, how_many_seconds=1):

    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(how_many_seconds)
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


@stoper
@slow(how_many_seconds=2)
def bar():
    return 'bar'


@upper_case
def foo():
    return 'foo'


if __name__ == '__main__':
    bar()
