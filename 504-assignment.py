from dataclasses import dataclass

"""

    1. Mamy zdefiniowane składniki.
    2. Mamy zdefiniowane posiłki i ich cenę
    3. Możemy tworzyć zamówienia.
    4. Możemy przypisać kucharza do zamówienia.
    
    Wszystko zapisujemy do plików.
    Robimy najprościej jak się da.
    Menu aplikacji oparte o 1,2,3...

"""


class Meal:
    pass


@dataclass
class Ingredient:
    id: int
    name: str


class Order:
    pass


class Cook:
    pass
