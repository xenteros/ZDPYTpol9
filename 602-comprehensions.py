from dataclasses import dataclass
from typing import *


@dataclass
class Address:
    street: str
    city: str
    country: str


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    address: Address


def users_names(users: List[User]):
    result = []
    for user in users:
        result.append(user.first_name)
    return result


def users_names_better(users: List[User]):
    return [user.first_name.upper() for user in users]


def warszawiacy(users: List[User]):
    return [user.first_name for user in users if user.address.city == 'Warszawa']


def foo(users: List[User]):
    return [user.first_name if user.address.city == 'Warszawa' else user.last_name for user in users]


def kobiety(users: List[User]):
    pass

def osoby_z_mailem_na_gmailu(users: List[User]):
    pass

def adresy_email_nie_gmaila(users: List[User]):
    pass

def imie_nazwisko_wszystkich(users: List[User]):
    #['jan_kowalski', 'danuta_nowak'...]
    pass

def uzytkownicy_pogrupowani_miastami(users: List[User]):
    """
        {
            'Warszawa': [...],
            'Wroclaw': [...],
            'Gdansk':[...]
    """
    pass

if __name__ == '__main__':
    a1 = Address('Krakowskie Przedmieście', 'Warszawa', 'Polska')
    a2 = Address('Aleje Jerozolimskie', 'Warszawa', 'Polska')
    a3 = Address('Kazimierza Wielkiego', 'Wrocław', 'Polska')
    a4 = Address('Bałtycka', 'Gdańsk', 'Polska')

    u1 = User(1, 'Jan', 'Kowalski', 'jan@kowalski.pl', a1)
    u2 = User(2, 'Danuta', 'Nowak', 'danuta.nowak@gmail.com', a2)
    u3 = User(3, 'Jacek', 'Sutryk', 'prezydent@wroclaw.pl', a3)
    u4 = User(4, 'Katarzyna', 'Gdańska', 'katarzyna.gdanska@gmail.com', a4)

    users = [u1, u2, u3, u4]
    print(users_names(users))
    print(users_names_better(users))
    print(warszawiacy(users))
