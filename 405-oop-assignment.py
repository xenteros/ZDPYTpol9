"""
    Stwórz aplikację do zarządzania grupą studentów. Aplikacja powinna posiadać następujące funkcjonalności:
        1. Dodanie studenta do grupy:
            * imię,
            * nazwisko,
            * email
            * numer indeksu
            * lista wyników z kolokwiów
        2. Przechowywanie wyników z kolokwiów
        3. Zaimportowanie wyników egzaminu z pliku csv
        4. Obliczanie, kto będzie miał jaką ocenę.
        5. Aplikacja ma zapisywać stan do pliku. Po ponownym włączeniu, powinna mieć taki stan, jak przed wyłączeniem.
        6. Wykorzystaj wyrażenia regularne do walidacji danych. Wyrażenie do adresu email wyszukaj w necie, albo zrób wersję uproszczoną
        7. Wykorzystaj do walidacji jakiś dekorator (dzięki temu, będzie można zmieniać zasady walidacji bez zmieniania kodu, który odpowiada za tworzenie obiektów
        8. Wykorzystaj lambdę do liczenia oceny - ta lambda może być przechowywana w polu instancji klasy
"""



class Student:
    pass

class Classroom:
    pass

    def import_students():
        pass

    def import_results():
        pass

    def get_grades():
        pass

    def to_csv_file():
        """
            można oszukać i wyniki z kolokwiów zapisać jako stringa, żeby "mieściły się" w kolumnie, a przy odczycie pliku manualnie to konwertować do listy
        :return:
        """
        pass