class ValidationException(Exception):
    """
    Klasa ma służyć temu, aby ktoś kto dostaje obiekt np. usera mógł sprawdzić wszystkie pola (imię, nazwisko, email)
    tego usera, wszystkie błędy wrzucić/opakować w wyjątek i wyrzucić do tego, kto takiego niepoprawnego usera mu
    dostarczył.

    Po wydrukowaniu takiego wyjątku, powinny się wydrukować wszystkie problemy związane z obiektem.

    Do wyjątku przekazywany będzie dict, gdzie kluczami będą nazwy pól (np. imię), a wartościami będą
    kody problemów (np. 'CANNOT_BE_BLANK').


    Kody będą stringami.
    """
    def __init__(self, issues):
        self.issues = issues

    def __str__(self):
        messages = [f'{key} : {value}' for key,value in self.issues.items()]
        return ','.join(messages)

class User:

    def __init__(self, firstname, lastname, email, phone):
        self.phone = phone
        self.email = email
        self.lastname = lastname
        self.firstname = firstname


def validate(user):
    problems = dict()
    if user.firstname is None:
        problems['firstname'] = 'CANNOT_BE_NONE'
    if not '@' in user.email:
        problems['email'] = 'MISSING_OBLIGATORY_AT_CHARACTER'
    if len(problems) > 0:
        raise ValidationException(problems)


if __name__ == '__main__':
    user = User(None, 'Kowalski', 'temp', 'acb')
    try:
        validate(user)
    except ValidationException as ve:
        print(ve)
        for field in ve.issues:
            print(f'{field} : {ve.issues[field]}')