"""
Name: Matt Staskal


The purpose of this program is to create a single file with player season total statistics for reference by
the PlayerCard class, to display on the GUI. It is done by combining all of the individual position files
that have been downloaded from FantasyData.com and formatted for intake.
*This file has already been created and is in use by the project program, so this program does not need to run before running the final project code*
"""


import json

season_totals_all_players = []

with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_QB.json') as qb:
    qb_list = json.load(qb)
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_RB.json') as rb:
    rb_list = json.load(rb)
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_WR.json') as wr:
    wr_list = json.load(wr)
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_TE.json') as te:
    te_list = json.load(te)
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_K.json') as k:
    k_list = json.load(k)
with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/SEASON_TOTAL_DST.json') as dst:
    dst_list = json.load(dst)

for i in qb_list:
    season_totals_all_players.append(i)
for i in rb_list:
    season_totals_all_players.append(i)
for i in wr_list:
    season_totals_all_players.append(i)
for i in te_list:
    season_totals_all_players.append(i)
for i in k_list:
    season_totals_all_players.append(i)
for i in dst_list:
    season_totals_all_players.append(i)

formatted = json.dumps(season_totals_all_players, indent=2)

season_totals_all_players = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/final_versions/SEASON_TOTALS_ALL_PLAYERS.json', 'w')
season_totals_all_players.writelines(formatted)
season_totals_all_players.close()