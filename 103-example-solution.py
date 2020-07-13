class TeamAlreadyRegisteredException(Exception):
    pass


class IllegalScoreException(Exception):
    pass


class League:

    def __init__(self):
        self.teams = set()
        with open('teams.csv', 'r', encoding='utf-8') as f:
            next(f)
            for line in f:
                self.teams.add(line.split(';')[-1].strip())
                pass
            if line.startswith('id'):
                last_id = 0
            else:
                last_id = int(line.strip().split(';')[0])
            self.next_id = last_id + 1

    def register_team(self):
        # print('register_team')
        team_name = input('What is the team name? ')
        if team_name in self.teams:
            raise TeamAlreadyRegisteredException
        self.teams.add(team_name)
        with open('teams.csv', 'a', encoding='utf-8') as teams:
            teams.write(f'{self.next_id};{team_name}\n')
            self.next_id += 1

    def display_all_teams(self):
        with open('teams.csv', 'r', encoding='utf-8') as f:
            first_line = next(f).strip().split(';')
            print(' | '.join(first_line))
            for team in f:
                print(' | '.join(team.strip().split(';')))

    def add_result(self):
        print('add_result')
        home = input('Who was the home team?')
        away = input('Who was the away team?')
        score = input(f'What was the score? ([{home} score]:[{away} score])')

        if not (home in self.teams and away in self.teams):
            raise IllegalScoreException #todo custom exception class

        try:
            home_score, away_score = [int(s) for s in score.split(':')]
        except ValueError:
            raise IllegalScoreException
        else:
            with open('results.csv', 'a', encoding='utf-8') as f:
                #id;home;away;home_score;away_score
                f.write(f'0;{home};{away};{home_score};{away_score}')


    def display_all_results(self):
        print('display_all_results')

    def display_standings(self):
        """
        Displays a standing, where 3 points are given for a win, 1 point for a draw and 0 for a loss.
        :return:
        """
        print('display_standings')

    def display_menu(self):
        print()
        print('1. Display all teams.')
        print('2. Display all results.')
        print('3. Display standings.')
        print('4. Register a team.')
        print('5. Register a result.')
        print('6. Exit.')
        print()

    def run(self):
        while True:
            self.display_menu()
            try:
                user_choice = int(input())
            except:
                pass
            else:
                if user_choice == 1:
                    self.display_all_teams()
                elif user_choice == 2:
                    pass
                elif user_choice == 3:
                    pass
                elif user_choice == 4:
                    self.register_team()
                elif user_choice == 5:
                    self.add_result()
                elif user_choice == 6:
                    return
                else:
                    pass


if __name__ == '__main__':
    league = League()
    league.run()