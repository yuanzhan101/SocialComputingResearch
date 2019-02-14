# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib2
import re
import pandas as pd

def my_function(name, url):
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'lxml')
    span = soup.find("span", id = "youtube-stats-header-uploads")
    span = str(span)
    match = re.search('<span id=(.*)>(.*)</span>', span)
    if match is None:
        uploads = ''
    else:
        uploads = match.group(2)
    span = soup.find("span", id = "youtube-stats-header-subs")
    span = str(span)
    match = re.search('<span id=(.*)>(.*)</span>', span)
    if match is None:
        subs = ''
    else:
        subs = match.group(2)
    span = soup.find("span", id = "youtube-stats-header-views")
    span = str(span)
    match = re.search('<span id=(.*)>(.*)</span>', span)

    if match is None:
        views = ''
    else:
        views = match.group(2)

    span = soup.find("span", id = "youtube-stats-header-country")
    span = str(span)
    match = re.search('<span id=(.*)>(.*)</span>', span)
    if match is None:
        country = ''
    else:
        country = match.group(2)

    span = soup.find("span", id = "youtube-stats-header-channeltype")
    span = str(span)
    match = re.search('<span id=(.*)>(.*)</span>', span)
    if match is None:
        channeltype = ''
    else:
        channeltype = match.group(2)

    a = soup.find("a", {"class": "core-button -margin core-small-wide ui-black"})
    a = str(a)
    match = re.search('<a class=(.*) href="(.*)" rel=(.*)>(.*)', a)
    if match is None:
        facebooklink = ''
    else:
        facebooklink = match.group(2)

    twitterlink = ''
    a = soup.findAll("a", {"class": "core-button core-small-wide ui-black"})
    if a is None:
        twitterlink = ''
    else:
        for l in a:
            l = str(l)
            if re.search('<a class=(.*) href="(.*)" rel=(.*)>\n<i class="fa fa-twitter" style="color:#fff;"></i>\n</a>', l):
                match = re.search('<a class=(.*) href="(.*)" rel=(.*)>\n<i class="fa fa-twitter" style="color:#fff;"></i>\n</a>', l)
                twitterlink = match.group(2)
    obj = [name, url, uploads, subs, views, country, channeltype, facebooklink, twitterlink]
    all.append(obj)

# my_function("vsd", 'https://socialblade.com/youtube/c/ed-sheeran')

data = pd.read_csv("youtubers.csv")
all = []
count = 0
for index,row in data.iterrows():
    print count
    name = row['name']
    url = row['url']
    link = str(url)
    r = requests.get(link)
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page, 'lxml')
    mydivs = soup.findAll("span", {"class": "YouTubeUserTopLight"})
    # print soup
    if len(mydivs) == 0:
        t1 = soup.findAll('h2', attrs={'style': 'float: left;'})
        t2 = str(t1[0])
        if re.match('(.*)<a href="(.*)" style=(.*)>(.*)</a>(.*)', t2):
            result = re.search('(.*)<a href="(.*)" style=(.*)>(.*)</a>(.*)', t2)
            url = "https://socialblade.com" + result.group(2)
            name = result.group(4)

    my_function(name, url)
    count = count + 1
    print url

file = "youtubers_update.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')

