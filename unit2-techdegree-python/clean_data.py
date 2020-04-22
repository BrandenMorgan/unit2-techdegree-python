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


panthers_list = balance_experience(0, 3)
bandits_list = balance_experience(3, 6)
warriors_list = balance_experience(6, 9)

teams = [{"Panthers": panthers_list}, {"Bandits": bandits_list}, {"Warriors": warriors_list}]
panthers = teams[0]
bandits = teams[1]
warriors = teams[2]


def get_players(name_of_team):
    list = []
    for team in teams:
        for team_name, team_value in team.items():
            for player in PLAYERS:
                for value in team_value:
                    if value in player['name'] and team_name == name_of_team:
                        list.append(player['name'])

    return list

print('Panther players:',len(get_players('Panthers')), get_players('Panthers'))

def get_guardians(name_of_team):
    list = []
    new_list = []
    for team in teams:
        for team_name, team_value in team.items():
            for player in PLAYERS:
                for value in team_value:
                    if value in player['name'] and team_name == name_of_team:
                        list.append(player['guardians'])
    for guardian in list:
        string = (', ').join(guardian)
        new_list.append(string)

    return new_list


panthers_guardians = get_guardians('Panthers')
print('Guardians:', panthers_guardians)


def get_heights(name_of_team):
    list = []
    for team in teams:
        for team_name, team_value in team.items():
            for player in PLAYERS:
                for value in team_value:
                    if value in player['name'] and team_name == name_of_team:
                        list.append(player['height'])
    average = sum(list) // len(list)
    return average


heights = get_heights('Panthers')
print('Average height:', heights)


def experienced(name_of_team):
    list = []
    for team in teams:
        for team_name, team_value in team.items():
            for player in PLAYERS:
                for value in team_value:
                    if value in player['name'] and team_name == name_of_team and player['experience'] == True:
                        list.append(player['name'])
    return list

print('Experienced players:',len(experienced('Panthers')), experienced('Panthers'))

def inexperienced(name_of_team):
    list = []
    for team in teams:
        for team_name, team_value in team.items():
            for player in PLAYERS:
                for value in team_value:
                    if value in player['name'] and team_name == name_of_team and player['experience'] == False:
                        list.append(player['name'])
    return list

print('Inexperienced players:', len(inexperienced('Panthers')), inexperienced('Panthers'))



def display_stats(team_list):
     display_message = (', ').join(team_list)
     return display_message
print('Panther players:', display_stats(get_players('Panthers')))
