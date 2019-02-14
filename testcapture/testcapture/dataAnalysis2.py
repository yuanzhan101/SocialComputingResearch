import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt


n = 200
data = pd.read_csv("youtubers_update_5.csv")
newList4 = data[['rateScore', 'followers']].copy()
estimator = KMeans(n_clusters=n)
res = estimator.fit_predict(newList4)
lable_pred = estimator.labels_
centroids = estimator.cluster_centers_
inertia = estimator.inertia_

folllower_list = np.array(data.followers)
viewScore_list = np.array(data.viewScore)
rateScore_list = np.array(data.rateScore)
r1 = np.quantile(rateScore_list, .25)
r2 = np.quantile(rateScore_list, .5)
r3 = np.quantile(rateScore_list, .75)

all_r1 = [];
all_r2 = [];
all_r3 = [];
all_r4 = [];

for row in centroids:
    if row[0] <= r1:
        all_r1.append(row)
    if (row[0] > r1) & (row[0] <= r2):
        all_r2.append(row)
    if (row[0] > r2) & (row[0] <= r3):
        all_r3.append(row)
    else:
        all_r4.append(row)

all_r1_length = len(all_r1)
all_r2_length = len(all_r2)
all_r3_length = len(all_r3)
all_r4_length = len(all_r4)

print "I cluster the data set into " + str(n) + " groups"


f1 = np.quantile(folllower_list, .25)
f2 = np.quantile(folllower_list, .5)
f3 = np.quantile(folllower_list, .75)

count_r1 = 0
for row in all_r1:
    if row[1] < f3:
        count_r1 = count_r1 + 1

count_r2 = 0
for row in all_r2:
    if (row[1] > f1) & (row[1] <= f2):
        count_r2 = count_r2 + 1

count_r3 = 0
for row in all_r3:
    if (row[1] > f2) & (row[1] <= f3):
        count_r3 = count_r3 + 1

count_r4 = 0
for row in all_r4:
    if row[1] > f3:
        count_r4 = count_r4 + 1


if all_r1_length == 0:
    percent1 = 0
else:
    percent1 =  int(count_r1/float(all_r1_length) * 100)

if all_r2_length == 0:
    percent2 = 0
else:
    percent2 = int(count_r2 / float(all_r2_length) * 100)

if all_r3_length == 0:
    percent3 = 0
else:
    percent3 = int(count_r3/float(all_r3_length) * 100)

if all_r4_length == 0:
    percent4 = 0
else:
    percent4 = int(count_r4/float(all_r4_length) * 100)


print "there are " + str(all_r1_length) + " clusters in 0-25% of rateScore, " +  str(percent1) + "% in 0-25% of number of followers"
print "there are " + str(all_r2_length) + " clusters in 25-50% of rateScore, " +  str(percent2) + "% in 25-50% of number of followers"
print "there are " + str(all_r3_length) + " clusters in 50-75% of rateScore, " +  str(percent3) + "% in 50-75% of number of followers"
print "there are " + str(all_r4_length) + " clusters in 75-100% of rateScore, " +  str(percent4) + "% in 75-100% of number of followers"

