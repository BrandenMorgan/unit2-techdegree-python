from constants import TEAMS, PLAYERS


all_players = [player['name'] for player in PLAYERS]

for player in PLAYERS:
    player['guardians'] = [player['guardians']]
    player['height'] = int(player['height'].replace('inches', ''))
    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False


def get_player_experience(value):
    list = [dict['name'] for dict in PLAYERS if dict['experience'] == value]
    return list


experienced_players = get_player_experience(True)
inexperienced_players = get_player_experience(False)


def balance_experience(start_index, end_index):
    team = experienced_players[start_index:end_index] + inexperienced_players[start_index:end_index]
    return team


panthers = balance_experience(0, 3)
bandits = balance_experience(3, 6)
warriors = balance_experience(6, 9)

def get_guardians(team):
    for member in team:
        for player in PLAYERS:
            if member in team and player['name'] == member:
                print(player['guardians'])
get_guardians(panthers)

team_dict = {"Panthers": panthers, "Bandits": bandits, "Warriors": warriors}


def make_new_list(value, list_key):
    list = [dictionary[list_key] for dictionary in PLAYERS if dictionary['team'] == value]
    return list

def get_player_list(team):
    team = (', ').join(team_dict[team])
    return team

panthers_players = get_player_list('Panthers')
bandits_players = get_player_list('Bandits')
warriors_players = get_player_list('Warriors')
