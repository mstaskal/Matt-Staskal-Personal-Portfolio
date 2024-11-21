"""
Name: Matt Staskal

The purpose of this program is to create a file that is formatted so that the PlayerCard can use it
to display a chosen players 2023 season statistics. File downloaded from FantasyData.com, position: Kicker.
*This file has already been created and is in use by the project program, so this program does not need to run before running the project code*
"""


import json
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/SEASON_TOTAL_K.json') as k:
    k_list = json.load(k)


formatted = json.dumps(k_list, indent=2)

print(formatted)

k_season_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/K_SEASON_FINAL.json', 'w')
k_season_final.writelines(formatted)
k_season_final.close()