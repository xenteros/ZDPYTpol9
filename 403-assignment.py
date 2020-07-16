def lower_case(func):
    def lower_case_wrapper(*args, **kwargs):
        for line in func(*args, **kwargs):
            yield line.lower()

    return lower_case_wrapper


@lower_case
def lazy_read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print('lazy_read just read the line')
            yield line


def slow():
    pass


if __name__ == '__main__':
    for line in lazy_read('books.csv'):
        print(line, end='')