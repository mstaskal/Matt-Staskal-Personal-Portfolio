"""
Name: Matt Staskal
The purpose of this program is to create a file that is formatted so that the PlayerCard can use it
to display a chosen players 2023 season statistics. File downloaded from FantasyData.com, position: Runningback.
*This file has already been created and is in use by the project program, so this program does not need to run before running the project code*
"""

import json
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/SEASON_TOTAL_RB.json') as rb:
    rb_list = json.load(rb)


formatted = json.dumps(rb_list, indent=2)

print(formatted)

rb_season_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/RB_SEASON_FINAL.json', 'w')
rb_season_final.writelines(formatted)
rb_season_final.close()