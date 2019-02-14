I use pycharm to run this
To use youtube api, you need to have your own client_secret file, which is regiester by google account
The instruction is https://stackoverflow.com/questions/40136699/using-google-api-for-python-where-do-i-get-the-client-secrets-json-file-from
After creating app-install account, you can download the json file save it as client_secret file like what we have.
Steps:
getYoutubers.py -> youtubers_update.csv
datacleaning1.py -> youtubers_update_2.csv
getvideoinformation.py file - > files in list(dir) (the 192 line in getvideoinformation.py need to be set to your dir)
getfollowers.py -> youtbers_update_3.csv
FillViewScore.py - > youtubers_update_4.csv
dataclearning3.py -> youtubers_update_5.csv

Analysis:
DataAnalysis.py
DataAnalysis.py
regression.py

All theses generated csv file are in data_generated folder.
I remove them to there.