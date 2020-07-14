"""
    Napisz własny silnik, który będzie w stanie sprawdzić, czy dany napis pasuje do wyrażenia regularnego.
    Trochę ustaleń:
        1. Nie robimy maszynki do wyszukiwania pasujących napisów w długim tekście, a maszynkę do sprawdzania
            czy dany napis w całości pasuje do wyrażenia
        2. Ograniczamy się do następujących elementów składni wyrażenia regularnego:
            * wzorce dosłowne (np. a, b, abc, foo)
            * modyfikatory liczby wystąpień: + i *
           [*]2 klasy znaków: [a-z] oraz [A-Z]
"""

#todo gdzieś trzeba zrobić sprawdzenie czy wierzchołek sukcesu się świeci

class Node:

    def __init__(self, green):
        self.transitions = dict()
        self.activated = False
        self.is_green = green

    def activate(self):
        self.activated = True

    def deactivate(self):
        self.activated = False

    def transition(self, letter):
        pass
        #todo

    def add_transition(self, letter, node): # trzeba się zastanowić, czy node jest tutaj potrzebny czy nie
        pass
        #todo


def create_automata(regex):
    pass
    #todo sprawdzenie czy regex jest poprawny - zawiera tylko te symbole na które się zgodziliśmy w poleceniu
    #todo pocięcie regexa na wierzchołki (transitions) ab+c -> [a, b+, c]
    #todo stworzenie całego automatu z odpowiednimi wierzchołkami

