"""
Name: Matt Staskal
Class: CIS 189
Module: Final project
Topic: Fantasy football player dashboard - Create Player heading information file
The purpose of this program is to create a file with basic player information to be displayed as the heading of the card when a player is located.
This information will be displayed just above the season total information. File downloaded from FantasyData.com.
*This file has already been created and is in use by the project program, so this program does not need to run before running the final project code*
"""


import json

with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/data_prep/PLAYER_CARDS.json') as pc:
    player_cards = json.load(pc)

for i in player_cards:
    del i["Played"]
    del i["PassingYards"]
    del i["PassingTouchdowns"]
    del i["PassingInterceptions"]
    del i["RushingYards"]
    del i["RushingTouchdowns"]
    del i["Receptions"]
    del i["ReceivingYards"]
    del i["ReceivingTouchdowns"]
    del i["Sacks"]
    del i["Interceptions"]
    del i["FumblesRecovered"]
    del i["FumblesForced"]
    del i["FantasyPoints"]
    del i["FantasyPointsPerGame"]

for i in player_cards[:]:
    if i["Position"] not in ["QB","RB","WR","TE","K","DST"]:
        player_cards.remove(i)

for i in player_cards[:]:
    searchable_name = i["Name"].lower()
    searchable_name1 = searchable_name.replace("-","")
    searchable_name2 = searchable_name1.replace(".","")
    searchable_name3 = searchable_name2.replace(" ","")
    i["Search Name"] = searchable_name3

formatted = json.dumps(player_cards, indent=2)

player_cards_final = open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/player_cards/PLAYER_CARDS_FINAL.json', 'w')
player_cards_final.writelines(formatted)
player_cards_final.close()

