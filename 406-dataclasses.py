from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str

    @classmethod
    def from_csv_string(cls, row, sep=';'):
        if not Student.is_csv_string_proper(row, sep):
            raise Exception()
        params = row.split(sep)
        print(params)
        return cls(*params)

    @staticmethod
    def is_csv_string_proper(row, sep=';'):
        return len(row.split(sep)) == 3

    def foo(self):
        print(self.first_name)


class StudentOld:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


def print_wrapper(a, b, *args, foo=None, **kwargs):
    for arg in args:
        print(arg)

    for kwarg in kwargs:
        print(f'{kwarg}={kwargs[kwarg]}')



if __name__ == '__main__':
    student = Student('Jan', 'Kowalski', 'jan@kowalski.com')
    student = Student.from_csv_string('krzysztof;nowak;krzysztof@gmail.com')
    print_wrapper("Ala", "ma", "kota", foo='bar', eggs='spam')
