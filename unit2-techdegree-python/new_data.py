from constants import TEAMS, PLAYERS
import sys
import time

all_players = [player['name'] for player in PLAYERS]

def get_player_experience(value):
    list = [dict['name'] for dict in PLAYERS if dict['experience'] == value]
    return list

all_experienced_players = get_player_experience('YES')
all_inexperienced_players = get_player_experience('NO')

def balance_experience(start_index, end_index):
    team = all_experienced_players[start_index:end_index] + all_inexperienced_players[start_index:end_index]
    return team

panthers = balance_experience(0, 3)
bandits = balance_experience(3, 6)
warriors = balance_experience(6, 9)


# Better way?
team_dict = {}
team_dict["Panthers"] = panthers
team_dict["Bandits"] = bandits
team_dict["Warriors"] = warriors


all_data = []
for team, name in team_dict.items():
    for player in PLAYERS:
        if player['name'] in name:
            player['team'] = team
            all_data.append(player)

# or longwinded list comprehension of dictionaries?
# all_data = [[(team, name) for team, name in team_dict.items()] for player in PLAYERS player['team'] = team if player['name'] in name]



def stats_message(team):
    print('\n' + "-*" * 20)
    print("          Team: {} Stats".format(team))
    print("-*" * 20, '\n')


def goodbye_message():
    print("\n*****Thank you for using BASKETBALL STATS TOOL*****")
    time.sleep(1)
    print('\n...Goodbye\n')
    time.sleep(1)


def total_players_message(number, names):
    print('\nTotal number of players: {}, \n {}'.format(number, names))


def guardian_message(names):
    print('\nGuardians: \n{}'.format(names))


def height_message(heights, average_height):
    print("\nHeights of team players:\n {}\n".format(heights))
    print("The team's average height is {} inches".format(average_height))


def experience_message(num_of_experienced_players, experiened_players, num_of_inexperienced_players, inexperienced_players):
    print('\nExperienced players: {}\n {}\n'.format(num_of_experienced_players, experiened_players),
    '\nInexperienced players: {}\n {}\n'.format(num_of_inexperienced_players, inexperienced_players))


def more_stats(*args):
    while True:
        try:
            args = input('\nWould you like to view more stats? [y]es/[n]o: ')
            if args.upper() != 'Y' and args.upper() != 'N':
                raise ValueError
            if args.upper() == 'Y':
                return args
            elif args.upper() == 'N':
                args = input('Would you like to return to the main menu? [y]es/[n]o: ')
                return args
        except ValueError:
            print('Please enter y or n.')


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


def view_stats():
    while True:
        try:
            stats = input("""\nWhich would you like to view?

        1) Guardians
        2) Heights
        3) Experience
        4) All stats
        > """)
            stats = int(stats)
            if stats > 4 or stats < 1:
                raise ValueError
            return stats
        except ValueError:
            print("Please choose an available option")


def make_new_list(value, list_key):
    list = [dictionary[list_key] for dictionary in all_data if dictionary['team'] == value]
    formatted_list = "- " + (', ').join(list)
    return len(list), formatted_list, list


def get_average_height(list):
    heights = [int(height.replace('inches', '')) for height in list]
    average_height = sum(heights) // len(heights)
    return average_height


def get_player_experience(value, answer):
    list = [dictionary['name'] for dictionary in all_data if dictionary['team'] == value and dictionary['experience'] == answer]
    formatted_list = "- " + (', ').join(list)
    return len(list), formatted_list


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
# show whole team each individual dict obj displayed nicely
