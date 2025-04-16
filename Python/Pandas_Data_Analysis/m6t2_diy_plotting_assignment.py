"""
* Name         : m6t2_diy_plotting_assignment.py
* Author       : Matt Staskal
* Created      : 02/12/25
* Module       : 6
* Topic        : 2
* Description  : Create 2 visualizations of a dataset of choice
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
home_prices = pd.read_csv('data_zillow_house_prices.csv')

#create a simple visual from your dataset using matplotlib
#explain what your visual demontrates
print("Data gathered from: https://www.kaggle.com/datasets/luisheitorribeiro/historical-house-prices-across-u-s-regions")
print("Monthly median home prices from January 2000 to August 2022 grouped by 893 metropolitan statistical areas\n")
print("Create a simple visual from your dataset using matplotlib")
print("Explain what your first visual demonstrates:")
print("\tThis visual demonstrates the change in Median Home Price (mhp) from January 2000 to August 2022 in Des Moines, IA")
print("\tmhp ranges from $126,044 on 1/31/2000 to $268,384 on 8/31/2022\n")


dsm_ia = home_prices[home_prices.RegionName == 'Des Moines, IA']
dsm_ia_prices = dsm_ia.drop(columns=['RegionID','SizeRank','RegionName','RegionType','StateName'])
dsm_ia_prices = dsm_ia_prices.transpose()
dsm_ia_prices.reset_index(inplace=True)
dsm_ia_prices.columns = ['date','median_price']

plt.plot(dsm_ia_prices['date'],dsm_ia_prices['median_price'])
plt.xticks(np.arange(0,278,9),rotation=45,fontsize=5)
plt.yticks(fontsize=8)
plt.title("Median Home Price in Des Moines, IA 1/31/2000 - 8/31/2022",fontsize=8)
plt.show()

#create a more complex visual from your dataset using matplotlib including multiple options like color, line weight
#explain what your 2nd visual demontrates and why it required a more complex visual
print("Create a more complex visual from your dataset using matplotlib including multiple options like color, line weight")
print("Explain what your 2nd visual demonstrates and why it required a more complex visual:")
print("\tThis visual demonstrates the change in mhp from January 2000 to August 2022 in the 6 largest msa's in the US, along with US median")
print("\tIt required a more complex visual to be able to clearly display and label the different regions, and make it easy draw conclusions from the visual")
print("\tFor example, mhp in Chicago, IL fell below median US mhp in 2018, while mhp in Dallas, TX went over US mhp in 2016")

usa_top_6 = home_prices.iloc[:7, 2:]
usa_top_6 = usa_top_6.drop(['RegionType', 'StateName'], axis=1)
usa_top_6.reset_index(drop=True, inplace=True)

usa_top_6_tp = usa_top_6.transpose()
usa_top_6_tp.reset_index(inplace=True)
usa_top_6_tp.rename(columns={
    "index": "Date",
    0: "United_States",
    1: "New_York_NY",
    2: "Los_Angeles_CA",
    3: "Chicago_IL",
    4: "Dallas_TX",
    5: "Houston_TX",
    6: "Washington_DC",
    }, inplace=True)

usa_top_6_tp_final = usa_top_6_tp.drop([usa_top_6_tp.index[0]]).reset_index(drop=True)
print(usa_top_6_tp_final.head())

plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['United_States'], c='black', label="USA_Median", lw=1, ls='--')
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['New_York_NY'], c='yellow', label="New_York_NY_1", lw=.85)
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['Los_Angeles_CA'], c='indigo', label="Los_Angeles_CA_2", lw=.85)
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['Chicago_IL'], c='grey', label="Chicago_IL_3", lw=.85)
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['Dallas_TX'], c='magenta', label="Dallas_TX_4", lw=.85)
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['Houston_TX'], c='limegreen', label="Houston_TX_5", lw=.85)
plt.plot(usa_top_6_tp_final['Date'], usa_top_6_tp_final['Washington_DC'], c='red', label="Washington_DC_6", lw=.85)
plt.xticks(np.arange(0, 278, 9), rotation=45, fontsize=6)
plt.yticks(fontsize=7)
plt.title("Median Home Price in 6 largest US Cities 1/31/2000 - 8/31/2022", fontsize=11)
plt.xlabel('Date', fontsize=9)
plt.ylabel('Median Home Price', fontsize=9)
plt.legend(title='Number next to city indicates population rank',fontsize='x-small',title_fontsize='small',alignment='left',facecolor='cyan')
plt.grid(axis='y', ls='--', lw=.5)
plt.gca().set_facecolor('floralwhite')
plt.show()