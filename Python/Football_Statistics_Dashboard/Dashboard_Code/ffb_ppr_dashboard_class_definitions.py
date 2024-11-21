"""
Name: Matt Staskal

The purpose of this program is to define classes to use to create the dashboard. The PlayerCard class contains the
tkinter object, searches for a player, and uses the Player class to create a player object to display the player's
information.
"""


import datetime
import json
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt
from final_project.player_reports import ppr_scoring_consist_class_def as consist, ppr_scoring_dist_class_def as dist, ppr_scoring_week_to_week_class_def as w2w
from final_project.team_logos.team_logos_dict import logo_dict as logos


class Player:
    #Player class used to create the base Player object, that is referenced by self.player_name to create GUI objects
    def __init__(self, player_id, name, position, team, rank,search_name):
        self.player_id = player_id
        self.player_name = name
        self.position = position
        self.team = team
        self.rank = rank
        self.search_name = search_name

        self.logos = logos

    def __str__(self):
        return f'Name: {self.player_name}  Pos: {self.position}  Team: {self.team}  2023 PPR Overall Rank: {self.rank}'

    def __repr__(self):
        return f'Name: {self.player_name}  Pos: {self.position}  Team: {self.team}  2023 PPR Overall Rank: {self.rank}'

    def display(self):
        return f'Name: {self.player_name}\nPos: {self.position}\nTeam: {self.team}\n2023 PPR Overall Rank: {self.rank}'

    def set_player_name(self, player_name):
        # Sets the player name, self.player_name used as base reference in program
        self.player_name = player_name

class InvalidNameException(Exception):
    def __init__(self, message="Error: Name must only contain alphabetical characters"):
        super(InvalidNameException, self).__init__(message)

