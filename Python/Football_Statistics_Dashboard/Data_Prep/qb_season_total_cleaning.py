"""
Name: Matt Staskal
The purpose of this program is to create a file that is formatted so that the PlayerCard can use it
to display a chosen players 2023 season statistics. File downloaded from FantasyData.com, position: Quarterback.
*This file has already been created and is in use by the project program, so this program does not need to run before running the project code*
"""

import json
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/SEASON_TOTAL_QB.json') as qb:
    qb_list = json.load(qb)


formatted = json.dumps(qb_list, indent=2)

print(formatted)

qb_season_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/QB_SEASON_FINAL.json', 'w')
qb_season_final.writelines(formatted)
qb_season_final.close()