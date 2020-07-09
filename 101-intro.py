def foo():
    try:
        x = int(input('Please enter a number: '))
    except ValueError as value_error:
        print('The number was invalid')
    else:
        return x


def bar():
    with open('books.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass

    bar()
