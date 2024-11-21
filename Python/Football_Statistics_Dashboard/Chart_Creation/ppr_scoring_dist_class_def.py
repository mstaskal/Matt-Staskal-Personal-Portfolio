"""
Name: Matt Staskal

The purpose of this program is to create class definitions that can be used to create player objects that are then used
to create matplotlib charts based on player statistics. This creates the Classes to be used in the scoring distribution chart.

"""

class QBDist:
    #self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self,rank,player_id,name,team,position,played,passing_completions,passing_attempts,passing_completion_percentage,passing_yards,points_from_passing_yards,pfpy_pct_total,passing_yards_per_attempt,passing_touchdowns,points_from_passing_tds,pfptd_pct_total,passing_interceptions,points_from_ints,pfint_pct_total,passing_rating,rushing_attempts,rushing_yards,points_from_ryds,pfry_pct_total,rushing_yards_per_attempt,rushing_touchdowns,points_from_rtds,pfrtd_pct_total,fantasy_points_pergameppr,fantasy_points_ppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.passing_completions = passing_completions
        self.passing_attempts = passing_attempts
        self.passing_completion_percentage = passing_completion_percentage
        self.passing_yards = passing_yards
        self.points_from_passing_yards = points_from_passing_yards
        self.pfpy_pct_total = pfpy_pct_total
        self.passing_yards_per_attempt = passing_yards_per_attempt
        self.passing_touchdowns = passing_touchdowns
        self.points_from_passing_tds = points_from_passing_tds
        self.pfptd_pct_total = pfptd_pct_total
        self.passing_interceptions = passing_interceptions
        self.points_from_ints = points_from_ints
        self.pfint_pct_total = pfint_pct_total
        self.passing_rating = passing_rating
        self.rushing_attempts = rushing_attempts
        self.rushing_yards = rushing_yards
        self.points_from_ryds = points_from_ryds
        self.pfry_pct_total = pfry_pct_total
        self.rushing_yards_per_attempt = rushing_yards_per_attempt
        self.rushing_touchdowns = rushing_touchdowns
        self.points_from_rtds = points_from_rtds
        self.pfrtd_pct_total = pfrtd_pct_total
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_ppr = fantasy_points_ppr


class RBDist:
    # self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self,rank,player_id,name,team,position,played,rushing_attempts,rushing_yards,points_from_rushing_yards,pfry_pct_total,rushing_yards_per_attempt,rushing_touchdowns,points_from_rushing_tds,pfrtd_pct_total,receiving_targets,receptions,points_from_rec,pfrec_pct_total,receiving_yards,points_from_recyds,pfrecy_pct_total,receiving_touchdowns,points_from_rectds,pfrectd_pct_total,fumbles,fumbles_lost,points_from_fumbles_lost,pffum_pct_total,fantasy_points_pergameppr,fantasy_points_ppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.rushing_attempts = rushing_attempts
        self.rushing_yards = rushing_yards
        self.points_from_rushing_yards = points_from_rushing_yards
        self.pfry_pct_total = pfry_pct_total
        self.rushing_yards_per_attempt = rushing_yards_per_attempt
        self.rushing_touchdowns = rushing_touchdowns
        self.points_from_rushing_tds = points_from_rushing_tds
        self.pfrtd_pct_total = pfrtd_pct_total
        self.receiving_targets = receiving_targets
        self.receptions = receptions
        self.points_from_rec = points_from_rec
        self.pfrec_pct_total = pfrec_pct_total
        self.receiving_yards = receiving_yards
        self.points_from_recyds = points_from_recyds
        self.pfrecy_pct_total = pfrecy_pct_total
        self.receiving_touchdowns = receiving_touchdowns
        self.points_from_rectds = points_from_rectds
        self.pfrectd_pct_total = pfrectd_pct_total
        self.fumbles = fumbles
        self.fumbles_lost = fumbles_lost
        self.points_from_fumbles_lost = points_from_fumbles_lost
        self.pffum_pct_total = pffum_pct_total
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_ppr = fantasy_points_ppr

class WRDist:
    # self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self, rank, player_id, name, team, position, played, receiving_targets, receptions, points_from_receptions, pfrec_pct_total, reception_percentage, receiving_yards, points_from_recyds, pfrecy_pct_total, receiving_touchdowns, points_from_rectds, pfrectd_pct_total, receiving_long, receiving_yds_per_target, receiving_yds_per_rec, rushing_attempts, rushing_yards, points_from_rushings_yards, pfry_pct_total, rushing_yards_per_attempt, rushing_touchdowns, points_from_rushing_tds, pfrtd_pct_total, fumbles, fumbles_lost, points_from_fumbles_lost, pffum_pct_total, fantasy_points_pergameppr, fantasy_points_ppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.receiving_targets = receiving_targets
        self.receptions = receptions
        self.points_from_receptions = points_from_receptions
        self.pfrec_pct_total = pfrec_pct_total
        self.reception_percentage = reception_percentage
        self.receiving_yards = receiving_yards
        self.points_from_recyds = points_from_recyds
        self.pfrecy_pct_total = pfrecy_pct_total
        self.receiving_touchdowns = receiving_touchdowns
        self.points_from_rectds = points_from_rectds
        self.pfrectd_pct_total = pfrectd_pct_total
        self.receiving_long = receiving_long
        self.receiving_yds_per_target = receiving_yds_per_target
        self.receiving_yds_per_rec = receiving_yds_per_rec
        self.rushing_attempts = rushing_attempts
        self.rushing_yards = rushing_yards
        self.points_from_rushings_yards = points_from_rushings_yards
        self.pfry_pct_total = pfry_pct_total
        self.rushing_yards_per_attempt = rushing_yards_per_attempt
        self.rushing_touchdowns = rushing_touchdowns
        self.points_from_rushing_tds = points_from_rushing_tds
        self.pfrtd_pct_total = pfrtd_pct_total
        self.fumbles = fumbles
        self.fumbles_lost = fumbles_lost
        self.points_from_fumbles_lost = points_from_fumbles_lost
        self.pffum_pct_total = pffum_pct_total
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_ppr = fantasy_points_ppr

