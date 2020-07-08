class NegativeValueException(Exception):

    def __init__(self, num):
        self.negative_number = num

    def __str__(self):
        return f'{self.negative_number} is a negative number.'


def get_non_negative_number_from_user():
    while True:
        try:
            x = int(input('Please enter a positive number: '))
            if x <= 0:
                raise NegativeValueException(x)
            return x
        except NegativeValueException as nve:
            print(nve)
            print('The number should be non-negative')
        except ValueError:
            print('The input is not a valid number')



def get_number_from_user():
    while True:
        try:
            x = int(input('Please enter a number: '))
            return x
        except (ValueError, TypeError):
            print('The number was invalid')
        except NameError:
            pass
        except:
            pass


if __name__ == '__main__':
    print(get_non_negative_number_from_user())