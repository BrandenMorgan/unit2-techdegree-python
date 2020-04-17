from constants import TEAMS, PLAYERS


def make_new_list(list_of_dicts, key, value, list_key):
    list = []
    for dictionary in list_of_dicts:
        if dictionary[key] == value:
            list.append(dictionary[list_key])
            formatted_list = "- " + (', ').join(list)
    return len(list), formatted_list # change tuple to accomodate length of players

panthers_player_list = make_new_list(PLAYERS, 'team', 'Panthers', 'name')
number_of_players, player_names = panthers_player_list[0], panthers_player_list[1]
print('\nTotal number of players:', number_of_players, '\n', player_names)

panthers_height_list = make_new_list(PLAYERS, 'team', 'Panthers', 'height')
panthers_heights = panthers_height_list[1]
print("\nHeights of team players:", '\n', panthers_heights)

panthers_experience = make_new_list(PLAYERS, 'team', 'Panthers', 'name')
panthers_num_of_experienced_players = panthers_experience[0]
print('\nExperienced players:', panthers_num_of_experienced_players)

panthers_guardians = make_new_list(PLAYERS, 'team', 'Panthers', 'guardians')
panthers_guardian_names = panthers_guardians[1].replace('and', ',')
print('\nGuardians:', '\n', panthers_guardian_names)