class TEDist:
    # self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self, rank, player_id, name, team, position, played, receiving_targets, receptions, points_from_receptions, pfrec_pct_total, reception_percentage, receiving_yards, points_from_recyds, pfrecy_pct_total, receiving_touchdowns, points_from_rectds, pfrectd_pct_total, receiving_long, receiving_yds_per_target, receiving_yds_per_rec, rushing_attempts, rushing_yards, points_from_rushings_yards, pfry_pct_total, rushing_yards_per_attempt, rushing_touchdowns, points_from_rushing_tds, pfrtd_pct_total, fumbles, fumbles_lost, points_from_fumbles_lost, pffum_pct_total, fantasy_points_pergameppr, fantasy_points_ppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.receiving_targets = receiving_targets
        self.receptions = receptions
        self.points_from_receptions = points_from_receptions
        self.pfrec_pct_total = pfrec_pct_total
        self.reception_percentage = reception_percentage
        self.receiving_yards = receiving_yards
        self.points_from_recyds = points_from_recyds
        self.pfrecy_pct_total = pfrecy_pct_total
        self.receiving_touchdowns = receiving_touchdowns
        self.points_from_rectds = points_from_rectds
        self.pfrectd_pct_total = pfrectd_pct_total
        self.receiving_long = receiving_long
        self.receiving_yds_per_target = receiving_yds_per_target
        self.receiving_yds_per_rec = receiving_yds_per_rec
        self.rushing_attempts = rushing_attempts
        self.rushing_yards = rushing_yards
        self.points_from_rushings_yards = points_from_rushings_yards
        self.pfry_pct_total = pfry_pct_total
        self.rushing_yards_per_attempt = rushing_yards_per_attempt
        self.rushing_touchdowns = rushing_touchdowns
        self.points_from_rushing_tds = points_from_rushing_tds
        self.pfrtd_pct_total = pfrtd_pct_total
        self.fumbles = fumbles
        self.fumbles_lost = fumbles_lost
        self.points_from_fumbles_lost = points_from_fumbles_lost
        self.pffum_pct_total = pffum_pct_total
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
        self.fantasy_points_ppr = fantasy_points_ppr

class KDist:
    # self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self, rank,player_id,name,team,position,played,fg,close,points_close,close_pct_total,mid,points_mid,mid_pct_total,long,points_long,long_pct_total,xp,points_xp,xp_pct_total,fantasy_points_ppr,fantasy_points_pergameppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.fg = fg
        self.close = close
        self.points_close = points_close
        self.close_pct_total = close_pct_total
        self.mid = mid
        self.points_mid = points_mid
        self.mid_pct_total = mid_pct_total
        self.long = long
        self.points_long = points_long
        self.long_pct_total = long_pct_total
        self.xp = xp
        self.points_xp = points_xp
        self.xp_pct_total = xp_pct_total
        self.fantasy_points_ppr = fantasy_points_ppr
        self.fantasy_points_pergameppr = fantasy_points_pergameppr

class DSTDist:
    # self.pfpy_pct_total, self.pfptd_pct_total, etc. are "percent of the total points scored" from that category of scoring, and are used to create chart. Calculated in excel first.
    def __init__(self,rank,player_id,name,team,position,played,sacks,points_sacks,pfsac_pct_total,interceptions,points_ints,pfint_pct_total,fumbles_recovered,points_fum,pff_pct_total,safeties,points_safety,pfsaf_pct_total,def_td,points_dtd,pfdtd_pct_total,sp_td,points_sptd,pfsptd_pct_total,points_allowed,points_points_allowed,pfpa_pct_total,fantasy_points_ppr,fantasy_points_pergameppr):
        self.rank = rank
        self.player_id = player_id
        self.name = name
        self.team = team
        self.position = position
        self.played = played
        self.sacks = sacks
        self.points_sacks = points_sacks
        self.pfsac_pct_total = pfsac_pct_total
        self.interceptions = interceptions
        self.points_ints = points_ints
        self.pfint_pct_total = pfint_pct_total
        self.fumbles_recovered = fumbles_recovered
        self.points_fum = points_fum
        self.pff_pct_total = pff_pct_total
        self.safeties = safeties
        self.points_safety = points_safety
        self.pfsaf_pct_total = pfsaf_pct_total
        self.def_td = def_td
        self.points_dtd = points_dtd
        self.pfdtd_pct_total = pfdtd_pct_total
        self.sp_td = sp_td
        self.points_sptd = points_sptd
        self.pfsptd_pct_total = pfsptd_pct_total
        self.points_allowed = points_allowed
        self.points_points_allowed = points_points_allowed
        self.pfpa_pct_total = pfpa_pct_total
        self.fantasy_points_ppr = fantasy_points_ppr
        self.fantasy_points_pergameppr = fantasy_points_pergameppr
