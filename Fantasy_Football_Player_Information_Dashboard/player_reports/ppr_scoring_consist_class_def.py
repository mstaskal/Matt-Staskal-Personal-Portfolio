"""
Name: Matt Staskal
Class: CIS 189
Module: Final project
Topic: Fantasy football player dashboard - Consistency report class definitions
The purpose of this program is to create class definitions that can be used to create player objects that are then used
to create matplotlib charts based on player statistics. This creates the Classes to be used in the consistency chart.
"""

class QBConsist:
    #fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev

class RBConsist:
    # fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev

class WRConsist:
    # fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev

class TEConsist:
    # fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev

class KConsist:
    # fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev

class DSTConsist:
    # fantasy points per game and st dev of fantasy points per game have been calculated in excel first
    def __init__(self,rank,name,team,position,played,fantasy_points_pergameppr,fantasy_points_pergameppr_stdev):
        self.rank = rank
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_pergameppr_stdev = fantasy_points_pergameppr_stdev