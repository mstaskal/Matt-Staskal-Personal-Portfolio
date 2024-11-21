"""
Name: Matt Staskal
The purpose of this program is to create a file that is formatted so that the PlayerCard can use it
to display a chosen players 2023 season statistics. File downloaded from FantasyData.com, position: Wide Receiver.
*This file has already been created and is in use by the project program, so this program does not need to run before running the project code*
"""

import json
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/SEASON_TOTAL_WR.json') as wr:
    wr_list = json.load(wr)


formatted = json.dumps(wr_list, indent=2)

print(formatted)

wr_season_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/WR_SEASON_FINAL.json', 'w')
wr_season_final.writelines(formatted)
wr_season_final.close()