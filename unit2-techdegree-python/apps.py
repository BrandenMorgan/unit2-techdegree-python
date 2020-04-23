# Old Version
# import new_data
# import sys
#
#
# def team_stats(team):
#     player_list = new_data.make_new_list(team, 'name')
#     guardians = new_data.make_new_list(team, 'guardians')
#     guardians = "- " + (', ').join(guardians)
#     height_list = new_data.make_new_list(team, 'height')
#     average_height = new_data.get_average_height(height_list)
#     experienced_players = new_data.get_player_experience(team, 'YES')
#     inexperienced = new_data.get_player_experience(team, 'NO')
#
#     new_data.stats_message(team)
#     new_data.total_players_message(len(player_list),  "- " + (', ').join(player_list))
#     keep_viewing = new_data.keep_viewing()
#
#
#     def view_all_stats_message(team):
#         new_data.total_players_message(len(player_list),  "- " + (', ').join(player_list))
#         new_data.guardian_message(guardians.replace(' and', ','))
#         new_data.height_message( "- " + (', ').join(height_list), average_height)
#         new_data.experience_message(len(experienced_players), "- " + (', ').join(experienced_players),
#                             len(inexperienced),  "- " + (', ').join(experienced_players))
#         keep_viewing = new_data.keep_viewing()
#         return keep_viewing
#     # Checks if the user wants to continue viewing stats
#     if keep_viewing.upper() in ['Y', 'YES']:
#         stats = new_data.view_stats()
#         # Print Team Guardians
#         if stats == 1:
#             new_data.guardian_message(guardians.replace(' and', ','))
#             keep_viewing = new_data.keep_viewing()
#             if keep_viewing.upper() in ['N', 'NO']:
#                 return keep_viewing
#         # Print Team Heights
#         elif stats == 2:
#             new_data.height_message("- " + (', ').join(height_list), average_height)
#             keep_viewing = new_data.keep_viewing()
#             if keep_viewing.upper() in ['N', 'NO']:
#                 return keep_viewing
#         # Print Players Via Experience
#         elif stats == 3:
#             new_data.experience_message(len(experienced_players), "- " + (', ').join(experienced_players),
#                                         len(inexperienced), "- " + (', ').join(experienced_players))
#             keep_viewing = new_data.keep_viewing()
#             if keep_viewing.upper() in ['N', 'NO']:
#                 return keep_viewing
#         # Print all stats
#         elif stats == 4:
#             keep_viewing = view_all_stats_message(team)
#
#     if keep_viewing.upper() in ['N', 'NO']:
#         new_data.goodbye_message()
#         sys.exit()
#     return keep_viewing
#
#
# def start_program():
#     while True:
#         new_data.main_menu()
#         team = new_data.get_user_team()
#         if team == 1:
#             view_more_stats = team_stats('Panthers')
#             if view_more_stats.upper() in ['N', 'NO']:
#                 new_data.goodbye_message()
#                 break
#         elif team == 2:
#             view_more_stats = team_stats('Bandits')
#             if view_more_stats.upper() in ['N', 'NO']:
#                 new_data.goodbye_message()
#                 break
#         elif team == 3:
#             view_more_stats = team_stats('Warriors')
#             if view_more_stats.upper() in ['N', 'NO']:
#                 new_data.goodbye_message()
#                 break
#
#
# # if __name__ == '__main__':
# #     start_program()
