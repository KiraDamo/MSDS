#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 7
DSC 450
@author: Kira Damo

"""
import pandas as pd
import numpy as np
import random

#Question 1

def random_num_list(n):
    '''This function takes n and creates a list of random numbers
    that is n length and all elements are integers that fall between
    44 and 100'''
    num_list = []
    for i in range(n):
        num = np.random.randint(44, 100)
        num_list.append(num)
    return num_list

#inserts 90 for n
nums = random_num_list(90)
print(nums)

series = pd.Series(nums)

#counts all elements that are below 54
count_under_54 = len(series[series < 54])
print(count_under_54)

#reshaping array
array = np.array(nums)
array = np.reshape(array, (9, 10))
#replacing values greater than or equal to 59 by 100
array[array >= 59] = 100

print(array)

#Question 2

import sqlite3
import json
import urllib.request

conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Tweet')
tweet_tbl = '''CREATE TABLE IF NOT EXISTS Tweet(
    id INT PRIMARY KEY,
    created_at TEXT,
    id_str TEXT,
    text TEXT,s
    ource TEXT,
    in_reply_to_user_id INT,
    in_reply_to_screen_name TEXT,
    in_reply_to_status_id INT,
    retweet_count INT,
    Contributors TEXT
    );'''

cursor.execute('DROP TABLE IF EXISTS User')
user_tbl = '''CREATE TABLE IF NOT EXISTS User(
    id INT PRIMARY KEY,
    name TEXT,
    screen_name TEXT,
    description TEXT,
    friends_count INT
 );'''

cursor.execute(tweet_tbl)
cursor.execute(user_tbl)

twitter_data_url = 'https://dbgroup.cdm.depaul.edu/DSC450/Module7.txt'

webFD = urllib.request.urlopen(twitter_data_url)
raw_tweets = webFD.read().decode('utf-8')

tweets = raw_tweets.strip().split('EndOfTweet')

user_insert = '''INSERT INTO User (name, screen_name, description, friends_count)VALUES (?, ?, ?, ?)'''
tweet_insert = '''INSERT INTO User (name, screen_name, description, friends_count)VALUES (?, ?, ?, ?)'''

with open('tweet_errors.txt', 'w', encoding='utf-8') as errors:
    for tweet in tweets:
        try:
            tdict = json.loads(tweet)
            user_data = [
                tdict['user']['name'],
                tdict['user']['screen_name'],
                tdict['user']['description'],
                tdict['user']['friends_count']
            ]
            user_data = [value if value != '' else None for value in user_data]
            cursor.execute(user_insert, user_data)
            tweet_data = [
                tdict['created_at'],
                tdict['id_str'],
                tdict['text'],
                tdict['source'],
                tdict.get('in_reply_to_user_id'),
                tdict.get('in_reply_to_screen_name'),
                tdict.get('in_reply_to_status_id'),
                tdict.get('retweet_count'),
                tdict.get('contributors')
            ]
            tweet_data = [value if value != '' else None for value in tweet_data]
            cursor.execute(tweet_insert, tweet_data)
        except ValueError:
            errors.write(tweet + 'EndOfTweet')
        

