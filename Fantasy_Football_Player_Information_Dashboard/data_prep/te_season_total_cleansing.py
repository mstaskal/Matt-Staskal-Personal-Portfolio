"""
Name: Matt Staskal
Class: CIS 189
Module: Final project
Topic: Fantasy football player dashboard - Create Tight End season totals file
The purpose of this program is to create a file that is formatted so that the PlayerCard can use it
to display a chosen players 2023 season statistics. File downloaded from FantasyData.com, position: Tight End.
*This file has already been created and is in use by the project program, so this program does not need to run before running the final project code*
"""

import json
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/SEASON_TOTAL_TE.json') as te:
    te_list = json.load(te)


formatted = json.dumps(te_list, indent=2)

print(formatted)

te_season_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/TE_SEASON_FINAL.json', 'w')
te_season_final.writelines(formatted)
te_season_final.close()