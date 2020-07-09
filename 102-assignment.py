"""
1. Stwórz aplikację konsolową do zarządzania wydarzeniem sportowym.
2. Aplikacja powinna mieć następujące funkcjonalności:
    a) rejestracja/dodanie zawodnika czy drużyny - zawodnik/druzyna w zależności od wybranego sportu (zespołowy lub indywidualny)
    b) podgląd zapisanych zawodników czy drużyn
    c) zapisanie wyniku spotkania
    d) wyświetlenie wyników
    e) wyświetlenie tabeli
3. Od początku (od 2a) wszystko co jest dodawane przez użytkownika od razu zapisujemy do pliku i ten plik zamykamy.
4. Gdy czytamy z pliku, od razu ten plik zamykamy po przeczytaniu tego, co nas interesowało.
5. Lepiej używać kilku plików niż jednego (pierwszy plik na zapisywanie listy zawodników, a drugi na wyniki)
6. Dopuszczamy tylko jedną drużynę o danej nazwie.
"""


def register_team():
    print('register_team')


def display_all_teams():
    with open('teams.csv', 'r', encoding='utf-8') as f:
        first_line = next(f).strip().split(';')
        print(' | '.join(first_line))
        for team in f:
            print(' | '.join(team.strip().split(';')))


def add_result():
    print('add_result')


def display_all_results():
    print('display_all_results')


def display_standings():
    print('display_standings')


def display_menu():
    print()
    print('1. Display all teams.')
    print('2. Display all results.')
    print('3. Display standings.')
    print('4. Register a team.')
    print('5. Register a result.')
    print('6. Exit.')
    print()


def run():
    while True:
        display_menu()
        try:
            user_choice = int(input())
        except:
            pass
        else:
            if user_choice == 1:
                display_all_teams()
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                pass
            elif user_choice == 4:
                pass
            elif user_choice == 5:
                pass
            elif user_choice == 6:
                return
            else:
                pass

if __name__ == '__main__':
    run()