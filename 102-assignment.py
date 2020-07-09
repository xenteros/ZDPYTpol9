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


def register_team(next_id):
    print('register_team')
    team_name = input('What is the team name? ')
    with open('teams.csv', 'a', encoding='utf-8') as teams:
        teams.write(f'{next_id};{team_name}\n')


def display_all_teams():
    with open('teams.csv', 'r', encoding='utf-8') as f:
        first_line = next(f).strip().split(';')
        print(' | '.join(first_line))
        for team in f:
            print(' | '.join(team.strip().split(';')))


def add_result():
    print('add_result')
    home = input('Who was the home team?')
    away = input('Who was the away team?')
    score = input(f'What was the score? ([{home} score]:[{away} score])')
    #todo sprawdzenie, czy takie drużyny istnieją, czy wynik jest legalny (np nieujemny) itd.
    #todo zapis wyniku do pliku


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


def initialize(teams='teams.csv', results='results.csv'):
    with open(teams, 'r', encoding='utf-8') as f:
        for line in f:
            pass
        if line.startswith('id'):
            return 1
        last_id = int(line.strip().split(';')[0])
        next_id = last_id + 1

    return next_id


def run():
    next_id = initialize()
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
                register_team(next_id)
                next_id += 1
            elif user_choice == 5:
                pass
            elif user_choice == 6:
                return
            else:
                pass


if __name__ == '__main__':
    run()
