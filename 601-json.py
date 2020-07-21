from json import dumps, loads
from dataclasses import *


@dataclass
class Pair:
    a: int
    b: int


if __name__ == '__main__':

    p1 = Pair(1,2)
    dumped = dumps(p1.__dict__)
    print(dumped)

    loaded = loads(dumped)
    print(loaded)
    p2 = Pair(**loaded)
    print(p2)
    p3 = Pair(a=1, b=2)