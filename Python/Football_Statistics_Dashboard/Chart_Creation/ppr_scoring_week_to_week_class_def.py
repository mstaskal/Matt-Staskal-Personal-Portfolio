"""
Name: Matt Staskal

The purpose of this program is to create class definitions that can be used to create player objects that are then used
to create matplotlib charts based on player statistics. This creates the Classes to be used in the week to week cumulative scoring chart.
"""

class W2W:
    def __init__(self,name,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18):
        #w1,w2,w3 etc. are the scores for that week of play
        self.name = name
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
        self.w5 = w5
        self.w6 = w6
        self.w7 = w7
        self.w8 = w8
        self.w9 = w9
        self.w10 = w10
        self.w11 = w11
        self.w12 = w12
        self.w13 = w13
        self.w14 = w14
        self.w15 = w15
        self.w16 = w16
        self.w17 = w17
        self.w18 = w18

    def w2w_chart_calc(self):
        # Each player is instance of W2W class with self.name as reference. This combines all weeks and creates a list of running cumulative scores.
        # param self: player object instance of W2W class
        # :returns: a list of cumulative season scores after each week of the season
        # :raises: n/a
        self.weekly_cum_scores = []
        self.weekly_cum_scores.append(int(self.w1))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[0] + self.w2))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[1] + self.w3))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[2] + self.w4))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[3] + self.w5))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[4] + self.w6))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[5] + self.w7))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[6] + self.w8))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[7] + self.w9))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[8] + self.w10))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[9] + self.w11))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[10] + self.w12))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[11] + self.w13))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[12] + self.w14))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[13] + self.w15))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[14] + self.w16))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[15] + self.w17))
        self.weekly_cum_scores.append(int(self.weekly_cum_scores[16] + self.w18))
        return self.weekly_cum_scores
