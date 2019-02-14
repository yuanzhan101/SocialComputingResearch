import pandas as pd
import numpy as np


data = pd.read_csv("youtubers_update_3.csv")
all = []
def wilson_score_norm(mean, var, total, p_z=6.):
    score = (mean + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * var + np.square(p_z)))) / \
            (1 + np.square(p_z) / total)
    return score

def normal_value(data2):
    viewlist = np.array(data2.viewCount)
    max = np.max(viewlist)
    min = np.min(viewlist)
    norm_values = (viewlist - min) / (max - min)
    total = norm_values.size
    mean = np.mean(norm_values)
    var = np.var(norm_values)
    return total, mean, var

def wilson_score(pos, total, p_z=5.):
    pos_rat = pos * 1. / total * 1.
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score

count = 0
for index,row in data.iterrows():
    data1 = pd.read_csv("C:\\Users\\yzhan101\\PycharmProjects\\testcapture\\list\\" + str(index) + ".csv")
    matrix = data1.as_matrix()
    viewScore = ''
    rateScore = ''
    if str(matrix[0][0]) == str(row['name']):
        total, mean, var = normal_value(data1)
        viewScore = wilson_score_norm(mean=mean, var=var, total=total)
        rateScoreList = []
        for i, row1 in data1.iterrows():
            goodrate = row1['likeCount']
            badrate = row1['dislikeCount']
            total = badrate+goodrate
            v = 0
            if total == 0:
                v = 0
            else:
                v = wilson_score(goodrate, badrate+goodrate)
            rateScoreList.append(v)

        rateScore = np.average(rateScoreList)
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
        object.append(viewScore)
        object.append(rateScore)
        all.append(object)
        print count
        count = count + 1

file = "youtubers_update_4.csv"
data1 = pd.DataFrame(all)
data1.columns = ['name', 'url', 'uploads', 'subsribers', 'views', 'country', 'channeltype', 'facebooklink', 'twitterlink', 'followers', 'viewScore', 'rateScore']
data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')









