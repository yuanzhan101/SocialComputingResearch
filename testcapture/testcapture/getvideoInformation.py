import urllib2
import re
from bs4 import BeautifulSoup
import pandas as pd
import os
# -*- coding: utf-8 -*-

# data = pd.read_csv("youtubers_update1.csv")
# for index,row in data.iterrows():
#     name = row['name']
#     youtubelink = row['youtubelink']
#     youtubelink = str(youtubelink)
#     match = re.match('https://youtube.com/channel/(.*)', youtubelink)
#     id = match.group(1)
#     all = []
#     all.append(name)
#     print name
#     name1 = name.decode("utf-8-sig", "ignore")
#     file = "C:\\Users\\yzhan101\\PycharmProjects\\testcapture\\list\\" + name1 + ".csv"
#     data1 = pd.DataFrame(all)
#     data1.columns = ['name']
#     data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')


import json

import google.oauth2.credentials

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def print_response(response):
    print(response)


# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
    resource = {}
    for p in properties:
        # Given a key like "snippet.title", split into "snippet" and "title", where
        # "snippet" will be an object and "title" will be a property in that object.
        prop_array = p.split('.')
        ref = resource
        for pa in range(0, len(prop_array)):
            is_array = False
            key = prop_array[pa]

            # For properties that have array values, convert a name like
            # "snippet.tags[]" to snippet.tags, and set a flag to handle
            # the value as an array.
            if key[-2:] == '[]':
                key = key[0:len(key) - 2:]
                is_array = True

            if pa == (len(prop_array) - 1):
                # Leave properties without values out of inserted resource.
                if properties[p]:
                    if is_array:
                        ref[key] = properties[p].split(',')
                    else:
                        ref[key] = properties[p]
            elif key not in ref:
                # For example, the property is "snippet.title", but the resource does
                # not yet have a "snippet" object. Create the snippet object here.
                # Setting "ref = ref[key]" means that in the next time through the
                # "for pa in range ..." loop, we will be setting a property in the
                # resource's "snippet" object.
                ref[key] = {}
                ref = ref[key]
            else:
                # For example, the property is "snippet.description", and the resource
                # already has a "snippet" object.
                ref = ref[key]
    return resource


# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            if value:
                good_kwargs[key] = value
    return good_kwargs


def channels_list_by_id(client, **kwargs):
    # See full sample for function
    kwargs = remove_empty_kwargs(**kwargs)

    response = client.channels().list(
        **kwargs
    ).execute()

    return response

def playlist_items_list_by_playlist_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().list(
    **kwargs
  ).execute()

  return response

def videos_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.videos().list(
    **kwargs
  ).execute()

  return response


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    client = get_authenticated_service()

    data = pd.read_csv("youtubers_update_2.csv")
    count = 0
    for index,row in data.iterrows():
        name = row['name']
        facebooklink = row['facebooklink']
        facebooklink = str(facebooklink)
        match = re.match('https://youtube.com/channel/(.*)', facebooklink)
        id1 = match.group(1)
        all = []

        channel_list = channels_list_by_id(client,
                                           part='snippet,contentDetails,statistics',
                                           id=id1)


        channel_list = channel_list['items'][0]

        playlist_Id = channel_list['contentDetails']['relatedPlaylists']['uploads']
        play_list = playlist_items_list_by_playlist_id(client,
                                                       part='snippet,contentDetails',
                                                       maxResults=50,
                                                       playlistId=playlist_Id)
        play_list = play_list['items']
        for item in play_list:
            video_id = item['contentDetails']['videoId']
            video = videos_list_by_id(client,
                                      part='snippet,contentDetails,statistics',
                                      id=video_id)
            video = video['items'][0]
            title = video['snippet']['title']
            statistics = video['statistics']
            viewCount = ''
            likeCount = ''
            dislikeCount = ''
            favoriteCount = ''
            commentCount = ''
            if len(statistics) == 5:
                viewCount = statistics['viewCount']
                likeCount = statistics['likeCount']
                dislikeCount = statistics['dislikeCount']
                favoriteCount = statistics['favoriteCount']
                commentCount = statistics['commentCount']
                obj = [name, title, viewCount, likeCount, dislikeCount, favoriteCount, commentCount]
                all.append(obj)
            else:
                continue

        file = "C:\\Users\\yzhan101\\PycharmProjects\\testcapture\\list1\\" + str(index) + ".csv"
        data1 = pd.DataFrame(all)
        data1.columns = ['name', 'title', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount']
        data1.to_csv(file, index=False, mode='a+', encoding='utf-8-sig')
        count = count + 1
        print count





