from new_data import *


def start_program():
    while True:
        main_menu()
        team = get_user_team()
        if team == 1:
            stats_message('Panthers')
            panthers_player_list = make_new_list('Panthers', 'name')
            total_players_message(panthers_player_list[0], panthers_player_list[1])
            view_more_stats = more_stats()
            if view_more_stats.upper() == 'Y':
                stats = view_stats()
                if stats == 1:
                    panthers_guardians = make_new_list('Panthers', 'guardians')
                    guardian_message(panthers_guardians[1].replace(' and', ','))
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 2:
                    panthers_height_list = make_new_list('Panthers', 'height')
                    panthers_average_height = get_average_height(panthers_height_list[2])
                    height_message(panthers_height_list[1], panthers_average_height)
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 3:
                    panthers_experienced_players = get_player_experience('Panthers', 'YES')
                    panthers_inexperienced = get_player_experience('Panthers', 'NO')
                    experience_message(panthers_experienced_players[0], panthers_experienced_players[1],
                                        panthers_inexperienced[0], panthers_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 4:
                    total_players_message(panthers_player_list[0], panthers_player_list[1])
                    panthers_guardians = make_new_list('Panthers', 'guardians')
                    guardian_message(panthers_guardians[1].replace(' and', ','))
                    panthers_height_list = make_new_list('Panthers', 'height')
                    panthers_average_height = get_average_height(panthers_height_list[2])
                    height_message(panthers_height_list[1], panthers_average_height)
                    panthers_experienced_players = get_player_experience('Panthers', 'YES')
                    panthers_inexperienced = get_player_experience('Panthers', 'NO')
                    experience_message(panthers_experienced_players[0], panthers_experienced_players[1],
                                        panthers_inexperienced[0], panthers_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
            elif view_more_stats.upper() == 'N':
                goodbye_message()
                break


        elif team == 2:
            stats_message('Bandits')
            bandits_player_list = make_new_list('Bandits', 'name')
            total_players_message(bandits_player_list[0], bandits_player_list[1])
            view_more_stats = more_stats()
            if view_more_stats.upper() == 'Y':
                stats = view_stats()
                if stats == 1:
                    bandits_guardians = make_new_list('Bandits', 'guardians')
                    guardian_message(bandits_guardians[1].replace(' and', ','))
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 2:
                    bandits_height_list = make_new_list('Bandits', 'height')
                    bandits_average_height = get_average_height(bandits_height_list[2])
                    height_message(bandits_height_list[1], bandits_average_height)
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 3:
                    bandits_experienced_players = get_player_experience('Bandits', 'YES')
                    bandits_inexperienced = get_player_experience('Bandits', 'NO')
                    experience_message(bandits_experienced_players[0], bandits_experienced_players[1],
                                         bandits_inexperienced[0], bandits_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 4:
                    total_players_message(bandits_player_list[0], bandits_player_list[1])
                    bandits_guardians = make_new_list('Bandits', 'guardians')
                    guardian_message(bandits_guardians[1].replace(' and', ','))
                    bandits_height_list = make_new_list('Bandits', 'height')
                    bandits_average_height = get_average_height(bandits_height_list[2])
                    height_message(bandits_height_list[1], bandits_average_height)
                    bandits_experienced_players = get_player_experience('Bandits', 'YES')
                    bandits_inexperienced = get_player_experience('Bandits', 'NO')
                    experience_message(bandits_experienced_players[0], bandits_experienced_players[1],
                                         bandits_inexperienced[0], bandits_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
            elif view_more_stats.upper() == 'N':
                goodbye_message()
                break

        elif team == 3:
            stats_message('Warriors')
            warriors_player_list = make_new_list('Warriors', 'name')
            total_players_message(warriors_player_list[0], warriors_player_list[1])
            view_more_stats = more_stats()
            if view_more_stats.upper() == 'Y':
                stats = view_stats()
                if stats == 1:
                    warriors_guardians = make_new_list('Warriors', 'guardians')
                    guardian_message(warriors_guardians[1].replace(' and', ','))
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 2:
                    warriors_height_list = make_new_list('Warriors', 'height')
                    warriors_average_height = get_average_height(warriors_height_list[2])
                    height_message(warriors_height_list[1], warriors_average_height)
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 3:
                    warriors_experienced_players = get_player_experience('Warriors', 'YES')
                    warriors_inexperienced = get_player_experience('Warriors', 'NO')
                    experience_message(warriors_experienced_players[0], warriors_experienced_players[1],
                                        warriors_inexperienced[0], warriors_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
                elif stats == 4:
                    total_players_message(warriors_player_list[0], warriors_player_list[1])
                    warriors_guardians = make_new_list('Warriors', 'guardians')
                    guardian_message(warriors_guardians[1].replace(' and', ','))
                    warriors_height_list = make_new_list('Warriors', 'height')
                    warriors_average_height = get_average_height(warriors_height_list[2])
                    height_message(warriors_height_list[1], warriors_average_height)
                    warriors_experienced_players = get_player_experience('Warriors', 'YES')
                    warriors_inexperienced = get_player_experience('Warriors', 'NO')
                    experience_message(warriors_experienced_players[0], warriors_experienced_players[1],
                                        warriors_inexperienced[0], warriors_inexperienced[1])
                    view_more_stats = more_stats(view_more_stats)
                    if view_more_stats.upper() == 'N':
                        goodbye_message()
                        break
        elif view_more_stats.upper() == 'N':
            goodbye_message()
            break


if __name__ == '__main__':
    start_program()
