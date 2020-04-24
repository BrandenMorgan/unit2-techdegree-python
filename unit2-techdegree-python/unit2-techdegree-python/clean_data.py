from constants import TEAMS, PLAYERS
import copy
import sys
import time


players_dict = copy.deepcopy(PLAYERS)

for player in players_dict:
    player['guardians'] = [player['guardians']]
    player['height'] = int(player['height'].replace('inches', ''))
    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False


def get_player_experience(value):
    list = [dict for dict in players_dict if dict['experience'] == value]
    return list


def goodbye_message():
    print("\n*****Thank you for using BASKETBALL STATS TOOL*****")
    time.sleep(1)
    print('\n...Goodbye\n')
    time.sleep(1)


def make_list(list, key):
    new_list = [player[key] for player in list]
    return new_list


def display_stats(team_list):
     display_message = (', ').join(team_list)
     return display_message


def make_guardians_list(list, key):
    new_list = [player[key] for player in list]
    guardian_list = [(', ').join(guardian) for guardian in new_list]
    message = display_stats(guardian_list)
    return message


def average_height(team):
    heights = make_list(team, 'height')
    average_height = sum(heights) // len(heights)
    return average_height


def get_experience(list, bool):
    new_list = [player['name'] for player in list if player['experience'] == bool]
    return new_list


def stats_message(team):
    print('\n' + "-*" * 20)
    print("          Team: {} Stats".format(team))
    print("-*" * 20, '\n')


def total_players_message(number, names):
    print('\nTotal number of players: {} \n {}'.format(number, names))


def guardian_message(names):
    print('\nGuardians: \n - {}'.format(names))


def height_message(average_height):
    print("\nThe team's average height is {} inches".format(average_height))


def experience_message(num_of_experienced_players, experiened_players, num_of_inexperienced_players, inexperienced_players):
    print('\nExperienced players: {}\n {}\n'.format(num_of_experienced_players, experiened_players),
    '\nInexperienced players: {}\n {}\n'.format(num_of_inexperienced_players, inexperienced_players))


def keep_viewing(*args):
    while True:
        try:
            args = input('\nWould you like to view more stats? [y]es/[n]o: ')
            if args.upper() not in ['Y', 'YES'] and args.upper() not in ['N', 'NO']:
                raise ValueError
            if args.upper() in ['Y', 'YES']:
                return args
            elif args.upper() in ['N', 'NO']:
                return args
        except ValueError:
            print('Oops... Please enter y or n.')


def view_stats():
    while True:
        try:
            stats = input("""\nWhich would you like to view?

        1) Guardians
        2) Average height
        3) Experience
        4) All stats
        > """)
            stats = int(stats)
            if stats > 4 or stats < 1:
                raise ValueError
            return stats
        except ValueError:
            print("Please choose an available option")


def main_menu():
    print("  \nBASKETBALL STATS TOOL\n")
    print("----MENU----\n")
    choice = get_users_choice()
    if choice == 1:
        print("\n")
        for number, team in enumerate(TEAMS, 1):
            print(number, ")", team)
    elif choice == 2:
        sys.exit(goodbye_message())


def get_users_choice():
    while True:
        try:
            choice = int(input("""Here are your choices:

        1) Display Team Stats
        2) Quit

Enter an option > """))
            choice = int(choice)
            if choice <= 0 or choice > 2:
                raise ValueError
            return choice
        except ValueError:
            print("Please enter a valid choice.\n")


def get_user_team():
    while True:
        try:
            team = int(input("\nSelect one of the above teams > "))
            team = int(team)
            if team > 3 or team < 1:
                raise ValueError
            return team
        except ValueError:
            print("Please enter a valid choice.\n")
