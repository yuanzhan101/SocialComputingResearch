import pandas as pd
# -*- coding: utf-8 -*-

data = pd.read_csv("youtubers_update_1.csv")
count = 0
all = []
for index,row in data.iterrows():
    views = row['views']
    # print views
    if views != '0.0':
        all.append(row)

file = "youtubers_update_2.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')