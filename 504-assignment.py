from dataclasses import dataclass
from typing import *

"""

    1. Mamy zdefiniowane składniki.
    2. Mamy zdefiniowane posiłki i ich cenę
    3. Możemy tworzyć zamówienia.
    4. Możemy przypisać kucharza do zamówienia.
    
    Wszystko zapisujemy do plików.
    Robimy najprościej jak się da.
    Menu aplikacji oparte o 1,2,3...

"""


@dataclass
class Ingredient:
    FILE_NAME = 'ingredients.csv'
    FROM_SPLIT_MAPPER = lambda x: Ingredient(int(x[0]), x[1])
    TO_SPLIT_MAPPER = None

    id: int
    name: str


@dataclass
class Meal:
    FILE_NAME = 'meals.csv'
    FROM_SPLIT_MAPPER = None
    TO_SPLIT_MAPPER = None

    id: int
    name: str
    ingredients: List[Ingredient]


class Order:
    pass


class Cook:
    pass


def read_ingredients():
    return read_csv_file(Ingredient.FILE_NAME, Ingredient.FROM_SPLIT_MAPPER)


def read_meals():
    read_csv_file(Meal.FILE_NAME, Meal.FROM_SPLIT_MAPPER)


def write_ingredients(ingredients: List[Ingredient]):
    with open(Ingredient.FILE_NAME, 'w', encoding='utf-8') as f:
        for ingredient in ingredients:
            f.write(f'{ingredient.id};{ingredient.name}\n')


def read_csv_file(file_name, mapper, encoding='utf-8'):
    with open(file_name, 'r', encoding=encoding) as f:
        for line in f:
            yield mapper(line.strip().split(';'))


if __name__ == '__main__':
    for i in read_ingredients():
        print(i)
