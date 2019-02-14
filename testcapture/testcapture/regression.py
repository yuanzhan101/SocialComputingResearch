
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import seaborn as sns

data = pd.read_csv('youtubers_update_5.csv')
#arr = np.array(youtubeData)

Y = data['followers']
X = data['rateScore']


plt.scatter(X, Y, color='black')
plt.title('Test Data')
plt.xlabel('Rate score')
plt.ylabel('Followers')
plt.xticks(())
plt.yticks(())

plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, Y)
predictions = regr.predict(X)
plt.scatter(Y,predictions)
 

