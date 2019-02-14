import sys
import csv
import pandas as pd
import numpy as np

"""
  This programs reads the input file containing all the datasets for youtube and Twitter with their 
  Then calculates the 25% of the popularity based on maximum view score, rate score and max followers.
  And then see if there is any commonality/commonalities between those groups (youtube & Twitter).
  @author Prem Subedi
"""
def main():
    analysis()

def analysis():
    data = pd.read_csv("youtubers_update_5.csv")
    dArray = np.array(data)
    maxTwitter =  np.max(data.followers)
    top25Twitter = maxTwitter - 0.25 * maxTwitter
    maxYtuber1 = np.max(data.viewScore)
    top25Ytber1 = maxYtuber1 - 0.25 * maxYtuber1

    maxYtuber2 = np.max(data.rateScore)
    top25Ytber2 = maxYtuber2 - 0.25 * maxYtuber2
    ytPopulous = []
    twPopulous = []
    for userInfo in dArray:
        if(userInfo[10] <= maxYtuber1 and userInfo[10] >= top25Ytber1):
            ytPopulous.append(userInfo[0])

        if(userInfo[11] <= maxYtuber2 and userInfo[11] >= top25Ytber2 ):
            ytPopulous.append(userInfo[0])
        if(userInfo[9] <= maxTwitter and userInfo[9] >= top25Twitter):
            twPopulous.append(userInfo[0])

    for twitterUser in twPopulous:
        if twitterUser in ytPopulous:
            print "True"
            print "Hence the user who is popular in Youtube has most followers in Twitter as well."
            break
        else:
            print "False"

if __name__ == "__main__":
    main()
