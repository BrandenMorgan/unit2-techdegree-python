# New Version
import clean_data
import sys
from constants import TEAMS, PLAYERS


experienced_players = clean_data.get_player_experience(True)
inexperienced_players = clean_data.get_player_experience(False)

def balance_experience(start_index, end_index):
    team = experienced_players[start_index:end_index] + inexperienced_players[start_index:end_index]
    return team

panthers = balance_experience(0, 3)
bandits = balance_experience(3, 6)
warriors = balance_experience(6, 9)

def team_stats(team):
    player_list = clean_data.make_list(team, 'name')
    guardians = clean_data.make_guardians_list(team, 'guardians')
    average_height = clean_data.average_height(team)
    experienced_players = clean_data.get_experience(team, True)
    inexperienced_players = clean_data.get_experience(team, False)

    clean_data.total_players_message(len(player_list),  "- " + (', ').join(player_list))
    keep_viewing = clean_data.keep_viewing()


    def view_all_stats_message(team):
        clean_data.total_players_message(len(player_list),  "- " + (', ').join(player_list))
        clean_data.guardian_message(guardians.replace(' and', ','))
        clean_data.height_message(average_height)
        clean_data.experience_message(len(experienced_players), "- " + (', ').join(experienced_players),
                            len(inexperienced_players),  "- " + (', ').join(inexperienced_players))
        keep_viewing = clean_data.keep_viewing()
        return keep_viewing

    # Checks if the user wants to continue viewing stats
    if keep_viewing.upper() in ['Y', 'YES']:
        stats = clean_data.view_stats()
        # Print Team Guardians
        if stats == 1:
            clean_data.guardian_message(guardians.replace(' and', ','))
            keep_viewing = clean_data.keep_viewing()
            if keep_viewing.upper() in ['N', 'NO']:
                return keep_viewing
        # Print Team Average Height
        elif stats == 2:
            clean_data.height_message(average_height)
            keep_viewing = clean_data.keep_viewing()
            if keep_viewing.upper() in ['N', 'NO']:
                return keep_viewing
        # Print Players Via Experience
        elif stats == 3:
            clean_data.experience_message(len(experienced_players), "- " + (', ').join(experienced_players),
                                        len(inexperienced_players), "- " + (', ').join(inexperienced_players))
            keep_viewing = clean_data.keep_viewing()
            if keep_viewing.upper() in ['N', 'NO']:
                return keep_viewing
        # Print all stats
        elif stats == 4:
            keep_viewing = view_all_stats_message(team)

    if keep_viewing.upper() in ['N', 'NO']:
        clean_data.goodbye_message()
        sys.exit()
    return keep_viewing


def start_program():
    while True:
        clean_data.main_menu()
        team = clean_data.get_user_team()
        if team == 1:
            clean_data.stats_message('Panthers')
            keep_viewing = team_stats(panthers)
            if keep_viewing.upper() in ['N', 'NO']:
                clean_data.goodbye_message()
                break
        elif team == 2:
            clean_data.stats_message('Bandits')
            keep_viewing = team_stats(bandits)
            if keep_viewing.upper() in ['N', 'NO']:
                clean_data.goodbye_message()
                break
        elif team == 3:
            clean_data.stats_message('Warriors')
            keep_viewing = team_stats(warriors)
            if keep_viewing.upper() in ['N', 'NO']:
                clean_data.goodbye_message()
                break


if __name__ == '__main__':
    start_program()
