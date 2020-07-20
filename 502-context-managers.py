class File(object):
    def __init__(self, file_name, mode, encoding='utf-8'):
        self.file = open(file_name, mode, encoding=encoding)
        self.name = file_name

    def __enter__(self):
        print(self.name)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':
    with File('books.csv', 'r') as f:
        for line in f:
            print(line, end='')