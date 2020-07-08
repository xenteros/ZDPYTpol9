def foo():
    print('foo')
    raiser()

def bar():
    print('bar')
    try:
        foo()
    except ValueError as e:
        print('I gatta u ' + str(e))

def spam():
    print('spam')
    bar()

def raiser():
    int('foo')

if __name__ == '__main__':
    spam()

