import time


class GameInterface:
    @staticmethod
    def get_number_of_teams():
        raise NotImplementedError

    @classmethod
    def get_team_names(cls, num_teams):
        raise NotImplementedError

    @classmethod
    def get_number_of_games_played(cls, number_of_teams):
        raise NotImplementedError

    def start_the_game(self):
        raise NotImplementedError


class Team(GameInterface):
    teams = []
    number_of_teams = 0

    def __init__(self, name):
        self.name = name
        self.win_games = 0
        self.played_games = 0
        Team.teams.append(self)
        Team.number_of_teams += 1

    def __str__(self):
        return self.name

    @classmethod
    def start_the_game(cls):
        number_of_teams = cls.get_number_of_teams()
        cls.get_team_names(number_of_teams)
        cls.get_number_of_games_played(number_of_teams)
        return cls.teams

    @classmethod
    def get_number_of_teams(cls):
        while True:
            num_teams = input('Enter the number of teams in the tournament: ')
            if not num_teams.isdigit() or int(num_teams) < 2:
                print('The minimum number of teams is 2, try again.')
            else:
                num_teams = int(num_teams)
                break

        return num_teams

    @classmethod
    def get_team_names(cls, num_teams):
        while True:
            for numer in range(num_teams):
                while True:
                    name_for_team = input(f'Enter the name for team #{numer + 1}: ')
                    if len(name_for_team) < 2:
                        print('Team names must have at least 2 characters, try again.')
                        continue
                    elif len(name_for_team.split(' ')) > 2:
                        print('Team names may have at most 2 words, try again.')
                        continue
                    else:
                        cls(name_for_team)
                        break
            break

    @classmethod
    def get_number_of_games_played(cls, num_teams):
        while True:
            number_of_games = int(input('Enter the number of games played by each team: '))
            if number_of_games < num_teams - 1:
                print('Invalid number of games. Each team plays each other at least once in the regular season, '
                      'try again.')
                continue

            for team in cls.teams:
                team.played_games = number_of_games
                while True:
                    wins = input(f'Enter the number of wins Team {team} had: ')
                    if not wins.isdigit() or int(wins) < 0:
                        print('The minimum number of wins is 0, try again.')
                    elif team.played_games < int(wins):
                        print(f'The maximum number of wins is {team.played_games}, try again.')
                    else:
                        team.win_games = int(wins)
                        break
            print()
            break


teams = Team.start_the_game()
print('Generating the games to be played in the first round of the tournament...', end='\n\n')
time.sleep(2)

teams = sorted(teams, key=lambda x: x.win_games)

for i in range(0, len(teams), 2):
    home_team = teams.pop(0)
    away_team = teams.pop(-1)
    print(f'Home: {home_team} VS Away: {away_team}')