class PlayerCard:

    def __init__(self, master, player_name="",this_player=""):
        #PlayerCard class is the outline for the Tkinter window
        self.master = master
        self.player_name = player_name
        self.this_player = this_player
        self.current_date = datetime.datetime.now()
        self.master.title(f'2023 Fantasy Football Player Profiles            Today\'s date: {self.current_date.month}-{self.current_date.day}-{self.current_date.year}')
        self.master.config(bg='gray20')
        with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/player_cards/PLAYER_CARDS_FINAL.json') as pc2023:
            self.player_list = json.load(pc2023)
        with open('C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/season_totals/SEASON_TOTALS_ALL_PLAYERS.json') as st2023:
            self.season_totals_list = json.load(st2023)

        self.search_prompt = tk.Label(self.master,
                                      text="To search a player, enter the player's first and last name, without spaces or special characters (Ex.\"amonrastbrown\")\nTo search a team, enter team's city followed by the team name, without spaces (Ex. \"sanfrancisco49ers\")\n",
                                      fg='gray80', font='system', height=4, width=100, justify='left',bg='gray20')
        self.search_prompt.grid(row=10,column=0,stick=W)

        self.search_button = tk.Button(self.master, text="Search",command=lambda : self.player_search(self.player_list, self.season_totals_list),bg='gray60',fg='gray90',relief='groove')
        self.search_button.grid(row=0, column=0,sticky=W)

        self.search_entry = tk.Entry(self.master,bg='gray60',fg='gray90',relief='groove')
        self.search_entry.grid(row=1, column=0, sticky=W)

        self.error_label = tk.Label(self.master,bg='gray20',fg='gray80',font='system')
        self.error_label.grid(row=2,column=0)

        self.result_label = tk.Label(self.master, text="",bg='gray20',fg='gray80',font='system',justify='left')
        self.result_label.grid(row=2, column=0,sticky=W)

        self.logo_display = tk.Label(self.master,bg='gray20')
        self.logo_display.grid(row=9, column=0,sticky=W)

        self.season_totals = tk.Label(self.master, text="",bg='gray20',fg='gray80',font='system',justify='left')
        self.season_totals.grid(row=3, column=0,sticky=W)

        self.dist_report_button = tk.Button(self.master, text="PPR Scoring Distribution Report",command=lambda: self.dist_chart(self.this_player.player_name, self.player_list),bg='gray60',fg='gray90',relief='groove',state='disabled',activebackground='gray60',activeforeground='gray90')
        self.dist_report_button.grid(row=4,column=0,sticky=W)

        self.consist_report_button = tk.Button(self.master, text="PPR Scoring Consistency Report",command=lambda: self.consist_chart(self.this_player.player_name, self.player_list),bg='gray60',fg='gray90',relief='groove',justify='left',state='disabled',activebackground='gray60',activeforeground='gray90')
        self.consist_report_button.grid(row=5,column=0,sticky=W)

        self.week2week_report_button = tk.Button(self.master, text="PPR Scoring Week by Week 2023",command=lambda: self.w2w_chart(self.this_player.player_name, self.player_list),bg='gray60',fg='gray90',relief='groove',justify='left',state='disabled',activebackground='gray60',activeforeground='gray90')
        self.week2week_report_button.grid(row=6,column=0,sticky=W)

        self.ff_ppr_explanation = tk.Button(self.master, text="Click for Details on Scoring/Data Sources",command=self.card_info,bg='gray60',fg='gray90',relief='groove',justify='left')
        self.ff_ppr_explanation.grid(row=7,column=0,sticky=W)
    def search_validation(self):
        # Input validation for player search. User can search using capital letters, but must remove any special characters or spaces
        # param self: PlayerCard object
        # :returns: a formatted version of the player name that can be used to search player card file for the name that is entered
        # :raises: InvalidNameException if special characters or spaces are entered
        name_characters = set("abcdefghijklmnopqrstuvwxyz0123456789")
        name_entered = self.search_entry.get()
        name_entry = name_entered.lower()

        found = False
        if not (name_characters.issuperset(name_entry)):
            self.error_label.config(text="Error: Name must only contain alphabetical characters. Please search again")
            self.result_label.config(text="")
            self.season_totals.config(text="")
            self.logo_display.config(image="")
            found = True
            raise InvalidNameException
        else:
            return name_entry
    def player_search(self, player_list, season_totals):
        # Player search function. Calls search_validation() to validate the entry, and then searches player cards for the formatted player name
        # param player_list: 2023 player card file, that is opened when instantiating the PlayerCard class, and passed in via the self.search_button widget
        # param season_totals: 2023 season totals list, that is opened when instantiating the PlayerCard class, and passed in via the self.search_button widget
        # :returns: creates a Player class instance of the searched player, displays player info via Player.display() function, season totals via PlayerCard.season_total_display(), team logo, and activates report buttons
        # :raises: error message prompting user to re-search if player not found. This is after the format has already been validated.
        try:
            self.search_validation()
        except:
            raise InvalidNameException
        else:
            found = False
            for i in player_list:
                if self.search_validation() == i["Search Name"]:
                    found = True
                    self.error_label.config(text="")
                    self.set_player_name(self.search_validation())
                    self.player_name = self.this_player
                    self.this_player = Player(i["PlayerID"], i["Name"], i["Position"], i["Team"], i["Rank"],i["Search Name"])
                    self.result_label.config(text=self.this_player.display(), font='system',fg='gray80',relief='groove')
                    self.player_team = i["Team"]
                    self.player_team_logo = self.this_player.logos[self.this_player.team]
                    self.team_img = ImageTk.PhotoImage(Image.open(self.player_team_logo))
                    self.logo_display.config(image=self.team_img)
                    self.season_total_display(season_totals, self.this_player.player_name)
                    self.dist_report_button.config(state='active')
                    self.consist_report_button.config(state='active')
                    self.week2week_report_button.config(state='active')
                    break
            if found == False:
                self.error_label.config(text="Player not found. Please re-enter player name using format specified below")
                self.result_label.config(text="")
                self.season_totals.config(text="")
                self.logo_display.config(image="")

    def set_player_name(self, player_name):
        # Sets the player name, self.player_name used as base reference in program
        self.player_name = player_name

    def card_info(self):
        # Messagebox widget activated on click, with information on data and scoring. Always active.
        messagebox.showinfo(title='Note',message=f'Fantasy Football points system based on \"PPR\" scoring system (1 Point Per Reception)\n'
                                                f'Data for 2023 Season, gathered from https://fantasydata.com/\n'
                                                f'Positions supported: Quarterback (QB), Runningback (RB), Wide Receiver (WR), Tight End (TE), Kicker (K), Defense/Special Teams(DST)\n'
                                                f'See https://fantasydata.com/api/fantasy-scoring-system/nfl for full explanation of scoring system')


    def season_total_display(self, season_totals_list, player_name):
        # Uses season_totals_list file to find the player and display the 2023 season total stats for that player according to their position
        # param season_totals_list: 2023 season totals list, that is opened when instantiating the PlayerCard class, and passed when a Player object is created
        # param player_name: self.player_name attribute passed in when a Player object is created
        # :returns: configures the season_totals Label widget to display the result variable string with 2023 season totals
        # :raises: n/a
        for i in season_totals_list:
            if player_name == i["Name"]:
                match i["Position"]:
                    case "QB":
                        result = f'2023 Totals:\n--------------------\nPass Att: {i["PassingCompletions"]}\nPass Comp: {i["PassingCompletions"]}\nPass Yds: {i["PassingYards"]}\nPass TD: {i["PassingTouchdowns"]}\nRush Att: {i["RushingAttempts"]}\nRush yds: {i["RushingYards"]}\nRush TD:{i["RushingTouchdowns"]}\nPPR Pts/Gm: {i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                    case "RB":
                        result = f'2023 Totals:\n--------------------\nRush Att: {i["RushingAttempts"]}\nRush yds: {i["RushingYards"]}\nRush TD: {i["RushingTouchdowns"]}\nRec Targets: {i["ReceivingTargets"]}\nRec: {i["Receptions"]}\nRec Yds: {i["ReceivingYards"]}\nRec TD:{i["ReceivingTouchdowns"]}\n2023 PPR Pts/Gm: {i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                    case "WR":
                        result = f'2023 Totals:\n--------------------\nRec Targets: {i["ReceivingTargets"]}\nRec: {i["Receptions"]}\nRec Yds: {i["ReceivingYards"]}\nRec TD: {i["ReceivingTouchdowns"]}\nRush Att: {i["RushingAttempts"]}\nRush yds: {i["RushingYards"]}\nRush TD:{i["RushingTouchdowns"]}\n2023 PPR Pts/Gm: {i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                    case "TE":
                        result = f'2023 Totals:\n--------------------\nRec Targets: {i["ReceivingTargets"]}\nRec: {i["Receptions"]}\nRec Yds: {i["ReceivingYards"]}\nRec TD: {i["ReceivingTouchdowns"]}\nRush Att: {i["RushingAttempts"]}\nRush yds: {i["RushingYards"]}\nRush TD:{i["RushingTouchdowns"]}\n2023 PPR Pts/Gm: {i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                    case "K":
                        result = f'2023 Totals:\n--------------------\nFG Att: {i["FieldGoalsAttempted"]}\nFG Made: {i["FieldGoalsMade"]}\nFG%: {i["FieldGoalPercentage"]}\nXP Att: {i["ExtraPointsAttempted"]}\nXP Made: {i["ExtraPointsMade"]}\nLongest FG: {i["FieldGoalsLongestMade"]}\nTotal Pts Scored: {i["FantasyPoints"]}\n2023 PPR Pts/Gm:{i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                    case "DST":
                        result = f'2023 Totals:\n--------------------\nPts Allowed: {i["PointsAllowedByDefenseSpecialTeams"]}\nInterceptions: {i["Interceptions"]}\nSacks: {i["Sacks"]}\nFum Recoveries: {i["FumblesRecovered"]}\nSafeties: {i["Safeties"]}\nTDs: {i["DefensiveTouchdowns"]}\nTotal Pts Scored: {i["FantasyPoints"]}\n2023 PPR Pts/Gm:{i["FantasyPointsPerGame"]}\n2023 Position Rank: {i["Rank"]}'
                self.season_totals.config(text=result, font='system',fg='gray80',pady=20)

    def dist_chart(self, player_name, player_list):
        # Creates matplotlip.pyplot bar and plot chart displaying players scoring distribution vs. league average. Displayed when self.dist_report_button is clicked
        # param player_name: self.player_name attribute passed in when a Player object is created
        # param player_list: 2023 player card file, that is opened when instantiating the PlayerCard class, and passed when a Player object is created
        # :returns: matplotlib.pyplot chart
        # :raises: n/a
        for i in player_list:
            if player_name == i["Name"]:
                match i["Position"]:
                    case "QB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_qb.csv') as qb_csv:
                            csv_reader = csv.reader(qb_csv, delimiter=',')
                            line_count = 0
                            qb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                qb_group[str(row[2])] = dist.QBDist(row[0], row[1], row[2], row[3], row[4],
                                                                    float(row[5]), float(row[6]), float(row[7]),
                                                                    float(row[8]), float(row[9]), float(row[10]),
                                                                    float(row[11]), float(row[12]), float(row[13]),
                                                                    float(row[14]), float(row[15]), float(row[16]),
                                                                    float(row[17]), float(row[18]), float(row[19]),
                                                                    float(row[20]), float(row[21]), float(row[22]),
                                                                    float(row[23]), float(row[24]), float(row[25]),
                                                                    float(row[26]), float(row[27]), float(row[28]),
                                                                    float(row[29]))

                        categories = ["% from Pass Yds", "% from Pass TDs", "% from INTs", "% from Rush Yds",
                                      "% from Rush TDs"]
                        plot_values = []
                        plot_values.append(qb_group[player_name].pfpy_pct_total)
                        plot_values.append(qb_group[player_name].pfptd_pct_total)
                        plot_values.append(qb_group[player_name].pfint_pct_total)
                        plot_values.append(qb_group[player_name].pfry_pct_total)
                        plot_values.append(qb_group[player_name].pfrtd_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(qb_group["League Average (150+ Pass Att)"].pfpy_pct_total)
                        league_average.append(qb_group["League Average (150+ Pass Att)"].pfptd_pct_total)
                        league_average.append(qb_group["League Average (150+ Pass Att)"].pfint_pct_total)
                        league_average.append(qb_group["League Average (150+ Pass Att)"].pfry_pct_total)
                        league_average.append(qb_group["League Average (150+ Pass Att)"].pfrtd_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average (150+ Pass Att)")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y',linestyle='--',color='gray')
                        plt.show()

                    case "RB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_rb.csv') as rb_csv:
                            csv_reader = csv.reader(rb_csv, delimiter=',')
                            line_count = 0
                            rb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                rb_group[str(row[2])] = dist.RBDist(row[0], row[1], row[2], row[3], row[4],
                                                                    float(row[5]), float(row[6]), float(row[7]),
                                                                    float(row[8]), float(row[9]), float(row[10]),
                                                                    float(row[11]), float(row[12]), float(row[13]),
                                                                    float(row[14]), float(row[15]), float(row[16]),
                                                                    float(row[17]), float(row[18]), float(row[19]),
                                                                    float(row[20]), float(row[21]), float(row[22]),
                                                                    float(row[23]), float(row[24]), float(row[25]),
                                                                    float(row[26]), float(row[27]), float(row[28]),
                                                                    float(row[29]))

                        categories = ["% from Rush Yds", "% from Rush TDs", "% from Receptions", "% from Receiving Yds",
                                      "% from Receiving TDs", "% from Fumbles"]
                        plot_values = []
                        plot_values.append(rb_group[player_name].pfry_pct_total)
                        plot_values.append(rb_group[player_name].pfrtd_pct_total)
                        plot_values.append(rb_group[player_name].pfrec_pct_total)
                        plot_values.append(rb_group[player_name].pfrecy_pct_total)
                        plot_values.append(rb_group[player_name].pfrectd_pct_total)
                        plot_values.append(rb_group[player_name].pffum_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(rb_group["League Average (60+ Carries)"].pfry_pct_total)
                        league_average.append(rb_group["League Average (60+ Carries)"].pfrtd_pct_total)
                        league_average.append(rb_group["League Average (60+ Carries)"].pfrec_pct_total)
                        league_average.append(rb_group["League Average (60+ Carries)"].pfrecy_pct_total)
                        league_average.append(rb_group["League Average (60+ Carries)"].pfrectd_pct_total)
                        league_average.append(rb_group["League Average (60+ Carries)"].pffum_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average (60+ Carries)")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "WR":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_wr.csv') as wr_csv:
                            csv_reader = csv.reader(wr_csv, delimiter=',')
                            line_count = 0
                            wr_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                wr_group[str(row[2])] = dist.WRDist(row[0], row[1], row[2], row[3], row[4],
                                                                    float(row[5]), float(row[6]), float(row[7]),
                                                                    float(row[8]), float(row[9]), float(row[10]),
                                                                    float(row[11]), float(row[12]), float(row[13]),
                                                                    float(row[14]), float(row[15]), float(row[16]),
                                                                    float(row[17]), float(row[18]), float(row[19]),
                                                                    float(row[20]), float(row[21]), float(row[22]),
                                                                    float(row[23]), float(row[24]), float(row[25]),
                                                                    float(row[26]), float(row[27]), float(row[28]),
                                                                    float(row[29]), float(row[30]), float(row[31]),
                                                                    float(row[32]), float(row[33]))

                        categories = ["% from Receptions", "% from Receiving Yds", "% from Receiving TDs",
                                      "% from Rush Yds", "% from Rush TDs", "% from Fumbles"]
                        plot_values = []
                        plot_values.append(wr_group[player_name].pfrec_pct_total)
                        plot_values.append(wr_group[player_name].pfrecy_pct_total)
                        plot_values.append(wr_group[player_name].pfrectd_pct_total)
                        plot_values.append(wr_group[player_name].pfry_pct_total)
                        plot_values.append(wr_group[player_name].pfrtd_pct_total)
                        plot_values.append(wr_group[player_name].pffum_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(wr_group["League Average (30+ Catches)"].pfrec_pct_total)
                        league_average.append(wr_group["League Average (30+ Catches)"].pfrecy_pct_total)
                        league_average.append(wr_group["League Average (30+ Catches)"].pfrectd_pct_total)
                        league_average.append(wr_group["League Average (30+ Catches)"].pfry_pct_total)
                        league_average.append(wr_group["League Average (30+ Catches)"].pfrtd_pct_total)
                        league_average.append(wr_group["League Average (30+ Catches)"].pffum_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average (30+ Catches)")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "TE":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_te.csv') as te_csv:
                            csv_reader = csv.reader(te_csv, delimiter=',')
                            line_count = 0
                            te_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                te_group[str(row[2])] = dist.TEDist(row[0], row[1], row[2], row[3], row[4],
                                                                    float(row[5]), float(row[6]), float(row[7]),
                                                                    float(row[8]), float(row[9]), float(row[10]),
                                                                    float(row[11]), float(row[12]), float(row[13]),
                                                                    float(row[14]), float(row[15]), float(row[16]),
                                                                    float(row[17]), float(row[18]), float(row[19]),
                                                                    float(row[20]), float(row[21]), float(row[22]),
                                                                    float(row[23]), float(row[24]), float(row[25]),
                                                                    float(row[26]), float(row[27]), float(row[28]),
                                                                    float(row[29]), float(row[30]), float(row[31]),
                                                                    float(row[32]), float(row[33]))

                        categories = ["% from Receptions", "% from Receiving Yds", "% from Receiving TDs",
                                      "% from Rush Yds", "% from Rush TDs", "% from Fumbles"]
                        plot_values = []
                        plot_values.append(te_group[player_name].pfrec_pct_total)
                        plot_values.append(te_group[player_name].pfrecy_pct_total)
                        plot_values.append(te_group[player_name].pfrectd_pct_total)
                        plot_values.append(te_group[player_name].pfry_pct_total)
                        plot_values.append(te_group[player_name].pfrtd_pct_total)
                        plot_values.append(te_group[player_name].pffum_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(te_group["League Average (20+ Catches)"].pfrec_pct_total)
                        league_average.append(te_group["League Average (20+ Catches)"].pfrecy_pct_total)
                        league_average.append(te_group["League Average (20+ Catches)"].pfrectd_pct_total)
                        league_average.append(te_group["League Average (20+ Catches)"].pfry_pct_total)
                        league_average.append(te_group["League Average (20+ Catches)"].pfrtd_pct_total)
                        league_average.append(te_group["League Average (20+ Catches)"].pffum_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average (20+ Catches)")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "K":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_k.csv') as k_csv:
                            csv_reader = csv.reader(k_csv, delimiter=',')
                            line_count = 0
                            k_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                k_group[str(row[2])] = dist.KDist(row[0], row[1], row[2], row[3], row[4],
                                                                  float(row[5]), float(row[6]), float(row[7]),
                                                                  float(row[8]), float(row[9]), float(row[10]),
                                                                  float(row[11]), float(row[12]), float(row[13]),
                                                                  float(row[14]), float(row[15]), float(row[16]),
                                                                  float(row[17]), float(row[18]), float(row[19]),
                                                                  float(row[20]))

                        categories = ["% from 0-39 Yds", "% from 40-49 Yds", "% from 50+ Yds", "% from Extra Pts", ]
                        plot_values = []
                        plot_values.append(k_group[player_name].close_pct_total)
                        plot_values.append(k_group[player_name].mid_pct_total)
                        plot_values.append(k_group[player_name].long_pct_total)
                        plot_values.append(k_group[player_name].xp_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(k_group["League Average (8+ Games Played)"].close_pct_total)
                        league_average.append(k_group["League Average (8+ Games Played)"].mid_pct_total)
                        league_average.append(k_group["League Average (8+ Games Played)"].long_pct_total)
                        league_average.append(k_group["League Average (8+ Games Played)"].xp_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average (8+ Games Played)")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "DST":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/scoring_distribution_report/ppr_scoring_dist_dst.csv') as dst_csv:
                            csv_reader = csv.reader(dst_csv, delimiter=',')
                            line_count = 0
                            dst_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                dst_group[str(row[2])] = dist.DSTDist(row[0], row[1], row[2], row[3], row[4],
                                                                      float(row[5]),
                                                                      float(row[6]), float(row[7]), float(row[8]),
                                                                      float(row[9]),
                                                                      float(row[10]), float(row[11]), float(row[12]),
                                                                      float(row[13]), float(row[14]), float(row[15]),
                                                                      float(row[16]), float(row[17]), float(row[18]),
                                                                      float(row[19]), float(row[20]), float(row[21]),
                                                                      float(row[22]), float(row[23]), float(row[24]),
                                                                      float(row[25]), float(row[26]), float(row[27]),
                                                                      float(row[28]))

                        categories = ["% from Sacks", "% from Interceptions", "% from Fumble Rec", "% from Safeties",
                                      "% from Def TDs", "% from Spec Teams TDs", "% from Points Allowed"]
                        plot_values = []
                        plot_values.append(dst_group[player_name].pfsac_pct_total)
                        plot_values.append(dst_group[player_name].pfint_pct_total)
                        plot_values.append(dst_group[player_name].pff_pct_total)
                        plot_values.append(dst_group[player_name].pfsaf_pct_total)
                        plot_values.append(dst_group[player_name].pfdtd_pct_total)
                        plot_values.append(dst_group[player_name].pfsptd_pct_total)
                        plot_values.append(dst_group[player_name].pfpa_pct_total)
                        plt.bar(categories, plot_values, color='blue', width=.2,label=player_name)

                        league_average = []
                        league_average.append(dst_group["League Average"].pfsac_pct_total)
                        league_average.append(dst_group["League Average"].pfint_pct_total)
                        league_average.append(dst_group["League Average"].pff_pct_total)
                        league_average.append(dst_group["League Average"].pfsaf_pct_total)
                        league_average.append(dst_group["League Average"].pfdtd_pct_total)
                        league_average.append(dst_group["League Average"].pfsptd_pct_total)
                        league_average.append(dst_group["League Average"].pfpa_pct_total)
                        plt.plot(categories, league_average, color='red',label="League Average")
                        plt.ylabel("Percent of total Points")
                        plt.title("Percent of total Points gained from each scoring category")
                        plt.legend(loc=1, fontsize="x-small")
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

    def consist_chart(self, player_name, player_list):
        # Creates matplotlip.pyplot scatter chart displaying players scoring consistency vs. league average and others at the position. Displayed when self.consist_report_button is clicked
        # param player_name: self.player_name attribute passed in when a Player object is created
        # param player_list: 2023 player card file, that is opened when instantiating the PlayerCard class, and passed when a Player object is created
        # :returns: matplotlib.pyplot chart
        # :raises: n/a
        for i in player_list:
            if player_name == i["Name"]:
                match i["Position"]:
                    case "QB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_qb.csv') as qb_csv:
                            csv_reader = csv.reader(qb_csv, delimiter=',')
                            line_count = 0
                            qb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                qb_group[str(row[1])] = consist.QBConsist(row[0], row[1], row[2], row[3], float(row[4]),
                                                                          float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(qb_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(qb_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in qb_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games)":
                                continue
                            if qb_group[key].played < 8:
                                continue
                            if qb_group[key].fantasy_points_pergameppr < 5:
                                continue
                            points_per_game_all.append(qb_group[key].fantasy_points_pergameppr)
                        for key, value in qb_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games)":
                                continue
                            if qb_group[key].played < 8:
                                continue
                            if qb_group[key].fantasy_points_pergameppr < 5:
                                continue
                            consistency_all.append(qb_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15, label="All Other QBs (8+ games, 5+PPG)",
                                    color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(qb_group["League Average (8+ Games)"].fantasy_points_pergameppr)
                        consistency_la.append(qb_group["League Average (8+ Games)"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average (8+ Games)",
                                    color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",title='Lower st dev = more consistent week-to-week scoring',title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "RB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_rb.csv') as rb_csv:
                            csv_reader = csv.reader(rb_csv, delimiter=',')
                            line_count = 0
                            rb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                rb_group[str(row[1])] = consist.RBConsist(row[0], row[1], row[2], row[3], float(row[4]),
                                                                          float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(rb_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(rb_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in rb_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 4+ PPG)":
                                continue
                            if rb_group[key].played < 8:
                                continue
                            if rb_group[key].fantasy_points_pergameppr < 4:
                                continue
                            points_per_game_all.append(rb_group[key].fantasy_points_pergameppr)
                        for key, value in rb_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 4+ PPG)":
                                continue
                            if rb_group[key].played < 8:
                                continue
                            if rb_group[key].fantasy_points_pergameppr < 4:
                                continue
                            consistency_all.append(rb_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15,
                                    label="All Other RBs (8+ games, 4+ PPG)", color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(
                            rb_group["League Average (8+ Games, 4+ PPG)"].fantasy_points_pergameppr)
                        consistency_la.append(
                            rb_group["League Average (8+ Games, 4+ PPG)"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average (8+ Games, 4+ PPG)",
                                    color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",
                                   title='Lower st dev = more consistent week-to-week scoring',
                                   title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "WR":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_wr.csv') as wr_csv:
                            csv_reader = csv.reader(wr_csv, delimiter=',')
                            line_count = 0
                            wr_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                wr_group[str(row[1])] = consist.WRConsist(row[0], row[1], row[2], row[3], float(row[4]),
                                                                          float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(wr_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(wr_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in wr_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 5+ PPG)":
                                continue
                            if wr_group[key].played < 8:
                                continue
                            if wr_group[key].fantasy_points_pergameppr < 5:
                                continue
                            points_per_game_all.append(wr_group[key].fantasy_points_pergameppr)
                        for key, value in wr_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 5+ PPG)":
                                continue
                            if wr_group[key].played < 8:
                                continue
                            if wr_group[key].fantasy_points_pergameppr < 5:
                                continue
                            consistency_all.append(wr_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15, label="All Other WRs (8+ games, 5+PPG)",
                                    color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(
                            wr_group["League Average (8+ Games, 5+ PPG)"].fantasy_points_pergameppr)
                        consistency_la.append(
                            wr_group["League Average (8+ Games, 5+ PPG)"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average (8+ Games, 5+ PPG)",
                                    color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",
                                   title='Lower st dev = more consistent week-to-week scoring',
                                   title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "TE":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_te.csv') as te_csv:
                            csv_reader = csv.reader(te_csv, delimiter=',')
                            line_count = 0
                            te_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                te_group[str(row[1])] = consist.TEConsist(row[0], row[1], row[2], row[3], float(row[4]),
                                                                          float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(te_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(te_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in te_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 3+ PPG)":
                                continue
                            if te_group[key].played < 8:
                                continue
                            if te_group[key].fantasy_points_pergameppr < 3:
                                continue
                            points_per_game_all.append(te_group[key].fantasy_points_pergameppr)
                        for key, value in te_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games, 3+ PPG)":
                                continue
                            if te_group[key].played < 8:
                                continue
                            if te_group[key].fantasy_points_pergameppr < 3:
                                continue
                            consistency_all.append(te_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15,
                                    label="All Other TEs (8+ games, 3+ PPG)",
                                    color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(
                            te_group["League Average (8+ Games, 3+ PPG)"].fantasy_points_pergameppr)
                        consistency_la.append(
                            te_group["League Average (8+ Games, 3+ PPG)"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average (8+ Games, 3+ PPG)",
                                    color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",
                                   title='Lower st dev = more consistent week-to-week scoring',
                                   title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "K":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_k.csv') as k_csv:
                            csv_reader = csv.reader(k_csv, delimiter=',')
                            line_count = 0
                            k_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                k_group[str(row[1])] = consist.KConsist(row[0], row[1], row[2], row[3], float(row[4]),
                                                                        float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(k_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(k_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in k_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games)":
                                continue
                            if k_group[key].played < 8:
                                continue
                            points_per_game_all.append(k_group[key].fantasy_points_pergameppr)
                        for key, value in k_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average (8+ Games)":
                                continue
                            if k_group[key].played < 8:
                                continue
                            consistency_all.append(k_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15, label="All Other Ks (8+ games)",
                                    color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(
                            k_group["League Average (8+ Games)"].fantasy_points_pergameppr)
                        consistency_la.append(
                            k_group["League Average (8+ Games)"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average (8+ Games)",
                                    color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",
                                   title='Lower st dev = more consistent week-to-week scoring',
                                   title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "DST":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/consistency_report/consist_dst.csv') as dst_csv:
                            csv_reader = csv.reader(dst_csv, delimiter=',')
                            line_count = 0
                            dst_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                dst_group[str(row[1])] = consist.DSTConsist(row[0], row[1], row[2], row[3],
                                                                            float(row[4]),
                                                                            float(row[5]), float(row[6]))

                        points_per_game_player = []
                        consistency_player = []
                        points_per_game_player.append(dst_group[player_name].fantasy_points_pergameppr)
                        consistency_player.append(dst_group[player_name].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_player, consistency_player, s=25, label=player_name, color="blue")

                        points_per_game_all = []
                        consistency_all = []
                        for key, value in dst_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average":
                                continue
                            points_per_game_all.append(dst_group[key].fantasy_points_pergameppr)
                        for key, value in dst_group.items():
                            if key == player_name:
                                continue
                            if key == "League Average":
                                continue
                            consistency_all.append(dst_group[key].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_all, consistency_all, s=15, label="All Other DSTs", color="red")

                        points_per_game_la = []
                        consistency_la = []
                        points_per_game_la.append(
                            dst_group["League Average"].fantasy_points_pergameppr)
                        consistency_la.append(
                            dst_group["League Average"].fantasy_points_pergameppr_stdev)
                        plt.scatter(points_per_game_la, consistency_la, label="League Average", color="limegreen")
                        plt.gca().invert_yaxis()
                        plt.title("Player Weekly Scoring Consistency")
                        plt.xlabel("Points per game")
                        plt.ylabel("St Dev of points per game")
                        plt.legend(loc=1, fontsize="x-small",
                                   title='Lower st dev = more consistent week-to-week scoring',
                                   title_fontsize='x-small')
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

    def w2w_chart(self, player_name, player_list):
        # Creates matplotlip.pyplot plot chart displaying players cumulative season total as the season progresses. Displayed when self.week2week_report_button is clicked
        # param player_name: self.player_name attribute passed in when a Player object is created
        # param player_list: 2023 player card file, that is opened when instantiating the PlayerCard class, and passed when a Player object is created
        # :returns: matplotlib.pyplot chart
        # :raises: n/a
        for i in player_list:
            if player_name == i["Name"]:
                match i["Position"]:
                    case "QB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_qb.csv') as w2wqb_csv:
                            csv_reader = csv.reader(w2wqb_csv, delimiter=',')
                            line_count = 0
                            w2wqb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wqb_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]), float(row[3]),
                                                                   float(row[4]),
                                                                   float(row[5]), float(row[6]), float(row[7]),
                                                                   float(row[8]), float(row[9]), float(row[10]),
                                                                   float(row[11]), float(row[12]), float(row[13]),
                                                                   float(row[14]), float(row[15]), float(row[16]),
                                                                   float(row[17]), float(row[18]))
                        weekly_scores = w2wqb_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks,weeks)
                        plt.ylim(0,450)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "WR":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_wr.csv') as w2wwr_csv:
                            csv_reader = csv.reader(w2wwr_csv, delimiter=',')
                            line_count = 0
                            w2wwr_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wwr_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]),
                                                                   float(row[3]), float(row[4]),
                                                                   float(row[5]), float(row[6]), float(row[7]),
                                                                   float(row[8]), float(row[9]), float(row[10]),
                                                                   float(row[11]), float(row[12]), float(row[13]),
                                                                   float(row[14]), float(row[15]), float(row[16]),
                                                                   float(row[17]), float(row[18]))
                        weekly_scores = w2wwr_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks, weeks)
                        plt.ylim(0, 400)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "RB":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_rb.csv') as w2wrb_csv:
                            csv_reader = csv.reader(w2wrb_csv, delimiter=',')
                            line_count = 0
                            w2wrb_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wrb_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]),
                                                                   float(row[3]), float(row[4]),
                                                                   float(row[5]), float(row[6]), float(row[7]),
                                                                   float(row[8]), float(row[9]), float(row[10]),
                                                                   float(row[11]), float(row[12]), float(row[13]),
                                                                   float(row[14]), float(row[15]), float(row[16]),
                                                                   float(row[17]), float(row[18]))
                        weekly_scores = w2wrb_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks, weeks)
                        plt.ylim(0, 450)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "TE":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_te.csv') as w2wte_csv:
                            csv_reader = csv.reader(w2wte_csv, delimiter=',')
                            line_count = 0
                            w2wte_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wte_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]),
                                                                   float(row[3]), float(row[4]),
                                                                   float(row[5]), float(row[6]), float(row[7]),
                                                                   float(row[8]), float(row[9]), float(row[10]),
                                                                   float(row[11]), float(row[12]), float(row[13]),
                                                                   float(row[14]), float(row[15]), float(row[16]),
                                                                   float(row[17]), float(row[18]))
                        weekly_scores = w2wte_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks, weeks)
                        plt.ylim(0, 250)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "K":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_k.csv') as w2wk_csv:
                            csv_reader = csv.reader(w2wk_csv, delimiter=',')
                            line_count = 0
                            w2wk_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wk_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]),
                                                                  float(row[3]), float(row[4]),
                                                                  float(row[5]), float(row[6]), float(row[7]),
                                                                  float(row[8]), float(row[9]), float(row[10]),
                                                                  float(row[11]), float(row[12]), float(row[13]),
                                                                  float(row[14]), float(row[15]), float(row[16]),
                                                                  float(row[17]), float(row[18]))
                        weekly_scores = w2wk_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks, weeks)
                        plt.ylim(0, 200)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()

                    case "DST":
                        with open(
                                'C:/Users/13199/Desktop/Matts/PycharmProjects/CIS189/final_project/game_by_game_report/game_by_game_dst.csv') as w2wdst_csv:
                            csv_reader = csv.reader(w2wdst_csv, delimiter=',')
                            line_count = 0
                            w2wdst_group = {}
                            for row in csv_reader:
                                if line_count == 0:
                                    line_count += 1
                                    continue
                                w2wdst_group[str(row[0])] = w2w.W2W(row[0], float(row[1]), float(row[2]),
                                                                    float(row[3]), float(row[4]),
                                                                    float(row[5]), float(row[6]), float(row[7]),
                                                                    float(row[8]), float(row[9]), float(row[10]),
                                                                    float(row[11]), float(row[12]), float(row[13]),
                                                                    float(row[14]), float(row[15]), float(row[16]),
                                                                    float(row[17]), float(row[18]))
                        weekly_scores = w2wdst_group[player_name].w2w_chart_calc()
                        weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
                        plt.plot(weeks, weekly_scores, color='blue')
                        plt.xlabel("Week")
                        plt.ylabel("Total PPR Points scored")
                        plt.title("2023 Weekly Cumulative Points Scored")
                        plt.xticks(weeks, weeks)
                        plt.ylim(0, 200)
                        plt.grid(axis='y', linestyle='--', color='gray')
                        plt.show()