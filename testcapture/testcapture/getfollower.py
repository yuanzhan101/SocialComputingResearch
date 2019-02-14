import urllib2
import re
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_csv("youtubers_update_2.csv")
all = []
count = 0
for index,row in data.iterrows():
    twitterlink = row['twitterlink']
    twitterlink = str(twitterlink)

    try:
        header = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(twitterlink, headers=header)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page, 'lxml')
        follow_list = soup.findAll('a', class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor")
        i = 0
        followers = ''
        while i < len(follow_list):
            t1 = str(follow_list[i])
            r1 = re.match('<a class=(.*) title="(.*) Followers"(.*)',t1)
            if not r1 is None:
                r1 = r1.group(2)
                followers = r1.replace(',', '')
                break
            i = i + 1


        object = [];
        object.append(row['name'])
        object.append(row['url'])
        object.append(row['uploads'])
        object.append(row['subsribers'])
        object.append(row['country'])
        object.append(row['views'])
        object.append(row['channeltype'])
        object.append(row['facebooklink'])
        object.append(row['twitterlink'])
        object.append(followers)

        all.append(object)
    except Exception, e:
        object = [];
        object.append(row['name'])
        object.append(row['url'])
        object.append(row['uploads'])
        object.append(row['subsribers'])
        object.append(row['country'])
        object.append(row['views'])
        object.append(row['channeltype'])
        object.append(row['facebooklink'])
        object.append(row['twitterlink'])
        object.append('')
        all.append(object)
        continue
    print count
    count = count + 1

file = "youtubers_update_3.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink', 'followers']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')

