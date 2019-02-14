import pandas as pd

data = pd.read_csv("youtubers_update_4.csv")
all = []
for index,row in data.iterrows():
    a = str(row['followers'])
    if a != 'nan':
        object = []
        object.append(row['name'])
        object.append(row['url'])
        object.append(row['uploads'])
        object.append(row['subsribers'])
        object.append(row['views'])
        object.append(row['country'])
        object.append(row['channeltype'])
        object.append(row['facebooklink'])
        object.append(row['twitterlink'])
        object.append(row['followers'])
        object.append(row['viewScore'])
        object.append(row['rateScore'])
        all.append(object)


file = "youtubers_update_5.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink', 'followers', 'viewScore', 'rateScore']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')