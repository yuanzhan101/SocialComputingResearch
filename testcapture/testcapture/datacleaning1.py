import urllib2
import re
from bs4 import BeautifulSoup
import pandas as pd
# -*- coding: utf-8 -*-

data = pd.read_csv("youtubers_update.csv")
count = 0
all = []
for index,row in data.iterrows():
    str1 = row['twitterlink']
    str1 = str(str1)
    if re.match("https://twitter.com/(.*)", str1):
        all.append(row)

file = "youtubers_update_1.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')


