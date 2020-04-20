from new_data import (
    all_players, get_player_experience, balance_experience, all_data, stats_message,
    goodbye_message, total_players_message, guardian_message, height_message, experience_message,
    more_stats, main_menu, view_stats, make_new_list, get_average_height, get_player_experience, get_user_team,
    get_users_choice
)
import sys

def team_stats(team):
    stats_message(team)
    player_list = make_new_list(team, 'name')
    total_players_message(player_list[0], player_list[1])
    view_more_stats = more_stats()
    if view_more_stats.upper() in ['Y', 'YES']:
        stats = view_stats()
        if stats == 1:
            guardians = make_new_list(team, 'guardians')
            guardian_message(guardians[1].replace(' and', ','))
            view_more_stats = more_stats(view_more_stats)
            if view_more_stats.upper() in ['N', 'NO']:
                return view_more_stats
        elif stats == 2:
            height_list = make_new_list(team, 'height')
            average_height = get_average_height(height_list[2])
            height_message(height_list[1], average_height)
            view_more_stats = more_stats(view_more_stats)
            if view_more_stats.upper() == 'N':
                return view_more_stats
        elif stats == 3:
            experienced_players = get_player_experience(team, 'YES')
            inexperienced = get_player_experience(team, 'NO')
            experience_message(experienced_players[0], experienced_players[1],
                                inexperienced[0], inexperienced[1])
            view_more_stats = more_stats(view_more_stats)
            if view_more_stats.upper() == 'N':
                return view_more_stats
        elif stats == 4:
            total_players_message(player_list[0], player_list[1])
            guardians = make_new_list(team, 'guardians')
            guardian_message(guardians[1].replace(' and', ','))
            height_list = make_new_list(team, 'height')
            average_height = get_average_height(height_list[2])
            height_message(height_list[1], average_height)
            experienced_players = get_player_experience(team, 'YES')
            inexperienced = get_player_experience(team, 'NO')
            experience_message(experienced_players[0], experienced_players[1],
                                inexperienced[0], inexperienced[1])
            view_more_stats = more_stats(view_more_stats)
            if view_more_stats.upper() in ['N', 'NO']:
                return view_more_stats
    if view_more_stats.upper() in ['N', 'NO']:
        goodbye_message()
        sys.exit()
    return view_more_stats


def start_program():
    while True:
        main_menu()
        team = get_user_team()
        if team == 1:
            view_more_stats = team_stats('Panthers')
            if view_more_stats.upper() in ['N', 'NO']:
                goodbye_message()
                break
        elif team == 2:
            view_more_stats = team_stats('Bandits')
            if view_more_stats.upper() in ['N', 'NO']:
                goodbye_message()
                break
        elif team == 3:
            view_more_stats = team_stats('Warriors')
            if view_more_stats.upper() in ['N', 'NO']:
                goodbye_message()
                break

                
if __name__ == '__main__':
    start_program()
